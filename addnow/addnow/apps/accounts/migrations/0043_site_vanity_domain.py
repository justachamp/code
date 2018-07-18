# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from addnow.apps.accounts import fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_auto_20150928_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='vanity_domain',
            field=fields.BlankAsNullDomainNameField(max_length=255, null=True, blank=True),
        ),
    ]
