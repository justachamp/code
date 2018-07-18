# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import logging
import urllib
from functools import wraps
from datetime import datetime
from urlparse import urlparse

from django.conf import settings
from django.core.signing import BadSignature
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseBadRequest, QueryDict
from django.http.response import Http404
from django.views.decorators.http import require_POST, require_http_methods, require_GET

from ipware.ip import get_real_ip
from celery.utils.iso8601 import parse_iso8601

from addnow.apps.accounts import constants
from addnow.apps.accounts.models import Site
from addnow.apps.tracker.channels import ServiceFactory
from addnow.apps.tracker.forms import SendEmailForm
from addnow.apps.tracker.models.collections import OutsideShares
from addnow.apps.tracker.tasks import add_hook, track_event as track_event_task, \
    save_external_shares as save_external_shares_task
# from addnow.apps.accounts.emails import trim_fail_email
from addnow.apps.tracker.trim import TrimService
from addnow.apps.tracker.utils import create_uuid
from addnow.apps.tracker.exceptions import TrimAPIException, BadTrimKeyException, ValidationFailedException
from addnow.cache import SiteSettingsCache, SocialCountersCache, SiteTrimSettingsCache, TrimFailCache


logger = logging.getLogger(__name__)

TRIM_FAIL_TIMEOUT = 30 * 60  # 30 minutes


def inject_site_id(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        site_id = request.GET.get('idsite')

        if not site_id:
            return JsonResponse({'message': 'Missing site id'}, status=400)

        try:
            site_id = Site.get_id_by_hash(site_id)
        except BadSignature:
            return JsonResponse({'message': 'Invalid site id'}, status=400)

        return view_func(request, site_id, *args, **kwargs)

    return wrapper


@inject_site_id
def track_event(request, site_id):
    """
    Main tracker endpoint
    """
    now = datetime.utcnow()

    real_ip = get_real_ip(request)
    headers = {}
    for k, v in request.META.items():
        if k.startswith('HTTP') or k == 'REMOTE_ADDR':
            if not isinstance(v, unicode):
                v = v.decode('utf-8')
            headers[k] = v
    try:
        track_event_task.delay(site_id, now, request.GET, headers, real_ip=real_ip)
    except IOError as e:
        logger.error('I/O error({0}): {1}'.format(e.errno, e.strerror))
        return JsonResponse({'code': e.errno, 'message': e.strerror}, status=500)

    return HttpResponse(status=204)


@inject_site_id
def site_settings(request, site_id):
    try:
        config = SiteSettingsCache.get_config(site_id)
    except Http404:
        return JsonResponse({'message': 'Site settings not found'}, status=400)
    del config['offset']
    config['uuid'] = create_uuid()
    return JsonResponse(config)


@require_POST
def click(request, site_id=None, tool=None):
    """
    2014-09-21T20:50:54
    Addnow post-click hook
    https://confluence.gravity4.com/display/AN/AddNow+-+Tr.im+integration

    POST, JSON payload
    shortcut    string	    Shortcut of the URL. (required)
    long_url	string	    The original URL that the user was redirected to. (required)
    clicked_at	datetime	The date and time of the click event.
    This will be important if the post-click hook is delayed for whatever reason. (required)
    """
    headers = {}
    query = {}
    real_ip = None
    service = request.GET.get('service')
    uuid = request.GET.get('uuid')
    title = request.GET.get('title')

    logger.info('click hook fired for site id %s (tool: %s, service: %s, uuid: %s) %s',
                site_id, tool, service, uuid, request.body)

    try:
        data = json.loads(request.body)
    except ValueError:
        logger.exception('json decode error')
        return HttpResponseBadRequest()

    url, clicked_at = data['long_url'], parse_iso8601(data['clicked_at'])
    if not (site_id and tool and url):
        logger.error('bad request', extra=locals())
        return HttpResponseBadRequest()

    try:
        site_id = int(Site.get_id_by_hash(site_id))
    except BadSignature:
        logger.exception("site_id can't be converted to int: %s", repr(site_id))
        return HttpResponseBadRequest()

    query['e_c'] = constants.Events.CLICK.value
    query['e_n'] = url
    query['e_t'] = tool
    query['e_a'] = service or constants.SOURCE_DARK_SOCIAL
    if uuid:
        query['e_u'] = uuid
    if title:
        query['e_i'] = urllib.unquote_plus(title)
    if 'referrer_host' in data:
        headers['HTTP_REFERER'] = data['referrer_host']
    if 'ip' in data:
        real_ip = data['ip']
    track_event_task.delay(site_id, clicked_at, query, headers=headers, real_ip=real_ip)

    return HttpResponse(status=204)


@require_POST
def create_shortlink(request):
    # IE9 uses XDomainRequest that don't set CONTENT_TYPE header
    if request.META.get('CONTENT_TYPE'):
        data = request.POST
    else:
        data = QueryDict(request.body)
    long_url, site_id, tool = data['original_url'], data['site_id'], data['tool']
    service = data.get('service')
    uuid = data.get('uuid')
    title = data.get('title')
    vanity_domain = data.get('vanity_domain')
    trim_api_key = None

    if site_id:
        try:
            site_id = Site.get_id_by_hash(site_id)
        except BadSignature:
            logger.exception("site_id can't be converted to int: %s", repr(site_id))
            return HttpResponseBadRequest()

    try:
        assert bool(long_url) and bool(tool)
    except (AssertionError, ValueError):
        logger.error('bad short link request', extra=locals())
        return HttpResponseBadRequest()
    if vanity_domain:
        try:
            trim_api_key = SiteTrimSettingsCache.get_key(site_id)
        except Http404:
            logger.exception("trim key for site with id %s doesn't exist: ", repr(site_id))
            return HttpResponseBadRequest()
    short_url = create_shortcut_and_add_hook(
        trim_api_key, vanity_domain, request,
        long_url, site_id, tool, service, title, uuid
    )
    return JsonResponse(dict(short_url=short_url))


# todo: cache
def send_email(request):

    # todo: move to js/html
    url = request.GET.get('url') or ''
    text = request.GET.get('text') or 'Read this interesting article'
    frontend_base_url = urlparse(settings.FRONTEND_BASE_URL)

    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            form.send_email()
            return render(request, 'tracker/email_sent.html', {'frontend_url': frontend_base_url.netloc})
    else:
        form = SendEmailForm()
    context = {'form': form, 'url': url, 'text': text, 'frontend_url': frontend_base_url.netloc}

    return render(request, 'tracker/email_form.html', context)


@require_http_methods(['POST', 'PATCH'])
def counters(request, site_id=None):
    """
    Endpoint handling counters

    It handles 2 methods

    * Getting cached results is done via POST method:

    POST /counters/site_id

        data: ['http://www.chahal.com/',
               'http://www.chahal.com/never-let-your-memories-be-greater-than-your-dreams',
               'http://www.hasthelargehadroncolliderdestroyedtheworldyet.com/']

    * Updating cached results is done via PATCH method

    PATCH /counters/site_id

        data: {
            'http://www.chahal.com/': {
                'pinterest': 88,
                'googlePlus': 56
            },
            'http://www.chahal.com/never-let-your-memories-be-greater-than-your-dreams': {
                'twitter': 44,
                'pinterest': 32
            }
        }

    """
    if site_id:
        try:
            site_id = Site.get_id_by_hash(site_id)
        except BadSignature:
            logger.exception("site_id can't be converted to int: %s", repr(site_id))
            return HttpResponseBadRequest()

    if request.method == 'POST':
        data = {}
        for url in request.POST.values():
            cache_key = dict(site_id=site_id, url=url)
            social_counters = SocialCountersCache.get(cache_key)
            if social_counters is None:
                social_counters = {}
                docs = OutsideShares().find({'site': int(site_id), 'url': url})
                for doc in docs:
                    social_counters[doc['source']] = doc['shares']
                SocialCountersCache.set(cache_key, social_counters, timeout=settings.COUNTERS_CACHE_TIMEOUT)
                data[url] = social_counters
        return JsonResponse(data)

    elif request.method == 'PATCH':
        request_data = json.loads(request.body)
        for url in request_data:
            save_external_shares_task.delay(site_id, url, **request_data[url])
        return JsonResponse(request_data)


@require_GET
def vanity_domains(request):
    trim_api_key = request.GET.get('trim_api_key')
    trim_service = TrimService(trim_api_key)
    try:
        domains = trim_service.get_vanity_domains()
        return JsonResponse(dict(vanity_domains=domains))
    except BadTrimKeyException as exc:
        return JsonResponse({'errors': [str(exc)]}, status=400)


@require_GET
def share(request, channel):
    """
    2015-04-21
    Addnow Non Javascript share-click

    https://jira.gravity4.com/browse/ADDNOW-208

    """

    service_factory = ServiceFactory()

    try:
        service = service_factory.get_service(channel)
    except KeyError:
        logger.exception('Unknown/unsupported service: %s', channel)
        return HttpResponseBadRequest('Unknown/unsupported service')

    clicked_at = datetime.utcnow()
    site_id = request.GET.get('site_id')

    if site_id:
        try:
            site_id = Site.get_id_by_hash(site_id)
        except BadSignature:
            logger.error('bad request', extra=locals())
            return HttpResponseBadRequest()

    try:
        trim_api_key = SiteTrimSettingsCache.get_key(site_id)
    except Http404:
        logger.exception("trim api key for site with id %s doesn't exist: ", repr(site_id))
        return HttpResponseBadRequest()

    url = request.GET.get('url')
    message = request.GET.get('message')
    title = request.GET.get('title')
    media_url = request.GET.get('media_url')
    vanity_domain = request.GET.get('vanity_domain')
    tool = request.GET.get('tool', constants.Tools.NEWSLETTER_SHARING_BUTTONS.value)

    if service.should_short_url:
        short_url = create_shortcut_and_add_hook(
            trim_api_key, vanity_domain, request, url, site_id,
            tool,
            channel, title, None
        )
    else:
        short_url = url

    logger.info('share hook fired %s newsletter (service: %s) %s', site_id, service, request.body)

    redirect_to = service.get_redirect_url(url=short_url, title=message, media_url=media_url)

    event = {}

    if url:
        event['e_a'] = channel
        event['e_c'] = constants.Events.SHARE.value
        event['e_n'] = url
        event['e_t'] = tool
    else:
        logger.error('bad request', extra={key: value for key, value in locals().items()
                                           if key != 'message'})
        return HttpResponseBadRequest()

    track_event_task.delay(site_id, clicked_at, event, {})

    return HttpResponseRedirect(redirect_to=redirect_to)


# Utils
def get_hook(request, site_id, tool, service, uuid, title):
    hook_path = reverse('tracker_click_hook', urlconf='addnow.urls.tracker', args=[int(site_id), tool])
    query = {}

    if service:
        query['service'] = service
    if uuid:
        query['uuid'] = uuid
    if title:
        if isinstance(title, unicode):
            title = title.encode('utf-8')
        query['title'] = urllib.quote_plus(title)
    if query:
        hook_path = '%s?%s' % (hook_path, urllib.urlencode(query))

    return request.build_absolute_uri(hook_path)


def get_shortcut_and_add_hook(trim_api_key, vanity_domain, request, long_url,
                              site_id, tool, service, title, uuid):
    trim_service = TrimService(trim_api_key)
    shortcut, short_url = trim_service.create_shortcut(long_url, site_id, tool, service, vanity_domain)
    hook = get_hook(request, site_id, tool, service, uuid, title)
    add_hook.delay(short_url, hook, trim_service)
    return short_url


def save_trim_fail(site_id, error):
    trim_fail = TrimFailCache.get({'site': site_id})
    now = datetime.now()
    if trim_fail is None:
        trim_fail = {
            'site': site_id,
            'first_fail': now,
            'number_of_requests': 0
        }
    trim_fail['last_try'] = now
    trim_fail['last_error'] = error
    trim_fail['number_of_requests'] += 1
    TrimFailCache.set({'site': site_id}, trim_fail, None)


def should_bypass_trim(site_id):
    trim_fail = TrimFailCache.get({'site': site_id})
    should_bypass = False
    if trim_fail is not None:
        delta = datetime.now() - trim_fail['last_try']
        if int(delta.total_seconds()) < TRIM_FAIL_TIMEOUT:
            should_bypass = True
    return should_bypass


def create_shortcut_and_add_hook(trim_api_key, vanity_domain, request, long_url, site_id, tool, service, title, uuid):
    if vanity_domain:
        if not should_bypass_trim(site_id):
            try:
                short_url = get_shortcut_and_add_hook(trim_api_key, vanity_domain, request, long_url, site_id, tool,
                                                      service, title, uuid)
                TrimFailCache.delete({'site': site_id})
                return short_url
            except BadTrimKeyException as e:
                logger.info("Trim connection problem: %s. We will bypass vanity domain for site %s for %s seconds"
                            % (e.message, site_id, TRIM_FAIL_TIMEOUT))
                save_trim_fail(site_id, e.message)
                trim_fail = TrimFailCache.get({'site': site_id})
                if trim_fail.get('number_of_requests') == 1:
                    logger.info("Sending email to site %s because invalid tr.im key: %s" % (site_id, e.message))
            except TrimAPIException as e:
                logger.info("Trim connection problem: %s. We will bypass vanity domain for site %s for %s seconds"
                            % (e.message, site_id, TRIM_FAIL_TIMEOUT))
                save_trim_fail(site_id, e.message)

    if should_bypass_trim(-1):
        return long_url
    else:
        try:
            short_url = get_shortcut_and_add_hook(None, None, request, long_url, site_id, tool, service, title, uuid)
            TrimFailCache.delete({'site': -1})
            return short_url
        except ValidationFailedException as e:
            logger.info("Trim validation problem: %s for site: %s , url: %s and service %s"
                        % (e.message, site_id, long_url, service))
        except TrimAPIException as e:
            logger.info("Trim connection problem: %s. We will default to long_url for %s seconds"
                        % (e.message, TRIM_FAIL_TIMEOUT))
            save_trim_fail(-1, e.message)
        return long_url
