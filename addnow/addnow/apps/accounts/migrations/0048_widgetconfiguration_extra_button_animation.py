# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_auto_20151212_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetconfiguration',
            name='extra_button_animation',
            field=models.BooleanField(default=False),
        ),
    ]
