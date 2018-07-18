import pytest

from etc import dimensions
from ui.targeting.models import (
    TargetValue, AppNexusCarrier, AppNexusDeviceMake, AppNexusDeviceModel
)
from ui.targeting.appnexus_base import appnexus_targeting_update


@pytest.fixture
def carrier(db):
    carrier, _ = AppNexusCarrier.objects.get_or_create(
        appnexus_id=1500100900,
        name='thousand-fivehundred-hundred-ninehundred'
    )
    return carrier


def test_update_targetvalues_new(clean_targeting, carrier):
    """Completely new target values is being added."""

    AppNexusCarrier.update_targetvalues()

    # both raw and representant are added
    assert 2 == TargetValue.objects.count()
    assert 1 == TargetValue.objects.representants().count()
    assert 1 == TargetValue.objects.represented().count()


def test_update_targetvalues_id_as_representant(clean_targeting, carrier):
    """
    Consumer adds value as translated, that's supposed to be raw according to appnexus api.

    We convert to raw, and add proper representant.
    """
    # simulate creating representant in event consumer
    carriertv, _ = TargetValue.objects.get_or_create_representant(
        exchange='appnexus',
        category=AppNexusCarrier.dimension,
        value=[carrier.appnexus_id]
    )
    assert carriertv.is_representant is True

    targetvaluecount = TargetValue.objects.count()

    AppNexusCarrier.update_targetvalues()

    # new TargetValues representant added
    assert targetvaluecount + 1 == TargetValue.objects.count()

    # and former representant is now raw value
    carriertv = TargetValue.objects.get(pk=carriertv.pk)
    assert carriertv.is_representant is False


def test_update_targetvalues_id_is_representing(clean_targeting, carrier):
    """
    We have value that API expects to be raw (appnexus_id) but it's already representing other values.

    No conversion applicable.
    """
    # simulate creating representant in event consumer
    carriertv, _ = TargetValue.objects.get_or_create_representant(
        exchange='appnexus',
        category=AppNexusCarrier.dimension,
        value=[carrier.appnexus_id]
    )
    TargetValue.objects.create_value_with_representant(
        ['This is completely wrong'], carriertv
    )
    assert carriertv.is_representant is True

    targetvaluecount = TargetValue.objects.count()

    AppNexusCarrier.update_targetvalues()

    # new TargetValues representant added
    assert targetvaluecount + 1 == TargetValue.objects.count()

    # but not assigned a raw value
    carriertv = TargetValue.objects.get(pk=carriertv.pk)
    assert carriertv.is_representant is True


@pytest.mark.django_db
def test_appnexus_targeting_update(clean_targeting, appnexus_api_requests):
    appnexus_targeting_update()
    representants = TargetValue.objects.representants()
    represented = TargetValue.objects.represented()

    # Targeting update on clean targeting should insert both representants
    # and represented.
    representant_carriers_count = representants.filter(
        category=AppNexusCarrier.dimension).count()
    represented_carriers_count = represented.filter(
        category=AppNexusCarrier.dimension).count()

    # this assertion is due to two elements having different id.
    # we want to bid on both of them,
    # but user should see only one representation
    assert representant_carriers_count == (represented_carriers_count - 1)

    # there should be same ammount of raw values and AppNexusCarrier objects
    assert AppNexusCarrier.objects.count() == represented_carriers_count

    representant_devices_count = representants.filter(
        category=dimensions.g_device).count()
    represented_devices_count = represented.filter(
        category=dimensions.g_device).count()

    assert representant_devices_count == represented_devices_count

    api_devices_count = AppNexusDeviceMake.objects.count() + \
                        AppNexusDeviceModel.objects.count()

    assert representant_devices_count == api_devices_count


@pytest.mark.django_db
def test_appnexus_targeting_update_representant(clean_targeting, appnexus_api_requests):
    wifi, _ = TargetValue.objects.get_or_create_unrepresented(
        AppNexusCarrier.dimension, ['WIFI'], 'appnexus')
    assert wifi.is_representant is False
    appnexus_targeting_update()

    wifi, _ = TargetValue.objects.get_or_create_representant(
        AppNexusCarrier.dimension, ['WIFI'])
    assert wifi.is_representant is True
    representants = TargetValue.objects.representants()
    represented = TargetValue.objects.represented()

    # Targeting update on clean targeting should insert both representants
    # and represented.
    assert representants.count() == represented.count() - 1
