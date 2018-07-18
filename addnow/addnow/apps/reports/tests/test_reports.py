# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from mock import patch

from addnow.apps.accounts import constants, factories
from addnow.apps.reports.archive import Report, get_site_stats
from addnow.apps.reports.tests.mocks import get_data
from addnow.apps.tracker import tasks
from addnow.apps.tracker.models.collections import OutsideShares
from addnow.apps.tracker.models.stats.base import BaseMonthly
from addnow.apps.tracker.models.stats.url import UrlBase, UrlDaily
from addnow.apps.tracker.tests.base import MongoTestCase


SUMMARY_EVENTS = ['shares', 'clicks', 'views', 'follows', 'copies']

date_range = [datetime.datetime(2015, i, 15) for i in range(1, 13)]


class ReportsTestCase(MongoTestCase):
    @classmethod
    def setUpClass(cls):
        super(ReportsTestCase, cls).setUpClass()
        cls.site = factories.SiteFactory()
        begin_date, end_date = date_range[0], date_range[-1]
        cls.report = Report(cls.site.pk, begin_date, end_date)

    def inc_counters(self):
        data = get_data(self.site.pk, date_range)
        for item in data:
            tasks.update_counters(item['event'], value=1, **item['data'])

    @patch('addnow.apps.reports.utils.DayRangeSplitter.split')
    def test__get_requests(self, split_day_range):
        split_day_range.return_value = [(datetime.datetime(2015, 12, 1), datetime.datetime(2015, 12, 31))]
        self.assertEqual(self.report.get_requests(), [
            {
                'range': split_day_range.return_value[0],
                'collection_name': BaseMonthly.collection_name,
                'aggregate_by_values': False
            }
        ])

        split_day_range.return_value = [(datetime.datetime(2015, 12, 1), datetime.datetime(2015, 12, 15))]
        self.assertEqual(self.report.get_requests(), [
            {
                'range': split_day_range.return_value[0],
                'collection_name': BaseMonthly.collection_name,
                'aggregate_by_values': True
            }
        ])

        split_day_range.return_value = [(datetime.datetime(2015, 12, 15), datetime.datetime(2015, 12, 31))]
        self.assertEqual(self.report.get_requests(), [
            {
                'range': split_day_range.return_value[0],
                'collection_name': BaseMonthly.collection_name,
                'aggregate_by_values': True
            }
        ])

    def test__get_totals(self):
        self.inc_counters()
        totals_from_daily_collection = UrlDaily().get_totals(
            self.site.pk, self.report.begin_date, self.report.end_date)
        report_totals = self.report.get_totals(UrlBase)
        self.assertEqual(totals_from_daily_collection, report_totals)

    def test__get_shares_and_clicks_by_tools(self):
        shares_and_clicks_by_tool = self.report.get_shares_and_clicks_by_tools()
        old_shares = [item['shares'] for item in shares_and_clicks_by_tool]
        old_clicks = [item['clicks'] for item in shares_and_clicks_by_tool]
        self.inc_counters()
        shares_and_clicks_by_tool = self.report.get_shares_and_clicks_by_tools()
        for item, old_share, old_click in zip(shares_and_clicks_by_tool, old_shares, old_clicks):
            self.assertEqual(item['shares'] - old_share, 1)
            self.assertEqual(item['clicks'] - old_click, 1)

    def test__get_top_social_channels(self):
        self.inc_counters()
        shares_and_clicks_by_tool = self.report.get_shares_and_clicks_by_tools()
        top_social_channels = self.report.get_top_social_channels()
        total_social_shares = sum([x['shares'] for x in top_social_channels])
        total_social_clicks = sum([x['clicks'] for x in top_social_channels])
        total_clicks_by_tool = sum([x['clicks'] for x in shares_and_clicks_by_tool])
        total_shares_by_tool = sum([x['shares'] for x in shares_and_clicks_by_tool])
        self.assertEqual(total_clicks_by_tool, total_social_clicks)
        self.assertEqual(total_shares_by_tool, total_social_shares)

    def test__get_total_external_shares(self):
        outside_shares = {
            constants.SOCIAL_SERVICE_TWITTER: 124,
            constants.SOCIAL_SERVICE_GOOGLE_PLUS: 981,
            constants.SOCIAL_SERVICE_FACEBOOK: 21,
            constants.SOCIAL_SERVICE_LINKEDIN: 2,
            constants.SOCIAL_SERVICE_PINTEREST: 91919
        }
        for source, shares in outside_shares.items():
            OutsideShares().set_counter(site=self.site.pk, url='http://test.com/', source=source, value=shares)
        total = self.report.get_total_external_shares()
        total = sum([x['sharesPercent'] for x in total])
        self.assertEqual(total, 100.0)

    @patch('addnow.apps.reports.archive.Report.get_events_summary')
    def test__get_site_stats(self, get_events_summary):
        base_datetime_for_report = datetime.datetime(2015, 6, 3)

        get_events_summary.return_value = [
            {
                'shares': 1000, 'clicks': 2000, 'follows': 3000,
                'copies': 4000, 'views': 5000, 'date': datetime.datetime(2015, 6, 3)
            }
        ]
        site_stats = get_site_stats(1, base_datetime_for_report, events=SUMMARY_EVENTS)
        expected_stats = {
            'shares': 1000, 'shares_7_average': 143, 'shares_30_average': 33,
            'clicks': 2000, 'clicks_7_average': 286, 'clicks_30_average': 67,
            'follows': 3000, 'follows_7_average': 429, 'follows_30_average': 100,
            'copies': 4000, 'copies_7_average': 571, 'copies_30_average': 133,
            'views': 5000, 'views_7_average': 714, 'views_30_average': 167
        }
        self.assertEqual(site_stats, expected_stats)

        get_events_summary.return_value = [
            {
                'shares': 1000, 'clicks': 2000, 'follows': 3000,
                'copies': 4000, 'views': 5000, 'date': datetime.datetime(2015, 6, 2)
            }
        ]
        expected_stats = {
            'shares': 0, 'shares_7_average': 143, 'shares_30_average': 33,
            'clicks': 0, 'clicks_7_average': 286, 'clicks_30_average': 67,
            'follows': 0, 'follows_7_average': 429, 'follows_30_average': 100,
            'copies': 0, 'copies_7_average': 571, 'copies_30_average': 133,
            'views': 0, 'views_7_average': 714, 'views_30_average': 167
        }
        site_stats = get_site_stats(1, base_datetime_for_report, events=SUMMARY_EVENTS)
        self.assertEqual(site_stats, expected_stats)

        get_events_summary.return_value = [
            {
                'shares': 1000, 'clicks': 2000, 'follows': 3000,
                'copies': 4000, 'views': 5000, 'date': datetime.datetime(2015, 5, 3)
            },
            {
                'shares': 1000, 'clicks': 2000, 'follows': 3000,
                'copies': 4000, 'views': 5000, 'date': datetime.datetime(2015, 5, 4)
            },
            {
                'shares': 1000, 'clicks': 2000, 'follows': 3000,
                'copies': 4000, 'views': 5000, 'date': datetime.datetime(2015, 5, 27)
            },
            {
                'shares': 1000, 'clicks': 2000, 'follows': 3000,
                'copies': 4000, 'views': 5000, 'date': datetime.datetime(2015, 6, 3)
            }
        ]
        expected_stats = {
            'shares': 1000, 'shares_7_average': 286, 'shares_30_average': 100,
            'clicks': 2000, 'clicks_7_average': 571, 'clicks_30_average': 200,
            'follows': 3000, 'follows_7_average': 857, 'follows_30_average': 300,
            'copies': 4000, 'copies_7_average': 1143, 'copies_30_average': 400,
            'views': 5000, 'views_7_average': 1429, 'views_30_average': 500
        }
        site_stats = get_site_stats(1, base_datetime_for_report, events=SUMMARY_EVENTS)
        self.assertEqual(site_stats, expected_stats)
