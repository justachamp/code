# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase

from mock import call, patch, PropertyMock, MagicMock
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from addnow.apps.accounts import constants, factories, models, serializers, views


class BaseAccountsViewsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(BaseAccountsViewsTestCase, cls).setUpClass()
        cls.factory = APIRequestFactory()

    def _authenticate_request(self, request, user=None):
        user = user or factories.UserFactory(email_is_verified=True)
        token = factories.ApiTokenFactory(user=user)
        force_authenticate(request, user=token['user'], token=token)
        return token


@patch('addnow.apps.accounts.views.TokenRateThrottle.allow_request', MagicMock(return_value=True))
@patch('addnow.apps.accounts.views.UpdateAccountRateThrottle.allow_request', MagicMock(return_value=True))
class AccountsViewsTestCase(BaseAccountsViewsTestCase):
    def test__retrieve_account__ok(self):
        request = self.factory.get(reverse('accounts_account'))
        token = self._authenticate_request(request)

        response = views.AccountView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, serializers.UpdateUserSerializer(token['user']).data)

    def _get_update_account_response(self, data, user=None):
        request = self.factory.patch(reverse('accounts_account'), data=data)
        if user:
            self._authenticate_request(request, user=user)
        return views.AccountView.as_view()(request)

    def test__update_account__wrong_password(self):
        user = factories.UserFactory(email_is_verified=True)
        data = {'email': user.email + '.info', 'password': 'new', 'old_password': 'wrong'}

        response = self._get_update_account_response(data, user)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['old_password'], ['Password is incorrect'])

    def test__update_account__offset_without_password(self):
        user = factories.UserFactory(email_is_verified=True)

        data = {'offset': 0}
        response = self._get_update_account_response(data, user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('addnow.apps.accounts.views.emails')
    def test__update_account__email_without_password(self, emails):
        user = factories.UserFactory(email_is_verified=True)

        data = {'email': 'aaa@bbb.com'}
        response = self._get_update_account_response(data, user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test__update_account__wrong_offset(self):
        user = factories.UserFactory(email_is_verified=True)

        for offset in (15 * 60, -13 * 60):
            data = {'offset': offset}

            response = self._get_update_account_response(data, user)

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(response.data['offset'], ['Invalid timezone offset'])

    @patch('addnow.apps.accounts.views.emails')
    def test__update_account__ok(self, emails):
        user = factories.UserFactory(email_is_verified=True)

        data_set = [
            dict(email='some@update.account.ok', old_password='password'),
            dict(password='new_pass', old_password='password'),
            dict(offset=12*60, old_password='new_pass'),
            dict(offset=-12*60),
            dict(),
            dict(email='new@update.account.ok', password='password', old_password='new_pass', offset=0),
        ]
        for data in data_set:
            response = self._get_update_account_response(data, user)

            fresh_user = models.User.objects.get(pk=user.pk)

            self.assertEqual(response.status_code, status.HTTP_200_OK, data)
            self.assertFalse(fresh_user.email_is_verified)
            self.assertDictEqual(
                response.data,
                serializers.UpdateUserSerializer(fresh_user).data,
                msg=data
            )

        self.assertEqual(emails.verification.call_count, 2)

    def test__obtain_token__invalid_pass(self):
        data = {'email': factories.UserFactory().email, 'password': 'wrong'}
        request = self.factory.post(reverse('accounts_token'), data=data)

        response = views.ObtainJSONWebToken.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)

    def test__obtain_token_inactive_user(self):
        user = factories.UserFactory(is_active=False, email_is_verified=True)
        data = {'email': user.email, 'password': user.password}
        request = self.factory.post(reverse('accounts_token'), data=data)

        response = views.ObtainJSONWebToken.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)

    def test__obtain_token_not_email_verified_user(self):
        user = factories.UserFactory(is_active=True, email_is_verified=False)
        data = {'email': user.email, 'password': user.password}
        request = self.factory.post(reverse('accounts_token'), data=data)

        response = views.ObtainJSONWebToken.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'], ['Unable to login with provided credentials.'])

    def test__obtain_token_incomplete_credentials(self):
        user = factories.UserFactory(is_active=True, email_is_verified=True)
        data = {'email': user.email}
        request = self.factory.post(reverse('accounts_token'), data=data)

        response = views.ObtainJSONWebToken.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'password': ['This field is required.']})
        self.assertNotIn('token', response.data)

    def test__obtain_token__ok(self):
        user = factories.UserFactory(email_is_verified=True)
        data = {'email': user.email, 'password': 'password'}
        request = self.factory.post(reverse('accounts_token'), data=data)

        response = views.ObtainJSONWebToken.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('addnow.apps.accounts.views.emails')
    def test__create_account(self, emails):
        data = {'email': 'new_email@ex.com', 'password': 'pass!word'}
        request = self.factory.post(reverse('accounts_create_user'), data=data)

        response = views.RegisterUserView.as_view()(request)

        user = models.User.objects.get(email=data['email'])
        expected_data = {
            'email': data['email'],
            'id': user.pk
        }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictEqual(response.data, expected_data)
        self.assertTrue(user.check_password(data['password']))
        emails.verification.assert_called_once_with(user)
        # Check in case invalid data
        data = {'email': 'bad_email', 'password': 'pass!word'}
        request = self.factory.post(reverse('accounts_create_user'), data=data)
        response = views.RegisterUserView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test__verify_email(self):
        user = factories.UserFactory()
        user.email_is_verified = False
        self.assertFalse(user.email_is_verified)
        args = (user.generate_email_token(),)
        path = reverse('accounts_email_verification', args=args)
        request = self.factory.get(path)

        response = views.EmailVerificationView.as_view()(request, *args)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(models.User.objects.get(pk=user.pk).email_is_verified)
        # validate_email_token == False
        with patch('addnow.apps.accounts.models.User.validate_email_token', MagicMock(return_value=False)):
            request = self.factory.get(path)
            response = views.EmailVerificationView.as_view()(request, *args)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('addnow.apps.accounts.views.emails')
    def test__password_reset__attempt(self, emails):
        user = factories.UserFactory(email_is_verified=True)
        data = {'email': user.email}
        path = reverse('accounts_password_reset_attempt')
        request = self.factory.post(path, data=data)

        response = views.PasswordResetAttemptView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        emails.password_reset_attempt.assert_called_once_with(user)

        # Case when password reset's data is invalid
        data = {'email': 'invalid_email'}
        request = self.factory.post(path, data=data)

        response = views.PasswordResetAttemptView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # email not found
        data = {'email': 'matias@gmail.com'}
        request = self.factory.post(path, data=data)

        response = views.PasswordResetAttemptView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # inactive user
        user = factories.UserFactory(is_active=False)
        data = {'email': user.email}
        request = self.factory.post(path, data=data)

        response = views.PasswordResetAttemptView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # email verified == False
        user = factories.UserFactory(email_is_verified=False)
        data = {'email': user.email}
        request = self.factory.post(path, data=data)

        response = views.PasswordResetAttemptView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test__password_reset__confirm(self):
        user = factories.UserFactory(email_is_verified=True)
        args = (str(user.pk), user.generate_password_reset_token())
        data = {'token': '|'.join(args), 'password': '123456'}
        path = reverse('accounts_password_reset_confirm')
        self.assertFalse(user.check_password(data['password']))

        request = self.factory.post(path, data=data)
        response = views.PasswordResetConfirmView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        user = models.User.objects.get(email=user.email)
        self.assertTrue(user.check_password(data['password']))

        # Invalid password
        data = {'token': '|'.join(args), 'password': 'awwww'}
        request = self.factory.post(path, data=data)
        response = views.PasswordResetConfirmView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Invalid data separator
        args = (str(user.pk), user.generate_password_reset_token())
        data = {'token': ','.join(args), 'password': '123456'}
        request = self.factory.post(path, data=data)
        response = views.PasswordResetConfirmView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SitesViewsTestCase(BaseAccountsViewsTestCase):
    @classmethod
    def setUpClass(cls):
        super(SitesViewsTestCase, cls).setUpClass()
        cls.path = reverse('accounts_sites')

    def setUp(self):
        super(SitesViewsTestCase, self).setUp()
        self.data = {'domain': 'example.com'}

    def test__sites__create__unauthorized(self):
        request = self.factory.post(self.path, data={})
        response = views.SiteListCreateView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test__sites__create__ok(self):
        self.data['domain'] = 'another.domain.com'
        request = self.factory.post(self.path, data=self.data)
        token = self._authenticate_request(request)
        response = views.SiteListCreateView.as_view()(request)
        site = models.Site.objects.get(pk=response.data['id'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(site.user_id, token['user'].pk)  # owner
        self.assertEqual(site.domain, self.data['domain'])

    def test__sites__create__duplicate(self):
        request = self.factory.post(self.path, data=self.data)
        self._authenticate_request(request)
        views.SiteListCreateView.as_view()(request)

        request = self.factory.post(self.path, data=self.data)
        self._authenticate_request(request)
        response = views.SiteListCreateView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test__sites__create__with_social_urls(self):
        self.data['social_urls'] = [{'service': 'facebook', 'url': 'http://test.com'}]
        self.data['domain'] = 'a.new.domain.com'

        request = self.factory.post(self.path, data=self.data)
        self._authenticate_request(request)
        response = views.SiteListCreateView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        social_url = models.SocialUrl.objects.get(site__pk=response.data['id'])
        self.assertEqual(social_url.pk, response.data['social_urls'][0]['id'])

    def test__sites__list__unauthorized(self):
        request = self.factory.get(self.path)
        response = views.SiteListCreateView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test__sites__list__ok(self):
        social_url = factories.FacebookUrlFactory()
        factories.GoogleUrlFactory(site=social_url.site)

        factories.SiteFactory(user=social_url.site.user)  # second site for authenticated user
        factories.SiteFactory()  # some random site

        request = self.factory.get(self.path)
        self._authenticate_request(request, user=social_url.site.user)
        response = views.SiteListCreateView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.__len__(), 2)


class SiteDetailViewsTestCase(BaseAccountsViewsTestCase):
    def test__site_detail__unauthorized(self):
        site = factories.SiteFactory()
        request = self.factory.get(reverse('accounts_site_detail', args=[site.pk]))
        self._authenticate_request(request)

        response = views.SiteRetrieveUpdateView.as_view()(request, pk=site.pk)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertDictEqual(response.data, {'detail': 'Not found.'})

    def test__site_detail__get(self):
        site = factories.SiteFactory()
        request = self.factory.get(reverse('accounts_site_detail', args=[site.pk]))
        self._authenticate_request(request, user=site.user)

        response = views.SiteRetrieveUpdateView.as_view()(request, pk=site.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, serializers.SiteSerializer(site).data)

    @patch('addnow.apps.accounts.views.SiteSettingsCache')
    def test__site_detail__update(self, cache):
        site = factories.SiteFactory()
        widget_configuration = factories.WidgetConfigurationFactory()

        data_set = [
            dict(domain='new_site_detail.com'),
            dict(social_urls=[{'service': 'facebook', 'url': 'http://fb.test.com'}]),
            dict(address_bar_sharing=True, widget_configurations=[widget_configuration.pk]),
        ]

        for data in data_set:
            request = self.factory.patch(reverse('accounts_site_detail', args=[site.pk]), data=data)
            self._authenticate_request(request, user=site.user)

            response = views.SiteRetrieveUpdateView.as_view()(request, pk=site.pk)

            self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
            fresh_site = models.Site.objects.get(pk=site.pk)
            self.assertDictEqual(response.data, serializers.SiteSerializer(fresh_site).data, msg=data)

        cache.delete.assert_called_with(dict(site_id=site.pk))
        self.assertEqual(cache.delete.call_count, 3)

    @patch('addnow.apps.accounts.views.SiteSettingsCache')
    @patch('addnow.apps.accounts.models.Site.hash_id', PropertyMock(return_value='1234'))
    def test__site_detail__update_when_model_has_social_urls(self, cache):
        site = factories.SiteFactory()
        data = {
            'domain': 'test.pt',
            'thank_you_message': 'test thank you message',
            'thank_you_advert_image_url': 'http://mydomain.com/test.png',
            'thank_you_advert_url': 'http://mydomain.com',
            'thank_you_advert_title': 'some title',
            'social_urls': [
                {
                    'service': 'facebook',
                    'url': 'facebook.com/newTestUrl'
                },
                {
                    'service': 'twitter',
                    'url': 'twitter.com/newTestUrl'
                }
            ],
            'address_bar_sharing': True,
            'copy_paste_sharing': True,
            'has_short_urls': True,
            'trim_api_key': '7ec3c5647b5c732db85d11deca8f6d95',
            'hash_id': '1234',
            'analytics_account': 'ac',
            'analytics_property': 'prop',
            'analytics_profile': 'prof',
            'vanity_domain': ''
        }
        request = self.factory.patch(reverse('accounts_site_detail', args=[site.pk]), data)
        self._authenticate_request(request, user=site.user)

        response = views.SiteRetrieveUpdateView.as_view()(request, pk=site.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = data.copy()
        expected['id'] = site.pk
        facebook_social_url_id = models.SocialUrl.objects.get(site__pk=site.pk, service='facebook').pk
        twitter_social_url_id = models.SocialUrl.objects.get(site__pk=site.pk, service='twitter').pk
        expected['social_urls'][0]['id'] = facebook_social_url_id
        expected['social_urls'][1]['id'] = twitter_social_url_id
        self.assertEqual(response.data, expected)
        cache.delete.assert_called_with(dict(site_id=site.pk))
        self.assertEqual(cache.delete.call_count, 1)

        # Delete twitter service from social_url
        data['social_urls'] = [{'service': 'facebook', 'url': 'facebook.com/newTestUrl'}]
        request = self.factory.put(reverse('accounts_site_detail', args=[site.pk]), data)
        self._authenticate_request(request, user=site.user)

        response = views.SiteRetrieveUpdateView.as_view()(request, pk=site.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = data.copy()
        expected['id'] = site.pk
        facebook_social_url_id = models.SocialUrl.objects.get(site__pk=site.pk, service='facebook').pk
        expected['social_urls'][0]['id'] = facebook_social_url_id
        self.assertEqual(response.data, expected)

    def test__site_detail__update_social_urls_with_duplicates(self):
        site = factories.SiteFactory()
        data = {
            'social_urls': [
                {
                    'service': 'facebook',
                    'url': 'facebook.com/testUrl'
                },
                {
                    'service': 'facebook',
                    'url': 'twitter.com/duplicateServiceUrl'
                }
            ]
        }
        request = self.factory.patch(
            reverse('accounts_site_detail', args=[site.pk]), data)
        self._authenticate_request(request, user=site.user)

        response = views.SiteRetrieveUpdateView.as_view()(request, pk=site.pk)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['social_urls'], ['Service must be unique for the site.'])


class WidgetsViewsTestCase(BaseAccountsViewsTestCase):
    @classmethod
    def setUpClass(cls):
        super(WidgetsViewsTestCase, cls).setUpClass()
        cls.site = factories.SiteFactory()
        cls.path = reverse('accounts_widgets', args=[cls.site.pk])

    def setUp(self):
        super(WidgetsViewsTestCase, self).setUp()
        self.data = {
            'name': 'Default',
            'type': constants.WIDGET_CONFIGURATION_SHARING_BUTTONS,
            'orientation': constants.BUTTON_ORIENTATION_HORIZONTAL,
            'button_size': constants.BUTTON_SIZE_MEDIUM,
            'button_style': constants.BUTTON_STYLE_ICON,
            'counter_position': constants.COUNTER_POSITION_RIGHT,
            'buttons': [{'service': 'facebook'}, {'service': 'twitter'}]
        }

    def _create_widget(self, authenticate=True, site=None):
        request = self.factory.post(self.path, data=self.data)
        site = site or self.site
        token = None
        if authenticate:
            token = self._authenticate_request(request, user=site.user)
        response = views.WidgetListCreateView.as_view()(request, site_pk=site.pk)
        return response, token

    def test__widgets__create__unauthorized(self):
        response, _ = self._create_widget(authenticate=False)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @patch('addnow.apps.accounts.views.SiteSettingsCache')
    def test__widgets__create__ok(self, cache):
        response, token = self._create_widget()
        widget = models.WidgetConfiguration.objects.get(pk=response.data['id'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(widget.site.user.id, token['user'].pk)  # owner
        self.assertEqual(widget.name, self.data['name'])
        self.assertEqual(widget.buttons.get(service='facebook').order, 0)
        self.assertEqual(widget.buttons.get(service='twitter').order, 1)

        cache.delete.assert_called_with(dict(site_id=self.site.pk))
        self.assertEqual(cache.delete.call_count, 1)

    def test__widgets__create__without_buttons(self):
        self.data['buttons'] = []

        response, _ = self._create_widget()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['buttons'], ['Widget configuration has no buttons.'])

    def test__widgets__create__more_than_one_allowed(self):
        user1 = factories.UserFactory()
        user2 = factories.UserFactory()
        site1 = factories.SiteFactory(user=user1)
        site2 = factories.SiteFactory(user=user1)
        site3 = factories.SiteFactory(user=user2)
        allow_many_widgets = [
            constants.WIDGET_CONFIGURATION_SHARING_BUTTONS,
            constants.WIDGET_CONFIGURATION_ORIGIN_BUTTONS,
            constants.WIDGET_CONFIGURATION_FOLLOW
        ]
        self.data.update({
            'position': constants.WIDGET_LEFT_POSITION,
            'page_title': 'Page title',
            'page_url': 'http://example.com',
            'media_url': 'http://media.com',
            'min_width': 0,
        })

        for widget_type in allow_many_widgets:
            self.data['type'] = widget_type
            # First creation
            response, _ = self._create_widget(site=site1)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            # Second creation for the same user and the same site
            self.data['name'] += '1'
            response, _ = self._create_widget(site=site1)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            # Second creation for the same user and another site
            self.data['name'] += '2'
            response, _ = self._create_widget(site=site2)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            # Second creation for another user
            self.data['name'] += '3'
            response, _ = self._create_widget(site=site3)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test__widgets__create__more_than_one_disallowed(self):
        user1 = factories.UserFactory()
        user2 = factories.UserFactory()
        site1 = factories.SiteFactory(user=user1)
        site2 = factories.SiteFactory(user=user1)
        site3 = factories.SiteFactory(user=user2)
        disallow_many_widgets = [
            constants.WIDGET_CONFIGURATION_COPY_PASTE,
            constants.WIDGET_CONFIGURATION_NEWSLETTER,
            constants.WIDGET_CONFIGURATION_MOBILE,
            constants.WIDGET_CONFIGURATION_VERTICAL_FLOAT
        ]
        self.data.update({
            'position': constants.WIDGET_LEFT_POSITION,
            'page_title': 'Page title',
            'page_url': 'http://example.com',
            'media_url': 'http://media.com',
            'min_width': 0,
        })

        for widget_type in disallow_many_widgets:
            self.data['type'] = widget_type
            # First creation
            response, _ = self._create_widget(site=site1)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            # Second creation fails for the same user and the same site
            self.data['name'] += '1'
            response, _ = self._create_widget(site=site1)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(response.data['non_field_errors'], [
                'You can not create more than one widget of this type.'
            ])
            # Second creation doesn't fail for the same user and another site
            self.data['name'] += '2'
            response, _ = self._create_widget(site=site2)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            # Second creation doesn't fail for another user
            self.data['name'] += '3'
            response, _ = self._create_widget(site=site3)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test__widgets__list__unauthorized(self):
        request = self.factory.get(self.path)
        response = views.WidgetListCreateView.as_view()(request, site_pk=self.site.pk)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test__widgets__list__ok(self):
        widget = factories.WidgetConfigurationFactory(site=self.site)
        factories.WidgetConfigurationFactory(site=widget.site)
        factories.WidgetConfigurationFactory()  # widget configuration of another user

        request = self.factory.get(self.path)
        self._authenticate_request(request, user=self.site.user)
        response = views.WidgetListCreateView.as_view()(request, site_pk=self.site.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.__len__(), 2)


class WidgetDetailViewsTestCase(BaseAccountsViewsTestCase):
    def test__widget_detail__unauthorized(self):
        site = factories.SiteFactory()
        widget = factories.WidgetConfigurationFactory(site=site)

        request = self.factory.get(reverse('accounts_widget_detail', args=[site.pk, widget.pk]))
        # self._authenticate_request(request)

        response = views.WidgetRetrieveUpdateView.as_view()(request, site_pk=site.pk, widget_pk=widget.pk)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertDictEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

    def test__widget_detail__get(self):
        serializers_map = {
            'sharing-buttons': serializers.SharingButtonsWidgetSerializer,
            'copy-paste': serializers.CopyPasteWidgetSerializer,
            'newsletter': serializers.NewsletterWidgetSerializer
        }

        for widget_type, serializer in serializers_map.items():
            site = factories.SiteFactory()
            widget = factories.WidgetConfigurationFactory(site=site, type=widget_type)

            request = self.factory.get(
                reverse('accounts_widget_detail', args=[site.pk, widget.pk]))
            self._authenticate_request(request, user=widget.site.user)

            response = views.WidgetRetrieveUpdateView.as_view()(
                request, site_pk=site.pk, widget_pk=widget.pk)

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertDictEqual(response.data, serializer(widget).data)

    @patch('addnow.apps.accounts.views.SiteSettingsCache')
    def test__widget_detail__update(self, cache):
        site = factories.SiteFactory()
        widget = factories.WidgetConfigurationFactory(site=site)

        data_set = [
            dict(name='new_widget_configuration_title'),
            dict(buttons=[
                {'service': 'facebook', 'is_extra_button': True},
                {'service': 'twitter', 'is_extra_button': False}
            ]),
            dict(orientation=constants.BUTTON_ORIENTATION_VERTICAL),
            dict(is_active=False),
        ]

        for data in data_set:
            request = self.factory.patch(
                reverse('accounts_widget_detail', args=[site.pk, widget.pk]),
                data=data
            )
            self._authenticate_request(request, user=widget.site.user)

            response = views.WidgetRetrieveUpdateView.as_view()(
                request, site_pk=site.pk, widget_pk=widget.pk)

            self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
            fresh_widget_configuration = models.WidgetConfiguration.objects.get(pk=widget.pk)
            self.assertDictEqual(
                response.data,
                serializers.SharingButtonsWidgetSerializer(fresh_widget_configuration).data,
                msg=data
            )
        cache.delete.assert_has_calls([call(dict(site_id=site.pk))])
        self.assertEqual(cache.delete.call_count, 4)

    @patch('addnow.apps.accounts.views.SiteSettingsCache')
    def test__widget_detail__update_buttons(self, cache):
        site = factories.SiteFactory()
        widget = factories.WidgetConfigurationFactory(site=site)

        factories.FacebookWidgetButtonFactory(order=0, configuration=widget)
        factories.GoogleWidgetButtonFactory(order=1, configuration=widget, is_extra_button=True)
        data = {
            'name': 'New title',
            'type': constants.WIDGET_CONFIGURATION_SHARING_BUTTONS,
            'orientation': constants.BUTTON_ORIENTATION_VERTICAL,
            'extra_button_animation': False,
            'button_size': constants.BUTTON_SIZE_SMALL,
            'button_style': constants.BUTTON_STYLE_ICON,
            'counter_position': constants.COUNTER_POSITION_TOP,
            'is_active': True,
            'has_link_share_button': False,
            'buttons': [
                {
                    'service': 'twitter',
                    'is_extra_button': False,
                    'is_short_link': True,
                    'text': 'Twitter',
                    'has_counter': True,
                    'follow_url': ''
                },
                {
                    'service': 'facebook',
                    'is_extra_button': False,
                    'is_short_link': True,
                    'text': 'Facebook',
                    'has_counter': True,
                    'follow_url': ''
                },
                {
                    'service': 'googlePlus',
                    'is_extra_button': False,
                    'is_short_link': True,
                    'text': 'Google+',
                    'has_counter': True,
                    'follow_url': ''
                },
                {
                    'service': 'pinterest',
                    'is_extra_button': False,
                    'is_short_link': False,
                    'text': 'Pinterest',
                    'has_counter': True,
                    'follow_url': ''
                }
            ]
        }
        request = self.factory.patch(
            reverse('accounts_widget_detail', args=[site.pk, widget.pk]), data)
        self._authenticate_request(request, user=widget.site.user)

        response = views.WidgetRetrieveUpdateView.as_view()(
            request, site_pk=site.pk, widget_pk=widget.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = data.copy()
        expected['id'] = widget.pk
        expected['vanity_domain'] = ''
        expected['position'] = ''
        self.assertDictEqual(response.data, expected)
        cache.delete.assert_called_with(dict(site_id=site.pk))
        self.assertEqual(cache.delete.call_count, 1)

    @patch('addnow.apps.accounts.views.SiteSettingsCache')
    def test__widget_detail__update_buttons_plus(self, cache):
        site = factories.SiteFactory()
        widget = factories.WidgetConfigurationFactory(site=site)

        factories.FacebookWidgetButtonFactory(order=0, configuration=widget, is_extra_button=False)
        factories.GoogleWidgetButtonFactory(order=1, configuration=widget, is_extra_button=False)
        data = {
            'name': 'New title',
            'type': constants.WIDGET_CONFIGURATION_SHARING_BUTTONS,
            'extra_button_animation': False,
            'orientation': constants.BUTTON_ORIENTATION_VERTICAL,
            'button_size': constants.BUTTON_SIZE_SMALL,
            'button_style': constants.BUTTON_STYLE_ICON,
            'counter_position': constants.COUNTER_POSITION_TOP,
            'is_active': True,
            'has_link_share_button': False,
            'buttons': [
                {
                    'service': 'googlePlus',
                    'is_extra_button': True,
                    'is_short_link': True,
                    'text': 'Google+',
                    'has_counter': True,
                    'follow_url': ''
                },
                {
                    'service': 'facebook',
                    'is_extra_button': True,
                    'is_short_link': True,
                    'text': 'Facebook',
                    'has_counter': True,
                    'follow_url': ''
                }
            ]
        }
        request = self.factory.patch(
            reverse('accounts_widget_detail', args=[site.pk, widget.pk]), data)
        self._authenticate_request(request, user=widget.site.user)

        response = views.WidgetRetrieveUpdateView.as_view()(
            request, site_pk=site.pk, widget_pk=widget.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = data.copy()
        expected['id'] = widget.pk
        expected['vanity_domain'] = ''
        expected['position'] = ''
        self.assertDictEqual(response.data, expected)
        cache.delete.assert_called_with(dict(site_id=site.pk))
        self.assertEqual(cache.delete.call_count, 1)

    @patch('addnow.apps.accounts.views.SiteSettingsCache')
    def test__newsletter_widget_detail__email_source(self, cache):
        site = factories.SiteFactory()
        widget = factories.WidgetConfigurationFactory(site=site, type=constants.WIDGET_CONFIGURATION_NEWSLETTER)

        factories.FacebookWidgetButtonFactory(order=0, configuration=widget)
        data = {
            'name': 'New title',
            'type': constants.WIDGET_CONFIGURATION_SHARING_BUTTONS,
            'orientation': constants.BUTTON_ORIENTATION_VERTICAL,
            'button_size': constants.BUTTON_SIZE_SMALL,
            'button_style': constants.BUTTON_STYLE_ICON,
            'counter_position': constants.COUNTER_POSITION_TOP,
            'is_active': True,
            'buttons': [
                {
                    'service': 'email',
                    'is_extra_button': True,
                    'is_short_link': True,
                    'text': 'Email',
                    'has_counter': False,
                    'follow_url': ''
                }
            ]
        }
        request = self.factory.patch(reverse('accounts_widget_detail', args=[site.pk, widget.pk]), data)
        self._authenticate_request(request, user=widget.site.user)

        response = views.WidgetRetrieveUpdateView.as_view()(request, site_pk=site.pk, widget_pk=widget.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = data.copy()
        expected['id'] = widget.pk
        expected['vanity_domain'] = ''
        self.assertEqual(response.data['buttons'], expected['buttons'])
        cache.delete.assert_called_with(dict(site_id=site.pk))
        self.assertEqual(cache.delete.call_count, 1)

    @patch('addnow.apps.accounts.views.SiteSettingsCache')
    def test__newsletter_widget_detail__update_media_url(self, cache):
        site = factories.SiteFactory()
        widget = factories.WidgetConfigurationFactory(site=site, type=constants.WIDGET_CONFIGURATION_NEWSLETTER)

        factories.FacebookWidgetButtonFactory(order=0, configuration=widget)
        factories.GoogleWidgetButtonFactory(order=1, configuration=widget)
        data = {
            'buttons': [
                {'service': 'twitter', 'is_extra_button': True},
                {'service': 'facebook', 'is_extra_button': True},
                {'service': 'pinterest', 'is_extra_button': True}
            ],
            'media_url': 'http://test.com'
        }
        request = self.factory.patch(
            reverse('accounts_widget_detail', args=[site.pk, widget.pk]), data)
        self._authenticate_request(request, user=widget.site.user)

        response = views.WidgetRetrieveUpdateView.as_view()(request, site_pk=site.pk, widget_pk=widget.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['media_url'], 'http://test.com')
        cache.delete.assert_called_with(dict(site_id=site.pk))
        self.assertEqual(cache.delete.call_count, 1)

        # data without pinterest social service
        data = {
            'buttons': [{'service': 'twitter', 'is_extra_button': True}],
            'media_url': 'http://test.com'
        }
        request = self.factory.patch(reverse('accounts_widget_detail', args=[site.pk, widget.pk]), data)
        self._authenticate_request(request, user=widget.site.user)

        response = views.WidgetRetrieveUpdateView.as_view()(request, site_pk=site.pk, widget_pk=widget.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['media_url'], 'http://test.com')
        cache.delete.assert_called_with(dict(site_id=site.pk))
        self.assertEqual(cache.delete.call_count, 2)

    @patch('addnow.apps.accounts.views.SiteSettingsCache')
    def test__newsletter_widget_detail__update_without_media_url(self, cache):
        site = factories.SiteFactory()
        widget = factories.WidgetConfigurationFactory(site=site, type=constants.WIDGET_CONFIGURATION_NEWSLETTER)

        factories.FacebookWidgetButtonFactory(order=0, configuration=widget)
        factories.GoogleWidgetButtonFactory(order=1, configuration=widget)
        data = {
            'buttons': [{'service': 'twitter'}, {'service': 'facebook'}, {'service': 'pinterest'}]
        }
        request = self.factory.patch(reverse('accounts_widget_detail', args=[site.pk, widget.pk]), data)
        self._authenticate_request(request, user=widget.site.user)

        response = views.WidgetRetrieveUpdateView.as_view()(request, site_pk=site.pk, widget_pk=widget.pk)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['media_url'], ['This field is required.'])

        # data without pinterest social service
        data = {
            'buttons': [{'service': 'twitter'}]
        }
        request = self.factory.patch(reverse('accounts_widget_detail', args=[site.pk, widget.pk]), data)
        self._authenticate_request(request, user=widget.site.user)

        response = views.WidgetRetrieveUpdateView.as_view()(request, site_pk=site.pk, widget_pk=widget.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cache.delete.assert_called_with(dict(site_id=site.pk))
        self.assertEqual(cache.delete.call_count, 1)

    def test__widget_detail__update_buttons_with_duplicates(self):
        site = factories.SiteFactory()
        widget = factories.WidgetConfigurationFactory(site=site)

        data = {
            'buttons': [{'service': 'facebook'}, {'service': 'facebook'}]
        }
        request = self.factory.patch(reverse('accounts_widget_detail', args=[site.pk, widget.pk]), data)
        self._authenticate_request(request, user=widget.site.user)

        response = views.WidgetRetrieveUpdateView.as_view()(request, site_pk=site.pk, widget_pk=widget.pk)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['buttons'], ['Service must be unique for the widget configuration.'])
