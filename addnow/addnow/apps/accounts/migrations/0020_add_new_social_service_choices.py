# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20150401_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialurl',
            name='service',
            field=models.CharField(max_length=20, choices=[
                (b'facebook', b'Facebook'), (b'twitter', b'Twitter'), (b'googlePlus', b'Google+'),
                (b'linkedin', b'Linkedin'), (b'pinterest', b'Pinterest'), (b'instagram', b'Instagram'),
                (b'digg', b'Digg'), (b'delicious', b'Delicious'), (b'stumbleupon', b'StumbleUpon'),
                (b'gmail', b'Gmail'), (b'whatsapp', b'WhatsApp'), (b'reddit', b'Reddit'),
                (b'tumblr', b'Tumblr'), (b'sms', b'SMS')]),
            preserve_default=True,
        ),
    ]
