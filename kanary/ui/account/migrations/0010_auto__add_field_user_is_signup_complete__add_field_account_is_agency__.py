# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.is_signup_complete'
        db.add_column(u'account_user', 'is_signup_complete',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Account.is_agency'
        db.add_column(u'account_account', 'is_agency',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Account.company_name'
        db.add_column(u'account_account', 'company_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Account.first_name'
        db.add_column(u'account_account', 'first_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Account.last_name'
        db.add_column(u'account_account', 'last_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Account.address'
        db.add_column(u'account_account', 'address',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Account.city'
        db.add_column(u'account_account', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True),
                      keep_default=False)

        # Adding field 'Account.zip_code'
        db.add_column(u'account_account', 'zip_code',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True),
                      keep_default=False)

        # Adding field 'Account.country'
        db.add_column(u'account_account', 'country',
                      self.gf('django.db.models.fields.CharField')(max_length=5, null=True),
                      keep_default=False)

        # Adding field 'Account.province'
        db.add_column(u'account_account', 'province',
                      self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Account.phone'
        db.add_column(u'account_account', 'phone',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)

        # Adding field 'Account.vat'
        db.add_column(u'account_account', 'vat',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Account.insufficient_funds_sent_emails_count'
        db.add_column(u'account_account', 'insufficient_funds_sent_emails_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Account.insufficient_funds_last_sent_email_at'
        db.add_column(u'account_account', 'insufficient_funds_last_sent_email_at',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.is_signup_complete'
        db.delete_column(u'account_user', 'is_signup_complete')

        # Deleting field 'Account.is_agency'
        db.delete_column(u'account_account', 'is_agency')

        # Deleting field 'Account.company_name'
        db.delete_column(u'account_account', 'company_name')

        # Deleting field 'Account.first_name'
        db.delete_column(u'account_account', 'first_name')

        # Deleting field 'Account.last_name'
        db.delete_column(u'account_account', 'last_name')

        # Deleting field 'Account.address'
        db.delete_column(u'account_account', 'address')

        # Deleting field 'Account.city'
        db.delete_column(u'account_account', 'city')

        # Deleting field 'Account.zip_code'
        db.delete_column(u'account_account', 'zip_code')

        # Deleting field 'Account.country'
        db.delete_column(u'account_account', 'country')

        # Deleting field 'Account.province'
        db.delete_column(u'account_account', 'province')

        # Deleting field 'Account.phone'
        db.delete_column(u'account_account', 'phone')

        # Deleting field 'Account.vat'
        db.delete_column(u'account_account', 'vat')

        # Deleting field 'Account.insufficient_funds_sent_emails_count'
        db.delete_column(u'account_account', 'insufficient_funds_sent_emails_count')

        # Deleting field 'Account.insufficient_funds_last_sent_email_at'
        db.delete_column(u'account_account', 'insufficient_funds_last_sent_email_at')


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
        u'account.invoice': {
            'Meta': {'ordering': "('-datetime',)", 'object_name': 'Invoice'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'amount': ('ui.fields.BudgetDecimalField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'account.payment': {
            'Meta': {'ordering': "('-datetime',)", 'object_name': 'Payment'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'amount': ('ui.fields.BudgetDecimalField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'account.user': {
            'Meta': {'object_name': 'User'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'users'", 'to': u"orm['account.Account']"}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_signup_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'unread_events_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['account']