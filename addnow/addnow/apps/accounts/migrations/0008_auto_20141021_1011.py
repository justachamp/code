# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_dsp_pixel_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dsp_pixel_url',
            field=models.URLField(default=b'', max_length=1000, verbose_name=b'DSP pixel', blank=True),
        ),
    ]
