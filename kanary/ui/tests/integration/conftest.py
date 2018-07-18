from collections import namedtuple

import pytest

from ui.tests.utils import DatabaseDataFactory
from ui.tests.initial_datafixtures import (
    auth_test_users, auth_test_accounts, auth_test_lpages, auth_test_campaigns,
    auth_default_invoices, auth_default_payments
)
from ui.targeting.appnexus import AppNexusSegment, AppNexusBase
from ui.targeting.utils import subclasses_of
from ui.targeting.models import TargetValue, PublisherTargetValue
from ui.publishers.models import PublisherSet
from etc import dimensions
from etc.constants import NEXAGE_NETWORK_ID
from bidrequest.constants import EXCHANGES
from ui.tests.base_fixtures import kclient


kclient

App = namedtuple('App', ['db', 'setup'])


@pytest.fixture
def auth_app(db, basic_fixture):
    setup = DatabaseDataFactory()
    setup.setup_accounts(auth_test_accounts)
    setup.setup_users(auth_test_users)
    setup.setup_landing_pages(auth_test_lpages)
    setup.setup_campaigns(auth_test_campaigns)
    return App(db, setup)


@pytest.fixture
def billing_app(db, auth_app):
    setup = auth_app.setup
    setup.setup_invoices(auth_default_invoices)
    setup.setup_payments(auth_default_payments)
    return App(db, setup)


@pytest.fixture
def defclient(client):
    '''Wraps django client into our version of test class and logs'''
    client.login()
    return client


@pytest.fixture
def budget_app(db, basic_fixture):
    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()
    setup.setup_landing_pages()
    setup.setup_campaigns()
    setup.setup_strategies()
    return App(db, setup)


@pytest.fixture
def state_app(db, basic_fixture):
    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()
    setup.setup_payments()
    setup.setup_landing_pages()
    setup.setup_creative_images()
    setup.setup_campaigns()
    setup.setup_strategies()
    setup.setup_bidding_periods()
    setup.setup_adverts()
    return setup


@pytest.fixture
def publishertargetvalue_positions(publishertargetvalues_db):
    '''
    Modify PublisherTargetValues so that they contain unknown positions.
    '''
    # Make all self-represented (unmoderated):
    for tv in PublisherTargetValue.objects.all():
        tv.positions = ['NOT_MAPPED_VALUE']
        tv.save()


@pytest.fixture
def clean_targeting(db):
    ''' Clear targeting to create an environment for targeting tests. '''
    TargetValue.objects.all().delete()
    for model in subclasses_of(AppNexusBase, 'ui.targeting.appnexus'):
        model.objects.all().delete()

    return db


@pytest.fixture
def targetvalues_all_states(clean_targeting):
    '''
    Create one target value of each state: representant, represented
    and unrepresented.
    The 'representant' object will represent created 'represented' object.
    '''
    tvs = {}
    # Kanary db fixture replaces original one. Drop targeting_initial.
    tvs['representant'] = TargetValue.objects.create_representant(
        'appnexus', dimensions.g_location, ['PL', 'Silesia', 'Sosnowiec'])
    tvs['represented'] = TargetValue.objects.create_value_with_representant(
        values=['PL', 'Slunsk', 'Sosnowiec'], representant=tvs['representant'])
    tvs['unrepresented'] = TargetValue.objects.create_unrepresented(
        'appnexus', dimensions.g_location, ['PL', 'Slask', 'Sosnowiec'])

    return tvs


@pytest.fixture
def publishertargetvalues_db(db):
    db_factory = DatabaseDataFactory()
    db_factory.setup_segments()

    networks = [
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.appnexus,
            'values': ('Application', 'Rubicon'),
            'represented_values': ('app', '23')
        },
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.appnexus,
            'values': ('Web', 'Rubicon'),
            'represented_values': ('site', '23')
        },
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.nexage,
            'values': ('Application', 'Nexage'),
            'represented_values': ('app', NEXAGE_NETWORK_ID)
        },
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.nexage,
            'values': ('Web', 'Nexage'),
            'represented_values': ('site', NEXAGE_NETWORK_ID)
        },
    ]
    networks_app = db_factory.setup_targetvalues(networks,
                                                 PublisherTargetValue)

    publishers_app = [
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.appnexus,
            'values': ('Application', 'Rubicon', 'Nincja Fruit'),
            'represented_values': ('app', '23', 'Nincja Fruit')
        },
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.nexage,
            'values': ('Application', 'Nexage', 'Ninja Fruit'),
            'represented_values': ('app', NEXAGE_NETWORK_ID,
                                   'Ninja Fruit')
        },
    ]
    publishers_app = db_factory.setup_targetvalues(publishers_app,
                                                   PublisherTargetValue)

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
                                   NEXAGE_NETWORK_ID,
                                   'rafalmichal.com')
        },
    ]
    publishers_site = db_factory.setup_targetvalues(publishers_site,
                                                    PublisherTargetValue)

    # setup restrictions
    def _add_restrictions(publisher):
        segment = AppNexusSegment.objects.brand_protection().get(
            appnexus_id=94999
        )

        if publisher.exchange == EXCHANGES.appnexus:
            positions = ['above']
        else:
            positions = ['1']

        publisher.sizes = ['500x40', '600x80']
        publisher.positions = positions
        publisher.save()
        publisher.segments.add(segment)

        return publisher

    map(_add_restrictions, publishers_app)
    map(_add_restrictions, publishers_site)

    return {
        'setup': db_factory,
        'networks_app': networks_app,
        'publishers_app': publishers_app,
        'publishers_site': publishers_site
    }


@pytest.fixture
def huge_publisherlist_db(publishertargetvalues_db, db):
    db_factory = publishertargetvalues_db['setup']

    publishers_app = []
    for i in range(250):
        publishers_app += [
            {
                'category': dimensions.g_publisher,
                'exchange': EXCHANGES.appnexus,
                'values': ('Application', 'Rubicon', str(i)),
                'represented_values': ('app', '23', str(i))
            },
            {
                'category': dimensions.g_publisher,
                'exchange': EXCHANGES.nexage,
                'values': ('Application', 'Nexage', str(i * 2)),
                'represented_values': ('app', str(i * 2),
                                       'Ninja Fruit')
            },
        ]
    publishers_app = db_factory.setup_targetvalues(publishers_app,
                                                   PublisherTargetValue)

    publishers_site = []
    for i in range(250):
        publishers_site += [
            {
                'category': dimensions.g_publisher,
                'exchange': EXCHANGES.appnexus,
                'values': ('Web', 'Rubicon', str(i)),
                'represented_values': ('site', '23', str(i))
            },
            {
                'category': dimensions.g_publisher,
                'exchange': EXCHANGES.nexage,
                'values': ('Web', 'Nexage', str(i * 2)),
                'represented_values': ('site',
                                       NEXAGE_NETWORK_ID,
                                       str(i * 2))
            },
        ]
    publishers_site = db_factory.setup_targetvalues(publishers_site,
                                                    PublisherTargetValue)

    # save
    [publisher.save() for publisher in (publishers_app + publishers_site)]

    return {
        'setup': db_factory,
        'publishers_app': publishers_app + publishertargetvalues_db['publishers_app'],
        'publishers_site': publishers_site + publishertargetvalues_db['publishers_site']
    }


@pytest.fixture
def publisherset_db(auth_app, publishertargetvalues_db):
    setup = auth_app.setup
    siteset = setup.setup_publisherset({
        'owner': auth_test_accounts[0]['name'],
        'inventory': PublisherSet.TYPE_SITE,
        'name': 'Awsome site set'
    })
    for site_pub in publishertargetvalues_db['publishers_site']:
        siteset.target_values.add(site_pub)
    siteset.save()
    appset = setup.setup_publisherset({
        'owner': auth_test_accounts[0]['name'],
        'inventory': PublisherSet.TYPE_APP,
        'name': 'Awsome app set'
    })
    for app_pub in publishertargetvalues_db['publishers_app']:
        appset.target_values.add(app_pub)
    appset.save()

    return auth_app


@pytest.fixture
def strategies_publisherset(state_app):
    networks = [
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.nexage,
            'values': ('Web', 'Nexage'),
            'represented_values': ('site', NEXAGE_NETWORK_ID)
        },
    ]
    state_app.setup_targetvalues(networks, PublisherTargetValue)

    publishers_site = [
        {
            'category': dimensions.g_publisher,
            'exchange': EXCHANGES.nexage,
            'values': ('Web', 'Nexage', 'rafalmichal.com'),
            'represented_values': ('site',
                                   NEXAGE_NETWORK_ID,
                                   'rafalmichal.com')
        },
    ]
    publishers_site = state_app.setup_targetvalues(publishers_site,
                                                   PublisherTargetValue)

    siteset = state_app.setup_publisherset({
        'owner': 'acc',
        'inventory': PublisherSet.TYPE_SITE,
        'name': 'Awsome site set'
    })

    siteset.target_values.add(publishers_site[0])
    siteset.save()


def pytest_runtest_call(item):
    def set_pytest_mark(name, decorator_func):
        if hasattr(item.obj, name):
            item.obj = decorator_func(item.obj)
            delattr(item.obj, name)
