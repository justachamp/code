import datetime

from tastypie import fields
from tastypie.validation import FormValidation


from adserving.types import Decimal
from ui.authorization import Auth
from ui.campaign.models import (
    BiddingPeriod, Campaign, Advert, Strategy, Site
)
from ui.campaign.forms import CampaignForm, StrategyValidation
from ui.utils import prepend_slug
from ui.common.api import SearchResource, ProtectedModelResource
from ui.common.search import QuoteUrl

from etc.constants import (
    BACKEND_DATE_FORMAT, BACKEND_TIME_FORMAT, BACKEND_DATE_TIME_FORMAT,
    UTC_TIME, TWOPLACES
)


class CampaignResource(ProtectedModelResource):

    prepend_urls = prepend_slug

    class Meta:

        resource_name = 'campaign'
        queryset = Campaign.objects_visible.all()
        fields = ('name')
        allowed_methods = ('get', 'post', 'put', 'delete', 'patch')
        authorization = Auth('account')
        always_return_data = True
        validation = FormValidation(form_class=CampaignForm)

    def get_object_list(self, request):
        ''' Filter by owner to avoid multiple objects with the same slug in details view '''
        all_objects = super(CampaignResource, self).get_object_list(request)
        return all_objects.filter(account=request.user.account)

    id = fields.IntegerField('id', readonly=True)
    slug = fields.CharField('slug', readonly=True)

    paused = fields.BooleanField('is_paused')
    archived = fields.BooleanField('is_archived', default=True)
    budget_total = fields.DecimalField('budget_total', readonly=True)
    budget_spent_with_commission = fields.DecimalField(
        'budget_spent_with_commission', readonly=True)
    budget_left = fields.DecimalField('budget_left', readonly=True)

    cap_campaign_selected = \
        fields.BooleanField('cap_campaign_selected', default=False)
    cap_strategy_selected = \
        fields.BooleanField('cap_strategy_selected', default=False)
    cap_creative_selected = \
        fields.BooleanField('cap_creative_selected', default=False)

    cap_campaign = fields.DecimalField('cap_total', default=0)
    cap_strategy = fields.DecimalField('cap_strategy', default=0)
    cap_creative = fields.DecimalField('cap_creative', default=0)
    cap_campaign_period = fields.CharField('cap_total_period', default=None)
    cap_strategy_period = fields.CharField('cap_strategy_period', default=None)
    cap_creative_period = fields.CharField('cap_creative_period', default=None)

    cap_campaign_presented = \
        fields.DecimalField('cap_total_presented', default=0)
    cap_strategy_presented = \
        fields.DecimalField('cap_strategy_presented', default=0)
    cap_creative_presented = \
        fields.DecimalField('cap_creative_presented', default=0)
    cap_campaign_period_presented = \
        fields.CharField('cap_total_period_presented', default=None)
    cap_strategy_period_presented = \
        fields.CharField('cap_strategy_period_presented', default=None)
    cap_creative_period_presented = \
        fields.CharField('cap_creative_period_presented', default=None)

    status = fields.CharField('status', readonly=True)

    default_landing_page_url = fields.CharField(null=False)

    def hydrate(self, bundle):
        account = bundle.request.user.account

        start = UTC_TIME % (bundle.data['start'], bundle.data["start_hour"])
        end = UTC_TIME % (bundle.data['end'], bundle.data["end_hour"])

        date_start = datetime.datetime.strptime(
            start,
            BACKEND_DATE_TIME_FORMAT
        )
        date_end = datetime.datetime.strptime(
            end,
            BACKEND_DATE_TIME_FORMAT
        )

        bundle.obj.account = account
        bundle.obj.start_UTC = account.into_UTC(date_start)
        bundle.obj.end_UTC = account.into_UTC(date_end)

        bundle.obj.budget_total = bundle.data['budget_total']

        # Warning: this will save actual value from UI. It will be updated
        # by cron which push redis data to the sql.
        if bundle.obj.pk:
            db_object = Campaign.objects.get(pk=bundle.obj.pk)
            bundle.obj.budget_spent = db_object.budget_spent
            bundle.obj.budget_spent_commission = db_object.budget_spent_commission

        bundle.obj.landing_site, _ = Site.objects.get_or_create(
            url=bundle.data['default_landing_page_url'],
            owner=account)

        bundle.obj.name = bundle.data['name']

        return bundle

    def hydrate_m2m(self, bundle):
        if bundle.obj is not None and bundle.obj.pk is not None:
            bundle.obj.conversion_def = {
                "name": bundle.data['conversion_name'],
                "value": bundle.data['conversion_value'],
                "active": bundle.data['conversion_active']
            }

        return bundle

    def dehydrate_state(self, bundle):
        bundle.data['state'] = bundle.obj.state.to_dict()

    def dehydrate_conversion(self, bundle):
        bundle.data['conversion_name'] = bundle.obj.conversion_def.name
        bundle.data['conversion_value'] = bundle.obj.conversion_def.value
        bundle.data['conversion_active'] = bundle.obj.conversion_def.active
        bundle.data['conversion_code'] = bundle.obj.conversion_tracking_code

    def dehydrate(self, bundle):
        strategies = bundle.obj.strategy_visible_set
        account = bundle.request.user.account

        date_start = account.from_UTC(bundle.obj.start_UTC)
        date_end = account.from_UTC(bundle.obj.end_UTC)

        bundle.data['start'] = date_start.strftime(BACKEND_DATE_FORMAT)
        bundle.data['start_hour'] = date_start.strftime(BACKEND_TIME_FORMAT)
        bundle.data['end'] = date_end.strftime(BACKEND_DATE_FORMAT)
        bundle.data['end_hour'] = date_end.strftime(BACKEND_TIME_FORMAT)

        bundle.data['seconds_left'] = bundle.obj.seconds_left

        bundle.data['default_landing_page_url'] = bundle.obj.landing_site.url
        bundle.data['account_timezone'] = bundle.obj.account.timezone

        if bundle.request.GET.get('with_strategies'):
            bundle.data['strategies'] = [
                {'name': s.name, 'slug': s.slug, 'paused': s.is_paused,
                 'id': s.id, 'state': s.state.to_dict()}
                for s in strategies
            ]

        # dehydrate fields that don't exists in a model
        self.dehydrate_state(bundle)
        self.dehydrate_conversion(bundle)

        return bundle


class Targeting(object):

    # frontend to backend maps

    SEARCH_FIELDS_MAPPING = (
        ('targetingIncludeLocations', 'location_include'),
        ('targetingExcludeLocations', 'location_exclude'),
        ('targetingIncludeDevices', 'device_include'),
        ('targetingExcludeDevices', 'device_exclude'),
        ('targetingIncludeOs', 'os_include'),
        ('targetingExcludeOs', 'os_exclude'),
        ('targetingIncludeCarriers', 'carrier_include'),
        ('targetingExcludeCarriers', 'carrier_exclude'),
        ('targetingIncludeGenderGroups', 'gender_include'),
        ('targetingExcludeGenderGroups', 'gender_exclude'),
        ('targetingIncludeAgeGroups', 'age_group_include'),
        ('targetingExcludeAgeGroups', 'age_group_exclude'),
    )

    CONTENT_CATEGORY_FIELDS_MAPPING = (
        ('targetingIncludeContent', 'category_include'),
        ('targetingExcludeContent', 'category_exclude'),
    )

    AUDIENCE_FIELDS_MAPPING = (
        ('targetingIncludeAudiences', 'audiences_include'),
        ('targetingExcludeAudiences', 'audiences_exclude'),
    )

    PROXIMIC_MATURITY_RATING_FIELDS_MAPPING = (
        (
            'targetingIncludeProximicMaturityRating',
            'proximic_maturity_rating_include',
        ),
        (
            'targetingExcludeProximicMaturityRating',
            'proximic_maturity_rating_exclude',
        ),
    )

    PROXIMIC_SAFETY_LEVEL_FIELDS_MAPPING = (
        (
            'targetingIncludeSafetyLevel',
            'proximic_safety_level_include',
        ),
        (
            'targetingExcludeSafetyLevel',
            'proximic_safety_level_exclude',
        ),
    )

    PROXIMIC_LANGUAGE_FIELDS_MAPPING = (
        (
            'targetingIncludeProximicLanguage',
            'proximic_language_include',
        ),
        (
            'targetingExcludeProximicLanguage',
            'proximic_language_exclude',
        ),
    )

    PROXIMIC_PAGE_QUALITY_FIELDS_MAPPING = (
        (
            'targetingIncludeProximicPageQuality',
            'proximic_page_quality_include',
        ),
        (
            'targetingExcludeProximicPageQuality',
            'proximic_page_quality_exclude',
        ),
    )

    PROXIMIC_PAGE_NOTICEABILITY_FIELDS_MAPPING = (
        (
            'targetingIncludeProximicPageNoticeability',
            'proximic_page_noticeability_include',
        ),
        (
            'targetingExcludeProximicPageNoticeability',
            'proximic_page_noticeability_exclude',
        ),
    )

    PROXIMIC_PAGE_PLACEMENT_FIELDS_MAPPING = (
        (
            'targetingIncludeProximicPagePlacement',
            'proximic_page_placement_include',
        ),
        (
            'targetingExcludeProximicPagePlacement',
            'proximic_page_placement_exclude',
        ),
    )

    PROXIMIC_CONTEXTUAL_FIELDS_MAPPING = (
        (
            'targetingIncludeProximicContextual',
            'proximic_contextual_include',
        ),
        (
            'targetingExcludeProximicContextual',
            'proximic_contextual_exclude',
        ),
    )

    PEER_CONTEXTUAL_SEGMENT_FIELDS_MAPPING = (
        (
            'targetingIncludePeerContextualSegment',
            'peer_contextual_include',
        ),
        (
            'targetingExcludePeerContextualSegment',
            'peer_contextual_exclude',
        ),
    )

    PEER_PAGE_QUALITY_FIELDS_MAPPING = (
        (
            'targetingIncludePeerPageQuality',
            'peer_page_quality_include',
        ),
        (
            'targetingExcludePeerPageQuality',
            'peer_page_quality_exclude',
        ),
    )

    PEER_LANGUAGE_FIELDS_MAPPING = (
        (
            'targetingIncludePeerLanguage',
            'peer_page_language_include',
        ),
        (
            'targetingExcludePeerLanguage',
            'peer_page_language_exclude'
        )
    )

    PEER_BRAND_PROTECTION_FIELDS_MAPPING = (
        (
            'targetingIncludePeerBrandProtection',
            'peer_brand_protection_include',
        ),
        (
            'targetingExcludePeerBrandProtection',
            'peer_brand_protection_exclude'
        )
    )

    LOTAME_DEMOGRAPHIC_FIELDS_MAPPING = (
        (
            'targetingIncludeLotameDemographic',
            'lotame_demographic_include',
        ),
        (
            'targetingExcludeLotameDemographic',
            'lotame_demographic_exclude'
        )
    )

    LOTAME_ADVANCED_DEMOGRAPHIC_FIELDS_MAPPING = (
        (
            'targetingIncludeLotameAdvancedDemographic',
            'lotame_advanced_demographic_include',
        ),
        (
            'targetingExcludeLotameAdvancedDemographic',
            'lotame_advanced_demographic_exclude'
        )
    )

    LOTAME_BEHAVIORAL_FIELDS_MAPPING = (
        (
            'targetingIncludeLotameBehavioralInterest',
            'lotame_behavioral_interest_include'
        ),
        (
            'targetingExcludeLotameBehavioralInterest',
            'lotame_behavioral_interest_exclude'
        )
    )

    LOTAME_INFLUENCERS_MAPPING = (
        (
            'targetingIncludeLotameInfluencers',
            'lotame_influencers_include'
        ),
        (
            'targetingExcludeLotameInfluencers',
            'lotame_influencers_exclude'
        )
    )

    LOTAME_OFFLINE_MAPPING = (
        (
            'targetingIncludeLotameOffline',
            'lotame_offline_include'
        ),
        (
            'targetingExcludeLotameOffline',
            'lotame_offline_exclude'
        )
    )

    ALL_MAPPINGS = {
        'search_mappings': SEARCH_FIELDS_MAPPING +
        AUDIENCE_FIELDS_MAPPING +
        CONTENT_CATEGORY_FIELDS_MAPPING +
        PROXIMIC_MATURITY_RATING_FIELDS_MAPPING +
        PROXIMIC_SAFETY_LEVEL_FIELDS_MAPPING +
        PROXIMIC_LANGUAGE_FIELDS_MAPPING +
        PROXIMIC_PAGE_QUALITY_FIELDS_MAPPING +
        PROXIMIC_PAGE_NOTICEABILITY_FIELDS_MAPPING +
        PROXIMIC_PAGE_PLACEMENT_FIELDS_MAPPING +
        PROXIMIC_CONTEXTUAL_FIELDS_MAPPING +
        PEER_CONTEXTUAL_SEGMENT_FIELDS_MAPPING +
        PEER_PAGE_QUALITY_FIELDS_MAPPING +
        PEER_LANGUAGE_FIELDS_MAPPING +
        PEER_BRAND_PROTECTION_FIELDS_MAPPING +
        LOTAME_DEMOGRAPHIC_FIELDS_MAPPING +
        LOTAME_ADVANCED_DEMOGRAPHIC_FIELDS_MAPPING +
        LOTAME_BEHAVIORAL_FIELDS_MAPPING +
        LOTAME_INFLUENCERS_MAPPING +
        LOTAME_OFFLINE_MAPPING
    }

    def backend_to_frontend_mapping(self, given_map, bundle_data, my_property):
        ''' Mapping frontend fields to backend fields '''
        for mapping in given_map:
            bundle_data[mapping[0]] = my_property[mapping[1]]

    def frontend_to_backend_mapping(self, given_map, bundle_data):
        ''' Mapping backend fields to frontend fields '''
        out = {}
        for mapping in given_map:
            out[mapping[1]] = bundle_data[mapping[0]]
        return out


class StrategyResource(ProtectedModelResource, Targeting):

    prepend_urls = prepend_slug

    class Meta:
        resource_name = 'strategy'
        queryset = Strategy.objects_visible.all()
        fields = (
            'name', 'landing_site_variable', 'budget_total', 'budget_daily',
            'budget_bid_CPM', 'capping_total', 'capping_day',
            'is_automatically_bidded', 'optimized_metric'
        )
        allowed_methods = ('get', 'post', 'patch', 'put', 'delete')
        always_return_data = True
        authorization = Auth('campaign__account')
        validation = StrategyValidation(**Targeting.ALL_MAPPINGS)

    def get_object_list(self, request):
        ''' Filter by owner to avoid multiple objects with the same slug in details view '''
        all_objects = super(StrategyResource, self).get_object_list(request)
        return all_objects.filter(campaign__account=request.user.account)

    id = fields.IntegerField('id', readonly=True)
    campaign = \
        fields.ForeignKey('ui.campaign.api.CampaignResource', 'campaign')
    campaign_slug = fields.CharField('campaign__slug', readonly=True)
    campaign_total_budget = fields.DecimalField('campaign__total_budget',
                                                null=True)
    periods = fields.ToManyField('ui.campaign.api.PeriodResource',
                                 'biddingperiod_set', full=True)

    paused = fields.BooleanField('is_paused')
    reviewed = fields.BooleanField('is_reviewed', readonly=True)

    slug = fields.CharField('slug', readonly=True)

    budget_spent_with_commission = fields.DecimalField('budget_spent_with_commission', readonly=True)

    budget_left = fields.DecimalField('budget_left', readonly=True)

    budget_daily_spent = fields.DecimalField('budget_daily_spent',
                                             readonly=True)

    distributed_evenly = fields.BooleanField('is_distributed_evenly')

    capping_total_spent = fields.DecimalField('capping_total_spent',
                                              readonly=True)
    capping_day_spent = fields.DecimalField('capping_day_spent',
                                            readonly=True)
    targetingIncludeAudiences = \
        fields.ToManyField('ui.storage.api.AudienceResource',
                           'audiences', full=True)
    targetingExcludeAudiences = \
        fields.ToManyField('ui.storage.api.AudienceResource',
                           'audiences_exclude', full=True)

    target_devices = fields.BooleanField('is_targeted_devices')
    target_localization = fields.BooleanField('is_targeted_local')
    target_user_profile = fields.BooleanField('is_targeted_user_profile')
    target_publisher = fields.BooleanField('is_targeted_publisher')

    publisherset = fields.ForeignKey(
        'ui.publishers.api.PublisherSetResource', 'publisherset', null=True)

    utm_tags = fields.BooleanField('is_UTM_tags')

    day_parted = fields.BooleanField('is_day_parted')

    bid_on_unknown_users = fields.BooleanField('is_bid_on_unknown_users')

    ui_to_db_mapping = {}
    db_to_ui_mapping = {}
    for ui_type, db_type in Strategy.STRATEGY_TYPES:
        ui_to_db_mapping[ui_type] = db_type
        db_to_ui_mapping[db_type] = ui_type

    # frontend -> backend
    def hydrate(self, bundle):

        # filling missing fields
        campaign_id = bundle.data['campaign']
        publisherset_id = bundle.data['publisherset']

        # FIXME: Use Django form for choices field.
        # Translate from UI names to db/targeting/bidreq names:
        bundle.obj.type = self.ui_to_db_mapping[bundle.data['type']]

        if isinstance(campaign_id, int):
            bundle.data['campaign'] = '/api/campaign/%d/' % campaign_id

        if isinstance(publisherset_id, int):
            bundle.data['publisherset'] =\
                '/api/publishers/sets/%d/' % publisherset_id

        bundle.data['periods'] = []
        bundle.data['target_localization'] = []
        bundle.data['target_user_profile'] = []
        bundle.data['target_publisher'] = []
        bundle.data['target_devices'] = []

        # Warning: this will save actual value from UI. It will be updated
        # by cron which push redis data to the sql.
        if bundle.obj.pk:
            db_object = Strategy.objects.get(pk=bundle.obj.pk)
            bundle.obj.budget_spent = db_object.budget_spent
            bundle.obj.budget_spent_commission = db_object.budget_spent_commission
            bundle.obj.budget_daily_spent = db_object.budget_daily_spent

        for preriod in bundle.data['bidding_periods']:
            if isinstance(preriod['from'], basestring)\
                    and isinstance(preriod['to'], basestring):
                preriod['from'] = datetime.datetime.strptime(
                    preriod['from'], '%H:%M').time()
                preriod['to'] = datetime.datetime.strptime(
                    preriod['to'], '%H:%M').time()

        return bundle

    # frontend -> backend (m2m)
    def hydrate_m2m(self, bundle):
        if bundle.obj is not None and bundle.obj.pk is not None:
            # adds related objects which are not explicitly in this resource
            bundle.obj.landing_sites_def = bundle.data['landing_sites']
            bundle.obj.bidding_periods = bundle.data['bidding_periods']
            bundle.obj.adverts_def = bundle.data['adverts']

            # map targeting search fields
            bundle.obj.search_fields_def = self.frontend_to_backend_mapping(
                self.SEARCH_FIELDS_MAPPING,
                bundle.data
            )

            # map content category targeting fields
            bundle.obj.content_categories_def = self.frontend_to_backend_mapping(
                self.CONTENT_CATEGORY_FIELDS_MAPPING,
                bundle.data,
            )

            # map segments targeting fields (maturity rating)
            bundle.obj.proximic_maturity_rating_fields_def = self.frontend_to_backend_mapping(
                self.PROXIMIC_MATURITY_RATING_FIELDS_MAPPING,
                bundle.data,
            )

            # map segments targeting fields (safety level)
            bundle.obj.proximic_safety_level_fields_def = self.frontend_to_backend_mapping(
                self.PROXIMIC_SAFETY_LEVEL_FIELDS_MAPPING,
                bundle.data,
            )

            # map segments targeting fields (language)
            bundle.obj.proximic_language_fields_def = self.frontend_to_backend_mapping(
                self.PROXIMIC_LANGUAGE_FIELDS_MAPPING,
                bundle.data,
            )

            # map segments targeting fields (page quality)
            bundle.obj.proximic_page_quality_fields_def = self.frontend_to_backend_mapping(
                self.PROXIMIC_PAGE_QUALITY_FIELDS_MAPPING,
                bundle.data,
            )

            # map segments targeting fields (page noticeability)
            bundle.obj.proximic_page_noticeability_fields_def = self.frontend_to_backend_mapping(
                self.PROXIMIC_PAGE_NOTICEABILITY_FIELDS_MAPPING,
                bundle.data,
            )

            # map segments targeting fields (page placement)
            bundle.obj.proximic_page_placement_fields_def = self.frontend_to_backend_mapping(
                self.PROXIMIC_PAGE_PLACEMENT_FIELDS_MAPPING,
                bundle.data,
            )

            # map segments targeting fields (contextual)
            bundle.obj.proximic_contextual_fields_def = self.frontend_to_backend_mapping(
                self.PROXIMIC_CONTEXTUAL_FIELDS_MAPPING,
                bundle.data,
            )

            bundle.obj.peer_content_categories_def = self.frontend_to_backend_mapping(
                self.PEER_CONTEXTUAL_SEGMENT_FIELDS_MAPPING,
                bundle.data,
            )

            bundle.obj.peer_page_quality_def = self.frontend_to_backend_mapping(
                self.PEER_PAGE_QUALITY_FIELDS_MAPPING,
                bundle.data
            )

            bundle.obj.peer_language_def = self.frontend_to_backend_mapping(
                self.PEER_LANGUAGE_FIELDS_MAPPING,
                bundle.data
            )

            bundle.obj.peer_brand_protection_def = self.frontend_to_backend_mapping(
                self.PEER_BRAND_PROTECTION_FIELDS_MAPPING,
                bundle.data
            )

            bundle.obj.lotame_demographic = self.frontend_to_backend_mapping(
                self.LOTAME_DEMOGRAPHIC_FIELDS_MAPPING,
                bundle.data
            )

            bundle.obj.lotame_advanced_demographic = self.frontend_to_backend_mapping(
                self.LOTAME_ADVANCED_DEMOGRAPHIC_FIELDS_MAPPING,
                bundle.data
            )

            bundle.obj.lotame_behavioral_interest = self.frontend_to_backend_mapping(
                self.LOTAME_BEHAVIORAL_FIELDS_MAPPING,
                bundle.data
            )

            bundle.obj.lotame_influencers = self.frontend_to_backend_mapping(
                self.LOTAME_INFLUENCERS_MAPPING,
                bundle.data
            )

            bundle.obj.lotame_offline = self.frontend_to_backend_mapping(
                self.LOTAME_OFFLINE_MAPPING,
                bundle.data
            )

        return super(ProtectedModelResource, self).hydrate_m2m(bundle)

    def dehydrate_state(self, bundle):
        bundle.data['state'] = bundle.obj.state.to_dict()

    # backend -> frontend
    def dehydrate(self, bundle):
        strategy = bundle.obj

        # FIXME: Use Django form for choices field.
        # Translate from db/targeting/bidreq names to UI names:
        # Dehydrate may be called twice. Check if the names are already
        # translated:
        bundle.data['type'] = self.db_to_ui_mapping[strategy.type]

        bundle.data['campaign'] = strategy.campaign_id
        bundle.data['publisherset'] = strategy.publisherset_id
        bundle.data['landing_sites'] = strategy.landing_sites_def
        bundle.data['bidding_periods'] = strategy.bidding_periods
        bundle.data['adverts'] = strategy.adverts_def

        if (strategy.budget_bid_CPM):
            bundle.data['budget_bid_CPM'] = \
                strategy.budget_bid_CPM.quantize(TWOPLACES)
        bundle.data['budget_spent_with_commission'] = Decimal(strategy.budget_spent_with_commission).quantize(TWOPLACES)
        bundle.data['budget_spent'] = \
            Decimal(strategy.budget_spent).quantize(TWOPLACES)

        if (strategy.budget_daily):
            bundle.data['budget_daily'] = \
                Decimal(strategy.budget_daily).quantize(TWOPLACES)

        bundle.data['budget_daily_spent'] = \
            Decimal(strategy.budget_daily_spent).quantize(TWOPLACES)
        bundle.data['budget_left'] = \
            Decimal(strategy.budget_left).quantize(TWOPLACES)

        # map targeting search fields
        self.backend_to_frontend_mapping(
            self.SEARCH_FIELDS_MAPPING,
            bundle.data,
            strategy.search_fields_def,
        )

        # map content category targeting
        self.backend_to_frontend_mapping(
            self.CONTENT_CATEGORY_FIELDS_MAPPING,
            bundle.data,
            strategy.content_categories_def,
        )

        # map proximic maturity rating targeting
        self.backend_to_frontend_mapping(
            self.PROXIMIC_MATURITY_RATING_FIELDS_MAPPING,
            bundle.data,
            strategy.proximic_maturity_rating_fields_def,
        )

        # map proximic safety level targeting
        self.backend_to_frontend_mapping(
            self.PROXIMIC_SAFETY_LEVEL_FIELDS_MAPPING,
            bundle.data,
            strategy.proximic_safety_level_fields_def,
        )

        # map proximic safety level targeting
        self.backend_to_frontend_mapping(
            self.PROXIMIC_LANGUAGE_FIELDS_MAPPING,
            bundle.data,
            strategy.proximic_language_fields_def,
        )

        # map proximic safety level targeting
        self.backend_to_frontend_mapping(
            self.PROXIMIC_PAGE_QUALITY_FIELDS_MAPPING,
            bundle.data,
            strategy.proximic_page_quality_fields_def,
        )

        # map proximic noticeability targeting
        self.backend_to_frontend_mapping(
            self.PROXIMIC_PAGE_NOTICEABILITY_FIELDS_MAPPING,
            bundle.data,
            strategy.proximic_page_noticeability_fields_def,
        )

        # map proximic page placement targeting
        self.backend_to_frontend_mapping(
            self.PROXIMIC_PAGE_PLACEMENT_FIELDS_MAPPING,
            bundle.data,
            strategy.proximic_page_placement_fields_def,
        )

        # map proximic contextual targeting
        self.backend_to_frontend_mapping(
            self.PROXIMIC_CONTEXTUAL_FIELDS_MAPPING,
            bundle.data,
            strategy.proximic_contextual_fields_def,
        )

        self.backend_to_frontend_mapping(
            self.PEER_CONTEXTUAL_SEGMENT_FIELDS_MAPPING,
            bundle.data,
            strategy.peer_content_categories_def
        )
        self.backend_to_frontend_mapping(
            self.PEER_LANGUAGE_FIELDS_MAPPING,
            bundle.data,
            strategy.peer_language_def
        )

        self.backend_to_frontend_mapping(
            self.PEER_BRAND_PROTECTION_FIELDS_MAPPING,
            bundle.data,
            strategy.peer_brand_protection_def
        )

        self.backend_to_frontend_mapping(
            self.PEER_PAGE_QUALITY_FIELDS_MAPPING,
            bundle.data,
            strategy.peer_page_quality_def
        )

        self.backend_to_frontend_mapping(
            self.LOTAME_DEMOGRAPHIC_FIELDS_MAPPING,
            bundle.data,
            strategy.lotame_demographic
        )

        self.backend_to_frontend_mapping(
            self.LOTAME_ADVANCED_DEMOGRAPHIC_FIELDS_MAPPING,
            bundle.data,
            strategy.lotame_advanced_demographic
        )

        self.backend_to_frontend_mapping(
            self.LOTAME_BEHAVIORAL_FIELDS_MAPPING,
            bundle.data,
            strategy.lotame_behavioral_interest
        )

        self.backend_to_frontend_mapping(
            self.LOTAME_INFLUENCERS_MAPPING,
            bundle.data,
            strategy.lotame_influencers
        )

        self.backend_to_frontend_mapping(
            self.LOTAME_OFFLINE_MAPPING,
            bundle.data,
            strategy.lotame_offline
        )

        self.dehydrate_state(bundle)

        return bundle


class PeriodResource(ProtectedModelResource):

    class Meta:
        resource_name = 'period'
        queryset = BiddingPeriod.objects.all()
        fields = ['start', 'end']
        allowed_methods = ('get', 'post', 'patch', 'put', 'delete')
        authorization = Auth('strategy__campaign__account')

    id = fields.IntegerField('id', readonly=True)
    strategy = \
        fields.ForeignKey('ui.campaign.api.StrategyResource', 'strategy')


class AdvertResource(ProtectedModelResource):

    class Meta:
        resource_name = 'advert'
        queryset = Advert.objects.all()
        fields = ['custom_bid_CPM', 'creative']
        allowed_methods = ('get', 'post', 'patch', 'put', 'delete')
        authorization = Auth('strategy__campaign__account')

    id = fields.IntegerField('id', readonly=True)
    strategy = \
        fields.ForeignKey('ui.campaign.api.StrategyResource', 'strategy')
    landing_page = \
        fields.ForeignKey('ui.campaign.api.SiteResource', 'landing_site')
    js_code = fields.CharField('js_code')
    custom_pixel = fields.CharField('custom_pixel', null=True)
    status = fields.CharField('status', readonly=True)

    def dehydrate_state(self, bundle):
        bundle.data['state'] = bundle.obj.state.to_dict()

    def dehydrate(self, bundle):
        self.dehydrate_state(bundle)

        return bundle


class SiteResource(SearchResource):

    class Meta:
        allowed_methods = ('get',)
        resource_name = 'site'
        queryset = Site.objects.all()
        authorization = Auth('owner')
        fields = ('url')

    id = fields.IntegerField('id', readonly=True)

    def build_search_query(self, request, search_query):
        '''
            Building search query for Site model
        '''
        return search_query.filter(url=QuoteUrl(request.GET.get('q', '')),
                                   owner_id=request.user.account_id)
