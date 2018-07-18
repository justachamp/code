import hashlib

from django.core.cache import cache as django_cache
from django.shortcuts import get_object_or_404

from addnow.apps.accounts.models import Site


class CacheWrapperMeta(type):

    def __getattr__(cls, class_method):
        def django_cache_func_partial(key, *args, **kwargs):
            return getattr(django_cache, class_method)(
                getattr(cls, 'build_key')(class_method, **key), *args, **kwargs
            )
        return django_cache_func_partial


class SocialCountersCache(object):
    """
    Usage:
        SocialCountersCache.get(dict(site_id=2, url='url'))
        SocialCountersCache.set(dict(site_id=2, url='url'), data, timeout=0)
        SocialCountersCache.delete(dict(site_id=2, url='url'))
        SocialCountersCache.delete_pattern(dict(site_id=2))
    """
    __metaclass__ = CacheWrapperMeta

    @classmethod
    def build_key(cls, class_method, **kwargs):
        url = kwargs.pop('url', None)

        if url is not None:
            kwargs['url_hash'] = hashlib.sha1(url).hexdigest()
        else:
            assert class_method == 'delete_pattern'
            kwargs['url_hash'] = '*'

        return '{site_id}:counters:{url_hash}'.format(**kwargs)


class SiteSettingsCache(object):
    """
    Usage:
        SiteSettingsCache.get(dict(site_id=2))
        SiteSettingsCache.set(dict(site_id=2), data, timeout=0)
        SiteSettingsCache.delete(dict(site_id=2))
    """
    __metaclass__ = CacheWrapperMeta

    @classmethod
    def build_key(cls, _, **kwargs):
        return '{site_id}:settings'.format(**kwargs)

    @classmethod
    def get_config(cls, site_id):
        key = dict(site_id=site_id)
        config = cls.get(key)
        if config is None or not config.get('hash_id'):
            config = get_object_or_404(Site, pk=site_id).get_config()
            SiteSettingsCache.set(key, config, timeout=None)

        return config


class SiteTrimSettingsCache(object):
    """
    Usage:
        SiteTrimSettingsCache.get(dict(site_id=2))
        SiteTrimSettingsCache.set(dict(site_id=2), data, timeout=0)
        SiteTrimSettingsCache.delete(dict(site_id=2))
    """
    __metaclass__ = CacheWrapperMeta

    @classmethod
    def build_key(cls, _, **kwargs):
        return '{site_id}:trim_key'.format(**kwargs)

    @classmethod
    def get_key(cls, site_id):
        key = dict(site_id=site_id)
        trim_key = cls.get(key)
        if trim_key is None:
            trim_key = get_object_or_404(Site, pk=site_id).trim_api_key
            SiteTrimSettingsCache.set(key, trim_key, timeout=None)

        return trim_key


class GeoIpCache(object):
    """
    Usage:
        GeoIpCache.get(dict(ip='8.8.8.8'))
        GeoIpCache.set(dict(ip='8.8.8.8'), data, timeout=0)
        GeoIpCache.delete(dict(ip='8.8.8.8'))
    """
    __metaclass__ = CacheWrapperMeta

    @classmethod
    def build_key(cls, _, **kwargs):
        return 'geoip:{ip}'.format(**kwargs)


class DigestCache(object):
    """
    Usage:
    DigestCache.get(dict(site_id=1, begin_date='2015-04-01 00:00:00',
                         end_date='2015-04-02 00:00:00', aggregation='hour'))
    DigestCache.set(dict(site_id=1, begin_date='2015-04-01 00:00:00',
                         end_date='2015-04-02 00:00:00', aggregation='hour'),
                         data, timeout=0)
    DigestCache.delete(dict(site_id=1, begin_date='2015-04-01 00:00:00',
                            end_date='2015-04-02 00:00:00', aggregation='hour'))
    """
    __metaclass__ = CacheWrapperMeta

    @classmethod
    def build_key(cls, _, **kwargs):
        return '{site_id}:digest:{begin_date}_{end_date}_{aggregation}'.format(**kwargs)


class TrimFailCache(object):
    """
    Usage:
    TrimFailCache.get({'site': site_id})
    TrimFailCache.set({'site': site_id, 'trim_fail': true, 'first_fail': datetime.now(), 'last_try': datetime.now()})
    TrimFail.delete({'site': site_id})
    """
    __metaclass__ = CacheWrapperMeta

    @classmethod
    def build_key(cls, _, **kwargs):
        return '{site}:trim_fail'.format(**kwargs)
