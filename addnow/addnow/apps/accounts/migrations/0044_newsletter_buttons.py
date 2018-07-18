# -*- coding: utf-8 -*-
from django.db import migrations

from addnow.apps.accounts.constants import *


def filter_newsletter(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    WidgetButton = apps.get_model('accounts', 'WidgetButton')

    for button in WidgetButton.objects.filter(configuration__type=WIDGET_CONFIGURATION_NEWSLETTER):
        if button.service not in [SOCIAL_SERVICE_FACEBOOK, SOCIAL_SERVICE_TWITTER,
                                  SOCIAL_SERVICE_GOOGLE_PLUS, SOCIAL_SERVICE_LINKEDIN,
                                  SOCIAL_SERVICE_PINTEREST]:
            button.delete()


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0043_site_vanity_domain'),
    ]

    operations = [
        migrations.RunPython(filter_newsletter, reverse)
    ]
