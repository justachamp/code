import pytest
import cPickle

from adserving.adserver import constants
from ui.cache.tasks import trigger_cache_mappings
from ui.campaign.models import Campaign


@pytest.fixture(autouse=True)
def module_fixture(app_audited, redisdb_profiles):
    pass


@pytest.mark.celery
def test_campaign_mapping_default_conv_values(campaigns, redisdb_adserver):
    ''' Test saving default conversion values to redis '''
    for index, campaign in enumerate(Campaign.objects.all()):
        conv = campaign.conversion_def
        conv.value = index + 1
        conv.save()

    trigger_cache_mappings()

    for index, campaign in enumerate(Campaign.objects.all()):
        rv = redisdb_adserver.hget(
            constants.campaign_default_conv_value_key, campaign.public_id)
        assert cPickle.loads(rv) == float(index + 1)
