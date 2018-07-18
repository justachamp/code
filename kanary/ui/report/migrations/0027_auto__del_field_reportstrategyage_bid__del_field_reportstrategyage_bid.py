# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ReportStrategyAge.bid'
        db.delete_column(u'report_reportstrategyage', 'bid')

        # Deleting field 'ReportStrategyAge.bid_value'
        db.delete_column(u'report_reportstrategyage', 'bid_value')

        # Deleting field 'ReportStrategyPublisherNetwork.bid'
        db.delete_column(u'report_reportstrategypublishernetwork', 'bid')

        # Deleting field 'ReportStrategyPublisherNetwork.bid_value'
        db.delete_column(u'report_reportstrategypublishernetwork', 'bid_value')

        # Deleting field 'ReportStrategyPeer39Language.bid'
        db.delete_column(u'report_reportstrategypeer39language', 'bid')

        # Deleting field 'ReportStrategyPeer39Language.bid_value'
        db.delete_column(u'report_reportstrategypeer39language', 'bid_value')

        # Deleting field 'ReportCampaignCategory.bid'
        db.delete_column(u'report_reportcampaigncategory', 'bid')

        # Deleting field 'ReportCampaignCategory.bid_value'
        db.delete_column(u'report_reportcampaigncategory', 'bid_value')

        # Deleting field 'ReportCampaignDomain.bid'
        db.delete_column(u'report_reportcampaigndomain', 'bid')

        # Deleting field 'ReportCampaignDomain.bid_value'
        db.delete_column(u'report_reportcampaigndomain', 'bid_value')

        # Deleting field 'ReportStrategyDomain.bid'
        db.delete_column(u'report_reportstrategydomain', 'bid')

        # Deleting field 'ReportStrategyDomain.bid_value'
        db.delete_column(u'report_reportstrategydomain', 'bid_value')

        # Deleting field 'ReportCampaignProximicNotice.bid'
        db.delete_column(u'report_reportcampaignproximicnotice', 'bid')

        # Deleting field 'ReportCampaignProximicNotice.bid_value'
        db.delete_column(u'report_reportcampaignproximicnotice', 'bid_value')

        # Deleting field 'ReportCampaignPosition.bid'
        db.delete_column(u'report_reportcampaignposition', 'bid')

        # Deleting field 'ReportCampaignPosition.bid_value'
        db.delete_column(u'report_reportcampaignposition', 'bid_value')

        # Deleting field 'ReportStrategyProximicContext.bid'
        db.delete_column(u'report_reportstrategyproximiccontext', 'bid')

        # Deleting field 'ReportStrategyProximicContext.bid_value'
        db.delete_column(u'report_reportstrategyproximiccontext', 'bid_value')

        # Deleting field 'ReportCampaignProximicContextual.bid'
        db.delete_column(u'report_reportcampaignproximiccontextual', 'bid')

        # Deleting field 'ReportCampaignProximicContextual.bid_value'
        db.delete_column(u'report_reportcampaignproximiccontextual', 'bid_value')

        # Deleting field 'ReportStrategyCategory.bid'
        db.delete_column(u'report_reportstrategycategory', 'bid')

        # Deleting field 'ReportStrategyCategory.bid_value'
        db.delete_column(u'report_reportstrategycategory', 'bid_value')

        # Deleting field 'ReportCampaign.bid'
        db.delete_column(u'report_reportcampaign', 'bid')

        # Deleting field 'ReportCampaign.bid_value'
        db.delete_column(u'report_reportcampaign', 'bid_value')

        # Deleting field 'ReportCampaignPublisher.bid'
        db.delete_column(u'report_reportcampaignpublisher', 'bid')

        # Deleting field 'ReportCampaignPublisher.bid_value'
        db.delete_column(u'report_reportcampaignpublisher', 'bid_value')

        # Deleting field 'ReportStrategyProximicQuality.bid'
        db.delete_column(u'report_reportstrategyproximicquality', 'bid')

        # Deleting field 'ReportStrategyProximicQuality.bid_value'
        db.delete_column(u'report_reportstrategyproximicquality', 'bid_value')

        # Deleting field 'ReportCampaignCarrier.bid'
        db.delete_column(u'report_reportcampaigncarrier', 'bid')

        # Deleting field 'ReportCampaignCarrier.bid_value'
        db.delete_column(u'report_reportcampaigncarrier', 'bid_value')

        # Deleting field 'ReportStrategyRegion.bid'
        db.delete_column(u'report_reportstrategyregion', 'bid')

        # Deleting field 'ReportStrategyRegion.bid_value'
        db.delete_column(u'report_reportstrategyregion', 'bid_value')

        # Deleting field 'ReportCampaignAge.bid'
        db.delete_column(u'report_reportcampaignage', 'bid')

        # Deleting field 'ReportCampaignAge.bid_value'
        db.delete_column(u'report_reportcampaignage', 'bid_value')

        # Deleting field 'ReportCampaignMake.bid'
        db.delete_column(u'report_reportcampaignmake', 'bid')

        # Deleting field 'ReportCampaignMake.bid_value'
        db.delete_column(u'report_reportcampaignmake', 'bid_value')

        # Deleting field 'ReportStrategyCountry.bid'
        db.delete_column(u'report_reportstrategycountry', 'bid')

        # Deleting field 'ReportStrategyCountry.bid_value'
        db.delete_column(u'report_reportstrategycountry', 'bid_value')

        # Deleting field 'ReportCampaignGender.bid'
        db.delete_column(u'report_reportcampaigngender', 'bid')

        # Deleting field 'ReportCampaignGender.bid_value'
        db.delete_column(u'report_reportcampaigngender', 'bid_value')

        # Deleting field 'ReportStrategyOs.bid'
        db.delete_column(u'report_reportstrategyos', 'bid')

        # Deleting field 'ReportStrategyOs.bid_value'
        db.delete_column(u'report_reportstrategyos', 'bid_value')

        # Deleting field 'ReportCampaignSite.bid'
        db.delete_column(u'report_reportcampaignsite', 'bid')

        # Deleting field 'ReportCampaignSite.bid_value'
        db.delete_column(u'report_reportcampaignsite', 'bid_value')

        # Deleting field 'ReportStrategyPeer39Contextual.bid'
        db.delete_column(u'report_reportstrategypeer39contextual', 'bid')

        # Deleting field 'ReportStrategyPeer39Contextual.bid_value'
        db.delete_column(u'report_reportstrategypeer39contextual', 'bid_value')

        # Deleting field 'ReportCampaignProximicMaturity.bid'
        db.delete_column(u'report_reportcampaignproximicmaturity', 'bid')

        # Deleting field 'ReportCampaignProximicMaturity.bid_value'
        db.delete_column(u'report_reportcampaignproximicmaturity', 'bid_value')

        # Deleting field 'ReportCampaignPublisherNetwork.bid'
        db.delete_column(u'report_reportcampaignpublishernetwork', 'bid')

        # Deleting field 'ReportCampaignPublisherNetwork.bid_value'
        db.delete_column(u'report_reportcampaignpublishernetwork', 'bid_value')

        # Deleting field 'ReportCampaignCountry.bid'
        db.delete_column(u'report_reportcampaigncountry', 'bid')

        # Deleting field 'ReportCampaignCountry.bid_value'
        db.delete_column(u'report_reportcampaigncountry', 'bid_value')

        # Deleting field 'ReportStrategyProximicMaturity.bid'
        db.delete_column(u'report_reportstrategyproximicmaturity', 'bid')

        # Deleting field 'ReportStrategyProximicMaturity.bid_value'
        db.delete_column(u'report_reportstrategyproximicmaturity', 'bid_value')

        # Deleting field 'ReportStrategyGender.bid'
        db.delete_column(u'report_reportstrategygender', 'bid')

        # Deleting field 'ReportStrategyGender.bid_value'
        db.delete_column(u'report_reportstrategygender', 'bid_value')

        # Deleting field 'ReportAdvert.bid'
        db.delete_column(u'report_reportadvert', 'bid')

        # Deleting field 'ReportAdvert.bid_value'
        db.delete_column(u'report_reportadvert', 'bid_value')

        # Deleting field 'ReportCampaignPeer39Language.bid'
        db.delete_column(u'report_reportcampaignpeer39language', 'bid')

        # Deleting field 'ReportCampaignPeer39Language.bid_value'
        db.delete_column(u'report_reportcampaignpeer39language', 'bid_value')

        # Deleting field 'ReportStrategyCarrier.bid'
        db.delete_column(u'report_reportstrategycarrier', 'bid')

        # Deleting field 'ReportStrategyCarrier.bid_value'
        db.delete_column(u'report_reportstrategycarrier', 'bid_value')

        # Deleting field 'ReportCampaignOs.bid'
        db.delete_column(u'report_reportcampaignos', 'bid')

        # Deleting field 'ReportCampaignOs.bid_value'
        db.delete_column(u'report_reportcampaignos', 'bid_value')

        # Deleting field 'ReportStrategyPeer39Brand.bid'
        db.delete_column(u'report_reportstrategypeer39brand', 'bid')

        # Deleting field 'ReportStrategyPeer39Brand.bid_value'
        db.delete_column(u'report_reportstrategypeer39brand', 'bid_value')

        # Deleting field 'ReportStrategyProximicSafety.bid'
        db.delete_column(u'report_reportstrategyproximicsafety', 'bid')

        # Deleting field 'ReportStrategyProximicSafety.bid_value'
        db.delete_column(u'report_reportstrategyproximicsafety', 'bid_value')

        # Deleting field 'ReportStrategyPublisher.bid'
        db.delete_column(u'report_reportstrategypublisher', 'bid')

        # Deleting field 'ReportStrategyPublisher.bid_value'
        db.delete_column(u'report_reportstrategypublisher', 'bid_value')

        # Deleting field 'ReportStrategy.bid'
        db.delete_column(u'report_reportstrategy', 'bid')

        # Deleting field 'ReportStrategy.bid_value'
        db.delete_column(u'report_reportstrategy', 'bid_value')

        # Deleting field 'ReportStrategyModel.bid'
        db.delete_column(u'report_reportstrategymodel', 'bid')

        # Deleting field 'ReportStrategyModel.bid_value'
        db.delete_column(u'report_reportstrategymodel', 'bid_value')

        # Deleting field 'ReportCampaignPeer39Contextual.bid'
        db.delete_column(u'report_reportcampaignpeer39contextual', 'bid')

        # Deleting field 'ReportCampaignPeer39Contextual.bid_value'
        db.delete_column(u'report_reportcampaignpeer39contextual', 'bid_value')

        # Deleting field 'ReportStrategyPeer39Quality.bid'
        db.delete_column(u'report_reportstrategypeer39quality', 'bid')

        # Deleting field 'ReportStrategyPeer39Quality.bid_value'
        db.delete_column(u'report_reportstrategypeer39quality', 'bid_value')

        # Deleting field 'ReportStrategyProximicNotice.bid'
        db.delete_column(u'report_reportstrategyproximicnotice', 'bid')

        # Deleting field 'ReportStrategyProximicNotice.bid_value'
        db.delete_column(u'report_reportstrategyproximicnotice', 'bid_value')

        # Deleting field 'ReportCampaignModel.bid'
        db.delete_column(u'report_reportcampaignmodel', 'bid')

        # Deleting field 'ReportCampaignModel.bid_value'
        db.delete_column(u'report_reportcampaignmodel', 'bid_value')

        # Deleting field 'ReportCampaignCity.bid'
        db.delete_column(u'report_reportcampaigncity', 'bid')

        # Deleting field 'ReportCampaignCity.bid_value'
        db.delete_column(u'report_reportcampaigncity', 'bid_value')

        # Deleting field 'ReportCampaignPeer39Quality.bid'
        db.delete_column(u'report_reportcampaignpeer39quality', 'bid')

        # Deleting field 'ReportCampaignPeer39Quality.bid_value'
        db.delete_column(u'report_reportcampaignpeer39quality', 'bid_value')

        # Deleting field 'ReportCampaignRegion.bid'
        db.delete_column(u'report_reportcampaignregion', 'bid')

        # Deleting field 'ReportCampaignRegion.bid_value'
        db.delete_column(u'report_reportcampaignregion', 'bid_value')

        # Deleting field 'ReportStrategyMake.bid'
        db.delete_column(u'report_reportstrategymake', 'bid')

        # Deleting field 'ReportStrategyMake.bid_value'
        db.delete_column(u'report_reportstrategymake', 'bid_value')

        # Deleting field 'ReportStrategyCity.bid'
        db.delete_column(u'report_reportstrategycity', 'bid')

        # Deleting field 'ReportStrategyCity.bid_value'
        db.delete_column(u'report_reportstrategycity', 'bid_value')

        # Deleting field 'ReportStrategyProximicLanguage.bid'
        db.delete_column(u'report_reportstrategyproximiclanguage', 'bid')

        # Deleting field 'ReportStrategyProximicLanguage.bid_value'
        db.delete_column(u'report_reportstrategyproximiclanguage', 'bid_value')

        # Deleting field 'ReportCampaignProximicPlace.bid'
        db.delete_column(u'report_reportcampaignproximicplace', 'bid')

        # Deleting field 'ReportCampaignProximicPlace.bid_value'
        db.delete_column(u'report_reportcampaignproximicplace', 'bid_value')

        # Deleting field 'ReportCampaignProximicLanguage.bid'
        db.delete_column(u'report_reportcampaignproximiclanguage', 'bid')

        # Deleting field 'ReportCampaignProximicLanguage.bid_value'
        db.delete_column(u'report_reportcampaignproximiclanguage', 'bid_value')

        # Deleting field 'ReportCampaignProximicSafety.bid'
        db.delete_column(u'report_reportcampaignproximicsafety', 'bid')

        # Deleting field 'ReportCampaignProximicSafety.bid_value'
        db.delete_column(u'report_reportcampaignproximicsafety', 'bid_value')

        # Deleting field 'ReportStrategyPosition.bid'
        db.delete_column(u'report_reportstrategyposition', 'bid')

        # Deleting field 'ReportStrategyPosition.bid_value'
        db.delete_column(u'report_reportstrategyposition', 'bid_value')

        # Deleting field 'ReportCampaignPeer39Brand.bid'
        db.delete_column(u'report_reportcampaignpeer39brand', 'bid')

        # Deleting field 'ReportCampaignPeer39Brand.bid_value'
        db.delete_column(u'report_reportcampaignpeer39brand', 'bid_value')

        # Deleting field 'ReportCampaignProximicQuality.bid'
        db.delete_column(u'report_reportcampaignproximicquality', 'bid')

        # Deleting field 'ReportCampaignProximicQuality.bid_value'
        db.delete_column(u'report_reportcampaignproximicquality', 'bid_value')

        # Deleting field 'ReportStrategyProximicPlace.bid'
        db.delete_column(u'report_reportstrategyproximicplace', 'bid')

        # Deleting field 'ReportStrategyProximicPlace.bid_value'
        db.delete_column(u'report_reportstrategyproximicplace', 'bid_value')

        # Deleting field 'ReportStrategySite.bid'
        db.delete_column(u'report_reportstrategysite', 'bid')

        # Deleting field 'ReportStrategySite.bid_value'
        db.delete_column(u'report_reportstrategysite', 'bid_value')


    def backwards(self, orm):
        # Adding field 'ReportStrategyAge.bid'
        db.add_column(u'report_reportstrategyage', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyAge.bid_value'
        db.add_column(u'report_reportstrategyage', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPublisherNetwork.bid'
        db.add_column(u'report_reportstrategypublishernetwork', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPublisherNetwork.bid_value'
        db.add_column(u'report_reportstrategypublishernetwork', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Language.bid'
        db.add_column(u'report_reportstrategypeer39language', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Language.bid_value'
        db.add_column(u'report_reportstrategypeer39language', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCategory.bid'
        db.add_column(u'report_reportcampaigncategory', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCategory.bid_value'
        db.add_column(u'report_reportcampaigncategory', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignDomain.bid'
        db.add_column(u'report_reportcampaigndomain', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignDomain.bid_value'
        db.add_column(u'report_reportcampaigndomain', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyDomain.bid'
        db.add_column(u'report_reportstrategydomain', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyDomain.bid_value'
        db.add_column(u'report_reportstrategydomain', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicNotice.bid'
        db.add_column(u'report_reportcampaignproximicnotice', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicNotice.bid_value'
        db.add_column(u'report_reportcampaignproximicnotice', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPosition.bid'
        db.add_column(u'report_reportcampaignposition', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPosition.bid_value'
        db.add_column(u'report_reportcampaignposition', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicContext.bid'
        db.add_column(u'report_reportstrategyproximiccontext', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicContext.bid_value'
        db.add_column(u'report_reportstrategyproximiccontext', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicContextual.bid'
        db.add_column(u'report_reportcampaignproximiccontextual', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicContextual.bid_value'
        db.add_column(u'report_reportcampaignproximiccontextual', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCategory.bid'
        db.add_column(u'report_reportstrategycategory', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCategory.bid_value'
        db.add_column(u'report_reportstrategycategory', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaign.bid'
        db.add_column(u'report_reportcampaign', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaign.bid_value'
        db.add_column(u'report_reportcampaign', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPublisher.bid'
        db.add_column(u'report_reportcampaignpublisher', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPublisher.bid_value'
        db.add_column(u'report_reportcampaignpublisher', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicQuality.bid'
        db.add_column(u'report_reportstrategyproximicquality', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicQuality.bid_value'
        db.add_column(u'report_reportstrategyproximicquality', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCarrier.bid'
        db.add_column(u'report_reportcampaigncarrier', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCarrier.bid_value'
        db.add_column(u'report_reportcampaigncarrier', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyRegion.bid'
        db.add_column(u'report_reportstrategyregion', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyRegion.bid_value'
        db.add_column(u'report_reportstrategyregion', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignAge.bid'
        db.add_column(u'report_reportcampaignage', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignAge.bid_value'
        db.add_column(u'report_reportcampaignage', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignMake.bid'
        db.add_column(u'report_reportcampaignmake', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignMake.bid_value'
        db.add_column(u'report_reportcampaignmake', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCountry.bid'
        db.add_column(u'report_reportstrategycountry', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCountry.bid_value'
        db.add_column(u'report_reportstrategycountry', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignGender.bid'
        db.add_column(u'report_reportcampaigngender', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignGender.bid_value'
        db.add_column(u'report_reportcampaigngender', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyOs.bid'
        db.add_column(u'report_reportstrategyos', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyOs.bid_value'
        db.add_column(u'report_reportstrategyos', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignSite.bid'
        db.add_column(u'report_reportcampaignsite', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignSite.bid_value'
        db.add_column(u'report_reportcampaignsite', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Contextual.bid'
        db.add_column(u'report_reportstrategypeer39contextual', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Contextual.bid_value'
        db.add_column(u'report_reportstrategypeer39contextual', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicMaturity.bid'
        db.add_column(u'report_reportcampaignproximicmaturity', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicMaturity.bid_value'
        db.add_column(u'report_reportcampaignproximicmaturity', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPublisherNetwork.bid'
        db.add_column(u'report_reportcampaignpublishernetwork', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPublisherNetwork.bid_value'
        db.add_column(u'report_reportcampaignpublishernetwork', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCountry.bid'
        db.add_column(u'report_reportcampaigncountry', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCountry.bid_value'
        db.add_column(u'report_reportcampaigncountry', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicMaturity.bid'
        db.add_column(u'report_reportstrategyproximicmaturity', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicMaturity.bid_value'
        db.add_column(u'report_reportstrategyproximicmaturity', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyGender.bid'
        db.add_column(u'report_reportstrategygender', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyGender.bid_value'
        db.add_column(u'report_reportstrategygender', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportAdvert.bid'
        db.add_column(u'report_reportadvert', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportAdvert.bid_value'
        db.add_column(u'report_reportadvert', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Language.bid'
        db.add_column(u'report_reportcampaignpeer39language', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Language.bid_value'
        db.add_column(u'report_reportcampaignpeer39language', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCarrier.bid'
        db.add_column(u'report_reportstrategycarrier', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCarrier.bid_value'
        db.add_column(u'report_reportstrategycarrier', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignOs.bid'
        db.add_column(u'report_reportcampaignos', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignOs.bid_value'
        db.add_column(u'report_reportcampaignos', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Brand.bid'
        db.add_column(u'report_reportstrategypeer39brand', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Brand.bid_value'
        db.add_column(u'report_reportstrategypeer39brand', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicSafety.bid'
        db.add_column(u'report_reportstrategyproximicsafety', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicSafety.bid_value'
        db.add_column(u'report_reportstrategyproximicsafety', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPublisher.bid'
        db.add_column(u'report_reportstrategypublisher', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPublisher.bid_value'
        db.add_column(u'report_reportstrategypublisher', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategy.bid'
        db.add_column(u'report_reportstrategy', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategy.bid_value'
        db.add_column(u'report_reportstrategy', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyModel.bid'
        db.add_column(u'report_reportstrategymodel', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyModel.bid_value'
        db.add_column(u'report_reportstrategymodel', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Contextual.bid'
        db.add_column(u'report_reportcampaignpeer39contextual', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Contextual.bid_value'
        db.add_column(u'report_reportcampaignpeer39contextual', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Quality.bid'
        db.add_column(u'report_reportstrategypeer39quality', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Quality.bid_value'
        db.add_column(u'report_reportstrategypeer39quality', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicNotice.bid'
        db.add_column(u'report_reportstrategyproximicnotice', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicNotice.bid_value'
        db.add_column(u'report_reportstrategyproximicnotice', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignModel.bid'
        db.add_column(u'report_reportcampaignmodel', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignModel.bid_value'
        db.add_column(u'report_reportcampaignmodel', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCity.bid'
        db.add_column(u'report_reportcampaigncity', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCity.bid_value'
        db.add_column(u'report_reportcampaigncity', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Quality.bid'
        db.add_column(u'report_reportcampaignpeer39quality', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Quality.bid_value'
        db.add_column(u'report_reportcampaignpeer39quality', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignRegion.bid'
        db.add_column(u'report_reportcampaignregion', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignRegion.bid_value'
        db.add_column(u'report_reportcampaignregion', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyMake.bid'
        db.add_column(u'report_reportstrategymake', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyMake.bid_value'
        db.add_column(u'report_reportstrategymake', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCity.bid'
        db.add_column(u'report_reportstrategycity', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCity.bid_value'
        db.add_column(u'report_reportstrategycity', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicLanguage.bid'
        db.add_column(u'report_reportstrategyproximiclanguage', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicLanguage.bid_value'
        db.add_column(u'report_reportstrategyproximiclanguage', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicPlace.bid'
        db.add_column(u'report_reportcampaignproximicplace', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicPlace.bid_value'
        db.add_column(u'report_reportcampaignproximicplace', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicLanguage.bid'
        db.add_column(u'report_reportcampaignproximiclanguage', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicLanguage.bid_value'
        db.add_column(u'report_reportcampaignproximiclanguage', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicSafety.bid'
        db.add_column(u'report_reportcampaignproximicsafety', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicSafety.bid_value'
        db.add_column(u'report_reportcampaignproximicsafety', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPosition.bid'
        db.add_column(u'report_reportstrategyposition', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPosition.bid_value'
        db.add_column(u'report_reportstrategyposition', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Brand.bid'
        db.add_column(u'report_reportcampaignpeer39brand', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Brand.bid_value'
        db.add_column(u'report_reportcampaignpeer39brand', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicQuality.bid'
        db.add_column(u'report_reportcampaignproximicquality', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicQuality.bid_value'
        db.add_column(u'report_reportcampaignproximicquality', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicPlace.bid'
        db.add_column(u'report_reportstrategyproximicplace', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicPlace.bid_value'
        db.add_column(u'report_reportstrategyproximicplace', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategySite.bid'
        db.add_column(u'report_reportstrategysite', 'bid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategySite.bid_value'
        db.add_column(u'report_reportstrategysite', 'bid_value',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)


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