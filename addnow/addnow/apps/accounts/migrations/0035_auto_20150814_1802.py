# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import addnow.apps.accounts.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_auto_20150810_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowWidget',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('accounts.widgetconfiguration',),
        ),
        migrations.AddField(
            model_name='widgetbutton',
            name='follow_url',
            field=addnow.apps.accounts.fields.BlankAsNullURLField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='button_style',
            field=models.CharField(blank=True, max_length=20, choices=[(b'icon', b'Icon'), (b'label', b'Label'), (b'counter', b'Counter')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='type',
            field=models.CharField(max_length=20, choices=[(b'sharing-buttons', b'Sharing buttons'), (b'copy-paste', b'Copy-paste'), (b'newsletter', b'Newsletter'), (b'mobile', b'Mobile'), (b'follow-buttons', b'Follow buttons')]),
            preserve_default=True,
        ),
    ]
