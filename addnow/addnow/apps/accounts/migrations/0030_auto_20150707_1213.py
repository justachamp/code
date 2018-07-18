# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import addnow.apps.accounts.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_site_short_urls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='api_key',
        ),
        migrations.AddField(
            model_name='site',
            name='trim_api_key',
            field=addnow.apps.accounts.fields.BlankAsNullCharField(max_length=255, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='widgetconfiguration',
            name='vanity_domain',
            field=addnow.apps.accounts.fields.BlankAsNullDomainNameField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='site',
            name='domain',
            field=addnow.apps.accounts.fields.BlankAsNullDomainNameField(unique=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='min_width',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
