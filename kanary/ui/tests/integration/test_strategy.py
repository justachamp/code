from functools import partial

import pytest
from django.core.exceptions import ValidationError

from etc import dimensions
from ui.targeting.models import TargetValue
from ui.campaign.models import Strategy
from ui.storage.models import Creative


def test_strategy_type_specific_targeting(running_app, search_engine):
    '''
    Check if device targeting is not saved in website campaign
    '''
    os = partial(TargetValue.objects.create, category=dimensions.g_os)
    carrier = partial(TargetValue.objects.create, category=dimensions.carrier)
    device = partial(TargetValue.objects.create, category=dimensions.g_device)

    os_android = os(value='Android')
    os_symbian = os(value='Symbian')
    carrier_orange = carrier(value='Orange')
    carrier_vodafone = carrier(value='Vodafone')
    device_sony = device(value='Sony Xperia Z')
    device_nexus = device(value='Nexus 5')

    targeting = {
        'os_include': [{'id': os_android.id}],
        'os_exclude': [{'id': os_symbian.id}],
        'carrier_include': [{'id': carrier_orange.id}],
        'carrier_exclude': [{'id': carrier_vodafone.id}],
        'device_include': [{'id': device_sony.id}],
        'device_exclude': [{'id': device_nexus.id}]
    }

    def check_target_values(strategy, target_values, exclude=False):
        strategy_target_values = []
        if not exclude:
            strategy_target_values = strategy.targeting_values
        else:
            strategy_target_values = strategy.targeting_values_exclude

        assert sorted(strategy_target_values.values_list('id', 'value')) == \
               sorted([(t.id, t.value) for t in target_values])

    # Set strategy type to SITE
    strategy = Strategy.objects.first()
    strategy.type = Strategy.SITE
    strategy.save()

    check_target_values(strategy, [])
    check_target_values(strategy, [], exclude=True)

    # Save targeting
    strategy.search_fields_def = targeting
    strategy.save()

    # Device targets should not be saved
    check_target_values(strategy, [os_android, carrier_orange])
    check_target_values(strategy, [os_symbian, carrier_vodafone], exclude=True)

    # Change strategy type to MOBILE
    strategy.type = Strategy.MOBILE
    strategy.save()

    # Save targeting
    strategy.search_fields_def = targeting
    strategy.save()

    # Device targets should be saved
    check_target_values(strategy, [os_android, carrier_orange, device_sony])
    check_target_values(strategy, [os_symbian, carrier_vodafone, device_nexus], exclude=True)


def test_adverts_def(running_app):
    '''
    Checks if adding and updating adverts in strategy set
    via adverts_def property is working properly.
    '''
    # strategy to change advert set
    strategy = Strategy.objects.all()[0]
    # creative used in new advert
    creative = Creative.objects.all()[0]
    # advert that will be updated
    advert = strategy.advert_set.all()[0]

    old_adverts_count = strategy.advert_set.count()

    # Some advert related properties to save
    new_creative_pixel = 'new_pixel_code'
    updated_creative_pixel = 'updated_pixel_code'

    new_advert = {
        "advert_id": 0,
        "bid_custom": None,
        "bid_day_parting": [],
        "bid_type": "default",
        "custom_variable": "?test=4",
        "creative_id": creative.id,
        "creative_name": creative.name,
        "creative_path": creative.api_data,
        "creative_type": creative.type,
        "landing_page_url": "http://www.google.com",
        "js_code": "",
        "custom_pixel": new_creative_pixel,
    }

    advert_to_update = {
        "advert_id": advert.id,
        "bid_custom": None,
        "bid_day_parting": [],
        "bid_type": "default",
        "custom_variable": "?test=4",
        "creative_id": advert.creative.id,
        "creative_name": advert.creative.name,
        "creative_path": advert.creative.api_data,
        "creative_type": advert.creative.type,
        "landing_page_url": advert.landing_site.url,
        "js_code": "",
        "custom_pixel": updated_creative_pixel,
    }

    # Add adverts to strategy
    strategy.adverts_def = [new_advert, advert_to_update]

    # One creative added, one updated
    assert strategy.advert_set.count() == old_adverts_count + 1

    custom_pixels = [ad.custom_pixel for ad in strategy.advert_set.all()]

    assert new_creative_pixel in custom_pixels
    assert updated_creative_pixel in custom_pixels


def test_adverts_def_invalid(running_app):
    '''
    Checks if trying to save invalid advert will raise proper error.
    '''
    strategy = Strategy.objects.all()[0]

    invalid_advert = {
        "advert_id": 0,
        "bid_custom": None,
        "bid_day_parting": [],
        "bid_type": "default",
        "custom_variable": "?test=4",
        "creative_id": 0,
        "creative_name": "No type creative",
        "creative_path": "/temp/path",
        "creative_type": "",
        "landing_page_url": "http://www.notype.pl",
        "js_code": "",
        "custom_pixel": ""
    }

    with pytest.raises(ValidationError):
        strategy.adverts_def = [invalid_advert]
