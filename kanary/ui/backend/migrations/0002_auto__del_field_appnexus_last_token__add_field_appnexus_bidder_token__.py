# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'AppNexus.last_token'
        db.delete_column(u'backend_appnexus', 'last_token')

        # Adding field 'AppNexus.bidder_token'
        db.add_column(u'backend_appnexus', 'bidder_token',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True),
                      keep_default=False)

        # Adding field 'AppNexus.member_token'
        db.add_column(u'backend_appnexus', 'member_token',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'AppNexus.last_token'
        db.add_column(u'backend_appnexus', 'last_token',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True),
                      keep_default=False)

        # Deleting field 'AppNexus.bidder_token'
        db.delete_column(u'backend_appnexus', 'bidder_token')

        # Deleting field 'AppNexus.member_token'
        db.delete_column(u'backend_appnexus', 'member_token')


    models = {
        u'backend.appnexus': {
            'Meta': {'object_name': 'AppNexus'},
            'bidder_token': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_token': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        }
    }

    complete_apps = ['backend']