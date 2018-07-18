# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='domain',
            new_name='url',
        ),
    ]
