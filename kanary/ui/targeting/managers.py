from django.db.models import Manager
from ui.targeting.targetcache import TargetCache


class TargetTreeManager(Manager):

    """
    Manager for :class:`ContentCategory`.

    You should define your custom QuerySets here.
    """

    def into_tree(self):
        """
        Returning tree structure for given model.
        """
        main_categories = self.filter(parent__isnull=True)

        return [
            rn.recursive_node_to_dict(rn) for rn in main_categories
        ]

    def representants(self):
        return self.all()


class TargetTreeValueManager(Manager):

    def get_multi_pk(self, exchange, dimension, values):
        """
        Read primary key from cache, or if not present from database.

        .. warning::

            It's rather impossible to get new segment during system life.
            To limit the number of database hit, if we won't find it in dimension table,
            we just set an 0 for it in cache and replace it with None in cache_values instead.

            We don't set None, since it's the value returned by cache if value isn't set.

        :param str exchange: exchange code
        :param str dimension: dimension name
        :param list values: category values for given exchange

        :returns: dictionary consisting of values and corresponding primary keys
        :rtype: dict
        """

        cache_values = TargetCache.multi_get_category_pk(
            exchange, values
        )
        for value, cache_val in cache_values.iteritems():
            if cache_val is not None:
                continue

            # This models just read primary keys
            try:
                category_val = self.get(name=value, exchange=exchange)
                TargetCache.set_category_pk(exchange, value, category_val.pk)
                cache_values[value] = category_val.pk
            except self.model.DoesNotExist:
                TargetCache.set_category_pk(exchange, value, 0)

        return cache_values


class SegmentManager(Manager):

    def get_multi_pk(self, exchange, dimension, values):
        """
        Read primary keys from cache, or if not present from database.

        .. note::

            segments are returned from appnexus only at the moment.

        .. warning::

            It's rather impossible to get new segment during system life.
            To limit the number of database hit, if we won't find it in dimension table,
            we just set an 0 for it in cache and replace it with None in cache_values instead.

            We don't set None, since it's the value returned by cache if value isn't set.

        :param str exchange: exchange code
        :param str dimension: dimension name
        :param list values: segment values for given exchange

        :returns: dictionary consisting of values and corresponding primary keys
        :rtype: dict
        """
        # only appnexus segments are available.
        if not exchange == 'appnexus':
            return {}

        dimension = self.model.DIMENSION

        cache_values = TargetCache.multi_get_segment_pk(
            exchange, dimension, values
        )

        for value, cache_val in cache_values.iteritems():
            if cache_val is not None:
                continue

            # This models just read primary keys
            try:
                segment_val = self.get(appnexus_id=value)
                TargetCache.set_segment_pk(exchange, dimension, value, segment_val.pk)
                cache_values[value] = segment_val.pk
            except self.model.DoesNotExist:
                TargetCache.set_segment_pk(exchange, dimension, value, 0)

        return cache_values

    def representants(self):
        return self.all()


class SegmentTreeManager(SegmentManager, TargetTreeManager):
    pass
