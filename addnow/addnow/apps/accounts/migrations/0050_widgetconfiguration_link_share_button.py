# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0049_auto_20160118_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetconfiguration',
            name='has_link_share_button',
            field=models.BooleanField(default=False),
        ),
        migrations.RenameField(
            model_name='widgetconfiguration',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterUniqueTogether(
            name='widgetconfiguration',
            unique_together=set([('user', 'name')]),
        ),
    ]
