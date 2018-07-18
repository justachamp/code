# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0051_auto_20160118_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='piwik_id',
        ),
        migrations.RemoveField(
            model_name='site',
            name='url',
        ),
        migrations.RemoveField(
            model_name='user',
            name='piwik_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='piwik_password_hash',
        ),
        migrations.RemoveField(
            model_name='user',
            name='piwik_token_auth',
        ),
        migrations.AddField(
            model_name='widgetconfiguration',
            name='site',
            field=models.ForeignKey(to='accounts.Site', null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='widget_configurations',
            field=models.ManyToManyField(help_text=b'deprecated by ADDNOW-807', related_name='sites', to='accounts.WidgetConfiguration', blank=True),
        ),
    ]
