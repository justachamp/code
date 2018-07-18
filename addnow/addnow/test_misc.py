"""
This file contains miscellaneous tests that cannot be put in any tests category
and don't deserve their own modules.
"""

import subprocess
import logging

from django.test import TestCase
from django.http.request import HttpRequest

from ipware.ip import get_real_ip
from nose.plugins.attrib import attr
from mock import patch, MagicMock

from addnow.apps.accounts.factories import SiteFactory
from addnow.cache import SiteSettingsCache, SocialCountersCache, GeoIpCache, DigestCache, TrimFailCache

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestMisc(TestCase):

    @attr('pep8')
    def test_code_with_pylama(self):
        """
        Checks code syntax with pylama.
        """
        status = subprocess.call(['pylama'])
        assert status == 0

    def test__cache_wrapper__meta(self):
        key = dict(site_id=1)

        delete_dict = dict(site_id=1)
        SiteSettingsCache.delete(delete_dict)

        self.assertIsNone(SiteSettingsCache.get(key))
        self.assertIsNone(SiteSettingsCache.set(key, 1, timeout=10))
        self.assertFalse(SiteSettingsCache.add(key, 2))
        self.assertEqual(SiteSettingsCache.get(key), 1)
        self.assertIsNone(SiteSettingsCache.delete(key))
        self.assertIsNone(SiteSettingsCache.get(key))

    @patch('addnow.cache.django_cache')
    def test__social_counters_cache__delete_prefix(self, django_cache):
        """
        Standard django's cache doesn't have `delete_pattern` method
            which is comes from `django-redis`
        """
        SocialCountersCache.delete_pattern(dict(site_id=1))

        django_cache.delete_pattern.assert_called_once_with('1:counters:*')

    @patch('addnow.cache.django_cache')
    def test__social_counters_cache__url_hash(self, django_cache):
        key = dict(site_id=1, url='http://test.com/')

        SocialCountersCache.get(key)

        django_cache.get.assert_called_once_with('1:counters:2f0bdb1d4987309e304ad0d7f982a37791fb06d4')

    @patch('addnow.cache.django_cache')
    def test__site_settings__build_key(self, django_cache):
        SiteSettingsCache.get(dict(site_id=1))

        django_cache.get.assert_called_once_with('1:settings')

    @patch('addnow.cache.django_cache')
    def test__geo_ip_cache__delete(self, django_cache):
        """
        Standard django's cache doesn't have `delete_pattern` method
            which is comes from `django-redis`
        """
        GeoIpCache.delete(dict(ip='8.8.8.8'))
        django_cache.delete.assert_called_once_with('geoip:8.8.8.8')

    @patch('addnow.cache.django_cache')
    def test__geo_ip_cache__build_key(self, django_cache):
        GeoIpCache.get(dict(ip='8.8.8.8'))
        django_cache.get.assert_called_once_with('geoip:8.8.8.8')

    @patch('addnow.cache.django_cache')
    def test__digest_cache__delete(self, django_cache):
        """
        Standard django's cache doesn't have `delete_pattern` method
            which is comes from `django-redis`
        """
        q = dict(site_id=1, begin_date='2015-04-03 00:00:00', end_date='2015-04-04 00:00:00', aggregation='day')
        DigestCache.delete(q)
        django_cache.delete.assert_called_once_with('1:digest:2015-04-03 00:00:00_2015-04-04 00:00:00_day')

    @patch('addnow.cache.django_cache')
    def test__digest_cache__build_key(self, django_cache):
        q = dict(site_id=1, begin_date='2015-04-03 00:00:00', end_date='2015-04-04 00:00:00', aggregation='day')
        DigestCache.get(q)
        django_cache.get.assert_called_once_with('1:digest:2015-04-03 00:00:00_2015-04-04 00:00:00_day')

    @patch('addnow.cache.django_cache')
    def test__trim_fail_cache__build_key(self, django_cache):
        q = dict(site=1, )
        TrimFailCache.get(q)
        django_cache.get.assert_called_once_with('1:trim_fail')

    @patch('addnow.cache.django_cache')
    def test__trim_fail_cache__delete(self, django_cache):
        """
        Standard django's cache doesn't have `delete_pattern` method
            which is comes from `django-redis`
        """
        q = dict(site=1)
        TrimFailCache.delete(q)
        django_cache.delete.assert_called_once_with('1:trim_fail')

    @patch('addnow.cache.SiteSettingsCache.set', MagicMock())
    def test_cache_get_config(self):
        site = SiteFactory()
        config = SiteSettingsCache.get_config(site.pk)
        self.assertEqual(config, site.get_config())
        original_config = config.copy()
        del config['hash_id']
        # It should regenerate hash_id in case of old cache
        with patch('addnow.cache.SiteSettingsCache.get', MagicMock(return_value=config)):
            self.assertEqual(SiteSettingsCache.get_config(site.pk), original_config)

        # It should not call the method class
        with patch('addnow.cache.SiteSettingsCache.get', MagicMock(return_value=original_config)):
            with patch('addnow.apps.accounts.models.Site.get_config') as site_config:
                SiteSettingsCache.get_config(site.pk)
                self.assertFalse(site_config.called)

        # It should call the method class
        with patch('addnow.cache.SiteSettingsCache.get', MagicMock(return_value=None)):
            with patch('addnow.apps.accounts.models.Site.get_config') as site_config:
                SiteSettingsCache.get_config(site.pk)
                self.assertTrue(site_config.called)

    def test_is_valid_ip(self):
        """ The 1.x IP should be taken instead of 70.x
        """
        request = HttpRequest()
        request.META = {
            'HTTP_X_FORWARDED_FOR': '1.39.32.155, 70.39.186.196'
        }
        ip = get_real_ip(request)
        self.assertEqual(ip, '1.39.32.155')
