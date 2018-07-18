# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    depends_on = (
        ("account", "0002_auto__del_field_user_event_last_read__add_field_user_unread_events_cou"),
    )

    def forwards(self, orm):
        # Adding model 'Creative'
        db.create_table(u'storage_creative', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_random', self.gf('django.db.models.fields.CharField')(
                default='fbe4a14d1bbf4965ca9c6882e96ba54dc4db2946', unique=True, max_length=128)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('cache_is_dirty', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
            ('is_folder', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(
                blank=True, related_name='children', null=True, to=orm['storage.Creative'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True)),
            ('appnexus_feedback', self.gf('django.db.models.fields.TextField')(null=True)),
            ('appnexus_sla_eta', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('appnexus_status', self.gf('django.db.models.fields.CharField')(default='n', max_length=1)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('landing_site_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'storage', ['Creative'])

        # Adding model 'Site'
        db.create_table(u'storage_site', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_random', self.gf('django.db.models.fields.CharField')(
                default='2b1aeaaf5d95b970a699ed6e179a5f2d5c23d978', unique=True, max_length=128)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
            ('is_folder', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(
                blank=True, related_name='children', null=True, to=orm['storage.Site'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'storage', ['Site'])

    def backwards(self, orm):
        # Deleting model 'Creative'
        db.delete_table(u'storage_creative')

        # Deleting model 'Site'
        db.delete_table(u'storage_site')

    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '40'})
        },
        u'storage.creative': {
            'Meta': {'object_name': 'Creative'},
            'appnexus_feedback': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'appnexus_sla_eta': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'appnexus_status': ('django.db.models.fields.CharField', [], {'default': "'n'", 'max_length': '1'}),
            'cache_is_dirty': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'default': "'3600d62231135008946b8bceecdf2755fe32a22c'", 'unique': 'True', 'max_length': '128'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_folder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landing_site_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['storage.Creative']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'storage.site': {
            'Meta': {'object_name': 'Site'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'default': "'6df922ed856aa1bcdfb578fbe439bbed6f473d6e'", 'unique': 'True', 'max_length': '128'}),
            'is_folder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['storage.Site']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['storage']
