# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_auto_20150911_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='dmp_execute_code',
            field=models.BooleanField(default=False),
        ),
    ]
