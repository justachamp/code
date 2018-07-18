# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20140902_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='piwik_site_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='piwik_user_id',
        ),
        migrations.AddField(
            model_name='site',
            name='piwik_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='piwik_login',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='piwik_password_hash',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='piwik_token_auth',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
