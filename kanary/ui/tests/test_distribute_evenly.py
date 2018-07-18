import pytest
from ui.tests.utils import audit_creative
from datetime import datetime, time, timedelta
from adserving.types import Decimal
from ui.campaign.models import Campaign, Strategy, Advert, BiddingPeriod,\
    AdvertPeriod, Site
from django.core.exceptions import ValidationError


class TestStrategy(Strategy):

        @classmethod
        def MapClass(cls):
            """
            CacheMaps are found by relative import. This is a mock class and we need a CacheMap
            of Strategy from its module so hardcode it.
            """
            return Strategy.MapClass()


@pytest.fixture
def bidding_periods_app(app):
    strategies = [
        {'name': 'Hello this is Citrus', 'campaign': 'I\'m a fruit',
         'budget_total': 12345, 'budget_daily': 12345,
         'budget_bid_CPM': Decimal('0.2')}
    ]

    creatives = [
        {'name': 'creative_image_1', 'owner': 'acc', 'width': 300,
         'height': 250, 'image': 'test_creative.jpg'},
        {'name': 'creative_image_2', 'owner': 'acc', 'width': 600,
         'height': 500, 'image': 'test_creative.jpg'},
    ]

    app.setup.setup_landing_pages()
    app.setup.setup_campaigns_running()
    app.setup.setup_strategies(strategies)
    app.setup.setup_creative_images(creatives)

    strategy = app.setup.models['strategy']['Hello this is Citrus']
    creative1 = app.setup.models['creative']['creative_image_1']
    creative2 = app.setup.models['creative']['creative_image_2']

    Advert.objects.create(
        strategy=strategy,
        creative=creative1,
        landing_site=Site.objects.get(
            url='http://www.google.com/',
            owner=strategy.campaign.account)
    )

    Advert.objects.create(
        strategy=strategy,
        creative=creative2,
        landing_site=Site.objects.get(
            url='http://www.google.com/',
            owner=strategy.campaign.account)
    )

    return app


def setup_bidding_periods(strategy, periods, save=True):
    bidding_periods = []

    for period in periods:
        new_period = BiddingPeriod(
            start=period['start'],
            end=period['end'],
            strategy=strategy
        )
        if save:
            new_period.save()
        bidding_periods.append(new_period)
    return bidding_periods


def setup_bidding_ads(strategy, ads):
    for index, ad in enumerate(ads):
        ad_db = Advert.objects.all()[index]
        if (ad['bid_type'] == 'custom'):
            ad_db._set_custom_bid_CPM(ad['value'])
            ad_db.save()
        elif (ad['bid_type'] == 'custom_parting'):
            for bid in ad['values']:
                period = BiddingPeriod.objects.get(
                    start=bid['start'],
                    end=bid['end']
                )
                AdvertPeriod.objects.create(
                    advert=ad_db,
                    period=period,
                    custom_bid_CPM=Decimal(bid['value'])
                )


def get_expected_periods(expected_periods):
    periods_db = []
    for period in expected_periods:
        periods_db.append(
            BiddingPeriod.objects.get(
                start=period['start'],
                end=period['end']
            )

        )
    return periods_db


@pytest.mark.parametrize('strategy_bid, periods, ads, nonzero_periods', (
    (
        # Custom bid value set to 1, all bidding periods are nonzero
        (
            1,
            [
                {'start': time(10, 0), 'end': time(13, 15)},
                {'start': time(13, 45), 'end': time(16, 30)},
            ],
            [
                {'bid_type': 'custom', 'value': 1},
                {'bid_type': 'custom', 'value': 1}
            ],
            [
                {'start': time(10, 0), 'end': time(13, 15)},
                {'start': time(13, 45), 'end': time(16, 30)},
            ]
        )
    ),
    (
        # Bid values in periods are set to strategy default, which is 0
        # No periods are nonzero
        (
            0,
            [
                {'start': time(10, 0), 'end': time(13, 15)},
                {'start': time(13, 45), 'end': time(16, 30)},
            ],
            [
                {'bid_type': 'default'},
                {'bid_type': 'default'}
            ],
            []
        )
    ),
    (
        # Both ads have custom bid value equal to 0
        # No periods are nonzero
        (
            1,
            [
                {'start': time(10, 0), 'end': time(13, 15)},
                {'start': time(13, 45), 'end': time(16, 30)},
            ],
            [
                {'bid_type': 'custom', 'value': 0},
                {'bid_type': 'custom', 'value': 0}
            ],
            []
        )
    ),
    (
        # Ads have custom bids for periods, only one of them has nonzero bid
        (
            1,
            [
                {'start': time(10, 0), 'end': time(13, 15)},
                {'start': time(13, 45), 'end': time(16, 30)},
            ],
            [
                {
                    'bid_type': 'custom_parting',
                    'values': [
                        {'start': time(10, 0), 'end':
                         time(13, 15), 'value': 1},
                        {'start': time(13, 45), 'end':
                         time(16, 30), 'value': 0}
                    ]
                },
                {
                    'bid_type': 'custom_parting',
                    'values': [
                        {'start': time(10, 0), 'end':
                         time(13, 15), 'value': 1},
                        {'start': time(13, 45), 'end':
                         time(16, 30), 'value': 0}
                    ]
                }
            ],
            [
                {'start': time(10, 0), 'end': time(13, 15)}
            ]
        )
    ),
    (
        # Ads have custom bids for periods, there is a nonzero bid for both
        # periods
        (
            1,
            [
                {'start': time(10, 0), 'end': time(13, 15)},
                {'start': time(13, 45), 'end': time(16, 30)},
            ],
            [
                {
                    'bid_type': 'custom_parting',
                    'values': [
                        {'start': time(10, 0), 'end':
                         time(13, 15), 'value': 0},
                        {'start': time(13, 45), 'end':
                         time(16, 30), 'value': 1}
                    ]
                },
                {
                    'bid_type': 'custom_parting',
                    'values': [
                        {'start': time(10, 0), 'end':
                         time(13, 15), 'value': 1},
                        {'start': time(13, 45), 'end':
                         time(16, 30), 'value': 0}
                    ]
                }
            ],
            [
                {'start': time(10, 0), 'end': time(13, 15)},
                {'start': time(13, 45), 'end': time(16, 30)},
            ]
        )
    ),
))
@pytest.mark.unit
def test_bidding_periods_nonzero(bidding_periods_app, strategy_bid, periods,
                                 ads, nonzero_periods):

    strategy = Strategy.objects.get(name='Hello this is Citrus')
    strategy.is_day_parted = True
    strategy.budget_bid_CPM = Decimal(strategy_bid)
    strategy.save()
    setup_bidding_periods(strategy, periods)
    setup_bidding_ads(strategy, ads)

    calculated_period_ids = [p.pk for p in strategy._bidding_periods_nonzero()]
    expected_period_ids = [p.pk for p in get_expected_periods(nonzero_periods)]

    assert sorted(calculated_period_ids) == sorted(expected_period_ids)


@pytest.mark.parametrize('periods, ratio', (
    (
        (
            []
        ),
        0
    ),
    (
        (
            [
                {'start': time(10, 0), 'end': time(16, 00)},
                {'start': time(16, 00), 'end': time(22, 00)},
            ]
        ),
        0.5
    ),
    (
        (
            [
                {'start': time(10, 0), 'end': time(13, 15)},
                {'start': time(13, 45), 'end': time(16, 30)},
            ]
        ),
        0.25
    )
))
@pytest.mark.unit
def test_bidding_periods_ratio(bidding_periods_app, periods, ratio):

    class MockStrategy(TestStrategy):

        def __init__(self, *args, **kwargs):
            super(MockStrategy, self).__init__(*args, **kwargs)
            self.__bidding_periods_nonzero = []

        @property
        def is_day_parted(self):
            return True

        @is_day_parted.setter
        def is_day_parted(self, value):
            self._is_day_parted = value

        def _bidding_periods_nonzero(self):
            return self.__bidding_periods_nonzero

        def set_bidding_periods_nonzero(self, value):
            self.__bidding_periods_nonzero = value

    campaign = Campaign.objects.all().first()
    strategy = MockStrategy(
        name='Strategy Cool',
        campaign=campaign,
        budget_total=12345,
        budget_daily=12345,
        budget_bid_CPM=0.2
    )

    bidding_periods = setup_bidding_periods(strategy, periods, save=False)

    strategy.set_bidding_periods_nonzero(bidding_periods)
    calculated_bidding_ratio = strategy.bidding_periods_ratio()
    assert 0 <= calculated_bidding_ratio <= 1
    assert strategy.bidding_periods_ratio() == ratio


@pytest.mark.unit
def test_bidding_periods_ratio_not_day_parted(bidding_periods_app):
    '''
    Test if bidding_periods_ratio is 1 for not day parted strategy
    '''

    campaign = Campaign.objects.all().first()
    strategy = Strategy.objects.create(
        name='Strategy Cool',
        campaign=campaign,
        budget_total=12345,
        budget_daily=12345,
        budget_bid_CPM=Decimal('0.2'),
        is_day_parted=False
    )

    assert strategy.bidding_periods_ratio() == 1


@pytest.mark.parametrize(
    'budget_daily, budget_daily_spent, budget_total, budget_total_spent, ratio, now, period_budget',
    [
        # Only one period is left until the end if day, period budget should
        # be equal to total budget
        (100, 0, 100, 0, 1, datetime(2014, 10, 20, 23, 59, 00), 100),
        # Only one period is left until the end if day
        # and bidding_ratio is 0.5, so period budget should equal
        # half of the total budget
        (100, 0, 100, 0, 0.5, datetime(2014, 10, 20, 23, 59, 00), 50),
        # Campaign end was reached, period budget should be 0
        (100, 0, 100, 0, 1, datetime(2014, 10, 21, 01, 00, 00), 0),
        # 1h left till end of campaign
        (60, 0, 60, 0, 1, datetime(2014, 10, 21, 00, 00, 00), 1),
        # Daily budget < total budget
        (50, 0, 100, 0, 1, datetime(2014, 10, 20, 23, 59, 00), 50),
        # Total budget < daily budget
        (100, 0, 50, 0, 1, datetime(2014, 10, 20, 23, 59, 00), 50),
        # Daily left budget < total left budget
        (100, 50, 100, 0, 1, datetime(2014, 10, 20, 23, 59, 00), 50),
        # Total left budget < daily left budget
        (100, 0, 100, 50, 1, datetime(2014, 10, 20, 23, 59, 00), 50),
        # Test cases with daily budget = None
        # 1h 1m left until end of campaign
        (None, 0, 61, 0, 1, datetime(2014, 10, 20, 23, 59, 00), 1)
    ])
@pytest.mark.unit
def test_period_budget(bidding_periods_app, budget_daily, budget_daily_spent,
                       budget_total, budget_total_spent, ratio, now,
                       period_budget):
    """ Check value of budget with different values of daily and total budget and daily and total spend. """
    class MyStrategy(TestStrategy):

        def bidding_periods_ratio(self):
            return self.__bidding_periods_ratio

        def set_bidding_periods_ratio(self, ratio):
            self.__bidding_periods_ratio = ratio

    campaign = Campaign.objects.all().first()
    campaign.end_UTC = datetime(2014, 10, 21, 01, 00, 00)
    campaign.save()

    strategy = MyStrategy(
        name='Strategy Cool',
        campaign=campaign,
        budget_total=budget_total,
        budget_daily=budget_daily,
        budget_bid_CPM=0.2
    )

    strategy.set_bidding_periods_ratio(ratio)
    strategy.budget_spent = budget_total_spent
    strategy.budget_daily_spent = budget_daily_spent

    assert strategy.period_budget(now) == Decimal(period_budget)


@pytest.fixture
def periods_left_app(app):
    app.setup.setup_landing_pages()
    app.setup.setup_campaigns_running()
    app.setup.setup_strategies()
    return app


@pytest.mark.parametrize('now, campaign_end, period_count, is_limited_daily', [
    (
        datetime(2014, 10, 20, 12, 00, 00),
        datetime(2014, 10, 20, 12, 00, 00),
        0,
        True
    ),
    (
        datetime(2014, 10, 20, 12, 00, 00),
        datetime(2014, 10, 20, 12, 00, 00),
        0,
        False
    ),
    (
        datetime(2014, 10, 20, 12, 15, 00),
        datetime(2014, 10, 20, 12, 00, 00),
        0,
        True
    ),
    (
        datetime(2014, 10, 20, 12, 15, 00),
        datetime(2014, 10, 20, 12, 00, 00),
        0,
        False
    ),
    (
        datetime(2014, 10, 20, 11, 59, 00),
        datetime(2014, 10, 20, 12, 00, 00),
        1,
        True
    ),
    (
        datetime(2014, 10, 20, 11, 59, 30),
        datetime(2014, 10, 20, 12, 00, 00),
        1,
        False
    ),
    (
        datetime(2014, 10, 20, 23, 59, 00),
        datetime(2014, 10, 21, 12, 00, 00),
        1,
        True
    ),
    (
        datetime(2014, 10, 20, 23, 59, 00),
        datetime(2014, 10, 21, 01, 00, 00),
        61,
        False
    ),
    (
        datetime(2014, 10, 20, 00, 00, 00),
        datetime(2014, 10, 21, 12, 00, 00),
        1440,
        True
    ),
    (
        datetime(2014, 10, 20, 00, 00, 00),
        datetime(2014, 10, 21, 12, 00, 00),
        2160,
        False
    )
])
@pytest.mark.unit
def test_periods_left(periods_left_app, now, campaign_end, period_count,
                      is_limited_daily):
    '''
    Test if end of campaign is taken into account when calculating the number
    of remaining periods
    '''
    PERIOD_LENGTH = 60.0
    PERIODS_PER_DAY = timedelta(days=1).total_seconds() / PERIOD_LENGTH
    Strategy.period_lenth = PERIOD_LENGTH

    strategy = Strategy.objects.all().first()

    if is_limited_daily:
        strategy.budget_daily = strategy.budget_total
    else:
        strategy.budget_daily = None
    strategy.save()

    campaign = strategy.campaign
    campaign.end_UTC = campaign_end

    campaign.save()

    periods_left = strategy.periods_left(now)
    assert 0 <= periods_left
    if strategy.budget_daily:
        periods_left <= PERIODS_PER_DAY
    assert strategy.periods_left(now) == period_count


@pytest.fixture
def period_budgets_app(app):
    app.setup.setup_payments()
    app.setup.setup_creative_images()
    app.setup.setup_landing_pages()
    app.setup.setup_campaigns_running()
    app.setup.setup_strategies()
    app.setup.setup_adverts()

    for creative in app.setup.models['creative'].values():
        audit_creative(creative)

    return app


@pytest.mark.parametrize('strategies', [
    [
        {'name': 'Hello this is Citrus', 'budget_bid_CPM': Decimal('0.2'),
         'budget_total': 12345, 'budget_daily': 12345,
         'is_distributed_evenly': True},
        {'name': 'Can I has a pumpkin', 'budget_bid_CPM': Decimal('0.2'),
         'budget_total': 12345, 'budget_daily': 12345,
         'is_distributed_evenly': False}
    ]
])
@pytest.mark.unit
def test_get_period_budgets(period_budgets_app, strategies):

    distributed_strategy = Strategy.objects.first()
    distributed_strategy.is_distributed_evenly = True
    distributed_strategy.save()

    period_budgets = Strategy.get_period_budgets(datetime.utcnow())

    for strategy in Strategy.objects.all():
        assert (strategy.public_id in period_budgets) == \
            strategy.is_distributed_evenly


@pytest.fixture
def period_validation_app(app):
    strategies = [
        {'name': 'Hello this is Citrus', 'campaign': 'I\'m a fruit',
         'budget_total': 12345, 'budget_daily': 12345,
         'budget_bid_CPM': Decimal('0.2')}
    ]
    app.setup.setup_landing_pages()
    app.setup.setup_campaigns_running()
    app.setup.setup_strategies(strategies)
    return app


@pytest.mark.parametrize('existing, new', [
    (
        {'start': time(hour=10), 'end': time(hour=12)},
        {'start': time(hour=12), 'end': time(hour=14)}
    ),
    (
        {'start': time(hour=10, minute=15), 'end': time(hour=12)},
        {'start': time(hour=9, minute=30), 'end': time(hour=10, minute=15)}
    ),
    (
        {'start': time(hour=10), 'end': time(hour=12)},
        {'start': time(hour=12, minute=15), 'end': time(hour=14)}
    ),
    (
        {'start': time(hour=10, minute=30), 'end': time(hour=12)},
        {'start': time(hour=9, minute=30), 'end': time(hour=10, minute=15)}
    ),
])
@pytest.mark.unit
def test_bidding_periods_valid(period_validation_app, existing, new):
    strategy = Strategy.objects.all().first()
    BiddingPeriod.objects.create(
        strategy=strategy,
        start=existing['start'],
        end=existing['end']
    )

    BiddingPeriod.objects.create(
        strategy=strategy,
        start=new['start'],
        end=new['end']
    )


@pytest.mark.parametrize('existing, new', [
    (
        {'start': time(hour=10), 'end': time(hour=12)},
        {'start': time(hour=10), 'end': time(hour=12)}
    ),
    (
        {'start': time(hour=10), 'end': time(hour=12)},
        {'start': time(hour=10, minute=15), 'end': time(hour=11)}
    ),
    (
        {'start': time(hour=10), 'end': time(hour=12)},
        {'start': time(hour=9, minute=30), 'end': time(hour=12, minute=45)}
    ),
    (
        {'start': time(hour=10), 'end': time(hour=12)},
        {'start': time(hour=9, minute=30), 'end': time(hour=10, minute=45)}
    ),
    (
        {'start': time(hour=10), 'end': time(hour=12)},
        {'start': time(hour=9, minute=30), 'end': time(hour=10, minute=45)}
    ),
])
@pytest.mark.unit
def test_bidding_periods_invalid(period_validation_app, existing, new):
    strategy = Strategy.objects.all().first()
    BiddingPeriod.objects.create(
        strategy=strategy,
        start=existing['start'],
        end=existing['end']
    )
    with pytest.raises(ValidationError):
        BiddingPeriod.objects.create(
            strategy=strategy,
            start=new['start'],
            end=new['end']
        )
