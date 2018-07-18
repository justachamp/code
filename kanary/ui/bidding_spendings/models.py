from itertools import izip
from datetime import timedelta, datetime
from decimal import Decimal as UnsafeDecimal
from math import ceil
import logging

from django.db import models as m
from django_extensions.db.models import TimeStampedModel


from adserving.types import Decimal
from adserving.bidder.spendings import (
    cast_currency_to_CPM, cast_CPM_to_dbbid, string_commission, cast_dbbid_to_currency
)
from ui.fields import BudgetSpentDecimalField
from ui.common.models import RandomId, LatestUpdate
from ui.account.models import Account
from ui.settings import DISTRIBUTE_BUDGET_EVENLY_PERIOD


log = logging.getLogger('django')


class BaseSpendingImportable(object):

    """
    Import spendings for given subject (ad, strategy, campaign) from Redis.
    """

    @classmethod
    def _get_spendings(cls, rd, last_update, ordered_spend_key, spend_key):
        """
        get spending values and last spend times and aggregate it in a dict.
        :param redis rd: Redis Client
        :param ui.common.LatestUpdate last_update: previous time of spendings
                update
        :param string ordered_spend_key: Key for redis Sorted Set (zset)
            with spendings, ranked by time
        :param string spend_key: Key for redis Hash Set (hset) with spendings
        :returns spending value and last time when spend like:
            {'subject cache id', (spend_value, unix time)}
        :rtype dict
        """
        if not ordered_spend_key or not spend_key:
            raise ValueError('''ordered_spend_key and spend_key
                must be specified''')

        # timed spend list. Score: unixtime
        spends_list = rd.zrangebyscore(ordered_spend_key,
                                       max='+inf',
                                       min=last_update.to_secs,
                                       withscores=True)

        # no spending lately (from last_query to now)
        if not spends_list:
            return {}

        # process to dict
        spends_dict = cls.preprocess_spends_list(spends_list)

        # extract ids
        ids = spends_dict.keys()

        # get spending and commission values in the same order as times
        with rd.pipeline() as p:
            # get spending values
            p.hmget(spend_key, ids)
            # get their commissions (id + "_commission")
            p.hmget(spend_key, map(lambda i: i + string_commission, ids))
            spends, commissions = p.execute()

        # the same order - izip make sense
        for obj_id, spend, commission in izip(ids, spends, commissions):
            # make it one dict
            spends_dict[obj_id] = (
                int(spend), int(commission or 0), int(spends_dict[obj_id])
            )
        return spends_dict

    @classmethod
    def preprocess_spends_list(cls, spends_list):
        """
        Preprocess spends list (list of tuples (spend_key, timestamp) into a dictionary.

        :param list spends_list: list of spendings as read from redis by zrangebyscore
            [(spending_object_key, timestamp),...]
        :returns: processed spends_list
        :rtype: dict
        """
        return dict(spends_list)


class SpendingImportable(BaseSpendingImportable):

    '''
        Total spendings import functionality

        Requires inheriting class to define total_ordered_spendings_key and
        total_spendings_key class variables.
    '''

    # Key for redis Sorted Set (zset) with total spendings, ranked by time
    total_ordered_spendings_key = None

    # Key for redis Hash Set (hset) with total spendings
    total_spendings_key = None

    @classmethod
    def import_total_spendings(cls, rd):
        with cls.latest_update() as prev:
            spends_dict = cls.get_total_spendings(rd, prev)
            if len(spends_dict) == 0:
                return None
            saved_spendings = cls.save_spendings(spends_dict)

        return saved_spendings, prev.latest_update

    @classmethod
    def get_total_spendings(cls, rd, last_update):
        '''
        get spending values and last spend times and aggregate it in a dict.
        :param redis rd: Redis Client
        :param ui.common.LatestUpdate last_update: previous time of spendings
                update
        :returns spending value and last time when spend like:
            {'subject cache id', (spend_value, unix time)}
        :rtype dict
        '''
        return cls._get_spendings(
            rd,
            last_update,
            cls.total_ordered_spendings_key,
            cls.total_spendings_key
        )


class DailySpendingImportable(BaseSpendingImportable):

    '''
        Daily spendings import functionality

        Requires inheriting class to define daily_ordered_spendings_key and
        daily_spendings_key class variables.
    '''

    # Key for redis Sorted Set (zset) with total spendings, ranked by time
    daily_ordered_spendings_key = None

    # Key for redis Hash Set (hset) with total spendings
    daily_spendings_key = None

    @classmethod
    def import_daily_spendings(cls, rd):
        with cls.latest_daily_update() as prev:
            spends_dict = cls.get_daily_spendings(rd, prev)
            if len(spends_dict) == 0:
                return None
            saved_spendings = cls.save_daily_spendings(spends_dict)

        return saved_spendings, prev.latest_update

    @classmethod
    def clear_daily_spendings(cls, rd):
        '''
        Delete daily spendings keys from Redis, set daily spent to 0
            in all instances
        '''
        with rd.pipeline() as p:
            p.delete(cls.daily_ordered_spendings_key)
            p.delete(cls.daily_spendings_key)
            p.execute()
        return cls.reset_daily_spendings()

    @classmethod
    def get_daily_spendings(cls, rd, last_update):
        '''
        get spending values and last spend times and aggregate it in a dict.
        :param redis rd: Redis Client
        :param ui.common.LatestUpdate last_update: previous time of spendings
                update
        :returns spending value and last time when spend like:
            {'subject cache id', (spend_value, unix time)}
        :rtype dict
        '''
        return cls._get_spendings(
            rd,
            last_update,
            cls.daily_ordered_spendings_key,
            cls.daily_spendings_key
        )


class Spendable(SpendingImportable, RandomId, TimeStampedModel):

    '''
    Base class for models that register spendings and implement
    budget limit
    '''

    budget_spent = BudgetSpentDecimalField(default=0)
    budget_spent_commission = BudgetSpentDecimalField(default=0)

    class Meta:
        abstract = True

    @property
    def budget_spent_with_commission(self):
        """Calculate budget spent with commission."""
        return self.budget_spent + self.budget_spent_commission

    @property
    def budget_left(self):
        """Return amount of budget left to operate on."""
        return max(0, self.budget_total - self.budget_spent_with_commission)

    @property
    def has_budget(self):
        return self.budget_left > 0

    def save_spending(self, spent_value, commission):
        '''
        :param int spent_value: spent value
        :param int commission: commission value
        :rtype: Spendable
        :returns: instance of :class:`Spendable`
        '''
        self.budget_spent = cast_dbbid_to_currency(spent_value)
        self.budget_spent_commission = cast_dbbid_to_currency(commission)
        self.save()
        return self

    @classmethod
    def latest_update(cls):
        return LatestUpdate.by_name(cls.__name__)

    @classmethod
    def save_spendings(cls, obj_spends):
        """
        Saves spendings for dict of cache objects.
        """
        saved = []
        for spendable in cls.objects_by_public_ids(obj_spends.keys()):
            spend, commission, spend_time = obj_spends[spendable.public_id]
            spendable.save_spending(spend, commission)
            saved.append(spendable)
        return saved


class DailySpendable(DailySpendingImportable, m.Model):

    '''
    Base class for models that register daily spendings and implement
    daily spendings limit
    '''

    budget_daily_spent = BudgetSpentDecimalField(default=0)

    class Meta:
        abstract = True

    @property
    def budget_daily_left(self):
        if not self.budget_daily:
            return 0

        return max(0, self.budget_daily - self.budget_daily_spent)

    def save_daily_spending(self, spent_value):
        self.budget_daily_spent = cast_dbbid_to_currency(spent_value)
        self.save()
        return self

    @classmethod
    def latest_daily_update(cls):
        return LatestUpdate.by_name(cls.__name__ + 'Daily')

    @classmethod
    def save_daily_spendings(cls, obj_spends):
        '''
        saves spendings for dict of cache objects
        '''
        saved = []
        for spendable in cls.objects_by_public_ids(obj_spends.keys()):
            spend, commission, spend_time = obj_spends[spendable.public_id]
            spendable.save_daily_spending(spend)
            saved.append(spendable)
        return saved

    @classmethod
    def reset_daily_spendings(cls):
        '''
        Set daily spent to 0 in all objects where daily spent > 0
        '''
        saved = []
        for spendable in cls.objects.filter(budget_daily_spent__gt=0):
            spendable.save_daily_spending(0)
            saved.append(spendable)
        return saved


class Distributable():

    '''
    Base class for models that should implement "Distribute evenly" feature.
    '''

    # Period in seconds
    period_length = DISTRIBUTE_BUDGET_EVENLY_PERIOD

    # Key for redis Hash Set (hset) with period spendings
    period_spendings_key = None
    # Key for redis Hash Set (hset) with period budgets
    period_budgets_key = None

    def seconds_until_end_of_campaign(self, now):
        return (self.campaign.end_UTC - now).total_seconds()

    def seconds_until_end_of_day(self, now):
        day_spent = timedelta(hours=now.hour,
                              minutes=now.minute,
                              seconds=now.second)
        return (timedelta(hours=24) - day_spent).total_seconds()

    def periods_left(self, now):
        '''
        Calculate the number of pacing periods left until of day or end
        of campaign. Numbers of periods are rounded up.

        :param datetime now: UTC datetime containing current time
        :returns the smaller of two - amount of periods until the end of day
            and until the end of campaign. If campaign has ended returns 0.
        :rtype float
        '''
        if now >= self.campaign.end_UTC:
            return 0

        end_of_campaign = self.seconds_until_end_of_campaign(now)
        end_of_day = self.seconds_until_end_of_day(now)

        seconds_left = end_of_campaign if not self.budget_daily \
            else min(end_of_day, end_of_campaign)

        return ceil(seconds_left / float(self.period_length))

    def period_budget(self, now):
        '''
        Calculate the period budget based on budget left and period length

        :param datetime now: UTC datetime containing current time
        :returns amount of money to spend in current period
        :rtype Decimal
        '''
        effective_budget = self.budget_left if not self.budget_daily \
            else min(self.budget_daily_left, self.budget_left)

        periods_left = self.periods_left(now)

        if not periods_left:
            return Decimal(0)

        # Period budgets are based on real time so they are ok to
        # be constructed from floats (that leads to 'ugly'
        # decimals).
        return (effective_budget / UnsafeDecimal(periods_left)
                * UnsafeDecimal(self.bidding_periods_ratio()))

    @classmethod
    def running(cls, query_set=None):
        """
        Return list of all active strategies for given query set or all visible objects.

        :param QuerySet query_set: [optional] query_set to filter
        :return: running objects according to query_set
        :rtype: list
        """
        if query_set is None:
            query_set = cls.objects_visible.all()
        return filter(lambda s: s.state.is_running, query_set)

    @classmethod
    def get_period_budgets(cls, now):
        """
        Get period budgets for all running and distributed evenly strategies

        :param datetime now: UTC datetime used to calculate remaining budget

        :returns: a dictionary where key is strategies public_id and value is
            period budget
        :rtype: dict
        """
        limits_dict = {}
        strategies = cls.objects_visible.filter(is_distributed_evenly=True)
        strategies = cls.running(strategies)

        for strategy in strategies:
            limits_dict[strategy.public_id] = strategy.period_budget(now)

        log.info('[SPENDINGS] Period budgets calculated (currency): {0}'.format(limits_dict))

        # Cast to budget precision used in Redis
        return {strategy: cast_CPM_to_dbbid(cast_currency_to_CPM(budget)) for strategy, budget in limits_dict.items()}

    @classmethod
    def reset_period_budgets(cls, rd):
        """
        Save new period budget to redis, and clear old stale period spendings data at once.

        Uses pipeline to make sure all these information will be executed without any pause.
        """
        now = datetime.utcnow()
        period_budgets = cls.get_period_budgets(now)
        spends = rd.hgetall(cls.period_spendings_key)
        spends_currency = {s: cast_dbbid_to_currency(spent) for s, spent in spends.items()}
        log.info('[SPENDINGS] Period spends read (dbbid, CPM): {0}'.format(spends))
        log.info('[SPENDINGS] Period spends read (currency): {0}'.format(spends_currency))

        with rd.pipeline() as p:
            p.delete(cls.period_budgets_key)
            if period_budgets:
                p.hmset(cls.period_budgets_key, period_budgets)
            p.delete(cls.period_spendings_key)
            p.execute()

        return period_budgets


class DailySpendings(m.Model):

    '''
    A model storing information about daily spendings per account
    for billing purposes.

    Spent budget, hidden commission, kanary commission, data costs
    '''

    date = m.DateField()
    account = m.ForeignKey(
        Account, related_name="daily_spendings", null=False
    )
    budget_spent = BudgetSpentDecimalField(default=0)
    audit_fees = BudgetSpentDecimalField(default=0)
    """
    Sum of what account had spent on audits given day.

    .. note:

        It's triplication of the information stored in Account and Creative,
        used for invoicing - We know when we spent the money.
    """
    hidden_commission = BudgetSpentDecimalField(default=0)
    kanary_commission = BudgetSpentDecimalField(default=0)

    data_cost_proximic = BudgetSpentDecimalField(default=0)
    data_cost_peer39 = BudgetSpentDecimalField(default=0)
    data_cost_lotame = BudgetSpentDecimalField(default=0)

    class Meta:
        ordering = (
            'account', '-date'
        )
        unique_together = (
            ('account', 'date'),
        )
