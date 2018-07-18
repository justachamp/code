# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_uniqueuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='copy_paste_sharing',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialurl',
            name='service',
            field=models.CharField(max_length=20, choices=[(b'facebook', b'Facebook'), (b'twitter', b'Twitter'), (b'google_plus', b'Google+'), (b'linkedin', b'Linkedin'), (b'pinterest', b'Pinterest')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uniqueuser',
            name='created_at',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
