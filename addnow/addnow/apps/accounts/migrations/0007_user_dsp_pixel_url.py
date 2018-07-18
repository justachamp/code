# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20140903_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dsp_pixel_url',
            field=models.URLField(default=b'', max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
