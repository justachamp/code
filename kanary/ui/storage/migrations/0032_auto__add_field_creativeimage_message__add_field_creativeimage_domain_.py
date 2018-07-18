# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CreativeImage.message'
        db.add_column(u'storage_creativeimage', 'message',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=500, null=True),
                      keep_default=False)

        # Adding field 'CreativeImage.domain'
        db.add_column(u'storage_creativeimage', 'domain',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=90, null=True),
                      keep_default=False)

        # Adding field 'CreativeImage.brand'
        db.add_column(u'storage_creativeimage', 'brand',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['storage.Brand'], null=True),
                      keep_default=False)


        # Changing field 'CreativeImage.body'
        db.alter_column(u'storage_creativeimage', 'body', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'CreativeImage.title'
        db.alter_column(u'storage_creativeimage', 'title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):
        # Deleting field 'CreativeImage.message'
        db.delete_column(u'storage_creativeimage', 'message')

        # Deleting field 'CreativeImage.domain'
        db.delete_column(u'storage_creativeimage', 'domain')

        # Deleting field 'CreativeImage.brand'
        db.delete_column(u'storage_creativeimage', 'brand_id')


        # Changing field 'CreativeImage.body'
        db.alter_column(u'storage_creativeimage', 'body', self.gf('django.db.models.fields.CharField')(max_length=90, null=True))

        # Changing field 'CreativeImage.title'
        db.alter_column(u'storage_creativeimage', 'title', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'account_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'audit_fees': ('ui.fields.BudgetDecimalField', [], {'default': '0'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'commission': ('django.db.models.fields.SmallIntegerField', [], {'default': "'10'"}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'insufficient_funds_last_sent_email_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'insufficient_funds_sent_emails_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_agency': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '40'}),
            'vat': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'storage.audience': {
            'Meta': {'ordering': "['name']", 'object_name': 'Audience'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_ip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"})
        },
        u'storage.brand': {
            'Meta': {'object_name': 'Brand'},
            'appnexus_access_status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '20'}),
            'brand_id': ('django.db.models.fields.IntegerField', [], {}),
            'check_access_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'page_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'thirdparty_page_id': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'storage.creative': {
            'Meta': {'ordering': "['name']", 'object_name': 'Creative'},
            'appnexus_audit_blocked_no_funds': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'appnexus_feedback': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'appnexus_sla_eta': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'appnexus_status': ('django.db.models.fields.CharField', [], {'default': "'n'", 'max_length': '2'}),
            'audit_fees': ('ui.fields.BudgetDecimalField', [], {'default': '0'}),
            'cache_is_dirty': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'destination': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '2'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'landing_site_url': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_storage.creative_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'to_audit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'storage.creativeflash': {
            'Meta': {'ordering': "['name']", 'object_name': 'CreativeFlash', '_ormbases': [u'storage.Creative']},
            u'creative_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['storage.Creative']", 'unique': 'True', 'primary_key': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'storage.creativeimage': {
            'Meta': {'ordering': "['name']", 'object_name': 'CreativeImage', '_ormbases': [u'storage.Creative']},
            'body': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['storage.Brand']", 'null': 'True'}),
            u'creative_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['storage.Creative']", 'unique': 'True', 'primary_key': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '90', 'null': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'message': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'})
        },
        u'storage.creativevideo': {
            'Meta': {'ordering': "['name']", 'object_name': 'CreativeVideo', '_ormbases': [u'storage.Creative']},
            u'creative_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['storage.Creative']", 'unique': 'True', 'primary_key': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'liverail_error': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'liverail_id': ('django.db.models.fields.IntegerField', [], {'max_length': '20', 'null': 'True', 'db_index': 'True'}),
            'liverail_status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '20', 'db_index': 'True'}),
            'media_variants': ('jsonfield.fields.JSONField', [], {'default': '{}', 'blank': 'True'})
        }
    }

    complete_apps = ['storage']