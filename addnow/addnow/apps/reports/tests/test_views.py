# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import calendar
import datetime
import json
import urllib

from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status

from addnow.apps.accounts import constants, factories
from addnow.apps.reports.tests.mocks import get_data
from addnow.apps.reports.views import archive as archive_views
from addnow.apps.tracker import tasks
from addnow.apps.tracker.tests.base import MongoTestCase


def get_begin_end_date():
    today_date = datetime.date.today()
    begin_date = today_date - datetime.timedelta(days=3)
    end_date = today_date + datetime.timedelta(days=1)
    begin_date = datetime.datetime.combine(begin_date, datetime.time.min)
    end_date = datetime.datetime.combine(end_date, datetime.time.max)
    return begin_date, end_date


def get_begin_end_date_timestamp():
    begin_date, end_date = get_begin_end_date()
    begin_date = calendar.timegm(begin_date.timetuple())
    end_date = calendar.timegm(end_date.timetuple())
    return begin_date, end_date


class BaseReportViewsTestCase(MongoTestCase):
    @classmethod
    def setUpClass(cls):
        super(BaseReportViewsTestCase, cls).setUpClass()
        cls.factory = APIRequestFactory()

    def _authenticate_request(self, request, user):
        token = factories.ApiTokenFactory(user=user)
        force_authenticate(request, user=token['user'], token=token)
        return token


class ReportViewsTestCase(BaseReportViewsTestCase):
    def sum_all(self, data):
        all = 0
        for row in data:
            if not row:
                continue
            for dimension_key in row:
                if isinstance(row[dimension_key], int):
                    all += row[dimension_key]
        return all

    def test__get_report_api(self):
        site = factories.SiteFactory()
        begin_date, end_date = get_begin_end_date_timestamp()
        params = {
            'site': site.pk,
            'begin_date': begin_date,
            'end_date': end_date,
            'events': 'clicks'
        }
        url = '/api/v1/reports?%s' % urllib.urlencode(params)
        request = self.factory.get(url)
        self._authenticate_request(request, user=site.user)
        old_response = archive_views.GetReport.as_view()(request)
        data = json.loads(old_response.content)
        old_data = self.sum_all(data)

        kwargs = dict(
            site=site.pk, source=constants.SOCIAL_SERVICE_FACEBOOK,
            url='http://test.com', tool=constants.Tools.SHARING_BUTTONS.value,
            domain='www.gravity4.com',
            date=datetime.datetime.utcnow(),
            country=constants.UNKNOWN_COUNTRY,
            browser=constants.UNKNOWN_BROWSER,
            search_term='', search_engine=''
        )
        tasks.update_counters(constants.Events.CLICK.value, **kwargs)
        request = self.factory.get(url)
        self._authenticate_request(request, user=site.user)
        response = archive_views.GetReport.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        new_data = self.sum_all(data)
        self.assertNotEqual(old_data, new_data)

    def test__get_report_api_incorrect_request(self):
        site = factories.SiteFactory()
        begin_date, end_date = get_begin_end_date_timestamp()
        params = {
            'begin_date': begin_date,
            'end_date': end_date,
            'events': 'clicks'
        }

        # Generate 400 (empty site id)
        url = '/api/v1/reports?%s' % urllib.urlencode(params)
        request = self.factory.get(url)
        self._authenticate_request(request, user=site.user)
        response = archive_views.GetReport.as_view()(request)
        self.assertEqual(response.status_code, 400)

        # Generate 404 (nonexistent site id)
        url = '/api/v1/reports?%s&site=404' % urllib.urlencode(params)
        request = self.factory.get(url)
        self._authenticate_request(request, user=site.user)
        response = archive_views.GetDigest.as_view()(request)
        self.assertEqual(response.status_code, 404)

        # Generate 403 (site's user != user)
        user = factories.UserFactory()
        url = '/api/v1/reports?%s&site=%s' % (urllib.urlencode(params), site.pk)
        request = self.factory.get(url)
        self._authenticate_request(request, user=user)
        response = archive_views.GetReport.as_view()(request)
        self.assertEqual(response.status_code, 403)

    def test__get_digest_api(self):
        site = factories.SiteFactory()
        begin_date, end_date = get_begin_end_date_timestamp()
        params = {
            'site': site.pk,
            'begin_date': begin_date,
            'end_date': end_date
        }
        url = '/api/v1/digest?%s' % urllib.urlencode(params)
        request = self.factory.get(url)
        self._authenticate_request(request, user=site.user)
        response = archive_views.GetDigest.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = get_data(site.pk)
        for item in data:
            tasks.update_counters(item['event'], value=1, **item['data'])
        request = self.factory.get(url)
        self._authenticate_request(request, user=site.user)
        response = archive_views.GetDigest.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test__get_digest_api_incorrect_request(self):
        site = factories.SiteFactory()
        begin_date, end_date = get_begin_end_date_timestamp()
        params = {
            'begin_date': begin_date,
            'end_date': end_date
        }

        # Generate 400 (empty site id)
        url = '/api/v1/digest?%s' % urllib.urlencode(params)
        request = self.factory.get(url)
        self._authenticate_request(request, user=site.user)
        response = archive_views.GetDigest.as_view()(request)
        self.assertEqual(response.status_code, 400)

        # Generate 404 (nonexistent site id)
        url = '/api/v1/digest?%s&site=200' % urllib.urlencode(params)
        request = self.factory.get(url)
        self._authenticate_request(request, user=site.user)
        response = archive_views.GetDigest.as_view()(request)
        self.assertEqual(response.status_code, 404)

        # Generate 403 (site's user != user)
        user = factories.UserFactory()
        url = '/api/v1/digest?%s&site=%s' % (urllib.urlencode(params), site.pk)
        request = self.factory.get(url)
        self._authenticate_request(request, user=user)
        response = archive_views.GetDigest.as_view()(request)
        self.assertEqual(response.status_code, 403)

    def test__cache_get_digest_data(self):
        site = factories.SiteFactory()
        begin_date, end_date = get_begin_end_date()
        archive_views.get_digest_data(site, begin_date, end_date, aggregation='day')
        cached, data = archive_views.get_digest_data(site, begin_date, end_date, aggregation='day')
        self.assertEqual(cached, True)
