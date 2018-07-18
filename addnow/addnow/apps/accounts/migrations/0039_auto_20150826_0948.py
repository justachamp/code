# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_auto_20150826_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='position',
            field=models.CharField(blank=True, max_length=20, choices=[(b'left', b'Left'), (b'right', b'Right'), (b'top', b'Top'), (b'bottom', b'Bottom')]),
            preserve_default=True,
        ),
    ]
