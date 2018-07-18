# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LiveViewCounter.public_id'
        db.alter_column(u'liveview_liveviewcounter', 'public_id', self.gf('django.db.models.fields.CharField')(max_length=27))

    def backwards(self, orm):

        # Changing field 'LiveViewCounter.public_id'
        db.alter_column(u'liveview_liveviewcounter', 'public_id', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        u'liveview.liveviewcounter': {
            'Meta': {'object_name': 'LiveViewCounter', 'index_together': "[['time', 'public_id']]"},
            'bid': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('django.db.models.fields.BigIntegerField', [], {}),
            'public_id': ('django.db.models.fields.CharField', [], {'max_length': '27'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['liveview']