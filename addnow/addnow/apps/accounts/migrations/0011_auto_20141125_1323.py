# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_is_verified',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='piwik_login',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='piwik_password_hash',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='piwik_token_auth',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
