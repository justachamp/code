'''
Module contains base classes for cache mappings-related classes.

Dictionary:
    pipe - redis pipeline
    trigger_change - methods that maps objects from db into cache
    cache_is_dirty - field of objects to be re-mapped into cache
            if True - objects in cache is valid
            if False - object needs to be mapped into cache
'''

import logging
from functools import partial
from datetime import datetime
from importlib import import_module

import cPickle
from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet
from django.dispatch import receiver
from django.db.models.signals import pre_save, m2m_changed
from django.db import transaction
from django.core.exceptions import FieldError

from ui.common.models import NotRemovable, LatestUpdate
from ui.cache.utils import cache_conn, redis_pipes_execute

log = logging.getLogger('django')
cpickledumps = partial(cPickle.dumps, protocol=2)


class CacheMapped(NotRemovable):

    ''' The base class for Model (Django) classes that can be
    inserted into cache '''

    cache_is_dirty = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True

    _MapClass = None
    cache_map = None
    _observing = {}

    def __init__(self, *args, **kwargs):
        super(CacheMapped, self).__init__(*args, **kwargs)

        cls = self.__class__
        self.cache_map = cls.MapClass()(self)
        cls._attach_observed()

    def cache_trigger_change(self, *args, **kwargs):
        return self.cache_map.trigger_change(*args, **kwargs)

    @property
    def cache_is_valid(self):
        return not self.cache_is_dirty

    @classmethod
    def _cache_dirty_dates(cls, prev):
        ''' Returns QuerySet with cls objects which observed_date_fields
        could make this object dirty since previous check.
        Arguments:
            prev (datetime.datetime) - previous check if date field outdated
        Returns:
            (models.query.QuerySet) - class objects with outdated
                                      observes_date_fields
        '''
        now = datetime.utcnow()
        q = lambda field: Q(**{field + '__gt': prev, field + '__lte': now})

        query = cls.objects.none()
        for field in cls.MapClass().observes_date_fields:
            sub_q = cls.objects.filter(q(field))
            query = sub_q if query is None else query | sub_q

        return query

    @classmethod
    @transaction.atomic
    def cache_dirtify_dates(cls):
        ''' Marks certain objects with observes_date_fields as dirty.
        The object can be dirty if one of date fields on previous check showed
        time in the future, and by now this thime is in past. In such case the
        method will mark them as dirty.
        '''
        MapClass = cls.MapClass()

        with LatestUpdate.by_name(MapClass.__name__) as prev:
            cls._cache_dirty_dates(prev.latest_update) \
                .filter(cache_is_dirty=False) \
                .update(cache_is_dirty=True)

    @classmethod
    @transaction.atomic
    def cache_trigger_mappings(cls, force=False):
        ''' Calls cache_trigger_change() for every dirty object
        Arguments:
            force - if True triggers all instances (not only dirty)
        '''
        cls.cache_dirtify_dates()

        connections = cls._init_cache_connections()
        objects = cls.objects.all()
        if not force:
            objects = objects.filter(cache_is_dirty=True)

        count = 0
        for count, obj in enumerate(objects, 1):
            obj.cache_trigger_change(connections, force=force)

        if count > 0:
            cls.MapClass().class_mapped()

        return count

    @classmethod
    def _init_cache_connections(cls):
        return cls.MapClass().init_cache_connections()

    @classmethod
    def MapClass(cls):
        if not cls.__dict__.get('_MapClass'):  # check own property, not inherited
            package = import_module(cls.__module__).__package__
            mapping = import_module('%s.cache_mapping' % package)
            cls._MapClass = mapping.__dict__['%sCacheMap' % cls.__name__]
        return cls._MapClass

    @classmethod
    def _attach_observed(cls):
        map_cls = cls.MapClass()
        if map_cls in cls._observing:
            return  # skips already observed classes

        for sender, definition in map_cls.observes.items():
            sender = models.get_model(*sender.split('.'))
            cls._attach_sender(sender,
                               definition['relation'],
                               definition.get('fields', []))

        for sender, relation in map_cls.observes_through.items():
            module, model, m2m_field = sender.split('.')
            sender = models.get_model(module, model)
            through = getattr(sender, m2m_field).through
            cls._attach_sender_m2m(through, relation)

        cls._observing[map_cls] = True

    @classmethod
    def _attach_sender(cls, sender_cls, relation, fields=[]):
        '''
        Attaches pre_save signal to sender_cls which dirtifies
        all objects under relation.

        :param sender_cls: class that sends signal (one we pin it to)
        :param callable relation: callable returning queryset for relation
            to update
        :param list fields: fields which change on sender_cls
            should trigger dirtification of related object,
            can be empty, in which case all fields will trigger dirtification

        .. warning::

            passing fields argument would reqiure sender_cls to inherit from
            :class:`ui.common.models.KanaryDirtyFieldsMixin`
            or provide `get_dirty_fields` method
        '''

        dispatch_uid = '{receiver}-CacheMapped-{sender}-{fields}'.format(
            receiver=cls.__name__.lower(),
            sender=sender_cls.__name__.lower(),
            fields=','.join(fields)
        )

        fields = set(fields)

        @receiver(pre_save, sender=sender_cls, weak=False,
                  dispatch_uid=dispatch_uid)
        def on_pre_save(sender, instance, **kwargs):
            related = relation(instance)

            if fields:
                if not fields.intersection(instance.get_dirty_fields().keys()):
                    return

            if isinstance(related, QuerySet):
                related.update(cache_is_dirty=True)
            else:
                related.__class__.objects.filter(pk=instance.pk) \
                    .update(cache_is_dirty=True)
                related.cache_is_dirty = True

    @classmethod
    def _attach_sender_m2m(cls, sender_cls, relation):
        '''
        Attaches methods to m2m_changed signal of sender models.

        :param sender_cls: class that sends signal (one we pin it to)
        :param str relation: relation pointing to observed class the m2m
            field is defined on

        '''

        @receiver(m2m_changed, sender=sender_cls, weak=False)
        def on_m2m_changed(sender, instance, action, reverse, **kwargs):
            if action not in ('post_add', 'post_remove', 'post_clear'):
                return

            if action == 'post_clear' and reverse:
                raise FieldError("Unable to update cache."
                                 "Don't use clear() on cached objects.")

            if reverse:
                relation_pks = kwargs['pk_set']
            else:
                relation_pks = [instance.pk]

            cls.objects.filter(
                **{relation + '__in': relation_pks}
            ).update(cache_is_dirty=True)


class CacheMap(object):
    """
    Base Class defining mapping from django model into cache
    By convention there should be CampaignCacheMap inside cache_mapping.py
    if there is class Campaign(CacheMapped) inside models.py.
    """

    abstract = None
    """
    All subclasses that set the `abstract` property to True will not be used for mapping.
    Abstractness will not be inherited - all classes that need it must set it True for themselves.
    """

    observes = {}
    """
    defining observed Django Models:
    observes = {
        'campaign.Campaign': lambda campaign: campaign,
        'campaign.Strategy': lambda strategy: strategy.campaign,
        'campaign.Advert': lambda advert: advert.strategy.campaign,
    }
    where
       - key is observed class (sender)
       - value is lambda which takes instance of class of key
         and tries to get the base object - in example - campaign
    """

    observes_through = {}
    """
    M2M fields are observed using observes_through dict
    e.g.
    observes_through = {
        'campaign.Strategy': 'targeting_values',
    }
    """

    observes_date_fields = []
    """
    Changes of date_time fields - cron check if some DateTimeField has expired. e.g. for Strategy:

    .. code-block:: python

        observes_date_fields = ['campaign__start_UTC', 'campaign__end_UTC']

    """

    key_obj = None
    """Cache key of hash where object is inserted."""

    alias = None
    """Custom defined alias name for instance."""

    connections = NotImplemented
    """Cache connection initializers, mappings will be fired for each of connection."""
    connection_serializers = {}
    """Set special data serializer for connections. Defaults to cPickle.dumps with protocol=2."""

    publishing_connections = {}
    '''
    Publishing connections used for mapping data. Allows to instantly publish
    through pubsub changed data to required channel on given connection.

    Format is as follows:

    .. code-block:: python

        {'connection_name': (channel_add, channel_del)}

    - channel add - will be used to publish mapped message returned by
        appropriate mapped_method.
    - channel_del - fired if appropriate mapped method returns None.
        Will be used to push deleted object's id to inform about change.
    '''

    def __init__(self, instance):
        self._instance = instance
        alias = self.alias or\
            instance._meta.verbose_name.lower().replace(' ', '_')
        setattr(self, alias, instance)

    def mapped(self):
        ''' Returns object that can be cPickle-dumped.
        If overriden - result of this method will be added into all connections
        Usage:

            - one mapping:

                connections = 'redisX', 'redisY'

                def mapped(self):
                    return {
                        'image_width' self.image.width,
                    }

        or:
            - different mappings per connection:

                connections = 'redisX', 'redisY'

                def mapped_redisX(self):
                    return {'use': True}

                def mapped_redisY(self):
                    return {'use': False}

        '''
        return NotImplemented

    @classmethod
    def class_mapped(cls):
        '''
        This method will be fired when at least one object from class will be dirty.
        '''
        return

    @property
    def id(self):
        ''' Returns id of cache object. Can be overridden.
        In most cases it's public_id and not django pk. '''
        return self._instance.public_id

    @transaction.atomic
    def trigger_change(self, connections=None, force=False):
        ''' Method checks if objects needs to be revalidated inside cache
        and then updates (removes or adds) it into cache. '''
        instance = self._instance

        if instance.cache_is_valid and force is False:
            return

        with redis_pipes_execute(connections):
            self._on_change(connections)

        instance.__class__.objects.filter(pk=instance.pk) \
            .update(cache_is_dirty=False)
        instance.cache_is_dirty = False

    def _on_change(self, redis_pipes):
        self.on_change_cleanup(redis_pipes)
        self._change_object(redis_pipes)
        self.on_change_add(redis_pipes)

    def on_change_cleanup(self, redis_pipes):
        return

    def on_change_add(self, redis_pipes):
        return

    def _change_object(self, redis_pipes):
        ''' Refresh object in cache (hash of cache objects)'''
        if not self.key_obj:
            return

        mapped = self.mapped()
        for connection_name, pipe in redis_pipes.items():
            pipe_mapped = mapped
            if hasattr(self, 'mapped_' + connection_name):
                pipe_mapped = getattr(self, 'mapped_' + connection_name)()

            serializer = self.connection_serializers.get(
                connection_name, cpickledumps
            )

            # return none, to clean redis
            if pipe_mapped is None:
                pipe.hdel(self.key_obj, self.id)
                # publishing message
                if connection_name in self.publishing_connections:
                    pipe.publish(
                        self.publishing_connections[connection_name][1],
                        serializer(self.id)
                    )

            elif pipe_mapped != NotImplemented:
                serialized_data = serializer(pipe_mapped)
                pipe.hset(self.key_obj, self.id, serialized_data)
                # publishing message
                if connection_name in self.publishing_connections:
                    pipe.publish(
                        self.publishing_connections[connection_name][0],
                        serialized_data
                    )

    @classmethod
    def init_cache_connections(cls):
        return dict((name, cache_conn[name]) for name in cls.connections)
