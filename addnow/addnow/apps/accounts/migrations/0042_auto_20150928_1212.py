# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_site_dmp_execute_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginButtonsWidget',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('accounts.widgetconfiguration',),
        ),
        migrations.AlterField(
            model_name='socialurl',
            name='service',
            field=models.CharField(max_length=20, choices=[(b'facebook', b'Facebook'), (b'twitter', b'Twitter'), (b'googlePlus', b'Google+'), (b'linkedin', b'LinkedIn'), (b'pinterest', b'Pinterest'), (b'instagram', b'Instagram'), (b'digg', b'Digg'), (b'delicious', b'Delicious'), (b'stumbleupon', b'StumbleUpon'), (b'gmail', b'Gmail'), (b'whatsapp', b'WhatsApp'), (b'reddit', b'Reddit'), (b'tumblr', b'Tumblr'), (b'sms', b'SMS'), (b'facebook-messenger', b'Facebook Messenger'), (b'facebook-like', b'Facebook Like')]),
        ),
        migrations.AlterField(
            model_name='widgetbutton',
            name='service',
            field=models.CharField(max_length=20, choices=[(b'facebook', b'Facebook'), (b'twitter', b'Twitter'), (b'googlePlus', b'Google+'), (b'linkedin', b'LinkedIn'), (b'pinterest', b'Pinterest'), (b'instagram', b'Instagram'), (b'digg', b'Digg'), (b'delicious', b'Delicious'), (b'stumbleupon', b'StumbleUpon'), (b'gmail', b'Gmail'), (b'whatsapp', b'WhatsApp'), (b'reddit', b'Reddit'), (b'tumblr', b'Tumblr'), (b'sms', b'SMS'), (b'facebook-messenger', b'Facebook Messenger'), (b'facebook-like', b'Facebook Like'), (b'email', b'Email')]),
        ),
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='type',
            field=models.CharField(max_length=20, choices=[(b'sharing-buttons', b'Sharing buttons'), (b'origin-buttons', b'Origin buttons'), (b'copy-paste', b'Copy-paste'), (b'newsletter', b'Newsletter'), (b'mobile', b'Mobile'), (b'follow-buttons', b'Follow buttons'), (b'vertical-float', b'Vertical float')]),
        ),
    ]
