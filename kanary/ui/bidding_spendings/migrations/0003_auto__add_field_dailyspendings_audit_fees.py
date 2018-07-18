# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DailySpendings.audit_fees'
        db.add_column(u'bidding_spendings_dailyspendings', 'audit_fees',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DailySpendings.audit_fees'
        db.delete_column(u'bidding_spendings_dailyspendings', 'audit_fees')


    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'account_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'commission': ('django.db.models.fields.SmallIntegerField', [], {'default': "'10'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '40'})
        },
        u'bidding_spendings.dailyspendings': {
            'Meta': {'ordering': "('account', '-date')", 'unique_together': "(('account', 'date'),)", 'object_name': 'DailySpendings'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'daily_spendings'", 'to': u"orm['account.Account']"}),
            'audit_fees': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_peer39': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_proximic': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'hidden_commission': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kanary_commission': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        }
    }

    complete_apps = ['bidding_spendings']