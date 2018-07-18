'''
Classes that contains information about object state of given entities.
All classes are composite extension to their base models.
'''
from datetime import datetime


from ui.storage.models import Creative
from ui.common.states import BaseState


class CampaignState(BaseState):

    def __init__(self, campaign, *args, **kwargs):
        self.campaign = campaign

    def filter_creatives(self, filter_func):
        '''
        Returns list of creatives that are in strategies related
        to self.campaign.

        :param function filter_func: filter criterium function
        :rtype list of Creative objects
        '''
        return filter(
            filter_func,
            Creative.objects.campaign_related(self.campaign)
        )

    # "own" properties (related only to campaign)
    @property
    def has_budget(self):
        return self.campaign.has_budget

    @property
    def account_has_money(self):
        return self.campaign.account.account_balance() > 0

    @property
    def finished(self):
        return self.campaign.end_UTC < datetime.utcnow()

    @property
    def scheduled(self):
        return self.campaign.start_UTC > datetime.utcnow()

    @property
    def in_progress(self):
        return self.campaign.end_UTC > datetime.utcnow() > self.campaign.start_UTC

    # related properties (computed based on models related to campaign)
    @property
    def strategies_with_budget(self):
        return filter(
            lambda s: s.has_budget,
            self.campaign.strategy_set.filter(is_deleted=False)
        )

    @property
    def strategies_without_budget(self):
        return filter(
            lambda s: not s.has_budget,
            self.campaign.strategy_set.filter(is_deleted=False)
        )

    @property
    def creatives_audited(self):
        return self.filter_creatives(lambda creative: creative.state.audited)

    @property
    def creatives_rejected(self):
        return self.filter_creatives(lambda creative: creative.state.rejected)

    @property
    def creatives_pending(self):
        return self.filter_creatives(lambda creative: creative.state.pending)

    @property
    def creatives_expired(self):
        return self.filter_creatives(lambda creative: creative.state.expired)

    @property
    def creatives_brand_page_rejected(self):
        return self.filter_creatives(lambda creative: creative.state.brand_page_rejected)

    @property
    def is_running(self):
        """
        :rtype: bool
        :returns: ``True`` if campaign is running else ``False``.
        """
        return (
            self.campaign.is_deleted is False
            and self.campaign.is_paused is False
            and self.in_progress is True
            and self.has_budget is True
            and self.account_has_money is True
        )

    @property
    def waits_for_account_charging(self):
        """
        :rtype: bool
        :returns: ``True`` if campaign is ready to run but
            account is not charged.
        """
        return (
            self.campaign.is_deleted is False
            and self.campaign.is_paused is False
            and self.in_progress is True
            and self.has_budget is True
            and self.account_has_money is False
        )

    def to_dict(self):
        bools = ['has_budget', 'finished', 'scheduled', 'in_progress']
        lists = ['strategies_with_budget', 'strategies_without_budget',
                 'creatives_audited', 'creatives_rejected', 'creatives_pending',
                 'creatives_expired', 'creatives_brand_page_rejected']

        return self._make_state_dict(self, bools, lists)


class StrategyState(BaseState):

    def __init__(self, strategy, *args, **kwargs):
        self.strategy = strategy

    def filter_creatives(self, filter_func):
        '''
        Returns list of creatives that are related to self.strategy.

        :param function filter_func: filter criterium function
        :rtype list of Creative objects
        '''
        return filter(
            filter_func,
            Creative.objects.strategy_related(self.strategy)
        )

    # "own" properties (related only to strategy)
    @property
    def has_budget(self):
        return self.strategy.has_budget

    # related properties (computed based on models related to campaign)
    @property
    def campaign_is_paused(self):
        return self.strategy.campaign.is_paused

    @property
    def campaign_has_budget(self):
        return self.strategy.campaign.state.has_budget

    @property
    def campaign_scheduled(self):
        return self.strategy.campaign.state.scheduled

    @property
    def campaign_finished(self):
        return self.strategy.campaign.state.finished

    @property
    def campaign_in_progress(self):
        return self.strategy.campaign.state.in_progress

    @property
    def creatives_audited(self):
        return self.filter_creatives(lambda creative: creative.state.audited)

    @property
    def creatives_rejected(self):
        return self.filter_creatives(lambda creative: creative.state.rejected)

    @property
    def creatives_pending(self):
        return self.filter_creatives(lambda creative: creative.state.pending)

    @property
    def creatives_expired(self):
        return self.filter_creatives(lambda creative: creative.state.expired)

    @property
    def creatives_brand_page_rejected(self):
        return self.filter_creatives(lambda creative: creative.state.brand_page_rejected)

    @property
    def is_running(self):
        """
        :rtype: bool
        :returns: ``True`` if strategy is running else ``False``.
        """
        return (
            self.strategy.campaign.state.is_running is True
            and self.strategy.is_deleted is False
            and self.strategy.is_paused is False
            and self.has_budget is True
            and any(self.creatives_audited)
        )

    def to_dict(self):
        bools = ['has_budget', 'campaign_has_budget', 'campaign_scheduled',
                 'campaign_finished', 'campaign_in_progress']
        lists = ['creatives_audited', 'creatives_pending',
                 'creatives_rejected', 'creatives_expired',
                 'creatives_brand_page_rejected']

        return self._make_state_dict(self, bools, lists)


class AdvertState(BaseState):

    def __init__(self, advert, *args, **kwargs):
        self.advert = advert

    # related properties (computed based on models related to advert)
    @property
    def campaign_is_paused(self):
        return self.advert.strategy.campaign.is_paused

    @property
    def campaign_has_budget(self):
        return self.advert.strategy.campaign.state.has_budget

    @property
    def campaign_scheduled(self):
        return self.advert.strategy.campaign.state.scheduled

    @property
    def campaign_in_progress(self):
        return self.advert.strategy.campaign.state.in_progress

    @property
    def campaign_finished(self):
        return self.advert.strategy.campaign.state.finished

    @property
    def strategy_is_paused(self):
        return self.advert.strategy.is_paused

    @property
    def strategy_has_budget(self):
        return self.advert.strategy.state.has_budget

    @property
    def audited(self):
        """ True if creative is audited and brand is confirmed. """
        creative_state = self.advert.creative.state
        is_audited = creative_state.audited and creative_state.brand_page_confirmed
        return is_audited

    @property
    def rejected(self):
        return self.advert.creative.state.rejected

    @property
    def pending(self):
        return self.advert.creative.state.pending

    @property
    def blocked(self):
        return self.advert.creative.state.blocked

    @property
    def expired(self):
        return self.advert.creative.state.expired

    @property
    def is_running(self):
        """
        Is running flag determines if we bid on advert or not.

        :rtype: bool
        :returns: ``True`` if advert is running else ``False``.
        """
        return (
            self.advert.strategy.state.is_running is True
            and self.advert.is_deleted is False
            and self.advert.creative.is_deleted is False
            and self.audited is True
        )

    def to_dict(self):
        bools = ['campaign_has_budget', 'strategy_has_budget',
                 'campaign_scheduled', 'campaign_in_progress',
                 'campaign_finished', 'audited', 'rejected', 'pending',
                 'blocked', 'expired']
        lists = []

        return self._make_state_dict(self, bools, lists)
