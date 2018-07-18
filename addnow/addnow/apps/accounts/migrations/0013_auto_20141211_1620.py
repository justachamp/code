# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urlparse import urlparse

from django.db import models, migrations


def extract_domain_from_url(apps, schema_editor):
    site_cls = apps.get_model('accounts', 'Site')

    for site in site_cls.objects.exclude(url='').only('url'):
        site.domain = urlparse(site.url).netloc
        site.save(update_fields=['domain'])


def reverse(apps, schema_editor):
    # Nothing to reverse
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20141209_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='domain',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='site',
            name='url',
            field=models.CharField(default=b'', help_text=b'deprecated', max_length=255, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='address_bar_sharing',
            field=models.BooleanField(default=False, blank=True),
            preserve_default=True,
        ),
        migrations.RunPython(extract_domain_from_url, reverse),
    ]
