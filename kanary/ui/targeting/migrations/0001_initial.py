# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exchange'
        db.create_table(u'targeting_exchange', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20, db_index=True)),
        ))
        db.send_create_signal(u'targeting', ['Exchange'])

        # Adding model 'TargetValue'
        db.create_table(u'targeting_targetvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=900, db_index=True)),
            ('exchange', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['targeting.Exchange'], null=True)),
            ('representant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='represented', null=True, on_delete=models.SET_NULL, to=orm['targeting.TargetValue'])),
            ('inserted_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'targeting', ['TargetValue'])

        # Adding unique constraint on 'TargetValue', fields ['exchange', 'category', 'value']
        db.create_unique(u'targeting_targetvalue', ['exchange_id', 'category', 'value'])

        # Adding model 'Gender'
        db.create_table(u'targeting_gender', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'targeting', ['Gender'])

        # Adding model 'AgeGroup'
        db.create_table(u'targeting_agegroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.IntegerField')()),
            ('end', self.gf('django.db.models.fields.IntegerField')()),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'targeting', ['AgeGroup'])

        # Adding model 'PublisherAdPositions'
        db.create_table(u'targeting_publisheradpositions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'targeting', ['PublisherAdPositions'])

        # Adding model 'PublishersInventoryType'
        db.create_table(u'targeting_publishersinventorytype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'targeting', ['PublishersInventoryType'])

        # Adding model 'AppNexusCategory'
        db.create_table(u'targeting_appnexuscategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=511)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('is_sensitive', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('targeting', ['AppNexusCategory'])

        # Adding model 'AppNexusOS'
        db.create_table(u'targeting_appnexusos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=511)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('platform_type', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('targeting', ['AppNexusOS'])

        # Adding model 'AppNexusContentCategory'
        db.create_table(u'targeting_appnexuscontentcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=511)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('is_system', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['targeting.AppNexusContentCategory'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('targeting', ['AppNexusContentCategory'])

        # Adding model 'AppNexusBrand'
        db.create_table(u'targeting_appnexusbrand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=511)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('num_creatives', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['targeting.AppNexusCategory'], null=True)),
            ('urls', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('targeting', ['AppNexusBrand'])

        # Adding model 'AppNexusLanguage'
        db.create_table(u'targeting_appnexuslanguage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=511)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('targeting', ['AppNexusLanguage'])

        # Adding model 'AppNexusTechnicalAttr'
        db.create_table(u'targeting_appnexustechnicalattr', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=511)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('targeting', ['AppNexusTechnicalAttr'])

        # Adding model 'AppNexusBrowser'
        db.create_table(u'targeting_appnexusbrowser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=511)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('platform_type', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('targeting', ['AppNexusBrowser'])

        # Adding model 'AppNexusInventoryAttr'
        db.create_table(u'targeting_appnexusinventoryattr', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=511)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('targeting', ['AppNexusInventoryAttr'])


    def backwards(self, orm):
        # Removing unique constraint on 'TargetValue', fields ['exchange', 'category', 'value']
        db.delete_unique(u'targeting_targetvalue', ['exchange_id', 'category', 'value'])

        # Deleting model 'Exchange'
        db.delete_table(u'targeting_exchange')

        # Deleting model 'TargetValue'
        db.delete_table(u'targeting_targetvalue')

        # Deleting model 'Gender'
        db.delete_table(u'targeting_gender')

        # Deleting model 'AgeGroup'
        db.delete_table(u'targeting_agegroup')

        # Deleting model 'PublisherAdPositions'
        db.delete_table(u'targeting_publisheradpositions')

        # Deleting model 'PublishersInventoryType'
        db.delete_table(u'targeting_publishersinventorytype')

        # Deleting model 'AppNexusCategory'
        db.delete_table(u'targeting_appnexuscategory')

        # Deleting model 'AppNexusOS'
        db.delete_table(u'targeting_appnexusos')

        # Deleting model 'AppNexusContentCategory'
        db.delete_table(u'targeting_appnexuscontentcategory')

        # Deleting model 'AppNexusBrand'
        db.delete_table(u'targeting_appnexusbrand')

        # Deleting model 'AppNexusLanguage'
        db.delete_table(u'targeting_appnexuslanguage')

        # Deleting model 'AppNexusTechnicalAttr'
        db.delete_table(u'targeting_appnexustechnicalattr')

        # Deleting model 'AppNexusBrowser'
        db.delete_table(u'targeting_appnexusbrowser')

        # Deleting model 'AppNexusInventoryAttr'
        db.delete_table(u'targeting_appnexusinventoryattr')


    models = {
        u'targeting.agegroup': {
            'Meta': {'object_name': 'AgeGroup'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
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
        u'targeting.gender': {
            'Meta': {'object_name': 'Gender'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'targeting.publisheradpositions': {
            'Meta': {'ordering': "('name',)", 'object_name': 'PublisherAdPositions'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'targeting.publishersinventorytype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'PublishersInventoryType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'targeting.targetvalue': {
            'Meta': {'unique_together': "[('exchange', 'category', 'value')]", 'object_name': 'TargetValue'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targeting.Exchange']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inserted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'representant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'represented'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['targeting.TargetValue']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'})
        }
    }

    complete_apps = ['targeting']
