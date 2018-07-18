# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def fix_duplicates(apps, schema_editor):
    Site = apps.get_model('accounts', 'Site')
    db = schema_editor.connection.alias

    dupes = Site.objects.using(db).values('domain').annotate(
        count=models.Count('id')
    ).values('domain').order_by().filter(count__gt=1)

    for dupe in dupes:
        sites = Site.objects.using(db).filter(domain=dupe['domain'])
        for idx, site in enumerate(sites.order_by('id')):
            if idx == 0:
                continue
            site.domain = '%s_%s' % (idx, site.domain)
            site.save()


def reverse_fix(apps, schema_editor):
    # Nothing to reverse, modified data is dynamic
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20150422_1258'),
    ]

    operations = [
        migrations.RunPython(fix_duplicates, reverse_code=reverse_fix),
        migrations.AlterField(
            model_name='site',
            name='domain',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='widgetbutton',
            name='service',
            field=models.CharField(max_length=20, choices=[(b'facebook', b'Facebook'), (b'twitter', b'Twitter'), (b'googlePlus', b'Google+'), (b'linkedin', b'Linkedin'), (b'pinterest', b'Pinterest'), (b'instagram', b'Instagram'), (b'digg', b'Digg'), (b'delicious', b'Delicious'), (b'stumbleupon', b'StumbleUpon'), (b'gmail', b'Gmail'), (b'whatsapp', b'WhatsApp'), (b'reddit', b'Reddit'), (b'tumblr', b'Tumblr'), (b'sms', b'SMS')]),
            preserve_default=True,
        ),
    ]
