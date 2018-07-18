# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_office', '0002_add_i18n_and_backend_alias'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReminderLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReminderRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('dimension', models.PositiveSmallIntegerField(help_text=b'Please specify value in days')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email_template', models.ForeignKey(to='post_office.EmailTemplate')),
            ],
        ),
        migrations.AddField(
            model_name='reminderlog',
            name='rule',
            field=models.ForeignKey(to='reminders.ReminderRule'),
        ),
        migrations.AddField(
            model_name='reminderlog',
            name='user',
            field=models.ForeignKey(related_name='reminders', to=settings.AUTH_USER_MODEL),
        ),
    ]
