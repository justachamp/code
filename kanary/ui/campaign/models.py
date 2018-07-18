from adserving.types import Decimal
from datetime import datetime, timedelta
from functools import partial
from collections import defaultdict
from operator import itemgetter

from django.db import transaction, models as m
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db.models import Q
from django.core.exceptions import ValidationError
from django_extensions.db.models import TimeStampedModel


import adserving.bidder.spendings as spending
from adserving.adserver.utils import adserver_url

from bidrequest.constants import VideoDuration, EXCHANGES

from etc.constants import CONV_PATH, CONV_VALUE_PLACEHOLDER, PUBLIC_ID_DELIMITER
from etc import dimensions
from ui.common.models import RandomId, KanaryDirtyFieldsMixin, public_id_randomizer
from ui.account.models import Account
from ui.storage.models import Creative, Audience, creative_factory
from ui.publishers.models import PublisherSet

from ui.fields import BudgetDecimalField, SmallDecimalField, CPMDecimalField, CharField255, LongURLField
from ui.utils import get_period_quarters, unique_slugify, is_timezoned

from ui.targeting.models import (
    TargetValue,
    ContentCategory,
    SegmentProximicMaturityRating,
    SegmentProximicSafetyLevel,
    SegmentProximicPageQuality,
    SegmentProximicPageNoticeability,
    SegmentProximicPagePlacement,
    SegmentProximicContextual,
    SegmentProximicPageLanguage,
    Peer39PageLanguage,
    Peer39ContextualSegment,
    Peer39BrandProtection,
    Peer39PageQuality,
    LotameDemographic,
    LotameAdvancedDemographic,
    LotameBehavioralInterest,
    LotameInfluencers,
    LotameOffline
)

from ui.notification.models import Event
from ui.cache.base_models import CacheMapped
from ui.bidding_spendings.models import Spendable, DailySpendable, Distributable

from adserving.optimizer.metrics import OPTIMIZATION_METRICS


class Site(m.Model):

    url = LongURLField(null=True)
    owner = m.ForeignKey(Account, related_name='sites')

    class Meta:
        unique_together = ('url', 'owner')

    def __unicode__(self):
        return '%s' % (self.url)

    @property
    def strategies(self):
        return Strategy.objects.filter(landing_sites__site=self)

    @property
    def adverts(self):
        return Advert.objects.filter(strategy__landing_sites__site=self)


# Capping periods:
CAP_PERIODS = (
    ('hour', 'h'),
    ('day', 'd'),
    ('month', 'm'),
    ('year', 'y'),
)
MAX_CAP_NAME_LENGTH = max([len(x[0]) for x in CAP_PERIODS])

CapField = partial(m.CharField, null=True, blank=True, choices=CAP_PERIODS,
                   max_length=MAX_CAP_NAME_LENGTH)


class Campaign(KanaryDirtyFieldsMixin, Spendable, CacheMapped):

    def __init__(self, *args, **kwargs):
        from .states import CampaignState

        super(Campaign, self).__init__(*args, **kwargs)
        self.state = CampaignState(self)

    class Meta:
        ordering = ('name', )
        unique_together = (
            ('account', 'slug'),
        )

    class Status:
        paused = 'paused'
        archived = 'archived'
        finished = 'finished'
        scheduled = 'scheduled'
        out_of_budget = 'outOfBudget'

    # fields
    account = m.ForeignKey(Account)
    name = CharField255()
    slug = CharField255()

    start_UTC = m.DateTimeField()
    end_UTC = m.DateTimeField()

    is_paused = m.BooleanField(default=False)
    is_archived = m.BooleanField(default=False)

    budget_total = BudgetDecimalField()

    # checkbox state for capping
    cap_campaign_selected = m.BooleanField(blank=True, default=False)
    cap_strategy_selected = m.BooleanField(blank=True, default=False)
    cap_creative_selected = m.BooleanField(blank=True, default=False)

    cap_total = m.IntegerField(null=True, blank=True)
    cap_strategy = m.IntegerField(null=True, blank=True)
    cap_creative = m.IntegerField(null=True, blank=True)

    cap_total_period = CapField()
    cap_strategy_period = CapField()
    cap_creative_period = CapField()

    # values presented in form
    cap_total_presented = m.IntegerField(null=True, blank=True)
    cap_strategy_presented = m.IntegerField(null=True, blank=True)
    cap_creative_presented = m.IntegerField(null=True, blank=True)
    cap_total_period_presented = CapField()
    cap_strategy_period_presented = CapField()
    cap_creative_period_presented = CapField()

    landing_site = m.ForeignKey(Site, null=False, on_delete=m.PROTECT)

    # Keys user by ui.bidding_spendings.importable
    total_ordered_spendings_key = spending.ordered_strat_spends
    """If strategy spendings have changed then campaign spendings has changed as well."""
    total_spendings_key = spending.spend_camp_key

    # class methods

    @classmethod
    def slugify_name(cls, campaign):
        return unique_slugify(campaign, {'account': campaign.account})

    # properties
    @property
    def full_name(self):
        return self.name

    @property
    def public_id_parts(self):
        return self.account.id_random, self.id_random

    @property
    def strategy_visible_set(self):
        ''' strategies which are visible to UI (not removed by user) '''
        return self.strategy_set.filter(is_deleted=False)

    @property
    def status(self):
        if self.is_archived:
            return self.Status.archived

        now = datetime.utcnow()
        if self.end_UTC <= now:
            return self.Status.finished
        if self.start_UTC > now:
            return self.Status.scheduled
        if self.budget_left == 0:
            return self.Status.out_of_budget

        return self.Status.paused

    @property
    def adverts(self):
        return Advert.objects.filter(strategy__campaign=self.pk)

    @property
    def seconds_left(self):
        '''
            Number of seconds left in campaign.
            :rtype: int
            :returns: 0 for finished, end - now for running, end - start
                for scheduled
        '''
        if self.state.finished:
            return 0
        elif self.state.scheduled:
            return (self.end_UTC - self.start_UTC).total_seconds()
        else:
            return (self.end_UTC - datetime.utcnow()).total_seconds()

    # instance methods

    def __unicode__(self):
        return self.name

    def copy(self):
        '''makes self a cloned object'''

        old_strategies = self.strategy_set.all()

        # new name
        i = 1
        new_name = self.name + ' (copy)'
        while Campaign.objects.filter(name=new_name).exclude(id=self.id)\
                .exists():
            new_name = self.name + ' (copy-{0})'.format(i)
            i += 1
        self.name = new_name

        self.id = self.pk = None
        self.id = None
        self.id_random = public_id_randomizer()
        self.save()

        for strategy in old_strategies:
            strategy.copy(campaign=self)

    @property
    def conversion_def(self):
        conversion, _ = Conversion.objects.get_or_create(campaign=self)
        return conversion

    @conversion_def.setter
    def conversion_def(self, newProperties):
        conversion, _ = Conversion.objects.get_or_create(campaign=self)
        conversion.name = newProperties['name']
        conversion.value = newProperties['value']
        conversion.save()

    @property
    def conversion_tracking_code(self):
        src = adserver_url(
            path=CONV_PATH,
            query={'campaign': self.public_id, 'value': CONV_VALUE_PLACEHOLDER},
            is_secure=None
        )
        return '<img src="{0}" alt="" />'.format(src)

    @classmethod
    def preprocess_spends_list(cls, spends_list):
        """
        Preprocess spends list (list of tuples (spend_key, timestamp) into a dictionary.

        Convert from dictionary of strategies into dictionary of campaigns,
        using the most recent timestamp extracted for campaign's strategies.

        :param list spends_list: list of spendings as read from redis by zrangebyscore
            [(spending_object_key, timestamp),...]
        :returns: processed spends_list
        :rtype: dict
        """
        spends = super(Campaign, cls).preprocess_spends_list(spends_list)
        processed_spends = {}
        for strategy_key, timestamp in spends.iteritems():
            campaign_key = strategy_key.rsplit(PUBLIC_ID_DELIMITER, 1)[0]
            processed_spends[campaign_key] = max(timestamp, processed_spends.get(campaign_key))
        return processed_spends


@receiver(pre_save, sender=Campaign, weak=False)
def campaign_pre_save(sender, instance, **kwargs):
    campaign = instance
    strategies = campaign.strategy_set

    # update slug
    campaign.slug = Campaign.slugify_name(campaign)

    # Increasing total budget to equal spent budget
    # should only happen if user changes budget in UI
    if campaign.has_changed('budget_spent'):
        # Total budget shouldn't change if new spending values are imported
        return

    if campaign.budget_total < campaign.budget_spent:
        campaign.budget_total = campaign.budget_spent

    for strategy in strategies.filter(budget_total__gt=campaign.budget_total):
        strategy.budget_total = campaign.budget_total
        strategy.save()


@receiver(post_save, sender=Campaign, weak=False)
def campaign_post_save(sender, instance, created, **kwargs):
    if created:
        Event.objects.create_campaign_created(instance)


class Conversion(KanaryDirtyFieldsMixin, m.Model):
    name = CharField255(blank=False, default="New conversion")
    value = SmallDecimalField(blank=False, default=1)
    active = m.BooleanField(default=False)
    campaign = m.ForeignKey(Campaign)


class SiteRatio(m.Model):

    site = m.ForeignKey(Site, on_delete=m.PROTECT)
    ratio = m.IntegerField(default=1)
    custom_variable = m.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        try:
            return '%s - %s' % (str(self.site), self.ratio)
        except Site.DoesNotExist:
            return self.ratio

    @property
    def adverts(self):
        return Advert.objects.filter(strategy__landing_sites=self)

    # class methods

    @classmethod
    def all_with_percent(cls, strategy_pk):
        '''
        Args:
            strategy_pk
        Returns:
            generator of tuples (site.pk(int), ratio(int), percent(float))
        '''
        sites = cls.objects.filter(strategy__pk=strategy_pk)
        ratio_all = sites.aggregate(m.Sum('ratio')).get('ratio__sum', 0)
        for site in sites:
            yield {
                'id': site.site.pk,
                'weight': site.ratio,
                'url': site.site.url,
                'custom_variable': site.custom_variable,
                'percent': 100. * site.ratio / ratio_all
            }


M2MField = partial(m.ManyToManyField, blank=True)


M2MFieldExclude = partial(M2MField, related_name='exclude')


class Strategy(KanaryDirtyFieldsMixin, Spendable, DailySpendable, Distributable, CacheMapped):

    FACEBOOK = 'fb'
    SITE = 'site'
    MOBILE = 'app'

    STRATEGY_TYPES = (
        ('Facebook', FACEBOOK),
        ('Web', SITE),
        ('Mobile', MOBILE),
    )

    # Map of relations between dimensions and model fields
    DIMENSIONS_TO_FIELDS_MAP = {
        dimensions.country: 'targeting_values',
        dimensions.region: 'targeting_values',
        dimensions.city: 'targeting_values',
        dimensions.g_location: 'targeting_values',
        dimensions.os: 'targeting_values',
        dimensions.age_group: 'targeting_values',
        dimensions.gender: 'targeting_values',
        dimensions.carrier: 'targeting_values',
        dimensions.g_device: 'targeting_values',
        dimensions.content_category: 'content_category_values',

        dimensions.proximic_maturity_rating: 'segment_proximic_maturity_rating',
        dimensions.proximic_safety_level: 'segment_proximic_safety_level',
        dimensions.proximic_page_quality: 'segment_proximic_page_quality',
        dimensions.proximic_page_noticeability: 'segment_proximic_page_noticeability',
        dimensions.proximic_page_placement: 'segment_proximic_page_placement',
        dimensions.proximic_contextual: 'segment_proximic_contextual',
        dimensions.proximic_page_language: 'segment_proximic_page_language',

        dimensions.peer_page_language: 'segment_peer_page_language',
        dimensions.peer_brand_protection: 'segment_peer_brand_protection',
        dimensions.peer_contextual: 'segment_peer_contextual',
        dimensions.peer_page_quality: 'segment_peer_page_quality',

        dimensions.lotame_demographic: 'segment_lotame_demographic',
        dimensions.lotame_advanced_demographic: 'segment_lotame_advanced_demographic',
        dimensions.lotame_behavioral_interest: 'segment_lotame_behavioral_interest',
        dimensions.lotame_influencers: 'segment_lotame_influencers',
        dimensions.lotame_offline: 'segment_lotame_offline',
    }

    def __init__(self, *args, **kwargs):
        from .states import StrategyState

        super(Strategy, self).__init__(*args, **kwargs)
        self.state = StrategyState(self)

    class Meta:
        ordering = ['name']
        unique_together = [('campaign', 'slug')]

    campaign = m.ForeignKey(Campaign, null=False)

    name = CharField255()
    slug = CharField255()

    type = m.CharField(max_length=6, null=False, choices=STRATEGY_TYPES,
                       default=SITE)

    is_paused = m.BooleanField(default=False)
    is_reviewed = m.BooleanField(default=True)

    budget_total = BudgetDecimalField()
    budget_daily = BudgetDecimalField(null=True, blank=True)

    is_distributed_evenly = m.BooleanField(default=False)

    budget_bid_CPM = CPMDecimalField(null=True, blank=True)

    # Options for bid price optimization
    optimized_metric = m.CharField(choices=OPTIMIZATION_METRICS, max_length=3, null=True, blank=True)
    is_automatically_bidded = m.BooleanField(default=False)

    # impressions limits
    capping_day = m.IntegerField(null=True, blank=True)
    capping_total = m.IntegerField(null=True, blank=True)

    capping_day_spent = m.IntegerField(default=0)
    capping_total_spent = m.IntegerField(default=0)

    # is_targeted
    is_targeted_local = m.BooleanField(default=False)  # localization
    is_targeted_devices = m.BooleanField(default=False)
    is_targeted_publisher = m.BooleanField(default=False)
    is_targeted_user_profile = m.BooleanField(default=False)

    targeting_values = m.ManyToManyField(TargetValue, blank=True)
    targeting_values_exclude = M2MFieldExclude(TargetValue)

    content_category_values = m.ManyToManyField(ContentCategory, blank=True)
    content_category_values_exclude = M2MFieldExclude(ContentCategory)

    # We require this set in order to proper dump information about ad's
    # segments into cache.
    # It's mostly required for proper calculation of spendings after winning
    # the auction in winnotice.
    segments = {
        'segment_proximic_maturity_rating',
        'segment_proximic_safety_level',
        'segment_proximic_page_quality',
        'segment_proximic_contextual',
        'segment_proximic_page_language',
        'segment_proximic_page_noticeability',
        'segment_proximic_page_placement',

        'segment_peer_page_quality',
        'segment_peer_contextual',
        'segment_peer_brand_protection',
        'segment_peer_page_language',

        'segment_lotame_demographic',
        'segment_lotame_advanced_demographic',
        'segment_lotame_behavioral_interest',
        'segment_lotame_influencers',
        'segment_lotame_offline',
    }

    segment_proximic_maturity_rating = M2MField(
        SegmentProximicMaturityRating
    )
    segment_proximic_maturity_rating_exclude = M2MFieldExclude(
        SegmentProximicMaturityRating
    )

    segment_proximic_safety_level = M2MField(
        SegmentProximicSafetyLevel
    )
    segment_proximic_safety_level_exclude = M2MFieldExclude(
        SegmentProximicSafetyLevel
    )

    segment_proximic_page_quality = M2MField(
        SegmentProximicPageQuality
    )
    segment_proximic_page_quality_exclude = M2MFieldExclude(
        SegmentProximicPageQuality
    )

    segment_proximic_page_noticeability = M2MField(
        SegmentProximicPageNoticeability
    )
    segment_proximic_page_noticeability_exclude = M2MFieldExclude(
        SegmentProximicPageNoticeability
    )

    segment_proximic_page_placement = M2MField(
        SegmentProximicPagePlacement
    )
    segment_proximic_page_placement_exclude = M2MFieldExclude(
        SegmentProximicPagePlacement
    )

    segment_proximic_contextual = M2MField(
        SegmentProximicContextual
    )
    segment_proximic_contextual_exclude = M2MFieldExclude(
        SegmentProximicContextual
    )

    segment_proximic_page_language = M2MField(
        SegmentProximicPageLanguage
    )

    segment_proximic_page_language_exclude = M2MFieldExclude(
        SegmentProximicPageLanguage
    )

    segment_peer_page_language = M2MField(
        Peer39PageLanguage
    )

    segment_peer_page_language_exclude = M2MFieldExclude(
        Peer39PageLanguage
    )

    segment_peer_page_quality = M2MField(
        Peer39PageQuality
    )

    segment_peer_page_quality_exclude = M2MFieldExclude(
        Peer39PageQuality
    )

    segment_peer_contextual = M2MField(
        Peer39ContextualSegment
    )

    segment_peer_contextual_exclude = M2MFieldExclude(
        Peer39ContextualSegment
    )

    segment_peer_brand_protection = M2MField(
        Peer39BrandProtection
    )

    segment_peer_brand_protection_exclude = M2MFieldExclude(
        Peer39BrandProtection
    )

    segment_peer_page_quality = M2MField(
        Peer39PageQuality
    )

    segment_peer_page_quality_exclude = M2MFieldExclude(
        Peer39PageQuality
    )

    segment_lotame_demographic = M2MField(
        LotameDemographic
    )

    segment_lotame_demographic_exclude = M2MFieldExclude(
        LotameDemographic
    )

    segment_lotame_advanced_demographic = M2MField(
        LotameAdvancedDemographic
    )

    segment_lotame_advanced_demographic_exclude = M2MFieldExclude(
        LotameAdvancedDemographic
    )

    segment_lotame_behavioral_interest = M2MField(
        LotameBehavioralInterest
    )

    segment_lotame_behavioral_interest_exclude = M2MFieldExclude(
        LotameBehavioralInterest
    )

    segment_lotame_influencers = M2MField(
        LotameInfluencers
    )

    segment_lotame_influencers_exclude = M2MFieldExclude(
        LotameInfluencers
    )

    segment_lotame_offline = M2MField(
        LotameOffline
    )

    segment_lotame_offline_exclude = M2MFieldExclude(
        LotameOffline
    )

    audiences = \
        m.ManyToManyField(Audience, related_name="includes", blank=True)
    audiences_exclude = \
        m.ManyToManyField(Audience, related_name="excludes", blank=True)
    publisherset = m.ForeignKey(PublisherSet, null=True, blank=True)

    landing_sites = m.ManyToManyField(SiteRatio)
    landing_site_variable = m.CharField(max_length=511, null=True, blank=True)

    is_UTM_tags = m.BooleanField(default=False)

    # day parting
    is_day_parted = m.BooleanField(default=False)

    is_bid_on_unknown_users = m.BooleanField(default=False)

    time_mask = "%H:%M"

    # Keys used by ui.bidding_spendings.SpendingImportable
    total_ordered_spendings_key = spending.ordered_strat_spends
    total_spendings_key = spending.spend_strat_key

    # Keys used by ui.bidding_spendings.DailySpendingImportable
    daily_ordered_spendings_key = spending.ordered_strat_spends
    """
    Key used ordered_strat_spends indicates any change.

    It which will also count in daily spendings.
    """
    daily_spendings_key = spending.spend_strat_daily_key

    # Keys used by ui.bidding_spendings.Distributable
    period_spendings_key = spending.spend_strat_period_key
    period_budgets_key = spending.budget_strat_period_key

    @classmethod
    def slugify_name(cls, strategy):
        account = {'campaign__account': strategy.campaign.account}
        return unique_slugify(strategy, account)

    # instance methods

    def __unicode__(self):
        try:
            return '%s/%s' % (str(self.campaign), self.name)
        except Campaign.DoesNotExist:
            return self.name

    def get_adverts_quarters(self):
        for advert in self.advert_set.all():
            for day_minute, bid in advert.get_quarters():
                yield advert, day_minute, bid

    # instance propertes
    @property
    def public_id_parts(self):
        return self.campaign.account.id_random, self.campaign.id_random, self.id_random

    @property
    def full_name(self):
        ''' Full strategy name including parent campaign '''
        return '%s / %s' % (self.campaign.name, self.name)

    @property
    def bidding_periods_instances(self):
        adverts = self.ad.values_list('pk', flat=True)
        periods = BiddingPeriod.objects\
                               .filter(advertperiod__advert__pk__in=adverts)
        return periods

    @property
    def landing_sites_def(self):
        return [s for s in SiteRatio.all_with_percent(self.pk)]

    @landing_sites_def.setter
    @transaction.atomic
    def landing_sites_def(self, sites_ratios):
        """
        Sets landing_sites attributes based on url, and weight dicts in a
        sites_ratios list. If this list is empty, landing site is set based
        on one from parent campaign.

        .. note::
            If site does not exists for account assigened to campaign,
            it gets created

        :param list sites_ratios:
        [{url:... , weight:..., custom_variable: ...}, ...], where url is
        Site.url, and weight is weight SiteRatio.ratio
        """
        self.landing_sites.all().delete()

        # if no landing site is saved, take one from campaign
        if not sites_ratios:
            sites_ratios = [{
                'url': self.campaign.landing_site.url,
                'custom_variable': '',
                'weight': 1
            }]

        for site_info in sites_ratios:
            site, _ = Site.objects.get_or_create(
                url=site_info['url'],
                owner=self.campaign.account
            )

            ratio = site_info['weight'] or 1
            sr = SiteRatio(site=site, ratio=ratio,
                           custom_variable=site_info['custom_variable'])
            sr.save()
            self.landing_sites.add(sr)

    @property
    def bidding_periods(self):
        periods = []
        for p in self.biddingperiod_set.all():
            periods.append({'from': p.start.strftime(self.time_mask),
                            'to': p.end.strftime(self.time_mask)})
        return periods

    @bidding_periods.setter
    @transaction.atomic
    def bidding_periods(self, periods):
        """
        Args:
            sites_ratios([[int, int], [int, int], ...])
            - list of [Site.pk, ratio]
        """
        self.biddingperiod_set.all().delete()
        for p in periods:
            bp = BiddingPeriod(start=p['from'], end=p['to'], strategy=self)
            bp.save()
            self.biddingperiod_set.add(bp)

    def _bidding_periods_nonzero(self):
        '''
        Get list of periods which have non zero bid in at least one advert
        If strategy is not day parted, returns an empty list

        '''
        if not self.is_day_parted:
            return BiddingPeriod.objects.none()

        return BiddingPeriod.objects.filter(
            Q(strategy=self),
            Q(strategy__advert__custom_bid_CPM__gt=0,
                advertperiod__isnull=True) |
            Q(advertperiod__custom_bid_CPM__gt=0)
        ).distinct()

    def bidding_periods_ratio(self):
        '''
        Part of day strategy is active based on bidding periods

        :returns part of day strategy is active, like: 0.5
        :rtype float
        '''

        if not self.is_day_parted:
            return 1

        period_sum = timedelta()

        for period in self._bidding_periods_nonzero():
            period_sum += period.timedelta

        DAY_SECONDS = 60.0 * 60 * 24

        return period_sum.seconds / DAY_SECONDS

    @property
    def adverts_def(self):
        '''
        Output example:
            "adverts": [{
                'advert_id': int,
                "bid_custom": null,
                "bid_day_parting": [{
                    "bid_custom": "2",
                    "from": "13:25",
                    "to": "14:25"
                }],
                "bid_type": "day_parting",
                "custom_variable": "?test=4",
                "creative_id": 1,
                "creative_name": "PlaceKitten wide"
                "creative_path": "/media/creatives/sVKhi4loKw.jpeg",
                "creative_type": "Image",
                "creative_destination": "facebook_sidebar",
                "creative_fb_title": "Title", // if destination is facebook_*
                "creative_fb_body": "Body", // if destination is facebook_*
                "creative_fb_brand_page_access": "confirmed", // if destination is fb_newsfeed
                "is_deleted": false,
                "landing_page": 2,
                "name": "onet.pl",
                'state': {
                   'audited': False,
                   'campaign_finished': True,
                   'campaign_has_budget': False,
                   'campaign_in_progress': False,
                   'campaign_scheduled': False,
                   'pending': False,
                   'rejected': True,
                   'strategy_has_budget': False
                }
            }],
        '''
        adverts = []
        for ad in self.advert_set.filter(is_deleted=False):
            landing_site_url = ''
            bidding_periods = []

            for bp in ad.advertperiod_set.all():
                bidding_periods.append({
                    'from': bp.period.start.strftime(self.time_mask),
                    'to': bp.period.end.strftime(self.time_mask),
                    'bid_custom': bp.custom_bid_CPM,
                })

            # to show defined period in form when there are no
            # advert periods given for this specific creative
            if not bidding_periods:
                for bp in self.biddingperiod_set.all():
                    bidding_periods.append({
                        'from': bp.start.strftime(self.time_mask),
                        'to': bp.end.strftime(self.time_mask),
                        'bid_custom': '0.00',
                    })

            if ad.landing_site:
                landing_site_url = ad.landing_site.url

            ad_info = {
                'advert_id': ad.id,
                'is_deleted': ad.creative.is_deleted,
                'creative_id': ad.creative.id,
                'creative_name': ad.creative.name,
                'creative_path': ad.creative.api_data,
                'creative_type': ad.creative.type,
                'creative_destination': ad.creative.get_destination_display(),
                'landing_page_url': landing_site_url,
                "js_code": ad.js_code,
                'custom_pixel': ad.custom_pixel,
                'custom_variable': ad.custom_variable,
                'bid_type': ad.status,
                'bid_custom': None if ad.is_default else ad.custom_bid_CPM,
                'bid_day_parting': bidding_periods,
                'state': ad.state.to_dict()
            }

            if ad.creative.is_facebook_destination():
                ad_info.update({
                    'creative_fb_title': ad.creative.title,
                    'creative_fb_body': ad.creative.body,
                })

            if ad.creative.is_facebook_destination(verify_is_newsfeed=True):
                ad_info.update({
                    'creative_fb_brand_page_access': ad.creative.brand.appnexus_access_status
                })

            adverts.append(ad_info)

        return adverts

    @adverts_def.setter
    @transaction.atomic
    def adverts_def(self, adverts):
        '''
        Input example:
            "adverts": [{
                "advert_id": int
                "bid_custom": null,
                "bid_day_parting": [{
                    "bid_custom": "2",
                    "from": "13:25",
                    "to": "14:25"
                }],
                "bid_type": "day_parting",
                "custom_variable": "?test=4",
                "creative_id": 1,
                "creative_name": "PlaceKitten wide"
                "creative_path": "/media/creatives/sVKhi4loKw.jpeg",
                "creative_type": "Image",
                "landing_page_url": "http://www.onet.pl",
                "js_code": "<script>...</script>",
                "name": "onet.pl",
            }],
        '''

        # safely delete adverts
        adverts_to_delete = self.advert_set.filter(
            is_deleted=False
        ).exclude(
            id__in=[a['advert_id'] for a in adverts if 'advert_id' in a]
        ).all()

        for ad in adverts_to_delete:
            ad.delete()

        for a in adverts:
            if int(a['creative_id']):
                creative = Creative.objects.get(pk=a['creative_id'])
            else:
                creative = creative_factory(
                    a['creative_type'],
                    owner=self.campaign.account,
                    name=a['creative_name'],
                    api_data=a['creative_path']
                )
                creative.save()

            if a['landing_page_url']:
                site, _ = Site.objects.get_or_create(
                    url=a['landing_page_url'],
                    owner=self.campaign.account
                )
            else:
                site = None

            if int(a['advert_id']):
                advert = Advert.objects.get(pk=a['advert_id'])
            else:
                advert = Advert()

            advert.strategy = self
            advert.creative = creative
            advert.landing_site = site
            advert.custom_variable = a['custom_variable']
            advert.js_code = a['js_code']
            advert.custom_pixel = a['custom_pixel']

            if a['bid_type'] == advert.Status.custom:
                advert.custom_bid_CPM_def = a['bid_custom']
                advert.is_default = False
            else:
                advert.custom_bid_CPM_def = None

            advert.save()

            if a['bid_type'] != advert.Status.custom_parting:
                continue

            for dp in a['bid_day_parting']:
                bidding_period = BiddingPeriod.objects.get(
                    strategy=self,
                    start=datetime.strptime(dp['from'], '%H:%M').time(),
                    end=datetime.strptime(dp['to'], '%H:%M').time()
                )

                creative_period = AdvertPeriod(
                    advert=advert,
                    period=bidding_period,
                    custom_bid_CPM=Decimal(
                        dp.get('bid_custom', self.budget_bid_CPM)
                    ),
                )
                creative_period.save()

    @property
    def search_fields_def(self):
        '''
        Output example:
            "device_include": [{
                "id": 4,
                "name": "Sony Xperia Z"
            }],
            "location_exclude": [{
                "id": 89,
                "name": "New York (state)",
                "type": "region"
            }]
        '''
        categories = (
            dimensions.g_location,
            dimensions.g_os,
            dimensions.carrier,
            dimensions.age_group,
            dimensions.gender,
            dimensions.g_device,
        )
        out = defaultdict(list)
        for category in categories:
            for item in self.targeting_values.filter(category=category):
                out['%s_include' % category].append({
                    'id': item.id,
                    'name': item.display_label,
                })
            for item in self.targeting_values_exclude\
                    .filter(category=category):
                out['%s_exclude' % category].append({
                    'id': item.id,
                    'name': item.display_label,
                })
        return out

    @search_fields_def.setter
    def search_fields_def(self, args):
        '''
        Input example:
            "device_include": [{
                "id": 4,
                "name": "Sony Xperia Z"
            }],
            "device_exclude": [{
                "id": 89,
                "name": "HTC Desire S"
            }]
        '''
        with transaction.atomic():
            self.targeting_values.clear()
            self.targeting_values_exclude.clear()

            for key, value in args.items():

                if (self.type == self.SITE) and key.startswith(dimensions.g_device):
                    continue

                if key.endswith('_include'):
                    field = self.targeting_values
                else:
                    field = self.targeting_values_exclude

                values_pks = map(itemgetter('id'), value)
                field.add(*values_pks)

    def common_checkbox_propery_def(self, model_fields, keys):
        '''
        Common part of each checkbox related property.

        :param model_fields: tuple with include and exclude fields
        :param keys: tuple with include and exclude keys used by frontend

        :rtype: dict
        :returns: dictionary with id and name for each element
        '''
        out = defaultdict(list)
        for model, key in zip(model_fields, keys):
            for item in model.all():
                out[key].append(
                    {
                        "id": item.id,
                        "name": item.name,
                    }
                )
        return out

    @transaction.atomic
    def common_checkbox_propery_setter(self, include_field, exclude_field,
                                       include_key, segment):
        '''
        Setter for checkbox-based fields.

        :param obj include_field: field containing included items
        :param obj exclude_field: field containing excluded items
        :param str include_key: frontend key containing included items
        :param dict segment: dictionary with included and excluded items

        .. note::
            segment example:
                "proximic_page_quality_include": [{
                    "id": 1,
                    "name": "High",
                }],
                "proximic_page_quality_exclude": [{
                    "id": 2,
                    "name": "Medium",
                }]
        '''

        include_field.clear()
        exclude_field.clear()

        for key, value in segment.items():

            if key == include_key:
                field = include_field
            else:
                field = exclude_field

            values_pks = map(itemgetter('id'), value)
            field.add(*values_pks)

    @property
    def proximic_maturity_rating_fields_def(self):
        """
        :returns: defaultdict with Proximic maturity rating (include/exclude)
        :rtype: defaultdict
        """
        model_fields = (
            self.segment_proximic_maturity_rating,
            self.segment_proximic_maturity_rating_exclude
        )
        keys = (
            'proximic_maturity_rating_include',
            'proximic_maturity_rating_exclude',
        )

        return self.common_checkbox_propery_def(model_fields, keys)

    @proximic_maturity_rating_fields_def.setter
    def proximic_maturity_rating_fields_def(self, segment):
        """
        Saving checkbox-related fields (Proximic maturity rating)
        """
        self.common_checkbox_propery_setter(
            self.segment_proximic_maturity_rating,
            self.segment_proximic_maturity_rating_exclude,
            'proximic_maturity_rating_include',
            segment
        )

    @property
    def proximic_safety_level_fields_def(self):
        """
        :returns: defaultdict with Proximic safety level (include/exclude)
        :rtype: defaultdict
        """
        model_fields = (
            self.segment_proximic_safety_level,
            self.segment_proximic_safety_level_exclude
        )
        keys = (
            'proximic_safety_level_include',
            'proximic_safety_level_exclude',
        )

        return self.common_checkbox_propery_def(model_fields, keys)

    @proximic_safety_level_fields_def.setter
    def proximic_safety_level_fields_def(self, segment):
        """
        Saving checkbox-related fields (Proximic safety level)
        """
        self.common_checkbox_propery_setter(
            self.segment_proximic_safety_level,
            self.segment_proximic_safety_level_exclude,
            'proximic_safety_level_include',
            segment
        )

    @property
    def proximic_language_fields_def(self):
        """
        :returns: defaultdict with Proximic languages (include/exclude)
        :rtype: defaultdict
        """
        model_fields = (
            self.segment_proximic_page_language,
            self.segment_proximic_page_language_exclude
        )
        keys = (
            'proximic_language_include',
            'proximic_language_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @proximic_language_fields_def.setter
    def proximic_language_fields_def(self, segment):
        """
        Saving checkbox-related fields (Proximic language)
        """
        self.common_checkbox_propery_setter(
            self.segment_proximic_page_language,
            self.segment_proximic_page_language_exclude,
            'proximic_language_include',
            segment
        )

    @property
    def proximic_page_quality_fields_def(self):
        """
        :returns: defaultdict with Proximic page quality (include/exclude)
        :rtype: defaultdict
        """
        model_fields = (
            self.segment_proximic_page_quality,
            self.segment_proximic_page_quality_exclude
        )
        keys = (
            'proximic_page_quality_include',
            'proximic_page_quality_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @proximic_page_quality_fields_def.setter
    def proximic_page_quality_fields_def(self, segment):
        """
        Saving checkbox-related fields (Proximic page quality)
        """
        self.common_checkbox_propery_setter(
            self.segment_proximic_page_quality,
            self.segment_proximic_page_quality_exclude,
            'proximic_page_quality_include',
            segment
        )

    @property
    def proximic_page_noticeability_fields_def(self):
        """
        :returns: defaultdict with Proximic page noticeability
            (include/exclude)
        :rtype: defaultdict
        """
        model_fields = (
            self.segment_proximic_page_noticeability,
            self.segment_proximic_page_noticeability_exclude
        )
        keys = (
            'proximic_page_noticeability_include',
            'proximic_page_noticeability_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @proximic_page_noticeability_fields_def.setter
    def proximic_page_noticeability_fields_def(self, segment):
        """
        Saving checkbox-related fields (Proximic page noticeability)
        """
        self.common_checkbox_propery_setter(
            self.segment_proximic_page_noticeability,
            self.segment_proximic_page_noticeability_exclude,
            'proximic_page_noticeability_include',
            segment
        )

    @property
    def proximic_page_placement_fields_def(self):
        """
        :returns: defaultdict with Proximic above the fold (include/exclude)
        :rtype: defaultdict
        """
        model_fields = (
            self.segment_proximic_page_placement,
            self.segment_proximic_page_placement_exclude
        )
        keys = (
            'proximic_page_placement_include',
            'proximic_page_placement_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @proximic_page_placement_fields_def.setter
    def proximic_page_placement_fields_def(self, segment):
        """
        Saving checkbox-related fields (Proximic above the fold)
        """
        self.common_checkbox_propery_setter(
            self.segment_proximic_page_placement,
            self.segment_proximic_page_placement_exclude,
            'proximic_page_placement_include',
            segment
        )

    @property
    def proximic_contextual_fields_def(self):
        """
        :returns: defaultdict with Proximic contextual (include/exclude)
        :rtype: defaultdict
        """
        model_fields = (
            self.segment_proximic_contextual,
            self.segment_proximic_contextual_exclude
        )
        keys = (
            'proximic_contextual_include',
            'proximic_contextual_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @proximic_contextual_fields_def.setter
    def proximic_contextual_fields_def(self, segment):
        """
        Saving checkbox-related fields (Proximic contextual)
        """
        self.common_checkbox_propery_setter(
            self.segment_proximic_contextual,
            self.segment_proximic_contextual_exclude,
            'proximic_contextual_include',
            segment
        )

    @property
    def content_categories_def(self):
        """
        :returns: defaultdict with content categories (include/exclude)
        :rtype: defaultdict
        """

        model_fields = (
            self.content_category_values,
            self.content_category_values_exclude
        )
        keys = (
            'category_include',
            'category_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @content_categories_def.setter
    def content_categories_def(self, segment):
        """
        Saving checkbox-related fields (content categories)
        """
        self.common_checkbox_propery_setter(
            self.content_category_values,
            self.content_category_values_exclude,
            'category_include',
            segment
        )

    @property
    def peer_content_categories_def(self):
        """
        :returns: defaultdict with peer39 content categories (include/exclude)
        :rtype: defaultdict
        """
        model_fields = (
            self.segment_peer_contextual,
            self.segment_peer_contextual_exclude
        )
        keys = (
            'peer_contextual_include',
            'peer_contextual_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @peer_content_categories_def.setter
    def peer_content_categories_def(self, category):
        self.common_checkbox_propery_setter(
            self.segment_peer_contextual,
            self.segment_peer_contextual_exclude,
            'peer_contextual_include',
            category
        )

    @property
    def peer_page_quality_def(self):
        """
        :returns: defaultdict with peer39 page quality (include/exclude)
        :rtype: defaultdict
        """
        model_fields = (
            self.segment_peer_page_quality,
            self.segment_peer_page_quality_exclude
        )
        keys = (
            'peer_page_quality_include',
            'peer_page_quality_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @peer_page_quality_def.setter
    def peer_page_quality_def(self, category):
        self.common_checkbox_propery_setter(
            self.segment_peer_page_quality,
            self.segment_peer_page_quality_exclude,
            'peer_page_quality_include',
            category
        )

    @property
    def peer_language_def(self):
        model_fields = (
            self.segment_peer_page_language,
            self.segment_peer_page_language_exclude
        )
        keys = (
            'peer_page_language_include',
            'peer_page_language_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @peer_language_def.setter
    def peer_language_def(self, segment):
        self.common_checkbox_propery_setter(
            self.segment_peer_page_language,
            self.segment_peer_page_language_exclude,
            'peer_page_language_include',
            segment
        )

    @property
    def peer_brand_protection_def(self):
        model_fields = (
            self.segment_peer_brand_protection,
            self.segment_peer_brand_protection_exclude
        )
        keys = (
            'peer_brand_protection_include',
            'peer_brand_protection_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @peer_brand_protection_def.setter
    def peer_brand_protection_def(self, segment):
        self.common_checkbox_propery_setter(
            self.segment_peer_brand_protection,
            self.segment_peer_brand_protection_exclude,
            'peer_brand_protection_include',
            segment
        )

    @property
    def lotame_demographic(self):
        model_fields = (
            self.segment_lotame_demographic,
            self.segment_lotame_demographic_exclude
        )
        keys = (
            'lotame_demographic_include',
            'lotame_demographic_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @lotame_demographic.setter
    def lotame_demographic(self, segment):
        self.common_checkbox_propery_setter(
            self.segment_lotame_demographic,
            self.segment_lotame_demographic_exclude,
            'lotame_demographic_include',
            segment
        )

    @property
    def lotame_advanced_demographic(self):
        model_fields = (
            self.segment_lotame_advanced_demographic,
            self.segment_lotame_advanced_demographic_exclude
        )
        keys = (
            'lotame_advanced_demographic_include',
            'lotame_advanced_demographic_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @lotame_advanced_demographic.setter
    def lotame_advanced_demographic(self, segment):
        self.common_checkbox_propery_setter(
            self.segment_lotame_advanced_demographic,
            self.segment_lotame_advanced_demographic_exclude,
            'lotame_advanced_demographic_include',
            segment
        )

    @property
    def lotame_behavioral_interest(self):
        model_fields = (
            self.segment_lotame_behavioral_interest,
            self.segment_lotame_behavioral_interest_exclude
        )
        keys = (
            'lotame_behavioral_interest_include',
            'lotame_behavioral_interest_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @lotame_behavioral_interest.setter
    def lotame_behavioral_interest(self, segment):
        self.common_checkbox_propery_setter(
            self.segment_lotame_behavioral_interest,
            self.segment_lotame_behavioral_interest_exclude,
            'lotame_behavioral_interest_include',
            segment
        )

    @property
    def lotame_influencers(self):
        model_fields = (
            self.segment_lotame_influencers,
            self.segment_lotame_influencers_exclude
        )
        keys = (
            'lotame_influencers_include',
            'lotame_influencers_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @lotame_influencers.setter
    def lotame_influencers(self, segment):
        self.common_checkbox_propery_setter(
            self.segment_lotame_influencers,
            self.segment_lotame_influencers_exclude,
            'lotame_influencers_include',
            segment
        )

    @property
    def lotame_offline(self):
        model_fields = (
            self.segment_lotame_offline,
            self.segment_lotame_offline_exclude
        )
        keys = (
            'lotame_offline_include',
            'lotame_offline_exclude',
        )
        return self.common_checkbox_propery_def(model_fields, keys)

    @lotame_offline.setter
    def lotame_offline(self, segment):
        self.common_checkbox_propery_setter(
            self.segment_lotame_offline,
            self.segment_lotame_offline_exclude,
            'lotame_offline_include',
            segment
        )

    @property
    def landing_sites_ratios(self):
        sites = list(self.landing_sites.values('ratio', 'site__url').all())
        ratio_sum = sum(s['ratio'] for s in sites)

        return [(str(s['site__url']), float(s['ratio']) / ratio_sum) for s in sites]

    def get_audience_ids(self, exclude=False):
        '''
        Returns audiences ids list for given strategy

        :param bool exclude: wheter to list include or exclude audiences

        :returns: list of audiences
        :rtype: list
        '''
        if exclude:
            query = self.audiences_exclude
        else:
            query = self.audiences
        for audience in query.values_list('id_random'):
            yield audience[0]

    def has_ip_audience(self):
        """
        Returns true, if any audience assigned is 'IP related'.

        :rtype: bool
        """
        return self.audiences.filter(is_ip=True).exists() or self.audiences_exclude.filter(is_ip=True).exists()

    def is_interest_based(self):
        """
        Returns True if strategy uses interest-based targeting defined by Network Advertising Initiative
        http://www.networkadvertising.org/

        This flag is set to True if strategy of an advert uses any of these targeting categories:
        * any audiences including G4 App and IP audiences, both include or exclude
        * behavioural segments - all Lotame segments at the moment
        * gender
        * age group

        :rtype: bool
        """
        behavioral_categories = [dimensions.gender, dimensions.age_group]
        return any(relation.exists() for relation in (
            self.targeting_values.filter(category__in=behavioral_categories),
            self.targeting_values_exclude.filter(category__in=behavioral_categories),
            self.audiences,
            self.audiences_exclude,
            self.segment_lotame_demographic,
            self.segment_lotame_demographic_exclude,
            self.segment_lotame_advanced_demographic,
            self.segment_lotame_advanced_demographic_exclude,
            self.segment_lotame_behavioral_interest,
            self.segment_lotame_behavioral_interest_exclude,
            self.segment_lotame_influencers,
            self.segment_lotame_influencers_exclude,
            self.segment_lotame_offline,
            self.segment_lotame_offline_exclude,
        ))

    def copy(self, campaign=None):
        '''
        Cloning strategy

        TIP: self.copy() makes self a cloned object
        '''

        sufix = ''
        if campaign is None:
            campaign = self.campaign
            sufix = ' (copy)'

        # old many-to-many values
        m2m_fields = {}
        for field in Strategy._meta.local_many_to_many:
            m2m_fields[field.name] = getattr(self, field.name).all()

        old_landing_sites_def = self.landing_sites_def
        old_bidding_periods = self.bidding_periods
        old_adverts_def = self.adverts_def
        old_search_fields_def = self.search_fields_def
        old_content_categories_def = self.content_categories_def
        old_proximic_maturity_rating_fields_def = self.proximic_maturity_rating_fields_def  # noqa

        i = 1
        new_name = self.name + sufix
        while Strategy.objects.filter(name=new_name, campaign=campaign)\
                .exclude(id=self.id).exists():
            new_name = self.name + ' (copy-{0})'.format(i)
            i += 1
        self.name = new_name

        self.pk = None
        self.id = None
        self.campaign = campaign
        self.created = datetime.utcnow()
        self.id_random = public_id_randomizer()
        self.save()

        for field in Strategy._meta.local_many_to_many:
            setattr(self, field.name, m2m_fields[field.name])

        self.landing_sites_def = old_landing_sites_def
        self.bidding_periods = old_bidding_periods
        self.adverts_def = old_adverts_def
        self.search_fields_def = old_search_fields_def
        self.content_categories_def = old_content_categories_def
        self.proximic_maturity_rating_fields_def = old_proximic_maturity_rating_fields_def  # noqa

    def get_appnexus_locations(self):
        '''
        Method for getting lists with Appnexus locations.

        :rtype: tuple
        :return: AppNexus location names
        '''

        included_locations = list(self.targeting_values.filter(
            category=dimensions.g_location,
            exchange=EXCHANGES.appnexus,
            representant__isnull=True
        ))

        representants_from_other_exchanges = self.targeting_values.filter(
            category=dimensions.g_location,
            representant__isnull=True
        ).exclude(exchange=EXCHANGES.appnexus)

        # translating to AppNexus (if there is any translation)
        for representant in representants_from_other_exchanges:
            appnexus_value = representant.untranslate_to(EXCHANGES.appnexus)
            if appnexus_value:
                included_locations += appnexus_value

        def get_country(target):
            """Extract country from location target."""
            return target.value_dict.get(dimensions.country)

        def get_region(target):
            """Extract country and region from location target."""
            region = target.value_dict.get(dimensions.region)
            if region:
                return ':'.join([get_country(target), region])

        return (
            set(map(get_country, included_locations)),
            set(map(get_region, included_locations)),
        )

    def get_appnexus_segments(self):
        '''
        Getting list of included segments from targeting.

        :rtype: list
        :return: AppNexus segment ids
        '''

        strategy_segments = []
        for segment in self.segments:
            strategy_segments += getattr(self, segment).all().values_list('appnexus_id', flat=True)
        return strategy_segments


@receiver(pre_save, sender=Strategy, weak=False)
def strategy_pre_save(sender, instance, **kwargs):
    strategy = instance

    # update slug
    strategy.slug = Strategy.slugify_name(strategy)

    # Increasing total budget to equal spent budget
    # should only happen if user changes budget in UI
    if strategy.has_changed('budget_spent') or strategy.has_changed('budget_daily_spent'):
        # Total budget shouldn't change if new spending values are imported
        return

    # strategy total budget can't be less than spent budget
    if strategy.budget_total < strategy.budget_spent:
        strategy.budget_total = strategy.budget_spent

    # strategy total budget can't be greater than campaign total budget
    if strategy.budget_total > strategy.campaign.budget_total:
        strategy.budget_total = strategy.campaign.budget_total


@receiver(post_save, sender=Strategy, weak=False)
def strategy_post_save(sender, instance, created, **kwargs):

    strategy = instance

    if created:
        Event.objects.create_strategy_created(strategy)


class BiddingPeriodManager(m.Manager):

    def representants(self):
        return self.all()


class BiddingPeriod(TimeStampedModel):

    # no timezone in start and end fields. Their timezone is based on strategy
    # timezone (no such field yet) or account timezone
    start = m.TimeField()  # no timezone!
    end = m.TimeField()  # no timezone!

    strategy = m.ForeignKey(Strategy)

    objects = BiddingPeriodManager()

    class Meta:
        ordering = ["start"]

    def __unicode__(self):
        return '%s - %s' % (self.start, self.end)

    def get_day_quarters(self):
        tz = self.strategy.campaign.account.timezone
        return get_period_quarters(self.start, self.end, tz)

    @property
    def timedelta(self):
        '''
        :returns timedelta between end and start
        '''
        return timedelta(
            hours=self.end.hour - self.start.hour,
            minutes=self.end.minute - self.start.minute
        )


@receiver(pre_save, sender=BiddingPeriod, weak=False)
def biddingperiod_presave(sender, instance, **kwargs):
    self = instance

    # validate
    if self.start > self.end:
        raise ValidationError("start can't be later than end")

    if is_timezoned(self.start):
        raise ValidationError("start can't have timezone")

    if is_timezoned(self.end):
        raise ValidationError("end can't have timezone")

    q = BiddingPeriod.objects.filter(
        strategy=self.strategy,
        start__lt=self.end,
        end__gt=self.start
    )
    if self.id:
        q = q.exclude(id=self.id)
    if q.exists():
        raise ValidationError(
            "current time range overlaps other bidding with same strategy"
        )


class AdvertType(object):

    """ HTML image banner """
    IMAGE = 'Image'

    """ Javascript """
    JAVASCRIPT = 'JavaScript'

    """ FLASH banner, may contain Javascript """
    FLASH = 'Flash'

    VIDEO = 'Video'


class Advert(KanaryDirtyFieldsMixin, CacheMapped, RandomId):

    def __init__(self, *args, **kwargs):
        from .states import AdvertState

        super(Advert, self).__init__(*args, **kwargs)
        self.state = AdvertState(self)

    strategy = m.ForeignKey(Strategy)
    creative = m.ForeignKey(Creative, on_delete=m.PROTECT)
    # custom Site:
    landing_site = m.ForeignKey(Site, on_delete=m.PROTECT, null=True)
    # custom tracking JS:
    js_code = m.TextField(default="")
    # pixel tracking:
    custom_pixel = LongURLField(null=True)

    custom_variable = m.CharField(max_length=255, null=True, blank=True)

    custom_bid_CPM = CPMDecimalField(null=True)
    is_default = m.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    class Status:
        strategy_default = 'default'
        custom = 'custom'
        custom_parting = 'day_parting'

    @property
    def full_name(self):
        ''' Object name including creative, strategy and campaign '''
        return '{campaign} / {strategy} / {creative}'.format(
            campaign=self.strategy.campaign.name,
            strategy=self.strategy.name,
            creative=self.creative.name
        )

    @property
    def has_periods(self):
        return self.advertperiod_set.exists()

    @property
    def public_id_parts(self):
        return (self.strategy.campaign.account.id_random, self.strategy.campaign.id_random,
                self.strategy.id_random, self.id_random)

    @property
    def status(self):
        if self.has_periods:
            return self.Status.custom_parting

        if self.is_default:
            return self.Status.strategy_default

        return self.Status.custom

    @property
    def type(self):
        """
        Advert type based on creative type and advert settings.

        :returns: One of AdvertType values
        :rtype: str
        """
        if self.creative.type == 'Image' and self.js_code:
            return AdvertType.JAVASCRIPT
        elif self.creative.type == 'Image':
            return AdvertType.IMAGE
        elif self.creative.type == 'Flash':
            return AdvertType.FLASH
        elif self.creative.type == 'Video':
            return AdvertType.VIDEO

    @property
    def width(self):
        return self.get_targeting_ad_size(self.creative.width)

    @property
    def height(self):
        return self.get_targeting_ad_size(self.creative.height)

    @property
    def duration(self):
        """
        Map creative duration to AppNexus video duration presets.
        """
        if self.type == AdvertType.VIDEO:
            if self.creative.duration == 15:
                return VideoDuration.VAST_15_SEC
            elif self.creative.duration == 30:
                return VideoDuration.VAST_30_SEC
            else:
                return VideoDuration.VAST_OTHER
        else:
            return None

    @property
    def landing_sites_ratios(self):
        if self.landing_site:
            return [(self.landing_site.url, 1)]

        return self.strategy.landing_sites_ratios

    def _set_custom_bid_CPM(self, bid):
        if bid is None:
            bid = self.strategy.budget_bid_CPM
            self.is_default = True
        self.custom_bid_CPM = Decimal(bid or 0)

    def _get_custom_bid_CPM(self):
        return self.custom_bid_CPM

    custom_bid_CPM_def = property(_get_custom_bid_CPM, _set_custom_bid_CPM)

    # methods

    def get_quarters(self):
        '''
        Returns tuples (iter) with serialized quarter and bid assigned
        for this quarter:
            [<serialized quarter name>, <bid value>]
            ['1630', None],
            ['1645', 10], ...
        '''
        timezone = self.strategy.campaign.account.timezone

        advert_bid = self.custom_bid_CPM
        if advert_bid is None:
            advert_bid = self.strategy.budget_bid_CPM

        if self.strategy.is_automatically_bidded:
            advert_bid = None

        if not self.has_periods:
            for quarter in get_period_quarters(tz=timezone):
                yield quarter, advert_bid
            return

        # if advert has periods yields proper bids_CPM values
        advert_periods = self.advertperiod_set \
            .only('period__start', 'period__end', 'custom_bid_CPM')

        for adperiod in advert_periods.all():
            start = adperiod.period.start
            end = adperiod.period.end
            for quarter in get_period_quarters(start, end, timezone):
                yield quarter, adperiod.custom_bid_CPM or advert_bid

    def get_targeting_ad_size(self, size):
        """
        Appnexus requires setting 1x1 pixel size in profile if we want to receive VAST ads.
        https://wiki.appnexus.com/display/adnexusdocumentation/Expandables+and+Rich+Media?src=search

        :return: real creative size (width or height) or 1 in case of video
        :rtype: int
        """
        if self.creative.type == AdvertType.VIDEO:
            return 1
        else:
            return size


@receiver(pre_save, sender=Advert)
def advert_pre_save(sender, instance, **kwargs):
    # advert cannot have both custom pixel and custom js code tracker
    if instance.custom_pixel and instance.js_code:
        raise ValidationError('Advert cannot contain both custom pixel and js code trackers.')


@receiver(post_save, sender=Advert, weak=False)
def advert_post_save(sender, instance, **kwargs):
    advert = instance
    creative = advert.creative
    # Update creative landing_page
    if creative.appnexus_status not in ['a', 'p'] or creative.is_facebook_destination():
        if not advert.landing_site:
            # Arbitrally choose a landing site for audit.
            landing_site = advert.strategy.landing_sites.all()[0].site
            creative.landing_site_url = landing_site.url
        elif creative.landing_site_url != advert.landing_site.url:
            creative.landing_site_url = advert.landing_site.url

        creative.save()


class AdvertPeriod(m.Model):

    advert = m.ForeignKey(Advert)
    period = m.ForeignKey(BiddingPeriod)
    custom_bid_CPM = CPMDecimalField()
