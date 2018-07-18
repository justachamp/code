# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AppNexus'
        db.create_table(u'backend_appnexus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_token', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
        ))
        db.send_create_signal(u'backend', ['AppNexus'])


    def backwards(self, orm):
        # Deleting model 'AppNexus'
        db.delete_table(u'backend_appnexus')


    models = {
        u'backend.appnexus': {
            'Meta': {'object_name': 'AppNexus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_token': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        }
    }

    complete_apps = ['backend']