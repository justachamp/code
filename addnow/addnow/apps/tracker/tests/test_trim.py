# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from testfixtures import log_capture
from mock import MagicMock, patch

from addnow.apps.accounts import constants
from addnow.apps.tracker.trim import TrimService
from addnow.apps.tracker.exceptions import TrimAPIException


class TestTrim(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestTrim, cls).setUpClass()
        cls.trim_service = TrimService()

    def _test_create_shortcut(self, log_data, long_url, site_id, response, service=None, vanity_domain=None):
        keyword, url = self.trim_service.create_shortcut(long_url, site_id, constants.Tools.COPY_PASTE.value,
                                                         service=service, vanity_domain=vanity_domain)
        self.assertEqual(keyword, response['keyword'])
        self.assertEqual(url, response['url'])
        log_data.check()

    @patch('addnow.apps.tracker.trim.TrimService.http_request')
    @log_capture()
    def test__create_shortcut(self, http_request, log_data):
        long_url = 'http://verylongsite.com'
        site_id = 1
        vanity_domain = 'test.local'

        # Regular case
        response = {'keyword': 'Az34w', 'url': 'http://tr.im/Az34w'}
        http_request.return_value = response
        self._test_create_shortcut(log_data, long_url, site_id, response)
        self._test_create_shortcut(log_data, long_url, site_id, response,
                                   service=constants.SOCIAL_SERVICE_FACEBOOK)
        self._test_create_shortcut(log_data, long_url, site_id, response,
                                   vanity_domain=vanity_domain)
        self._test_create_shortcut(log_data, long_url, site_id, response,
                                   service=constants.SOCIAL_SERVICE_FACEBOOK,
                                   vanity_domain=vanity_domain)

        # Wrong case
        response = {'keyword': 'Az34w'}
        http_request.return_value = response
        self.assertRaises(TrimAPIException, self.trim_service.create_shortcut, long_url, site_id,
                          constants.Tools.COPY_PASTE.value, service=constants.SOCIAL_SERVICE_FACEBOOK,
                          vanity_domain=vanity_domain)
        log_data.check(
            (
                'addnow.apps.tracker.trim',
                'ERROR',
                "Couldn't return data from response {u'keyword': u'%s'}" % response['keyword']
            )
        )

    @patch('addnow.apps.tracker.trim.TrimService.http_request')
    @log_capture()
    def test__create_hook(self, http_request, log_data):
        short_url = 'http://tr.im/Az34w'
        hook = 'http://test.com'

        # Regular case
        response = {'id': 'Az34w'}
        http_request.return_value = response
        hook_id = self.trim_service.create_hook(short_url, hook)
        self.assertEqual(hook_id, response['id'])
        log_data.check(
            (
                'addnow.apps.tracker.trim',
                'DEBUG',
                'Hook(%s) for short_url(%s) was created. Id is: %s' % (hook, short_url, response['id'])
            )
        )
        log_data.clear()

        # Wrong case
        response = {'blahblah': 'Az34w'}
        http_request.return_value = response
        hook_id = self.trim_service.create_hook(short_url, hook)
        self.assertIsNone(hook_id)
        log_data.check(
            (
                'addnow.apps.tracker.trim',
                'WARNING',
                'Hook(%s) for short_url(%s) was not created. Response was: %s' % (hook, short_url, response)
            )
        )

    def test__http_request(self):
        # Valid post
        with patch('requests.post') as post:
            with patch('requests.get', MagicMock()):
                self.trim_service.http_request('post', '1', '2')
                post.assert_called_once()
        # Valid get
        with patch('requests.post', MagicMock()):
            with patch('requests.get') as get:
                self.trim_service.http_request('get', '1', '2')
                get.assert_called_once()
        # Invalid exception in post
        with patch('requests.post', MagicMock(side_effect=Exception())):
            with patch('requests.get', MagicMock()):
                self.assertRaises(TrimAPIException, self.trim_service.http_request, 'post', '1', '2')
        # Invalid type
        with patch('requests.post', MagicMock()):
            with patch('requests.get', MagicMock()):
                self.assertRaises(TrimAPIException, self.trim_service.http_request, 'not_exist', '1', '2')
