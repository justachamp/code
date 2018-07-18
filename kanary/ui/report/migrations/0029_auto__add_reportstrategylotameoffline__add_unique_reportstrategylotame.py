# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReportStrategyLotameOffline'
        db.create_table(u'report_reportstrategylotameoffline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('imp_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Strategy'], to_field='id_random')),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_strategy_lotameoffline', null=True, to=orm['targeting.LotameOffline'])),
        ))
        db.send_create_signal(u'report', ['ReportStrategyLotameOffline'])

        # Adding unique constraint on 'ReportStrategyLotameOffline', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportstrategylotameoffline', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportCampaignLotameBehavioralInterest'
        db.create_table(u'report_reportcampaignlotamebehavioralinterest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('imp_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Campaign'], to_field='id_random')),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_campaign_lotamebehavioralinterest', null=True, to=orm['targeting.LotameBehavioralInterest'])),
        ))
        db.send_create_signal(u'report', ['ReportCampaignLotameBehavioralInterest'])

        # Adding model 'ReportStrategyLotameBehavioralInterest'
        db.create_table(u'report_reportstrategylotamebehavioralinterest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('imp_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Strategy'], to_field='id_random')),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_strategy_lotamebehavioralinterest', null=True, to=orm['targeting.LotameBehavioralInterest'])),
        ))
        db.send_create_signal(u'report', ['ReportStrategyLotameBehavioralInterest'])

        # Adding model 'ReportCampaignLotameDemographic'
        db.create_table(u'report_reportcampaignlotamedemographic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('imp_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Campaign'], to_field='id_random')),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_campaign_lotamedemographic', null=True, to=orm['targeting.LotameDemographic'])),
        ))
        db.send_create_signal(u'report', ['ReportCampaignLotameDemographic'])

        # Adding unique constraint on 'ReportCampaignLotameDemographic', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportcampaignlotamedemographic', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportCampaignLotameInfluencers'
        db.create_table(u'report_reportcampaignlotameinfluencers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('imp_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Campaign'], to_field='id_random')),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_campaign_lotameinfluencers', null=True, to=orm['targeting.LotameInfluencers'])),
        ))
        db.send_create_signal(u'report', ['ReportCampaignLotameInfluencers'])

        # Adding unique constraint on 'ReportCampaignLotameInfluencers', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportcampaignlotameinfluencers', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportStrategyLotameAdvancedDemographic'
        db.create_table(u'report_reportstrategylotameadvanceddemographic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('imp_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Strategy'], to_field='id_random')),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_strategy_lotameadvanceddemographic', null=True, to=orm['targeting.LotameAdvancedDemographic'])),
        ))
        db.send_create_signal(u'report', ['ReportStrategyLotameAdvancedDemographic'])

        # Adding model 'ReportStrategyLotameInfluencers'
        db.create_table(u'report_reportstrategylotameinfluencers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('imp_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Strategy'], to_field='id_random')),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_strategy_lotameinfluencers', null=True, to=orm['targeting.LotameInfluencers'])),
        ))
        db.send_create_signal(u'report', ['ReportStrategyLotameInfluencers'])

        # Adding unique constraint on 'ReportStrategyLotameInfluencers', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportstrategylotameinfluencers', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportCampaignLotameAdvancedDemographic'
        db.create_table(u'report_reportcampaignlotameadvanceddemographic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('imp_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Campaign'], to_field='id_random')),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_campaign_lotameadvanceddemographic', null=True, to=orm['targeting.LotameAdvancedDemographic'])),
        ))
        db.send_create_signal(u'report', ['ReportCampaignLotameAdvancedDemographic'])

        # Adding model 'ReportStrategyLotameDemographic'
        db.create_table(u'report_reportstrategylotamedemographic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('imp_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Strategy'], to_field='id_random')),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_strategy_lotamedemographic', null=True, to=orm['targeting.LotameDemographic'])),
        ))
        db.send_create_signal(u'report', ['ReportStrategyLotameDemographic'])

        # Adding unique constraint on 'ReportStrategyLotameDemographic', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportstrategylotamedemographic', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportCampaignLotameOffline'
        db.create_table(u'report_reportcampaignlotameoffline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('imp_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Campaign'], to_field='id_random')),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_campaign_lotameoffline', null=True, to=orm['targeting.LotameOffline'])),
        ))
        db.send_create_signal(u'report', ['ReportCampaignLotameOffline'])

        # Adding unique constraint on 'ReportCampaignLotameOffline', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportcampaignlotameoffline', ['dimension_id', 'related_id', 'time'])


    def backwards(self, orm):
        # Removing unique constraint on 'ReportCampaignLotameOffline', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportcampaignlotameoffline', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportStrategyLotameDemographic', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportstrategylotamedemographic', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportStrategyLotameInfluencers', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportstrategylotameinfluencers', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportCampaignLotameInfluencers', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportcampaignlotameinfluencers', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportCampaignLotameDemographic', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportcampaignlotamedemographic', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportStrategyLotameOffline', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportstrategylotameoffline', ['dimension_id', 'related_id', 'time'])

        # Deleting model 'ReportStrategyLotameOffline'
        db.delete_table(u'report_reportstrategylotameoffline')

        # Deleting model 'ReportCampaignLotameBehavioralInterest'
        db.delete_table(u'report_reportcampaignlotamebehavioralinterest')

        # Deleting model 'ReportStrategyLotameBehavioralInterest'
        db.delete_table(u'report_reportstrategylotamebehavioralinterest')

        # Deleting model 'ReportCampaignLotameDemographic'
        db.delete_table(u'report_reportcampaignlotamedemographic')

        # Deleting model 'ReportCampaignLotameInfluencers'
        db.delete_table(u'report_reportcampaignlotameinfluencers')

        # Deleting model 'ReportStrategyLotameAdvancedDemographic'
        db.delete_table(u'report_reportstrategylotameadvanceddemographic')

        # Deleting model 'ReportStrategyLotameInfluencers'
        db.delete_table(u'report_reportstrategylotameinfluencers')

        # Deleting model 'ReportCampaignLotameAdvancedDemographic'
        db.delete_table(u'report_reportcampaignlotameadvanceddemographic')

        # Deleting model 'ReportStrategyLotameDemographic'
        db.delete_table(u'report_reportstrategylotamedemographic')

        # Deleting model 'ReportCampaignLotameOffline'
        db.delete_table(u'report_reportcampaignlotameoffline')


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
        u'campaign.advert': {
            'Meta': {'ordering': "['id']", 'object_name': 'Advert'},
            'cache_is_dirty': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'creative': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['storage.Creative']", 'on_delete': 'models.PROTECT'}),
            'custom_bid_CPM': ('ui.fields.CPMDecimalField', [], {'null': 'True'}),
            'custom_pixel': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'custom_variable': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'js_code': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'landing_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Site']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'strategy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']"})
        },
        u'campaign.campaign': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('account', 'slug'),)", 'object_name': 'Campaign'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'budget_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_spent_commission': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_total': ('ui.fields.BudgetDecimalField', [], {}),
            'cache_is_dirty': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'cap_campaign_selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cap_creative': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cap_creative_period': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'cap_creative_period_presented': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'cap_creative_presented': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cap_creative_selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cap_strategy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cap_strategy_period': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'cap_strategy_period_presented': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'cap_strategy_presented': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cap_strategy_selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cap_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cap_total_period': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'cap_total_period_presented': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'cap_total_presented': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end_UTC': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'is_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_paused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landing_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Site']", 'on_delete': 'models.PROTECT'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_UTC': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'campaign.site': {
            'Meta': {'unique_together': "(('url', 'owner'),)", 'object_name': 'Site'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sites'", 'to': u"orm['account.Account']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'campaign.siteratio': {
            'Meta': {'object_name': 'SiteRatio'},
            'custom_variable': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ratio': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Site']", 'on_delete': 'models.PROTECT'})
        },
        u'campaign.strategy': {
            'Meta': {'ordering': "['name']", 'unique_together': "[('campaign', 'slug')]", 'object_name': 'Strategy'},
            'audiences': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'includes'", 'blank': 'True', 'to': u"orm['storage.Audience']"}),
            'audiences_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'excludes'", 'blank': 'True', 'to': u"orm['storage.Audience']"}),
            'budget_bid_CPM': ('ui.fields.CPMDecimalField', [], {'null': 'True', 'blank': 'True'}),
            'budget_daily': ('ui.fields.BudgetDecimalField', [], {'null': 'True', 'blank': 'True'}),
            'budget_daily_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_spent_commission': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_total': ('ui.fields.BudgetDecimalField', [], {}),
            'cache_is_dirty': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']"}),
            'capping_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'capping_day_spent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'capping_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'capping_total_spent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content_category_values': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.ContentCategory']", 'symmetrical': 'False', 'blank': 'True'}),
            'content_category_values_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.ContentCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'is_UTM_tags': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_automatically_bidded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_day_parted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_distributed_evenly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_paused': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_targeted_devices': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_targeted_local': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_targeted_publisher': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_targeted_user_profile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landing_site_variable': ('django.db.models.fields.CharField', [], {'max_length': '511', 'null': 'True', 'blank': 'True'}),
            'landing_sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['campaign.SiteRatio']", 'symmetrical': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'optimized_metric': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'publisherset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishers.PublisherSet']", 'null': 'True', 'blank': 'True'}),
            'segment_lotame_advanced_demographic_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.LotameAdvancedDemographic']"}),
            'segment_lotame_advanved_demographic': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.LotameAdvancedDemographic']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_lotame_behavioral_interest': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.LotameBehavioralInterest']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_lotame_behavioral_interest_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.LotameBehavioralInterest']"}),
            'segment_lotame_demographic': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.LotameDemographic']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_lotame_demographic_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.LotameDemographic']"}),
            'segment_lotame_influencers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.LotameInfluencers']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_lotame_influencers_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.LotameInfluencers']"}),
            'segment_lotame_offline': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.LotameOffline']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_lotame_offline_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.LotameOffline']"}),
            'segment_peer_brand_protection': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.Peer39BrandProtection']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_peer_brand_protection_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.Peer39BrandProtection']"}),
            'segment_peer_contextual': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.Peer39ContextualSegment']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_peer_contextual_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.Peer39ContextualSegment']"}),
            'segment_peer_page_language': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.Peer39PageLanguage']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_peer_page_language_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.Peer39PageLanguage']"}),
            'segment_peer_page_quality': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.Peer39PageQuality']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_peer_page_quality_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.Peer39PageQuality']"}),
            'segment_proximic_contextual': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.SegmentProximicContextual']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_proximic_contextual_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"}),
            'segment_proximic_maturity_rating': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.SegmentProximicMaturityRating']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_proximic_maturity_rating_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.SegmentProximicMaturityRating']"}),
            'segment_proximic_page_language': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.SegmentProximicPageLanguage']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_proximic_page_language_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"}),
            'segment_proximic_page_noticeability': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.SegmentProximicPageNoticeability']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_proximic_page_noticeability_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"}),
            'segment_proximic_page_placement': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.SegmentProximicPagePlacement']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_proximic_page_placement_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"}),
            'segment_proximic_page_quality': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.SegmentProximicPageQuality']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_proximic_page_quality_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"}),
            'segment_proximic_safety_level': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.SegmentProximicSafetyLevel']", 'symmetrical': 'False', 'blank': 'True'}),
            'segment_proximic_safety_level_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.SegmentProximicSafetyLevel']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'targeting_values': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.TargetValue']", 'symmetrical': 'False', 'blank': 'True'}),
            'targeting_values_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.TargetValue']"}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'site'", 'max_length': '6'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'publishers.publisherset': {
            'Meta': {'object_name': 'PublisherSet'},
            'blacklist': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'is_network': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publisher_sets'", 'to': u"orm['account.Account']"}),
            'target_values': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.TargetValue']", 'symmetrical': 'False'})
        },
        u'report.reportadvert': {
            'Meta': {'unique_together': "(('related', 'time'),)", 'object_name': 'ReportAdvert'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaign': {
            'Meta': {'unique_together': "(('related', 'time'),)", 'object_name': 'ReportCampaign'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignAge'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_age'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaigncarrier': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCarrier'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_carrier'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaigncategory': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCategory'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_category'", 'null': 'True', 'to': u"orm['targeting.ContentCategoryValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaigncity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCity'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_city'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaigncountry': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCountry'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_country'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaigndomain': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignDomain'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_domain'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaigngender': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignGender'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_gender'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignlotameadvanceddemographic': {
            'Meta': {'object_name': 'ReportCampaignLotameAdvancedDemographic'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_lotameadvanceddemographic'", 'null': 'True', 'to': u"orm['targeting.LotameAdvancedDemographic']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignlotamebehavioralinterest': {
            'Meta': {'object_name': 'ReportCampaignLotameBehavioralInterest'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_lotamebehavioralinterest'", 'null': 'True', 'to': u"orm['targeting.LotameBehavioralInterest']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignlotamedemographic': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignLotameDemographic'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_lotamedemographic'", 'null': 'True', 'to': u"orm['targeting.LotameDemographic']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignlotameinfluencers': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignLotameInfluencers'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_lotameinfluencers'", 'null': 'True', 'to': u"orm['targeting.LotameInfluencers']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignlotameoffline': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignLotameOffline'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_lotameoffline'", 'null': 'True', 'to': u"orm['targeting.LotameOffline']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignmake': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignMake'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_make'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignmodel': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignModel'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_model'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignos': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignOs'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_os'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignpeer39brand': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Brand'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_brandprotection'", 'null': 'True', 'to': u"orm['targeting.Peer39BrandProtection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignpeer39contextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Contextual'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_contextual'", 'null': 'True', 'to': u"orm['targeting.Peer39ContextualSegment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignpeer39language': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Language'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.Peer39PageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignpeer39quality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Quality'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagequality'", 'null': 'True', 'to': u"orm['targeting.Peer39PageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignposition': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPosition'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_position'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignproximiccontextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicContextual'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_contextual'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignproximiclanguage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicLanguage'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignproximicmaturity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicMaturity'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_maturity'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicMaturityRating']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignproximicnotice': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicNotice'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagenoticeability'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignproximicplace': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicPlace'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pageplacement'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignproximicquality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicQuality'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagequality'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignproximicsafety': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicSafety'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_safety'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicSafetyLevel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignpublisher': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPublisher'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_publisher'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignpublishernetwork': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPublisherNetwork'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_network'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignregion': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignRegion'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_region'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportcampaignsite': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignSite'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategy': {
            'Meta': {'unique_together': "(('related', 'time'),)", 'object_name': 'ReportStrategy'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategyage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyAge'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_age'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategycarrier': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCarrier'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_carrier'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategycategory': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCategory'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_category'", 'null': 'True', 'to': u"orm['targeting.ContentCategoryValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategycity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCity'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_city'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategycountry': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCountry'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_country'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategydomain': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyDomain'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_domain'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategygender': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyGender'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_gender'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategylotameadvanceddemographic': {
            'Meta': {'object_name': 'ReportStrategyLotameAdvancedDemographic'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_lotameadvanceddemographic'", 'null': 'True', 'to': u"orm['targeting.LotameAdvancedDemographic']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategylotamebehavioralinterest': {
            'Meta': {'object_name': 'ReportStrategyLotameBehavioralInterest'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_lotamebehavioralinterest'", 'null': 'True', 'to': u"orm['targeting.LotameBehavioralInterest']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategylotamedemographic': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyLotameDemographic'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_lotamedemographic'", 'null': 'True', 'to': u"orm['targeting.LotameDemographic']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategylotameinfluencers': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyLotameInfluencers'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_lotameinfluencers'", 'null': 'True', 'to': u"orm['targeting.LotameInfluencers']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategylotameoffline': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyLotameOffline'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_lotameoffline'", 'null': 'True', 'to': u"orm['targeting.LotameOffline']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategymake': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyMake'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_make'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategymodel': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyModel'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_model'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategyos': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyOs'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_os'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategypeer39brand': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Brand'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_brandprotection'", 'null': 'True', 'to': u"orm['targeting.Peer39BrandProtection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategypeer39contextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Contextual'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_contextual'", 'null': 'True', 'to': u"orm['targeting.Peer39ContextualSegment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategypeer39language': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Language'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.Peer39PageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategypeer39quality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Quality'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagequality'", 'null': 'True', 'to': u"orm['targeting.Peer39PageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategyposition': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPosition'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_position'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategyproximiccontext': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicContext'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_contextual'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategyproximiclanguage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicLanguage'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategyproximicmaturity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicMaturity'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_maturity'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicMaturityRating']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategyproximicnotice': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicNotice'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagenoticeability'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategyproximicplace': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicPlace'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pageplacement'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategyproximicquality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicQuality'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagequality'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategyproximicsafety': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicSafety'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_safety'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicSafetyLevel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategypublisher': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPublisher'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_publisher'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategypublishernetwork': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPublisherNetwork'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_network'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategyregion': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyRegion'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_region'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'report.reportstrategysite': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategySite'},
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'imp_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
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
        u'storage.creative': {
            'Meta': {'ordering': "['name']", 'object_name': 'Creative'},
            'appnexus_audit_blocked_no_funds': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'appnexus_feedback': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'appnexus_sla_eta': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'appnexus_status': ('django.db.models.fields.CharField', [], {'default': "'n'", 'max_length': '1'}),
            'audit_fees': ('ui.fields.BudgetDecimalField', [], {'default': '0'}),
            'cache_is_dirty': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'landing_site_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_storage.creative_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'to_audit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'targeting.appnexussegment': {
            'Meta': {'object_name': 'AppNexusSegment'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        u'targeting.contentcategory': {
            'Meta': {'ordering': "('id',)", 'unique_together': "[('name', 'parent')]", 'object_name': 'ContentCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.ContentCategory']"})
        },
        u'targeting.contentcategoryvalue': {
            'Meta': {'ordering': "('id',)", 'unique_together': "[('name', 'exchange', 'representant')]", 'object_name': 'ContentCategoryValue'},
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targeting.Exchange']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'representant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'represented'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['targeting.ContentCategory']"})
        },
        u'targeting.exchange': {
            'Meta': {'object_name': 'Exchange'},
            'code': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        u'targeting.lotameadvanceddemographic': {
            'Meta': {'object_name': 'LotameAdvancedDemographic'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lotame_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'targeting.lotamebehavioralinterest': {
            'Meta': {'object_name': 'LotameBehavioralInterest'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lotame_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'targeting.lotamedemographic': {
            'Meta': {'object_name': 'LotameDemographic'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lotame_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'targeting.lotameinfluencers': {
            'Meta': {'object_name': 'LotameInfluencers'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lotame_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'targeting.lotameoffline': {
            'Meta': {'object_name': 'LotameOffline'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lotame_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'targeting.peer39brandprotection': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Peer39BrandProtection'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'peer39_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'targeting.peer39contextualsegment': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Peer39ContextualSegment'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.Peer39ContextualSegment']"}),
            'peer39_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'targeting.peer39pagelanguage': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Peer39PageLanguage'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'peer39_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'targeting.peer39pagequality': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Peer39PageQuality'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.Peer39PageQuality']"}),
            'peer39_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'targeting.publishertargetvalue': {
            'Meta': {'ordering': "('id',)", 'object_name': 'PublisherTargetValue', '_ormbases': [u'targeting.TargetValue']},
            '_positions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            '_sizes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'segments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['targeting.AppNexusSegment']", 'symmetrical': 'False'}),
            u'targetvalue_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['targeting.TargetValue']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'targeting.segmentproximiccontextual': {
            'Meta': {'ordering': "('name',)", 'object_name': 'SegmentProximicContextual'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"})
        },
        u'targeting.segmentproximicmaturityrating': {
            'Meta': {'object_name': 'SegmentProximicMaturityRating'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'targeting.segmentproximicpagelanguage': {
            'Meta': {'ordering': "('name',)", 'object_name': 'SegmentProximicPageLanguage'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"})
        },
        u'targeting.segmentproximicpagenoticeability': {
            'Meta': {'ordering': "('id',)", 'object_name': 'SegmentProximicPageNoticeability'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"})
        },
        u'targeting.segmentproximicpageplacement': {
            'Meta': {'ordering': "('id',)", 'object_name': 'SegmentProximicPagePlacement'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"})
        },
        u'targeting.segmentproximicpagequality': {
            'Meta': {'ordering': "('id',)", 'object_name': 'SegmentProximicPageQuality'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"})
        },
        u'targeting.segmentproximicsafetylevel': {
            'Meta': {'object_name': 'SegmentProximicSafetyLevel'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'targeting.targetvalue': {
            'Meta': {'ordering': "('id',)", 'unique_together': "[('exchange', 'category', 'value')]", 'object_name': 'TargetValue'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targeting.Exchange']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'representant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'represented'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['targeting.TargetValue']"}),
            'value': ('django.db.models.fields.TextField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['report']