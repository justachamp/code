# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='domain',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
