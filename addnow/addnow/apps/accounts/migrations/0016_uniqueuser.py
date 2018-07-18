# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_user_offset'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueUser',
            fields=[
                ('uuid', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
