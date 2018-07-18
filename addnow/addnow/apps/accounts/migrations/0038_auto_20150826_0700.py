# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_auto_20150824_0945'),
    ]

    def turn_no_counter_has_null(apps, schema_editor):
        WidgetConfiguration = apps.get_model('accounts', 'WidgetConfiguration')
        widget_configurations = WidgetConfiguration.objects.all()

        for widget_configuration in widget_configurations:
            if widget_configuration.counter_position == 'no_counter':
                widget_configuration.counter_position = ''
                widget_configuration.save()

    def revert_turn_no_counter_has_null(apps, schema_editor):
        WidgetConfiguration = apps.get_model('accounts', 'WidgetConfiguration')
        widget_configurations = WidgetConfiguration.objects.all()

        for widget_configuration in widget_configurations:
            if widget_configuration.counter_position == '':
                widget_configuration.counter_position = 'no_counter'
                widget_configuration.save()

    operations = [
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='counter_position',
            field=models.CharField(blank=True, max_length=20, choices=[(b'top', b'Top'), (b'right', b'Right')]),
            preserve_default=True,
        ),
        migrations.RunPython(turn_no_counter_has_null, revert_turn_no_counter_has_null),
    ]
