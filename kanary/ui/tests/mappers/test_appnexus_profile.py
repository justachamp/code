import pytest
from mock import patch

from ui.cache.tasks import trigger_cache_mappings
from ui.campaign.models import Strategy
from ui.campaign.appnexus_profile_updater import WEB_TYPES, MOBILE_TYPES, SUPPLY_TYPES, build_profile
from ui.targeting.models import TargetValue, TargetMap, SegmentProximicSafetyLevel
from etc.config import settings
from etc import dimensions
from bidrequest.constants import EXCHANGES


@pytest.fixture
def clean_strategy(app_audited):

    Strategy.objects.all().update(is_paused=True)

    for strategy in Strategy.objects.all():
        # let's clear strategy's settings!
        strategy.targeting_values.clear()

    return app_audited

nothing_set_profile = {
    'id': settings.appnexus_profile_id,
    'size_targets': [],
    'country_action': 'exclude',
    'country_targets': [],
    'region_action': 'exclude',
    'region_targets': [],
    'segment_boolean_operator': 'or',
    'segment_targets': [],
    'supply_type_action': 'include',
    'supply_type_targets': list(WEB_TYPES | MOBILE_TYPES),
    'description': 'Automatic profile (off)',
    'passthrough_percent': 0
}


def check_update_response(expected_response):
    '''
    Checking response from profile updater.

    :param dict expected_response: dictionary with updated profile fields.
    '''
    profile_settings = build_profile()
    # things to update
    assert profile_settings == expected_response


def test_appnexus_profile_notset(app_noaudit):
    """Check empty appnexus_profile."""

    check_update_response(nothing_set_profile)


def test_appnexus_profile_update(clean_strategy):
    '''
    1. Checking if celery task is setting the correct data through API.
    2. Checking if celery task is fired (by cache mapper) after changing targeting in strategy
    '''

    # undeleting one strategy
    strategy = Strategy.objects.all()[0]
    strategy.is_paused = False
    strategy.save()

    expected_response = nothing_set_profile.copy()
    expected_response['description'] = 'Automatic profile (on)'
    expected_response['passthrough_percent'] = settings.appnexus_profile_passthrough
    expected_response['supply_type_targets'] = list(SUPPLY_TYPES[strategy.type])

    # checking ads sizes
    expected_response['size_targets'] = [{'height': 90, 'width': 728}]
    check_update_response(expected_response)

    # setting targeting on USA
    usa_appnexus = TargetValue.objects.create(
        exchange=EXCHANGES.appnexus,
        category=dimensions.g_location,
        value=TargetMap.pack(['USA', None, None]),
    )
    strategy.targeting_values.add(usa_appnexus)

    # setting targeting on Germany in Nexage
    germany_nexage = TargetValue.objects.create(
        exchange=EXCHANGES.nexage,
        category=dimensions.g_location,
        value=TargetMap.pack(['Germany', None, None]),
    )

    # setting AppNexus representant for Nexage country
    germany_appnexus = TargetValue.objects.create(
        exchange=EXCHANGES.appnexus,
        category=dimensions.g_location,
        value=TargetMap.pack(['GER', None, None]),
        representant=germany_nexage
    )

    # setting targeting on Germany from Nexage
    strategy.targeting_values.add(germany_nexage)

    # checking countries targeting
    expected_response['country_action'] = 'include'
    expected_response['country_targets'] = [{'country': 'GER'}, {'country': 'USA'}]
    check_update_response(expected_response)

    # changing country to region
    germany_nexage.value = TargetMap.pack(['Germany', 'LT', None])
    germany_nexage.save()
    germany_appnexus.value = TargetMap.pack(['GER', 'LT', None])
    germany_appnexus.save()

    # setting AppNexus representant for Nexage region in USA
    # (chenging country to region)
    usa_appnexus.value = TargetMap.pack(['USA', 'FL', None])
    usa_appnexus.save()

    expected_response['region_action'] = 'include'
    expected_response['region_targets'] = [{'region': 'USA:FL'}, {'region': 'GER:LT'}]
    check_update_response(expected_response)

    # setting targeting on Proximic Safety Level segment
    FAKE_APPNEXUS_ID = 330728
    strategy.segment_proximic_safety_level.add(SegmentProximicSafetyLevel.objects.create(
        appnexus_id=FAKE_APPNEXUS_ID,
        name='Safe from Adult'
    ))

    # checking segments targeting
    expected_response['segment_boolean_operator'] = 'or'
    expected_response['segment_targets'] = [{'id': FAKE_APPNEXUS_ID, 'action': 'include'}]
    check_update_response(expected_response)

    # checking if celery task is triggered (inside cache mapper)
    # after changes in strategy
    with patch('ui.campaign.tasks.appnexus_update_profile.delay') as mock_task:
        assert mock_task.call_count == 0
        # strategy changes, we should update AppNexus profile
        trigger_cache_mappings()
        assert mock_task.call_count == 1
        # no changes - no task
        trigger_cache_mappings()
        assert mock_task.call_count == 1

    # Remove all adverts from strategies and check if profile is empty
    for strategy in Strategy.objects.all():
        for advert in strategy.advert_set.all():
            advert.delete()

    check_update_response(nothing_set_profile)
