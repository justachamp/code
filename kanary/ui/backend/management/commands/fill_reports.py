from optparse import make_option
import inspect
from datetime import datetime, timedelta
from adserving.types import Decimal
import random
from random import randint

from django.db import transaction
from django.core.management.base import BaseCommand


from etc import dimensions
from etc.constants import COMMISSION, HIDDEN_COMMISSION

from ui.account.models import Account

from ui.bidding_spendings.models import DailySpendings

from ui.campaign.models import Campaign

from ui.targeting.models import (
    PublisherTargetValue, TargetValue, ContentCategoryValue,
    SegmentProximicMaturityRating, SegmentProximicSafetyLevel, SegmentProximicPageQuality,
    SegmentProximicPageNoticeability, SegmentProximicPagePlacement, SegmentProximicContextual,
    SegmentProximicPageLanguage,
    Peer39PageLanguage, Peer39BrandProtection, Peer39ContextualSegment, Peer39PageQuality,
    LotameDemographic, LotameAdvancedDemographic, LotameBehavioralInterest,
    LotameInfluencers, LotameOffline,
)

import ui.report.models as RM
from ui.report.models import BaseReport, ReportCampaign, ReportStrategy, ReportAdvert

DEFAULT_DATA_COST_RANGE = (1, 3)
DEFAULT_BID_CPM_RANGE = (40, 70)
DEFAULT_CTR_RANGE = (4, 9)
DEFAULT_CONV_RATE_RANGE = (5, 10)
DEFAULT_CONV_VALUE_RANGE = (1, 30)
DEFAULT_PERIOD_HOURS = 6


def filter_by_key(key, target_values):
    """Filter a list of target values by their keys"""
    return filter(lambda t: t.key == key, target_values)


def get_report_classes():
    """Return a list of classes that store reports"""
    classes = []

    report_models = 'ui.report.models'
    report_module = __import__(report_models, globals(), locals(), -1)
    for cls_name in dir(report_module):
        cls = getattr(report_module, cls_name)
        if inspect.isclass(cls) and issubclass(cls, BaseReport) and not cls._meta.abstract:
            classes.append(cls)
    return classes


def campaign_time_spent_ratio(campaign):
    """
    Calculate part of campaign that has elapsed

    :return: Ratio between 0.0 and 1.0
    :rtype: Decimal
    """
    campaign_duration = int((campaign.end_UTC - campaign.start_UTC).total_seconds())
    campaign_elapsed = int((datetime.utcnow() - campaign.start_UTC).total_seconds())
    if campaign_elapsed < 0:
        return Decimal(0)
    return Decimal(campaign_elapsed) / campaign_duration


def count_periods_in_daterange(start, end, period):
    """
    Counts how many full periods are within given daterange.

    :param datetime.datetime start: beginning of daterange
    :param datetime.datetime end: end of daterange
    :param datetime.timedelta: period to count
    :rtype: int
    """
    return int((end - start).total_seconds() / period.total_seconds())


def distribute_sum_randomly(n, total):
    """
    Return a randomly chosen list of n numbers summing to total.
    Depends on total type values will be integers or Decimals.

    Examples:
    >>> distribute_sum_randomly(5, 100)
    >>> [5, 21, 57, 13, 4]

    >>> distribute_sum_randomly(3, Decimal('84.65'))
    >>> [Decimal('41.94'), Decimal('27.15'), Decimal('15.56')]
    """
    if total == 0 or total == Decimal('0'):
        return [total for i in xrange(0, n)]

    dividers = []
    for i in xrange(1, n):
        if isinstance(total, int):
            divider = random.randint(1, total)
        else:
            divider_decimal = random.random() * float(total)
            divider = Decimal('%f' % divider_decimal)
        dividers.append(divider)

    dividers.sort()

    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]


@transaction.atomic
class Command(BaseCommand):
    help = """QA and dev command to insert example reports into database."""

    option_list = BaseCommand.option_list + (
        make_option(
            '--min-data-cost',
            action='store',
            dest='min-data-cost',
            default=DEFAULT_DATA_COST_RANGE[0],
            help='Minimum %% of data cost within range <0, 100>'),
        make_option(
            '--max-data-cost',
            action='store',
            dest='max-data-cost',
            default=DEFAULT_DATA_COST_RANGE[1],
            help='Maximum %% of data cost within range <0, 100>'),
        make_option(
            '--min-bid-cpm',
            action='store',
            dest='min-bid-cpm',
            default=DEFAULT_BID_CPM_RANGE[0],
            help='Minimum %% of bid cpm within range <0, 100>'),
        make_option(
            '--max-bid-cpm',
            action='store',
            dest='max-bid-cpm',
            default=DEFAULT_BID_CPM_RANGE[1],
            help='Maximum %% of bid cpm within range <0, 100>'),
        make_option(
            '--min-ctr',
            action='store',
            dest='min-ctr',
            default=DEFAULT_CTR_RANGE[0],
            help='Minimum %% of ctr within range <0, 100>'),
        make_option(
            '--max-ctr',
            action='store',
            dest='max-ctr',
            default=DEFAULT_CTR_RANGE[1],
            help='Maximum %% of ctr within range <0, 100>'),
        make_option(
            '--min-conv-rate',
            action='store',
            dest='min-conv-rate',
            default=DEFAULT_CONV_RATE_RANGE[0],
            help='Minimum %% of conversion rate within range <0, 100>'),
        make_option(
            '--max-conv-rate',
            action='store',
            dest='max-conv-rate',
            default=DEFAULT_CONV_RATE_RANGE[1],
            help='Maximum %% of conversion rate within range <0, 100>'),
        make_option(
            '--min-conv-value',
            action='store',
            dest='min-conv-value',
            default=DEFAULT_CONV_VALUE_RANGE[0],
            help='Minimum %% of conversion value within range <0, 100>'),
        make_option(
            '--max-conv-value',
            action='store',
            dest='max-conv-value',
            default=DEFAULT_CONV_VALUE_RANGE[1],
            help='Maximum %% of conversion value within range <0, 100>'),
        make_option(
            '--period-hours',
            action='store',
            dest='period-hours',
            default=DEFAULT_PERIOD_HOURS,
            help='Time between report entries'),
    )

    @transaction.atomic
    def handle(self, *args, **opt):
        range_params = [
            ('DATA_COST_RANGE', 'min-data-cost', 'max-data-cost'),
            ('BID_CPM_RANGE', 'min-bid-cpm', 'max-bid-cpm'),
            ('CTR_RANGE', 'min-ctr', 'max-ctr'),
            ('CONV_RATE_RANGE', 'min-conv-rate', 'max-conv-rate'),
            ('CONV_VALUE_RANGE', 'min-conv-value', 'max-conv-value')
        ]

        self.options = {}
        for option, min_value, max_value in range_params:
            self.options[option] = (int(opt[min_value]), int(opt[max_value]))

        self.options['PERIOD_HOURS'] = int(opt['period-hours'])

        self.stdout.write('Deleting existing reports')
        self.clean_reports()
        self.stdout.write('Filling database with reports')
        self.fill_reports()

    def clean_reports(self):
        """Remove all reports from database"""
        report_classes = get_report_classes()

        for report_class in report_classes:
            report_class.objects.all().delete()

    def fill_reports(self):
        """Fake reports for running and finished campaigns"""

        for campaign in filter(lambda c: not c.state.scheduled, Campaign.objects.all()):
            self.fake_campaign_report(campaign)

        today = datetime.utcnow().date()
        account = Account.objects.first()
        for ago in range(0, 5):
            date = today - timedelta(days=ago)
            budget_spent = randint(100, 300)
            audit_fees = random.random() * 3

            kanary_commission = budget_spent * COMMISSION / (1 + COMMISSION)
            hidden_commission = (budget_spent - kanary_commission) * HIDDEN_COMMISSION / (1 + HIDDEN_COMMISSION)

            data_cost_proximic = random.random() * randint(1, 5)
            data_cost_peer39 = random.random() * randint(1, 5)
            data_cost_lotame = random.random() * randint(1, 5)

            DailySpendings.objects.create(date=date, account=account, budget_spent=budget_spent, audit_fees=audit_fees,
                hidden_commission=hidden_commission, kanary_commission=kanary_commission,
                data_cost_proximic=data_cost_proximic, data_cost_peer39=data_cost_peer39,
                data_cost_lotame=data_cost_lotame)

    def fake_campaign_report(self, campaign):
        """Fake all reports related to Campaign and Strategy model for a single campaign"""

        def total_spent(metrics_dict):
            return (metrics_dict['imp_value']
                    + metrics_dict['data_cost_value']
                    + metrics_dict['commission_value'])

        campaign_time_spent = Decimal(campaign_time_spent_ratio(campaign))
        campaign_budget_left = campaign.budget_total * campaign_time_spent

        campaign_metrics = {
            'imp': 0,
            'imp_value': Decimal('0'),
            'clk': 0,
            'conv': 0,
            'conv_value': Decimal('0'),
            'data_cost_value': Decimal('0'),
            'commission_value': Decimal('0'),
        }

        for strategy in campaign.strategy_set.all():
            strategy_spent = strategy.budget_total * campaign_time_spent
            effective_spent = min(campaign_budget_left, strategy_spent)

            strategy_metrics = self.fake_strategy_report(strategy, effective_spent)

            if strategy_metrics:
                reported_spent = total_spent(strategy_metrics)
                campaign_budget_left -= reported_spent
                strategy.budget_spent = reported_spent
                strategy.save()

                for metric, value in strategy_metrics.iteritems():
                    campaign_metrics[metric] += value

        campaign_spent = total_spent(campaign_metrics)

        campaign.budget_spent = campaign_spent
        campaign.save()

        self.create_campaign_reports(campaign, campaign_metrics)

    def get_randomized_metrics(self, budget, base_cpm):
        """
        Generate basic metrics values within ranges provided in configuration

        :return: values for BASE_METRICS
        :rtype: dict
        """

        conf = self.options
        commission_value = budget / (Decimal(1) + COMMISSION)
        inventory_cost = budget - commission_value
        data_cost_value = randint(
            *conf['DATA_COST_RANGE']) / Decimal(100) * inventory_cost
        imp_value = inventory_cost - data_cost_value
        cpm = randint(*conf['BID_CPM_RANGE']) / Decimal(100) * base_cpm
        imp = imp_value * 1000 / cpm
        ctr = randint(*conf['CTR_RANGE']) / Decimal(100)
        clk = imp * ctr
        conv_rate = randint(*conf['CONV_RATE_RANGE']) / Decimal(100)
        conv = clk * conv_rate
        conv_value = conv * randint(*conf['CONV_VALUE_RANGE']) / Decimal(100)

        return {
            'imp': imp.quantize(Decimal('1')),
            'imp_value': imp_value,
            'clk': clk.quantize(Decimal('1')),
            'conv': conv.quantize(Decimal('1')),
            'conv_value': conv_value,
            'data_cost_value': data_cost_value,
            'commission_value': commission_value,
        }

    def fake_strategy_report(self, strategy, budget):
        """
        Fake all reports related to Strategy model for a single strategy

        :return: sums of faked simple metrics like {'imp': 100, }
        :rtype dict:
        """

        audited_adverts = filter(lambda a: a.state.audited, strategy.advert_set.all())

        advert_count = len(audited_adverts)

        if not advert_count:
            return

        metrics = self.get_randomized_metrics(budget, strategy.budget_bid_CPM)

        metrics_per_advert = {}
        for metric, value in metrics.iteritems():
            metrics_per_advert[metric] = value / advert_count

        for int_metric in ['imp', 'clk', 'conv']:
            metrics_per_advert[int_metric] = int(metrics_per_advert[int_metric])

        start = strategy.campaign.start_UTC
        end = min(datetime.utcnow(), strategy.campaign.end_UTC)

        for advert in audited_adverts:
            self.fake_report(advert, ReportAdvert, start, end, **metrics_per_advert)

        metrics_per_advert = {
            'imp': int(metrics['imp'] / advert_count),
            'imp_value': (metrics['imp_value'] / advert_count),
            'clk': int(metrics['clk'] / advert_count),
            'conv': int(metrics['conv'] / advert_count),
            'conv_value': metrics['conv_value'] / advert_count,
            'data_cost_value': metrics['data_cost_value'] / advert_count,
            'commission_value': metrics['commission_value'] / advert_count
        }

        overall_metrics = {}
        for metric, per_advert_value in metrics_per_advert.iteritems():
            overall_metrics[metric] = per_advert_value * advert_count

        self.create_strategy_reports(
            strategy,
            overall_metrics
        )

        return overall_metrics

    def create_campaign_reports(self, campaign, metrics):
        start = campaign.start_UTC
        end = min(datetime.utcnow(), campaign.end_UTC)
        self.fake_report(campaign, ReportCampaign, start, end, **metrics)

        for model, dimension in [
            (RM.ReportCampaignOs, dimensions.g_os),
            (RM.ReportCampaignCarrier, dimensions.carrier),
            (RM.ReportCampaignDomain, dimensions.domain),
            (RM.ReportCampaignPosition, dimensions.position),
            (RM.ReportCampaignAge, dimensions.age_group),
            (RM.ReportCampaignGender, dimensions.gender),
        ]:
            self.fake_report(
                campaign,
                model,
                start,
                end,
                dimensions=list(TargetValue.objects.filter(category=dimension, representant=None)) + [None],
                **metrics
            )

        devices = TargetValue.objects.filter(category=dimensions.g_device)
        locations = TargetValue.objects.filter(category=dimensions.g_location)
        publishers = PublisherTargetValue.objects.all()

        for model, target_values in [
            (RM.ReportCampaignCountry, filter_by_key(dimensions.country, locations)),
            (RM.ReportCampaignRegion, filter_by_key(dimensions.region, locations)),
            (RM.ReportCampaignCity, filter_by_key(dimensions.city, locations)),
            (RM.ReportCampaignPublisher, filter_by_key(dimensions.publisher_name, publishers)),
            (RM.ReportCampaignPublisherNetwork, filter_by_key(dimensions.network, publishers)),
            (RM.ReportCampaignMake, filter_by_key(dimensions.make, devices)),
            (RM.ReportCampaignModel, filter_by_key(dimensions.model, devices))
        ]:
            self.fake_report(
                campaign,
                model,
                start,
                end,
                dimensions=target_values + [None],
                **metrics
            )

        self.fake_report(
            campaign,
            RM.ReportCampaignSite,
            start,
            end,
            dimensions=['http://foo.com', 'http://bar.net', 'http://baz.org', None],
            **metrics
        )

        for dimension_model, report_model in [
            (SegmentProximicMaturityRating, RM.ReportCampaignProximicMaturity),
            (SegmentProximicSafetyLevel, RM.ReportCampaignProximicSafety),
            (SegmentProximicPageQuality, RM.ReportCampaignProximicQuality),
            (SegmentProximicPageNoticeability, RM.ReportCampaignProximicNotice),
            (SegmentProximicPagePlacement, RM.ReportCampaignProximicPlace),
            (SegmentProximicPageLanguage, RM.ReportCampaignProximicLanguage),
            (Peer39PageLanguage, RM.ReportCampaignPeer39Language),
            (Peer39BrandProtection, RM.ReportCampaignPeer39Brand),
        ]:
            self.fake_report(
                campaign,
                report_model,
                start,
                end,
                dimensions=list(dimension_model.objects.all()) + [None],
                **metrics
            )

        for dimension_model, report_model in [
            (ContentCategoryValue, RM.ReportCampaignCategory),
            (SegmentProximicContextual, RM.ReportCampaignProximicContextual),
            (Peer39ContextualSegment, RM.ReportCampaignPeer39Contextual),
            (Peer39PageQuality, RM.ReportCampaignPeer39Quality),
            (LotameDemographic, RM.ReportCampaignLotameDemographic),
            (LotameAdvancedDemographic, RM.ReportCampaignLotameAdvancedDemographic),
            (LotameBehavioralInterest, RM.ReportCampaignLotameBehavioralInterest),
            (LotameInfluencers, RM.ReportCampaignLotameInfluencers),
            (LotameOffline, RM.ReportCampaignLotameOffline),
        ]:
            self.fake_report(
                campaign,
                report_model,
                start,
                end,
                dimensions=list(dimension_model.objects.all()[:10]) + [None],
                **metrics
            )

    def create_strategy_reports(self, strategy, metrics):
        start = strategy.campaign.start_UTC
        end = min(datetime.utcnow(), strategy.campaign.end_UTC)
        self.fake_report(strategy, ReportStrategy, start, end, **metrics)

        for model in [
            RM.ReportStrategyOs,
            RM.ReportStrategyCarrier,
            RM.ReportStrategyDomain,
            RM.ReportStrategyPosition,
            RM.ReportStrategyAge,
            RM.ReportStrategyGender,
        ]:
            self.fake_report(
                strategy,
                model,
                start,
                end,
                dimensions=list(
                    TargetValue.objects.filter(category=model.dimension_hierarchy, representant=None)) + [None],
                **metrics
            )

        devices = TargetValue.objects.filter(category=dimensions.g_device)
        locations = TargetValue.objects.filter(category=dimensions.g_location)
        publishers = PublisherTargetValue.objects.all()
        for model, target_values in [
            (RM.ReportStrategyCountry, filter_by_key(dimensions.country, locations)),
            (RM.ReportStrategyRegion, filter_by_key(dimensions.region, locations)),
            (RM.ReportStrategyCity, filter_by_key(dimensions.city, locations)),
            (RM.ReportStrategyPublisher, filter_by_key(dimensions.publisher_name, publishers)),
            (RM.ReportStrategyPublisherNetwork, filter_by_key(dimensions.network, publishers)),
            (RM.ReportStrategyMake, filter_by_key(dimensions.make, devices)),
            (RM.ReportStrategyModel, filter_by_key(dimensions.model, devices))
        ]:
            self.fake_report(
                strategy,
                model,
                start,
                end,
                dimensions=target_values + [None],
                **metrics
            )

        self.fake_report(
            strategy,
            RM.ReportStrategySite,
            start,
            end,
            dimensions=['http://foo.com', 'http://bar.net', 'http://baz.org', None],
            **metrics
        )

        for dimension_model, report_model in [
            (SegmentProximicMaturityRating, RM.ReportStrategyProximicMaturity),
            (SegmentProximicSafetyLevel, RM.ReportStrategyProximicSafety),
            (SegmentProximicPageQuality, RM.ReportStrategyProximicQuality),
            (SegmentProximicPageNoticeability, RM.ReportStrategyProximicNotice),
            (SegmentProximicPagePlacement, RM.ReportStrategyProximicPlace),
            (SegmentProximicPageLanguage, RM.ReportStrategyProximicLanguage),
            (Peer39PageLanguage, RM.ReportStrategyPeer39Language),
            (Peer39BrandProtection, RM.ReportStrategyPeer39Brand),
        ]:
            self.fake_report(
                strategy,
                report_model,
                start,
                end,
                dimensions=list(dimension_model.objects.all()) + [None],
                **metrics
            )

        for dimension_model, report_model in [
            (ContentCategoryValue, RM.ReportStrategyCategory),
            (SegmentProximicContextual, RM.ReportStrategyProximicContext),
            (Peer39ContextualSegment, RM.ReportStrategyPeer39Contextual),
            (Peer39PageQuality, RM.ReportStrategyPeer39Quality),
            (LotameDemographic, RM.ReportStrategyLotameDemographic),
            (LotameAdvancedDemographic, RM.ReportStrategyLotameAdvancedDemographic),
            (LotameBehavioralInterest, RM.ReportStrategyLotameBehavioralInterest),
            (LotameInfluencers, RM.ReportStrategyLotameInfluencers),
            (LotameOffline, RM.ReportStrategyLotameOffline),
        ]:
            self.fake_report(
                strategy,
                report_model,
                start,
                end,
                dimensions=list(dimension_model.objects.all()[:10]) + [None],
                **metrics
            )

    def fake_report(
            self, reported_obj, report_class, start, end,
            imp, imp_value, clk, conv, conv_value, data_cost_value, commission_value,
            dimensions=None):
        """
        Creates report with fake data for a provided model instance and distributes metrics values
        within created set.

        :param (Campaign, Strategy, Advert) reported_obj: reported Django Model instance
        :param BaseReport: report class
        :param datetime start: start of report data
        :param datetime end: end of report data
        :param int imp: total number of impressions in report
        :param Decimal imp_value: total value of impressions in report
        :param int clk: total number of clicks in report
        :param int conv: total number of conversions in report
        :param Decimal conv_value: total value of conversions in report
        :param Decimal data_cost_value: total value of data cost in report
        :param Decimal commision_value: total value of commision in report.
        :param list dimensions: list of dimensions (target values) to include in the report (or None)
        """
        period = timedelta(hours=self.options['PERIOD_HOURS'])
        periods_count = count_periods_in_daterange(start, end, period)
        key_metric_mapping = [
            ('imp', imp),
            ('imp_value', imp_value),
            ('clk', clk),
            ('conv', conv),
            ('conv_value', conv_value),
            ('data_cost_value', data_cost_value),
            ('commission_value', commission_value)
        ]
        # stores lists with metrics values for each metric and period
        values_per_period = {}

        # count values of each metric in each period
        for key, metric_value in key_metric_mapping:
            values_per_period.update({key: distribute_sum_randomly(periods_count, metric_value)})

        if not dimensions:
            dimensions = [None]

        # distribute metric values for each period for all dimensions
        for key, metric_value_list in values_per_period.iteritems():
            values_per_period[key] = map(
                lambda m: distribute_sum_randomly(len(dimensions), m),
                metric_value_list
            )

        for dimension_number in xrange(0, len(dimensions)):
            for period_number in xrange(0, periods_count):
                report_time = start + (period * period_number)

                report = report_class(
                    time=report_time,
                    imp_value=values_per_period['imp_value'][period_number][dimension_number],
                    imp=values_per_period['imp'][period_number][dimension_number],
                    clk=values_per_period['clk'][period_number][dimension_number],
                    conv=values_per_period['conv'][period_number][dimension_number],
                    conv_value=values_per_period['conv_value'][period_number][dimension_number],
                    data_cost_value=values_per_period['data_cost_value'][period_number][dimension_number],
                    commission_value=values_per_period['commission_value'][period_number][dimension_number]
                )
                if dimensions[0] is not None:
                    report.dimension = dimensions[dimension_number]

                report.related = reported_obj
                report.save()
