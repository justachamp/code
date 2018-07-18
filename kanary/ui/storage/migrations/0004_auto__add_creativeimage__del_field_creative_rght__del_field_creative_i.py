# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CreativeImage'
        db.create_table(u'storage_creativeimage', (
            (u'creative_ptr', self.gf('django.db.models.fields.related.OneToOneField')(
                to=orm['storage.Creative'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'storage', ['CreativeImage'])

        # Deleting field 'Creative.rght'
        db.delete_column(u'storage_creative', 'rght')

        # Deleting field 'Creative.lft'
        db.delete_column(u'storage_creative', 'lft')

        # Deleting field 'Creative.is_folder'
        db.delete_column(u'storage_creative', 'is_folder')

        # Deleting field 'Creative.tree_id'
        db.delete_column(u'storage_creative', 'tree_id')

        # Deleting field 'Creative.parent'
        db.delete_column(u'storage_creative', 'parent_id')

        # Deleting field 'Creative.level'
        db.delete_column(u'storage_creative', 'level')

        # Renaming field 'Creative.image'
        db.rename_column(u'storage_creative', 'image', 'old_image')

        # Adding field 'Creative.polymorphic_ctype'
        db.add_column(u'storage_creative', 'polymorphic_ctype',
                      self.gf('django.db.models.fields.related.ForeignKey')(
                          related_name=u'polymorphic_storage.creative_set', null=True, to=orm['contenttypes.ContentType']),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting model 'CreativeImage'
        db.delete_table(u'storage_creativeimage')

        # User chose to not deal with backwards NULL issues for 'Creative.rght'
        raise RuntimeError("Cannot reverse this migration. 'Creative.rght' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Creative.image'
        raise RuntimeError("Cannot reverse this migration. 'Creative.image' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Creative.lft'
        raise RuntimeError("Cannot reverse this migration. 'Creative.lft' and its values cannot be restored.")
        # Adding field 'Creative.is_folder'
        db.add_column(u'storage_creative', 'is_folder',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Creative.tree_id'
        raise RuntimeError("Cannot reverse this migration. 'Creative.tree_id' and its values cannot be restored.")
        # Adding field 'Creative.parent'
        db.add_column(u'storage_creative', 'parent',
                      self.gf('mptt.fields.TreeForeignKey')(
                          related_name='children', null=True, to=orm['storage.Creative'], blank=True),
                      keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Creative.level'
        raise RuntimeError("Cannot reverse this migration. 'Creative.level' and its values cannot be restored.")

        # Renaming field 'Creative.old_image'
        db.rename_column(u'storage_creative', 'old_image', 'image')

        # Deleting field 'Creative.polymorphic_ctype'
        db.delete_column(u'storage_creative', 'polymorphic_ctype_id')

    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '40'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'storage.creative': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Creative'},
            'appnexus_feedback': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'appnexus_sla_eta': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'appnexus_status': ('django.db.models.fields.CharField', [], {'default': "'n'", 'max_length': '1'}),
            'cache_is_dirty': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'default': "'7cc8e52de56aa940b26a6d3d1894f0b6c7f63682'", 'unique': 'True', 'max_length': '128'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landing_site_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'old_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_storage.creative_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'storage.creativeimage': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'CreativeImage', '_ormbases': [u'storage.Creative']},
            u'creative_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['storage.Creative']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['storage']
