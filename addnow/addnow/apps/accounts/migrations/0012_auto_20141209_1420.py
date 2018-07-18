# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20141125_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service', models.CharField(max_length=20, choices=[(b'facebook', b'Facebook'), (b'twitter', b'Twitter'), (b'google', b'Google'), (b'linkedin', b'Linkedin'), (b'pinterest', b'Pinterest')])),
                ('url', models.CharField(max_length=255)),
                ('site', models.ForeignKey(related_name='social_urls', to='accounts.Site')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='socialurl',
            unique_together=set([('site', 'service')]),
        ),
        migrations.AddField(
            model_name='site',
            name='api_key',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='sharing_message',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='site',
            name='piwik_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
