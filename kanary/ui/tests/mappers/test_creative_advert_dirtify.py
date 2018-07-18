import pytest

from mock import patch

from ui.cache.tasks import trigger_cache_mappings
from ui.campaign.models import Advert, Site
from ui.storage.models import Creative
from ui.storage.tasks import appnexus_update_status_all


@pytest.mark.parametrize("creative_type",
                         ("image", "flash", "video"))
@pytest.mark.django_db
@patch(
    'ui.storage.models.appnexus_api.creative',
    return_value={'audit_status': 'audited', 'audit_feedback': 'ok'}
)
def test_creative_audit_dirtify(creative_resource, audit_app, creative_type):
    """Test that Creative audit dirtifies the cache."""
    if creative_type == 'video':
        audit_app.setup_creative_videos()
    creative_name = 'creative_%s_1' % creative_type
    audit_app.setup_adverts(adverts=[
        {
            'name': 'ad_lemon',
            'strategy': 'Hello this is Citrus',
            'creative': creative_name,
            'url': 'http://www.google.com/',
        },
        {
            'name': 'ad_orange',
            'strategy': 'Hello this is Citrus',
            'creative': creative_name,
            'url': 'http://www.wp.pl/',
        },
        {
            'name': 'ad_carrot',
            'strategy': 'han i has a pumpkin?',
            'creative': creative_name,
            'url': 'http://www.google.com/',
        },
        {
            'name': 'ad_celery',
            'strategy': 'han i has a pumpkin?',
            'creative': creative_name,
            'url': 'http://www.wp.pl/',
        },
    ])
    creative = audit_app.models['creative'][creative_name]

    creative.appnexus_status = 'p'
    creative.save()

    trigger_cache_mappings()
    assert len(creative.advert_set.all()) > 0
    for ad in creative.advert_set.all():
        assert not ad.cache_is_dirty

    appnexus_update_status_all()
    assert creative.cache_is_dirty

    for ad in creative.advert_set.all():
        assert ad.cache_is_dirty
