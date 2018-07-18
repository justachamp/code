# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20150604_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetconfiguration',
            name='min_width',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
