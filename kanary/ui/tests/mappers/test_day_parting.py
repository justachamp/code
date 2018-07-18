import cPickle

from etc import redis_keys
from ui.cache.tasks import trigger_cache_mappings
from ui.campaign.models import Strategy, Advert


def check_ads_bid_value(redisdb, budget_size):
    ''' Checks if given budget is set properly in ads'''

    for advert in Advert.objects.all():
        ad = redisdb.hget(redis_keys.ads, advert.public_id)
        ad = cPickle.loads(ad)
        for bid in ad.bids.values():
            assert bid == budget_size


def test_default_bid_cpm_strategy(app_audited, redisdb_targeting, redisdb_profiles):
    '''Checks if bid values are properly written to cache from strategy'''

    budget_size = 99.

    for strategy in Strategy.objects.all():
        strategy.budget_bid_CPM = budget_size
        strategy.save()
    trigger_cache_mappings()

    check_ads_bid_value(redisdb_targeting, budget_size)


def test_default_bid_cpm_advert(app_audited, redisdb_targeting, redisdb_profiles):
    '''Checks if bid values are properly written to cache from advert'''
    budget_size = 989.

    for advert in Advert.objects.all():
        advert.custom_bid_CPM = budget_size
        advert.save()

    for strategy in Strategy.objects.all():
        strategy.budget_bid_CPM = int(budget_size * 2)
        strategy.save()

    trigger_cache_mappings()

    check_ads_bid_value(redisdb_targeting, budget_size)
