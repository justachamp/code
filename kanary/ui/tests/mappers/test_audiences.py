import cPickle

import pytest

from ui.campaign.models import Advert, Strategy
from ui.storage.models import Audience
from ui.cache.tasks import trigger_cache_mappings
from etc import redis_keys


@pytest.fixture(autouse=True)
def module_fixture(app_audited_audiences, redisdb_profiles):
    pass


def test_strategy_audience_is_ip(redisdb_targeting):

    strategy = Strategy.objects.first()
    audiences = Audience.objects.all()
    strategy.audiences = audiences
    strategy.save()

    trigger_cache_mappings()
    advert = strategy.advert_set.first()
    cache_ad = cPickle.loads(redisdb_targeting.hget(redis_keys.ads, advert.public_id))
    assert cache_ad.has_ip_audiences is False

    ip_audience = Audience.objects.first()
    ip_audience.is_ip = True
    ip_audience.save()

    trigger_cache_mappings()
    cache_ad = cPickle.loads(redisdb_targeting.hget(redis_keys.ads, advert.public_id))
    assert cache_ad.has_ip_audiences is True




@pytest.mark.parametrize('included', (True, False))
def test_strategy_audience_add(redisdb_targeting, included):

    strategy = Strategy.objects.first()
    audiences = Audience.objects.all()
    if included:
        strategy.audiences = audiences
    else:
        strategy.audiences_exclude = audiences
    strategy.save()

    trigger_cache_mappings()
    for advert in Advert.objects.all():
        cache_ad = cPickle.loads(redisdb_targeting.hget(redis_keys.ads, advert.public_id))
        aud_include = frozenset(advert.strategy.get_audience_ids())
        aud_exclude = frozenset(advert.strategy.get_audience_ids(exclude=True))
        assert cache_ad.audiences_include == aud_include
        assert cache_ad.audiences_exclude == aud_exclude


@pytest.mark.parametrize('included', (True, False))
def test_strategy_audience_remove(redisdb_targeting, included):

    strategy = Strategy.objects.first()
    audiences = Audience.objects.all()
    if included:
        strategy.audiences = audiences
    else:
        strategy.audiences_exclude = audiences
    strategy.save()

    trigger_cache_mappings()

    if included:
        strategy.audiences.remove(audiences[0])
    else:
        strategy.audiences_exclude.remove(audiences[0])
    strategy.save()

    trigger_cache_mappings()
    for advert in Advert.objects.all():
        cache_ad = cPickle.loads(redisdb_targeting.hget(redis_keys.ads, advert.public_id))
        aud_include = frozenset(advert.strategy.get_audience_ids())
        aud_exclude = frozenset(advert.strategy.get_audience_ids(exclude=True))
        assert cache_ad.audiences_include == aud_include
        assert cache_ad.audiences_exclude == aud_exclude
        if included:
            assert audiences[0] not in aud_include
        else:
            assert audiences[0] not in aud_exclude
