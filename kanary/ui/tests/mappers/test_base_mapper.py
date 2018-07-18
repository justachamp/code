import pytest
import cPickle

from etc import redis_keys
from ui.cache.tasks import trigger_cache_mappings
from ui.campaign.models import Advert


@pytest.fixture(autouse=True)
def module_fixture(app_audited, redisdb_profiles):
    pass


@pytest.mark.celery
def test_advert_mapping_landing_sites(redisdb_targeting):
    trigger_cache_mappings()

    for advert in Advert.objects.all():
        target_ad = cPickle.loads(redisdb_targeting.hget(redis_keys.ads, advert.public_id))
        assert target_ad.landing_sites == [("http://google.pl", 1)]
