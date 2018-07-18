# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20150708_1252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='widgetbutton',
            options={'ordering': ('is_extra_button', 'order')},
        ),
        migrations.AddField(
            model_name='widgetbutton',
            name='is_extra_button',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
