from datetime import datetime, timedelta

import pytest
from django.core.management import call_command

from adserving.types import Decimal
from ui.campaign.models import Campaign, Strategy
from ui.tests.initial_datafixtures import date_format
from ui.tests.browser.page import Controls
from ui.tests.browser.page.list import ElementList


def utcnow_with_timedelta(**kwargs):
    return (datetime.utcnow() + timedelta(**kwargs)).strftime(date_format)


@pytest.fixture
def creative_statuses(user_db):
    ''' Initializes database with all data implemented in setup '''

    setup = user_db
    IMAGES = [
        {'name': 'Image audited', 'appnexus_status': 'a'},
        {'name': 'Image audit pending', 'appnexus_status': 'p'},
        {'name': 'Image audit blocked', 'appnexus_status': 'p',
         'appnexus_audit_blocked_no_funds': True},
        {'name': 'Image audit rejected', 'appnexus_status': 'r'},
        {'name': 'Image audit expired', 'appnexus_status': 'e'},
    ]
    for image in IMAGES:
        image.update({'owner': 'acc', 'width': 300, 'height': 250,
                      'image': 'creatives/test_creative.jpg'})

        setup.setup_creative_images([image])
    return setup


@pytest.fixture
def campaign_statuses(creative_statuses):
    '''Campaigns with all possible statuses'''
    campaign_finished = {'name': 'Campaign finished', 'account': 'acc',
                         'start_UTC': utcnow_with_timedelta(days=-7),
                         'end_UTC': utcnow_with_timedelta(days=-3),
                         'budget_total': 2000, 'budget_spent': 2000,
                         'landing_site': 'http://www.google.com/'}

    campaign_running = {'name': 'Campaign running', 'account': 'acc',
                         'start_UTC': utcnow_with_timedelta(days=-4),
                         'end_UTC': utcnow_with_timedelta(days=3),
                         'budget_total': 8000, 'landing_site': 'http://www.google.com/'}

    campaign_scheduled = {'name': 'Campaign scheduled', 'account': 'acc',
                         'start_UTC': utcnow_with_timedelta(days=10),
                         'end_UTC': utcnow_with_timedelta(days=13),
                         'budget_total': 1000, 'landing_site': 'http://www.google.com/'}

    strategy_a = {'name': 'Strategy A', 'campaign': 'Campaign finished',
                  'budget_total': 1000, 'budget_bid_CPM': Decimal('0.1')}
    strategy_b = {'name': 'Strategy B', 'campaign': 'Campaign running',
                  'budget_total': 0, 'budget_bid_CPM': Decimal('0.1')}
    strategy_c = {'name': 'Strategy C', 'campaign': 'Campaign scheduled',
                  'budget_total': 100, 'budget_bid_CPM': Decimal('0.1')}

    setup = creative_statuses
    setup.setup_landing_pages()
    setup.setup_campaigns([campaign_finished, campaign_running, campaign_scheduled])
    setup.setup_strategies([strategy_a, strategy_b, strategy_c])
    ADVERTS = [
        {'name': 'Ad audited', 'strategy': 'Strategy A',
         'creative': 'Image audited'},
        {'name': 'Ad audit pending', 'strategy': 'Strategy B',
         'creative': 'Image audit pending'},
        {'name': 'Ad audit rejected', 'strategy': 'Strategy B',
         'creative': 'Image audit rejected'},
        {'name': 'Ad audit blocked', 'strategy': 'Strategy C',
         'creative': 'Image audit blocked'},
        {'name': 'Ad audit expired', 'strategy': 'Strategy C',
         'creative': 'Image audit expired'}
    ]
    for advert in ADVERTS:
        advert.update({'url': 'http://www.google.com/'})
        setup.setup_adverts([advert])

    call_command('rebuild_index', interactive=False)

    return setup


@pytest.fixture
def strategy_statuses(creative_statuses):
    '''Fixture with one strategy with all available statuses and another clean'''
    strategy_problematic = {'name': 'Strategy problematic', 'campaign': 'I\'m a fruit',
                  'budget_total': 0, 'budget_bid_CPM': Decimal('0.1')}
    strategy_clean = {'name': 'Strategy clean', 'campaign': 'I\'m a fruit',
                  'budget_total': 1000, 'budget_bid_CPM': Decimal('0.1')}

    setup = creative_statuses
    setup.setup_landing_pages()
    setup.setup_campaigns()

    setup.setup_strategies([strategy_problematic, strategy_clean])

    ADVERTS = [
        {'name': 'Ad audited', 'strategy': 'Strategy clean',
         'creative': 'Image audited'},
        {'name': 'Ad audited', 'strategy': 'Strategy problematic',
         'creative': 'Image audited'},
        {'name': 'Ad audit pending', 'strategy': 'Strategy problematic',
         'creative': 'Image audit pending'},
        {'name': 'Ad audit rejected', 'strategy': 'Strategy problematic',
         'creative': 'Image audit rejected'},
        {'name': 'Ad audit blocked', 'strategy': 'Strategy problematic',
         'creative': 'Image audit blocked'},
        {'name': 'Ad audit expired', 'strategy': 'Strategy problematic',
         'creative': 'Image audit expired'}
    ]

    for advert in ADVERTS:
        advert.update({'url': 'http://www.google.com/'})
        setup.setup_adverts([advert])

    call_command('rebuild_index', interactive=False)

    return setup


class State(object):
    AUDIT_POSITIVE = 'audit_positive'
    AUDIT_PENDING = 'audit_pending'
    AUDIT_BLOCKED = 'audit_blocked'
    AUDIT_REJECTED = 'audit_rejected'
    AUDIT_EXPIRED = 'audit_expired'
    OUT_OF_BUDGET = 'out_of_budget'
    SCHEDULED = 'scheduled'
    FINISHED = 'finished'


def get_statuses(classes, mapping):
    """Returns a list of State objects based on given classes list and class to State mapping"""

    def is_status_class(class_name):
        return class_name in mapping.keys()

    status_classes = filter(is_status_class, classes)
    return [mapping[class_name] for class_name in status_classes]


class SidebarListRow(object):
    """ Object representing list row in sidebar """
    # Fill with model-specific statuses
    STATUS_MAPPING = NotImplemented

    STATUS_CLASS = NotImplemented

    def __init__(self, row):
        self.row = row
        self._statuses = self.row.element.find_elements_by_class_name(self.STATUS_CLASS)

    def __repr__(self):
        return '<{self.__class__.__name__}: {self.row.text}>'.format(self=self)

    @property
    def statuses(self):
        statuses = []
        for status_element in filter(lambda el: el.is_displayed(), self._statuses):
            all_classes = status_element.get_attribute('class').split(' ')
            element_statuses = get_statuses(all_classes, self.STATUS_MAPPING)
            # Each icon element should have exactly 1 status class
            if len(element_statuses) != 1:
                raise Exception('Invalid status classes %s' % all_classes)

            statuses.append(element_statuses[0])

        return statuses


class CampaignRow(SidebarListRow):
    """ Object representing campaign row in sidebar """

    STATUS_MAPPING = {
        'status-creative-in-review': State.AUDIT_PENDING,
        'status-creative-rejected': State.AUDIT_REJECTED,
        'status-creative-expired': State.AUDIT_EXPIRED,
        'status-out-of-budget': State.OUT_OF_BUDGET,
        'status-scheduled': State.SCHEDULED,
        'status-finished': State.FINISHED
    }

    STATUS_CLASS = '-t-campaign-state'


class StrategyRow(SidebarListRow):
    """ Object representing strategy row in sidebar """

    STATUS_MAPPING = {
        'status-creative-in-review': State.AUDIT_PENDING,
        'status-creative-rejected': State.AUDIT_REJECTED,
        'status-creative-expired': State.AUDIT_EXPIRED,
        'status-out-of-budget': State.OUT_OF_BUDGET,
    }

    STATUS_CLASS = '-t-strategy-state'


class CreativeRow(SidebarListRow):
    """ Object representing advert row in sidebar """

    STATUS_MAPPING = {
        'status-creative-passed': State.AUDIT_POSITIVE,
        'status-creative-blocked': State.AUDIT_BLOCKED,
        'status-creative-in-review': State.AUDIT_PENDING,
        'status-creative-rejected': State.AUDIT_REJECTED,
        'status-creative-expired': State.AUDIT_EXPIRED
    }

    STATUS_CLASS = '-t-creative-state'


class CreativeDetails(Controls):
    """Creative details view in strategy"""

    STATUS_MAPPING = {
        'status-creative-audited': State.AUDIT_POSITIVE,
        'status-creative-blocked': State.AUDIT_BLOCKED,
        'status-creative-pending': State.AUDIT_PENDING,
        'status-creative-rejected': State.AUDIT_REJECTED,
        'status-creative-expired': State.AUDIT_EXPIRED
    }

    STATUS_CLASS = '-t-creative-status'

    def __init__(self, client, container_selector='#content .-t-creative-details'):
        self.client = client
        self.container_selector = container_selector
        self.refresh()

    def refresh(self):
        """Refreshses references to the wrapped object"""
        self.container = self.client.find_element_by_css_selector(self.container_selector)

    @property
    def _status(self):
        """Status DOM element"""
        return self.container.find_element_by_class_name(self.STATUS_CLASS)

    @property
    def status(self):
        all_classes = self._status.get_attribute('class').split(' ')
        [status] = get_statuses(all_classes, self.STATUS_MAPPING)
        return status

    @property
    def _name(self):
        """Status DOM element"""
        return self.container.find_element_by_class_name('-t-title')

    @property
    def name(self):
        return self._name.text


# tests
@pytest.mark.usefixtures('campaign_statuses')
def test_campaign_statuses(client):
    """Checks for proper status classes in campaigns"""
    client.get('/#campaigns')

    campaigns_list = ElementList(client, '-t-campaigns-list', '-t-campaign-item', '-t-campaign')

    CAMPAIGN_STATUSES = {
        'Campaign finished': [State.OUT_OF_BUDGET, State.FINISHED],
        'Campaign running': [State.OUT_OF_BUDGET, State.AUDIT_REJECTED, State.AUDIT_PENDING],
        'Campaign scheduled': [State.SCHEDULED, State.AUDIT_EXPIRED, State.AUDIT_PENDING]
    }

    assert sorted(CAMPAIGN_STATUSES) == sorted(el.text for el in campaigns_list.items)

    for campaign in campaigns_list.items:
        campaign_row = CampaignRow(campaign)
        assert sorted(campaign_row.statuses) == sorted(CAMPAIGN_STATUSES[campaign.text])


@pytest.mark.usefixtures('strategy_statuses')
def test_strategy_statuses(client):
    """Checks for proper status classes in strategy list and creatives list in strategy"""

    campaign = Campaign.objects.get(name='I\'m a fruit')
    campaign_hash = '/#campaigns/%s' % campaign.slug
    client.get(campaign_hash)

    strategies_list = ElementList(client, '-t-strategies-list', '-t-strategy-item', '-t-strategy')

    STRATEGY_STATUSES = {
        'Strategy problematic': [State.OUT_OF_BUDGET, State.AUDIT_EXPIRED, State.AUDIT_REJECTED, State.AUDIT_PENDING],
        'Strategy clean': [],
    }

    assert sorted(STRATEGY_STATUSES) == sorted(el.text for el in strategies_list.items)

    for strategy in strategies_list.items:
        strategy_row = StrategyRow(strategy)
        assert sorted(strategy_row.statuses) == sorted(STRATEGY_STATUSES[strategy.text])


@pytest.mark.usefixtures('strategy_statuses')
def test_advert_statuses(client):
    """Checks creative statuses in strategy site"""

    strategy = Strategy.objects.get(name='Strategy problematic')
    campaign = strategy.campaign
    strategy_hash = '/#campaigns/{campaign}/{strategy}'.format(campaign=campaign.slug, strategy=strategy.slug)
    client.get(strategy_hash)

    creatives_list = ElementList(client, '-t-creatives-list', '-t-creative-item', '-t-creative-name')

    CREATIVE_STATUSES = {
        'Image audited': State.AUDIT_POSITIVE,
        'Image audit pending': State.AUDIT_PENDING,
        'Image audit rejected': State.AUDIT_REJECTED,
        'Image audit blocked': State.AUDIT_BLOCKED,
        'Image audit expired': State.AUDIT_EXPIRED
    }

    assert sorted(CREATIVE_STATUSES) == sorted(el.text for el in creatives_list.items)

    for creative in creatives_list.items:
        # Check status in sidebar
        creative_row = CreativeRow(creative)
        name = creative.text
        assert creative_row.statuses == [CREATIVE_STATUSES[name]]

        # Check status in details
        creative.click()
        creative_details_page = CreativeDetails(client)
        assert creative_details_page.name == name
        assert creative_details_page.status == CREATIVE_STATUSES[name]
