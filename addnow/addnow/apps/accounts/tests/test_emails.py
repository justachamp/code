# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from mock import patch

from addnow.apps.accounts import factories
from addnow.apps.accounts.emails import password_reset_attempt, verification, encouraging_email


class TestEmails(TestCase):
    @patch('addnow.apps.accounts.emails.send_post_office_email')
    def test__verification(self, send_email):
        user = factories.UserFactory()
        verification(user)
        send_email.assert_called_once()

    @patch('addnow.apps.accounts.emails.send_post_office_email')
    def test__password_reset_attempt(self, send_email):
        user = factories.UserFactory()
        password_reset_attempt(user)
        send_email.assert_called_once()

    @patch('addnow.apps.accounts.emails.send_post_office_email')
    def test__encouraging_email(self, send_email):
        user = factories.UserFactory()
        encouraging_email(user, 'template_name')
        send_email.assert_called_once()
