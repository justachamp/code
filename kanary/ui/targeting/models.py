import ast
from functools import partial

from django.db import IntegrityError
from django.db import models as m
from django.db.models import F, Q
from django.db.models.signals import post_save, pre_delete
from mptt.models import TreeForeignKey

from etc import dimensions
from etc.constants import separator, TARGETING_ADDITIONAL_DATA_COSTS
from bidrequest import segments
from ui.targeting.appnexus import AppNexusSegment
from ui.targeting.targetcache import TargetCache
from ui.targeting.managers import TargetTreeManager, TargetTreeValueManager, SegmentManager, SegmentTreeManager
from adserving.bidder.targeting.constants import PROXIMIC, PEER39, LOTAME


ExchangeField = partial(m.CharField, max_length=50, db_index=True, null=True)


class InvalidTargetValues(ValueError):

    ''' Indicates values passed to TargetMap are invalid. '''


class TargetValueQueryError(IntegrityError):
    pass


class TargetMap(object):

    '''Defined interface of a object which contains data about targeting,
    possible keys, etc.
    '''

    @classmethod
    def get_group_by_key(cls, key):
        for group, keys in dimensions.hierarchy.iteritems():
            if key in keys:
                return group

    @classmethod
    def unpack(cls, value):
        '''Tries to deserialize string into code friendly which contains
        data about targeted value.
        i.e. "Android;5.0" -> ["Android", "5.0"]'''
        if not isinstance(value, basestring):
            return value
        return map(lambda x: x or None, value.split(separator))

    @classmethod
    def family_line(cls, value):
        '''
        Unpack and join 'family lines' of TargetValues' strings, replacing
        empty hierarchy elements with 'Unknown'.

        >>> TargetMap.family_line('Android\x1d5.0')
        'Android - 5.0'
        >>> TargetMap.family_line('Android\x1d')
        'Android - Unknown'
        >>> TargetMap.family_line('DE\x1d\x1d')
        'DE - Unknown - Unknown'
        '''
        values = cls.unpack(value)
        if not values:
            return None
        values = map(lambda val: val or 'Unknown', values)  # Fill unknown fields.
        return u' - '.join(values)

    @classmethod
    def pack(cls, values):
        '''Tries to serialize list/iterable of values into db/string
        friendly format.
        i.e. ["Android", "5.0"] -> "Android;5.0"'''
        if not cls.is_valid(values):
            raise InvalidTargetValues(values)
        stripped_strings = map(lambda x: unicode(x or '').strip(), values)
        return separator.join(stripped_strings)

    @classmethod
    def is_valid(self, values):
        '''Checks if (unpacked) targeting value has un-empty/broken structure.
        By broken we mean list with only null values
        i.e. is_valid(["Android", "5.0"]) -> True
        is_valid(["Android", None]) -> True
        is_valid([None, None]) -> False
        is_valid([None]) -> False'''
        return not(all(map(lambda x: x is None, values))) if values else False


class ProfileValue(m.Model):

    class Meta:
        abstract = True

    @property
    def cache_keys(self):
        '''Dumps keys which are in close to bidder-friendly format, i.e.
        "country", "usa"'''
        return NotImplemented


class TargetValueManager(m.Manager):

    '''
    Glossary:
        - representant - TargetValue inserted from API or a by a human
          as a textual representation of other TargetValues
        - represented - TargetValue instance that has a representant
        - unrepresented - TargetValue with no representant
          (not to be mistaken with untranslated - TargetValue's value after
          untranslation process - see mapping of TargetValues to redis).
    '''

    def unrepresented(self, **kwargs):
        ''' Return QuerySet of target values that lack a representant. '''
        return self.filter(representant__pk=F('pk')).filter(**kwargs)

    def represented(self, **kwargs):
        ''' Return QuerySet of target values that have a representant. '''
        return self.filter(representant__isnull=False).exclude(
            representant__pk=F('pk')).filter(**kwargs)

    def representants(self):
        ''' Return QuerySet of representants. '''
        return self.filter(representant__isnull=True)

    def __getattr__(self, name):
        '''
        This makes Manager support shorter syntax for representants queries
        i.e. Smth.objects.representants_device_os returns representants of
        device os
        '''
        if name.startswith('representants_category_'):
            key = name.split('_', 2)[-1]
            return lambda: self.representants_category_X(key)
        raise AttributeError(name)

    def representants_category_X(self, category):
        return self.representants().filter(category=category)

    def get_unrepresented_values(self, exchange, category):
        '''
        Return unmoderated values for given exchange (code) and category.
        '''
        query = self.unrepresented(category=category, exchange=exchange)
        return map(lambda t: t.value_list, query)

    def create_representant(self, exchange, category, value):
        ''' Create representant.
        :param str exchange: exchange name
        :param str category: TargetValue category name
        :param list value: iterable of dimension values or Nones, but not
            Nones exclusively
        '''
        item = self.create(exchange=exchange, category=category,
                           value=TargetMap.pack(value))
        return item

    def get_or_create_representant(self, category, value, exchange=None,
                                   strict=True):
        '''
        Get the representant or create a new one.
        :param str category: TargetValue category name
        :param list value: iterable of dimension values or Nones, but not
            Nones exclusively
        :param str exchange: exchange name optional, defaults to None
        :param bool strict: if True, search will be performed only within
            representants, so TargetValue of any state may be returned.
            IF strict is False, method gets any object, or creates representant
            '''

        kwargs = {
            'category': category,
            'value': TargetMap.pack(value)
        }
        if exchange:
            kwargs['exchange'] = exchange

        q = self.representants() if strict else self
        try:
            item, _ = q.get_or_create(**kwargs)
        except IntegrityError:
            raise TargetValueQueryError(
                'Tried to get_or_create representant TargetValue when such '
                'unrepresented or represented exists: %s, %s, %s ' %
                (exchange, category, value))
        return item, _

    def create_unrepresented(self, exchange, category, value):
        '''
        Create new value with no representant.
        '''
        item = self.create(
            exchange=exchange, category=category, value=TargetMap.pack(value))

        item.representant = item
        item.save()
        return item

    def get_or_create_unrepresented(self, category, value, exchange,
                                    strict=True):
        '''
        Get or create new value with no representant.
        :param str category: TargetValue category name
        :param list value: iterable of dimension values or Nones, but not
            Nones exclusively
        :param (str, NoneType) exchange: exchange name optional
        :param bool strict: if True, search will be performed only within
            unrepresented TargetValues, so TargetValue of any state may
            be returned.
            IF strict is False, method gets any object, or creates represented
            value.
        '''
        q = self.unrepresented() if strict else self
        try:
            item, added = q.get_or_create(
                exchange=exchange, category=category,
                value=TargetMap.pack(value))
        except IntegrityError:
            raise TargetValueQueryError(
                'Tried to get_or_create unrepresented TargetValue when such '
                'representant or represented exists: %s, %s, %s ' %
                (exchange, category, value))

        # This if is just an optimisation.
        if added:
            item.representant = item
            item.save()

        return item, added

    def create_value_with_representant(self, values, representant):
        '''
        Create a new TargetValue for the given representant, keeping same
        exchange and category.
        :param values (list): new representant's values, eg.:
            ['USA', 'New York', 'Brooklyn']
        '''
        exchange_code = representant.exchange
        category = representant.get_category()

        represented, _ = self.get_or_create_unrepresented(
            category, values, exchange_code)
        represented.representant = representant
        represented.save()

        return represented

    def get_representant_object(self, exchange, category, values):
        '''
        Retrieves representant object for given value

        :param str exchange: exchange code
        :param str category: category which holds representant
        :param list values: list of represented values
        '''
        value = TargetMap.pack(values)
        try:
            item = (self.representants() | self.represented()).get(
                exchange=exchange, category=category, value=value)
            return item.representant if item.representant else item
        except TargetValue.DoesNotExist:
            return

    def get_representant_value_list(self, exchange, category, value):
        represented = self.get_representant_object(exchange, category, value)
        return represented.value_list if represented else None

    def get_representant_dict(self, exchange, category, value):
        represented = self.get_representant_object(exchange, category, value)
        return represented.value_dict if represented else None

    def create_value_with_custom_representant(
            self, exchange, category, represented_values, representant_values):
        '''
        Get or create representant if needed, add a new TargetValue represented
        by the representant.

        :param str exchange: exchange code
        :param str category: category name
        :param list represented_values: target value
        :param list representant_values: representant's value
        '''

        representant, _ = self.get_or_create_representant(
            category=category,
            value=representant_values,
            exchange=exchange
        )

        return self.create_value_with_representant(
            represented_values, representant
        )

    def make_all_representants(self):
        return self.update(representant=None)

    def get_or_create_multi_pk(self, exchange, category, values):
        """
        Get primary key corresponding to exchange, category and value.

        :param str exchange: exchange code
        :param str category: target value category
        :param list values: list of target value hierarchy values

        :returns: dictionary of values and corresponding primary keys
        :rtype: dict

        .. note::

            If value does not exists, it will be created!

        """

        cache_values = TargetCache.multi_get_target_pk(
            exchange, category, values
        )
        for value, cache_val in cache_values.iteritems():
            if cache_val is not None:
                continue

            try:
                tv, _ = self.get_or_create_representant(
                    category=category,
                    value=value,
                    exchange=exchange,
                    strict=False
                )
                TargetCache.set_target_pk(exchange, category, value, tv.pk)
                cache_values[value] = tv.pk
            except (InvalidTargetValues, TargetValueQueryError):
                pass

        return cache_values


class PublisherTargetValueManager(TargetValueManager):

    def get_representant_object(self, exchange, category, values):
        '''
        For parameter description see
        :meth:`ui.targeting.TargetValueManager.get_representant_object`

        .. note::

            This method overwrites category parameter to always be
            :data:`etc.dimensions.g_publisher`. It also returns a
            :class:`~ui.targeting.models.PublisherTargetValue` instance
            to be consistent with PublisherTargetValueManager
        '''
        representant = TargetValueManager.get_representant_object(
            self,
            exchange=exchange,
            category=dimensions.g_publisher,
            values=values
        )
        if representant:
            return representant.publishertargetvalue

    def representants(self):
        return TargetValueManager.representants(self).\
            filter(category=dimensions.g_publisher)

    def get_or_create_multi_pk(self, exchange, dimension, values):
        """
        Get primary keys corresponding to exchange, and list of values.

        :param str exchange: exchange code
        :param list values: list of target values hierarchy values

        :returns: dictionary of values and corresponding primary keys
        :rtype: dict

        .. note::

            If value does not exists, it will be created!

        """

        cache_values = TargetCache.multi_get_publisher_pk(
            exchange, values
        )
        for value, cache_val in cache_values.iteritems():
            if cache_val is not None:
                continue

            try:
                publisher_tv, _ = PublisherTargetValue.\
                    objects.get_or_create_unrepresented(
                        value=value,
                        exchange=exchange,
                        category='publisher',
                        strict=False,
                    )
                TargetCache.set_publisher_pk(exchange, value, publisher_tv.pk)
                cache_values[value] = publisher_tv.pk
            except (InvalidTargetValues, TargetValueQueryError):
                pass

        return cache_values

    def get_publisher_info_by_pk(self, pk):
        '''
        Retrieves information about publisher based on his id in database.

        :param int pk: publisher's primary key.
        :rtype: dict
        :returns: dict with sizes, positions and segments of publisher.
        '''
        cache_val = TargetCache.get_publisher_info(pk)
        if cache_val is not None:
            return cache_val

        # make sure we get representant only
        try:
            publisher_tv = self.representants().get(represented__pk=pk)
            info = {
                'sizes': publisher_tv.sizes,
                'positions': publisher_tv.positions,
                'segments': [
                    seg.appnexus_id for seg in publisher_tv.segments.all()]
            }
            TargetCache.set_publisher_info(pk, info)
            return info
        except PublisherTargetValue.DoesNotExist:
            pass


class TargetValue(ProfileValue):

    '''
    Contains information about profile keys values
    '''

    # Contains category name
    # category somehow describes structure of key.
    # i.e. 'location'. 'gender'
    category = m.CharField(max_length=200, db_index=True)

    # Contains full targeted value, saved in delimited format i.e.
    # 'USA:NY:New York', 'Symbian:5.0' etc.
    # If value is an empty string it matches unspecified option
    # for given targeting value
    value = m.TextField(db_index=True)

    # Source of value in system
    exchange = ExchangeField()

    # Holds informations about object representatives in system
    # if given TargetValue is a representant itself this field is set to None
    representant = m.ForeignKey('self', null=True, related_name='represented',
                                on_delete=m.SET_NULL)

    objects = TargetValueManager()

    class Meta:
        get_latest_by = 'inserted_at'
        unique_together = [('exchange', 'category', 'value')]
        ordering = ('id', )

    @property
    def is_representant(self):
        return self.representant is None

    @property
    def has_representant(self):
        return not (self.is_representant or (self.representant == self))

    @property
    def key(self):
        '''Tries to retrieve keyname based on category name'''
        keys = dimensions.hierarchy[self.category]
        values = TargetMap.unpack(self.value)
        filtered = []
        for key, value in zip(keys, values):
            if value is None:
                continue
            filtered.append(key)
        return filtered[-1] if len(filtered) else None

    @property
    def value_list(self):
        '''Maps target value into list. Places None if item is "". '''
        return TargetMap.unpack(self.value)

    @property
    def value_dict(self):
        '''Maps target value into dict with keys'''
        return dict(zip(dimensions.hierarchy[self.category], self.value_list))

    @property
    def display_value(self):
        '''
        Return first non-empty value from reversed unpacked target value
        (~= best precision value).
        '''
        for value in TargetMap.unpack(self.value)[::-1]:
            if value is not None:
                return value
        return u''  # Should never happen.

    @property
    def display_label(self):
        '''Label to display, dedicated for user view'''
        labelmap = {
            dimensions.region: "{0} (state)",
        }
        value = self.display_value
        return unicode(labelmap.get(self.key, value)).format(value)

    def __unicode__(self):
        return u"{0}:{1}{2}".format(
            self.key,
            self.family_line or self.value,
            ' (%s)' % (self.exchange or '')
        )

    def get_category(self):
        for category_name, keys in dimensions.hierarchy.items():
            if self.key in keys:
                return category_name

    @property
    def cache_keys(self):
        return dimensions.hierarchy[self.category], self.value_list

    @property
    def family_line(self):
        return TargetMap.family_line(self.value)

    @property
    def adverts(self):
        from ui.campaign.models import Advert
        return Advert.objects.filter(
            Q(strategy__targeting_values=self)
            | Q(strategy__targeting_values_exclude=self)
        )

    def read_represented(self):
        """Read raw values for exchanges."""
        return self.represented.all() | self.__class__.objects.filter(pk=self.pk)

    def untranslate_to(self, exchange):
        """
        :param str exchange: one of bidrequest.constants.EXCHANGES.ALL
        """
        return self.read_represented().filter(exchange=exchange).distinct()

    def make_representant(self):
        self.representant = None

    def make_represented(self, representant):
        self.representant = representant

    def make_unrepresented(self):
        self.representant = self


class PublisherTargetValue(TargetValue):

    _sizes = m.TextField(null=True)
    _positions = m.TextField(null=True)
    segments = m.ManyToManyField(AppNexusSegment)

    class Meta:
        ordering = ('id',)

    objects = PublisherTargetValueManager()

    # Properties that allows saving and retrieving list to a TextField

    @property
    def sizes(self):
        if not self._sizes:
            return []
        return ast.literal_eval(self._sizes)

    @sizes.setter
    def sizes(self, value):
        if not isinstance(value, list):
            raise TypeError('Value must be a list type.')
        self._sizes = str(value)

    @property
    def positions(self):
        if not self._positions:
            return []
        return ast.literal_eval(self._positions)

    @positions.setter
    def positions(self, value):
        if not isinstance(value, list):
            raise TypeError('Value must be a list type.')
        self._positions = str(value)

    @property
    def network_publisher(self):
        """
        Return publisher value list without inventory part.

        :returns: network, publisher
        :rtype: tuple
        """
        return tuple(self.value_list[1:])

    @property
    def network_id(self):
        '''
        Returns network's id bound for publisher.

        It's internal id for Nexage (where network represents self by name)
        And it's AppNexus' ID for networks from AppNexus
        '''

        if self.represented.exists():
            represented_dict = self.represented.get().value_dict
            return represented_dict[dimensions.network]

    @property
    def inventory_key(self):
        '''
        Returns inventory key behind inventory description for representant
        '''
        key = dimensions.publisher_inventory
        if not self.represented.exists():
            return self.value_dict[key]

        return self.represented.get().value_dict[key]

    @property
    def indexable(self):
        '''
        Determine whether instance is indexable, or not.
        :returns: Returns True, or False to determine,
        whether this instance should be indexed or not
        '''
        if self.representant_id or not self.network_id:
            return False
        return True


class TargetBase(ProfileValue):

    key = NotImplemented

    class Meta:
        abstract = True

    @property
    def cache_keys(self):
        return dimensions.hierarchy[self.key], [self.code]


class TargetTree(m.Model):

    ''''
    Abstract class which allows us implement nested-like target values.
    '''
    name = m.TextField(db_index=True)

    parent = TreeForeignKey(
        'self',
        related_name='children',
        null=True,
        blank=True
    )

    objects = TargetTreeManager()

    class Meta:
        get_latest_by = 'inserted_at'
        unique_together = [('name', 'parent')]
        ordering = ('id',)
        abstract = True

    def __unicode__(self):
        return self.name

    def untranslate_to(self, exchange):
        """
        :param str exchange: one of bidrequest.constants.EXCHANGES.ALL
        """
        return self.represented.filter(
            exchange=exchange
        ).distinct()

    @classmethod
    def recursive_node_to_dict(cls, node):
        result = {
            'id': node.pk,
            'key': dimensions.content_category,
            'code': node.name,
            'label': node.name,
            'name': node.name,
        }

        children_items = cls.objects.filter(
            parent=node.pk)

        children = [
            cls.recursive_node_to_dict(c) for c in children_items
        ]

        if children:
            result['children'] = children

        return result

    def get_nested_nodes(self):
        '''
        Getting all nested nodes as a flat list (including self node).

        :rtype: list of objects
        :returns: list of nodes
        '''
        node_list = [self]
        if self.children.count() > 0:
            for child in self.children.all():
                node_list.extend(child.get_nested_nodes())
        return node_list


class TargetTreeValue(m.Model):

    """
    Class which represents categories' hierarchy values.
    It's used by trees to dump their representants into cache.

    .. warning::
        One should add values to this table only in migrations.
    """
    name = m.TextField(db_index=True)

    exchange = ExchangeField()

    objects = TargetTreeValueManager()

    class Meta:
        get_latest_by = 'inserted_at'
        unique_together = [('name', 'exchange', 'representant')]
        ordering = ('id',)
        abstract = True

    @property
    def cache_keys(self):
        return [dimensions.hierarchy[self.DIMENSION], [self.name]]

    @property
    def representats(self):
        raise NotImplemented()


class ContentCategory(TargetTree):

    """
    Class which represents categories' hierarchy.

    Class is empty because almost every field is covered by base class.
    General Purpose of its existence is to provide "data-partition" for
    content category feature in targeting UI.
    .. warning::
        One should add values to this table only in migrations.
    """
    pass


class ContentCategoryValue(TargetTreeValue):

    """
    Class which maps categories from bidder to our categories.

    .. warning::
        One should add values to this table only in migrations.
    """
    DIMENSION = dimensions.content_category
    representant = m.ForeignKey(
        ContentCategory,
        null=True,
        related_name='represented',
        on_delete=m.SET_NULL
    )


class SegmentProximicBase(m.Model):
    PROVIDER = PROXIMIC

    PRICE_CPM = TARGETING_ADDITIONAL_DATA_COSTS['brand_protection']

    appnexus_id = m.IntegerField()
    name = m.CharField(max_length=300)

    objects = SegmentManager()

    class Meta:
        abstract = True

    @property
    def cache_keys(self):
        return (
            dimensions.hierarchy[self.DIMENSION],
            [self.appnexus_id],
        )


class SegmentProximicMaturityRating(SegmentProximicBase):

    """
    We use class name in backend as segment type.

    You have to set provider name and price cpm.

    .. note::

        please see :attr:`bidrequest.segments.proximic_maturity_rating`
        for values we match and update them accordingly
    """

    SEGMENT_IDS = segments.proximic_maturity_rating
    DIMENSION = dimensions.proximic_maturity_rating
    description = m.TextField(blank=True)


class SegmentProximicSafetyLevel(SegmentProximicBase):

    """
    Class is responsible for containing infornation about Safety level
    segments selected by user in strategy's targeting options.

    .. note::

        please see :attr:`bidrequest.segments.proximic_safety_level`
        for values we match and update them accordingly
    """
    SEGMENT_IDS = segments.proximic_safety_level
    DIMENSION = dimensions.proximic_safety_level


class SegmentTree(TargetTree):

    '''
    Base class for all segment-like tree widgets, supported by segment
    mechanism dedicated for appnexus and data providers related to them.
    Part of SegmentTree items can be marked as a Virtual elements which can't
    translate into appnexus category but must be displayed in our system.
    '''
    appnexus_id = m.IntegerField(null=True)

    objects = SegmentTreeManager()

    class Meta:
        abstract = True
        ordering = ('id',)

    @property
    def DIMENSION(self):
        raise NotImplemented()

    @property
    def cache_keys(self):
        return (dimensions.hierarchy[self.DIMENSION],
                [self.appnexus_id])

    def untranslate_to(self, exchange):
        if self.appnexus_id:
            return [self]
        return []


class ProximicSegmentTree(SegmentTree):

    PROVIDER = PROXIMIC

    class Meta:
        abstract = True
        ordering = ('id',)


class SegmentProximicPageQuality(ProximicSegmentTree):

    """

    .. note::

        please see :attr:`bidrequest.segments.proximic_page_quality`
        for values we match and update them accordingly
    """
    PRICE_CPM = TARGETING_ADDITIONAL_DATA_COSTS['page_quality']
    SEGMENT_IDS = segments.proximic_page_quality
    DIMENSION = dimensions.proximic_page_quality


class SegmentProximicPageNoticeability(ProximicSegmentTree):

    """

    .. note::

        please see :attr:`bidrequest.segments.proximic_page_noticeability`
        for values we match and update them accordingly
    """
    PRICE_CPM = TARGETING_ADDITIONAL_DATA_COSTS['page_noticeability']
    SEGMENT_IDS = segments.proximic_page_noticeability
    DIMENSION = dimensions.proximic_page_noticeability


class SegmentProximicPagePlacement(ProximicSegmentTree):

    """

    .. note::

        please see :attr:`bidrequest.segments.proximic_page_placement`
        for values we match and update them accordingly
    """
    PRICE_CPM = TARGETING_ADDITIONAL_DATA_COSTS['page_placement']
    SEGMENT_IDS = segments.proximic_page_placement
    DIMENSION = dimensions.proximic_page_placement


class SegmentProximicContextual(ProximicSegmentTree):

    """

    .. note::

        please see :attr:`bidrequest.segments.proximic_contextual`
        for values we match and update them accordingly
    """
    PRICE_CPM = TARGETING_ADDITIONAL_DATA_COSTS['contextual_categories']
    SEGMENT_IDS = segments.proximic_contextual
    DIMENSION = dimensions.proximic_contextual

    class Meta:
        ordering = ('name',)


class SegmentProximicPageLanguage(ProximicSegmentTree):

    """

    .. note::

        please see :attr:`bidrequest.segments.proximic_languages`
        for values we match and update them accordingly
    """
    PRICE_CPM = TARGETING_ADDITIONAL_DATA_COSTS['language']
    SEGMENT_IDS = segments.proximic_languages
    DIMENSION = dimensions.proximic_page_language

    class Meta:
        ordering = ('name',)


class Peer39Base(m.Model):

    PROVIDER = PEER39

    PRICE_CPM = TARGETING_ADDITIONAL_DATA_COSTS['peer39']

    # Id provided by peer39
    peer39_id = m.IntegerField(null=True)

    class Meta:
        abstract = True


class Peer39FlatBase(Peer39Base):

    '''
    Base class for flat lists of Peer39 segments
    '''

    appnexus_id = m.IntegerField()

    name = m.CharField(max_length=300)

    objects = SegmentManager()

    class Meta:
        abstract = True
        ordering = ('id',)

    @property
    def cache_keys(self):
        return (
            dimensions.hierarchy[self.DIMENSION],
            [self.appnexus_id],
        )

    def __unicode__(self):
        return self.name


class Peer39PageLanguage(Peer39FlatBase):

    """
    Segment provided by Peer39 describing page language

    .. note::

        please see :attr:`bidrequest.segments.peer39_languages`
        for values we match and update them accordingly
    """
    SEGMENT_IDS = segments.peer39_languages
    DIMENSION = dimensions.peer_page_language


class Peer39BrandProtection(Peer39FlatBase):

    """
    Segment provided by Peer39 describing brand protection

    .. note::

        please see :attr:`bidrequest.segments.peer39_brand_protection`
        for values we match and update them accordingly
    """
    SEGMENT_IDS = segments.peer39_brand_protection
    DIMENSION = dimensions.peer_brand_protection


class Peer39ContextualSegment(Peer39Base, SegmentTree):

    """
    Segment provided by Peer39 describing page context

    .. note::

        please see :attr:`bidrequest.segments.peer39_contextual`
        for values we match and update them accordingly
    """
    SEGMENT_IDS = segments.peer39_contextual
    DIMENSION = dimensions.peer_contextual

    class Meta:
        ordering = ('name',)


class Peer39PageQuality(Peer39Base, SegmentTree):

    """
    Segment provided by Peer39 describing page quality

    .. note::

        please see :attr:`bidrequest.segments.peer39_page_quality`
        for values we match and update them accordingly
    """
    SEGMENT_IDS = segments.peer39_page_quality
    DIMENSION = dimensions.peer_page_quality

    class Meta:
        ordering = ('name',)


class LotameBase(m.Model):
    """Behavioral segments provided by Lotame"""
    PROVIDER = LOTAME

    # Id provided by lotame, used for reporting and billing
    lotame_id = m.IntegerField(unique=True)

    appnexus_id = m.IntegerField(unique=True)

    name = m.CharField(max_length=300)

    objects = SegmentManager()

    class Meta:
        abstract = True

    @property
    def DIMENSION(self):
        # Dimension should be defined on category level
        raise NotImplemented()

    @property
    def PRICE_CPM(self):
        # Segment price should be defined on category level
        raise NotImplemented()

    def __unicode__(self):
        return self.name


class LotameDemographic(LotameBase):
    """Audience provided by Lotame based on demographic information"""

    SEGMENT_IDS = segments.lotame_demographic
    DIMENSION = dimensions.lotame_demographic
    PRICE_CPM = TARGETING_ADDITIONAL_DATA_COSTS['lotame_demographic']
    SEGMENT_IDS = segments.lotame_demographic


class LotameAdvancedDemographic(LotameBase):
    """Audience provided by Lotame based on advanced demographic info"""

    SEGMENT_IDS = segments.lotame_advanced_demographic
    DIMENSION = dimensions.lotame_advanced_demographic
    PRICE_CPM = TARGETING_ADDITIONAL_DATA_COSTS['lotame_advanced_demographic']
    SEGMENT_IDS = segments.lotame_advanced_demographic


class LotameBehavioralInterest(LotameBase):
    """Audience provided by Lotame based on user interests"""

    SEGMENT_IDS = segments.lotame_behavioral_interest
    DIMENSION = dimensions.lotame_behavioral_interest
    PRICE_CPM = TARGETING_ADDITIONAL_DATA_COSTS['lotame_behavioral_interest']
    SEGMENT_IDS = segments.lotame_behavioral_interest


class LotameInfluencers(LotameBase):
    """
    Audience provided by Lotame containing people who have created content
    on the Internet
    """

    SEGMENT_IDS = segments.lotame_influencers
    DIMENSION = dimensions.lotame_influencers
    PRICE_CPM = TARGETING_ADDITIONAL_DATA_COSTS['lotame_influencer']
    SEGMENT_IDS = segments.lotame_influencers


class LotameOffline(LotameBase):
    """Audience provided by Lotame based on offline purchases"""

    SEGMENT_IDS = segments.lotame_offline
    DIMENSION = dimensions.lotame_offline
    PRICE_CPM = TARGETING_ADDITIONAL_DATA_COSTS['lotame_offline']
    SEGMENT_IDS = segments.lotame_offline


from ui.targeting.appnexus import *  # noqa


def publishertargetvalue_clear_info(sender, instance, *args, **kwargs):
    """
    Clear publishers info cache.

    Should be used in case of save or delete.

    """

    TargetCache.delete_publisher_info(instance.pk)


post_save.connect(
    publishertargetvalue_clear_info, sender=PublisherTargetValue, weak=False)
pre_delete.connect(
    publishertargetvalue_clear_info, sender=PublisherTargetValue, weak=False)


def publisher_clear_pk(sender, instance, *args, **kwargs):
    """
    Clear publisher pk key.

    Should be used only when deleting.

    """
    publisher_tv = instance

    if publisher_tv.exchange:
        TargetCache.delete_publisher_pk(instance.exchange,
                                        instance.value_list)


pre_delete.connect(publisher_clear_pk, sender=PublisherTargetValue)


def targetvalue_clear_pk(sender, instance, *args, **kwargs):
    """
    Clear target value pk key.

    Should be used only when deleting.

    """
    targetvalue = instance

    if targetvalue.exchange:
        TargetCache.delete_target_pk(instance.exchange, instance.category,
                                     instance.value_list)

pre_delete.connect(targetvalue_clear_pk, sender=TargetValue, weak=False)
