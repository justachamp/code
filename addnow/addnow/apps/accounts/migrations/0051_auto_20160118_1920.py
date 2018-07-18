# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_widgetconfiguration_link_share_button'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialurl',
            name='service',
            field=models.CharField(max_length=20, choices=[(b'facebook', b'Facebook'), (b'twitter', b'Twitter'), (b'googlePlus', b'Google+'), (b'linkedin', b'LinkedIn'), (b'pinterest', b'Pinterest'), (b'instagram', b'Instagram'), (b'digg', b'Digg'), (b'delicious', b'Delicious'), (b'stumbleupon', b'StumbleUpon'), (b'gmail', b'Gmail'), (b'whatsapp', b'WhatsApp'), (b'reddit', b'Reddit'), (b'tumblr', b'Tumblr'), (b'sms', b'SMS'), (b'facebook-messenger', b'Facebook Messenger'), (b'facebook-like', b'Facebook Like'), (b'youtube', b'Youtube'), (b'line', b'Line'), (b'weibo', b'Weibo')]),
        ),
        migrations.AlterField(
            model_name='widgetbutton',
            name='service',
            field=models.CharField(max_length=20, choices=[(b'facebook', b'Facebook'), (b'twitter', b'Twitter'), (b'googlePlus', b'Google+'), (b'linkedin', b'LinkedIn'), (b'pinterest', b'Pinterest'), (b'instagram', b'Instagram'), (b'digg', b'Digg'), (b'delicious', b'Delicious'), (b'stumbleupon', b'StumbleUpon'), (b'gmail', b'Gmail'), (b'whatsapp', b'WhatsApp'), (b'reddit', b'Reddit'), (b'tumblr', b'Tumblr'), (b'sms', b'SMS'), (b'facebook-messenger', b'Facebook Messenger'), (b'facebook-like', b'Facebook Like'), (b'youtube', b'Youtube'), (b'line', b'Line'), (b'weibo', b'Weibo'), (b'email', b'Email')]),
        ),
    ]
