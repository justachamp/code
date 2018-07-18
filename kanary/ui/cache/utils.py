from contextlib import contextmanager

import redis
from django.conf import settings


class CacheConnector(object):

    """Lazy redis connections."""

    def __init__(self):
        """Initialize cache connection dictionary"""
        self._cache_conn = {}

    def __getitem__(self, redis_name):
        """Read and connect if necessary to proper redis server."""
        try:
            cache_connection = self._cache_conn[redis_name]
        except KeyError as e:
            if redis_name not in settings.REDIS:
                raise e

            pool = redis.ConnectionPool(**settings.REDIS[redis_name])
            cache_connection = redis.Redis(connection_pool=pool)
            self._cache_conn[redis_name] = cache_connection

        return cache_connection


cache_conn = CacheConnector()


@contextmanager
def redis_pipes_execute(connections):
    pipes = dict((name, r.pipeline()) for name, r in connections.iteritems())
    yield pipes
    for pipe in pipes.values():
        pipe.execute()
