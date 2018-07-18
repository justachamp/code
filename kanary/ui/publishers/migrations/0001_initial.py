# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("targeting", "0008_auto__add_publishertargetvalue"),
    )

    def forwards(self, orm):
        # Adding model 'PublisherSet'
        db.create_table(u'publishers_publisherset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publisher_sets', to=orm['account.Account'])),
            ('set_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'publishers', ['PublisherSet'])

        # Adding M2M table for field target_values on 'PublisherSet'
        db.create_table(u'publishers_publisherset_target_values', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('publisherset', models.ForeignKey(orm[u'publishers.publisherset'], null=False)),
            ('targetvalue', models.ForeignKey(orm[u'targeting.targetvalue'], null=False))
        ))
        db.create_unique(u'publishers_publisherset_target_values', ['publisherset_id', 'targetvalue_id'])

    def backwards(self, orm):
        # Deleting model 'PublisherSet'
        db.delete_table(u'publishers_publisherset')

        # Removing M2M table for field target_values on 'PublisherSet'
        db.delete_table('publishers_publisherset_target_values')

    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '40'})
        },
        u'publishers.publisherset': {
            'Meta': {'object_name': 'PublisherSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publisher_sets'", 'to': u"orm['account.Account']"}),
            'set_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'target_values': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.TargetValue']", 'symmetrical': 'False'})
        },
        u'targeting.exchange': {
            'Meta': {'object_name': 'Exchange'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'targeting.targetvalue': {
            'Meta': {'ordering': "('id',)", 'unique_together': "[('exchange', 'category', 'value')]", 'object_name': 'TargetValue'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targeting.Exchange']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inserted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'representant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'represented'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['targeting.TargetValue']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'})
        }
    }

    complete_apps = ['publishers']
