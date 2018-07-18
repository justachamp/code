import logging

from django.core.cache import cache as dj_cache

from googleapiclient.discovery_cache import base

from addnow.apps.analytics.settings import DISCOVERY_DOC_TIMEOUT


# Get an instance of a logger
logger = logging.getLogger(__name__)


class Cache(base.Cache):
    """A cache with Django cache"""

    def __init__(self, max_age):
        """Constructor.

          Args:
            max_age: Cache expiration in seconds.
        """
        self._max_age = max_age

    def get(self, url):
        try:
            return dj_cache.get(url)
        except Exception as e:
            logger.warning(e, exc_info=True)

    def set(self, url, content):
        try:
            dj_cache.set(url, content, self._max_age)
        except Exception as e:
            logger.warning(e, exc_info=True)

cache = Cache(max_age=DISCOVERY_DOC_TIMEOUT)
