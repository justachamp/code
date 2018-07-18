import pytest
from itertools import count

from etc import dimensions, constants
from bidrequest.utils import age_group
from bidrequest.constants import EXCHANGES
from ui.tests.utils import DatabaseDataFactory, \
    default_landing_page, default_campaign, default_strategies
from ui.tests.mappers.utils import advert_generator, fbx_page_generator
from ui.tests.initial_datafixtures import default_account
from ui.publishers.models import PublisherSet
from ui.targeting.models import (
    PublisherTargetValue,
    SegmentProximicMaturityRating,
    SegmentProximicPageLanguage,
    SegmentProximicPagePlacement,
    Peer39PageLanguage,
    LotameDemographic, LotameBehavioralInterest, LotameInfluencers, LotameOffline
)
from ui.campaign.models import Strategy


class App:

    def __init__(self, db, setup):
        self.db = db
        self.setup = setup


@pytest.fixture
def app_audited(app, basic_fixture, device_mock_data, appnexus_api_auditing):
    list(fbx_page_generator())
    list(advert_generator(device_mock_data))
    app.setup.setup_payments()
    return app


@pytest.fixture
def app_noaudit(app, basic_fixture, device_mock_data):
    list(fbx_page_generator())
    list(advert_generator(device_mock_data, noaudit=True))
    return app


@pytest.fixture
def app_noaudit_publisherset(app_noaudit):
    setup = app_noaudit.setup

    siteset = setup.setup_publisherset({
        'owner': default_account[0]['name'],
        'inventory': PublisherSet.TYPE_SITE,
        'name': 'Awsome site set'
    })
    publishers_site = [
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.appnexus,
            'values': ('Web', 'Rubicon', 'rafalmichal.com'),
            'represented_values': ('site', '23', 'rafalmichal.com')
        },
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.nexage,
            'values': ('Web', 'Nexage', 'rafalmichal.com'),
            'represented_values': ('site',
                                   constants.NEXAGE_NETWORK_ID,
                                   'rafalmichal.com')
        },
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.smaato,
            'values': ('Web', 'Smaato', 'rafalmichal.com'),
            'represented_values': ('site',
                                   constants.SMAATO_NETWORK_ID,
                                   'rafalmichal.com')
        },
    ]
    publishers_site = setup.setup_targetvalues(publishers_site,
                                               PublisherTargetValue)

    # adding first publisher only
    siteset.target_values.add(publishers_site[0])
    siteset.save()
    Strategy.objects.update(publisherset=siteset)

    return app_noaudit


@pytest.fixture
def app_audited_publisherset(app_audited):
    setup = app_audited.setup

    siteset = setup.setup_publisherset({
        'owner': default_account[0]['name'],
        'inventory': PublisherSet.TYPE_SITE,
        'name': 'Awsome site set'
    })
    publishers_site = [
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.appnexus,
            'values': ('Web', 'Rubicon', 'rafalmichal.com'),
            'represented_values': ('site', '23', 'rafalmichal.com')
        },
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.nexage,
            'values': ('Web', 'Nexage', 'rafalmichal.com'),
            'represented_values': ('site',
                                   constants.NEXAGE_NETWORK_ID,
                                   'rafalmichal.com')
        },
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.smaato,
            'values': ('Web', 'Smaato', 'rafalmichal.com'),
            'represented_values': ('site',
                                   constants.SMAATO_NETWORK_ID,
                                   'rafalmichal.com')
        },
    ]
    publishers_site = setup.setup_targetvalues(publishers_site,
                                               PublisherTargetValue)

    # adding first publisher only
    siteset.target_values.add(publishers_site[0])
    siteset.save()
    Strategy.objects.update(publisherset=siteset)

    return app_audited


@pytest.fixture
def app_audited_audiences(app_audited):
    setup = app_audited.setup
    setup.setup_audiences()
    return app_audited


@pytest.fixture
def audit_app(db, basic_fixture):
    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()

    landing_pages = default_landing_page \
        + [{'owner': 'acc', 'url': 'http://www.onet.com/'}]
    setup.setup_landing_pages(landing_pages)

    campaigns = default_campaign + [
        {'name': 'Meat', 'account': 'acc', 'budget_total': 8000,
         'start_UTC': '2013-01-01T00:00', 'end_UTC': '2013-01-31T00:00',
         'landing_site': 'http://www.onet.com/'}
    ]
    setup.setup_campaigns(campaigns)
    strategies = default_strategies + [
        {'name': 'Roast beef', 'campaign': 'Meat', 'budget_total': 67676,
         'budget_bid_CPM': 0.1}
    ]
    setup.setup_strategies(strategies)
    setup.setup_creative_images()
    setup.setup_creative_flash()
    return setup


@pytest.fixture
def campaigns(app_audited):
    app_audited.setup.setup_landing_pages()
    app_audited.setup.setup_campaigns()
    return app_audited


@pytest.fixture
def strategies(campaigns):
    campaigns.setup.setup_strategies()
    return campaigns


@pytest.fixture
def device_mock_data(db):
    from ui.targeting.models import TargetMap, TargetValue

    targeting = [
        (None, dimensions.gender, ['Male'], True),
        (None, dimensions.age_group, [age_group('17')], True),
        (None, dimensions.g_location, ['USA', 'New York', 'Manhattan'], True),
    ]

    target_values = []
    for exchange, category, value, include in targeting:
        target_values.append(({
            'exchange': exchange,
            'category': category,
            'value': TargetMap.pack(value),
        }, include))

    values = [
        ['targeting_values', TargetValue, target_values],
    ]
    test_data = [
        ['appnexus', '12:30', '15:30', values, 'default'],
        ['appnexus', '16:00', '18:00', values, 'default'],
        ['facebook', '12:30', '15:30', values, 'facebook_sidebar'],
        ['facebook', '12:30', '15:30', values, 'facebook_newsfeed']
    ]
    return test_data


@pytest.fixture
def segments(db):
    """Return saved segment instances."""
    counter = count()  # ids factory
    instances = {}

    # In this loop we create segment instances that require 2 parameters.
    for model in (
        SegmentProximicMaturityRating, SegmentProximicPageLanguage, SegmentProximicPagePlacement,
        Peer39PageLanguage,
    ):
        instances[model.__name__] = model.objects.create(appnexus_id=counter.next(), name=model.__name__)

    # In this loop we create Lotame segment instances that require 3 parameters - 2 as above
    # and an additional `lotame_id`.
    for model in (LotameDemographic, LotameBehavioralInterest, LotameInfluencers, LotameOffline):
        instances[model.__name__] = model.objects.create(
            appnexus_id=counter.next(), lotame_id=counter.next(), name=model.__name__)

    return instances
