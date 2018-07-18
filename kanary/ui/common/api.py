import logging

from elasticsearch import TransportError
from tastypie.utils import trailing_slash
from tastypie.resources import ModelResource
from tastypie.paginator import Paginator as TastypiePaginator
from haystack.query import SearchQuerySet
from django.conf import settings
from django.conf.urls import url
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404

log = logging.getLogger('django')


class SearchPaginator(TastypiePaginator):

    def get_count(self):
        return self.objects.paginator.count

    def page(self):
        page = super(SearchPaginator, self).page()
        page['meta']['page'] = self.objects.number
        return page


class SimpleSearchResource(object):

    min_autocomplete_query_length = 0
    force_search_results_limit = 0  # 0 means inf

    def get_search_query(self, request, **kwargs):

        # Do the query.
        cls_meta = self._meta.object_class._meta
        django_ct = '{0}.{1}'.format(cls_meta.app_label, cls_meta.object_name)
        search_query = SearchQuerySet().filter(django_ct=django_ct.lower())
        search_query = self.build_search_query(request, search_query)
        if self.force_search_results_limit:
            search_query = search_query[:self.force_search_results_limit]
        return search_query

    def get_paginated_search_query(self, request, **kwargs):

        search_query = self.get_search_query(request, **kwargs)
        limit = request.GET.get('limit', settings.API_LIMIT_PER_PAGE)
        paginator = Paginator(search_query, limit)

        try:
            page = int(request.GET.get('page', 1))
            return paginator.page(page)
        except InvalidPage:
            raise Http404("Sorry, no results on that page.")

    def build_search_query(self, request, search_query):
        '''
            method used to build_search query. Should return search_query!

            :param request: django request object
            :param haystack.query.SearchQuerySet search_query: search query set
                limited to resource model class
        '''
        return search_query


class ProtectedModelResource(ModelResource):

    ''' Override @csrf_exempt decorator added by tastypie to enable CSRF protection'''

    def wrap_view(self, view):
        def wrapper(request, *args, **kwargs):
            return ModelResource.wrap_view(self, view)(request, *args, **kwargs)
        return wrapper


class SearchResource(SimpleSearchResource, ProtectedModelResource):

    def prepend_urls(self):
        return [
            url(
                r"^(?P<resource_name>{0})/search{1}$".format(
                    self._meta.resource_name,
                    trailing_slash()
                ),
                self.wrap_view('get_search'),
                name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        """Get search result."""
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        page = SimpleSearchResource.get_paginated_search_query(self, request, **kwargs)

        objects = []

        for result in page.object_list:
            found_object = result.object
            # this won't allow empty objects to appear (like those that fell outside the reach of index_queryset)
            if found_object is None:
                # self healing mechanism. Remove such object from index
                try:
                    result.searchindex.remove_object(result.id)
                except TransportError:
                    log.error('[SearchResource] failed to remove bogus document {0}'.format(result))
                # do not process it
                continue
            bundle = self.build_bundle(obj=found_object, request=request)
            bundle = self.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)
