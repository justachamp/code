'''
UI API declaration

Contains API for UI definition. It uses tastypie declarative approach.
Try to keep it as much REST as possible. But sometimes we will adjust some
responses to adjust it for reduction of number of requests from UI.

'''

from django.conf.urls import url
from django.http import Http404
from tastypie import fields
from tastypie.resources import Resource
from tastypie.authorization import Authorization
from tastypie.utils import trailing_slash
from tastypie.bundle import Bundle
from haystack.query import EmptySearchQuerySet

from etc import dimensions
from ui.targeting.models import (
    TargetValue,
    PublisherTargetValue,
    ContentCategory,
    SegmentProximicMaturityRating,
    SegmentProximicSafetyLevel,
    SegmentProximicPageLanguage,
    SegmentProximicPageQuality,
    SegmentProximicPageNoticeability,
    SegmentProximicPagePlacement,
    SegmentProximicContextual,
    Peer39ContextualSegment,
    Peer39PageQuality,
    Peer39PageLanguage,
    Peer39BrandProtection,
    LotameDemographic,
    LotameAdvancedDemographic,
    LotameBehavioralInterest,
    LotameInfluencers,
    LotameOffline
)
from ui.common.api import (
    SearchResource,
    SimpleSearchResource,
    SearchPaginator,
    ProtectedModelResource
)


class TargetingSearchResource(SearchResource):

    min_autocomplete_query_length = 2
    force_search_results_limit = 10

    def build_search_query(self, request, search_query):
        value = request.GET.get('q', '')
        if len(value) < self.min_autocomplete_query_length:
            return EmptySearchQuerySet()
        return search_query.filter(value=value, category=self.Meta.search_category)


class TargetResource(ProtectedModelResource):

    name = fields.CharField('value', readonly=True)

    class Meta:
        fields = ['name']
        allowed_methods = ('get', )
        authorization = Authorization()


class DeviceOSResource(TargetResource, TargetingSearchResource):

    class Meta:
        resource_name = dimensions.g_os
        queryset = TargetValue.objects.representants_category_os()
        search_category = dimensions.g_os

    def dehydrate(self, bundle):
        bundle.data['type'] = dimensions.g_os
        bundle.data['name'] = bundle.obj.display_label
        bundle.data['help'] = bundle.obj.family_line
        return bundle


class DeviceModelResource(TargetResource, TargetingSearchResource):

    class Meta:
        resource_name = dimensions.g_device
        queryset = TargetValue.objects.representants_category_device()
        search_category = dimensions.g_device

    def dehydrate(self, bundle):
        bundle.data['type'] = dimensions.g_device
        return bundle


class LocationResource(TargetResource, TargetingSearchResource):

    class Meta:
        resource_name = dimensions.g_location
        queryset = TargetValue.objects.representants_category_location()
        search_category = dimensions.g_location
        fields = ['pk', 'key', 'value', 'type']

    def build_search_query(self, request, search_query):
        query = super(LocationResource, self).build_search_query(request,
                                                                 search_query)
        return query.order_by('rank')

    def dehydrate(self, bundle):
        bundle.data['id'] = bundle.obj.id
        bundle.data['type'] = 'location'
        bundle.data['name'] = bundle.obj.display_label
        bundle.data['help'] = bundle.obj.family_line
        return bundle


class AgeGroupResource(TargetResource):

    class Meta:
        resource_name = 'age_group'
        queryset = TargetValue.objects.representants_category_age_group()


class GenderResource(TargetResource):

    class Meta:
        resource_name = 'gender'
        queryset = TargetValue.objects.representants_category_gender()


class TreeResource(Resource):

    def base_urls(self):
        return [
            url(r"^(?P<resource_name>%s)%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_tree'),
                name="api_get_tree"
                ),
        ]

    def get_tree(self, request, **kwargs):
        tree = self.Meta.cls.objects.into_tree()

        return self.create_response(
            request, {
                'tree': tree
            }
        )


class ContentCategoryTreeResource(TreeResource):

    class Meta:
        resource_name = 'categories_tree'
        cls = ContentCategory


class SegmentProximicMaturityRatingResource(ProtectedModelResource):

    class Meta:
        resource_name = 'proximic_maturity_rating'
        queryset = SegmentProximicMaturityRating.objects.all()


class SegmentProximicSafetyLevelResource(ProtectedModelResource):

    class Meta:
        resource_name = 'proximic_safety_level'
        queryset = SegmentProximicSafetyLevel.objects.all()


class SegmentProximicLanguageResource(ProtectedModelResource):

    class Meta:
        resource_name = 'proximic_language'
        queryset = SegmentProximicPageLanguage.objects.all()


class SegmentProximicPageQualityResource(ProtectedModelResource):

    class Meta:
        resource_name = 'proximic_page_quality'
        queryset = SegmentProximicPageQuality.objects.all()


class SegmentProximicPageNoticeabilityResource(TreeResource):

    class Meta:
        resource_name = 'proximic_page_noticeability'
        cls = SegmentProximicPageNoticeability


class SegmentProximicPagePlacementResource(TreeResource):

    class Meta:
        resource_name = 'proximic_page_placement'
        cls = SegmentProximicPagePlacement


class SegmentProximicContextualResource(TreeResource):

    class Meta:
        resource_name = 'proximic_contextual'
        cls = SegmentProximicContextual


class PeerTreeResource(Resource):

    class Meta:
        abstract = True
        allowed_methods = ('get', )
        cls = None
        name_in_url = None

    def base_urls(self):
        return [
            url(r"^(?P<resource_name>%s)%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_tree'),
                name=self.Meta.name_in_url
                ),
        ]

    def get_tree(self, request, **kwargs):

        tree = self.Meta.cls.objects.into_tree()

        return self.create_response(
            request, {
                'tree': tree
            }
        )


class SegmentPeerContextualSegmentResource(PeerTreeResource):

    class Meta:
        resource_name = 'peer_contextual_segments_tree'
        cls = Peer39ContextualSegment
        name_in_url = 'api_get_tree_peer39_contextual'


class SegmentPeerPageQualityResource(PeerTreeResource):

    class Meta:
        resource_name = 'peer_page_quality_tree'
        cls = Peer39PageQuality
        name_in_url = 'api_get_tree_peer39_page_quality'


class PeerLanguageResource(ProtectedModelResource):

    class Meta:
        resource_name = 'peer_language'
        queryset = Peer39PageLanguage.objects.all()


class PeerBrandProtection(ProtectedModelResource):

    class Meta:
        resource_name = 'peer_brand_protection'
        queryset = Peer39BrandProtection.objects.all()


class LotameDemographicResource(ProtectedModelResource):

    class Meta:
        resource_name = 'lotame_demographic'
        queryset = LotameDemographic.objects.all()


class LotameAdvancedDemographicResource(ProtectedModelResource):

    class Meta:
        resource_name = 'lotame_advanced_demographic'
        queryset = LotameAdvancedDemographic.objects.all()


class LotameBehavioralInterestResource(ProtectedModelResource):

    class Meta:
        resource_name = 'lotame_behavioral_interest'
        queryset = LotameBehavioralInterest.objects.all()


class LotameInfluencersResource(ProtectedModelResource):

    class Meta:
        resource_name = 'lotame_influencers'
        queryset = LotameInfluencers.objects.all()


class LotameOfflineResource(ProtectedModelResource):

    class Meta:
        resource_name = 'lotame_offline'
        queryset = LotameOffline.objects.all()


class CarrierResource(TargetResource, TargetingSearchResource):

    class Meta:
        resource_name = 'carrier'
        queryset = TargetValue.objects.representants_category_carrier()
        search_category = dimensions.carrier

    def dehydrate(self, bundle):
        bundle.data['type'] = dimensions.carrier
        return bundle


class PublisherAdPositionsResource(TargetResource):

    class Meta:
        resource_name = 'publisher_ad_positions'
        queryset = TargetValue.objects.representants_category_position()


class PublishersInventoryTypeResource(TargetResource):

    class Meta:
        resource_name = 'publishers_inventory_type'
        queryset = TargetValue.objects.representants_category_inventory()


class PublishersResource(SimpleSearchResource, Resource):

    min_autocomplete_query_length = 3

    id = fields.CharField('pk')
    name = fields.CharField('name')
    network = fields.CharField('network')
    inventory = fields.CharField('inventory')
    publisher_id = fields.CharField()
    sizes = fields.ListField('sizes')
    positions = fields.ListField('positions')
    segments = fields.ListField('segments')

    class Meta:
        resource_name = dimensions.g_publisher
        list_allowed_methods = ('get', )
        details_allowed_methods = ()
        authorization = Authorization()
        object_class = PublisherTargetValue
        paginator_class = SearchPaginator

    def dehydrate_publisher_id(self, bundle):
        return '{0}-{1}'.format(
            bundle.obj.network_id,
            bundle.obj.publisher_id
        )

    def get_object_list(self, request):
        '''
        .. note::

            Method has to be implemented (as it returns NotImplementedError
            otherwise), so let it return objects list.
        '''
        return SimpleSearchResource.get_paginated_search_query(self, request)

    def build_search_query(self, request, search_query):
        ids = request.GET.getlist('ids')  # specific ids
        inventory = request.GET.get('inventory')  # publisher type
        network_id = request.GET.get('network_id')  # network id
        publisher_id = request.GET.get('publisher_id')  # publisher id
        name = request.GET.get('name', '')  # publisher name
        network = request.GET.get('network', '')  # network name

        if inventory:
            search_query = search_query.filter_and(inventory=inventory)

        if publisher_id:
            try:
                network_id, publisher_id = publisher_id.split('-')
            except ValueError:
                # Search string does not contain "-"
                pass

            search_query = search_query.filter_and(
                publisher_id=publisher_id
            )

        if network_id:
            search_query = search_query.filter(network_id=network_id)

        if len(name) >= self.min_autocomplete_query_length:
            search_query = search_query.filter(name=name)

        if len(network) >= self.min_autocomplete_query_length:
            search_query = search_query.filter(network=network)

        if ids:
            search_query = search_query.filter(django_id__in=ids)

        return search_query.filter_and(pubkey=dimensions.publisher_name)

    def obj_get_list(self, bundle):
        return self.get_object_list(bundle.request)

    def obj_get(self, bundle, **kwargs):
        search_query = SimpleSearchResource.get_search_query(
            self,
            bundle.request
        )

        objects = search_query.filter(django_id=kwargs['pk'])
        if objects:
            return objects[0]

        raise Http404("Sorry, no such Publisher")

    def detail_uri_kwargs(self, bundle_or_object):

        kwargs = {}
        if isinstance(bundle_or_object, Bundle):
            kwargs['pk'] = bundle_or_object.obj.pk
        else:
            kwargs['pk'] = bundle_or_object.pk
        return kwargs


class NetworkResource(SimpleSearchResource, Resource):

    min_autocomplete_query_length = 3

    id = fields.CharField('pk')
    network_id = fields.CharField('network_id')
    network = fields.CharField('network')
    inventory = fields.CharField('inventory')

    class Meta:
        resource_name = dimensions.network
        allowed_methods = ('get', )
        authorization = Authorization()
        object_class = PublisherTargetValue
        paginator_class = SearchPaginator

    def get_object_list(self, request):
        '''
        .. note::

            Method has to be implemented (as it returns NotImplementedError
            otherwise), so let it return objects list.
        '''
        return SimpleSearchResource.get_paginated_search_query(self, request)

    def build_search_query(self, request, search_query):

        inventory = request.GET.get('inventory')  # publisher type
        network_id = request.GET.get('network_id')  # network id
        network = request.GET.get('network', '')  # network name

        if inventory:
            search_query = search_query.filter_and(inventory=inventory)

        if network_id:
            search_query = search_query.filter_and(network_id=network_id)

        if len(network) >= self.min_autocomplete_query_length:
            search_query = search_query.filter_and(network=network)

        return search_query.filter_and(pubkey=dimensions.network)

    def obj_get_list(self, bundle):
        return self.get_object_list(bundle.request)

    def detail_uri_kwargs(self, bundle_or_object):

        kwargs = {}
        if isinstance(bundle_or_object, Bundle):
            kwargs['pk'] = bundle_or_object.obj.pk
        else:
            kwargs['pk'] = bundle_or_object.pk
        return kwargs
