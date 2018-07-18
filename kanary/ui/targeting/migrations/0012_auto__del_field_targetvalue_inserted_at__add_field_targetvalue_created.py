# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TargetValue.inserted_at'
        db.delete_column(u'targeting_targetvalue', 'inserted_at')

        # Adding field 'TargetValue.created'
        db.add_column(u'targeting_targetvalue', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'TargetValue.modified'
        db.add_column(u'targeting_targetvalue', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'TargetValue.inserted_at'
        db.add_column(u'targeting_targetvalue', 'inserted_at',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'TargetValue.created'
        db.delete_column(u'targeting_targetvalue', 'created')

        # Deleting field 'TargetValue.modified'
        db.delete_column(u'targeting_targetvalue', 'modified')


    models = {
        'targeting.appnexusbrand': {
            'Meta': {'object_name': 'AppNexusBrand'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['targeting.AppNexusCategory']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'num_creatives': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'urls': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'targeting.appnexusbrowser': {
            'Meta': {'object_name': 'AppNexusBrowser'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'platform_type': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'targeting.appnexuscategory': {
            'Meta': {'object_name': 'AppNexusCategory'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_sensitive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexuscontentcategory': {
            'Meta': {'object_name': 'AppNexusContentCategory'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_system': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['targeting.AppNexusContentCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'targeting.appnexusinventoryattr': {
            'Meta': {'object_name': 'AppNexusInventoryAttr'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexuslanguage': {
            'Meta': {'object_name': 'AppNexusLanguage'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexusos': {
            'Meta': {'object_name': 'AppNexusOS'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'platform_type': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'targeting.appnexussegment': {
            'Meta': {'object_name': 'AppNexusSegment'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexustechnicalattr': {
            'Meta': {'object_name': 'AppNexusTechnicalAttr'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        u'targeting.exchange': {
            'Meta': {'object_name': 'Exchange'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'targeting.publishertargetvalue': {
            'Meta': {'ordering': "('id',)", 'object_name': 'PublisherTargetValue', '_ormbases': [u'targeting.TargetValue']},
            '_positions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            '_sizes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'segments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['targeting.AppNexusSegment']", 'symmetrical': 'False'}),
            u'targetvalue_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['targeting.TargetValue']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'targeting.targetvalue': {
            'Meta': {'ordering': "('id',)", 'unique_together': "[('exchange', 'category', 'value')]", 'object_name': 'TargetValue'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targeting.Exchange']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'representant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'represented'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['targeting.TargetValue']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'})
        }
    }

    complete_apps = ['targeting']