# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from datetime import datetime

from django.conf import settings
from django.http import JsonResponse

from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from addnow.apps.accounts.models import Site
from addnow.apps.analytics import reports as analytics_reports
from addnow.apps.reports.archive import Report
from addnow.apps.reports.utils import combine_lists_by_fields
from addnow.apps.tracker.models.reports import ALL_DIMENSIONS
from addnow.cache import DigestCache


logger = logging.getLogger(__name__)

SUMMARY_EVENTS = ['shares', 'clicks', 'views', 'follows', 'copies']


def make_digest(site_id, begin_date, end_date, aggregation):
    logger.debug('Making digest report...')
    report = Report(site_id, begin_date, end_date)

    return {
        'eventsSummary': report.get_events_summary(aggregation, events=SUMMARY_EVENTS),
        'sharesAndClicksByTool': report.get_shares_and_clicks_by_tools(),
        'topSocialChannels': report.get_top_social_channels(),
        'topContentByShares': report.get_top_content('shares'),
        'topContentByClicks': report.get_top_content('clicks'),
        'topFrequentlyCopied': report.get_top_frequently_copied(),
        'topCountries': report.get_top_countries(),
        'totalExternalShares': report.get_total_external_shares()
    }


def get_ga_events_summary(site, begin_date, end_date, aggregation, events_summary):
    ga_views = analytics_reports.get_views(site, begin_date, end_date, aggregation)
    return combine_lists_by_fields(events_summary, ga_views, 'date')


def get_digest_data(site, begin_date, end_date, aggregation, cache_timeout=86400, clear_cache=False):
    cache_query = {
        'site_id': site.pk,
        'begin_date': str(begin_date),
        'end_date': str(end_date),
        'aggregation': aggregation
    }

    digest_data = DigestCache.get(cache_query) or {}
    cached = True

    if not digest_data or clear_cache:
        cached = False
        digest_data = make_digest(site.pk, begin_date, end_date, aggregation)

        if site.analytics_profile:
            logger.debug('Getting reports from Google Analytics API...')
            digest_data['eventsSummary'] = get_ga_events_summary(
                site, begin_date, end_date, aggregation, digest_data['eventsSummary'])
            digest_data['referringDomains'] = analytics_reports.get_referring_domains(site, begin_date, end_date)
            digest_data['searchTerms'] = analytics_reports.get_search_terms(site, begin_date, end_date)
            digest_data['searchEngines'] = analytics_reports.get_search_engines(site, begin_date, end_date)
        if clear_cache:
            DigestCache.delete(cache_query)
        DigestCache.set(cache_query, digest_data, timeout=cache_timeout)
    return cached, digest_data


class GetReport(APIView):
    """
    Report Api.
    Examples:
    http://addnow.dev:8081/api/v1/reports?site=1&begin_date=<timestamp>&end_date=<timestamp>&events=clicks,copies
    http://addnow.dev:8081/api/v1/reports?site=1&begin_date=<timestamp>&end_date=<timestamp>&events=clicks,copies&dimensions=browser,copy
    http://addnow.dev:8081/api/v1/reports?site=1&begin_date=<timestamp>&end_date=<timestamp>&events=clicks,copies&dimensions=browser,copy&summary=true
    """
    permission_classes = (IsAuthenticated,)

    mandatory_fields = ('site', 'begin_date', 'end_date', 'events')

    def get(self, request):
        params = request.GET.dict()

        for key in self.mandatory_fields:
            if key not in params.keys():
                raise ValidationError('Mandatory field: "%s" is missing' % key)

        try:
            site = Site.objects.get(pk=params['site'])
        except Site.DoesNotExist as ex:
            raise NotFound(ex.message)
        if site.user != request.user:
            raise PermissionDenied()

        begin_date = datetime.fromtimestamp(int(params['begin_date']))
        end_date = datetime.fromtimestamp(int(params['end_date']))
        aggregation = params.get('aggregation', 'day')
        events = params['events'].split(',')
        dimensions = params.get('dimensions')
        if dimensions:
            dimensions = dimensions.split(',')
        else:
            dimensions = ALL_DIMENSIONS.keys()

        report = Report(site.pk, begin_date, end_date)
        report_data = report.get_report(aggregation, events, dimensions)

        return JsonResponse(report_data, safe=False)


class GetDigest(APIView):
    """
    Digest Api.
    Examples:
    http://api.addnow.dev/api/v1/digest?site=1&begin_date=<timestamp>&end_date=<timestamp>
    http://api.addnow.dev/api/v1/digest?site=1&begin_date=<timestamp>&end_date=<timestamp>&aggregation=day
    """
    permission_classes = (IsAuthenticated,)

    mandatory_fields = ('site', 'begin_date', 'end_date')

    def get(self, request):
        params = request.GET.dict()

        for key in self.mandatory_fields:
            if key not in params.keys():
                raise ValidationError('Mandatory field: "%s" is missing' % key)

        try:
            site = Site.objects.get(pk=params['site'])
        except Site.DoesNotExist as ex:
            raise NotFound(ex.message)
        if site.user != request.user:
            raise PermissionDenied()

        begin_date = datetime.fromtimestamp(int(params['begin_date']))
        end_date = datetime.fromtimestamp(int(params['end_date']))
        aggregation = params.get('aggregation', 'day')
        cached, digest_data = get_digest_data(site, begin_date, end_date, aggregation,
                                              cache_timeout=settings.DASHBOARD_DIGEST_CACHE_TIMEOUT)

        return JsonResponse({'cached': cached, 'data': digest_data})
