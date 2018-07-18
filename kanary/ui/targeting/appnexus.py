from django.db import models as m
from mptt.models import MPTTModel, TreeForeignKey

from adserving.bidder.appnexus_api import AppNexusAPI
from etc import dimensions
from ui.targeting.appnexus_base import AppNexusBase, AppNexusTargetValue
from ui.utils import chop


__all__ = [
    'AppNexusOS', 'AppNexusContentCategory', 'AppNexusSegment',
    'AppNexusCarrier', 'AppNexusDeviceMake', 'AppNexusDeviceModel'
]


class AppNexusOS(AppNexusBase, AppNexusTargetValue):

    api_method = AppNexusAPI.operating_systems
    dimension = dimensions.g_os

    platform_type = m.CharField(max_length=6)

    class Meta:
        app_label = 'targeting'


class AppNexusCarrier(AppNexusBase, AppNexusTargetValue):

    ''' Stores data about carriers (GSM network name and country or WiFi). '''

    api_method = AppNexusAPI.carriers
    dimension = dimensions.carrier

    # Blank in case of WiFi:
    country_name = m.CharField(max_length=30, blank=True)
    country_code = m.CharField(max_length=5, blank=True)

    class Meta:
        app_label = 'targeting'


class AppNexusDeviceMake(AppNexusBase, AppNexusTargetValue):

    '''Stores data about device makers (Producers)'''

    api_method = AppNexusAPI.device_makers
    dimension = dimensions.g_device

    class Meta:
        app_label = 'targeting'


class AppNexusDeviceModel(AppNexusBase, AppNexusTargetValue):

    '''Stores data about device producers'''

    api_method = AppNexusAPI.device_models
    dimension = dimensions.g_device

    make_appnexus_id = m.PositiveIntegerField(null=True)
    # eg. "pc", "phone", or "tablet"
    device_type = m.CharField(max_length=6, blank=True)
    screen_width = m.PositiveSmallIntegerField(null=True)
    screen_height = m.PositiveSmallIntegerField(null=True)

    class Meta:
        app_label = 'targeting'

        unique_together = (
            ('name', 'make_appnexus_id'),
        )

    @property
    def maker(self):
        '''
        :returns: corresponding AppNexusDeviceMake object
        :rtype: ui.targeting.models.AppNexusDeviceMake
        '''
        try:
            return AppNexusDeviceMake.objects.get(
                appnexus_id=self.make_appnexus_id)
        except AppNexusDeviceMake.DoesNotExist:
            return False

    @property
    def translated_target_value(self):
        maker = self.maker
        if maker:
            return [maker.name, self.name]
        else:
            return []

    @property
    def raw_target_value(self):
        maker = self.maker
        if maker:
            return [unicode(maker.appnexus_id), unicode(self.appnexus_id)]
        else:
            return []


# The following classes are not yet used for frontend presentation
# They are only stored in database.
class AppNexusContentCategory(MPTTModel, AppNexusBase):

    """Pets & Animals, Fun & Trivia, etc."""

    api_method = AppNexusAPI.content_categories

    is_system = m.BooleanField(default=False)
    description = m.TextField(null=True)
    parent = TreeForeignKey('self', related_name='children', null=True,
                            blank=True)

    class Meta:
        app_label = 'targeting'


class BrandProtectionManager(m.Manager):

    def brand_protection(self):
        return self.get_query_set().filter(name__startswith='Brand Protection')


class AppNexusSegment(AppNexusBase):

    '''Stores data about proximic segments.'''

    objects = BrandProtectionManager()
    api_method = AppNexusAPI.segments

    class Meta:
        app_label = 'targeting'

    @property
    def display_name(self):
        last_category_name = self.name.split("::")[-1]
        return chop(last_category_name, '(proximic)')
