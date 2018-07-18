# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings

from oauth2client.contrib.django_orm import CredentialsField


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20150708_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.ForeignKey(related_name='addnow_user', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('credential', CredentialsField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
