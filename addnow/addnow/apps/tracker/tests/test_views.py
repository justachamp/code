# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib
from datetime import datetime

from django.core.signing import Signer
from django.core.urlresolvers import reverse
from django.test.testcases import TestCase
from django.test import Client
from django.test.client import RequestFactory
from django.test.utils import override_settings
from django.utils import timezone

from testfixtures import log_capture
from freezegun import freeze_time
from mock import MagicMock, patch, ANY

from addnow.apps.accounts import constants, factories
from addnow.apps.tracker import channels, views
from addnow.apps.tracker.models import collections
from addnow.apps.tracker.tests.base import MongoTestCase
from addnow.apps.tracker.exceptions import TrimAPIException, BadTrimKeyException, ValidationFailedException
from addnow.cache import TrimFailCache


class TestTracker(MongoTestCase):
    FROZEN_TIME = datetime(2012, 1, 14, 5, 1, 54, tzinfo=timezone.UTC())

    @classmethod
    def setUpClass(cls):
        super(TestTracker, cls).setUpClass()
        cls.client = Client()
        cls.factory = RequestFactory()
        cls.site = factories.SiteFactory(
            thank_you_message='test',
            thank_you_advert_image_url='',
            thank_you_advert_url='',
            thank_you_advert_title='',
            address_bar_sharing=True,
            domain='test-tasks.com'
        )
        cls.click_url = reverse('tracker_click')
        cls.track_event = reverse('track_event')
        cls.site_settings_url = reverse('site_settings')
        cls.site_id = Signer().sign(cls.site.pk)
        cls.counters_url = reverse('counters', kwargs={'site_id': cls.site_id})
        cls.counters_url_int = reverse('counters', kwargs={'site_id': cls.site.pk})
        cls.create_shortlink_url = reverse('tracker_create_shortlink')

    def _test_track_event(self, track_event_task, query):
        headers = {'HTTP_COOKIE': '', 'REMOTE_ADDR': '127.0.0.1'}
        response = self.client.get(self.track_event + '?' + urllib.urlencode(query))
        self.assertEqual(response.status_code, 204)
        track_event_task.delay.assert_called_ones_with(self.site.pk, self.FROZEN_TIME, query,
                                                       headers=headers, real_ip=None)

    def _test_click(self, track_event_task, kwargs, trim_data, query=None, params=None, headers=None, real_ip=None):
        data = json.dumps(trim_data)
        hook_url = reverse('tracker_click_hook', kwargs=kwargs)
        if params:
            hook_url += '?%s' % urllib.urlencode(params)

        response = self.client.post(hook_url, data=data, content_type='application/json')
        if not query:
            self.assertEqual(response.status_code, 400)
            self.assertFalse(track_event_task.delay.called)
        else:
            self.assertEqual(response.status_code, 204)
            headers = headers or {}
            track_event_task.delay.assert_called_once_with(self.site.pk, self.FROZEN_TIME, query,
                                                           headers=headers, real_ip=real_ip)

    @freeze_time(FROZEN_TIME)
    @patch('addnow.apps.tracker.views.track_event_task')
    def test__track_event_endpoint(self, track_event_task):
        site_ids = [self.site.pk, self.site_id]

        for site_id in site_ids:
            query = {
                'idsite': site_id,
                'e_c': constants.Events.CLICK.value
            }
            self._test_track_event(track_event_task, query)
            track_event_task.reset_mock()

    @freeze_time(FROZEN_TIME)
    @patch('addnow.apps.tracker.views.track_event_task')
    def test__track_event_endpoint_for_address_bar_sharing(self, track_event_task):
        site_ids = [self.site.pk, self.site_id]

        for site_id in site_ids:
            query = {
                'idsite': site_id,
                'e_c': constants.Events.CLICK.value,
                'e_n': 'http://example.com/',
                'e_a': constants.Tools.ADDRESS_BAR.value,
                'e_v': '1421773436',
                'e_u': 'rYdFxqC6EeS2EIyJpWQPRw'
            }
            self._test_track_event(track_event_task, query)
            track_event_task.reset_mock()

    @patch('addnow.apps.tracker.views.track_event_task')
    @log_capture()
    def test__click_missing_params_400(self, track_event_task, log_data):
        response = self.client.post(self.click_url)
        self.assertEqual(response.status_code, 400)
        self.assertFalse(track_event_task.delay.called)
        log_data.check(
            (
                'addnow.apps.tracker.views',
                'INFO',
                'click hook fired for site id None (tool: None, service: None, '
                'uuid: None) --BoUnDaRyStRiNg--\r\n'
            ),
            (
                'addnow.apps.tracker.views',
                'ERROR',
                'json decode error'
            )
        )

    @patch('addnow.apps.tracker.views.track_event_task')
    @log_capture()
    def test_click_invalid_site_id_400(self, track_event_task, log_data):
        kwargs = {
            'site_id': 'AAAVBBBDD',
            'tool': constants.Tools.SHARING_BUTTONS.value
        }
        trim_data = {
            'long_url': 'http://www.example.com',
            'clicked_at': self.FROZEN_TIME.isoformat()
        }
        log_capture_dict = {
            'site_id': kwargs['site_id'],
            'tool': constants.Tools.SHARING_BUTTONS.value,
            'service': None,
            'uuid': None,
            'data': json.dumps(trim_data)
        }

        self._test_click(track_event_task, kwargs, trim_data)
        log_data.check(
            (
                'addnow.apps.tracker.views',
                'INFO',
                'click hook fired for site id %(site_id)s (tool: %(tool)s, service: %(service)s, '
                'uuid: %(uuid)s) %(data)s' % log_capture_dict
            ),
            (
                'addnow.apps.tracker.views',
                'ERROR',
                "site_id can't be converted to int: u'%s'" % kwargs['site_id']
            )
        )

    @patch('addnow.apps.tracker.views.track_event_task')
    @log_capture()
    def test__click_missing_long_url_400(self, track_event_task, log_data):
        site_ids = [self.site.pk, self.site_id]

        for site_id in site_ids:
            kwargs = {
                'site_id': site_id,
                'tool': constants.Tools.SHARING_BUTTONS.value
            }
            trim_data = {
                'long_url': None,
                'clicked_at': self.FROZEN_TIME.isoformat()
            }
            params = {'service': constants.SOCIAL_SERVICE_FACEBOOK}
            log_capture_dict = {
                'site_id': site_id,
                'tool': constants.Tools.SHARING_BUTTONS.value,
                'service': constants.SOCIAL_SERVICE_FACEBOOK,
                'uuid': None,
                'data': json.dumps(trim_data)
            }

            self._test_click(track_event_task, kwargs, trim_data, params=params)
            log_data.check(
                (
                    'addnow.apps.tracker.views',
                    'INFO',
                    'click hook fired for site id %(site_id)s (tool: %(tool)s, service: %(service)s, '
                    'uuid: %(uuid)s) %(data)s' % log_capture_dict
                ),
                (
                    'addnow.apps.tracker.views',
                    'ERROR',
                    'bad request'
                )
            )
            track_event_task.reset_mock()
            log_data.clear()

    @freeze_time(FROZEN_TIME)
    @patch('addnow.apps.tracker.views.track_event_task')
    @log_capture()
    def test__click_success_204_with_service(self, track_event_task, log_data):
        site_ids = [self.site.pk, self.site_id]

        for site_id in site_ids:
            kwargs = {
                'site_id': site_id,
                'tool': constants.Tools.SHARING_BUTTONS.value
            }
            trim_data = {
                'long_url': 'http://www.example.com',
                'clicked_at': self.FROZEN_TIME.isoformat()
            }
            params = {'service': constants.SOCIAL_SERVICE_FACEBOOK}
            query = {
                'e_c': constants.Events.CLICK.value,
                'e_a': constants.SOCIAL_SERVICE_FACEBOOK,
                'e_n': trim_data['long_url'],
                'e_t': constants.Tools.SHARING_BUTTONS.value
            }
            log_capture_dict = {
                'site_id': site_id,
                'tool': constants.Tools.SHARING_BUTTONS.value,
                'service': constants.SOCIAL_SERVICE_FACEBOOK,
                'uuid': None,
                'data': json.dumps(trim_data)
            }

            self._test_click(track_event_task, kwargs, trim_data, query=query, params=params)
            log_data.check(
                (
                    'addnow.apps.tracker.views',
                    'INFO',
                    'click hook fired for site id %(site_id)s (tool: %(tool)s, service: %(service)s, '
                    'uuid: %(uuid)s) %(data)s' % log_capture_dict
                )
            )
            track_event_task.reset_mock()
            log_data.clear()

    @freeze_time(FROZEN_TIME)
    @patch('addnow.apps.tracker.views.track_event_task')
    @log_capture()
    def test__click_success_204_without_service(self, track_event_task, log_data):
        site_ids = [self.site.pk, self.site_id]

        for site_id in site_ids:
            kwargs = {
                'site_id': site_id,
                'tool': constants.Tools.COPY_PASTE.value
            }
            trim_data = {
                'long_url': 'http://www.example.com',
                'clicked_at': self.FROZEN_TIME.isoformat(),
                'referrer_host': 'gravity4.com',
                'ip': '10.0.2.2'
            }
            params = {'title': 'The+title'}
            query = {
                'e_c': constants.Events.CLICK.value,
                'e_a': constants.SOURCE_DARK_SOCIAL,
                'e_n': trim_data['long_url'],
                'e_i': urllib.unquote_plus(params['title']),
                'e_t': constants.Tools.COPY_PASTE.value
            }
            log_capture_dict = {
                'site_id': site_id,
                'tool': constants.Tools.COPY_PASTE.value,
                'service': None,
                'uuid': None,
                'data': json.dumps(trim_data)
            }

            self._test_click(track_event_task, kwargs, trim_data, query=query, params=params,
                             headers={'HTTP_REFERER': trim_data['referrer_host']}, real_ip=trim_data['ip'])
            log_data.check(
                (
                    'addnow.apps.tracker.views',
                    'INFO',
                    'click hook fired for site id %(site_id)s (tool: %(tool)s, service: %(service)s, '
                    'uuid: %(uuid)s) %(data)s' % log_capture_dict
                )
            )
            track_event_task.reset_mock()
            log_data.clear()

    @freeze_time(FROZEN_TIME)
    @patch('addnow.apps.tracker.views.track_event_task')
    @log_capture()
    def test__click_success_204_with_uuid_service(self, track_event_task, log_data):
        site_ids = [self.site.pk, self.site_id]

        for site_id in site_ids:
            kwargs = {
                'site_id': site_id,
                'tool': constants.Tools.SHARING_BUTTONS.value
            }
            trim_data = {
                'long_url': 'http://www.example.com',
                'clicked_at': self.FROZEN_TIME.isoformat()
            }
            params = {
                'service': constants.SOCIAL_SERVICE_FACEBOOK,
                'uuid': 'ALMOSTUNIQUEID'
            }
            query = {
                'e_c': constants.Events.CLICK.value,
                'e_n': trim_data['long_url'],
                'e_t': constants.Tools.SHARING_BUTTONS.value,
                'e_a': constants.SOCIAL_SERVICE_FACEBOOK,
                'e_u': params['uuid']
            }
            log_capture_dict = {
                'site_id': site_id,
                'tool': constants.Tools.SHARING_BUTTONS.value,
                'service': constants.SOCIAL_SERVICE_FACEBOOK,
                'uuid': params['uuid'],
                'data': json.dumps(trim_data)
            }

            self._test_click(track_event_task, kwargs, trim_data, query=query, params=params)
            log_data.check(
                (
                    'addnow.apps.tracker.views',
                    'INFO',
                    'click hook fired for site id %(site_id)s (tool: %(tool)s, service: %(service)s, '
                    'uuid: %(uuid)s) %(data)s' % log_capture_dict
                )
            )
            track_event_task.reset_mock()
            log_data.clear()

    def test__inject_site_id_400(self):
        request = self.factory.get(self.site_settings_url)
        response = views.site_settings(request)
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(json.loads(response.content), {'message': 'Missing site id'})

    def test__inject_site_id_invalid_400(self):
        request = self.factory.get('%s?idsite=AABB' % self.site_settings_url)
        response = views.site_settings(request)
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(json.loads(response.content), {'message': 'Invalid site id'})

    @patch('addnow.apps.tracker.views.create_uuid')
    def test__site_settings_cached(self, create_uuid):
        facebook_url = 'http://facebook.com/test'
        thank_you_message = 'test'
        uuid = 'yPEZFA4eEeWv9ggAJ/e7NQ'
        site = factories.SiteFactory(
            thank_you_message=thank_you_message,
            address_bar_sharing=True,
            copy_paste_sharing=True,
            domain='test-site-settings-2.com'
        )
        factories.FacebookUrlFactory(url=facebook_url, site=site)
        create_uuid.return_value = uuid
        site_ids = [str(site.pk), site.hash_id]

        for site_id in site_ids:
            request = self.factory.get(self.site_settings_url + '?idsite=' + site_id)
            expected = {
                'sharing': {'byHash': True, 'copyPaste': True, 'hasShortUrls': True},
                'thank_you': {
                    'services': {constants.SOCIAL_SERVICE_FACEBOOK: facebook_url},
                    'message': thank_you_message,
                    'advertImageUrl': u'',
                    'advertTitle': u'',
                    'advertUrl': u'',
                },
                'hash_id': site.hash_id,
                'widget_configurations': [],
                'uuid': uuid,
                'dmp_execute_code': False,
                'vanity_domain': ''
            }
            response = views.site_settings(request)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(expected, json.loads(response.content))

    @patch('addnow.apps.tracker.views.save_external_shares_task')
    @log_capture()
    def test__counters_require_post_or_patch_405(self, save_external_shares_task, log_data):
        response = self.client.get(self.counters_url)
        self.assertEqual(response.status_code, 405)
        self.assertFalse(save_external_shares_task.delay.called)
        log_data.check()

    @override_settings(USE_TZ=False)
    @patch('addnow.cache.SocialCountersCache.set')
    @patch('addnow.apps.tracker.views.save_external_shares_task')
    @log_capture()
    def test__counters_post_success_200(self, save_external_shares_task, set_cache, log_data):
        counters_urls = [self.counters_url, self.counters_url_int]
        outside_shares = {
            constants.SOCIAL_SERVICE_TWITTER: 124,
            constants.SOCIAL_SERVICE_GOOGLE_PLUS: 981,
            constants.SOCIAL_SERVICE_FACEBOOK: 21,
            constants.SOCIAL_SERVICE_LINKEDIN: 2,
            constants.SOCIAL_SERVICE_PINTEREST: 91919
        }
        url = 'http://www.example.com'

        # Add some values in outside_shares so it's improved covering
        for source, shares in outside_shares.items():
            collections.OutsideShares().set_counter(site=self.site.pk, url=url, source=source, value=shares)

        for counter_url in counters_urls:
            response = self.client.post(counter_url, {'url': url})
            self.assertEqual(response.status_code, 200)
            self.assertTrue(set_cache.called)
            self.assertFalse(save_external_shares_task.delay.called)
            log_data.check()

    @patch('addnow.apps.tracker.views.save_external_shares_task')
    @log_capture()
    def test__counters_patch_success_200(self, save_external_shares_task, log_data):
        counters_urls = [self.counters_url, self.counters_url_int]
        url = 'http://www.hasthelargehadroncolliderdestroyedtheworldyet.com/'
        data = {
            url: {
                'twitter': 444,
                'googlePlus': 673,
                'facebook': 81821,
                'linkedin': 85,
                'pinterest': 6
            }
        }

        for counter_url in counters_urls:
            response = self.client.patch(counter_url, json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data, json.loads(response.content))
            save_external_shares_task.assert_called_once(self.site.pk, url, **data[url])
            log_data.check()
            save_external_shares_task.reset_mock()

    @patch('addnow.apps.tracker.views.save_external_shares_task', MagicMock())
    @log_capture()
    def test__counters_invalid_site_id_400(self, log_data):
        kwargs = {'site_id': 'LALALALA'}
        invalid_counter_url = reverse('counters', kwargs=kwargs)
        url = 'http://www.hasthelargehadroncolliderdestroyedtheworldyet.com/'
        data = {
            url: {
                'twitter': 444,
                'googlePlus': 673,
                'facebook': 81821,
                'linkedin': 85,
                'pinterest': 6
            }
        }

        response = self.client.patch(invalid_counter_url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        log_data.check(
            (
                'addnow.apps.tracker.views',
                'ERROR',
                "site_id can't be converted to int: u'%s'" % kwargs['site_id']
            )
        )

    @patch('addnow.apps.tracker.trim.TrimService.create_shortcut')
    @patch('addnow.apps.tracker.views.add_hook')
    @patch('addnow.apps.tracker.views.should_bypass_trim')
    @log_capture()
    def test__create_shortlink_success_200(self, should_bypass_trim, add_hook, create_shortcut, log_data):
        original_url = 'http://test/original/url'
        short_url = 'http://short'
        uuid = 'yPEZFA4eEeWv9ggAJ/e7NQ'
        title = 'Some title'

        site_ids = [self.site.pk, self.site_id]
        for site_id in site_ids:
            data = {
                'original_url': original_url,
                'site_id': site_id,
                'tool': constants.Tools.SHARING_BUTTONS.value,
                'service': constants.SOCIAL_SERVICE_FACEBOOK,
                'uuid': uuid,
                'title': title,
            }
            create_shortcut.return_value = 'test_keyword', short_url
            add_hook.return_value = 0
            should_bypass_trim.return_value = False
            response = self.client.post(self.create_shortlink_url, data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content, json.dumps({'short_url': short_url}))
            create_shortcut.assert_called_once_with(
                original_url, str(self.site.pk), constants.Tools.SHARING_BUTTONS.value,
                constants.SOCIAL_SERVICE_FACEBOOK, None
            )
            hook_query = {
                'service': constants.SOCIAL_SERVICE_FACEBOOK,
                'uuid': uuid,
                'title': urllib.quote_plus(title)
            }
            add_hook.delay.assert_called_once_with(
                short_url,
                'http://testserver/click/%d/%s?%s' % (self.site.pk, constants.Tools.SHARING_BUTTONS.value,
                                                      urllib.urlencode(hook_query)),
                ANY
            )
            log_data.check()
            create_shortcut.reset_mock()
            add_hook.reset_mock()
            should_bypass_trim.reset_mock()
            log_data.clear()

    @patch('addnow.apps.tracker.trim.TrimService.create_shortcut', MagicMock())
    @patch('addnow.apps.tracker.views.add_hook', MagicMock())
    @log_capture()
    def test__create_shortlink_invalid_tool_400(self, log_data):
        data = {
            'original_url': 'http://test.me/url',
            'site_id': 12345,
            'tool': '',
            'service': constants.SOCIAL_SERVICE_FACEBOOK,
            'uuid': 'yPEZFA4eEeWv9ggAJ/e7NQ',
            'title': 'Some title'
        }
        response = self.client.post(self.create_shortlink_url, data)
        self.assertEqual(response.status_code, 400)
        log_data.check(('addnow.apps.tracker.views', 'ERROR', 'bad short link request'),)

    @log_capture()
    def test__create_shortlink_invalid_site_id_400(self, log_data):
        data = {
            'original_url': 'http://test.me/url',
            'site_id': 'aaa',
            'tool': constants.Tools.SHARING_BUTTONS.value,
            'service': constants.SOCIAL_SERVICE_FACEBOOK
        }
        response = self.client.post(self.create_shortlink_url, data)
        self.assertEqual(response.status_code, 400)
        log_data.check(
            (
                'addnow.apps.tracker.views',
                'ERROR',
                "site_id can't be converted to int: u'%s'" % data['site_id']
            )
        )

    @patch('addnow.apps.tracker.trim.TrimService.http_request')
    @log_capture()
    def test__create_shortlink_without_vanity_domain_and_trim_connection_problem(self, http_request, log_data):
        original_url = 'http://test.me/url'
        exception_message = 'test expection message'
        timeout = views.TRIM_FAIL_TIMEOUT
        site_ids = [self.site.pk, self.site_id]
        for site_id in site_ids:
            TrimFailCache.delete({'site': -1})
            data = {
                'original_url': original_url,
                'site_id': site_id,
                'tool': constants.Tools.SHARING_BUTTONS.value,
                'service': constants.SOCIAL_SERVICE_FACEBOOK
            }
            http_request.side_effect = TrimAPIException(exception_message)
            response = self.client.post(self.create_shortlink_url, data)
            self.assertEqual(response.content, json.dumps({'short_url': original_url}))
            # Second time it should use cache and not call trim service
            response = self.client.post(self.create_shortlink_url, data)
            self.assertEqual(response.content, json.dumps({'short_url': original_url}))
            http_request.assert_called_once_with('post', 'links', data={
                'seed': 'an_%s_sharing-buttons_facebook' % self.site.id,
                'long_url': original_url
            })
            log_data.check(
                (
                    'addnow.apps.tracker.views',
                    'INFO',
                    "Trim connection problem: %s. We will default to long_url for %s seconds" %
                    (exception_message, timeout)
                )
            )
            log_data.clear()
            http_request.reset_mock()

    @patch('addnow.apps.tracker.trim.TrimService.http_request')
    @log_capture()
    def test__create_shortlink_with_vanity_domain_and_trim_connection_problem(self, http_request, log_data):
        original_url = 'http://test.me/url'
        exception_message = "Dumb exception message"
        timeout = views.TRIM_FAIL_TIMEOUT
        site_ids = [self.site.pk, self.site_id]
        for site_id in site_ids:
            TrimFailCache.delete({'site': self.site.pk})
            TrimFailCache.delete({'site': -1})
            data = {
                'original_url': original_url,
                'site_id': site_id,
                'tool': constants.Tools.SHARING_BUTTONS.value,
                'service': constants.SOCIAL_SERVICE_FACEBOOK,
                'vanity_domain': 'test_vanity.domain.pt'
            }
            http_request.side_effect = TrimAPIException(exception_message)
            response = self.client.post(self.create_shortlink_url, data)
            self.assertEqual(response.content, json.dumps({'short_url': original_url}))
            # Second time it should use cache and not call trim service
            response = self.client.post(self.create_shortlink_url, data)
            self.assertEqual(response.content, json.dumps({'short_url': original_url}))
            http_request.assert_called_twice_with('post', 'links', data={
                'seed': 'an_%s_sharing-buttons_facebook' % self.site.id,
                'long_url': original_url
            })
            log_data.check(
                (
                    'addnow.apps.tracker.views',
                    'INFO',
                    "Trim connection problem: %s. We will bypass vanity domain for site %s for %s seconds" %
                    (exception_message, self.site.pk, timeout)
                ),
                (
                    'addnow.apps.tracker.views',
                    'INFO',
                    "Trim connection problem: %s. We will default to long_url for %s seconds" %
                    (exception_message, timeout)
                ),
            )
            log_data.clear()
            http_request.reset_mock()

    @patch('addnow.apps.tracker.trim.TrimService.http_request')
    @log_capture()
    def test__create_shortlink_with_vanity_domain_and_bad_trim_key(self, http_request, log_data):
        original_url = 'http://test.me/url'
        exception_message = "{'Forbidden': 'Authentication Failed.'}"
        timeout = views.TRIM_FAIL_TIMEOUT
        site_ids = [self.site.pk, self.site_id]
        for site_id in site_ids:
            TrimFailCache.delete({'site': self.site.pk})
            TrimFailCache.delete({'site': -1})
            data = {
                'original_url': original_url,
                'site_id': site_id,
                'tool': constants.Tools.SHARING_BUTTONS.value,
                'service': constants.SOCIAL_SERVICE_FACEBOOK,
                'vanity_domain': 'test_vanity.domain.pt'
            }
            http_request.side_effect = BadTrimKeyException(exception_message)
            response = self.client.post(self.create_shortlink_url, data)
            self.assertEqual(response.content, json.dumps({'short_url': original_url}))
            # Second time it should use cache and not call trim service
            response = self.client.post(self.create_shortlink_url, data)
            self.assertEqual(response.content, json.dumps({'short_url': original_url}))
            http_request.assert_called_twice_with('post', 'links', data={
                'seed': 'an_%s_sharing-buttons_facebook' % self.site.id,
                'long_url': original_url
            })
            log_data.check(
                (
                    'addnow.apps.tracker.views',
                    'INFO',
                    "Trim connection problem: %s. We will bypass vanity domain for site %s for %s seconds" %
                    (exception_message, self.site.pk, timeout)
                ),
                (
                    'addnow.apps.tracker.views',
                    'INFO',
                    "Sending email to site %s because invalid tr.im key: %s" %
                    (self.site.pk, exception_message)
                ),
                (
                    'addnow.apps.tracker.views',
                    'INFO',
                    "Trim connection problem: %s. We will default to long_url for %s seconds" %
                    (exception_message, timeout)
                ),
            )
            log_data.clear()
            http_request.reset_mock()

    @patch('addnow.apps.tracker.trim.TrimService.http_request')
    @log_capture()
    def test__create_shortlink_when_using_default_trim_key_and_short_url_already_taken(self, http_request, log_data):
        original_url = 'http://test.me/url'
        exception_message = "Already taken"
        site_ids = [self.site.pk, self.site_id]
        for site_id in site_ids:
            TrimFailCache.delete({'site': self.site.pk})
            TrimFailCache.delete({'site': -1})
            data = {
                'original_url': original_url,
                'site_id': site_id,
                'tool': constants.Tools.SHARING_BUTTONS.value,
                'service': constants.SOCIAL_SERVICE_FACEBOOK,
            }
            http_request.side_effect = ValidationFailedException(exception_message)
            response = self.client.post(self.create_shortlink_url, data)
            self.assertEqual(response.content, json.dumps({'short_url': original_url}))
            # Second time it should not use cache and call trim service again
            response = self.client.post(self.create_shortlink_url, data)
            self.assertEqual(response.content, json.dumps({'short_url': original_url}))
            http_request.assert_called_twice_with('post', 'links', data={
                'seed': 'an_%s_sharing-buttons_facebook' % self.site.id,
                'long_url': original_url
            })
            log_data.check(
                (
                    'addnow.apps.tracker.views',
                    'INFO',
                    "Trim validation problem: %s for site: %s , url: %s and service %s" %
                    (exception_message, self.site.pk, original_url, constants.SOCIAL_SERVICE_FACEBOOK)
                ),
                (
                    'addnow.apps.tracker.views',
                    'INFO',
                    "Trim validation problem: %s for site: %s , url: %s and service %s" %
                    (exception_message, self.site.pk, original_url, constants.SOCIAL_SERVICE_FACEBOOK)
                )
            )
            log_data.clear()
            http_request.reset_mock()

    def test__check_trim_service_and_cache(self):
        should_bypass = views.should_bypass_trim(self.site.pk)
        self.assertEqual(should_bypass, False)
        views.save_trim_fail(self.site.id, 'trim_service')
        should_bypass = views.should_bypass_trim(self.site.pk)
        self.assertEqual(should_bypass, True)
        trim_fail = TrimFailCache.get({'site': self.site.pk})
        self.assertEqual(trim_fail['last_error'], 'trim_service')

    @patch('django.core.mail.EmailMultiAlternatives.send')
    def test_send_email(self, send_email):
        # With data
        data = {
            'from_email': 'matias@gmail.com',
            'to_email': 'matias@gmail.com',
            'message': '1234567890',
            'captcha': '1234'
        }
        self.client.post(reverse('tracker_send_email'), data=data)
        send_email.assert_called_once()


class TestNonJavascriptSharing(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestNonJavascriptSharing, cls).setUpClass()
        cls.client = Client()
        cls.factory = RequestFactory()
        cls.service_factory = channels.ServiceFactory()
        cls.service_objects = {
            constants.SOCIAL_SERVICE_GMAIL: channels.GmailService,
            constants.SOCIAL_SERVICE_GOOGLE_PLUS: channels.GooglePlusService,
            constants.SOCIAL_SERVICE_FACEBOOK: channels.FacebookService,
            constants.SOCIAL_SERVICE_TWITTER: channels.TwitterService,
            constants.SOCIAL_SERVICE_DIGG: channels.DiggService,
            constants.SOCIAL_SERVICE_DELICIOUS: channels.DeliciousService,
            constants.SOCIAL_SERVICE_STUMBLEUPON: channels.StumbleuponService,
            constants.SOCIAL_SERVICE_LINKEDIN: channels.LinkedinService,
            constants.SOCIAL_SERVICE_PINTEREST: channels.PinterestService,
            constants.SOCIAL_SERVICE_WHATSAPP: channels.WhatsappService,
            constants.SOCIAL_SERVICE_TUMBLR: channels.TumblrService,
            constants.SOCIAL_SERVICE_REDDIT: channels.RedditService,
            constants.SOCIAL_SERVICE_INSTAGRAM: channels.Service
        }
        cls.site = factories.SiteFactory(
            thank_you_message='test',
            address_bar_sharing=True,
            copy_paste_sharing=True,
            domain='test-site-settings.com',
            trim_api_key='123'
        )
        cls.site_id = Signer().sign(cls.site.pk)

    def test__all_channels(self):
        for class_instance in self.service_objects.values():
            try:
                instance = class_instance()
                url = instance.get_redirect_url().split('?')[0]
                self.assertEqual(url, instance.url)
            except NotImplementedError:
                pass

    def test__factory_on_real_channels(self):
        for channel in self.service_objects.keys():
            service = self.service_factory.get_service(channel)
            self.assertIsInstance(service, self.service_objects[channel])

    def test__factory_on_bad_channels(self):
        with self.assertRaises(KeyError):
            self.service_factory.get_service('test-bad-service')

    def test__unsupported_service(self):
        share_url = reverse('tracker_share', kwargs={'channel': 'someservice'})
        response = self.client.get(share_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, 'Unknown/unsupported service')

    def test__url_without_params(self):
        share_url = reverse('tracker_share', kwargs={'channel': constants.SOCIAL_SERVICE_GMAIL})
        response = self.client.get(share_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, '')

    @patch('addnow.apps.tracker.views.track_event_task', MagicMock())
    @patch('addnow.apps.tracker.views.create_shortcut_and_add_hook')
    def test__facebook_sharing(self, create_shortcut_and_add_hook):
        factories.FacebookUrlFactory(url='http://facebook.com/test', site=self.site)
        share_url = reverse('tracker_share', kwargs={'channel': constants.SOCIAL_SERVICE_FACEBOOK})
        url = 'http://%s' % self.site.domain

        site_ids = [self.site.pk, self.site_id]
        for site_id in site_ids:
            current_url = share_url + '?' + urllib.urlencode({
                'url': url,
                'site_id': site_id,
                'title': self.site.thank_you_message
            })
            request = self.factory.get(current_url)
            response = views.share(request, constants.SOCIAL_SERVICE_FACEBOOK)

            create_shortcut_and_add_hook.assert_called_once_with(
                self.site.trim_api_key, None, request, url, str(self.site.pk),
                constants.Tools.NEWSLETTER_SHARING_BUTTONS.value, constants.SOCIAL_SERVICE_FACEBOOK,
                self.site.thank_you_message, None
            )

            self.assertEqual(response.status_code, 302)

            # Test empty url
            current_url = share_url + '?' + urllib.urlencode({
                'url': '',
                'site_id': site_id,
                'title': self.site.thank_you_message
            })
            request = self.factory.get(current_url)
            response = views.share(request, constants.SOCIAL_SERVICE_FACEBOOK)

            self.assertEqual(response.status_code, 400)

            create_shortcut_and_add_hook.reset_mock()

    @patch('addnow.apps.tracker.views.track_event_task', MagicMock())
    @patch('addnow.apps.tracker.views.create_shortcut_and_add_hook')
    def test__reddit_sharing(self, create_shortcut_and_add_hook):
        factories.FacebookUrlFactory(url='http://reddit.com/test', site=self.site)
        share_url = reverse('tracker_share', kwargs={'channel': constants.SOCIAL_SERVICE_REDDIT})
        url = 'http://%s' % self.site.domain

        site_ids = [self.site.pk, self.site_id]
        for site_id in site_ids:
            current_url = share_url + '?' + urllib.urlencode({
                'url': url,
                'site_id': site_id,
                'title': self.site.thank_you_message
            })
            request = self.factory.get(current_url)
            response = views.share(request, constants.SOCIAL_SERVICE_REDDIT)

            create_shortcut_and_add_hook.assert_not_called()

            self.assertEqual(response.status_code, 302)

            # Test empty url
            current_url = share_url + '?' + urllib.urlencode({
                'url': '',
                'site_id': site_id,
                'title': self.site.thank_you_message
            })
            request = self.factory.get(current_url)
            response = views.share(request, constants.SOCIAL_SERVICE_REDDIT)

            self.assertEqual(response.status_code, 400)

            create_shortcut_and_add_hook.reset_mock()

    def test__create_shortcut_and_add_hook(self):
        factories.FacebookUrlFactory(url='http://facebook.com/test', site=self.site)
        share_url = reverse('tracker_share', kwargs={'channel': constants.SOCIAL_SERVICE_FACEBOOK})

        site_ids = [self.site.pk, self.site_id]
        for site_id in site_ids:
            current_url = share_url + '?' + urllib.urlencode({
                'url': 'http://%s' % self.site.domain,
                'site_id': site_id,
                'title': self.site.thank_you_message
            })
            request = self.factory.get(current_url)
            views.share(request, constants.SOCIAL_SERVICE_FACEBOOK)
            url = 'http://test-site-settings.com'
            short_url = views.create_shortcut_and_add_hook(
                None, None, request, url, str(self.site.id),
                constants.Tools.NEWSLETTER_SHARING_BUTTONS.value,
                constants.SOCIAL_SERVICE_FACEBOOK,
                self.site.thank_you_message, None
            )
            self.assertEqual(short_url, url)

    def test__invalid_sharing(self):
        share_url = reverse('tracker_share', kwargs={'channel': constants.SOCIAL_SERVICE_TWITTER})

        share_url += '?' + urllib.urlencode({
            'url': 'http://lalala.com',
            'site_id': 'LALALA',
            'title': 'oops'
        })
        request = self.factory.get(share_url)
        response = views.share(request, constants.SOCIAL_SERVICE_FACEBOOK)

        self.assertEqual(response.status_code, 400)
