# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_add_new_social_service_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='WidgetButton',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service', models.CharField(max_length=20, choices=[(b'facebook', b'Facebook'), (b'twitter', b'Twitter'), (b'googlePlus', b'Google+'), (b'linkedin', b'Linkedin'), (b'pinterest', b'Pinterest'), (b'instagram', b'Instagram'), (b'digg', b'Digg'), (b'delicious', b'Delicious'), (b'stumbleupon', b'StumbleUpon'), (b'gmail', b'Gmail'), (b'whatsapp', b'WhatsApp'), (b'reddit', b'Reddit'), (b'tumblr', b'Tumblr')])),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WidgetConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('orientation', models.CharField(max_length=20, choices=[(b'vertical', b'Vertical'), (b'horizontal', b'Horizontal')])),
                ('button_size', models.CharField(max_length=20, choices=[(b'small', b'Small'), (b'medium', b'Medium'), (b'large', b'Large')])),
                ('button_style', models.CharField(max_length=20, choices=[(b'icon', b'Icon'), (b'label', b'Label')])),
                ('counter_position', models.CharField(max_length=20, choices=[(b'top', b'Top'), (b'right', b'Right'), (b'no_counter', b'No counter')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='widgetbutton',
            name='configuration',
            field=models.ForeignKey(related_name='buttons', to='accounts.WidgetConfiguration'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='widgetbutton',
            unique_together=set([('configuration', 'service')]),
        ),
        migrations.RemoveField(
            model_name='site',
            name='widget_layout',
        ),
        migrations.AddField(
            model_name='site',
            name='widget_configurations',
            field=models.ManyToManyField(related_name='sites', null=True, to='accounts.WidgetConfiguration', blank=True),
            preserve_default=True,
        ),
    ]
