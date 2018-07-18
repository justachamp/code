import re

from collections import defaultdict
from datetime import datetime
from functools import partial

from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from etc.constants import METRICS, BACKEND_DATE_FORMAT, FRONTEND_REPORTS_ITEMS_LIMIT
from etc import dimensions
from ui.utils import render_to_json
from ui.report.models import BaseReportCampaign, BaseReportStrategy, ReportAdvert, ReportStrategy, ReportCampaign
from ui.campaign.models import Campaign, Strategy
from ui.targeting.utils import subclasses_of
from ui.targeting.models import TargetMap, TargetValue


report_subclasses = partial(subclasses_of, module_name='ui.report.models')

CAMPAIGN_TARGETING_MODELS = report_subclasses(BaseReportCampaign) + [ReportStrategy]
STRATEGY_TARGETING_MODELS = report_subclasses(BaseReportStrategy) + [ReportAdvert]

# dimension to model maps
DIMENSION_MODEL_MAP_CAMPAIGN = {getattr(m, 'dimension_element', None): m for m in CAMPAIGN_TARGETING_MODELS}
DIMENSION_MODEL_MAP_STRATEGY = {getattr(m, 'dimension_element', None): m for m in STRATEGY_TARGETING_MODELS}


def date_range_from_url(request):
    '''
    Helper function for getting dates form url.

    :param request: Django Http Request
    :rtype tuple of date objects
    :returns (start_date or None, end_date)
    '''

    start_date_str = request.GET.get('start_date')
    try:
        start_date = datetime.strptime(start_date_str, BACKEND_DATE_FORMAT)
    except (ValueError, TypeError):
        start_date = None

    end_date_str = request.GET.get('end_date')
    try:
        end_date = datetime.strptime(end_date_str, BACKEND_DATE_FORMAT)
    except (ValueError, TypeError):
        end_date = datetime.utcnow()

    return (start_date, end_date)


def format_chart(raw_chart):
    '''
    Format chart for frontend.

    :param list raw_chart: list of results dicts of chart query
    :return: dict of chart data with legend and metrics series over time

    ..note::
        raw_chart is like:
        [
            {
                'related_id': u'0',
                'dt': datetime.datetime(2014, 4, 21, 0, 0),
                'v': Decimal('785792')
            },
            {
                'related_id': u'1',
                'dt': datetime.datetime(2014, 4, 21, 0, 0),
                'v': Decimal('1212')
            },
            ...
        ]
        We map data by stringified datetime.
        {
            2014, 4, 21, 0, 0: {
                u'1': Decimal('1212'),
                u'0': Decimal('785792')
            },
            ...
        }
    '''
    series_by_date = defaultdict(dict)

    for row in raw_chart:
        dt = row['dt']
        series_by_date[str(dt)][row['object_id']] = row['v']

    return {'series': series_by_date}


@render_to_json(preserve_http_response=True)
def report_data(raw_table, overview, report_name, start_date, end_date, dimension, running_objects, strategy_obj):
    """
    Provides full data for report

    :param list raw_table: report table query result
    :param dict overview: dict of aggregated metrics (same metrics as in single table row)
    :param str report_name: report name 'Campaign' or 'Strategy'
    :param datetime start_date: start date used for the query
    :param datetime end_date: end date used for the query
    :param str dimension: name of dimension used for the query
    :param list running_objects: ids of objects currently running
    :param object strategy_obj: strategy object or None for campaign
    """

    def metrics_dict(row):
        return {metric: row[metric] for metric in METRICS.keys()}

    # this flag tells that we should display or hide whitelist/blacklist buttons
    dimension_from_targeting = strategy_obj and dimension in Strategy.DIMENSIONS_TO_FIELDS_MAP.keys()

    targeting_exclude_values = []
    report_related_field = None

    if dimension_from_targeting:
        # checking included and excluded values from given dimension
        report_related_field = Strategy.DIMENSIONS_TO_FIELDS_MAP.get(dimension)
        targeting_exclude_values = getattr(strategy_obj, '%s_exclude' % report_related_field)\
                                        .values_list('id', flat=True)
        if report_related_field == 'targeting_values':
            # adding filter by category
            targeting_exclude_values = targeting_exclude_values.filter(category=dimensions.dim_groups[dimension])

    table = []
    for row in raw_table:
        # Label can be null.
        packed_label = row.get('label') or 'Unknown'
        # Family line of a label can be an empty string.
        label = TargetMap.family_line(packed_label) or 'Unknown'

        table.append([{
            'pk': row['object_id'],
            'label': label,
            'is_running': running_objects is None or row['object_id'] in running_objects,
            'blacklist': row['object_id'] in targeting_exclude_values,
        }, metrics_dict(row)])

    result = {
        'date_range': {
            'start': start_date.isoformat(),
            'end': end_date.isoformat(),
        },
        'dimension': dimension,
        'dimension_from_targeting': dimension_from_targeting,
        'report_related_field': report_related_field,
        'level': report_name,
        'overview': metrics_dict(overview),
        'table': table,
    }

    return {
        'response': result
    }


@login_required
def campaign_overview_report(request, campaign_slug):
    ''' Report for campaign '''

    start_date, end_date = date_range_from_url(request)
    limit = int(request.GET.get('limit', FRONTEND_REPORTS_ITEMS_LIMIT))
    dimension = request.GET.get('dim') or 'strategy'
    model = DIMENSION_MODEL_MAP_CAMPAIGN[dimension]

    campaign = get_object_or_404(
        Campaign,
        slug=campaign_slug,
        account__users=request.user
    )

    if dimension == 'strategy':
        pks = [s.pk for s in campaign.strategy_set.all()]
    else:
        pks = [campaign.pk]
    start_date = start_date or model.get_earliest_time(pks) or datetime.utcnow()

    table = model.objects.report_table(
        related_obj=campaign,
        start_date=start_date,
        end_date=end_date,
        sort_by=request.GET.get('sort'),
        limit=limit,
    )
    overview = ReportCampaign.objects.report_overview(campaign)
    if dimension == 'strategy':
        running_objects = []
        for strategy in campaign.strategy_set.filter(is_deleted=False):
            if strategy.state.is_running:
                running_objects.append(strategy.id_random)
    else:
        running_objects = None

    return report_data(table, overview, 'Campaign', start_date, end_date, dimension, running_objects, None)


@login_required
def strategy_overview_report(request, strategy_slug):
    ''' Report for strategy '''

    start_date, end_date = date_range_from_url(request)
    limit = int(request.GET.get('limit', FRONTEND_REPORTS_ITEMS_LIMIT))
    dimension = request.GET.get('dim') or 'advert'
    model = DIMENSION_MODEL_MAP_STRATEGY[dimension]

    strategy = get_object_or_404(
        Strategy,
        slug=strategy_slug,
        campaign__account__users=request.user
    )

    if dimension == 'advert':
        pks = [s.pk for s in strategy.advert_set.all()]
    else:
        pks = [strategy.pk]
    start_date = start_date or model.get_earliest_time(pks) or datetime.utcnow()

    table = model.objects.report_table(
        related_obj=strategy,
        start_date=start_date,
        end_date=end_date,
        sort_by=request.GET.get('sort'),
        limit=limit,
    )
    overview = ReportStrategy.objects.report_overview(strategy)
    if dimension == 'advert':
        running_objects = []
        for advert in strategy.advert_set.filter(is_deleted=False):
            if advert.state.is_running:
                running_objects.append(advert.id_random)
    else:
        running_objects = None

    return report_data(table, overview, 'Strategy', start_date, end_date, dimension, running_objects, strategy)


@render_to_json(preserve_http_response=True)
@login_required
def overview_chart(request, model_name, slug):
    dimension = request.GET.get('dim') or 'advert'
    user = request.user
    if model_name == 'Strategy':
        report_base = Strategy.objects.filter(campaign__account__users=user)
        report_model = DIMENSION_MODEL_MAP_STRATEGY[dimension]
    elif model_name == 'Campaign':
        report_base = Campaign.objects.filter(account__users=user)
        report_model = DIMENSION_MODEL_MAP_CAMPAIGN[dimension]
    else:
        return HttpResponseNotFound()

    related_ids = request.GET.getlist('related_ids[]', [])
    # HACK: when preparing the URL to query, an array containing object ids and
    # potentially one null is passed to $.param. $.param tolerates null values
    # and encodes them as empty strings. They get passed to an url-encoded string
    # that forms 'related_ids' query param.
    # However, Django ignores empty strings in query lists. So, in order to capture
    # the null values, we have to find that one ignored array element in loose items
    # in the GET dictionary.
    # The 'lost null' element has a key 'related_ids[SOME_INT]' and value of an empty
    # unicode string.
    # The null table row and null chart series correspond to Report instances
    # where FK named 'dimension' or 'related' is null (example: landing site).
    # They are displayed as 'Unknown'. There are also 'Unknown' Report instances
    # that have their related objects which have the 'Unknown' value themselves
    # (like unknown position).
    lost_null_keys = filter(lambda key: re.match(r'related_ids\[\d+\]', key), request.GET.iterkeys())
    if lost_null_keys:
        [lost_null_key] = lost_null_keys  # There should be only one.
        if request.GET[lost_null_key] == u'':
            related_ids.append(None)

    chart_metric = request.GET.get('chart_metric', 'imp')
    start_date, end_date = date_range_from_url(request)
    if None in (start_date, end_date):
        return HttpResponseBadRequest()

    report_obj = report_base.get(slug=slug)

    chart = report_model.objects.report_chart(
        report_base_obj=report_obj,
        reported_related_ids=related_ids,
        metric=chart_metric,
        start_date=start_date,
        end_date=end_date,
    )
    return format_chart(chart)


@require_http_methods(['POST'])
@login_required
def whitelist_blacklist(request, action, strategy_slug):
    '''
    Include or exclude target value from targeting in given strategy.

    :param str action: 'whitelist' or 'blacklist'
    :param str strategy_slug

    POST FIELDS:
        - report_related_field (str) - eg. segment_peer_contextual
        - id (str) - id of target object

    :returns: new label for whitelist/blacklist button
    '''

    strategy = get_object_or_404(
        Strategy,
        slug=strategy_slug,
        campaign__account__users=request.user
    )

    # eg. segment_peer_contextual
    report_related_field = request.POST['report_related_field']

    if report_related_field not in Strategy.DIMENSIONS_TO_FIELDS_MAP.values():
        return HttpResponseNotFound('model field %s is not available in model' % report_related_field)

    # eg. <ContentCategory: Arts & Entertainment>
    targeting_obj = getattr(strategy, report_related_field).model.objects.get(id=request.POST['id'])

    if isinstance(targeting_obj, TargetValue) and not targeting_obj.is_representant:
        # get representant
        targeting_obj = targeting_obj.representant

    # if targeting_obj is a node in tree structure
    # we also want to include/exclude all on his children
    if hasattr(targeting_obj, 'get_nested_nodes'):
        targeting_objects = targeting_obj.get_nested_nodes()
    else:
        targeting_objects = [targeting_obj]

    if action == 'blacklist':
        # eg.
        #   - add to Stategy.content_category_values_exclude
        #   - remove from Stategy.content_category_values
        getattr(strategy, '%s_exclude' % report_related_field).add(*targeting_objects)
        getattr(strategy, report_related_field).remove(*targeting_objects)
        return HttpResponse('whitelist')

    # whitelist
    #   - add to Stategy.content_category_values
    #   - remove from Stategy.content_category_values_exclude
    getattr(strategy, report_related_field).add(*targeting_objects)
    getattr(strategy, '%s_exclude' % report_related_field).remove(*targeting_objects)
    return HttpResponse('blacklist')
