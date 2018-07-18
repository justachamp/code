# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20150707_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='analytics_account',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='analytics_profile',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='analytics_property',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='has_analytics',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
