# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.signing import Signer
from django.test import TestCase

from mock import patch, PropertyMock

from addnow.apps.accounts import constants, factories, models


class TestModels(TestCase):
    def test__user_manager(self):
        user_manager = models.User.objects
        user = user_manager.create_user('normal@mail.com', '1234')
        self.assertIn(user, models.User.objects.all())
        super_user = user_manager.create_superuser('super@mail.com', '1234')
        self.assertIn(super_user, models.User.objects.all())

    def test__user_model(self):
        user = models.User.objects.create('user@mail.com', '1234', is_admin=True)
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.has_sites, 0)
        self.assertEqual(user.get_full_name(), 'user@mail.com')
        self.assertEqual(user.get_short_name(), 'user@mail.com')
        self.assertEqual(user.has_perm(''), True)
        self.assertEqual(user.has_module_perms(''), True)

    def test__all_widgets(self):
        all_widgets = (
            (constants.WIDGET_CONFIGURATION_SHARING_BUTTONS, models.SharingButtonsWidget),
            (constants.WIDGET_CONFIGURATION_COPY_PASTE, models.CopyPasteWidget),
            (constants.WIDGET_CONFIGURATION_NEWSLETTER, models.NewsletterWidget),
            (constants.WIDGET_CONFIGURATION_MOBILE, models.MobileWidget),
            (constants.WIDGET_CONFIGURATION_FOLLOW, models.FollowWidget),
        )
        for widget_type, class_instance in all_widgets:
            site = factories.SiteFactory()
            class_instance.objects.all().delete()
            for i in range(5):
                factories.WidgetConfigurationFactory(site=site, type=widget_type)
            # Check it from the object's manager
            self.assertEqual(class_instance.objects.all().count(), 5)

    def test__site_get_id_by_hash(self):
        site = factories.SiteFactory()
        site_id_int = str(site.pk)
        self.assertEqual(models.Site.get_id_by_hash(site_id_int), site_id_int)
        signer = Signer()
        site_id = signer.sign(site.pk)
        self.assertEqual(models.Site.get_id_by_hash(site_id), site_id_int)

    @patch('addnow.apps.accounts.models.Site.hash_id', PropertyMock(return_value='13:NJPFNaC41thbepMv_YjCqSefKlg'))
    def test__site_get_config(self):
        site = factories.SiteFactory(domain='test.com', thank_you_message='test')
        expected = {
            'hash_id': '13:NJPFNaC41thbepMv_YjCqSefKlg',
            'sharing': {
                'byHash': False,
                'copyPaste': False,
                'hasShortUrls': True
            },
            'thank_you': {
                'services': {},
                'message': 'test',
                'advertImageUrl': '',
                'advertTitle': '',
                'advertUrl': '',
            },
            'widget_configurations': [],
            'offset': 0,
            'dmp_execute_code': False,
            'vanity_domain': ''
        }

        self.assertDictEqual(site.get_config(), expected)

    @patch('addnow.apps.accounts.models.Site.hash_id', PropertyMock(return_value='13:NJPFNaC41thbepMv_YjCqSefKlg'))
    def test__site_get_config_with_social_urls(self):
        site = factories.SiteFactory(domain='test.com', thank_you_message='test')
        factories.FacebookUrlFactory(url='social1.com/test', site=site)
        factories.GoogleUrlFactory(url='social2.com/test', site=site)

        expected = {
            'hash_id': '13:NJPFNaC41thbepMv_YjCqSefKlg',
            'sharing': {
                'byHash': False,
                'copyPaste': False,
                'hasShortUrls': True
            },
            'thank_you': {
                'services': {
                    'facebook': 'social1.com/test',
                    'googlePlus': 'social2.com/test'
                },
                'message': 'test',
                'advertImageUrl': '',
                'advertTitle': '',
                'advertUrl': '',
            },
            'widget_configurations': [],
            'offset': 0,
            'dmp_execute_code': False,
            'vanity_domain': ''
        }

        self.assertEqual(site.get_config(), expected)
