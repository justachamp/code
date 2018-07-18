"""
Test:
 - derivative metrics on-the-fly calculation
 - report query identity
  - for simple reports (1 expression in WHERE)
  - for dimension reports (2 exprs), where dimension may be a string or a FK
 - table aggregation
 - chart granulation
 - table sorting
"""
from datetime import datetime, timedelta, date

import pytest
import simplejson
from django.core.urlresolvers import reverse
from django.db.models import Sum

from etc import dimensions
from adserving.types import Decimal, map_to_decimal
from ui.report.models import (
    ReportAdvert, ReportStrategy,
    ReportStrategyOs, ReportCampaignOs,
    ReportStrategyModel, ReportCampaignModel, ReportStrategyMake, ReportCampaignMake,
    ReportStrategyCountry, ReportCampaignCountry, ReportStrategyRegion, ReportCampaignRegion,
    ReportStrategyCity, ReportCampaignCity, ReportStrategyCarrier, ReportCampaignCarrier,
    ReportStrategyDomain, ReportCampaignDomain, ReportStrategyGender, ReportCampaignGender,
    ReportStrategyAge, ReportCampaignAge, ReportStrategyPosition, ReportCampaignPosition,
    ReportStrategyPublisherNetwork, ReportCampaignPublisherNetwork, ReportStrategyPublisher, ReportCampaignPublisher,
    ReportStrategySite, ReportCampaignSite, ReportStrategyCategory, ReportCampaignCategory,
    ReportStrategyProximicMaturity, ReportCampaignProximicMaturity,
    ReportStrategyProximicSafety, ReportCampaignProximicSafety,
    ReportStrategyProximicQuality, ReportCampaignProximicQuality,
    ReportStrategyProximicNotice, ReportCampaignProximicNotice,
    ReportStrategyProximicPlace, ReportCampaignProximicPlace,
    ReportStrategyProximicContext, ReportCampaignProximicContextual,
    ReportStrategyProximicLanguage, ReportCampaignProximicLanguage,
    ReportStrategyPeer39Language, ReportCampaignPeer39Language,
    ReportStrategyPeer39Brand, ReportCampaignPeer39Brand,
    ReportStrategyPeer39Contextual, ReportCampaignPeer39Contextual,
    ReportStrategyPeer39Quality, ReportCampaignPeer39Quality,
    ReportStrategyLotameDemographic, ReportCampaignLotameDemographic,
    ReportStrategyLotameAdvancedDemographic, ReportCampaignLotameAdvancedDemographic,
    ReportStrategyLotameBehavioralInterest, ReportCampaignLotameBehavioralInterest,
    ReportStrategyLotameInfluencers, ReportCampaignLotameInfluencers,
    ReportStrategyLotameOffline, ReportCampaignLotameOffline,
)
from ui.campaign.models import Advert, Strategy, Campaign
from ui.targeting.models import TargetValue, LotameBehavioralInterest, LotameBase
from ui.tests.initial_datafixtures import default_strategies, default_user
from ui.utils import url_with_querystring


DT0 = datetime(2014, 4, 1, 16)
DT1 = datetime(2014, 4, 1, 19)
DT2 = datetime(2014, 4, 2, 11)

REPORT_DATA = (
    # dt   data_cost  imp  imp_value  clk     conv  conv_value
    # _total                   _value
    (DT0, 10, 47, 120, 15, 5, 60),
    (DT1, 35, 30, 160, 80, 90, 7),
    (DT2, 7, 29, 80, 10, 2, 22),
)


def db_round(dec):
    '''
    Return decimal rounded to the precision that tolerates cummulative
    differences of precision in Python and Postgres.
    '''
    prec = Decimal('1e-14')  # Use precision that is 'good enough'.
    return dec.quantize(prec)


@pytest.mark.parametrize('report_class, related_class, related_object_attr', (
        (ReportAdvert, Advert, 'strategy'),
        (ReportStrategy, Strategy, 'campaign')
))
@pytest.mark.parametrize('imp_value, commission_value, data_cost_value', map_to_decimal([
    (0, 0, 0),
    (432, '87.54', 20),
]))
@pytest.mark.parametrize('imp, clk', map_to_decimal([
    (0, 0),
    (40, 30)
]))
@pytest.mark.parametrize('conv, conv_value', map_to_decimal([
    (0, 0),
    (15, 231414),
]))
def test_derivative_metrics(state_app, report_class, related_class,
                            related_object_attr, imp_value,
                            imp, clk, conv, conv_value,
                            commission_value, data_cost_value):
    imp_value_total = imp_value + commission_value + data_cost_value
    net_earned = conv_value - imp_value_total

    report = report_class(
        time=datetime.utcnow(),
        imp=imp,
        imp_value=imp_value,
        clk=clk,
        conv=conv,
        conv_value=conv_value,
        commission_value=commission_value,
        data_cost_value=data_cost_value
    )
    report.related = related_class.objects.first()
    report.save()

    aggregation = report_class.objects.report_table(
        related_obj=getattr(report.related, related_object_attr),
        sort_by='imp'
    )

    assert len(aggregation) == 1

    report_data = aggregation[0]

    ecpm = ctr = ecpc = ecpa = conv_rate = roi = Decimal(0)

    if imp_value:
        roi = (conv_value - imp_value_total) / imp_value_total * 100

    if clk:
        ecpc = imp_value_total / clk
        conv_rate = conv / clk * 100

    if imp:
        ecpm = imp_value_total / imp * 1000
        ctr = clk / imp * 100

    if conv:
        ecpa = imp_value_total / conv

    prec = Decimal('1.0000000')

    for metric in ['ecpc', 'ecpa', 'ecpm', 'ctr', 'conv_rate', 'roi', 'net_earned']:
        a = report_data[metric].quantize(prec)
        b = locals().get(metric).quantize(prec)
        assert a == b


@pytest.mark.parametrize('report_class, related_class, related_object_attr', (
        (ReportAdvert, Advert, 'strategy'),
        (ReportStrategy, Strategy, 'campaign')
))
@pytest.mark.parametrize('imp_value, imp_value_total, data_cost_value', map_to_decimal([
    ((0, 0), (0, 0), (0, 0)),
    ((432, 320), (444, 356), (12, 36)),
]))
@pytest.mark.parametrize('imp, clk', map_to_decimal([
    ((0, 0), (0, 0)),
    ((40, 30), (30, 15))
]))
@pytest.mark.parametrize('conv, conv_value', map_to_decimal([
    ((0, 0), (0, 0)),
    ((15, 3), (231414, 123)),
]))
def test_aggregate_correctnes(state_app, report_class, related_class,
                              related_object_attr, imp_value,
                              imp, clk, conv, conv_value,
                              imp_value_total, data_cost_value):
    now = datetime.utcnow()
    later = now + timedelta(hours=1, minutes=13)
    related = related_class.objects.first()
    report1 = report_class(
        time=now, imp_value=imp_value[0], imp=imp[0],
        clk=clk[0], conv=conv[0], conv_value=conv_value[0],
        data_cost_value=data_cost_value[0])
    report1.related = related
    report1.save()

    report2 = report_class(
        time=later, imp_value=imp_value[1], imp=imp[1],
        clk=clk[1], conv=conv[1], conv_value=conv_value[1],
        data_cost_value=data_cost_value[1])
    report2.related = related
    report2.save()

    aggregation = report_class.objects.report_table(
        related_obj=getattr(related, related_object_attr),
        start_date=date.today(),
        end_date=date.today() + timedelta(days=1),
        sort_by='imp',
    )
    assert len(aggregation) == 1
    report_data = aggregation[0]

    # All values needs to be cast to string, due to different precision
    # available, and the fact, that sometimes, I got a little more digits
    # when casting Decimal to float, than from operations on floats alone

    ecpm = ctr = ecpc = conv_rate = roi = Decimal(0)

    if sum(imp_value_total):
        numerator = sum(conv_value) - sum(imp_value_total)
        denominator = sum(imp_value_total)
        roi = (numerator / denominator) * 100

    if sum(clk):
        ecpc = sum(imp_value_total) / sum(clk)
        conv_rate = (sum(conv) / sum(clk)) * 100

    if sum(imp):
        ecpm = (sum(imp_value_total) / sum(imp)) * 1000
        ctr = (sum(clk) / sum(imp)) * 100

    assert db_round(report_data['ecpm']) == db_round(ecpm)
    assert db_round(report_data['ctr']) == db_round(ctr)
    assert db_round(report_data['ecpc']) == db_round(ecpc)
    assert db_round(report_data['conv_rate']) == db_round(conv_rate)
    assert db_round(report_data['roi']) == db_round(roi)


@pytest.mark.parametrize('report_class, related_class', (
        (ReportStrategyOs, Strategy),
        (ReportCampaignOs, Campaign),
        (ReportStrategyModel, Strategy),
        (ReportCampaignModel, Campaign),
        (ReportStrategyMake, Strategy),
        (ReportCampaignMake, Campaign),
        (ReportStrategyCountry, Strategy),
        (ReportCampaignCountry, Campaign),
        (ReportStrategyRegion, Strategy),
        (ReportCampaignRegion, Campaign),
        (ReportStrategyCity, Strategy),
        (ReportCampaignCity, Campaign),
        (ReportStrategyCarrier, Strategy),
        (ReportCampaignCarrier, Campaign),
        (ReportStrategyDomain, Strategy),
        (ReportCampaignDomain, Campaign),
        (ReportStrategyGender, Strategy),
        (ReportCampaignGender, Campaign),
        (ReportStrategyAge, Strategy),
        (ReportCampaignAge, Campaign),
        (ReportStrategyPosition, Strategy),
        (ReportCampaignPosition, Campaign),
        (ReportStrategyPublisherNetwork, Strategy),
        (ReportCampaignPublisherNetwork, Campaign),
        (ReportStrategyPublisher, Strategy),
        (ReportCampaignPublisher, Campaign),
        (ReportStrategySite, Strategy),
        (ReportCampaignSite, Campaign),
        (ReportStrategyCategory, Strategy),
        (ReportCampaignCategory, Campaign),
        (ReportStrategyProximicMaturity, Strategy),
        (ReportCampaignProximicMaturity, Campaign),
        (ReportStrategyProximicSafety, Strategy),
        (ReportCampaignProximicSafety, Campaign),
        (ReportStrategyProximicQuality, Strategy),
        (ReportCampaignProximicQuality, Campaign),
        (ReportStrategyProximicNotice, Strategy),
        (ReportCampaignProximicNotice, Campaign),
        (ReportStrategyProximicPlace, Strategy),
        (ReportCampaignProximicPlace, Campaign),
        (ReportStrategyProximicContext, Strategy),
        (ReportCampaignProximicContextual, Campaign),
        (ReportStrategyProximicLanguage, Strategy),
        (ReportCampaignProximicLanguage, Campaign),
        (ReportStrategyPeer39Language, Strategy),
        (ReportCampaignPeer39Language, Campaign),
        (ReportStrategyPeer39Brand, Strategy),
        (ReportCampaignPeer39Brand, Campaign),
        (ReportStrategyPeer39Contextual, Strategy),
        (ReportCampaignPeer39Contextual, Campaign),
        (ReportStrategyPeer39Quality, Strategy),
        (ReportCampaignPeer39Quality, Campaign),
        (ReportStrategyLotameDemographic, Strategy),
        (ReportCampaignLotameDemographic, Campaign),
        (ReportStrategyLotameAdvancedDemographic, Strategy),
        (ReportCampaignLotameAdvancedDemographic, Campaign),
        (ReportStrategyLotameBehavioralInterest, Strategy),
        (ReportCampaignLotameBehavioralInterest, Campaign),
        (ReportStrategyLotameInfluencers, Strategy),
        (ReportCampaignLotameInfluencers, Campaign),
        (ReportStrategyLotameOffline, Strategy),
        (ReportCampaignLotameOffline, Campaign),
))
def test_report_unknown(state_app, report_class, related_class):
    """Simple test for unknown aggregation."""
    IMPS = 20
    now = datetime.utcnow()
    later = now + timedelta(hours=1, minutes=13)
    related = related_class.objects.first()
    report_class.objects.create(
        time=now, imp_value=1, imp=IMPS, related_id=related.id_random
    )
    report_class.objects.create(
        time=later, imp_value=1, imp=IMPS, related_id=related.id_random
    )

    [report] = report_class.objects.report_table(related)
    assert report['label'] is None
    assert report['imp'] == IMPS * 2, "Should aggregate from two report entries"


@pytest.mark.parametrize('report_class, related_class, related_obj_attr', (
        (ReportAdvert, Advert, 'strategy'),
        (ReportStrategy, Strategy, 'campaign'),
))
def test_aggregate_dateranges(state_app, report_class, related_class, related_obj_attr):
    related = related_class.objects.first()

    for (dt, data_cost_value, imp, imp_value, clk, conv, conv_value) in REPORT_DATA:
        report = report_class(
            time=dt,
            imp=imp,
            imp_value=imp_value,
            clk=clk,
            conv=conv,
            conv_value=conv_value,
            data_cost_value=data_cost_value,
        )
        report.related = related
        report.save()

    def check_aggregation(start_date, end_date, imp, imp_vt):
        '''
        asserts imp and imp_value_total
        '''

        [aggregation] = report_class.objects.report_table(
            related_obj=getattr(related, related_obj_attr),
            sort_by='imp',
            start_date=start_date,
            end_date=end_date,
        )

        assert aggregation['imp'] == imp
        assert aggregation['imp_value_total'] == imp_vt

    # DATERANGE: 2014-04-01 - 2014-04-01
    check_aggregation(
        start_date=DT0.date(),
        end_date=DT0.date(),
        imp=Decimal('77'),
        imp_vt=Decimal('325'),
    )

    # DATERANGE: 2014-04-01 - 2014-04-02
    check_aggregation(
        start_date=DT0.date(),
        end_date=DT2.date(),
        imp=Decimal('106'),
        imp_vt=Decimal('412'),
    )


@pytest.mark.parametrize('report_model, dimension_factory', [
    (ReportCampaignSite, lambda: 'http://konik.org/'),
    (ReportCampaignSite, lambda: None),
    (ReportCampaignOs, lambda: TargetValue.objects.create_representant('appnexus', dimensions.g_os, ['GNU', 'HURD'])),
    (ReportCampaignOs, lambda: None),
    (
            ReportCampaignLotameBehavioralInterest,
            lambda: LotameBehavioralInterest.objects.create(
                appnexus_id=222222, lotame_id=1111221,
                name='Users who expressed love to their pet cat by moaning the cat\'s name during REM phase sleep.')
    ),
    (ReportCampaignLotameBehavioralInterest, lambda: None),
])
def test_report_record_identity(auth_app, report_model, dimension_factory):
    '''
    Check if report queries that require joins with TargetValues/segments don't merge distinct reports.
    (We need to filter using both ReportModel.dimension and ReportModel.related fields).

    The code is shared among most report managers. (ReportCategoryManager has slightly different SQL).

    If 'dimension' column was ignored, site reports of campaign 1 and 2 would be merged
    and instead of separate series, sum of both series would appear in both reports.
    '''
    dimension_object = dimension_factory()

    campaign_1 = Campaign.objects.get(name='campaign_1')
    campaign_2 = Campaign.objects.get(name='campaign_2')

    time = datetime(2014, 7, 1)
    start = time - timedelta(days=1)
    end = time + timedelta(weeks=1000)  # Big enough so that there is only one dot on the graph.

    # Create report models we query for:
    report_model.objects.create(time=time, imp=10, related=campaign_1, dimension=dimension_object)
    report_model.objects.create(time=time + timedelta(hours=1), imp=20, related=campaign_1, dimension=dimension_object)
    report_model.objects.create(time=time, imp=1, related=campaign_2, dimension=dimension_object)
    report_model.objects.create(time=time, imp=3, related=campaign_2)

    # Create dimensions for report models we should ignore:
    tv_os_emacs = TargetValue.objects.create_representant('appnexus', dimensions.g_os, ['GNU', 'Emacs'])
    segment_lotame_people = LotameBehavioralInterest.objects.create(
        appnexus_id=333333, lotame_id=222331, name='People who type "Google" in Google.')

    # Create report models we should ignore:
    for campaign in (campaign_1, campaign_2):
        ReportCampaignSite.objects.create(time=time, imp=100000, related=campaign, dimension='http://slonik.com')
        ReportCampaignOs.objects.create(time=time, imp=100000, related=campaign, dimension=tv_os_emacs)
        ReportCampaignLotameBehavioralInterest.objects.create(time=time, imp=100000, related=campaign,
                                                              dimension=segment_lotame_people)

    # Django ORM aggregation is finally useful! Calculate expected sums:
    sum_in_campaign_1_report = report_model.objects.filter(
        dimension=dimension_object, related=campaign_1).aggregate(Sum('imp'))['imp__sum']
    sum_in_campaign_2_report = report_model.objects.filter(
        dimension=dimension_object, related=campaign_2).aggregate(Sum('imp'))['imp__sum']

    def chart_query(base_obj):
        """
        Execute chart query and return aggregated impression number for chart data points.

        Also checks the number of datapoints
        """
        related_query = dimension_object
        if not (isinstance(dimension_object, str) or dimension_object is None):
            related_query = dimension_object.pk

        report = report_model.objects.report_chart(
            report_base_obj=base_obj, reported_related_ids=[related_query],
            metric='imp', start_date=start, end_date=end)

        assert len(report) == 1, \
            'The range in query should be so large that the report will be granulated to single datapoint.'
        return report[0]['v']

    def table_query(base_obj):
        if isinstance(dimension_object, str) or dimension_object is None:
            expected_label = dimension_object
        elif isinstance(dimension_object, TargetValue):
            expected_label = dimension_object.value
        elif isinstance(dimension_object, LotameBase):
            expected_label = dimension_object.name

        report = report_model.objects.report_table(
            related_obj=base_obj, start_date=start, end_date=end, limit=None)
        [checked_row] = filter(lambda row: row['label'] == expected_label, report)
        return checked_row['imp']

    assert chart_query(campaign_1) == sum_in_campaign_1_report
    assert table_query(campaign_1) == sum_in_campaign_1_report

    assert chart_query(campaign_2) == sum_in_campaign_2_report
    assert table_query(campaign_2) == sum_in_campaign_2_report


def test_sorting(state_app):
    '''
    Checking aggregation with different sorting.
    '''

    campaign = Campaign.objects.get(name='I\'m a fruit')

    i = 0
    for strategy in campaign.strategy_set.all():

        for (dt, data_cost_value, imp, imp_value, clk, conv, conv_value) in REPORT_DATA:
            report = ReportStrategy(
                time=dt,
                imp_value=imp_value + i,
                imp=imp + i,
                clk=clk + i,
                conv=conv + i,
                conv_value=conv_value + i,
                data_cost_value=data_cost_value + i,
            )
            report.related = strategy
            report.save()

        i += 1

    def check_sorting(start_date, end_date, metric_name, values):
        '''
        Checking sorting order.

        :param datetime start_date
        :param datetime end_date
        :param string metric_name: metric slug
        :param list values: list of expected values
        '''

        aggregation = ReportStrategy.objects.report_table(
            related_obj=campaign,
            start_date=start_date,
            end_date=end_date,
            sort_by=metric_name,
        )
        if metric_name.startswith('~'):
            metric_name = metric_name[1:]

        column = [x[metric_name] for x in aggregation]
        assert column == values

    # ASC
    check_sorting(
        start_date=datetime(2014, 4, 1),
        end_date=datetime(2014, 4, 1),
        metric_name='imp',
        values=[Decimal('77'), Decimal('79')],
    )

    # DESC
    check_sorting(
        start_date=datetime(2014, 4, 1),
        end_date=datetime(2014, 4, 1),
        metric_name='~imp',
        values=[Decimal('79'), Decimal('77')],
    )


def make_report_series(strategy, from_date, to_date, interval):
    '''
    Creates basic report for a specified strategy, with time series
    from start to end date spaced by given interval.

    :param strategy: Strategy object
    :param from_date: datetime.datetime
    :param to_date: datetime.datetime
    :param interval: datetime.timedelta
    '''
    current_date = from_date

    while to_date > current_date:
        # metrics values are not important, series are
        report = ReportStrategy(time=current_date)

        report.related = strategy
        report.save()

        current_date += interval


@pytest.mark.parametrize('report_data, grain_data', [
    (
            ('30-06-2014', '01-07-2014', timedelta(minutes=15)),  # 1 day, 1 event/15 min
            [
                ('30-06-2014', '30-06-2014', 4 * 24),  # 1 day, 97 data series (grouping by 1/4h)
                ('30-06-2014', '03-07-2014', 24),  # 4 days,  24 series (grouping by hour)
                ('30-06-2014', '08-07-2014', 1),  # 8 days, 1 series (grouping by day)
            ]
    ),
    (
            ('01-01-2014', '10-06-2014', timedelta(days=1)),  # 160 days, 1 event/day
            [
                ('01-01-2014', '07-06-2014', 6),  # 7 days, 6 series (grouping by day)
                ('01-01-2014', '11-02-2014', 7),  # 40 days, 7 series (grouping by week)
                ('01-01-2014', '01-06-2014', 6),  # 150 days, 6 series (grouping by month)
                ('01-01-2014', '31-12-2023', 1),  # 3650 days, 1 series (grouping by years)
            ]
    ),
])
def test_report_series_granulation(client, state_app, report_data, grain_data):
    '''
    Checks how many report series are returned from backend
    based on time grain.
    '''
    TIME_FORMAT = '%d-%m-%Y'
    strategy = state_app.models['strategy'][default_strategies[0]['name']]

    start_date = datetime.strptime(report_data[0], TIME_FORMAT)
    end_date = datetime.strptime(report_data[1], TIME_FORMAT)
    interval = report_data[2]

    make_report_series(strategy, start_date, end_date, interval)

    for fetched_data in grain_data:
        report_request_url = url_with_querystring(
            reverse('report_chart', args=['Campaign', strategy.campaign.slug]),
            **{
                'start_date': fetched_data[0],
                'end_date': fetched_data[1],
                'dim': 'strategy',
                'related_ids[]': strategy.id_random
            }
        )

        client.login(
            username=default_user[0]['username'],
            password=default_user[0]['password']
        )

        response = simplejson.loads(
            client.get(report_request_url).content
        )

        assert len(response['series']) == fetched_data[2]
