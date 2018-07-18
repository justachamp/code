# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from datetime import datetime

from testfixtures import log_capture
from mock import MagicMock, patch, call

from django.db import transaction
from django.test.utils import override_settings
from django.utils import timezone

from addnow.apps.accounts import constants, factories, models
from addnow.apps.tracker import tasks
from addnow.apps.tracker.models import collections
from addnow.apps.tracker.tests.base import MongoTestCase
from addnow.apps.tracker.trim import TrimService
from addnow.apps.tracker.utils import create_uuid, strip_scheme, decode_uuid


class TestTasks(MongoTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestTasks, cls).setUpClass()
        cls.site = factories.SiteFactory(
            thank_you_message='test',
            address_bar_sharing=True,
            domain='test-tasks.com'
        )
        cls.trim_service = TrimService()
        cls.timestamp = datetime(2000, 1, 15, 4, 7)

    def setUp(self):
        super(TestTasks, self).setUp()
        self.cleaned_data = {
            'site': self.site.pk,
            'date': self.timestamp,
            'source': None,
            'tool': None,
            'domain': None,
            'url': None,
            'title': None,
            'search_engine': None,
            'search_term': None,
            'country': constants.UNKNOWN_COUNTRY,
            'browser': constants.UNKNOWN_BROWSER,
            'copied_keywords': []
        }

    def _test_track_event(self, update_counters, event, query, headers=None, real_ip=None):
        tasks.track_event.delay(self.site.pk, self.timestamp, query, headers=headers, real_ip=real_ip)
        update_counters.delay.assert_called_once_with(event, **self.cleaned_data)

    @patch('addnow.apps.tracker.tasks.track_event.delay', MagicMock(side_effect=Exception))
    @log_capture()
    def test__task_failure(self, log_data):
        self.assertRaises(Exception, tasks.track_event.delay, self.site.pk, '1', '1')
        log_data.check()

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture()
    def test__track_event(self, update_counters, log_data):
        query = {
            'e_c': constants.Events.CLICK.value,
            'e_a': constants.SOCIAL_SERVICE_FACEBOOK,
            'e_t': constants.Tools.SHARING_BUTTONS.value
        }

        self.cleaned_data.update({
            'tool': constants.Tools.SHARING_BUTTONS.value,
            'source': constants.SOCIAL_SERVICE_FACEBOOK
        })
        self._test_track_event(update_counters, constants.Events.CLICK.value, query)
        log_data.check()
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture()
    def test__track_view_event(self, update_counters, log_data):
        query = {
            'e_i': 'AddNow Demo',
            'e_c': constants.Events.VIEW.value,
            'e_n': 'http://example.com/',
            'e_t': constants.Tools.SHARING_BUTTONS.value
        }

        self.cleaned_data.update({
            'url': query['e_n'],
            'title': query['e_i'],
            'tool': constants.Tools.SHARING_BUTTONS.value,
        })
        self._test_track_event(update_counters, constants.Events.VIEW.value, query)
        log_data.check()
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture()
    def test__referrer_track(self, update_counters, log_data):
        query = {
            'e_c': constants.Events.CLICK.value,
            'e_a': constants.SOCIAL_SERVICE_FACEBOOK,
            'e_t': constants.Tools.SHARING_BUTTONS.value
        }
        domain = 'www.google.com'
        headers = {'HTTP_REFERER': 'http://%s' % domain}

        self.cleaned_data.update({
            'tool': constants.Tools.SHARING_BUTTONS.value,
            'source': constants.SOCIAL_SERVICE_FACEBOOK,
            'domain': domain,
            'search_engine': 'Google'
        })
        self._test_track_event(update_counters, constants.Events.CLICK.value, query, headers=headers)
        log_data.check()

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture()
    def test__track_event_with_new_uuid(self, update_counters, log_data):
        uuid = 'K\xee\xab\xae\xa0\xb2\x11\xe4\xb6\x10\x8c\x89\xa5d\x0fG'
        created_at = datetime(2000, 2, 23, 4, 15)
        factories.UniqueUserFactory(uuid=uuid, created_at=created_at)
        query = {
            'e_c': constants.Events.CLICK.value,
            'e_a': constants.SOCIAL_SERVICE_FACEBOOK,
            'e_u': '3zYLCqCyEeS2EIyJpWQPRw',
            'e_t': constants.Tools.SHARING_BUTTONS.value
        }

        self.cleaned_data.update({
            'tool': constants.Tools.SHARING_BUTTONS.value,
            'source': constants.SOCIAL_SERVICE_FACEBOOK
        })
        self._test_track_event(update_counters, constants.Events.CLICK.value, query)
        log_data.check()
        self.assertEqual(
            {frozenset(obj.items()) for obj in models.UniqueUser.objects.all().values()},
            {
                frozenset([
                    ('uuid', uuid),
                    ('created_at', created_at.replace(tzinfo=timezone.UTC()))
                ]),
                frozenset([
                    ('uuid', decode_uuid(query['e_u'])),
                    ('created_at', self.timestamp.replace(tzinfo=timezone.UTC()))
                ])
            }
        )

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture()
    def test__track_event_with_used_uuid(self, update_counters, log_data):
        uuid = '\xdf6\x0b\n\xa0\xb2\x11\xe4\xb6\x10\x8c\x89\xa5d\x0fG'
        created_at = datetime(2000, 2, 23, 4, 15)
        factories.UniqueUserFactory(uuid=uuid, created_at=created_at)
        query = {
            'e_c': constants.Events.CLICK.value,
            'e_a': constants.SOCIAL_SERVICE_FACEBOOK,
            'e_u': '3zYLCqCyEeS2EIyJpWQPRw',
            'e_t': constants.Tools.SHARING_BUTTONS.value
        }

        with transaction.atomic():
            tasks.track_event.delay(self.site.pk, self.timestamp, query)
        self.assertTrue(update_counters.delay.called)
        log_data.check()
        self.assertEqual(
            {frozenset(obj.items()) for obj in models.UniqueUser.objects.all().values()},
            {frozenset([
                ('uuid', uuid),
                ('created_at', created_at.replace(tzinfo=timezone.UTC()))
            ])}
        )

    @patch('addnow.apps.tracker.tasks.update_counters')
    def test__track_event_with_too_long_uuid(self, update_counters):
        query = {
            'e_c': constants.Events.COPY.value,
            'e_a': constants.SOCIAL_SERVICE_FACEBOOK,
            'e_u': 'x' * 20,
        }

        tasks.track_event.delay(self.site.pk, self.timestamp, query)
        self.assertFalse(update_counters.delay.called)
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture(level=logging.INFO)
    def test__track_event_without_source(self, update_counters, log_data):
        query = {
            'e_c': constants.Events.SHARE.value,
            'e_t': constants.Tools.SHARING_BUTTONS.value
        }

        self.cleaned_data.update({
            'tool': constants.Tools.SHARING_BUTTONS.value
        })
        self._test_track_event(update_counters, constants.Events.SHARE.value, query)
        log_data.check()
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture()
    def test__track_event_with_error_invalid_source(self, update_counters, log_data):
        query = {
            'e_c': constants.Events.CLICK.value,
            'e_a': 'lalalal',
        }

        tasks.track_event.delay(self.site.pk, self.timestamp, query)
        self.assertFalse(update_counters.delay.called)
        log_data.check(
            (
                'addnow.apps.tracker.tasks',
                'ERROR',
                'Incorrect event: Incorrect source value: %s' % query['e_a']
            )
        )
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture(level=logging.INFO)
    def test__track_event_without_tool(self, update_counters, log_data):
        query = {
            'e_c': constants.Events.VIEW.value,
            'e_n': 'http://example.com/'
        }

        self.cleaned_data.update({
            'url': query['e_n']
        })
        self._test_track_event(update_counters, constants.Events.VIEW.value, query)
        log_data.check()
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture()
    def test__track_event_with_error_invalid_tool(self, update_counters, log_data):
        query = {
            'e_c': constants.Events.CLICK.value,
            'e_t': 'lalalal',
        }

        tasks.track_event.delay(self.site.pk, self.timestamp, query)
        self.assertFalse(update_counters.delay.called)
        log_data.check(
            (
                'addnow.apps.tracker.tasks',
                'ERROR',
                'Incorrect event: Incorrect tool value: %s' % query['e_t']
            )
        )
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture()
    def test__track_event_with_ip_on_header(self, update_counters, log_data):
        query = {
            'e_c': constants.Events.SHARE.value,
            'e_a': constants.SOCIAL_SERVICE_TWITTER,
            'e_n': 'http://example.com/',
            'e_t': constants.Tools.SHARING_BUTTONS.value
        }
        real_ip = '8.8.8.8'
        headers = {'IP': real_ip}

        self.cleaned_data.update({
            'url': query['e_n'],
            'tool': constants.Tools.SHARING_BUTTONS.value,
            'source': constants.SOCIAL_SERVICE_TWITTER,
            'country': 'US'
        })
        self._test_track_event(update_counters, constants.Events.SHARE.value, query,
                               headers=headers, real_ip=real_ip)
        log_data.check()
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture()
    def test__track_event_ip_on_header_with_invalid_geolocation(self, update_counters, log_data):
        query = {
            'e_c': constants.Events.SHARE.value,
            'e_a': constants.SOCIAL_SERVICE_TWITTER,
            'e_n': 'http://example.com/',
            'e_t': constants.Tools.SHARING_BUTTONS.value
        }
        real_ip = '0.0.0.0'
        headers = {'IP': real_ip}

        self.cleaned_data.update({
            'url': query['e_n'],
            'tool': constants.Tools.SHARING_BUTTONS.value,
            'source': constants.SOCIAL_SERVICE_TWITTER
        })
        self._test_track_event(update_counters, constants.Events.SHARE.value, query,
                               headers=headers, real_ip=real_ip)
        log_data.check()
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @override_settings(USE_TZ=False)
    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture(level=logging.INFO)
    def test__track_use_address_bar_event_twice_leads_to_share_first_time(self, update_counters, log_data):
        query = {
            'e_c': constants.Events.CLICK.value,
            'e_a': constants.SOCIAL_SERVICE_TWITTER,
            'e_n': 'http://exampleTwice.com/',
            'e_u': create_uuid(),
            'e_t': constants.Tools.ADDRESS_BAR.value
        }
        real_ip = '8.8.8.8'
        headers = {'IP': real_ip}

        self.cleaned_data.update({
            'url': query['e_n'],
            'tool': constants.Tools.ADDRESS_BAR.value,
            'source': constants.SOCIAL_SERVICE_TWITTER,
            'country': 'US'
        })

        tasks.track_event.delay(self.site.pk, self.timestamp, query, headers=headers, real_ip=real_ip)
        self.assertEqual(update_counters.delay.call_count, 2)
        self.assertEqual(update_counters.delay.mock_calls[0],
                         call(constants.Events.SHARE.value, **self.cleaned_data))
        self.assertEqual(update_counters.delay.mock_calls[1],
                         call(constants.Events.CLICK.value, **self.cleaned_data))
        log_data.check(
            (
                'addnow.apps.tracker.tasks',
                'INFO',
                'address-bar click event processed as share+click'
            )
        )

        log_data.clear()
        with transaction.atomic():
            tasks.track_event.delay(self.site.pk, self.timestamp, query, headers=headers, real_ip=real_ip)
        update_counters.delay.assert_called_with(constants.Events.CLICK.value, **self.cleaned_data)
        log_data.check(
            (
                'addnow.apps.tracker.tasks',
                'INFO',
                'address-bar click event processed as click only'
            )
        )
        self.assertEqual(models.UniqueUser.objects.all().count(), 1)

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture()
    def test__track_event_with_timestamp_override(self, update_counters, log_data):
        query = {
            'e_c': constants.Events.SHARE.value,
            'e_a': constants.SOCIAL_SERVICE_TWITTER,
            'e_n': 'http://example.com/',
            'e_v': '947521140',
            'e_t': constants.Tools.SHARING_BUTTONS.value
        }

        self.cleaned_data.update({
            'url': query['e_n'],
            'tool': constants.Tools.SHARING_BUTTONS.value,
            'source': constants.SOCIAL_SERVICE_TWITTER,
            'date': datetime.utcfromtimestamp(int(query['e_v']))
        })
        self._test_track_event(update_counters, constants.Events.SHARE.value, query)
        log_data.check()
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture()
    def test__track_event_with_keywords(self, update_counters, log_data):
        query = {
            'e_c': constants.Events.COPY.value,
            'e_n': 'http://example.com/',
            'e_t': constants.Tools.COPY_PASTE.value,
            'e_k': 'This is the best tool you can get!'
        }

        self.cleaned_data.update({
            'url': query['e_n'],
            'tool': constants.Tools.COPY_PASTE.value,
            'copied_keywords': ['tool']
        })
        self._test_track_event(update_counters, constants.Events.COPY.value, query)
        log_data.check()
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @patch('addnow.apps.tracker.tasks.update_counters')
    @log_capture()
    def test__track_event_with_error_timestamp_override(self, update_counters, log_data):
        query = {
            'e_c': constants.Events.SHARE.value,
            'e_a': constants.SOCIAL_SERVICE_TWITTER,
            'e_n': 'http://example.com/',
            'e_v': 'ERROR'
        }

        tasks.track_event.delay(self.site.pk, self.timestamp, query)
        self.assertFalse(update_counters.delay.called)
        log_data.check(
            ('addnow.apps.tracker.tasks', 'ERROR', 'Incorrect event: Unexpected timestamp format: %s' % query['e_v'])
        )
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @patch('addnow.apps.tracker.tasks.update_counters', MagicMock())
    @log_capture()
    def test__track_event_with_error_uuid(self, log_data):
        query = {
            'e_c': constants.Events.COPY.value,
            'e_n': 'http://example.com/',
            'e_t': constants.Tools.COPY_PASTE.value,
            'e_k': 'This is the best tool you can get!',
            'e_u': '12345'
        }

        tasks.track_event.delay(self.site.pk, self.timestamp, query, None)
        log_data.check(
            ('addnow.apps.tracker.tasks', 'ERROR', "Incorrect event: UUID decoding error for u'%s'" % query['e_u'])
        )
        self.assertEqual(models.UniqueUser.objects.all().count(), 0)

    @patch('addnow.apps.tracker.models.reports.Follows.inc')
    def test__update_counters(self, follows_inc):
        kwargs = dict(site=self.site.pk, source=constants.SOCIAL_SERVICE_FACEBOOK,
                      url='http://test.com/', title=None, date=datetime.utcnow())
        tasks.update_counters.delay(constants.Events.FOLLOW.value, **kwargs)
        follows_inc.assert_called_once_with(1, **kwargs)

    @patch('addnow.apps.tracker.models.collections.OutsideShares.set_counter')
    def test__save_external_shares(self, set_outside_shares):
        outside_shares = {
            constants.SOCIAL_SERVICE_TWITTER: 124,
            constants.SOCIAL_SERVICE_GOOGLE_PLUS: 981,
            constants.SOCIAL_SERVICE_FACEBOOK: 21,
            constants.SOCIAL_SERVICE_LINKEDIN: 2,
            constants.SOCIAL_SERVICE_PINTEREST: 91919
        }
        url = 'http://test.com/'

        tasks.save_external_shares.delay(self.site.pk, url, **outside_shares)
        self.assertEqual(set_outside_shares.call_count, 5)

        expected_call_args_list = []
        for source, shares in outside_shares.items():
            expected_call_args_list.append(call(site=self.site.pk, url=url, source=source, value=shares))
        self.assertEqual(set_outside_shares.call_args_list, expected_call_args_list)

    def test__save_external_shares_with_no_update_counters(self):
        outside_shares = {
            constants.SOCIAL_SERVICE_TWITTER: 124,
            constants.SOCIAL_SERVICE_GOOGLE_PLUS: 981,
            constants.SOCIAL_SERVICE_FACEBOOK: 21,
            constants.SOCIAL_SERVICE_LINKEDIN: 2,
            constants.SOCIAL_SERVICE_PINTEREST: 91919
        }
        url = 'http://test.com/'

        for source, shares in outside_shares.items():
            collections.OutsideShares().set_counter(site=self.site.pk, url=url, source=source, value=shares)
        with patch('addnow.apps.tracker.models.collections.OutsideShares.set_counter') as set_counter:
            tasks.save_external_shares.delay(self.site.pk, url, **outside_shares)
            self.assertFalse(set_counter.called)

    @patch('addnow.apps.tracker.trim.TrimService.get_hooks_count')
    @patch('addnow.apps.tracker.trim.TrimService.create_hook')
    @log_capture()
    def test__add_hook_when_there_is_no_hook(self, create_hook, get_hooks_count, log_data):
        get_hooks_count.return_value = 0
        short_url = 'http://test.com/short'
        hook = 'http://testserver/click/134/sharing-buttons?service=facebook'

        tasks.add_hook.delay(short_url, hook, self.trim_service)
        create_hook.assert_called_once_with(strip_scheme(short_url), hook)
        log_data.check(
            (
                'addnow.apps.tracker.tasks',
                'INFO',
                'Trying to add hook: %s' % hook
            )
        )
        # Check in case create_hook raises an exception
        create_hook.side_effect = Exception()
        self.assertRaises(Exception, tasks.add_hook.delay, short_url, hook)

    @patch('addnow.apps.tracker.trim.TrimService.get_hooks_count')
    @patch('addnow.apps.tracker.trim.TrimService.create_hook')
    @log_capture()
    def test__add_hook_when_there_is_hook(self, create_hook, get_hooks_count, log_data):
        get_hooks_count.return_value = 1
        short_url = 'http://test.com/short'
        hook = 'http://testserver/click/134/sharing-buttons?service=facebook'

        tasks.add_hook.delay(short_url, hook, self.trim_service)
        self.assertFalse(create_hook.called)
        log_data.check(
            (
                'addnow.apps.tracker.tasks',
                'INFO',
                'Trying to add hook: %s' % hook
            ),
            (
                'addnow.apps.tracker.tasks',
                'INFO',
                'Hook is already provided for url %s' % short_url
            )
        )
