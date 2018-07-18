# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_site_widget_layout'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='offset',
            field=models.SmallIntegerField(default=0, verbose_name=b'timezone offset in minutes', blank=True),
            preserve_default=True,
        ),
    ]
