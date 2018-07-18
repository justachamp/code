# -*- coding: utf-8 -*-
from django.db import migrations

from addnow.apps.accounts.constants import *


def filter_instagram(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    WidgetButton = apps.get_model('accounts', 'WidgetButton')

    for button in WidgetButton.objects.filter(configuration__type=WIDGET_CONFIGURATION_VERTICAL_FLOAT):
        if button.service == SOCIAL_SERVICE_INSTAGRAM:
            button.delete()


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_newsletter_buttons'),
    ]

    operations = [
        migrations.RunPython(filter_instagram, reverse)
    ]
