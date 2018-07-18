from django.conf.urls import url
from tastypie.fields import ListField, BooleanField, CharField, IntegerField
from tastypie.validation import Validation, FormValidation
from tastypie.constants import ALL

from ui.authorization import Auth
from ui.storage.models import (
    Creative, Audience, Brand,
    DESTINATION, ACCESS_STATUS, creative_factory,
)
from ui.storage.forms import AudienceForm
from ui.common.api import ProtectedModelResource

from adserving.adserver.utils import get_audience_code, get_audience_piggyback_url


def is_not_exist_or_null(field, bundle_data):
    result = field not in bundle_data or not bundle_data[field]

    # Make strip
    if not result and isinstance(bundle_data[field], basestring):
        data = bundle_data[field].strip()
        # If field is '' then return True
        result = not bool(data)

    return result


class CreativeValidation(Validation):

    '''
        Validation that checks Creative

        note:
            we transform destination field in hydrate.
    '''
    error_messages = {'Image': 'Please, provide an image',
                      'Flash': 'Please, provide a Flash object',
                      'Video': 'Please, provide a video object'}

    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'No data has been given.'}

        errors = {}

        if 'type' not in bundle.data or bundle.data['type'] not in self.error_messages.keys():
            errors['Type'] = ['No type selected!']

        if is_not_exist_or_null('name', bundle.data):
            errors['Name'] = 'Please, provide a name'

        if is_not_exist_or_null('api_data', bundle.data):
            errors[bundle.data['type']] =\
                self.error_messages[bundle.data['type']]

        if bundle.obj.is_facebook_destination():
            if is_not_exist_or_null('fb_title', bundle.data):
                errors['Title'] = 'Please, provide a title'
            if is_not_exist_or_null('fb_body', bundle.data):
                errors['Body'] = 'Please, provide a body'

            is_newsfeed = bundle.obj.is_facebook_destination(verify_is_newsfeed=True)
            if is_newsfeed and is_not_exist_or_null('fb_brand_page', bundle.data):
                errors['Facebook page'] = 'Please, provide a facebook page'

        return errors


class CreativeResource(ProtectedModelResource):

    class Meta:
        resource_name = 'creative'
        allowed_methods = ('get', 'post', 'get', 'put', 'delete')
        always_return_data = True
        filtering = {
            'destination': ('exact', 'startswith',),
        }

        queryset = Creative.objects_visible.all()
        authorization = Auth('owner')
        fields = ('name', 'width', 'height',
                  'api_data', 'destination')
        validation = CreativeValidation()

    id = IntegerField('id', readonly=True)
    size = ListField('size', readonly=True)
    type = CharField(readonly=True)
    status = CharField('appnexus_status', readonly=True)
    api_data = CharField('api_data')
    vast_url = CharField('vast_url', readonly=True, null=True)
    to_audit = BooleanField('to_audit', readonly=True, null=True)

    fb_title = CharField('title', null=True)
    fb_body = CharField('body', null=True)
    fb_message = CharField('message', null=True)
    fb_domain = CharField('domain', null=True)
    fb_brand_page = IntegerField('brand_id', null=True)

    def prepend_urls(self):
        return [
            url(
                r"^{0}/audit/(?P<creative_id>[\d]+)$".format(
                    self._meta.resource_name,
                ),
                self.wrap_view('manual_audit'), name="creative_manual_audit"
            ),
        ]

    def manual_audit(self, request, creative_id, **kwargs):
        """
        Manual audit api view.

        :param request: request object
        :param int creative_id: creative which we want to send to audit

        Returns detail response.
        """
        creative = Creative.objects.get(id=creative_id)
        creative.to_audit = True
        creative.save()
        return self.get_detail(request, pk=creative_id)

    def dehydrate_destination(self, bundle):
        return bundle.obj.get_destination_display()

    def dehydrate(self, bundle):
        creative = bundle.obj
        # get type based on class name
        bundle.data['type'] = creative.type
        bundle.data['status'] = creative.state.status
        bundle.data['is_auditable'] = creative.is_auditable

        if creative.is_facebook_destination(verify_is_newsfeed=True):
            bundle.data['fb_brand_page_access'] = creative.brand.appnexus_access_status

        if creative.type == 'Video':
            bundle.data['liverail_status'] = creative.liverail_status
        else:
            bundle.data['liverail_status'] = ''

        # If facebook creative was added to strategy,
        # Add information about strategy and campaign
        if creative.is_facebook_destination():
            # For facebook creatives there is only one advert
            advert = creative.advert_set.filter(is_deleted=False,
                                                strategy__is_deleted=False,
                                                strategy__campaign__is_deleted=False).first()
            if advert:
                strategy = advert.strategy
                campaign = strategy.campaign
                bundle.data['strategy'] = strategy.name
                bundle.data['campaign'] = campaign.name

        return bundle

    def hydrate_destination(self, bundle):
        bundle.data['destination'] = DESTINATION[bundle.data['destination']]
        return bundle

    def hydrate_fb_brand_page(self, bundle):
        """ Clear creative brand page if it is not facebook newsfeed. """
        if bundle.data['destination'] != 'facebook_newsfeed':
            bundle.data['fb_brand_page'] = None
        return bundle

    def hydrate(self, bundle):
        # A bug in Tastypie: on update, hydrate is called 2 times,
        # once with obj.id == None and method == 'PUT'
        # We should create an object only if method is POST
        if not bundle.obj.id and bundle.request.method == 'POST':
            bundle.obj = creative_factory(
                bundle.data['type'],
                owner=bundle.request.user.account
            )

        return bundle


class AudienceResource(ProtectedModelResource):

    id = IntegerField('id', readonly=True)
    is_deleted = BooleanField('is_deleted', default=False, readonly=True)
    owner = CharField(readonly=True)
    tracking_code = CharField(readonly=True)
    piggyback_url = CharField(readonly=True)

    class Meta:
        authorization = Auth('owner')
        allowed_methods = ('get', 'post', 'get', 'put', 'delete')
        always_return_data = True
        filtering = {
            "is_deleted": (ALL)
        }
        fields = ('name', 'id_random')
        validation = FormValidation(form_class=AudienceForm)
        queryset = Audience.objects.all()
        resource_name = 'audience'

    def hydrate(self, bundle):
        bundle.obj.owner = bundle.request.user.account
        return bundle

    def dehydrate(self, bundle):
        # We need to use public_id here
        public_id = bundle.obj.public_id
        bundle.data['tracking_code'] = get_audience_code(public_id)
        bundle.data['piggyback_url'] = get_audience_piggyback_url(public_id)
        return bundle


class BrandValidation(Validation):
    """ Validation that checks Brand. """

    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'No data has been given.'}

        errors = {}

        if is_not_exist_or_null('page_name', bundle.data):
            errors['Page Name'] = ['Please, provide a Page Name']

        if is_not_exist_or_null('brand_id', bundle.data):
            errors['AppNexus Brand ID'] = ['Please, provide a AppNexus Brand ID']
        elif not isinstance(bundle.data['brand_id'], int) and not bundle.data['brand_id'].isdigit():
            errors['AppNexus Brand ID'] = ['AppNexus Brand ID should contain only digits']

        if is_not_exist_or_null('facebook_page_id', bundle.data):
            errors['Page ID'] = ['Please, provide a Page ID']
        elif not bundle.data['facebook_page_id'].isdigit():
            errors['Page ID'] = ['Page ID should contain only digits']

        return errors


class BrandResource(ProtectedModelResource):

    class Meta:
        resource_name = 'brand'
        authorization = Auth('owner')
        allowed_methods = ('get', 'post', 'get', 'put', 'delete')
        always_return_data = True
        filtering = {
            'is_deleted': (ALL),
            'appnexus_access_status': ('exact', 'startswith',),
        }
        validation = BrandValidation()
        queryset = Brand.objects.all()
        fields = ('brand_id', 'check_access_status', 'page_name')

    id = IntegerField('id', readonly=True)
    facebook_page_id = CharField('thirdparty_page_id')
    appnexus_access_status = CharField('appnexus_access_status', readonly=True)
    owner = CharField('owner', readonly=True)

    # Get only not deleted Brands
    def get_object_list(self, request):
        return super(BrandResource, self).get_object_list(request).filter(is_deleted=False)

    def raise_appnexus_error(self, request, error_msg):
        ""
        from tastypie.exceptions import ImmediateHttpResponse

        errors = {'brand': {'error': error_msg}}
        raise ImmediateHttpResponse(response=self.error_response(request, errors))

    def hydrate(self, bundle):
        bundle.obj.owner = bundle.request.user.account
        # Send for confirmation
        if bundle.data['check_access_status'] is True:
            bundle.obj.appnexus_access_status = ACCESS_STATUS['pending']

        return bundle

    # Before save call AppNexus API to check brand id and facebook page id
    def save(self, bundle, skip_errors=False):
        if bundle.request.method == 'POST':
            self.is_valid(bundle)

            if not bundle.errors:
                result = bundle.obj.update_access_status()
                if 'error' in result:
                    self.raise_appnexus_error(bundle.request, result['error'])

        return super(BrandResource, self).save(bundle, skip_errors)

    def dehydrate_appnexus_access_status(self, bundle):
        return bundle.obj.get_appnexus_access_status_display()

    def dehydrate(self, bundle):
        return bundle
