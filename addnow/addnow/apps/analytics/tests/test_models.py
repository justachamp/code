from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase

from oauth2client.client import OAuth2Credentials
from oauth2client.contrib.django_orm import Storage

from addnow.apps.analytics.factories import UserFactory, CredentialsModelFactory
from addnow.apps.analytics.models import CredentialsModel


class TestCredentialsModel(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCredentialsModel, cls).setUpClass()
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
        cls.user_without_analytics = UserFactory(has_analytics=False)
        cls.user_with_analytics = UserFactory(has_analytics=True)
        cls.credentials = CredentialsModelFactory(user=cls.user_with_analytics, credential=cls.credential)

    def test_users(self):
        self.assertIsInstance(self.user_without_analytics, get_user_model())
        self.assertIsInstance(self.user_with_analytics, get_user_model())

    def test_credentials_created(self):
        self.assertNotEqual(self.credentials.user, self.user_without_analytics)
        self.assertEqual(self.credentials.user, self.user_with_analytics)
        self.assertEqual(self.credentials.credential, self.credential)

    def test_storage(self):
        storage = Storage(CredentialsModel, 'user', self.user_with_analytics, 'credential')
        credential = storage.get()

        self.assertIsInstance(storage, Storage)
        self.assertIsInstance(credential, OAuth2Credentials)
        self.assertEqual(credential.access_token, self.credential.access_token)

    def test_delete_handler(self):
        user = get_user_model().objects.get(pk=self.user_with_analytics.pk)

        self.assertTrue(user.has_analytics)
        self.assertEqual(CredentialsModel.objects.all().count(), 1)

        storage = Storage(CredentialsModel, 'user', user, 'credential')
        storage.delete()

        user = get_user_model().objects.get(pk=self.user_with_analytics.pk)
        self.assertFalse(user.has_analytics)
        self.assertEqual(CredentialsModel.objects.all().count(), 0)
