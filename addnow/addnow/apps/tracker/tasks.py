# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta

from django.conf import settings
from django.db import IntegrityError

from celery.utils.log import get_task_logger
from celery import Task
from pymongo.errors import PyMongoError
from referer_parser import Referer
from user_agents import parse

from addnow.apps.accounts import constants
from addnow.apps.accounts.models import UniqueUser
from addnow.apps.tracker.exceptions import IncorrectEventException
from addnow.apps.tracker.models import reports
from addnow.apps.tracker.models.collections import OutsideShares, UpdateCounters, GeoIPModel
from addnow.apps.tracker.utils import get_geoip_data, get_keywords, strip_scheme, decode_uuid
from addnow.cache import SiteSettingsCache, SocialCountersCache
from addnow.celery import app


ALLOWED_KEYWORD_TAGS = ('NN', 'NNS', 'NNP', 'NNPS')

logger = get_task_logger(__name__)


class BuriableTask(Task):
    abstract = True

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.warning('task failed %r', [exc, task_id, args, kwargs, einfo])
        self.retry(queue='buried_jobs')


def _create_unique_user(uuid, date):
    try:
        uuid = decode_uuid(uuid)
    except TypeError:
        raise IncorrectEventException('UUID decoding error for %s' % repr(uuid))

    if len(uuid) != 16:
        raise IncorrectEventException('Decoded UUID too long %s' % repr(uuid))

    try:
        unique_user = UniqueUser(uuid=uuid, created_at=date)
        unique_user.save(force_insert=True)
        is_first = True
    except IntegrityError:
        is_first = False
    return is_first


def _clean_event_data(site_id, date, query, headers=None, real_ip=None):
    is_first = True
    domain = None
    search_engine = None
    search_term = None
    country = constants.UNKNOWN_COUNTRY
    copied_keywords = []

    event = query.get('e_c')
    source = query.get('e_a')
    tool = query.get('e_t')
    uuid = query.get('e_u')
    url = query.get('e_n')
    title = query.get('e_i')
    timestamp = query.get('e_v')
    keywords_string = query.get('e_k')

    headers = headers or {}
    site_config = SiteSettingsCache.get_config(site_id)

    try:
        event = constants.Events(event).value
    except ValueError:
        raise IncorrectEventException('Incorrect event value: %s' % event)

    if timestamp:
        try:
            date = datetime.utcfromtimestamp(int(timestamp))
        except (ValueError, TypeError):
            raise IncorrectEventException('Unexpected timestamp format: %s' % timestamp)
    date = date + timedelta(minutes=site_config['offset'])

    if source and source not in constants.SOURCE_SET:
        raise IncorrectEventException('Incorrect source value: %s' % source)

    if tool:
        try:
            tool = constants.Tools(tool).value
        except ValueError:
            raise IncorrectEventException('Incorrect tool value: %s' % tool)

    if uuid:
        is_first = _create_unique_user(uuid, date)

    user_agent = parse(headers.get('HTTP_USER_AGENT', ''))
    browser = user_agent.browser.family
    referrer = headers.get('HTTP_REFERER')
    if referrer:
        r = Referer(referrer)
        domain = r.uri.netloc
        search_engine = r.referer
        search_term = r.search_term
    if real_ip:
        geoip_data = get_geoip_data(real_ip)
        if geoip_data and geoip_data['country_code']:
            country = geoip_data['country_code']
    if keywords_string:
        copied_keywords = get_keywords(keywords_string, ALLOWED_KEYWORD_TAGS)

    cleaned_data = dict(
        site=int(site_id),
        date=date,
        source=source,
        tool=tool,
        url=url,
        title=title,
        browser=browser,
        domain=domain,
        search_engine=search_engine,
        search_term=search_term,
        country=country,
        copied_keywords=copied_keywords
    )
    return event, is_first, cleaned_data


@app.task(base=BuriableTask)
def track_event(site_id, timestamp, query, headers=None, real_ip=None):
    """
    :type timestamp: datetime.datetime
    :param timestamp: event's timestamp in utc
    :param query: query string
    """

    try:
        event, is_first, kwargs = _clean_event_data(site_id, timestamp, query, headers, real_ip)
    except IncorrectEventException as exc:
        logger.error('Incorrect event: ' + str(exc))
    else:
        tool = kwargs['tool']
        if event == constants.Events.VIEW.value and real_ip:
            save_geoip_data.delay(site_id, timestamp, real_ip)
        if event == constants.Events.CLICK.value and tool == constants.Tools.ADDRESS_BAR.value:
            if is_first:
                logger.info('address-bar click event processed as share+click')
                update_counters.delay(constants.Events.SHARE.value, **kwargs)
            else:
                logger.info('address-bar click event processed as click only')
        update_counters.delay(event, **kwargs)


@app.task(bind=True, max_retries=10, base=BuriableTask)
def update_counters(self, event, value=1, **kwargs):
    """
    Updates aggregated reporting counters (shares, clicks) in database.
    :param kwargs: cleaned data
    """
    report_class = reports.REPORT_TYPES[event]

    number_of_queries = report_class.inc(value, **kwargs)
    log_stats(self, 'hits')
    log_stats(self, event, inc=number_of_queries, retry=False)


@app.task(bind=True, max_retries=100)
def add_hook(self, short_url, hook, trim_service):
    logger.info('Trying to add hook: {0}'.format(hook))
    try:
        if trim_service.get_hooks_count(strip_scheme(short_url)) == 0:
            trim_service.create_hook(strip_scheme(short_url), hook)
        else:
            logger.info('Hook is already provided for url {0}'.format(short_url))
    except Exception as exc:
        self.retry(exc=exc, countdown=(self.request.retries ** 2) + 1)


@app.task(max_retries=100, base=BuriableTask)
def save_external_shares(site_id, url, **data):
    """
    Saves external shares
    """
    clear_cache = False
    for source, actual_shares in data.items():
        query = {'site': int(site_id), 'source': source, 'url': url}
        outside_shares = OutsideShares()
        doc = outside_shares.find_one(query)
        actual_shares = int(actual_shares)
        current_shares = doc['shares'] if doc else 0
        if actual_shares != current_shares:
            del query['checksum']
            outside_shares.set_counter(value=actual_shares, **query)
            clear_cache = True
    if clear_cache:
        SocialCountersCache.delete(dict(site_id=site_id, url=url))


@app.task(max_retries=100, base=BuriableTask)
def save_geoip_data(site_id, timestamp, real_ip):
    geoip_data = get_geoip_data(real_ip)
    if geoip_data:
        geoip_data['country'] = geoip_data.pop('country_name')
        GeoIPModel().save(site=site_id, timestamp=timestamp, geo=geoip_data)


def log_stats(task_instance, field, inc=1, retry=True):
    if settings.CELERY_ALWAYS_EAGER:
        return

    try:
        UpdateCounters().inc({'_id': 1}, {field: inc}, upsert=True)
    except PyMongoError as exc:
        if retry:
            task_instance.retry(exc=exc, countdown=(task_instance.request.retries ** 2) + 1)
