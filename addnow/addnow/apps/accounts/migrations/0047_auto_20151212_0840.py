# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_auto_20151203_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='CircularMobileWidget',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('accounts.widgetconfiguration',),
        ),
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='position',
            field=models.CharField(blank=True, max_length=20, choices=[(b'left', b'Left'), (b'right', b'Right'), (b'top', b'Top'), (b'bottom', b'Bottom'), (b'top-left', b'Top Left'), (b'bottom-left', b'Bottom Left'), (b'top-right', b'Top Right'), (b'bottom-right', b'Bottom Right')]),
        ),
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='type',
            field=models.CharField(max_length=20, choices=[(b'sharing-buttons', b'Sharing buttons'), (b'origin-buttons', b'Origin buttons'), (b'copy-paste', b'Copy-paste'), (b'newsletter', b'Newsletter'), (b'mobile', b'Mobile'), (b'follow-buttons', b'Follow buttons'), (b'vertical-float', b'Vertical float'), (b'circular-mobile', b'Circular Mobile')]),
        ),
    ]
