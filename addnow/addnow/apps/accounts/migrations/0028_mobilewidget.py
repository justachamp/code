# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_widgetconfiguration_min_width'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileWidget',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('accounts.widgetconfiguration',),
        ),
    ]
