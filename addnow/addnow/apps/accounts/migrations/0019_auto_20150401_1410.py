# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20150324_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apitoken',
            name='generated_by',
        ),
        migrations.RemoveField(
            model_name='apitoken',
            name='user',
        ),
        migrations.DeleteModel(
            name='ApiToken',
        ),
    ]
