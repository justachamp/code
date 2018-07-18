# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing index on 'ReportStrategyAge', fields ['time']
        db.delete_index(u'report_reportstrategyage', ['time'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['time']
        db.delete_index(u'report_reportstrategypublishernetwork', ['time'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['time']
        db.delete_index(u'report_reportstrategypeer39language', ['time'])

        # Removing index on 'ReportCampaignCategory', fields ['time']
        db.delete_index(u'report_reportcampaigncategory', ['time'])

        # Removing index on 'ReportCampaignDomain', fields ['time']
        db.delete_index(u'report_reportcampaigndomain', ['time'])

        # Removing index on 'ReportStrategyDomain', fields ['time']
        db.delete_index(u'report_reportstrategydomain', ['time'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['time']
        db.delete_index(u'report_reportcampaignproximicnotice', ['time'])

        # Removing index on 'ReportCampaignPosition', fields ['time']
        db.delete_index(u'report_reportcampaignposition', ['time'])

        # Removing index on 'ReportStrategyProximicContext', fields ['time']
        db.delete_index(u'report_reportstrategyproximiccontext', ['time'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['time']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['time'])

        # Removing index on 'ReportStrategyCategory', fields ['time']
        db.delete_index(u'report_reportstrategycategory', ['time'])

        # Removing index on 'ReportCampaign', fields ['time']
        db.delete_index(u'report_reportcampaign', ['time'])

        # Removing index on 'ReportCampaignPublisher', fields ['time']
        db.delete_index(u'report_reportcampaignpublisher', ['time'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['time']
        db.delete_index(u'report_reportstrategyproximicquality', ['time'])

        # Removing index on 'ReportCampaignCarrier', fields ['time']
        db.delete_index(u'report_reportcampaigncarrier', ['time'])

        # Removing index on 'ReportStrategyRegion', fields ['time']
        db.delete_index(u'report_reportstrategyregion', ['time'])

        # Removing index on 'ReportCampaignAge', fields ['time']
        db.delete_index(u'report_reportcampaignage', ['time'])

        # Removing index on 'ReportCampaignMake', fields ['time']
        db.delete_index(u'report_reportcampaignmake', ['time'])

        # Removing index on 'ReportStrategyCountry', fields ['time']
        db.delete_index(u'report_reportstrategycountry', ['time'])

        # Removing index on 'ReportCampaignGender', fields ['time']
        db.delete_index(u'report_reportcampaigngender', ['time'])

        # Removing index on 'ReportStrategyOs', fields ['time']
        db.delete_index(u'report_reportstrategyos', ['time'])

        # Removing index on 'ReportCampaignSite', fields ['time']
        db.delete_index(u'report_reportcampaignsite', ['time'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['time']
        db.delete_index(u'report_reportstrategypeer39contextual', ['time'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['time']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['time'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['time']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['time'])

        # Removing index on 'ReportCampaignCountry', fields ['time']
        db.delete_index(u'report_reportcampaigncountry', ['time'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['time']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['time'])

        # Removing index on 'ReportStrategyGender', fields ['time']
        db.delete_index(u'report_reportstrategygender', ['time'])

        # Removing index on 'ReportAdvert', fields ['time']
        db.delete_index(u'report_reportadvert', ['time'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['time']
        db.delete_index(u'report_reportcampaignpeer39language', ['time'])

        # Removing index on 'ReportStrategyCarrier', fields ['time']
        db.delete_index(u'report_reportstrategycarrier', ['time'])

        # Removing index on 'ReportCampaignOs', fields ['time']
        db.delete_index(u'report_reportcampaignos', ['time'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['time']
        db.delete_index(u'report_reportstrategypeer39brand', ['time'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['time']
        db.delete_index(u'report_reportstrategyproximicsafety', ['time'])

        # Removing index on 'ReportStrategyPublisher', fields ['time']
        db.delete_index(u'report_reportstrategypublisher', ['time'])

        # Removing index on 'ReportStrategy', fields ['time']
        db.delete_index(u'report_reportstrategy', ['time'])

        # Removing index on 'ReportStrategyModel', fields ['time']
        db.delete_index(u'report_reportstrategymodel', ['time'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['time']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['time'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['time']
        db.delete_index(u'report_reportstrategypeer39quality', ['time'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['time']
        db.delete_index(u'report_reportstrategyproximicnotice', ['time'])

        # Removing index on 'ReportCampaignModel', fields ['time']
        db.delete_index(u'report_reportcampaignmodel', ['time'])

        # Removing index on 'ReportCampaignCity', fields ['time']
        db.delete_index(u'report_reportcampaigncity', ['time'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['time']
        db.delete_index(u'report_reportcampaignpeer39quality', ['time'])

        # Removing index on 'ReportCampaignRegion', fields ['time']
        db.delete_index(u'report_reportcampaignregion', ['time'])

        # Removing index on 'ReportStrategyMake', fields ['time']
        db.delete_index(u'report_reportstrategymake', ['time'])

        # Removing index on 'ReportStrategyCity', fields ['time']
        db.delete_index(u'report_reportstrategycity', ['time'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['time']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['time'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['time']
        db.delete_index(u'report_reportcampaignproximicplace', ['time'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['time']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['time'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['time']
        db.delete_index(u'report_reportcampaignproximicsafety', ['time'])

        # Removing index on 'ReportStrategyPosition', fields ['time']
        db.delete_index(u'report_reportstrategyposition', ['time'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['time']
        db.delete_index(u'report_reportcampaignpeer39brand', ['time'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['time']
        db.delete_index(u'report_reportcampaignproximicquality', ['time'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['time']
        db.delete_index(u'report_reportstrategyproximicplace', ['time'])

        # Removing index on 'ReportStrategySite', fields ['time']
        db.delete_index(u'report_reportstrategysite', ['time'])


    def backwards(self, orm):
        # Adding index on 'ReportStrategySite', fields ['time']
        db.create_index(u'report_reportstrategysite', ['time'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['time']
        db.create_index(u'report_reportstrategyproximicplace', ['time'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['time']
        db.create_index(u'report_reportcampaignproximicquality', ['time'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['time']
        db.create_index(u'report_reportcampaignpeer39brand', ['time'])

        # Adding index on 'ReportStrategyPosition', fields ['time']
        db.create_index(u'report_reportstrategyposition', ['time'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['time']
        db.create_index(u'report_reportcampaignproximicsafety', ['time'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['time']
        db.create_index(u'report_reportcampaignproximiclanguage', ['time'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['time']
        db.create_index(u'report_reportcampaignproximicplace', ['time'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['time']
        db.create_index(u'report_reportstrategyproximiclanguage', ['time'])

        # Adding index on 'ReportStrategyCity', fields ['time']
        db.create_index(u'report_reportstrategycity', ['time'])

        # Adding index on 'ReportStrategyMake', fields ['time']
        db.create_index(u'report_reportstrategymake', ['time'])

        # Adding index on 'ReportCampaignRegion', fields ['time']
        db.create_index(u'report_reportcampaignregion', ['time'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['time']
        db.create_index(u'report_reportcampaignpeer39quality', ['time'])

        # Adding index on 'ReportCampaignCity', fields ['time']
        db.create_index(u'report_reportcampaigncity', ['time'])

        # Adding index on 'ReportCampaignModel', fields ['time']
        db.create_index(u'report_reportcampaignmodel', ['time'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['time']
        db.create_index(u'report_reportstrategyproximicnotice', ['time'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['time']
        db.create_index(u'report_reportstrategypeer39quality', ['time'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['time']
        db.create_index(u'report_reportcampaignpeer39contextual', ['time'])

        # Adding index on 'ReportStrategyModel', fields ['time']
        db.create_index(u'report_reportstrategymodel', ['time'])

        # Adding index on 'ReportStrategy', fields ['time']
        db.create_index(u'report_reportstrategy', ['time'])

        # Adding index on 'ReportStrategyPublisher', fields ['time']
        db.create_index(u'report_reportstrategypublisher', ['time'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['time']
        db.create_index(u'report_reportstrategyproximicsafety', ['time'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['time']
        db.create_index(u'report_reportstrategypeer39brand', ['time'])

        # Adding index on 'ReportCampaignOs', fields ['time']
        db.create_index(u'report_reportcampaignos', ['time'])

        # Adding index on 'ReportStrategyCarrier', fields ['time']
        db.create_index(u'report_reportstrategycarrier', ['time'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['time']
        db.create_index(u'report_reportcampaignpeer39language', ['time'])

        # Adding index on 'ReportAdvert', fields ['time']
        db.create_index(u'report_reportadvert', ['time'])

        # Adding index on 'ReportStrategyGender', fields ['time']
        db.create_index(u'report_reportstrategygender', ['time'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['time']
        db.create_index(u'report_reportstrategyproximicmaturity', ['time'])

        # Adding index on 'ReportCampaignCountry', fields ['time']
        db.create_index(u'report_reportcampaigncountry', ['time'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['time']
        db.create_index(u'report_reportcampaignpublishernetwork', ['time'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['time']
        db.create_index(u'report_reportcampaignproximicmaturity', ['time'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['time']
        db.create_index(u'report_reportstrategypeer39contextual', ['time'])

        # Adding index on 'ReportCampaignSite', fields ['time']
        db.create_index(u'report_reportcampaignsite', ['time'])

        # Adding index on 'ReportStrategyOs', fields ['time']
        db.create_index(u'report_reportstrategyos', ['time'])

        # Adding index on 'ReportCampaignGender', fields ['time']
        db.create_index(u'report_reportcampaigngender', ['time'])

        # Adding index on 'ReportStrategyCountry', fields ['time']
        db.create_index(u'report_reportstrategycountry', ['time'])

        # Adding index on 'ReportCampaignMake', fields ['time']
        db.create_index(u'report_reportcampaignmake', ['time'])

        # Adding index on 'ReportCampaignAge', fields ['time']
        db.create_index(u'report_reportcampaignage', ['time'])

        # Adding index on 'ReportStrategyRegion', fields ['time']
        db.create_index(u'report_reportstrategyregion', ['time'])

        # Adding index on 'ReportCampaignCarrier', fields ['time']
        db.create_index(u'report_reportcampaigncarrier', ['time'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['time']
        db.create_index(u'report_reportstrategyproximicquality', ['time'])

        # Adding index on 'ReportCampaignPublisher', fields ['time']
        db.create_index(u'report_reportcampaignpublisher', ['time'])

        # Adding index on 'ReportCampaign', fields ['time']
        db.create_index(u'report_reportcampaign', ['time'])

        # Adding index on 'ReportStrategyCategory', fields ['time']
        db.create_index(u'report_reportstrategycategory', ['time'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['time']
        db.create_index(u'report_reportcampaignproximiccontextual', ['time'])

        # Adding index on 'ReportStrategyProximicContext', fields ['time']
        db.create_index(u'report_reportstrategyproximiccontext', ['time'])

        # Adding index on 'ReportCampaignPosition', fields ['time']
        db.create_index(u'report_reportcampaignposition', ['time'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['time']
        db.create_index(u'report_reportcampaignproximicnotice', ['time'])

        # Adding index on 'ReportStrategyDomain', fields ['time']
        db.create_index(u'report_reportstrategydomain', ['time'])

        # Adding index on 'ReportCampaignDomain', fields ['time']
        db.create_index(u'report_reportcampaigndomain', ['time'])

        # Adding index on 'ReportCampaignCategory', fields ['time']
        db.create_index(u'report_reportcampaigncategory', ['time'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['time']
        db.create_index(u'report_reportstrategypeer39language', ['time'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['time']
        db.create_index(u'report_reportstrategypublishernetwork', ['time'])

        # Adding index on 'ReportStrategyAge', fields ['time']
        db.create_index(u'report_reportstrategyage', ['time'])


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
        u'campaign.advert': {
            'Meta': {'ordering': "['id']", 'object_name': 'Advert'},
            'budget_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_spent_commission': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'cache_is_dirty': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'creative': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['storage.Creative']", 'on_delete': 'models.PROTECT'}),
            'custom_bid_CPM': ('ui.fields.CPMDecimalField', [], {'null': 'True'}),
            'custom_variable': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'js_code': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'landing_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Site']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
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
            'budget_bid_CPM': ('ui.fields.CPMDecimalField', [], {}),
            'budget_daily': ('ui.fields.BudgetDecimalField', [], {'null': 'True', 'blank': 'True'}),
            'budget_daily_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_spent_commission': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_total': ('ui.fields.BudgetDecimalField', [], {}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']"}),
            'capping_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'capping_day_spent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'capping_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'capping_total_spent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content_category_values': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.ContentCategory']", 'symmetrical': 'False', 'blank': 'True'}),
            'content_category_values_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.ContentCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'exchanges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.Exchange']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'is_UTM_tags': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_day_parted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_distributed_evenly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_targeted_devices': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_targeted_local': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_targeted_publisher': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_targeted_user_profile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landing_site_variable': ('django.db.models.fields.CharField', [], {'max_length': '511', 'null': 'True', 'blank': 'True'}),
            'landing_sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['campaign.SiteRatio']", 'symmetrical': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'publisherset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publishers.PublisherSet']", 'null': 'True', 'blank': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'is_network': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publisher_sets'", 'to': u"orm['account.Account']"}),
            'target_values': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.TargetValue']", 'symmetrical': 'False'})
        },
        u'report.reportadvert': {
            'Meta': {'unique_together': "(('related', 'time'),)", 'object_name': 'ReportAdvert'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaign': {
            'Meta': {'unique_together': "(('related', 'time'),)", 'object_name': 'ReportCampaign'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignAge'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_age'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaigncarrier': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCarrier'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_carrier'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaigncategory': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCategory'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_category'", 'null': 'True', 'to': u"orm['targeting.ContentCategoryValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaigncity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_city'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaigncountry': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCountry'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_country'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaigndomain': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignDomain'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_domain'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaigngender': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignGender'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_gender'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignmake': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignMake'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_make'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignmodel': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignModel'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_model'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignos': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignOs'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_os'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignpeer39brand': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Brand'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_brandprotection'", 'null': 'True', 'to': u"orm['targeting.Peer39BrandProtection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignpeer39contextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Contextual'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_contextual'", 'null': 'True', 'to': u"orm['targeting.Peer39ContextualSegment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignpeer39language': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Language'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.Peer39PageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignpeer39quality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Quality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagequality'", 'null': 'True', 'to': u"orm['targeting.Peer39PageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignposition': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPosition'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_position'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximiccontextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicContextual'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_contextual'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximiclanguage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicLanguage'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximicmaturity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicMaturity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_maturity'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicMaturityRating']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximicnotice': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicNotice'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagenoticeability'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximicplace': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicPlace'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pageplacement'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximicquality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicQuality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagequality'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximicsafety': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicSafety'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_safety'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicSafetyLevel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignpublisher': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPublisher'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_publisher'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignpublishernetwork': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPublisherNetwork'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_network'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignregion': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignRegion'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_region'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignsite': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignSite'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategy': {
            'Meta': {'unique_together': "(('related', 'time'),)", 'object_name': 'ReportStrategy'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyAge'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_age'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategycarrier': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCarrier'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_carrier'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategycategory': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCategory'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_category'", 'null': 'True', 'to': u"orm['targeting.ContentCategoryValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategycity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_city'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategycountry': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCountry'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_country'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategydomain': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyDomain'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_domain'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategygender': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyGender'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_gender'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategymake': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyMake'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_make'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategymodel': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyModel'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_model'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyos': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyOs'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_os'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategypeer39brand': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Brand'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_brandprotection'", 'null': 'True', 'to': u"orm['targeting.Peer39BrandProtection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategypeer39contextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Contextual'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_contextual'", 'null': 'True', 'to': u"orm['targeting.Peer39ContextualSegment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategypeer39language': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Language'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.Peer39PageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategypeer39quality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Quality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagequality'", 'null': 'True', 'to': u"orm['targeting.Peer39PageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyposition': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPosition'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_position'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximiccontext': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicContext'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_contextual'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximiclanguage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicLanguage'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximicmaturity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicMaturity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_maturity'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicMaturityRating']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximicnotice': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicNotice'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagenoticeability'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximicplace': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicPlace'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pageplacement'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximicquality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicQuality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagequality'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximicsafety': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicSafety'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_safety'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicSafetyLevel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategypublisher': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPublisher'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_publisher'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategypublishernetwork': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPublisherNetwork'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_network'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyregion': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyRegion'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_region'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategysite': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategySite'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'storage.audience': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'owner'),)", 'object_name': 'Audience'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"})
        },
        u'storage.creative': {
            'Meta': {'ordering': "['name']", 'object_name': 'Creative'},
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
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.ContentCategory']"})
        },
        u'targeting.contentcategoryvalue': {
            'Meta': {'ordering': "('id',)", 'unique_together': "[('name', 'exchange', 'representant')]", 'object_name': 'ContentCategoryValue'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targeting.Exchange']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'representant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'represented'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['targeting.ContentCategory']"})
        },
        u'targeting.exchange': {
            'Meta': {'object_name': 'Exchange'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'targeting.peer39brandprotection': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Peer39BrandProtection'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'peer39_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'targeting.peer39contextualsegment': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Peer39ContextualSegment'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.Peer39ContextualSegment']"}),
            'peer39_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'targeting.peer39pagelanguage': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Peer39PageLanguage'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'peer39_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'targeting.peer39pagequality': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Peer39PageQuality'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
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
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"})
        },
        u'targeting.segmentproximicmaturityrating': {
            'Meta': {'object_name': 'SegmentProximicMaturityRating'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'targeting.segmentproximicpagelanguage': {
            'Meta': {'ordering': "('name',)", 'object_name': 'SegmentProximicPageLanguage'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"})
        },
        u'targeting.segmentproximicpagenoticeability': {
            'Meta': {'ordering': "('id',)", 'object_name': 'SegmentProximicPageNoticeability'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"})
        },
        u'targeting.segmentproximicpageplacement': {
            'Meta': {'ordering': "('id',)", 'object_name': 'SegmentProximicPagePlacement'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"})
        },
        u'targeting.segmentproximicpagequality': {
            'Meta': {'ordering': "('id',)", 'object_name': 'SegmentProximicPageQuality'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"})
        },
        u'targeting.segmentproximicsafetylevel': {
            'Meta': {'object_name': 'SegmentProximicSafetyLevel'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'targeting.targetvalue': {
            'Meta': {'ordering': "('id',)", 'unique_together': "[('exchange', 'category', 'value')]", 'object_name': 'TargetValue'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targeting.Exchange']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'representant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'represented'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['targeting.TargetValue']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'})
        }
    }

    complete_apps = ['report']