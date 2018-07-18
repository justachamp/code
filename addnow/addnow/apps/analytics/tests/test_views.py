from datetime import datetime, timedelta

from django.core.cache import cache
from django.core.urlresolvers import reverse

import mock

from oauth2client.client import OAuth2Credentials
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework import status

from addnow.apps.accounts.factories import ApiTokenFactory
from addnow.apps.analytics import views
from addnow.apps.analytics.factories import UserFactory, CredentialsModelFactory
from addnow.apps.analytics.models import CredentialsModel
from addnow.apps.analytics.tests import mocks
from addnow.apps.analytics import settings as analytics_settings


class BaseAnalyticsViewsTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(BaseAnalyticsViewsTestCase, cls).setUpClass()
        cls.factory = APIRequestFactory()

    def _authenticate_request(self, request, user=None):
        user = user or UserFactory(email_is_verified=True)
        token = ApiTokenFactory(user=user)
        force_authenticate(request, user=token['user'], token=token)
        return token


class TestAnalyticsViews(BaseAnalyticsViewsTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestAnalyticsViews, cls).setUpClass()
        expired = datetime.now() + timedelta(days=7)

        cls.credential = OAuth2Credentials(
            access_token='Vya29.sAE15SnT-0EB3t1Lu3lILrnqnMm7eOT4RQ68Z9Dj9C2SYoDiF2KS9f7ChC4hQmYhWLFIHQ',
            client_id='202813734956-crji4su846f5po938d3qdh9uv1fnh6qt.apps.googleusercontent.com',
            client_secret='DOlTzD_wbBrY00_g9B97jtzU',
            refresh_token='V1/RloEsuNAmko7GyhW_0DAlH-3OQmmJ0UbJTVf95Q7M6Q',
            token_expiry=expired,
            token_uri='https://accounts.google.com/o/oauth2/token',
            user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/43.0.2357.132 Safari/537.36',
            revoke_uri='https://accounts.google.com/o/oauth2/revoke'
        )
        cls.user = UserFactory(has_analytics=True, email_is_verified=True)
        cls.credentials = CredentialsModelFactory(user=cls.user, credential=cls.credential)

    def test_login(self):
        request = self.factory.get(reverse('analytics:analytics_login'))
        response = views.LoginView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_authenticated(self):
        request = self.factory.get(reverse('analytics:analytics_login'))
        self._authenticate_request(request)
        response = views.LoginView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_url', response.data.keys())

    def test_logout(self):
        request = self.factory.get(reverse('analytics:analytics_logout'))
        response = views.LogoutView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_authenticated_without_credential(self):
        request = self.factory.get(reverse('analytics:analytics_logout'))
        self._authenticate_request(request)
        response = views.LogoutView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @mock.patch('oauth2client.client.OAuth2Credentials.revoke', side_effect=mocks.mocked_expired_credential_revoke)
    def test_logout_authenticated_with_expired_credential(self, mock_revoke):
        request = self.factory.get(reverse('analytics:analytics_logout'))
        self._authenticate_request(request, self.user)

        # with self.assertRaises(TokenRevokeError):
        #     views.LogoutView.as_view()(request)
        self.assertEqual(len(mock_revoke.call_args_list), 0)

    @mock.patch('oauth2client.client.OAuth2Credentials.revoke', side_effect=mocks.mocked_credential_revoke)
    def test_logout_authenticated_with_credential(self, mock_revoke):
        request = self.factory.get(reverse('analytics:analytics_logout'))
        self._authenticate_request(request, self.user)

        self.assertEqual(CredentialsModel.objects.all().count(), 1)

        response = views.LogoutView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CredentialsModel.objects.all().count(), 0)
        self.assertEqual(len(mock_revoke.call_args_list), 1)

    def test_auth_callback(self):
        request = self.factory.post(reverse('analytics:analytics_auth'))
        response = views.AuthCallbackView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_callback_authenticated_without_mandatory_fields(self):
        request = self.factory.post(reverse('analytics:analytics_auth'))
        self._authenticate_request(request)
        response = views.AuthCallbackView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @mock.patch('oauth2client.contrib.xsrfutil.validate_token', side_effect=mocks.mocked_validate_token)
    def test_auth_callback_authenticated_with_wrong_state(self, mock_validate_token):
        request = self.factory.post(reverse('analytics:analytics_auth'), data={'state': '0', 'code': '2'})
        self._authenticate_request(request)
        response = views.AuthCallbackView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(mock_validate_token.called)
        self.assertEqual(mock_validate_token.call_count, 1)

    @mock.patch('oauth2client.contrib.xsrfutil.validate_token', side_effect=mocks.mocked_validate_token)
    def test_auth_callback_authenticated1(self, mock_validate_token):
        request = self.factory.post(reverse('analytics:analytics_auth'), data={'state': '1', 'code': '2'})
        self._authenticate_request(request)
        response = views.AuthCallbackView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertTrue(mock_validate_token.called)

    @mock.patch('oauth2client.contrib.xsrfutil.validate_token', side_effect=mocks.mocked_validate_token)
    @mock.patch('oauth2client.client.OAuth2WebServerFlow.step2_exchange', side_effect=mocks.mocked_step2_exchange)
    def test_auth_callback_authenticated2(self, mock_validate_token, mocked_step2_exchange):
        request = self.factory.post(reverse('analytics:analytics_auth'), data={'state': '1', 'code': '2'})
        self._authenticate_request(request)
        response = views.AuthCallbackView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(mock_validate_token.called)
        self.assertTrue(mocked_step2_exchange.called)

    def test_account(self):
        request = self.factory.get(reverse('analytics:accounts'))
        response = views.AccountsView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @mock.patch('addnow.apps.analytics.utils.get_service')
    def test_account_authenticated(self, get_service):
        request = self.factory.get(reverse('analytics:accounts'))
        self._authenticate_request(request)
        response = views.AccountsView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(get_service.called)
        self.assertIsInstance(response.data, list)

    def test_pageviews(self):
        request = self.factory.get(reverse('analytics:pageviews', args=['1']))
        response = views.PageviewsView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_pageviews_authenticated1(self):
        site_id = 1
        request = self.factory.get(reverse('analytics:pageviews', args=[site_id]))
        self._authenticate_request(request)
        response = views.PageviewsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    @mock.patch('addnow.apps.accounts.models.Site.objects.get', side_effect=mocks.mocked_site)
    def test_pageviews_authenticated2(self, mocked_site):
        site_id = 1
        request = self.factory.get(reverse('analytics:pageviews', args=[site_id]))
        self._authenticate_request(request)
        response = views.PageviewsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertTrue(mocked_site.called)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['detail'], 'Analytics view (profile) ID does not provided for this site')

    @mock.patch('addnow.apps.analytics.utils.get_report_data')
    @mock.patch('addnow.apps.accounts.models.Site.objects.get', side_effect=mocks.mocked_site)
    def test_pageviews_authenticated3(self, mocked_site, get_report_data):
        site_id = 2
        request = self.factory.get(reverse('analytics:pageviews', args=[site_id]))
        self._authenticate_request(request)
        response = views.PageviewsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(mocked_site.called)
        self.assertTrue(get_report_data.called)
        self.assertIsInstance(response.data, mock.MagicMock)

    def test_referring_domains(self):
        request = self.factory.get(reverse('analytics:referring_domains', args=['1']))
        response = views.ReferringDomainsView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_referring_domains_authenticated1(self):
        site_id = 1
        request = self.factory.get(reverse('analytics:referring_domains', args=[site_id]))
        self._authenticate_request(request)
        response = views.ReferringDomainsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    @mock.patch('addnow.apps.accounts.models.Site.objects.get', side_effect=mocks.mocked_site)
    def test_referring_domains_authenticated2(self, mocked_site):
        site_id = 1
        request = self.factory.get(reverse('analytics:referring_domains', args=[site_id]))
        self._authenticate_request(request)
        response = views.ReferringDomainsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertTrue(mocked_site.called)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['detail'], 'Analytics view (profile) ID does not provided for this site')

    @mock.patch('addnow.apps.analytics.utils.get_report_data')
    @mock.patch('addnow.apps.accounts.models.Site.objects.get', side_effect=mocks.mocked_site)
    def test_referring_domains_authenticated3(self, mocked_site, get_report_data):
        site_id = 2
        request = self.factory.get(reverse('analytics:referring_domains', args=[site_id]))
        self._authenticate_request(request)
        response = views.ReferringDomainsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(mocked_site.called)
        self.assertTrue(get_report_data.called)
        self.assertIsInstance(response.data, mock.MagicMock)

    def test_search_terms(self):
        request = self.factory.get(reverse('analytics:search_terms', args=['1']))
        response = views.SearchTermsView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_terms_authenticated1(self):
        site_id = 1
        request = self.factory.get(reverse('analytics:search_terms', args=[site_id]))
        self._authenticate_request(request)
        response = views.SearchTermsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    @mock.patch('addnow.apps.accounts.models.Site.objects.get', side_effect=mocks.mocked_site)
    def test_search_terms_authenticated2(self, mocked_site):
        site_id = 1
        request = self.factory.get(reverse('analytics:search_terms', args=[site_id]))
        self._authenticate_request(request)
        response = views.SearchTermsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertTrue(mocked_site.called)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['detail'], 'Analytics view (profile) ID does not provided for this site')

    @mock.patch('addnow.apps.analytics.utils.get_report_data')
    @mock.patch('addnow.apps.accounts.models.Site.objects.get', side_effect=mocks.mocked_site)
    def test_search_terms_authenticated3(self, mocked_site, get_report_data):
        site_id = 2
        request = self.factory.get(reverse('analytics:search_terms', args=[site_id]))
        self._authenticate_request(request)
        response = views.SearchTermsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(mocked_site.called)
        self.assertTrue(get_report_data.called)
        self.assertIsInstance(response.data, mock.MagicMock)

    def test_search_engines(self):
        request = self.factory.get(reverse('analytics:search_engines', args=['1']))
        response = views.SearchEnginesView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_engines_authenticated1(self):
        site_id = 1
        request = self.factory.get(reverse('analytics:search_engines', args=[site_id]))
        self._authenticate_request(request)
        response = views.SearchEnginesView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    @mock.patch('addnow.apps.accounts.models.Site.objects.get', side_effect=mocks.mocked_site)
    def test_search_engines_authenticated2(self, mocked_site):
        site_id = 1
        request = self.factory.get(reverse('analytics:search_engines', args=[site_id]))
        self._authenticate_request(request)
        response = views.SearchEnginesView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertTrue(mocked_site.called)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['detail'], 'Analytics view (profile) ID does not provided for this site')

    @mock.patch('addnow.apps.analytics.utils.get_report_data')
    @mock.patch('addnow.apps.accounts.models.Site.objects.get', side_effect=mocks.mocked_site)
    def test_search_engines_authenticated3(self, mocked_site, get_report_data):
        site_id = 2
        request = self.factory.get(reverse('analytics:search_engines', args=[site_id]))
        self._authenticate_request(request)
        response = views.SearchEnginesView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(mocked_site.called)
        self.assertTrue(get_report_data.called)
        self.assertIsInstance(response.data, mock.MagicMock)

    def test_active_visitors(self):
        request = self.factory.get(reverse('analytics:active_visitors', args=['1']))
        response = views.ActiveVisitorsView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_active_visitors_authenticated1(self):
        site_id = 1
        request = self.factory.get(reverse('analytics:active_visitors', args=[site_id]))
        self._authenticate_request(request)
        response = views.ActiveVisitorsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    @mock.patch('addnow.apps.accounts.models.Site.objects.get', side_effect=mocks.mocked_site)
    def test_active_visitors_authenticated2(self, mocked_site):
        site_id = 1
        request = self.factory.get(reverse('analytics:active_visitors', args=[site_id]))
        self._authenticate_request(request)
        response = views.ActiveVisitorsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertTrue(mocked_site.called)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['detail'], 'Analytics view (profile) ID does not provided for this site')

    @mock.patch('addnow.apps.analytics.utils.get_report_data', side_effect=mocks.get_analytics_ga_users_data)
    @mock.patch('addnow.apps.analytics.utils.get_profile', side_effect=mocks.get_analytics_profile)
    @mock.patch('addnow.apps.accounts.models.Site.objects.get', side_effect=mocks.mocked_site)
    def test_active_visitors_authenticated3(self, mocked_site, get_profile, get_report_data):
        site_id = 2
        cache.delete(analytics_settings.TIMEZONE_CACHE_KEY_PLACEHOLDER % True)
        request = self.factory.get(reverse('analytics:active_visitors', args=[site_id]) + '?history=1')
        self._authenticate_request(request)
        response = views.ActiveVisitorsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(mocked_site.called)
        self.assertTrue(get_profile.called)
        self.assertTrue(get_report_data.called)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 15)

        first = response.data[0]
        last = response.data[-1]

        expected_first = {
            'elapsed': 0,
            'geo': {'latitude': '44.2167', 'country': 'Russia', 'longitude': '42.0500', 'city': 'Cherkessk'},
        }
        expected_last = {
            'elapsed': 240,
            'geo': {'latitude': '54.5519', 'country': 'Russia', 'longitude': '36.2851', 'city': 'Kaluga'},
        }
        self.assertDictContainsSubset(expected_first, first)
        self.assertDictContainsSubset(expected_last, last)

    @mock.patch('addnow.apps.analytics.utils.get_realtime_data', side_effect=mocks.get_analytics_realtime_users_data)
    @mock.patch('addnow.apps.analytics.utils.get_profile', side_effect=mocks.get_analytics_profile)
    @mock.patch('addnow.apps.accounts.models.Site.objects.get', side_effect=mocks.mocked_site)
    def test_active_visitors_authenticated4(self, mocked_site, get_profile, get_realtime_data):
        site_id = 2
        cache.delete(analytics_settings.TIMEZONE_CACHE_KEY_PLACEHOLDER % True)
        request = self.factory.get(reverse('analytics:active_visitors', args=[site_id]) + '?history=')
        self._authenticate_request(request)
        response = views.ActiveVisitorsView.as_view()(request, site_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(mocked_site.called)
        self.assertTrue(get_profile.called)
        self.assertTrue(get_realtime_data.called)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 17)

        first = response.data[0]
        last = response.data[-1]

        expected_first = {
            'elapsed': 0,
            'geo': {'latitude': '44.216667', 'country': 'Russia', 'longitude': '42.049999', 'city': 'Cherkessk'},
        }
        expected_last = {
            'elapsed': 0,
            'geo': {'latitude': '59.934277', 'country': 'Russia', 'longitude': '30.335098', 'city': 'Saint Petersburg'},
        }
        self.assertDictContainsSubset(expected_first, first)
        self.assertDictContainsSubset(expected_last, last)
