# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20150907_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credentialsmodel',
            old_name='id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='credentialsmodel',
            name='user',
            field=models.OneToOneField(related_name='analytics_credential', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
