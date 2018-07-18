# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DailySpendings.data_cost_lotame'
        db.add_column(u'bidding_spendings_dailyspendings', 'data_cost_lotame',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DailySpendings.data_cost_lotame'
        db.delete_column(u'bidding_spendings_dailyspendings', 'data_cost_lotame')


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
        u'bidding_spendings.dailyspendings': {
            'Meta': {'ordering': "('account', '-date')", 'unique_together': "(('account', 'date'),)", 'object_name': 'DailySpendings'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'daily_spendings'", 'to': u"orm['account.Account']"}),
            'audit_fees': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_lotame': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_peer39': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_proximic': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'hidden_commission': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kanary_commission': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        }
    }

    complete_apps = ['bidding_spendings']