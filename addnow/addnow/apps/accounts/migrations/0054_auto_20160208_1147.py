# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0053_auto_20160208_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='site',
            field=models.ForeignKey(related_name='widgets', to='accounts.Site'),
        ),
        migrations.AlterUniqueTogether(
            name='widgetconfiguration',
            unique_together=set([('site', 'name')]),
        ),
        migrations.RemoveField(
            model_name='widgetconfiguration',
            name='user',
        ),
    ]
