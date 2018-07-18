# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DailySpendings'
        db.create_table(u'bidding_spendings_dailyspendings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(related_name='daily_spendings', to=orm['account.Account'])),
            ('budget_spent', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('hidden_commission', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('kanary_commission', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
        ))
        db.send_create_signal(u'bidding_spendings', ['DailySpendings'])

        # Adding unique constraint on 'DailySpendings', fields ['account', 'date']
        db.create_unique(u'bidding_spendings_dailyspendings', ['account_id', 'date'])


    def backwards(self, orm):
        # Removing unique constraint on 'DailySpendings', fields ['account', 'date']
        db.delete_unique(u'bidding_spendings_dailyspendings', ['account_id', 'date'])

        # Deleting model 'DailySpendings'
        db.delete_table(u'bidding_spendings_dailyspendings')


    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'account_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'commission': ('django.db.models.fields.SmallIntegerField', [], {'default': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '40'})
        },
        u'bidding_spendings.dailyspendings': {
            'Meta': {'ordering': "('account', '-date')", 'unique_together': "(('account', 'date'),)", 'object_name': 'DailySpendings'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'daily_spendings'", 'to': u"orm['account.Account']"}),
            'budget_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'hidden_commission': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kanary_commission': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        }
    }

    complete_apps = ['bidding_spendings']