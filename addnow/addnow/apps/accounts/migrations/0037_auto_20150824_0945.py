# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_auto_20150818_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerticalFloatWidget',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('accounts.widgetconfiguration',),
        ),
        migrations.AddField(
            model_name='widgetconfiguration',
            name='position',
            field=models.CharField(blank=True, max_length=20, choices=[(b'left', b'Left'), (b'right', b'Right')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='type',
            field=models.CharField(max_length=20, choices=[(b'sharing-buttons', b'Sharing buttons'), (b'copy-paste', b'Copy-paste'), (b'newsletter', b'Newsletter'), (b'mobile', b'Mobile'), (b'follow-buttons', b'Follow buttons'), (b'vertical-float', b'Vertical float')]),
            preserve_default=True,
        ),
    ]
