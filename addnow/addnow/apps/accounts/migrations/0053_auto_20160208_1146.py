# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def extract_site_from_m2m(apps, schema_editor):
    widget_conf_cls = apps.get_model('accounts', 'WidgetConfiguration')
    for row in widget_conf_cls.objects.all():
        site = row.sites.all().first()
        if site:
            row.site = site  # take first Site object from m2m
            row.save()
        else:
            sites = row.user.site_set.all()
            if len(sites) == 1:
                row.site = sites[0]
                row.save()
            else:
                row.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0052_auto_20160201_0953'),
    ]

    operations = [
        migrations.RunPython(extract_site_from_m2m)
    ]
