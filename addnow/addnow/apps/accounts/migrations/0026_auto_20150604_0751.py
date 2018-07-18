# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20150527_0754'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialurl',
            options={'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='widgetconfiguration',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
