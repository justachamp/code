# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def turn_has_short_urls_true(apps, *args):
    Site = apps.get_model('accounts', 'Site')
    sites = Site.objects.all()

    for site in sites:
        site.has_short_urls = True
        site.save()


def reverse(apps, schema_editor):
    # Nothing to reverse
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_mobilewidget'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='has_short_urls',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.RunPython(turn_has_short_urls_true, reverse),
    ]
