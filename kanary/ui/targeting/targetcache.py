from hashlib import md5

from django.core.cache import get_cache
from django.utils.encoding import force_bytes

from etc.config import settings
from stats import cache


def silent_fail(fn):
    '''
    Return None if the cache is disabled.
    '''
    def wrapped(cls, *args, **kwargs):
        if settings.targeting_cache_enabled is False:
            return None
        return fn(cls, *args, **kwargs)
    return wrapped


class TargetCache(object):
    '''
    Static class used by managers to connect to targeting cache.
    Fails silently if the cache is disabled.
    '''

    tv_cache = get_cache('targetvalues')

    @classmethod
    def make_key(cls, prefix, *args):
        """
        Generate key for cache based on passed args.

        :param str prefix: redis key prefix
        :param list args: list of strings or iterables containing strings.
            The iterable will be deeply mapped so that each string gets converted
            to unicode and each tuple gets converted to list.

        :returns: generated key
        :rtype: str
        :returns: md5 hash of given args
        """

        def normalize(item):
            '''
            Deeply map the iterable converting iterable and nested iterables to list
            and casting everything else to unicode.
            :raises (TypeError, UnicodeDecodeError): if cannot convert to unicode
            :return: list of nested lists and unicode
            :rtype: list
            '''
            if hasattr(item, '__iter__'):
                # Map implicitly converts the iterable to list.
                # Leaf nodes will be normalized recursively.
                return map(normalize, item)
            else:
                # Not an iterable. Leaf node. Strings like 'aaa' and u'aaa'
                # are supposed to be the same. Also, '1' and 1 are treated the same
                # but it does not bother us.
                return force_bytes(item)

        normalized = normalize(*args)
        key = repr(normalized)
        return '{0}:{1}'.format(prefix, md5(key).hexdigest())

    @classmethod
    @silent_fail
    def get(cls, prefix, *key_args):
        cache.targetvalues.get.increment()

        got = cls.tv_cache.get(cls.make_key(prefix, key_args))

        if got is None:
            cache.targetvalues.cache_miss.increment()
        return got

    @classmethod
    def multi_get(cls, prefix, constant_part, variables):
        """
        Get multiple keys stored in redis if the cache is enabled.

        :param str prefix: cache prefix
        :param list constant_part: part that's constant for all requested keys.
        :param list variables: list of changing elements for keys.

        .. note::

            constant_part is usually something like [exchange, dimension],
            while variables would be [('US',), ('US', 'NY'), ('US', 'NY', 'NY')]

        :return: dictionary with corresponding variables and cache values or Nones
            instead of values if the cache is disabled
        :rtype: dict
        """
        keys = []
        key_value_map = {}
        for variable in variables:
            elements = list(constant_part)
            elements.append(variable)
            key = cls.make_key(prefix, elements)
            key_value_map[variable] = key
            keys.append(key)

        if settings.targeting_cache_enabled is True:
            results = cls.tv_cache.get_many(keys)
        else:
            # No cache, respond with Nones.
            results = {k: None for k in key_value_map.values()}
        return {v: results.get(key_value_map[v]) for v in variables}

    @classmethod
    @silent_fail
    def set(cls, prefix, *args):
        key_args, val = args[0:-1], args[-1]
        return cls.tv_cache.set(cls.make_key(prefix, key_args), val)

    @classmethod
    @silent_fail
    def delete(cls, prefix, *key_args):
        return cls.tv_cache.delete(cls.make_key(prefix, key_args))

    # Target values cache methods
    @classmethod
    def get_target_pk(cls, exchange, category, value_list):
        return cls.get('target_value', exchange, category, value_list)

    @classmethod
    def multi_get_target_pk(cls, exchange, category, values):
        """
        Get multiple primary keys for given target_value values.

        :param str exchange: exchange name
        :param str category: dimension name
        :param list values: list of all values to query

        :return: dictionary of corresponding values and primary keys
        :rtype: dict
        """
        return cls.multi_get('target_value', [exchange, category], values)

    @classmethod
    def set_target_pk(cls, exchange, category, value_list, pk):
        cls.set('target_value', exchange, category, value_list, pk)

    @classmethod
    def delete_target_pk(cls, exchange, category, value_list):
        cls.delete('target_value', exchange, category, value_list)

    # Publisher target cache methods for values
    @classmethod
    def get_publisher_pk(cls, exchange, value):
        return cls.get('publisher_value', exchange, value)

    @classmethod
    def multi_get_publisher_pk(cls, exchange, values):
        """
        Get multiple primary keys for given publisher values.

        :param str exchange: exchange name
        :param list values: list of all values to query

        :return: dictionary of corresponding values and primary keys
        :rtype: dict
        """
        return cls.multi_get('publisher_value', [exchange], values)

    @classmethod
    def set_publisher_pk(cls, exchange, value, pk):
        cls.set('publisher_value', exchange, value, pk)

    @classmethod
    def delete_publisher_pk(cls, exchange, value):
        cls.delete('publisher_value', exchange, value)

    # Publisher target cache methods for pks
    @classmethod
    def get_publisher_info(cls, pk):
        return cls.get('publisher_pk', pk)

    @classmethod
    def set_publisher_info(cls, pk, info):
        cls.set('publisher_pk', pk, info)

    @classmethod
    def delete_publisher_info(cls, pk):
        cls.delete('publisher_pk', pk)

    # Content category target cache methods for values
    @classmethod
    def get_category_pk(cls, exchange, value):
        return cls.get('content_category', exchange, value)

    @classmethod
    def multi_get_category_pk(cls, exchange, values):
        """
        Get multiple primary keys for given category values.

        :param str exchange: exchange name
        :param list values: list of all categories to query

        :return: dictionary of corresponding categories and primary keys
        :rtype: dict
        """
        return cls.multi_get('content_category', [exchange], values)

    @classmethod
    def set_category_pk(cls, exchange, value, pk):
        cls.set('content_category', exchange, value, pk)

    @classmethod
    def delete_category_pk(cls, exchange, value):
        cls.delete('content_category', exchange, value)

    # Segment target cache methods for values,
    @classmethod
    def get_segment_pk(cls, exchange, dimension, value):
        """
        :param str exchange: exchange name
        :param str dimension: dimension name, used to differentiate appnexus segments
            (they use one pool if ids, but different dimension)
        :param str value: appnexus segment identification
        """
        return cls.get('segment', exchange, dimension, value)

    # Segment target cache methods for values,
    @classmethod
    def multi_get_segment_pk(cls, exchange, dimension, values):
        """
        Get multiple primary keys for given publisher values.

        :param str exchange: exchange name
        :param str dimension: dimension name, used to differentiate appnexus segments
            (they use one pool if ids, but different dimension)
        :param list values: list of appnexus segment identifications

        :return: dictionary of corresponding sgments and primary keys
        :rtype: dict
        """
        return cls.multi_get('segment', [exchange, dimension], values)

    @classmethod
    def set_segment_pk(cls, exchange, dimension, value, pk):
        """
        :param str exchange: exchange name
        :param str dimension: dimension name, used to differentiate appnexus segments
            (they use one pool if ids, but different dimension)
        :param str value: appnexus segment identification
        :param in pk: primary key for given segment in given segment-dimension
        """
        cls.set('segment', exchange, dimension, value, pk)

    @classmethod
    def delete_segment_pk(cls, exchange, dimension, value):
        """
        :param str exchange: exchange name
        :param str dimension: dimension name, used to differentiate appnexus segments
            (they use one pool if ids, but different dimension)
        :param str value: appnexus segment identification
        """
        cls.delete('segment', exchange, dimension, value)
