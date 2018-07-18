import cPickle

import pytest

from etc import redis_keys
from ui.cache.tasks import trigger_cache_mappings
from ui.campaign.models import Advert
from ui.account.models import Account

from adserving.bidder import utils

from etc import constants


def check_commission(redisdb, commission):
    """
    Compares the value from the postgresql database to
    value from redis.

    :param redis.client.Redis redisdb: instance of Redis
    :param int commission: value of commission
    """
    for advert in Advert.objects.all():
        ad = redisdb.hget(redis_keys.ads, advert.public_id)
        ad = cPickle.loads(ad)

        commission_from_redis = utils.decrypt(ad.encrypted_commission)
        assert commission_from_redis == str(commission)

        hcommission_from_redis = utils.decrypt(ad.encrypted_hidden_commission)
        assert hcommission_from_redis == str(constants.HIDDEN_COMMISSION)


def test_default_commission(app_audited, redisdb_targeting):
    """
    Test default value of commission value.
    """
    trigger_cache_mappings()

    check_commission(redisdb_targeting, constants.COMMISSION)


@pytest.mark.parametrize("commission", (0, 40, 75, 100, 150))
def test_different_commission(app_audited, redisdb_targeting, commission):
    """
    Test different values for commission field.
    """
    for account in Account.objects.all():
        account.commission = commission
        account.save()

    trigger_cache_mappings()

    check_commission(redisdb_targeting, commission)
