# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0048_widgetconfiguration_extra_button_animation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='sharing_message',
            new_name='thank_you_message',
        ),
        migrations.AddField(
            model_name='site',
            name='thank_you_advert_image_url',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='site',
            name='thank_you_advert_title',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='site',
            name='thank_you_advert_url',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
