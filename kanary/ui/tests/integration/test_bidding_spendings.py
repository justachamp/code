from datetime import datetime

import pytest
import simplejson
from mock import patch

from pytest_dbfixtures import factories
from adserving.types import Decimal
import adserving.bidder.spendings
from ui.tests.utils import DatabaseDataFactory, audit_creative
from ui.common.models import LatestUpdate
from ui.campaign.models import Campaign, Strategy, Advert
from ui.bidding_spendings.tasks import update_bidder_spendings
from etc.constants import EPOCH, cpm_offset_length, f_offset_length, PUBLIC_ID_DELIMITER
from etc.config import settings

# currency offset
offset = 10 ** (cpm_offset_length + f_offset_length)


@pytest.fixture
def bidding_app(db):
    """Extension of default setup by storing additional bidding periods"""
    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()
    setup.setup_creative_images()
    setup.setup_landing_pages()
    setup.setup_campaigns()
    setup.setup_strategies()
    setup.setup_bidding_periods()
    setup.setup_adverts()
    return setup


@pytest.fixture
def db_factory_two_camps(bidding_app):
    """
    Extends bidding_app fixture by adding another campaign. In result database
    has two campaigns.
    """
    campaigns = [
        {'name': 'I\'m a ninja', 'account': 'acc',
         'budget_total': 8000, 'start_UTC': '2013-01-01T00:00',
         'end_UTC': '2013-01-31T00:00',
         'landing_site': 'http://www.google.com/'},
    ]
    strategies = [
        {'name': 'Hello this is ninja', 'campaign': 'I\'m a ninja',
         'budget_total': 12345, 'budget_bid_CPM': Decimal('0.2')},
    ]

    bidding_app.setup_campaigns(campaigns)
    bidding_app.setup_strategies(strategies)
    return bidding_app


@pytest.fixture
def db_factory_four_strategies(bidding_app):
    strategies = [
        {'name': 'Strategy 3', 'campaign': 'I\'m a fruit',
         'budget_total': 8000, 'budget_bid_CPM': Decimal('0.1')},
        {'name': 'Strategy 4', 'campaign': 'I\'m a fruit',
         'budget_total': 4321, 'budget_bid_CPM': Decimal('0.1')}
    ]
    bidding_app.setup_strategies(strategies)
    return bidding_app


@pytest.fixture
def period_budgets_app(app):
    ''' A minimal fixture for testing period budgets '''
    app.setup.setup_payments()
    app.setup.setup_landing_pages()
    app.setup.setup_creative_images()
    app.setup.setup_campaigns_running()
    app.setup.setup_strategies()
    app.setup.setup_adverts()

    for creative in app.setup.models['creative'].values():
        audit_creative(creative)

    return app


rc = factories.redisdb(
    'redis_proc',
    host=settings.spending_redis_host,
    port=settings.spending_redis_port,
)


class TestBiddingSpendingsSubscriber(object):
    def insert_redis_spendings(self, rc, db, model, ordered_spend_key,
                               spend_key, spendings):
        '''
        push some spendings into testing redis

        :param rc: redis client from fixture
        :param db: database factory oobject from fixture
        '''
        for name, spending in spendings.items():
            last_updated, value = spending
            public_id = db.models[model][name].public_id
            rc.zadd(ordered_spend_key, last_updated, public_id)
            rc.hset(spend_key, public_id, value)

    @pytest.mark.parametrize('model', (
            [
                Campaign,
                Strategy,
            ]
    ))
    def test_get_total_spendings_empty(self, rc, model, bidding_app):
        '''
        for empty redis database get_total_spendings should return empty dict
        '''
        rc.flushall()

        spendings = model.get_total_spendings(rc, model.latest_update())

        assert spendings == {}

    def test_get_daily_spendings_empty(self, rc, bidding_app):
        '''
        for empty redis database get_daily_spendings should return empty dict
        '''
        rc.flushall()

        spendings = Strategy.get_daily_spendings(rc, Strategy.latest_daily_update())

        assert spendings == {}

    def test_import_strategy_spending(self, rc, bidding_app):
        '''
        Test importing strategy spendings from Redis to Django models

        1. Put total and daily spendings to Redis.
        2. Get spendings from a specified timestamp.
        3. Check if spendings newer that the timestamp are imported,
            and older were not imported.
        '''
        total_spendings = {
            # 'name': (time__offset, spent)
            'Hello this is Citrus': (20, 1500),
            'han i has a pumpkin?': (5, 200)
        }
        daily_spendings = {
            # 'name': (time__offset, spent)
            'Hello this is Citrus': (20, 150),
            'han i has a pumpkin?': (5, 20)
        }

        # Save spendings to redis.
        rc.flushall()

        self.insert_redis_spendings(rc, bidding_app, 'strategy',
                                    Strategy.total_ordered_spendings_key,
                                    Strategy.total_spendings_key,
                                    total_spendings)

        self.insert_redis_spendings(rc, bidding_app, 'strategy',
                                    Strategy.daily_ordered_spendings_key,
                                    Strategy.daily_spendings_key,
                                    daily_spendings)

        # Select a date which is newer than some spendings
        query_offset = 10
        update_from = datetime.fromtimestamp(query_offset)

        # Set it as the latest_update for Strategy and StrategyDaily
        LatestUpdate(object_name='Strategy',
                     latest_update=update_from).save()
        LatestUpdate(object_name='StrategyDaily',
                     latest_update=update_from).save()

        # Import spendings
        total_imported_spends, total_last_update = \
            Strategy.import_total_spendings(rc)
        daily_imported_spends, daily_last_update = \
            Strategy.import_daily_spendings(rc)
        updated_strategy_spent_ids = \
            [m.pk for m in total_imported_spends]
        updated_strategy_daily_spent_ids = \
            [m.pk for m in daily_imported_spends]

        get_strategy = lambda name: Strategy.objects.get(
            pk=bidding_app.models['strategy'][name].pk)

        # Check if total budgets were saved correctly
        for name, spending in total_spendings.iteritems():
            time_offset, spent = spending
            strategy = get_strategy(name)
            if time_offset >= query_offset:
                assert strategy.budget_spent == Decimal(spent) / offset
                assert strategy.pk in updated_strategy_spent_ids
            else:
                assert strategy.budget_spent == Decimal(0) / offset
                assert strategy.pk not in updated_strategy_spent_ids

        # Check if daily budgets were saved correctly
        for name, spending in daily_spendings.iteritems():
            time_offset, spent = spending
            strategy = get_strategy(name)
            if time_offset >= query_offset:
                assert strategy.budget_daily_spent == Decimal(spent) / offset
                assert strategy.pk in updated_strategy_daily_spent_ids
            else:
                assert strategy.budget_daily_spent == Decimal(0) / offset
                assert strategy.pk not in updated_strategy_daily_spent_ids

        # Check if update times were saved
        assert total_last_update == \
               LatestUpdate.objects.get(object_name='Strategy').latest_update

        assert daily_last_update == \
               LatestUpdate.objects.get(object_name='StrategyDaily').latest_update

    def test_clear_strategy_daily_spending(self, rc, bidding_app):
        '''
        Test cleaning strategy daily spendings in Redis and Django

        1. Save some daily spendings.
        2. Import them to Django.
        3. Clear daily spendings.
        4. Check if they are removed from Redis and Django.
        '''
        daily_spendings = {
            # 'name': (time__offset, spent)
            'Hello this is Citrus': (20, 150),
            'han i has a pumpkin?': (5, 20)
        }
        # Save some daily spendings to Redis.
        rc.flushall()

        self.insert_redis_spendings(rc, bidding_app, 'strategy',
                                    Strategy.daily_ordered_spendings_key,
                                    Strategy.daily_spendings_key,
                                    daily_spendings)

        # Import them to Postgres
        imported_spends, _ = Strategy.import_daily_spendings(rc)

        # Clear spendings
        cleared_spends = Strategy.clear_daily_spendings(rc)

        # Check if all spendings have been removed from Postgres
        imported_ids = [m.pk for m in imported_spends]
        cleared_ids = [m.pk for m in cleared_spends]

        assert sorted(imported_ids) == sorted(cleared_ids)

        # Check if there are no spendings in Redis
        redis_spendings = Strategy.get_daily_spendings(rc,
                                                       Strategy.latest_daily_update())

        assert redis_spendings == {}

        # And all strategies have daily_spent == 0
        for strategy in Strategy.objects.all():
            assert strategy.budget_daily_spent == 0

    def test_strategy_clear_period_spendings(self, rc, bidding_app):
        '''
        Test deleting strategy custom period spendings from Redis

        1. Save some spendings to Redis
        2. Check if they were saved correctly
        3. Remove them using Strategy.clear_period_spendings()
        4. Check if they were removed
        '''

        def get_public_id(name):
            return bidding_app.models['strategy'][name].public_id

        period_spendings = {
            'Hello this is Citrus': 1,
            'han i has a pumpkin?': 2
        }
        rc.flushall()

        # Save period spendings to Redis.
        for name, value in period_spendings.items():
            public_id = get_public_id(name)
            rc.hset(Strategy.period_spendings_key, public_id, value)

        # Check if they were saved
        retrieved_spendings = rc.hgetall(Strategy.period_spendings_key)

        for name, value in period_spendings.items():
            public_id = get_public_id(name)
            assert float(retrieved_spendings[public_id]) == value

        assert len(retrieved_spendings) == len(period_spendings)

        # Try to reset period keys (spendings and budget)
        Strategy.reset_period_budgets(rc)

        assert rc.hgetall(Strategy.period_spendings_key) == {}, "Spendings should be cleared!"

    def test_strategy_set_period_budgets(self, rc, period_budgets_app):
        '''
        Test setting strategy budgets in Redis
        '''

        strategy = Strategy.objects.first()
        strategy.is_distributed_evenly = True
        strategy.save()

        assert strategy.state.is_running is True

        # Save period budgets
        saved_budgets = Strategy.reset_period_budgets(rc)

        # Check if they were saved
        retrieved_budgets = rc.hgetall(Strategy.period_budgets_key)

        assert len(retrieved_budgets) == len(saved_budgets)
        assert strategy.public_id in retrieved_budgets
        assert Decimal(retrieved_budgets[strategy.public_id]) == \
               saved_budgets[strategy.public_id]

        # this should take strategy off distribute evenly loop
        strategy.is_distributed_evenly = False
        strategy.save()

        # Try to remove them and check if they were removed
        saved_budgets = Strategy.reset_period_budgets(rc)

        assert rc.hgetall(Strategy.period_budgets_key) == {}, "Period budgets should be cleared!"

    def test_get_spendings_non_empty(self, rc, db_factory_four_strategies):
        '''
        define 4 strategies with spendings.
        In test:
        1. spendings are requested from unix 10 and above, so strategy 'han i has a pumpkin?'
        should not appear in results.
        2. returned value should be a dict with strategies: 'Hello this is Citrus',
        'Strategy 3' and 'Strategy 4'
        3. keys should be RandomId of models
        4. values should be tuples like (accumaltive spend values, spend_time)
        '''

        default_spendings = {
            'Hello this is Citrus': (10, 666),
            'han i has a pumpkin?': (9, 777),
            'Strategy 3': (12, 999),
            'Strategy 4': (15, 999)
        }

        self.insert_redis_spendings(rc, db_factory_four_strategies, 'strategy',
                                    Strategy.total_ordered_spendings_key,
                                    Strategy.total_spendings_key,
                                    default_spendings)

        update_from = datetime.fromtimestamp(10)
        LatestUpdate(object_name='Strategy', latest_update=update_from).save()

        strat_spends = Strategy.get_total_spendings(rc, Strategy.latest_update())

        strat1_public_id = db_factory_four_strategies.models['strategy']['Hello this is Citrus'].public_id
        assert strat_spends[strat1_public_id][0] == 666
        assert strat_spends[strat1_public_id][2] == 10

        strat3_public_id = db_factory_four_strategies.models['strategy']['Strategy 3'].public_id
        assert strat_spends[strat3_public_id][0] == 999
        assert strat_spends[strat3_public_id][2] == 12

        strat4_public_id = db_factory_four_strategies.models['strategy']['Strategy 4'].public_id
        assert strat_spends[strat4_public_id][0] == 999
        assert strat_spends[strat4_public_id][2] == 15

        strat2_public_id = db_factory_four_strategies.models['strategy']['han i has a pumpkin?'].public_id
        assert strat2_public_id not in strat_spends
        rc.flushall()

    def test_get_latest_update(self, bidding_app):
        latest = LatestUpdate.objects.create(object_name=Campaign.__name__)

        last_update_campaign = Campaign.latest_update()
        last_update_strategy = Strategy.latest_update()
        last_update_strategy_daily = Strategy.latest_daily_update()

        assert last_update_campaign.latest_update == latest.latest_update
        assert last_update_strategy.latest_update == EPOCH
        assert last_update_strategy_daily.latest_update == EPOCH

    def test_save_spendings(self, db_factory_four_strategies):
        '''
        save spendings takes spendings generated by get_spendings function
        and stores them in database via django active record.
        '''
        strategies = db_factory_four_strategies.models['strategy']

        strat_obj_spends = {
            strategies['Hello this is Citrus'].public_id: (30, 3, 123),
            strategies['han i has a pumpkin?'].public_id: (40, 4, 321),
            strategies['Strategy 3'].public_id: (1, 1, 31),
        }

        saved_models = Strategy.save_spendings(strat_obj_spends)

        assert len(saved_models) == 3
        strat1 = Strategy.objects.get(pk=strategies['Hello this is Citrus'].pk)
        strat2 = Strategy.objects.get(pk=strategies['han i has a pumpkin?'].pk)
        strat3 = Strategy.objects.get(pk=strategies['Strategy 3'].pk)

        assert strat1.budget_spent == Decimal('30') / offset
        assert strat1.budget_spent_commission == Decimal('3') / offset

        assert strat2.budget_spent == Decimal('40') / offset
        assert strat2.budget_spent_commission == Decimal('4') / offset

        assert strat3.budget_spent == Decimal('1') / offset
        assert strat3.budget_spent_commission == Decimal('1') / offset

    def test_save_model_spending(self, bidding_app):
        '''
        save_object_spending gets django model object and saves given
        spending value and spending time
        '''
        saved_strat = bidding_app.models['strategy']['Hello this is Citrus']
        saved_strat.save_spending(5, 1)
        saved_strat.save_daily_spending(1)

        strategy = Strategy.objects.get(pk=saved_strat.pk)
        assert strategy.budget_spent == Decimal('5') / offset
        assert strategy.budget_daily_spent == Decimal('1') / offset
        assert strategy.budget_spent_commission == Decimal('1') / offset

        saved_camp = bidding_app.models['campaign']['I\'m a fruit']
        saved_camp.save_spending(5, 1)

        campaign = Campaign.objects.get(pk=saved_camp.pk)
        assert campaign.budget_spent == Decimal('5') / offset
        assert campaign.budget_spent_commission == Decimal('1') / offset

    def test_get_django_objects(self, bidding_app):
        '''
        in database we store partial id_random (random md5 hashes)
        random ids which are stored in bidders are based on this id's.
        For ex.
        Ad random id is accid(delimiter)campid(delimiter)strategyid(delimiter)adid
        Strategy: accid(delimiter)campid(delimiter)strategyid
        Campaign: accid(delimiter)campid

        get_django_objects should return django objects based on mixed
        id (with delimiters) and model type
        '''

        # closure for getting public_id (property in django model)
        pubids = lambda model: [i.public_id for i in model.objects.all()]

        # for ads
        ad_pubids = pubids(Advert)
        # there are 4 ads for this test we get only first two with get_dj_obj
        ad_objects = Advert.objects_by_public_ids(ad_pubids[:2])

        # we expect those two objects in ad_objects
        ad_pubids[0] in [i.public_id for i in ad_objects]
        ad_pubids[1] in [i.public_id for i in ad_objects]
        # and the third one should not be in returned results
        ad_pubids[2] not in [i.public_id for i in ad_objects]

        # for strategies
        strat_pubids = pubids(Strategy)
        strat_objects = Strategy.objects_by_public_ids([strat_pubids[0], ])
        strat_pubids[0] == strat_objects[0].public_id

        # for campaigns
        camp_pubid = pubids(Campaign)
        camp_objects = Campaign.objects_by_public_ids(camp_pubid)
        assert camp_pubid[0] == camp_objects[0].public_id


def test_update_bidder_spendings(redisdb_spendings, bidding_app):
    """
    Create a redis spending entries for campaign.
    Check redis pubsub channel for correct message.
    """
    # no point in this test if we don't have any campaign here
    assert Campaign.objects.count() > 0

    # let's patch publish method to intercept published message
    with patch.object(update_bidder_spendings.rd, 'publish'):
        for campaign in Campaign.objects.all():
            redisdb_spendings.hset(
                adserving.bidder.spendings.spend_camp_key,
                campaign.public_id,
                Decimal('0.8')
            )
            redisdb_spendings.hset(
                adserving.bidder.spendings.spend_camp_key,
                campaign.public_id + adserving.bidder.spendings.string_commission,
                Decimal('0.2')
            )

        update_bidder_spendings()

        channel, message = update_bidder_spendings.rd.publish.call_args[0]
        message = simplejson.loads(message, use_decimal=True)
        assert adserving.bidder.spendings.spend_account_key in message
        assert adserving.bidder.spendings.spend_camp_key in message
        assert adserving.bidder.spendings.spend_strat_key in message
        assert adserving.bidder.spendings.spend_strat_daily_key in message
        assert adserving.bidder.spendings.spend_strat_period_key in message
        # message should have twice that much of entries for campaigns
        assert len(message[adserving.bidder.spendings.spend_camp_key]) == 2 * Campaign.objects.count()
        for account, value in message[adserving.bidder.spendings.spend_account_key].iteritems():
            count = Campaign.objects.filter(account__id_random=account).count()
            # value should be equal to campaign numbers account holds (0.8 for spend, and 0.2 for commission above)
            assert value == count * adserving.bidder.spendings.cast_dbbid_to_CPM(1)


def test_redis_migration(db_factory_two_camps, redisdb_spendings):
    '''
    This test checks whether public ids in old format (without account part)
    will be corrected by update_bidder_spendings function. It also assures
    that data integrity (sum of campaign spends has to be equal to account
    spends) is checked in update_bidder_spendings
    '''
    strategy1 = Strategy.objects.get(name='Hello this is Citrus')
    campaign1 = strategy1.campaign

    strategy2 = Strategy.objects.get(name='Hello this is ninja')
    campaign2 = strategy2.campaign

    old_strategy1_public_id = strategy1.public_id.split(PUBLIC_ID_DELIMITER, 1)[1]
    old_campaign1_public_id = campaign1.id_random

    string_commission = adserving.bidder.spendings.string_commission

    redisdb_spendings.hset(adserving.bidder.spendings.spend_strat_key, old_strategy1_public_id, 1)
    redisdb_spendings.hset(adserving.bidder.spendings.spend_strat_key, strategy2.public_id, 2)
    redisdb_spendings.hset(adserving.bidder.spendings.spend_strat_daily_key, old_strategy1_public_id, 1)
    redisdb_spendings.hset(adserving.bidder.spendings.spend_strat_daily_key, strategy2.public_id, 2)
    redisdb_spendings.hset(adserving.bidder.spendings.spend_camp_key, old_campaign1_public_id + string_commission, 3)
    redisdb_spendings.hset(adserving.bidder.spendings.spend_camp_key, campaign2.public_id + string_commission, 4)

    redisdb_spendings.hset(adserving.bidder.spendings.spend_strat_key, strategy2.public_id + string_commission, 4)
    redisdb_spendings.hset(adserving.bidder.spendings.spend_strat_key, old_strategy1_public_id + string_commission, 3)
    redisdb_spendings.hset(adserving.bidder.spendings.spend_strat_period_key, strategy2.public_id, 2)
    redisdb_spendings.hset(adserving.bidder.spendings.spend_strat_period_key, old_strategy1_public_id, 1)
    redisdb_spendings.hset(adserving.bidder.spendings.budget_strat_period_key, strategy2.public_id, 2)
    redisdb_spendings.hset(adserving.bidder.spendings.budget_strat_period_key, old_strategy1_public_id, 1)
    redisdb_spendings.hset(adserving.bidder.spendings.spend_camp_key, campaign2.public_id, 2)
    redisdb_spendings.hset(adserving.bidder.spendings.spend_camp_key, old_campaign1_public_id, 1)

    # set account spends to different value than sum of campaign 1 and campaign 2 spends
    redisdb_spendings.hset(adserving.bidder.spendings.spend_account_key, campaign1.account.public_id, 1)

    update_bidder_spendings()

    assert redisdb_spendings.hgetall(adserving.bidder.spendings.spend_strat_key) == \
           {strategy1.public_id: '1', strategy2.public_id: '2',
            strategy1.public_id + string_commission: '3', strategy2.public_id + string_commission: '4'}
    assert redisdb_spendings.hgetall(adserving.bidder.spendings.spend_strat_daily_key) == \
           {strategy1.public_id: '1', strategy2.public_id: '2'}
    assert redisdb_spendings.hgetall(adserving.bidder.spendings.spend_strat_period_key) == \
           {strategy1.public_id: '1', strategy2.public_id: '2'}
    assert redisdb_spendings.hgetall(adserving.bidder.spendings.budget_strat_period_key) == \
           {strategy1.public_id: '1', strategy2.public_id: '2'}
    assert redisdb_spendings.hgetall(adserving.bidder.spendings.spend_camp_key) == \
           {campaign1.public_id: '1', campaign2.public_id: '2',
            campaign1.public_id + string_commission: '3', campaign2.public_id + string_commission: '4'}
    assert redisdb_spendings.hgetall(adserving.bidder.spendings.spend_account_key) == \
           {campaign1.account.public_id: '10'}
