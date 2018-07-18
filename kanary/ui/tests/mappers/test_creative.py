import pytest
import cPickle
from mock import patch

from etc import redis_keys
from ui.cache.tasks import trigger_cache_mappings
from ui.campaign.models import Advert, Site
from ui.storage.models import CreativeVideo

from bidrequest.constants import VideoDuration


def save_advert(strategy, creative, landing_site):
    return Advert.objects.create(
        strategy=strategy, creative=creative, landing_site=landing_site)


def assert_sites_in_cache(redis, model, not_sites=None):
    cached = redis.hget(redis_keys.ads, model.public_id)
    cached = cPickle.loads(cached)
    sites = [tuple(t) for t in model.landing_sites_ratios]
    assert cached['landing_sites'] == sites

    if not_sites:
        assert not_sites not in cached['landing_sites']
    return cached


@pytest.mark.celery
def test_creative_types_cached(redisdb_adserver, redisdb_profiles, audit_app):
    '''
        - check if all creatives gets cached when needed
    '''

    creative = audit_app.models['creative']['creative_image_1']
    creative_flash = audit_app.models['creative']['creative_flash_1']
    trigger_cache_mappings()

    cached = assert_sites_in_cache(redisdb_adserver, creative)
    assert cached['type'] == creative.type

    cached = assert_sites_in_cache(redisdb_adserver, creative_flash)
    assert cached['type'] == creative_flash.type


@pytest.mark.celery
def test_creative_mapping_landing_sites(redisdb_adserver, redisdb_profiles, audit_app):
    '''
        - Creates advert with creative for given strategy in one campaign
        - Checks if creative got it's landing_site_url in cache
        - Creates different advert for strategy from different campaign with
        same creative
        - Checks if creative has it's landing_site_url in cache, and if it
        wasn't switched
    '''

    creative = audit_app.models['creative']['creative_image_1']
    strategy = audit_app.models['strategy']['Hello this is Citrus']
    roast_strategy = audit_app.models['strategy']['Roast beef']
    save_advert(
        strategy=strategy,
        creative=creative,
        landing_site=Site.objects.get(url='http://www.google.com/',
                                      owner=strategy.campaign.account)
    )
    creative.appnexus_set_audited()

    trigger_cache_mappings()
    assert_sites_in_cache(redisdb_adserver, creative)

    raw_advert = save_advert(
        strategy=roast_strategy,
        creative=creative,
        landing_site=Site.objects.get(url='http://www.onet.com/',
                                      owner=roast_strategy.campaign.account)
    )

    trigger_cache_mappings()
    # other site is from the second campaign.
    # Creative should retain first pinned site,
    # and that's what should be in cache
    other_site_ratings = [raw_advert.landing_site, 1]
    assert_sites_in_cache(redisdb_adserver, creative,
                          not_sites=other_site_ratings)


@pytest.mark.parametrize('duration, appnexus_duration', [
    (11, VideoDuration.VAST_OTHER),
    (20, VideoDuration.VAST_OTHER),
    (15, VideoDuration.VAST_15_SEC),
    (30, VideoDuration.VAST_30_SEC),
])
def test_video_creative_adverts_mapping(video_creative_db, duration, appnexus_duration):
    """Test video creative mapping."""
    creative = video_creative_db.models['creative']['creative_video_1']
    creative.duration = duration

    assert creative.width != 1
    assert creative.height != 1

    ad = creative.advert_set.first()
    # Special video sizes:
    assert ad.width == 1
    assert ad.height == 1

    assert ad.duration == appnexus_duration

    # Make it running. We care about mapped duration and size, not about the state.
    with patch.object(ad.state.__class__, 'is_running', True):
        target_ad = ad.cache_map.mapped_targeting()
        assert target_ad.durations.include == appnexus_duration
        assert target_ad.durations.excludes is False
        assert target_ad.width == 1
        assert target_ad.height == 1


def test_video_creatives_adserver_mapping(video_creative_db, redisdb_adserver, redisdb_profiles):
    """Test for correct CreativeVideo mapping to adserver."""
    video = CreativeVideo.objects.first()
    trigger_cache_mappings()
    video_adserver = cPickle.loads(redisdb_adserver.hget(redis_keys.ads, video.public_id))

    assert 'mediafiles_secure' in video_adserver
    assert 'mediafiles' in video_adserver
    assert 'duration' in video_adserver
    assert video_adserver['mediafiles_secure'] == video.media_variants_secure
    assert video_adserver['mediafiles'] == video.media_variants
