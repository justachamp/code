# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20141211_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='widget_layout',
            field=models.CharField(default=b'', max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
