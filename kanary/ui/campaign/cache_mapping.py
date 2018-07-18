'''
After every change in mapping we should add new migration to set
cache_is_dirty == False in order to make models re-loaded into cache.
'''
import cPickle
from functools import partial
from collections import OrderedDict, defaultdict
from urlparse import urlparse, urljoin
from random import choice

from adserving.types import Decimal
from adserving.adserver import constants
from adserving.bidder.targeting.targetad import TargetAd, TargetDimension
from adserving.bidder.targeting.constants import DATA_PROVIDERS, LOTAME_SEGMENT_APPNEXUS_ID, LOTAME

from etc import redis_keys, dimensions
from etc.config import settings
from etc.constants import (
    TARGETING_CHANNEL,
    CDN_RESOURCE_KEY_MASK,
    TARGETING_CLEAN_CHANNEL,
    HIDDEN_COMMISSION,
    OPTIMIZER_CHANNEL,
    OPTIMIZER_CLEAN_CHANNEL,
)

from ui.cache.base_models import CacheMap
from ui.campaign.tasks import appnexus_update_profile


CDN = urljoin(settings.globals_media_cdn_url, CDN_RESOURCE_KEY_MASK)


class AdvertCacheMap(CacheMap):

    """
    .. note::
        We add values into :class:`ContentCategory` and
        :class:`ContentCategoryValue` during migrations, so we
        don't have to observe them. But we must observe their relation.
    """

    connections = (
        'adserver', 'targeting',
    )
    publishing_connections = {
        'targeting': (TARGETING_CHANNEL, TARGETING_CLEAN_CHANNEL),
    }
    key_obj = redis_keys.ads

    observes = {
        'campaign.Strategy': {
            'relation': lambda strategy: strategy.advert_set.all(),
            'fields': ['type', 'is_paused', 'is_deleted',
                       'budget_total', 'budget_daily', 'budget_bid_CPM',
                       'is_day_parted', 'publisherset_id']
        },
        'campaign.Campaign': {
            'relation': lambda campaign: campaign.adverts,
            'fields': ['is_paused', 'is_deleted', 'budget_total', 'cap_total',
                       'cap_strategy', 'cap_creative', 'cap_total_period',
                       'cap_strategy_period', 'cap_creative_period',
                       'cap_campaign_selected', 'cap_strategy_selected',
                       'cap_creative_selected']
        },
        'campaign.Advert': {
            'relation': lambda advert: advert,
            'fields': ['is_deleted', 'custom_bid_CPM', 'is_default', 'js_code',
                       'custom_pixel', 'landing_site_id']
        },
        'campaign.SiteRatio': {
            'relation': lambda siter: siter.adverts.all(),
        },
        'campaign.Site': {
            'relation': lambda site: site.adverts.all(),
        },
        'campaign.BiddingPeriod': {
            'relation': lambda p: p.strategy.advert_set.all(),
        },
        'campaign.AdvertPeriod': {
            'relation': lambda adperiod: adperiod.advert,
        },
        'storage.Creative': {
            'relation': lambda creative: creative.advert_set.all(),
        },
        'storage.CreativeImage': {
            'relation': lambda creative: creative.advert_set.all(),
        },
        'storage.CreativeFlash': {
            'relation': lambda creative: creative.advert_set.all(),
        },
        'storage.CreativeVideo': {
            'relation': lambda creative: creative.advert_set.all(),
        },
        'storage.Audience': {
            'relation': lambda audience: audience.adverts,
            'fields': ['is_ip']
        },
        'targeting.TargetValue': {
            'relation': lambda target: target.adverts,
        },
        'publishers.PublisherSet': {
            'relation': lambda publisherset: publisherset.adverts,
        },
        'account.Account': {
            'relation': lambda account: account.adverts,
            'fields': ['commission', 'audit_fees']
        },
        'account.Payment': {
            'relation': lambda payment: payment.account.adverts,
        }
    }

    observes_through = {
        'campaign.Strategy.targeting_values': 'strategy',
        'publishers.PublisherSet.target_values': 'strategy__publisherset',
        'campaign.Strategy.audiences': 'strategy',
        'campaign.Strategy.audiences_exclude': 'strategy',
        'campaign.Strategy.content_category_values': 'strategy',
        'campaign.Strategy.content_category_values_exclude': 'strategy',

        'campaign.Strategy.segment_proximic_maturity_rating': 'strategy',
        'campaign.Strategy.segment_proximic_maturity_rating_exclude': 'strategy',
        'campaign.Strategy.segment_proximic_safety_level': 'strategy',
        'campaign.Strategy.segment_proximic_safety_level_exclude': 'strategy',
        'campaign.Strategy.segment_proximic_page_quality': 'strategy',
        'campaign.Strategy.segment_proximic_page_quality_exclude': 'strategy',
        'campaign.Strategy.segment_proximic_page_noticeability': 'strategy',
        'campaign.Strategy.segment_proximic_page_noticeability_exclude': 'strategy',
        'campaign.Strategy.segment_proximic_page_placement': 'strategy',
        'campaign.Strategy.segment_proximic_page_placement_exclude': 'strategy',
        'campaign.Strategy.segment_proximic_contextual': 'strategy',
        'campaign.Strategy.segment_proximic_contextual_exclude': 'strategy',
        'campaign.Strategy.segment_proximic_page_language': 'strategy',
        'campaign.Strategy.segment_proximic_page_language_exclude': 'strategy',

        'campaign.Strategy.segment_peer_page_quality': 'strategy',
        'campaign.Strategy.segment_peer_page_quality_exclude': 'strategy',
        'campaign.Strategy.segment_peer_contextual': 'strategy',
        'campaign.Strategy.segment_peer_contextual_exclude': 'strategy',
        'campaign.Strategy.segment_peer_brand_protection': 'strategy',
        'campaign.Strategy.segment_peer_brand_protection_exclude': 'strategy',
        'campaign.Strategy.segment_peer_page_language': 'strategy',
        'campaign.Strategy.segment_peer_page_language_exclude': 'strategy',

        'campaign.Strategy.segment_lotame_demographic': 'strategy',
        'campaign.Strategy.segment_lotame_demographic_exclude': 'strategy',
        'campaign.Strategy.segment_lotame_advanced_demographic': 'strategy',
        'campaign.Strategy.segment_lotame_advanced_demographic_exclude': 'strategy',
        'campaign.Strategy.segment_lotame_behavioral_interest': 'strategy',
        'campaign.Strategy.segment_lotame_behavioral_interest_exclude': 'strategy',
        'campaign.Strategy.segment_lotame_influencers': 'strategy',
        'campaign.Strategy.segment_lotame_influencers_exclude': 'strategy',
        'campaign.Strategy.segment_lotame_offline': 'strategy',
        'campaign.Strategy.segment_lotame_offline_exclude': 'strategy',
    }
    observes_date_fields = (
        'strategy__campaign__start_UTC',
        'strategy__campaign__end_UTC'
    )

    def mapped_adserver(self):

        adserver_mapping = self.advert.creative.cache_map.mapped()
        adserver_mapping['adid'] = str(self.advert.public_id)
        adserver_mapping['js_code'] = self.advert.js_code
        adserver_mapping['custom_pixel'] = self.advert.custom_pixel
        adserver_mapping['type'] = self.advert.type

        return adserver_mapping

    def mapped_targeting(self):
        """
        General TargetAd construction.

        :returns: TargetAd instance or nothing
        """

        if not self.advert.state.is_running:
            return None

        strategy = self.advert.strategy
        campaign = strategy.campaign

        capping = {}
        if campaign.cap_campaign_selected:
            capping['campaign'] = (campaign.cap_total,
                                   campaign.cap_total_period)
        if campaign.cap_strategy_selected:
            capping['strategy'] = (campaign.cap_strategy,
                                   campaign.cap_strategy_period)
        if campaign.cap_creative_selected:
            capping['ad'] = (campaign.cap_creative,
                             campaign.cap_creative_period)

        hidden_commission = Decimal(HIDDEN_COMMISSION) / 100

        # get bids and bids with hidden commission
        # hence, we don't need calculate it during bid response
        # see build_response method in bidders
        bids = {k: float(v) if v else 0 for k, v in self.advert.get_quarters()}
        bids_minus_commissions = {
            k: float(v - (v * hidden_commission))
            if v else 0 for k, v in self.advert.get_quarters()
        }

        segment_dimensions = {}

        for segment_field in self.advert.strategy.segments:
            segment_dimensions[segment_field.lstrip('segment_')] = TargetDimension(
                {
                    segment.appnexus_id for segment in getattr(self.advert.strategy, segment_field).all()
                },
                {
                    segment.appnexus_id for segment
                    in getattr(self.advert.strategy, segment_field + '_exclude').all()
                }
            )

        # When some strategy uses segments, it exclusively matches opportunities that have all those
        # segments given.
        # We pay only for won auctions.
        # That means we can pre-calculate the final data providers cost here because we already know
        # all segments that will always be used for this ad.

        # The dict must be ordered - keys order should reflect DATA_PROVIDERS_MACRO list elements.
        data_providers = OrderedDict.fromkeys(DATA_PROVIDERS, Decimal(0))
        lotame_prices = defaultdict(list)  # Price to appnexus ids mapping for lotame.

        for segment_field in self.advert.strategy.segments:
            include_manager = getattr(self.advert.strategy, segment_field)
            exclude_manager = getattr(self.advert.strategy, segment_field + '_exclude')

            for segment in include_manager.all() | exclude_manager.all():
                # Total cost of data per provider is always the cost of the most expensive segment.
                data_providers[segment.PROVIDER] = max(
                    segment.PRICE_CPM, data_providers[segment.PROVIDER])
                if segment.PROVIDER == LOTAME:
                    lotame_prices[segment.PRICE_CPM].append(segment.appnexus_id)

        # Select one of the Lotame segments matching the biggest price.
        # Now data_providers are same as strings in DATA_PROVIDERS_MACRO.
        if lotame_prices:
            max_lotame_price = max(lotame_prices.keys())
            data_providers[LOTAME_SEGMENT_APPNEXUS_ID] = choice(lotame_prices[max_lotame_price])
        else:
            data_providers[LOTAME_SEGMENT_APPNEXUS_ID] = None

        return TargetAd(
            id=self.advert.public_id,
            creative_id=self.advert.creative.public_id,
            appnexus_creative_id=self.advert.creative.appnexus_id,
            strategy_id=self.advert.strategy.public_id,
            campaign_id=self.advert.strategy.campaign.public_id,
            account_id=self.advert.creative.owner.public_id,
            # audiences
            audiences_include=self.advert.strategy.get_audience_ids(),
            audiences_exclude=self.advert.strategy.get_audience_ids(exclude=True),
            has_ip_audiences=self.advert.strategy.has_ip_audience(),
            capping=capping,
            # creative characteristics
            width=self.advert.width,
            height=self.advert.height,
            formats=self.advert.type,
            durations=self.advert.duration,
            # landing sites
            landing_sites=self.advert.landing_sites_ratios,
            # budgets
            strategy_budget=self.advert.strategy.budget_total,
            campaign_budget=self.advert.strategy.campaign.budget_total,
            daily_budget=self.advert.strategy.budget_daily,
            account_budget=self.advert.creative.owner.total_paid(),
            account_fees=self.advert.creative.owner.audit_fees,
            # commission
            commission=self.advert.creative.owner.commission,
            hidden_commission=HIDDEN_COMMISSION,
            # targeting
            inventory=self.advert.strategy.type,
            locations=TargetDimension(
                list(self.targetvalues_dimension_values(dimensions.g_location)),
                list(self.targetvalues_dimension_values(dimensions.g_location, False)),
            ),
            os=TargetDimension(
                list(self.targetvalues_dimension_values(dimensions.g_os)),
                list(self.targetvalues_dimension_values(dimensions.g_os, False)),
            ),
            device=TargetDimension(
                list(self.targetvalues_dimension_values(dimensions.g_device)),
                list(self.targetvalues_dimension_values(dimensions.g_device, False)),
            ),
            carrier=TargetDimension(
                list(self.targetvalues_dimension_values(dimensions.carrier)),
                list(self.targetvalues_dimension_values(dimensions.carrier, False)),
            ),
            age_group=TargetDimension(
                list(self.targetvalues_dimension_values(dimensions.age_group)),
                list(self.targetvalues_dimension_values(dimensions.age_group, False)),
            ),
            gender=TargetDimension(
                list(self.targetvalues_dimension_values(dimensions.gender)),
                list(self.targetvalues_dimension_values(dimensions.gender, False)),
            ),
            # Already should get TargetDimension
            publishers=self.publisher_target_dimensions(),
            quarter=TargetDimension(list(self.biddingperiod_dimensions())),
            content_category=TargetDimension(
                list(self.category_dimensions()),
                list(self.category_dimensions(False))
            ),
            # Flag required for opting-out of interest based ads
            is_interest_based=self.advert.strategy.is_interest_based(),
            # other
            adomain=[urlparse(self.advert.creative.landing_site_url or '').netloc],
            iurl=CDN % dict(cid=self.advert.creative.public_id),
            bids=bids,
            bids_minus_commissions=bids_minus_commissions,
            automatically_bidded=self.advert.strategy.is_automatically_bidded,
            is_bid_on_unknown_users=self.advert.strategy.is_bid_on_unknown_users,
            data_providers=data_providers,
            # and segment targeted dimensions
            **segment_dimensions
        )

    @classmethod
    def class_mapped(cls):
        # restrict traffic from AppNexus
        appnexus_update_profile.delay()

    # get strategy dimension values set
    def targetvalues_dimension_values(self, dimension, include=True):
        """
        Return dimension values for strategy from given category of TargetValue.

        :param str category: TargetValue category
        :param bool include: depend on which manager to use, including, or excluding

        :returns: generator returning tuples of target value lists
        """
        strategy = self.advert.strategy

        manager = strategy.targeting_values if include else strategy.targeting_values_exclude

        for representant in manager.representants().filter(category=dimension).all():
            for raw in representant.read_represented():
                if len(dimensions.hierarchy[dimension]) == 1:
                    yield raw.value_list[0]
                else:
                    yield tuple(raw.value_list)

    def publisher_target_dimensions(self):
        """
        Return TargetDimension dimension values for PublisherTargetValue.

        :returns: TargetDimension instance for publisher dimension
        :rtype: adserving.bidder.targeting.targetad.TargetDimension
        """

        publisherset = self.advert.strategy.publisherset
        if not publisherset:
            return TargetDimension()

        publishers = set()
        for representant in publisherset.target_values.all():
            for raw in representant.read_represented():
                # cut off inventory part
                publishers.add(raw.publishertargetvalue.network_publisher)

        if publisherset.blacklist:
            return TargetDimension(exclude=list(publishers))

        return TargetDimension(include=list(publishers))

    def biddingperiod_dimensions(self):
        """
        Return quarter dimension value.

        :returns: generator returning quarters to bid on
        """
        for bidding_period in self.advert.strategy.biddingperiod_set.all():
            for quarter in bidding_period.get_day_quarters():
                yield quarter

    def category_dimensions(self, include=True):
        """
        Return a content category dimension values.

        :param bool include: depend on which manager to use, including, or excluding

        :returns: generator returning category values. We're assuming here that categories can
        be stored as integers (appnexus categories) or strings (e.g. IAB-*). So if we compare them we must
        return proper type.
        """
        strategy = self.advert.strategy

        manager = strategy.content_category_values if include else strategy.content_category_values_exclude
        for category in manager.all():
            for raw in category.represented.all():
                try:
                    yield int(raw.name)
                except ValueError:
                    yield raw.name


class StrategyCacheMap(CacheMap):

    connections = (
        'optimizer',
    )
    connection_serializers = {
        'optimizer': partial(cPickle.dumps, protocol=2),
    }
    publishing_connections = {
        'optimizer': (OPTIMIZER_CHANNEL, OPTIMIZER_CLEAN_CHANNEL),
    }

    key_obj = redis_keys.strategy_cache_map

    observes = {
        'campaign.Strategy': {
            'relation': lambda strategy: strategy,
            'fields': ['budget_total', 'budget_spent', 'budget_daily', 'budget_daily_spent', 'is_automatically_bidded']
        },
        'campaign.Campaign': {
            'relation': lambda campaign: campaign.strategy_set.all(),
            'fields': ['budget_total', 'budget_spent']
        },
    }
    observes_date_fields = (
        'campaign__start_UTC',
        'campaign__end_UTC'
    )

    def mapped_optimizer(self):
        if self.strategy.is_automatically_bidded:
            return {
                'strategy_id': self.strategy.public_id,
                'start_UTC': self.strategy.campaign.start_UTC,
                'end_UTC': self.strategy.campaign.end_UTC,
                'strategy_budget_total': self.strategy.budget_total,
                'strategy_budget_spent': self.strategy.budget_spent,
                'campaign_budget_total': self.strategy.campaign.budget_total,
                'campaign_budget_spent': self.strategy.campaign.budget_spent,
                'budget_daily': self.strategy.budget_daily,
                'budget_daily_spent': self.strategy.budget_daily_spent,
                'optimized_metric': self.strategy.optimized_metric,
            }


class CampaignCacheMap(CacheMap):

    connections = 'adserver',
    observes = {
        'campaign.Campaign': {
            'relation': lambda campaign: campaign,
            'fields': ['is_deleted']
        },
        'campaign.Conversion': {
            'relation': lambda conversion: conversion.campaign,
            'fields': ['value']
        },
    }
    key_obj = constants.campaign_default_conv_value_key

    def mapped_adserver(self):
        ''' Gets default conversion value of campaign for cache '''
        return self.campaign.conversion_def.value
