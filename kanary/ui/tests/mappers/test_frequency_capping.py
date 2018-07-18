import cPickle
import pytest

from etc import redis_keys
from ui.cache.tasks import trigger_cache_mappings
from ui.campaign.models import Campaign, Advert


def check_ads_capping(redisdb, value):
    for advert in Advert.objects.all():
        ad = redisdb.hget(redis_keys.ads, advert.public_id)
        ad = cPickle.loads(ad)

        assert ad.capping == value


@pytest.mark.parametrize('capping', [
    {},
    {'campaign': (100, 'year')},
    {'strategy': (100, 'hour')},
    {'ad': (100, 'day')},
    {'campaign': (100, 'day'), 'strategy': (50, 'day'), 'ad': (10, 'day')},
])
def test_advert_capping(app_audited, redisdb_targeting, redisdb_profiles, capping):
    if capping:
        for campaign in Campaign.objects.all():
            for cap_obj, (cap_limit, cap_period) in capping.items():
                if cap_obj == 'campaign':
                    campaign.cap_campaign_selected = True
                    campaign.cap_total = cap_limit
                    campaign.cap_total_period = cap_period
                elif cap_obj == 'strategy':
                    campaign.cap_strategy_selected = True
                    campaign.cap_strategy = cap_limit
                    campaign.cap_strategy_period = cap_period
                elif cap_obj == 'ad':
                    campaign.cap_creative_selected = True
                    campaign.cap_creative = cap_limit
                    campaign.cap_creative_period = cap_period
            campaign.save()

    trigger_cache_mappings()

    check_ads_capping(redisdb_targeting, capping)
