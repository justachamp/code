# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

import addnow.apps.accounts.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_auto_20150814_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='vanity_domain',
            field=addnow.apps.accounts.fields.BlankAsNullDomainNameField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
