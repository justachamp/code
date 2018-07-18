# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import unicode_literals

from datetime import datetime, timedelta

from collections import Counter
from itertools import groupby
from operator import itemgetter

from addnow.apps.reports.utils import DayRangeSplitter
from addnow.apps.tracker.models.collections import OutsideShares
from addnow.apps.tracker.models.reports import ALL_DIMENSIONS
from addnow.apps.tracker.models.stats.base import BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.stats.country import CountryBase
from addnow.apps.tracker.models.stats.keyword import KeywordBase
from addnow.apps.tracker.models.stats.source import SourceBase
from addnow.apps.tracker.models.stats.tool import ToolBase
from addnow.apps.tracker.models.stats.url import UrlBase


class Report(object):
    aggregations = {
        'hour': {
            'model_class': BaseDaily,
            'aggregate_by_values': True
        },
        'day': {
            'model_class': BaseMonthly,
            'aggregate_by_values': True
        },
        'month': {
            'model_class': BaseMonthly,
            'aggregate_by_values': False
        },
        'year': {
            'model_class': BaseYearly,
            'aggregate_by_values': False
        }
    }

    docs_limit = 100

    def __init__(self, site_id, begin_date, end_date, docs_limit=None):
        self.site_id = site_id
        self.begin_date = begin_date
        self.end_date = end_date
        self.docs_limit = docs_limit or self.docs_limit

    def _get_model_class(self, base_model_class, collection_name):
        subclasses = base_model_class.__subclasses__()
        return next(subclass for subclass in subclasses if subclass.collection_name == collection_name)

    def get_requests(self):
        requests = []

        date_ranges = DayRangeSplitter.split(self.begin_date, self.end_date)
        for date_range in date_ranges:
            begin_is_first = DayRangeSplitter.is_first_period(date_range[0])
            end_is_last = DayRangeSplitter.is_last_period(date_range[1])
            requests.append({
                'range': date_range,
                'collection_name': BaseMonthly.collection_name,
                'aggregate_by_values': not (begin_is_first and end_is_last)
            })

        return requests

    def get_totals(self, base_model_class, events=None, group_fields=None):
        events = events or base_model_class.get_events()
        if group_fields is None:
            group_fields = base_model_class.data_fields

        requests = self.get_requests()
        result_data = []
        merged_data = []

        for request in requests:
            begin_date, end_date = request['range']
            aggregate_by_values = request['aggregate_by_values']
            collection_name = request['collection_name']
            model_class = self._get_model_class(base_model_class, collection_name)
            result_data += model_class().get_totals(
                self.site_id, begin_date, end_date,
                events=events, group_fields=group_fields,
                aggregate_by_values=aggregate_by_values, limit=self.docs_limit
            )

        if group_fields:
            key_func = itemgetter(*group_fields)
            for key, grouper in groupby(sorted(result_data, key=key_func), key_func):
                key_fields = key if isinstance(key, tuple) else (key,)
                sum_dict = Counter(dict(zip(group_fields, key_fields)))
                for item in grouper:
                    counters = {event: item[event] for event in events}
                    sum_dict.update(counters)
                merged_data.append(dict(sum_dict))
            merged_data = sorted(merged_data, key=itemgetter(*events), reverse=True)
        else:
            if not result_data:
                return {event: 0 for event in events}
            sum_dict = Counter({})
            for item in result_data:
                sum_dict.update(item)
            merged_data = dict(sum_dict)

        return merged_data

    def _add_percentages(self, data, events, totals):
        for item in data:
            for event in events:
                event_percent = round(item[event] / totals[event] * 100, 0) if totals[event] > 0 else 0
                item['%sPercent' % event] = event_percent
        return data

    def _add_viral_lift(self, data):
        for item in data:
            viral_lift = round(item['clicks'] / item['shares'], 2) if item['shares'] > 0 else 0
            item['viralLift'] = viral_lift
        return data

    def get_shares_and_clicks_by_tools(self):
        events = ['shares', 'clicks']
        totals = self.get_totals(ToolBase, events=events, group_fields=[])
        data = self.get_totals(ToolBase, events=events)
        data = self._add_percentages(data, events, totals)
        return data

    def get_top_social_channels(self):
        events = ['shares', 'clicks']
        totals = self.get_totals(SourceBase, events=events, group_fields=[])
        data = self.get_totals(SourceBase, events=events)
        data = self._add_percentages(data, events, totals)
        return data

    def get_top_content(self, event):
        events = [event]
        totals = self.get_totals(UrlBase, events=events, group_fields=[])
        data = self.get_totals(UrlBase, events=events)
        data = self._add_percentages(data, events, totals)
        for item in data:
            del item['checksum']
        return data

    def get_top_frequently_copied(self):
        data = self.get_totals(KeywordBase, events=['copies'])
        return data

    def get_top_countries(self):
        events = ['shares', 'clicks']
        data = self.get_totals(CountryBase, events=events)
        data = self._add_viral_lift(data)
        return data

    def get_total_external_shares(self):
        totals = OutsideShares().get_totals_without_group(self.site_id)
        data = OutsideShares().get_totals(self.site_id, group_fields=['source'], limit=self.docs_limit)
        data = self._add_percentages(data, events=['shares'], totals=totals)
        return data

    def get_events_summary(self, aggregation, events):
        if aggregation not in self.aggregations.keys():
            return []
        model_class = self.aggregations[aggregation]['model_class']
        aggregate_by_values = self.aggregations[aggregation]['aggregate_by_values']
        events_summary = model_class().get_events_summary(self.site_id, self.begin_date, self.end_date, events,
                                                          aggregate_by_values=aggregate_by_values)
        return events_summary

    def get_report(self, aggregation, events, dimensions, summary=False):
        if aggregation not in self.aggregations.keys():
            return []
        model_class = self.aggregations[aggregation]['model_class']
        aggregate_by_values = self.aggregations[aggregation]['aggregate_by_values']
        report_data = model_class().get_report(self.site_id, self.begin_date, self.end_date, events, dimensions,
                                               summary=summary, aggregate_by_values=aggregate_by_values)
        for item in report_data:
            keys = item.keys()
            dimension_class = ALL_DIMENSIONS[item['dimension']]
            including_events = dimension_class.get_events()
            for event in events:
                if event in keys and event not in including_events:
                    del item[event]
        return report_data


def get_site_stats(site_id, now_date, events):
    """
    Returns stats for events for specified base datetime,
    average for latest 7 days and average for latest 30 days.
    :param site_id: The site id
    :type site_id: str or int
    :param now_date: The base datetime to build the report
    :type now_date: datetime
    :param events: Events to be included in report
    :type events: list
    :rtype: dict
    """

    now_date = datetime.combine(now_date.date(), datetime.min.time())
    begin_date_for_7 = now_date - timedelta(days=7)
    begin_date_for_30 = now_date - timedelta(days=30)
    stats = {}
    report = Report(int(site_id), begin_date_for_30, now_date)
    summary_data = report.get_events_summary(aggregation='day', events=events)
    summary_data_7 = [item for item in summary_data if item['date'] >= begin_date_for_7]
    summary_data_30 = [item for item in summary_data if item['date'] >= begin_date_for_30]
    summary_data_today = [item for item in summary_data if item['date'] == now_date]

    for event in events:
        stats[event] = sum(item[event] for item in summary_data_today)
        total_7 = sum(item[event] for item in summary_data_7)
        stats['%s_7_average' % event] = int(round(total_7 / 7, 0))
        total_30 = sum(item[event] for item in summary_data_30)
        stats['%s_30_average' % event] = int(round(total_30 / 30, 0))

    return stats
