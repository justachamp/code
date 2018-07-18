# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20150511_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='CopyPasteWidget',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('accounts.widgetconfiguration',),
        ),
        migrations.CreateModel(
            name='NewsletterWidget',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('accounts.widgetconfiguration',),
        ),
        migrations.CreateModel(
            name='SharingButtonsWidget',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('accounts.widgetconfiguration',),
        ),
        migrations.AddField(
            model_name='widgetconfiguration',
            name='media_url',
            field=models.URLField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='widgetconfiguration',
            name='page_title',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='widgetconfiguration',
            name='page_url',
            field=models.URLField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='widgetconfiguration',
            name='type',
            field=models.CharField(default='sharing-buttons', max_length=20, choices=[(b'sharing-buttons', b'Sharing buttons'), (b'copy-paste', b'Copy-paste'), (b'newsletter', b'Newsletter'), (b'mobile', b'Mobile')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='button_size',
            field=models.CharField(blank=True, max_length=20, choices=[(b'small', b'Small'), (b'medium', b'Medium'), (b'big', b'Big'), (b'large', b'Large')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='button_style',
            field=models.CharField(blank=True, max_length=20, choices=[(b'icon', b'Icon'), (b'label', b'Label')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='counter_position',
            field=models.CharField(blank=True, max_length=20, choices=[(b'top', b'Top'), (b'right', b'Right'), (b'no_counter', b'No counter')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='orientation',
            field=models.CharField(blank=True, max_length=20, choices=[(b'vertical', b'Vertical'), (b'horizontal', b'Horizontal')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='widgetconfiguration',
            name='title',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='widgetconfiguration',
            unique_together=set([('user', 'title')]),
        ),
    ]
