# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

import addnow.apps.accounts.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_auto_20150724_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='trim_api_key',
            field=addnow.apps.accounts.fields.BlankAsNullCharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
