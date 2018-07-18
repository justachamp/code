# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def delete_null_values(apps, schema_editor):
    Site = apps.get_model('accounts', 'Site')

    sites = Site.objects.all()

    for site in sites:
        if site.api_key is None:
            site.api_key = ''
        if site.sharing_message is None:
            site.sharing_message = ''
        site.save()


def reverse(apps, schema_editor):
    # Nothing to reverse
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20150525_1439'),
    ]

    operations = [
        migrations.RunPython(delete_null_values, reverse_code=reverse),
        migrations.AlterField(
            model_name='site',
            name='api_key',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='site',
            name='sharing_message',
            field=models.CharField(default='', max_length=500, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='site',
            name='url',
            field=models.CharField(help_text=b'deprecated', max_length=255, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='site',
            name='widget_configurations',
            field=models.ManyToManyField(related_name='sites', to='accounts.WidgetConfiguration', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='dsp_pixel_url',
            field=models.URLField(max_length=1000, verbose_name=b'DSP pixel', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='offset',
            field=models.SmallIntegerField(default=0, verbose_name=b'timezone offset in minutes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='piwik_login',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='piwik_password_hash',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='piwik_token_auth',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
