# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20150218_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialurl',
            name='service',
            field=models.CharField(max_length=20, choices=[(b'facebook', b'Facebook'), (b'twitter', b'Twitter'), (b'googlePlus', b'Google+'), (b'linkedin', b'Linkedin'), (b'pinterest', b'Pinterest'), (b'instagram', b'Instagram')]),
            preserve_default=True,
        ),
    ]
