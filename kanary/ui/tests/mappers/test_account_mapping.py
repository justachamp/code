import cPickle

from etc import redis_keys
from ui.cache.tasks import trigger_cache_mappings
from ui.campaign.models import Advert
from ui.account.models import Account
from adserving.bidder.spendings import cast_currency_to_CPM


def test_accountdetail_advert(app_audited, redisdb_profiles, redisdb_targeting, redisdb_optimizer):
    """
    Check if cached_ad has correct information stored on.
    """
    trigger_cache_mappings()
    for advert in Advert.objects.all():
        cached_ad = cPickle.loads(
            redisdb_targeting.hget(redis_keys.ads, advert.public_id))
        assert cached_ad.account_budget == cast_currency_to_CPM(advert.creative.owner.total_paid())
        assert cached_ad.account_fees == cast_currency_to_CPM(advert.creative.owner.audit_fees)
        assert cached_ad.account_id == advert.creative.owner.public_id

    account = Account.objects.first()
    account.audit_fees = 1
    account.save()
    trigger_cache_mappings()

    for advert in Advert.objects.all():
        cached_ad = cPickle.loads(
            redisdb_targeting.hget(redis_keys.ads, advert.public_id))
        assert cached_ad.account_budget == cast_currency_to_CPM(advert.creative.owner.total_paid())
        assert cached_ad.account_fees == cast_currency_to_CPM(1)
        assert cached_ad.account_id == advert.creative.owner.public_id
