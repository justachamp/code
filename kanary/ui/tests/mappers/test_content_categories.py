import cPickle

from etc import redis_keys
from ui.cache.tasks import trigger_cache_mappings
from ui.campaign.models import Strategy, Advert
from ui.targeting.models import ContentCategory


def check_target_values(redisdb, content_categories, include=True):
    """
    :param redis.client.Redis redisdb: redis client
    :param list content_categories: a list with \
        instances of :class:`ContentCategory`
    :param bool exclude: if True checks target_values key \
        else target_values_exclude key
    """

    for advert in Advert.objects.all():

        ad = redisdb.hget(redis_keys.ads, advert.public_id)
        ad = cPickle.loads(ad)

        for category in content_categories:
            for raw_category in category.represented.all():
                raw_name = int(raw_category.name) if str(raw_category.name).isdigit() else raw_category.name
                assert raw_name in getattr(ad.content_category, 'include' if include else 'exclude')


def test_content_categories(app_audited, redisdb_targeting, redisdb_profiles):
    """
    Checks redis targeting (content categories - include and exclude).
    """
    content_categories = ContentCategory.objects.all()

    for strategy in Strategy.objects.all():
        strategy.content_category_values = content_categories
    trigger_cache_mappings()

    check_target_values(redisdb_targeting, content_categories)

    for strategy in Strategy.objects.all():
        strategy.content_category_values.clear()
        strategy.content_category_values_exclude = content_categories
    trigger_cache_mappings()

    check_target_values(redisdb_targeting, content_categories, include=False)
