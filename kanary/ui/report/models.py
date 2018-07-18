from functools import partial

from django.db.models import Model, ForeignKey

from etc import dimensions
from etc.constants import PUBLIC_ID_DELIMITER
from ui.fields import BudgetSpentDecimalField, QuarterDateTimeField, BigDecimalField, LongURLField
from ui.campaign.models import Advert, Strategy, Campaign
from ui.targeting.models import (
    TargetValue, PublisherTargetValue, ContentCategoryValue,
    SegmentProximicMaturityRating, SegmentProximicSafetyLevel,
    SegmentProximicPageQuality, SegmentProximicPageNoticeability,
    SegmentProximicPagePlacement, SegmentProximicContextual,
    SegmentProximicPageLanguage,
    Peer39PageLanguage, Peer39BrandProtection, Peer39ContextualSegment,
    Peer39PageQuality,
    LotameDemographic, LotameAdvancedDemographic, LotameBehavioralInterest,
    LotameInfluencers, LotameOffline,
)
from ui.report.managers import (
    ReportCampaignManager,
    ReportStrategyManager,
    ReportAdvertManager,
    ReportCategoryManager,
    ReportSiteManager,
    ReportTargetValueManager,
    ReportDataProviderManager,
)


# partials for Fields declaration in BaseReport
BigDecimalField = partial(BigDecimalField, default=0)
BudgetField = partial(BudgetSpentDecimalField, default=0)
ForeignKeyNull = partial(ForeignKey, null=True)


class BaseReport(Model):

    class Meta:
        abstract = True
        unique_together = (
            ('dimension', 'related', 'time'),
        )

    # time
    time = QuarterDateTimeField()

    # proximic, peer39, etc.
    data_cost_value = BudgetField()

    # (price + data cost) * kanary commission
    commission_value = BudgetField()

    imp = BigDecimalField()
    # imp_value = price paid + hidden commission
    imp_value = BudgetField()

    clk = BigDecimalField()
    conv = BigDecimalField()
    conv_value = BudgetField()

    @property
    def displayed_name(self):
        '''
        Returns name of related object. Must be overriden.
        '''
        raise NotImplementedError

    @staticmethod
    def get_related_id(public_id):
        ''' Must be overriden to return random_id based on public_id
        :param str public_id: e.g. CAMP1_STR3_AD4
        :returns random_id of related table
        :rtype str
        '''
        raise NotImplementedError

    @classmethod
    def group_base_message_key(cls, message):
        """
        Return base message key for grouping.

        :param reports.event.EventMsg message: message to group
        :returns: base grouping keys like (ad, time) or (strategy, time)
        :rtype: list of tuples

        """
        raise NotImplementedError

    @classmethod
    def group_message_keys(cls, message):
        """
        Define message grouping for given report type.

        :param reports.event.EventMsg message: message to group
        :returns: list of grouping keys
        :rtype: list of tuples
        """
        raise NotImplementedError

    @classmethod
    def aggregation_divisor(cls, mesage):
        """
        Return number of elements we aggregate given message in.

        :param reports.event.EventMsg message: message to get aggregation divisor
        :returns: aggregation divisor
        :rtype: int
        """
        raise NotImplementedError

    @classmethod
    def get_earliest_time(cls, pks):
        '''
        Find earliest date in database. If there is no data return None.

        :param list pks: list of related object ids (ints)
        :return: earliest date or None
        :rtype: datetime or None
        '''
        try:
            return cls.objects.filter(related__pk__in=pks).earliest('time').time
        except cls.DoesNotExist:
            return None

    @classmethod
    def identity_map(cls, report_aggregation):
        """
        Build identification dictionary based for given report type.

        :param reports.django_layer.ReportAggregation report_aggregation: report aggregation for which we're generating
            identity_map

        :returns: dictionary containing model fields and values by which we can identify report row type
        :rtype: dict
        """
        return {
            'related_id': cls.get_related_id(report_aggregation.id),
            'time': report_aggregation.time,
        }


class BaseReportAdvert(BaseReport):

    class Meta(BaseReport.Meta):
        abstract = True

    objects = ReportAdvertManager()

    related = ForeignKey(Advert, to_field='id_random')

    @staticmethod
    def get_related_id(public_id):
        """
        :param str public_id: e.g. ACC1_CAMP1_STR3_AD4

        :returns random_id of Advert, e.g. AD4
        :rtype str
        """
        return public_id.split(PUBLIC_ID_DELIMITER)[-1]

    @classmethod
    def group_base_message_key(cls, message):
        """
        Define grouping for messages based on ad_id and date.
        """
        return {'id': message.ad_id, 'time': message.date}

    @classmethod
    def group_message_keys(cls, message):
        """
        Define grouping for messages based on ad_id and date.
        """
        yield cls.group_base_message_key(message)


class ReportAdvert(BaseReportAdvert):

    dimension_element = 'advert'

    class Meta:
        unique_together = (
            ('related', 'time'),
        )

    @property
    def displayed_name(self):
        '''
        Returns name of related object.
        '''
        return self.related.creative.name

    @classmethod
    def aggregation_divisor(cls, message):
        return 1


class BaseReportStrategy(BaseReport):

    class Meta(BaseReport.Meta):
        abstract = True

    objects = ReportStrategyManager()

    related = ForeignKey(Strategy, to_field='id_random')

    @staticmethod
    def get_related_id(public_id):
        """
        :param str public_id: e.g. ACC_1_CAMP1_STR3_AD4

        :returns random_id of Strategy, e.g. STR3
        :rtype str
        """
        return public_id.split(PUBLIC_ID_DELIMITER)[2]

    @classmethod
    def group_base_message_key(cls, message):
        """
        Define grouping for messages based on strategy_id and date.
        """
        return {'id': message.strategy_id, 'time': message.date}

    @classmethod
    def group_message_keys(cls, message):
        """
        Define grouping for messages based on strategy_id and date.
        """
        yield cls.group_base_message_key(message)


class BaseReportTargetValueStrategy(BaseReportStrategy):

    class Meta(BaseReportStrategy.Meta):
        abstract = True

    objects = ReportTargetValueManager()


class ReportStrategy(BaseReportStrategy):

    dimension_element = 'strategy'

    class Meta:
        unique_together = (
            ('related', 'time'),
        )

    @property
    def displayed_name(self):
        '''
        Returns name of related object.
        '''
        return self.related.name

    @classmethod
    def aggregation_divisor(cls, message):
        return 1


class BaseReportCampaign(BaseReport):

    class Meta(BaseReport.Meta):
        abstract = True

    objects = ReportCampaignManager()

    related = ForeignKey(Campaign, to_field='id_random')

    @staticmethod
    def get_related_id(public_id):
        """
        :param str public_id: e.g. ACC1_CAMP1_STR3_AD4

        :returns random_id of Strategy, e.g. CAMP1
        :rtype str
        """
        return public_id.split(PUBLIC_ID_DELIMITER)[1]

    @classmethod
    def group_base_message_key(cls, message):
        """
        Define grouping for messages based on strategy_id and date.
        """
        return {'id': message.campaign_id, 'time': message.date}

    @classmethod
    def group_message_keys(cls, message):
        """
        Define grouping for messages based on strategy_id and date.
        """
        yield cls.group_base_message_key(message)


class ReportCampaign(BaseReportCampaign):

    class Meta:
        unique_together = (
            ('related', 'time'),
        )

    @property
    def displayed_name(self):
        '''
        Returns name of related object.
        '''
        return self.related.name

    @classmethod
    def aggregation_divisor(cls, message):
        return 1


class BaseReportTargetValueCampaign(BaseReportCampaign):

    class Meta(BaseReportCampaign.Meta):
        abstract = True

    objects = ReportTargetValueManager()


class BaseReportDimension(object):

    dimension_hierarchy = NotImplemented
    """Hierarchy report is based on."""

    dimension_element = NotImplemented
    """Hierarchy's element report is based on."""

    @classmethod
    def group_message_keys(cls, message):
        """
        Define grouping for messages based on
        BaseReportDimension.group_message_keys and
        appropriate dimension class definition setting.

        this method requires child model to define
        """
        group_key = super(BaseReportDimension, cls).group_base_message_key(message)

        # both dimension_hierarchy and dimension_element should be defined,
        # or group_message should be overridden
        if NotImplemented in [cls.dimension_hierarchy, cls.dimension_element]:
            raise NotImplementedError

        dimension = message.dimension[cls.dimension_hierarchy]

        if dimension:
            hierarchy = dimensions.hierarchy[cls.dimension_hierarchy]
            dimension = dimension[hierarchy.index(cls.dimension_element)]

        else:
            dimension = None

        yield dict(dimension_id=dimension, **group_key)

    @classmethod
    def identity_map(cls, report_aggregation):
        """Extends basic identity dict with dimension_id"""
        identity = super(BaseReportDimension, cls).identity_map(report_aggregation)
        identity['dimension_id'] = report_aggregation.dimension_id
        return identity

    @classmethod
    def aggregation_divisor(cls, message):
        return 1


# ========================
# Os related report tables
# ========================


class ReportStrategyOs(BaseReportDimension, BaseReportTargetValueStrategy):

    dimension_hierarchy = dimensions.g_os
    dimension_element = dimensions.os

    dimension = ForeignKeyNull(TargetValue, related_name='reports_strategy_os')


class ReportCampaignOs(BaseReportDimension, BaseReportTargetValueCampaign):

    dimension_hierarchy = dimensions.g_os
    dimension_element = dimensions.os

    dimension = ForeignKeyNull(TargetValue, related_name='reports_campaign_os')


# ===========================
# Device related report model
# ===========================


class ReportStrategyModel(BaseReportDimension, BaseReportTargetValueStrategy):

    dimension_hierarchy = dimensions.g_device
    dimension_element = dimensions.model

    dimension = ForeignKeyNull(TargetValue, related_name='reports_strategy_model')


class ReportCampaignModel(BaseReportDimension, BaseReportTargetValueCampaign):

    dimension_hierarchy = dimensions.g_device
    dimension_element = dimensions.model

    dimension = ForeignKeyNull(TargetValue, related_name='reports_campaign_model')


class ReportStrategyMake(BaseReportDimension, BaseReportTargetValueStrategy):

    dimension_hierarchy = dimensions.g_device
    dimension_element = dimensions.make

    dimension = ForeignKeyNull(TargetValue, related_name='reports_strategy_make')


class ReportCampaignMake(BaseReportDimension, BaseReportTargetValueCampaign):

    dimension_hierarchy = dimensions.g_device
    dimension_element = dimensions.make

    dimension = ForeignKeyNull(TargetValue, related_name='reports_campaign_make')


# ========
# Location
# ========


class ReportStrategyCountry(BaseReportDimension, BaseReportTargetValueStrategy):

    dimension_hierarchy = dimensions.g_location
    dimension_element = dimensions.country

    dimension = ForeignKeyNull(TargetValue, related_name='reports_strategy_country')


class ReportCampaignCountry(BaseReportDimension, BaseReportTargetValueCampaign):

    dimension_hierarchy = dimensions.g_location
    dimension_element = dimensions.country

    dimension = ForeignKeyNull(TargetValue, related_name='reports_campaign_country')


class ReportStrategyRegion(BaseReportDimension, BaseReportTargetValueStrategy):

    dimension_hierarchy = dimensions.g_location
    dimension_element = dimensions.region

    dimension = ForeignKeyNull(TargetValue, related_name='reports_strategy_region')


class ReportCampaignRegion(BaseReportDimension, BaseReportTargetValueCampaign):

    dimension_hierarchy = dimensions.g_location
    dimension_element = dimensions.region

    dimension = ForeignKeyNull(TargetValue, related_name='reports_campaign_region')


class ReportStrategyCity(BaseReportDimension, BaseReportTargetValueStrategy):

    dimension_hierarchy = dimensions.g_location
    dimension_element = dimensions.city

    dimension = ForeignKeyNull(TargetValue, related_name='reports_strategy_city')


class ReportCampaignCity(BaseReportDimension, BaseReportTargetValueCampaign):

    dimension_hierarchy = dimensions.g_location
    dimension_element = dimensions.city

    dimension = ForeignKeyNull(TargetValue, related_name='reports_campaign_city')


# =======
# Carrier
# =======


class ReportStrategyCarrier(BaseReportDimension, BaseReportTargetValueStrategy):

    dimension_hierarchy = dimensions.carrier
    dimension_element = dimensions.carrier

    dimension = ForeignKeyNull(TargetValue, related_name='reports_strategy_carrier')


class ReportCampaignCarrier(BaseReportDimension, BaseReportTargetValueCampaign):

    dimension_hierarchy = dimensions.carrier
    dimension_element = dimensions.carrier

    dimension = ForeignKeyNull(TargetValue, related_name='reports_campaign_carrier')


# ======
# Domain
# ======


class ReportStrategyDomain(BaseReportDimension, BaseReportTargetValueStrategy):

    dimension_hierarchy = dimensions.domain
    dimension_element = dimensions.domain

    dimension = ForeignKeyNull(TargetValue, related_name='reports_strategy_domain')


class ReportCampaignDomain(BaseReportDimension, BaseReportTargetValueCampaign):

    dimension_hierarchy = dimensions.domain
    dimension_element = dimensions.domain

    dimension = ForeignKeyNull(TargetValue, related_name='reports_campaign_domain')


# =========
# Gender ;)
# =========


class ReportStrategyGender(BaseReportDimension, BaseReportTargetValueStrategy):

    dimension_hierarchy = dimensions.gender
    dimension_element = dimensions.gender

    dimension = ForeignKeyNull(TargetValue, related_name='reports_strategy_gender')


class ReportCampaignGender(BaseReportDimension, BaseReportTargetValueCampaign):

    dimension_hierarchy = dimensions.gender
    dimension_element = dimensions.gender

    dimension = ForeignKeyNull(TargetValue, related_name='reports_campaign_gender')


# ===
# Age
# ===


class ReportStrategyAge(BaseReportDimension, BaseReportTargetValueStrategy):

    dimension_hierarchy = dimensions.age_group
    dimension_element = dimensions.age_group

    dimension = ForeignKeyNull(TargetValue, related_name='reports_strategy_age')


class ReportCampaignAge(BaseReportDimension, BaseReportTargetValueCampaign):

    dimension_hierarchy = dimensions.age_group
    dimension_element = dimensions.age_group

    dimension = ForeignKeyNull(TargetValue, related_name='reports_campaign_age')


# ========
# Position
# ========


class ReportStrategyPosition(BaseReportDimension, BaseReportTargetValueStrategy):

    dimension_hierarchy = dimensions.position
    dimension_element = dimensions.position

    dimension = ForeignKeyNull(TargetValue, related_name='reports_strategy_position')


class ReportCampaignPosition(BaseReportDimension, BaseReportTargetValueCampaign):

    dimension_hierarchy = dimensions.position
    dimension_element = dimensions.position

    dimension = ForeignKeyNull(TargetValue, related_name='reports_campaign_position')


# =========
# Publisher
# =========


class ReportStrategyPublisherNetwork(BaseReportDimension, BaseReportStrategy):

    objects = ReportTargetValueManager()

    dimension_hierarchy = dimensions.g_publisher
    dimension_element = dimensions.network

    dimension = ForeignKeyNull(PublisherTargetValue, related_name='reports_strategy_network')


class ReportCampaignPublisherNetwork(BaseReportDimension, BaseReportCampaign):

    objects = ReportTargetValueManager()

    dimension_hierarchy = dimensions.g_publisher
    dimension_element = dimensions.network

    dimension = ForeignKeyNull(PublisherTargetValue, related_name='reports_campaign_network')


class ReportStrategyPublisher(BaseReportDimension, BaseReportStrategy):

    objects = ReportTargetValueManager()

    dimension_hierarchy = dimensions.g_publisher
    dimension_element = dimensions.publisher_name

    dimension = ForeignKeyNull(PublisherTargetValue, related_name='reports_strategy_publisher')


class ReportCampaignPublisher(BaseReportDimension, BaseReportCampaign):

    objects = ReportTargetValueManager()

    dimension_hierarchy = dimensions.g_publisher
    dimension_element = dimensions.publisher_name

    dimension = ForeignKeyNull(PublisherTargetValue, related_name='reports_campaign_publisher')


# ====
# Site
# ====


class BaseReportSite(object):

    dimension_element = dimensions.site

    @classmethod
    def group_message_keys(cls, message):
        """
        Define grouping for messages based on
        BaseReportDimension.group_message_keys and
        appropriate dimension class definition setting.

        this method requires child model to define
        """
        group_key = super(BaseReportSite, cls).group_base_message_key(message)
        yield dict(dimension_id=message.landing_site, **group_key)

    @classmethod
    def identity_map(cls, report_aggregation):
        """Extends basic identity dict with dimension"""
        identity = super(BaseReportSite, cls).identity_map(report_aggregation)
        # delete what's not needed for this site
        del identity['dimension_id']
        identity['dimension'] = report_aggregation.dimension_id
        return identity


class ReportStrategySite(BaseReportSite, BaseReportDimension, BaseReportStrategy):

    objects = ReportSiteManager()

    dimension = LongURLField(null=True)


class ReportCampaignSite(BaseReportSite, BaseReportDimension, BaseReportCampaign):

    objects = ReportSiteManager()

    dimension = LongURLField(null=True)


# ===========================================================
# Multivalues - these dimensions can multiply in bidrequests
# ===========================================================

class BaseMultivalueReport(object):

    @classmethod
    def group_message_keys(cls, message):
        """
        Define grouping for messages based on
        BaseReportDimension.group_message_keys and
        appropriate dimension class definition setting.

        this method requires child model to define
        """
        group_key = super(BaseMultivalueReport, cls).group_base_message_key(message)

        # We use assumption (and simplification) in here:
        # "Multivalue" dimensions have always only one-level hierarchy
        extracted_dimensions = message.dimension[cls.dimension_hierarchy]

        for dimension in extracted_dimensions:
            yield dict(dimension_id=dimension, **group_key)

        if not extracted_dimensions:
            yield dict(dimension_id=None, **group_key)

    @classmethod
    def aggregation_divisor(cls, message):
        """
        Calculate aggregation_divisor for BaseReportDimension instances
        """
        if NotImplemented in [cls.dimension_hierarchy, cls.dimension_element]:
            raise NotImplementedError

        # dimension is defined, and hierarchy is dimension as well,
        # we count elements
        if message.dimension[cls.dimension_hierarchy]:
            return len(message.dimension[cls.dimension_hierarchy])

        # there is always at least one unknown!
        return 1


# ================
# content category
# ================


class ReportStrategyCategory(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportCategoryManager()

    dimension_hierarchy = ContentCategoryValue.DIMENSION
    dimension_element = ContentCategoryValue.DIMENSION

    dimension = ForeignKeyNull(ContentCategoryValue, related_name='reports_strategy_category')


class ReportCampaignCategory(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportCategoryManager()

    dimension_hierarchy = ContentCategoryValue.DIMENSION
    dimension_element = ContentCategoryValue.DIMENSION

    dimension = ForeignKeyNull(ContentCategoryValue, related_name='reports_campaign_category')


# ========
# Proximic
# ========


class ReportStrategyProximicMaturity(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicMaturityRating.DIMENSION
    dimension_element = SegmentProximicMaturityRating.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicMaturityRating, related_name='reports_strategy_maturity')


class ReportCampaignProximicMaturity(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicMaturityRating.DIMENSION
    dimension_element = SegmentProximicMaturityRating.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicMaturityRating, related_name='reports_campaign_maturity')


class ReportStrategyProximicSafety(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicSafetyLevel.DIMENSION
    dimension_element = SegmentProximicSafetyLevel.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicSafetyLevel, related_name='reports_strategy_safety')


class ReportCampaignProximicSafety(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicSafetyLevel.DIMENSION
    dimension_element = SegmentProximicSafetyLevel.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicSafetyLevel, related_name='reports_campaign_safety')


class ReportStrategyProximicQuality(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicPageQuality.DIMENSION
    dimension_element = SegmentProximicPageQuality.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicPageQuality, related_name='reports_strategy_pagequality')


class ReportCampaignProximicQuality(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicPageQuality.DIMENSION
    dimension_element = SegmentProximicPageQuality.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicPageQuality, related_name='reports_campaign_pagequality')


class ReportStrategyProximicNotice(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicPageNoticeability.DIMENSION
    dimension_element = SegmentProximicPageNoticeability.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicPageNoticeability, related_name='reports_strategy_pagenoticeability')


class ReportCampaignProximicNotice(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicPageNoticeability.DIMENSION
    dimension_element = SegmentProximicPageNoticeability.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicPageNoticeability, related_name='reports_campaign_pagenoticeability')


class ReportStrategyProximicPlace(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicPagePlacement.DIMENSION
    dimension_element = SegmentProximicPagePlacement.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicPagePlacement, related_name='reports_strategy_pageplacement')


class ReportCampaignProximicPlace(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicPagePlacement.DIMENSION
    dimension_element = SegmentProximicPagePlacement.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicPagePlacement, related_name='reports_campaign_pageplacement')


class ReportStrategyProximicContext(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicContextual.DIMENSION
    dimension_element = SegmentProximicContextual.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicContextual, related_name='reports_strategy_contextual')


class ReportCampaignProximicContextual(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicContextual.DIMENSION
    dimension_element = SegmentProximicContextual.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicContextual, related_name='reports_campaign_contextual')


class ReportStrategyProximicLanguage(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicPageLanguage.DIMENSION
    dimension_element = SegmentProximicPageLanguage.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicPageLanguage, related_name='reports_strategy_pagelanguage')


class ReportCampaignProximicLanguage(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = SegmentProximicPageLanguage.DIMENSION
    dimension_element = SegmentProximicPageLanguage.DIMENSION

    dimension = ForeignKeyNull(SegmentProximicPageLanguage, related_name='reports_campaign_pagelanguage')


# ======
# Peer39
# ======


class ReportStrategyPeer39Language(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = Peer39PageLanguage.DIMENSION
    dimension_element = Peer39PageLanguage.DIMENSION

    dimension = ForeignKeyNull(Peer39PageLanguage, related_name='reports_strategy_pagelanguage')


class ReportCampaignPeer39Language(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = Peer39PageLanguage.DIMENSION
    dimension_element = Peer39PageLanguage.DIMENSION

    dimension = ForeignKeyNull(Peer39PageLanguage, related_name='reports_campaign_pagelanguage')


class ReportStrategyPeer39Brand(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = Peer39BrandProtection.DIMENSION
    dimension_element = Peer39BrandProtection.DIMENSION

    dimension = ForeignKeyNull(Peer39BrandProtection, related_name='reports_strategy_brandprotection')


class ReportCampaignPeer39Brand(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = Peer39BrandProtection.DIMENSION
    dimension_element = Peer39BrandProtection.DIMENSION

    dimension = ForeignKeyNull(Peer39BrandProtection, related_name='reports_campaign_brandprotection')


class ReportStrategyPeer39Contextual(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = Peer39ContextualSegment.DIMENSION
    dimension_element = Peer39ContextualSegment.DIMENSION

    dimension = ForeignKeyNull(Peer39ContextualSegment, related_name='reports_strategy_contextual')


class ReportCampaignPeer39Contextual(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = Peer39ContextualSegment.DIMENSION
    dimension_element = Peer39ContextualSegment.DIMENSION

    dimension = ForeignKeyNull(Peer39ContextualSegment, related_name='reports_campaign_contextual')


class ReportStrategyPeer39Quality(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = Peer39PageQuality.DIMENSION
    dimension_element = Peer39PageQuality.DIMENSION

    dimension = ForeignKeyNull(Peer39PageQuality, related_name='reports_strategy_pagequality')


class ReportCampaignPeer39Quality(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = Peer39PageQuality.DIMENSION
    dimension_element = Peer39PageQuality.DIMENSION

    dimension = ForeignKeyNull(Peer39PageQuality, related_name='reports_campaign_pagequality')


# ======
# Lotame
# ======


class ReportStrategyLotameDemographic(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = LotameDemographic.DIMENSION
    dimension_element = LotameDemographic.DIMENSION

    dimension = ForeignKeyNull(LotameDemographic, related_name='reports_strategy_lotamedemographic')


class ReportCampaignLotameDemographic(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = LotameDemographic.DIMENSION
    dimension_element = LotameDemographic.DIMENSION

    dimension = ForeignKeyNull(LotameDemographic, related_name='reports_campaign_lotamedemographic')


class ReportStrategyLotameAdvancedDemographic(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    class Meta(object):
        # Actually less verbose than class name to fit into auth's permission name varchar(50).
        verbose_name = 'report strat. lotame adv. demographics'

    objects = ReportDataProviderManager()

    dimension_hierarchy = LotameAdvancedDemographic.DIMENSION
    dimension_element = LotameAdvancedDemographic.DIMENSION

    dimension = ForeignKeyNull(LotameAdvancedDemographic, related_name='reports_strategy_lotameadvanceddemographic')


class ReportCampaignLotameAdvancedDemographic(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    class Meta(object):
        # Actually less verbose than class name to fit into auth's permission name varchar(50).
        verbose_name = 'report camp. lotame adv. demographics'

    objects = ReportDataProviderManager()

    dimension_hierarchy = LotameAdvancedDemographic.DIMENSION
    dimension_element = LotameAdvancedDemographic.DIMENSION

    dimension = ForeignKeyNull(LotameAdvancedDemographic, related_name='reports_campaign_lotameadvanceddemographic')


class ReportStrategyLotameBehavioralInterest(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    class Meta(object):
        # Actually less verbose than class name to fit into auth's permission name varchar(50).
        verbose_name = 'report strat. lotame behav. interest'

    objects = ReportDataProviderManager()

    dimension_hierarchy = LotameBehavioralInterest.DIMENSION
    dimension_element = LotameBehavioralInterest.DIMENSION

    dimension = ForeignKeyNull(LotameBehavioralInterest, related_name='reports_strategy_lotamebehavioralinterest')


class ReportCampaignLotameBehavioralInterest(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    class Meta(object):
        # Actually less verbose than class name to fit into auth's permission name varchar(50).
        verbose_name = 'report camp. lotame behav. interest'

    objects = ReportDataProviderManager()

    dimension_hierarchy = LotameBehavioralInterest.DIMENSION
    dimension_element = LotameBehavioralInterest.DIMENSION

    dimension = ForeignKeyNull(LotameBehavioralInterest, related_name='reports_campaign_lotamebehavioralinterest')


class ReportStrategyLotameInfluencers(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = LotameInfluencers.DIMENSION
    dimension_element = LotameInfluencers.DIMENSION

    dimension = ForeignKeyNull(LotameInfluencers, related_name='reports_strategy_lotameinfluencers')


class ReportCampaignLotameInfluencers(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = LotameInfluencers.DIMENSION
    dimension_element = LotameInfluencers.DIMENSION

    dimension = ForeignKeyNull(LotameInfluencers, related_name='reports_campaign_lotameinfluencers')


class ReportStrategyLotameOffline(BaseMultivalueReport, BaseReportDimension, BaseReportStrategy):

    objects = ReportDataProviderManager()

    dimension_hierarchy = LotameOffline.DIMENSION
    dimension_element = LotameOffline.DIMENSION

    dimension = ForeignKeyNull(LotameOffline, related_name='reports_strategy_lotameoffline')


class ReportCampaignLotameOffline(BaseMultivalueReport, BaseReportDimension, BaseReportCampaign):

    objects = ReportDataProviderManager()

    dimension_hierarchy = LotameOffline.DIMENSION
    dimension_element = LotameOffline.DIMENSION

    dimension = ForeignKeyNull(LotameOffline, related_name='reports_campaign_lotameoffline')
