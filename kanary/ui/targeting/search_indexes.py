from haystack.indexes import (
    Indexable, CharField, IntegerField, MultiValueField
)
from celery_haystack.indexes import CelerySearchIndex

from ui.targeting.models import TargetValue, TargetMap, PublisherTargetValue
from ui.haystack_extensions import AutocompleteField
from etc import dimensions


class TargetValueIndex(CelerySearchIndex, Indexable):

    '''Base search index which will be shared between various search indexes
    in targeting. It's strongly related to django-haystack'''

    # text field with document=True is required
    text = CharField(document=True)
    value = AutocompleteField(model_attr='value')
    category = CharField(model_attr='category')
    rank = IntegerField()

    def get_model(self):
        return TargetValue

    def prepare_rank(self, target_value):

        if not target_value.category == dimensions.g_location:
            return 1

        dimension_rank = (
            (dimensions.city, 3),
            (dimensions.region, 2),
            (dimensions.country, 1)
        )

        values = target_value.value_dict

        for dimension, rank in dimension_rank:
            if dimension in values:
                # Return rank of lowest hierarchy only
                return rank

    def prepare_value(self, target_value):
        '''
        Add hierarchy name to location target values, to enable filtering
        by hierarchy

        Example:
        'USA' -> 'USA country'
        'USA;Wisconsin' -> 'USA;Wisconsin state'
        'USA;Pensylvania;California' -> ''USA;Pensylvania;California city'
        '''
        if not target_value.category == dimensions.g_location:
            return target_value.value

        # Hierarchy names which are appended to index values
        location_hierarchies = ['country', 'state', 'city']

        values = list(target_value.value_list)
        last_index = len(values) - 1
        hierarchy = location_hierarchies[last_index]
        values[last_index] = "%s %s" % (values[last_index], hierarchy)
        return TargetMap.pack(values)

    def index_queryset(self, **kwargs):
        '''Returns query on which haystack will perform indexing'''
        return self.get_model().objects.representants().exclude(
            category=dimensions.g_publisher
        )


class PublisherTargetValueIndex(CelerySearchIndex, Indexable):

    '''
    Specific publisher TargetValue search index.
    Aim is to store PublisherTargetValue objects as docs within searchengine
    itself

    .. note::

        When querying search engine, remember to pass such query:

        .. code-block:: python

            SearchQuerySet().filter(
                django_ct='targeting.publishertargetvalue'
            ).all()

    '''

    text = CharField(document=True)
    """ Text name was previously NgramField, but due to problems with
    haystack/whoosh support for this field, we've migrated NgramField
    to CharField. NgramField(document=True) caused strange behaviours in
    SearchQuerySet(), e.g. all() returned empty set but filtering worked fine.
    An after-life of this dicovery can be tracked at:
    https://github.com/toastdriven/django-haystack/issues/913
    """
    name = AutocompleteField()
    network = AutocompleteField()
    inventory = CharField()
    publisher_id = IntegerField(null=True)
    network_id = IntegerField()
    pubkey = CharField()

    # Restrictions
    sizes = MultiValueField(indexed=False)
    positions = MultiValueField(indexed=False)
    segments = MultiValueField(indexed=False)

    def get_model(self):
        return PublisherTargetValue

    def index_queryset(self, **kwargs):
        '''Returns query on which haystack will perform indexing'''
        return self.get_model().objects.representants()

    def should_update(self, publisher_tv, **kwargs):
        return publisher_tv.indexable

    def prepare_name(self, publisher_tv):
        if publisher_tv.key == dimensions.publisher_name:
            return publisher_tv.value_dict[dimensions.publisher_name]
        return ''

    def prepare_text(self, publisher_tv):
        return publisher_tv.value

    def prepare_inventory(self, publisher_tv):
        return publisher_tv.inventory_key

    def prepare_pubkey(self, publisher_tv):
        return publisher_tv.key

    def prepare_sizes(self, publisher_tv):
        return publisher_tv.sizes

    def prepare_positions(self, publisher_tv):
        '''Translates position value and saves to list'''
        translated_positions = []

        for position in publisher_tv.positions:
            representant = TargetValue.objects.get_representant_value_list(
                exchange=publisher_tv.exchange,
                category=dimensions.position,
                value=[position],
            )
            if representant is not None:
                translated_positions.extend(representant)

        return translated_positions

    def prepare_segments(self, publisher_tv):
        return [seg.display_name for seg in publisher_tv.segments.all()]

    def prepare(self, publisher_tv):
        self.prepared_data = super(
            PublisherTargetValueIndex, self
        ).prepare(publisher_tv)

        network_name = publisher_tv.value_dict[dimensions.network]
        network_id = publisher_tv.network_id

        self.prepared_data['network'] = network_name
        self.prepared_data['network_id'] = network_id

        if publisher_tv.key == dimensions.publisher_name:
            self.prepared_data['publisher_id'] = publisher_tv.id

        return self.prepared_data
