# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LiveViewCounter'
        db.create_table(u'liveview_liveviewcounter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('public_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('bid', self.gf('django.db.models.fields.BigIntegerField')()),
            ('imp', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'liveview', ['LiveViewCounter'])

        # Adding index on 'LiveViewCounter', fields ['time', 'public_id']
        db.create_index(u'liveview_liveviewcounter', ['time', 'public_id'])


    def backwards(self, orm):
        # Removing index on 'LiveViewCounter', fields ['time', 'public_id']
        db.delete_index(u'liveview_liveviewcounter', ['time', 'public_id'])

        # Deleting model 'LiveViewCounter'
        db.delete_table(u'liveview_liveviewcounter')


    models = {
        u'liveview.liveviewcounter': {
            'Meta': {'object_name': 'LiveViewCounter', 'index_together': "[['time', 'public_id']]"},
            'bid': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('django.db.models.fields.BigIntegerField', [], {}),
            'public_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['liveview']