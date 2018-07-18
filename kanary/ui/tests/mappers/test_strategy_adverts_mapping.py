import cPickle
from operator import attrgetter
from datetime import time
from collections import OrderedDict

from mock import patch
import pytest

from adserving.bidder.targeting.constants import PROXIMIC, PEER39, LOTAME, LOTAME_SEGMENT_APPNEXUS_ID
from adserving.types import Decimal
from etc import redis_keys, dimensions
from ui.cache.tasks import trigger_cache_mappings
from ui.campaign.models import Advert, Strategy, BiddingPeriod, AdvertPeriod


def test_advert_is_running(request, app_noaudit, redisdb_profiles, redisdb_targeting):
    """ Checks if is_running flag of Advert object is correctly mapped in
    strategy dict inside cache i.e. there should be only audited Adverts
    (creatives).
    """

    # run celery task (in should be run in parallel celery beat)
    trigger_cache_mappings()

    assert (redisdb_targeting.hkeys(redis_keys.ads) == [],
            'There shouldn\'t be any running adverts')

    # simulate creative audit to change its is_running flag underneath
    for strategy in Strategy.objects.all():
        for advert in strategy.advert_set.all():
            advert.creative.appnexus_set_audited()
            advert.creative.save()

    # run celery task
    trigger_cache_mappings()

    assert (redisdb_targeting.hkeys(redis_keys.ads) != [],
            'There should be some adverts in redis')
    # simulate creative audit to change its is_running flag underneath

    # deactivate and check if adverts have been removed
    for strategy in Strategy.objects.all():
        strategy.is_paused = True
        strategy.save()

    trigger_cache_mappings()

    assert (redisdb_targeting.hkeys(redis_keys.ads) == [],
            'There shouldn\'t be any running adverts')


def test_bidding_period_change(request, app_audited, redisdb_profiles,
                               redisdb_targeting):
    """ Checks if changing bidding periods affects redis cached strategy """

    strategy = Strategy.objects.all()[0]
    ad = strategy.advert_set.all()[0]
    Advert.objects.exclude(pk=ad.pk).delete()

    # run celery task
    trigger_cache_mappings()

    ads = redisdb_targeting.hgetall(redis_keys.ads)

    # change some periods
    period = BiddingPeriod.objects.create(
        start=time(13, 45),
        end=time(16, 30),
        strategy=strategy,
    )
    strategy.biddingperiod_set.add(period)

    ad_period = AdvertPeriod.objects.create(
        advert=ad,
        period=period,
        custom_bid_CPM=1,
    )
    ad.advertperiod_set.add(ad_period)

    # run celery task
    trigger_cache_mappings()

    # ads should be now updated
    ads_after_change = redisdb_targeting.hgetall(redis_keys.ads)

    assert ads != ads_after_change

    loaded_change_ad = cPickle.loads(ads_after_change[ad.public_id])

    # list of quarters we targeted
    targeted_quarters = list(loaded_change_ad.quarter.include)
    # it comes from set, let us sort it since sets don't have order!
    targeted_quarters.sort()

    ad_quarters = [q[0] for q in ad.get_quarters()]

    # Check if we don't save a one period too much.
    assert ad_quarters[-1].endswith('15')
    assert targeted_quarters == ad_quarters


def test_bidding_targetvalues(app_audited, redisdb_profiles, redisdb_targeting):
    """Check proper target values being set up on advert."""

    strategy = Strategy.objects.all()[0]
    ad = strategy.advert_set.all()[0]

    trigger_cache_mappings()

    loaded_ad = cPickle.loads(redisdb_targeting.hget(redis_keys.ads, ad.public_id))

    assert loaded_ad.inventory.include == ad.strategy.type

    # --------------------------------------------------------------------------
    # we repeat functionality of AdvertCacheMap.targetvalues_dimension_values
    # To actually check if it's working correctly.
    # It's done for age_group, location, and os dimensions
    # --------------------------------------------------------------------------

    age_group_include = set()
    for age_group in ad.strategy.targeting_values.representants().filter(category=dimensions.age_group).all():
        for raw in age_group.read_represented():
            age_group_include.add(raw.value_list[0])

    age_group_exclude = set()
    for age_group in ad.strategy.targeting_values_exclude.representants().filter(category=dimensions.age_group).all():
        for raw in age_group.read_represented():
            age_group_exclude.add(raw.value_list[0])

    assert loaded_ad.age_group.excludes is False
    assert loaded_ad.age_group.values == age_group_include - age_group_exclude

    country_include = set()
    country_region_include = set()
    country_region_city_include = set()
    for location in ad.strategy.targeting_values.representants().filter(category=dimensions.g_location).all():
        for raw in location.read_represented():
            for i, element in enumerate(raw.value_list, 1):
                raw_list = tuple(raw.value_list[:i])
                if len(raw_list) == 1:
                    country_include.add(raw_list[0])
                elif len(raw_list) == 2:
                    country_region_include.add(raw_list)
                else:
                    country_region_city_include.add(raw_list)

    country_exclude = set()
    country_region_exclude = set()
    country_region_city_exclude = set()
    for location in ad.strategy.targeting_values_exclude.representants().filter(category=dimensions.g_location).all():
        for raw in location.read_represented():
            raw_list = tuple(raw.value_list)
            if len(raw_list) == 1:
                country_exclude.add(raw_list[0])
            elif len(raw_list) == 2:
                country_region_exclude.add(raw_list)
            else:
                country_region_city_exclude.add(raw_list)

    assert loaded_ad.country.excludes is False
    assert loaded_ad.country_region.excludes is False
    assert loaded_ad.country_region_city.excludes is False
    assert set(loaded_ad.country.values) == country_include - country_exclude
    assert set(loaded_ad.country_region.values) == country_region_include - country_region_exclude
    assert set(loaded_ad.country_region_city.values) == country_region_city_include - country_region_city_exclude

    os_include = set()
    os_name_version_include = set()
    for os in ad.strategy.targeting_values.representants().filter(category=dimensions.g_os).all():
        for raw in os.read_represented():
            for i, element in enumerate(raw.value_list, 1):
                raw_list = tuple(raw.value_list[:i])
                if len(raw_list) == 1:
                    os_include.add(raw_list[0])
                else:
                    os_name_version_include.add(raw_list)

    os_exclude = set()
    os_name_version_exclude = set()
    for os in ad.strategy.targeting_values_exclude.representants().filter(category=dimensions.g_os).all():
        for raw in os.read_represented():
            raw_list = tuple(raw.value_list)
            if len(raw_list) == 1:
                os_exclude.add(raw_list[0])
            else:
                os_name_version_exclude.add(raw_list)

    assert loaded_ad.os_name.excludes is True
    assert loaded_ad.os_name_version.excludes is True
    assert set(loaded_ad.os_name.values) == os_exclude
    assert set(loaded_ad.os_name_version.values) == os_name_version_exclude

    assert len(os_include) == 0
    assert len(os_name_version_include) == 0

    assert len(loaded_ad.network_publisher.values) == 0
    assert len(loaded_ad.quarter.values) == 0
    assert len(loaded_ad.carrier.values) == 0
    assert len(loaded_ad.gender.values) == 0
    assert len(loaded_ad.content_category.include) == 0
    assert len(loaded_ad.content_category.exclude) == 0


def test_bidding_publishers(app_audited_publisherset, redisdb_profiles, redisdb_targeting):
    """Check for proper publishers being set on advert."""

    strategy = Strategy.objects.all()[0]
    ad = strategy.advert_set.all()[0]

    for excludes in (False, True):

        # set proper blacklist value
        strategy.publisherset.blacklist = excludes
        # save publisherset
        strategy.publisherset.save()
        trigger_cache_mappings()

        # load cached ad
        loaded_ad = cPickle.loads(redisdb_targeting.hget(redis_keys.ads, ad.public_id))

        assert loaded_ad.network.excludes is excludes
        if excludes is False:
            # includes generates its' values all levels of sub-dimensions
            assert len(loaded_ad.network.values) == 2
        else:
            # excludes set only it's own level
            assert len(loaded_ad.network.values) == 0

        assert loaded_ad.network_publisher.excludes is excludes
        assert len(loaded_ad.network_publisher.values) == 2


def test_data_cost_precalculation(app_audited, segments):
    """Test validity of precalculated data cost."""

    # If segment prices change, this test may stop testing price calculation functions.
    # The prices must be different because otherwise many wrong algorithms would yield a good result.
    # E.g first(prices), choice(prices), max(prices), min(prices), median(prices), avg(prices) all return
    # 1 when prices are all equal to 1 while only max is OK.
    # So we first check if the prices tend to differ.
    assert segments['SegmentProximicMaturityRating'].PRICE_CPM == Decimal('0.05')
    assert segments['SegmentProximicPagePlacement'].PRICE_CPM == Decimal('0.1')
    assert segments['SegmentProximicPageLanguage'].PRICE_CPM == Decimal('0.05')
    assert segments['Peer39PageLanguage'].PRICE_CPM == Decimal('0.05')
    assert segments['LotameDemographic'].PRICE_CPM == Decimal('0.25')
    assert segments['LotameBehavioralInterest'].PRICE_CPM == Decimal('0.75')
    assert segments['LotameInfluencers'].PRICE_CPM == Decimal(1)
    assert segments['LotameOffline'].PRICE_CPM == Decimal(1)

    strategy = Strategy.objects.first()
    ad = strategy.advert_set.first()

    expected_data_cost = OrderedDict([(PEER39, 0), (PROXIMIC, 0), (LOTAME, 0)])

    def check_expected_data_cost(lotame_segments=None):
        """
        Check segments mapping validity by directly comparing prices and checking
        if mapped lotame segment is one of segments in list.
        :param (list, NoneType) lotame_segments: list of Lotame segments the mapped segment
            id is choosen from
        """
        mapped_providers = ad.cache_map.mapped_targeting().data_providers
        assert isinstance(mapped_providers, OrderedDict)

        mapped_cost = mapped_providers.copy()
        del mapped_cost[LOTAME_SEGMENT_APPNEXUS_ID]
        assert mapped_cost == expected_data_cost

        if not lotame_segments:
            assert mapped_providers[LOTAME_SEGMENT_APPNEXUS_ID] is None
        else:
            assert mapped_providers[LOTAME_SEGMENT_APPNEXUS_ID] in [s.appnexus_id for s in lotame_segments]

    assert ad.state.is_running
    check_expected_data_cost()

    # We're adding segments consequently and checking if data providers' costs get updated:

    # Proximic segments:
    strategy.segment_proximic_maturity_rating_exclude.add(segments['SegmentProximicMaturityRating'])
    strategy.save()
    expected_data_cost[PROXIMIC] = Decimal('0.05')
    check_expected_data_cost()

    strategy.segment_proximic_page_placement.add(segments['SegmentProximicPagePlacement'])
    strategy.save()
    expected_data_cost[PROXIMIC] = Decimal('0.1')
    check_expected_data_cost()

    strategy.segment_proximic_page_language.add(segments['SegmentProximicPageLanguage'])
    strategy.save()
    # Data cost should not change - cost of SegmentProximicPageLanguage is lower than current proximic cost.
    check_expected_data_cost()

    # Peer39 segments:
    strategy.segment_peer_page_language.add(segments['Peer39PageLanguage'])
    strategy.save()
    expected_data_cost[PEER39] = Decimal('0.05')
    check_expected_data_cost()

    # Lotame segments:
    strategy.segment_lotame_demographic.add(segments['LotameDemographic'])
    strategy.save()
    expected_data_cost[LOTAME] = Decimal('0.25')
    check_expected_data_cost(lotame_segments=[segments['LotameDemographic']])

    strategy.segment_lotame_behavioral_interest_exclude.add(segments['LotameBehavioralInterest'])
    strategy.save()
    expected_data_cost[LOTAME] = Decimal('0.75')
    check_expected_data_cost(lotame_segments=[segments['LotameBehavioralInterest']])

    strategy.segment_lotame_influencers.add(segments['LotameInfluencers'])
    strategy.save()
    expected_data_cost[LOTAME] = Decimal(1)
    check_expected_data_cost(lotame_segments=[segments['LotameInfluencers']])

    # Test with 2 Lotame segments with same price equal to 1 CPM.
    # In that case the choice is random so test it multiple times to make sure we most probably
    # hit both cases - when LotameInfluencers xor LotameOffline is the choosen segment.
    for _ in xrange(100):  # 1 / (2^100) probablility that we hit the same segment all the times. Good enough.
        strategy.segment_lotame_offline.add(segments['LotameOffline'])
        strategy.save()
        expected_data_cost[LOTAME] = Decimal(1)
        check_expected_data_cost(lotame_segments=[segments['LotameInfluencers'], segments['LotameOffline']])


@pytest.mark.parametrize('segment_name, strategy_segment_slot, target_ad_segment_id_getter', [
    (
        'LotameBehavioralInterest',
        'segment_lotame_behavioral_interest_exclude',
        attrgetter('lotame_behavioral_interest.exclude'),
    ),
    (
        'LotameDemographic',
        'segment_lotame_demographic_exclude',
        attrgetter('lotame_demographic.exclude'),
    ),
    (
        'LotameInfluencers',
        'segment_lotame_influencers',
        attrgetter('lotame_influencers.include'),
    ),
])
def test_lotame_segments_mapping(redisdb_targeting, strategies, segments,
                                 segment_name, strategy_segment_slot, target_ad_segment_id_getter):
    """Check if segments attached to a strategy are mapped to TargetAd pickles in targeting redis as expected."""
    strategy = Strategy.objects.get(name='Strategy day parting 0')
    ad = strategy.advert_set.first()

    segment = segments[segment_name]
    getattr(strategy, strategy_segment_slot).add(segment)

    trigger_cache_mappings()

    target_ad = cPickle.loads(redisdb_targeting.hget(redis_keys.ads, ad.public_id))
    assert target_ad_segment_id_getter(target_ad) == {segment.appnexus_id}


@pytest.mark.parametrize('is_interest_based', [
    True,
    False
])
def test_is_interest_based(redisdb_targeting, strategies, is_interest_based):
    """
    Check if TargetAd.is_interest_based is correctly mapped to targeting redis

    Full unit test for Strategy.is_interest_based is placed in test_strategy module.
    """

    with patch.object(Strategy, 'is_interest_based', return_value=is_interest_based):
        ad = Advert.objects.first()

        trigger_cache_mappings()

        # Load cached advert from Redis
        loaded_ad = cPickle.loads(redisdb_targeting.hget(redis_keys.ads, ad.public_id))
        assert loaded_ad.is_interest_based == is_interest_based
