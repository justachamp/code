from urlparse import urlparse

import pytest

from ui.tests.utils import (
    DatabaseDataFactory, default_landing_page, default_campaign,
    default_strategies,
)
from adserving.types import Decimal
from ui.campaign.models import Advert, Site
from ui.storage.models import AppNexusCreative, STATUS, CreativeImage, CreativeFlash, CreativeVideo


@pytest.fixture
def audit_app(basic_fixture):
    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()

    landing_pages = default_landing_page + \
                    [{'owner': 'acc', 'url': 'http://www.onet.com/'}]
    setup.setup_landing_pages(landing_pages)

    campaigns = default_campaign + [
        {'name': 'Meat', 'account': 'acc', 'budget_total': 8000,
         'start_UTC': '2013-01-01T00:00', 'end_UTC': '2013-01-31T00:00',
         'landing_site': 'http://www.onet.com/'}
    ]
    setup.setup_campaigns(campaigns)
    strategies = default_strategies + [
        {'name': 'Roast beef', 'campaign': 'Meat', 'budget_total': 67676,
         'budget_bid_CPM': Decimal('0.1')}
    ]
    setup.setup_strategies(strategies)
    setup.setup_creative_images()
    return setup


def save_advert(strategy, creative, landing_site):
    return Advert.objects.create(
        strategy=strategy, creative=creative, landing_site=landing_site)


@pytest.mark.parametrize('status, is_attached, auditable', (
        (STATUS['no_audit'], True, True),
        (STATUS['pending'], True, False),
        (STATUS['rejected'], True, True),
        (STATUS['unauditable'], True, False),
        (STATUS['audited'], True, False),
        (STATUS['expired'], True, True),
        (STATUS['no_audit'], False, False),
        (STATUS['pending'], False, False),
        (STATUS['rejected'], False, False),
        (STATUS['unauditable'], False, False),
        (STATUS['audited'], False, False),
        (STATUS['expired'], False, False),
))
def test_is_auditable(status, is_attached, auditable):
    """Test correctness of is_auditable property."""
    creative = AppNexusCreative(appnexus_status=status)

    # simulate attaching creative to strategy (by adding landing site as in advert creation)
    # unattached creatives cannot be audited.
    if is_attached:
        creative.landing_site_url = 'http://some.of.strategy.sites.com'

    assert creative.is_auditable == auditable


@pytest.mark.django_db
def test_creative_with_landing_url(audit_app):
    '''
        - Creates advert with creative for given strategy in one campaign
        - Checks if creative got landing_site.url from strategy's campaign
        - Creates different advert for strategy from different campaign with
        same creative
        - Checks if creative still has landing_site.url from first strategy's
        campaign
    '''

    creative = audit_app.models['creative']['creative_image_1']
    strategy = audit_app.models['strategy']['Hello this is Citrus']
    roast_strategy = audit_app.models['strategy']['Roast beef']

    # not used in any advert, so attribute should be null
    assert not creative.landing_site_url

    save_advert(
        strategy=strategy,
        creative=creative,
        landing_site=Site.objects.get(url='http://www.google.com/',
                                      owner=strategy.campaign.account)
    )

    # connected to attribute, so it should be same
    assert creative.landing_site_url == strategy.campaign.landing_site.url

    save_advert(
        strategy=roast_strategy,
        creative=creative,
        landing_site=Site.objects.get(url='http://www.google.com/',
                                      owner=roast_strategy.campaign.account)
    )

    # creative should keep firstly connected site
    assert creative.landing_site_url == strategy.campaign.landing_site.url
    assert creative.landing_site_url != \
           roast_strategy.campaign.landing_site.url


@pytest.mark.parametrize('creative_type', (
        CreativeImage,
        CreativeFlash,
        CreativeVideo,
))
@pytest.mark.django_db
def test_creative_appnexus_media_url(audit_app, creative_type):
    """Make sure appnexus_media_url has always a scheme added."""
    account = audit_app.models['account']['acc']
    creative = creative_type(owner=account)
    url = urlparse(creative.appnexus_media_url)
    assert url.scheme
