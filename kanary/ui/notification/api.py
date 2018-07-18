from tastypie import fields
from tastypie.resources import ALL

from ui.authorization import Auth
from ui.notification.models import Event, EventCategory
from ui.utils import prepend_slug
from ui.common.api import ProtectedModelResource

from etc.constants import BACKEND_DATE_TIME_FORMAT


class EventResource(ProtectedModelResource):

    prepend_urls = prepend_slug

    class Meta:
        resource_name = 'event'
        queryset = Event.objects.all()
        allowed_methods = ('get', )
        authorization = Auth('account')
        fields = ['id']
        filtering = {'id': ALL}

    header = fields.CharField('header')
    message = fields.CharField('message')
    category_id = fields.IntegerField('category_id')

    def dehydrate(self, bundle):
        obj = bundle.obj
        bundle.data['datetime'] = bundle.request.user.account \
            .from_UTC(obj.datetime_UTC).strftime(BACKEND_DATE_TIME_FORMAT)
        return bundle

    def alter_list_data_to_serialize(self, request, data):
        data['meta']['unread'] = request.user.unread_events_count
        # it's almost pushed, so we can assume, user can read it(?)
        return data


class EventCategoryResource(ProtectedModelResource):

    prepend_urls = prepend_slug

    class Meta:
        resource_name = 'event_category'
        queryset = EventCategory.objects.all()
        allowed_methods = ('get', )
        fields = ['id', 'name']
