import datetime
from collections import defaultdict

import simplejson
from django.conf import settings
from celery import task
from celery.utils.log import get_task_logger

from adserving.types import Decimal
import adserving.bidder.spendings as spending
from etc.constants import SPENDING_INFO_CHANNEL, PUBLIC_ID_DELIMITER
from ui.tasks import RedisTask
from ui.campaign.models import Campaign, Strategy
from ui.bidding_spendings.models import DailySpendings

from adserving.bidder.spendings.constants import DATE_FORMAT, DATE_GLOB_ALL


log = get_task_logger(__name__)


class BiddingSpendingsRedisTask(RedisTask):
    host = settings.REDIS['bidder_spendings']['host']
    port = settings.REDIS['bidder_spendings']['port']
    db = settings.REDIS['bidder_spendings']['db']

    def __init__(self, *args, **kwargs):
        RedisTask.__init__(self, *args, **kwargs)
        # infinite in-memory cache
        self.reset_cache()

    def reset_cache(self):
        """Reset's locally hold cache."""
        self.cache = {}


@task(base=BiddingSpendingsRedisTask)
def put_spendings_to_daily_spendings():
    rd = put_spendings_to_daily_spendings.rd
    update_daily_spendings(rd=rd)


@task(base=BiddingSpendingsRedisTask)
def put_today_spendings_to_daily_spendings():
    rd = put_today_spendings_to_daily_spendings.rd
    date, _time = str(datetime.datetime.utcnow()).split()

    keys_regexp = DATE_FORMAT.format(date=date) + "*"

    update_daily_spendings(keys_regexp=keys_regexp, rd=rd)


def update_daily_spendings(keys_regexp=DATE_GLOB_ALL, rd=None):
    """
    Get daily spendings from redis and put them to
    DailySpendings.
    """

    keys = rd.keys(keys_regexp)

    spendings = defaultdict(dict)
    models = {}

    for key in keys:
        # get date and public id of camp
        try:
            date, _, camp_public_id = key.split(PUBLIC_ID_DELIMITER)
        except ValueError:
            # Old format.
            # We don't need to worry about same account having new and old format keys
            # because the values are summed below.
            # TODO: Restore previous code when all 'date:*' hashes with old format names are deleted. KANARY-1929.
            # After that find some folk singer to sing about how the old format was better.
            date, camp_public_id = key.split(PUBLIC_ID_DELIMITER)
        _, date = date.split(':')

        # add model to dict if not exists
        if camp_public_id not in models:
            models[camp_public_id] = Campaign.objects.get(
                id_random=camp_public_id
            )

        # get account id and values from redis
        # values like
        # {"spent": "123000", "commission": "123", "hidden_commission" "123"}
        account_id = models[camp_public_id].account.id
        values = rd.hgetall(key)

        acc_date = "{acc_id}_{date}".format(acc_id=account_id, date=date)

        # initiate defaultdict
        # why acc_date? Because we aggregated per account, not per campaign
        if not spendings[acc_date]:
            spendings[acc_date] = defaultdict(int)

        for k, v in values.items():
            # mapping from string to int
            spendings[acc_date][k] += int(v)

    for acc_date, values in spendings.items():
        # get items and update models in database
        account_id, date = acc_date.split("_")

        daily_spendings, created = DailySpendings.objects.get_or_create(
            date=date,
            account_id=account_id
        )

        daily_spendings.budget_spent = spending.cast_dbbid_to_currency(
            values["spent"]
        )

        daily_spendings.hidden_commission = spending.cast_dbbid_to_currency(
            values["hidden_commission"]
        )

        daily_spendings.kanary_commission = spending.cast_dbbid_to_currency(
            values["commission"]
        )

        daily_spendings.data_cost_proximic = spending.cast_dbbid_to_currency(
            values["proximic_price"]
        )

        daily_spendings.data_cost_peer39 = spending.cast_dbbid_to_currency(
            values["peer39_price"]
        )

        daily_spendings.data_cost_lotame = spending.cast_dbbid_to_currency(
            values["lotame_price"]
        )

        daily_spendings.save()


@task(base=BiddingSpendingsRedisTask)
def import_spendings():
    '''
    Pull spendings from Redis to Django. Update pacing period budgets
    based on fresh spendings.
    '''

    rd = import_spendings.rd

    Strategy.import_total_spendings(rd)

    Strategy.import_daily_spendings(rd)

    Campaign.import_total_spendings(rd)

    period_budgets = Strategy.reset_period_budgets(rd)
    log.info('[SPENDINGS] Period budgets set (dbbid, CPM): {0}'.format(period_budgets))


def check_format_of_keys(rd, spendings, key, part_count, model):
    '''
    Check whether all keys in spendings are in new format - with account random id.
    In case of wrong keys make changes also to redis database

    :param rd: redis client
    :param dict spendings: spendings dictionary to be checked with respect to format
        of keys. Keys are either public id or public id with spending.string_commission
        concatenated at the end. Values in dictionary are amount of spent budget.
    :param str key: key under which spendings is stored in redis database
    :param int part_count: number of random id parts in public id that would mean
        that account random id is missing
    :param type model: model for which id is to be fixed
    :return: dictionary with correct keys
    :rtype: dict
    '''
    pipe = rd.pipeline()
    for public_id, value in spendings.items():
        old_public_id = public_id
        if public_id.endswith(spending.string_commission):
            public_id = public_id[:-len(spending.string_commission)]
            with_commission = True
        else:
            with_commission = False

        if len(public_id.split(PUBLIC_ID_DELIMITER)) == part_count:
            random_id = public_id.split(PUBLIC_ID_DELIMITER)[-1]
            obj = model.objects.get(id_random=random_id)
            public_id = obj.public_id

            if with_commission:
                public_id = public_id + spending.string_commission

            spendings[public_id] = value
            del spendings[old_public_id]

            pipe.hincrby(key, public_id, value)
            pipe.hdel(key, old_public_id)

    pipe.execute()
    return spendings


@task(base=BiddingSpendingsRedisTask)
def update_bidder_spendings():
    '''
    Publish all spendings and budgets update notification to Redis pub/sub,
    notify slave bidders to receive this information
    '''
    rd = update_bidder_spendings.rd
    campaign_key = spending.spend_camp_key
    strategy_key = spending.spend_strat_key
    strategy_daily_key = spending.spend_strat_daily_key
    strategy_period_spend_key = spending.spend_strat_period_key
    account_key = spending.spend_account_key

    # Pacing period budgets are saved to Redis directly, not using cache mapper
    # because they need to be updated often, not only when strategies
    # have changed
    strategy_period_budget_key = spending.budget_strat_period_key

    spendings = {
        campaign_key: rd.hgetall(campaign_key),
        strategy_key: rd.hgetall(strategy_key),
        strategy_daily_key: rd.hgetall(strategy_daily_key),
        strategy_period_spend_key: rd.hgetall(strategy_period_spend_key),
        strategy_period_budget_key: rd.hgetall(strategy_period_budget_key),
        account_key: rd.hgetall(account_key),
    }

    # checking if keys are in new format (with account random id)
    # campaign
    spendings[campaign_key] = check_format_of_keys(rd, spendings[campaign_key], campaign_key, 1, Campaign)
    # strategy
    spendings[strategy_key] = check_format_of_keys(rd, spendings[strategy_key], strategy_key, 2, Strategy)
    # strategy daily
    spendings[strategy_daily_key] = check_format_of_keys(rd, spendings[strategy_daily_key],
                                                         strategy_daily_key, 2, Strategy)
    # strategy period
    spendings[strategy_period_spend_key] = check_format_of_keys(rd, spendings[strategy_period_spend_key],
                                                                strategy_period_spend_key, 2, Strategy)
    # strategy period budget
    spendings[strategy_period_budget_key] = check_format_of_keys(rd, spendings[strategy_period_budget_key],
                                                                 strategy_period_budget_key, 2, Strategy)

    # checking whether account spendings are correctly set in redis database
    account_spendings = defaultdict(Decimal)

    for campaign_id, campaign_spend in spendings[campaign_key].iteritems():
        # get account_id for given campaign.
        account_id = campaign_id.split(PUBLIC_ID_DELIMITER)[0]
        # and add it to account_spendings
        account_spendings[account_id] += Decimal(campaign_spend)

    for account_id in account_spendings:
        if account_id not in spendings[account_key] \
                or Decimal(spendings[account_key][account_id]) != account_spendings[account_id]:
            spendings[account_key][account_id] = account_spendings[account_id]
            rd.hset(account_key, account_id, account_spendings[account_id])

    # cast prices to CPM
    for d in spendings.values():
        for key, value in d.items():
            d[key] = spending.cast_dbbid_to_CPM(value)

    spendings_json = simplejson.dumps(spendings)
    rd.publish(SPENDING_INFO_CHANNEL, spendings_json)


@task(base=BiddingSpendingsRedisTask)
def clear_daily_spendings():
    '''
    Clear daily spendings in Redis and Postgres
    '''
    rd = clear_daily_spendings.rd
    Strategy.clear_daily_spendings(rd)
