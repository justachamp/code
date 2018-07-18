from etc import redis_keys
from ui.cache.base_models import CacheMap
from adserving.adserver.xsd import seconds_to_xs_time


def identity(obj):
    """
    Function returns passed parameter.
    """
    return obj


class CreativeCacheMap(CacheMap):

    abstract = True  # Don't map directly, use subclasses.
    alias = 'creative'

    observes = {
        'storage.Creative': {
            'relation': identity,
        },
        'storage.CreativeImage': {
            'relation': identity,
        },
        'storage.CreativeFlash': {
            'relation': identity,
        },
        'storage.CreativeVideo': {
            'relation': identity
        }
    }

    connections = 'adserver',

    key_obj = redis_keys.ads

    def mapped(self):
        # adid equals cid since creative can be in multiple ads
        return {
            'adid': str(self.creative.public_id),
            'cid': str(self.creative.public_id),
            'w': self.creative.width,
            'h': self.creative.height,
            'landing_sites': self.creative.landing_sites_ratios,
            'type': self.creative.type
        }


class CreativeFlashCacheMap(CreativeCacheMap):

    """It's needed by Cache filler, even though it isn't called later on."""
    abstract = False


class CreativeImageCacheMap(CreativeCacheMap):

    """It's needed by Cache filler, even though it isn't called later on."""
    abstract = False


class CreativeVideoCacheMap(CreativeCacheMap):

    """
    Extends base CreativeCacheMap by adding informations about Video media-data
    extracted from LiveRail service.
    """

    abstract = False

    def mapped(self):

        ad_info = super(CreativeVideoCacheMap, self).mapped()
        ad_info['adname'] = self.creative.name
        ad_info['duration'] = seconds_to_xs_time(self.creative.duration or 0)
        ad_info['mediafiles'] = self.creative.media_variants
        ad_info['mediafiles_secure'] = self.creative.media_variants_secure
        return ad_info
