# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Renaming field 'ReportStrategyAge.winbid_value'
        db.rename_column(u'report_reportstrategyage', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyAge.winbid'
        db.delete_column(u'report_reportstrategyage', 'winbid')

        # Renaming field 'ReportStrategyPublisherNetwork.winbid_value'
        db.rename_column(u'report_reportstrategypublishernetwork', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyPublisherNetwork.winbid'
        db.delete_column(u'report_reportstrategypublishernetwork', 'winbid')

        # Renaming field 'ReportStrategyPeer39Language.winbid_value'
        db.rename_column(u'report_reportstrategypeer39language', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyPeer39Language.winbid'
        db.delete_column(u'report_reportstrategypeer39language', 'winbid')

        # Renaming field 'ReportCampaignCategory.winbid_value'
        db.rename_column(u'report_reportcampaigncategory', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignCategory.winbid'
        db.delete_column(u'report_reportcampaigncategory', 'winbid')

        # Renaming field 'ReportCampaignDomain.winbid_value'
        db.rename_column(u'report_reportcampaigndomain', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignDomain.winbid'
        db.delete_column(u'report_reportcampaigndomain', 'winbid')

        # Renaming field 'ReportStrategyDomain.winbid_value'
        db.rename_column(u'report_reportstrategydomain', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyDomain.winbid'
        db.delete_column(u'report_reportstrategydomain', 'winbid')

        # Renaming field 'ReportCampaignProximicNotice.winbid_value'
        db.rename_column(u'report_reportcampaignproximicnotice', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignProximicNotice.winbid'
        db.delete_column(u'report_reportcampaignproximicnotice', 'winbid')

        # Renaming field 'ReportCampaignPosition.winbid_value'
        db.rename_column(u'report_reportcampaignposition', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignPosition.winbid'
        db.delete_column(u'report_reportcampaignposition', 'winbid')

        # Renaming field 'ReportStrategyProximicContext.winbid_value'
        db.rename_column(u'report_reportstrategyproximiccontext', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyProximicContext.winbid'
        db.delete_column(u'report_reportstrategyproximiccontext', 'winbid')

        # Renaming field 'ReportCampaignProximicContextual.winbid_value'
        db.rename_column(u'report_reportcampaignproximiccontextual', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignProximicContextual.winbid'
        db.delete_column(u'report_reportcampaignproximiccontextual', 'winbid')

        # Renaming field 'ReportStrategyCategory.winbid_value'
        db.rename_column(u'report_reportstrategycategory', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyCategory.winbid'
        db.delete_column(u'report_reportstrategycategory', 'winbid')

        # Renaming field 'ReportCampaign.winbid_value'
        db.rename_column(u'report_reportcampaign', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaign.winbid'
        db.delete_column(u'report_reportcampaign', 'winbid')

        # Renaming field 'ReportCampaignPublisher.winbid_value'
        db.rename_column(u'report_reportcampaignpublisher', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignPublisher.winbid'
        db.delete_column(u'report_reportcampaignpublisher', 'winbid')

        # Renaming field 'ReportStrategyProximicQuality.winbid_value'
        db.rename_column(u'report_reportstrategyproximicquality', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyProximicQuality.winbid'
        db.delete_column(u'report_reportstrategyproximicquality', 'winbid')

        # Renaming field 'ReportCampaignCarrier.winbid_value'
        db.rename_column(u'report_reportcampaigncarrier', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignCarrier.winbid'
        db.delete_column(u'report_reportcampaigncarrier', 'winbid')

        # Renaming field 'ReportStrategyRegion.winbid_value'
        db.rename_column(u'report_reportstrategyregion', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyRegion.winbid'
        db.delete_column(u'report_reportstrategyregion', 'winbid')

        # Renaming field 'ReportCampaignAge.winbid_value'
        db.rename_column(u'report_reportcampaignage', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignAge.winbid'
        db.delete_column(u'report_reportcampaignage', 'winbid')

        # Renaming field 'ReportCampaignMake.winbid_value'
        db.rename_column(u'report_reportcampaignmake', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignMake.winbid'
        db.delete_column(u'report_reportcampaignmake', 'winbid')

        # Renaming field 'ReportStrategyCountry.winbid_value'
        db.rename_column(u'report_reportstrategycountry', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyCountry.winbid'
        db.delete_column(u'report_reportstrategycountry', 'winbid')

        # Renaming field 'ReportCampaignGender.winbid_value'
        db.rename_column(u'report_reportcampaigngender', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignGender.winbid'
        db.delete_column(u'report_reportcampaigngender', 'winbid')

        # Renaming field 'ReportStrategyOs.winbid_value'
        db.rename_column(u'report_reportstrategyos', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyOs.winbid'
        db.delete_column(u'report_reportstrategyos', 'winbid')

        # Renaming field 'ReportCampaignSite.winbid_value'
        db.rename_column(u'report_reportcampaignsite', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignSite.winbid'
        db.delete_column(u'report_reportcampaignsite', 'winbid')

        # Renaming field 'ReportStrategyPeer39Contextual.winbid_value'
        db.rename_column(u'report_reportstrategypeer39contextual', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyPeer39Contextual.winbid'
        db.delete_column(u'report_reportstrategypeer39contextual', 'winbid')

        # Renaming field 'ReportCampaignProximicMaturity.winbid_value'
        db.rename_column(u'report_reportcampaignproximicmaturity', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignProximicMaturity.winbid'
        db.delete_column(u'report_reportcampaignproximicmaturity', 'winbid')

        # Renaming field 'ReportCampaignPublisherNetwork.winbid_value'
        db.rename_column(u'report_reportcampaignpublishernetwork', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignPublisherNetwork.winbid'
        db.delete_column(u'report_reportcampaignpublishernetwork', 'winbid')

        # Renaming field 'ReportCampaignCountry.winbid_value'
        db.rename_column(u'report_reportcampaigncountry', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignCountry.winbid'
        db.delete_column(u'report_reportcampaigncountry', 'winbid')

        # Renaming field 'ReportStrategyProximicMaturity.winbid_value'
        db.rename_column(u'report_reportstrategyproximicmaturity', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyProximicMaturity.winbid'
        db.delete_column(u'report_reportstrategyproximicmaturity', 'winbid')

        # Renaming field 'ReportStrategyGender.winbid_value'
        db.rename_column(u'report_reportstrategygender', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyGender.winbid'
        db.delete_column(u'report_reportstrategygender', 'winbid')

        # Renaming field 'ReportAdvert.winbid_value'
        db.rename_column(u'report_reportadvert', 'winbid_value', 'imp_value')

        # Deleting field 'ReportAdvert.winbid'
        db.delete_column(u'report_reportadvert', 'winbid')

        # Renaming field 'ReportCampaignPeer39Language.winbid_value'
        db.rename_column(u'report_reportcampaignpeer39language', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignPeer39Language.winbid'
        db.delete_column(u'report_reportcampaignpeer39language', 'winbid')

        # Renaming field 'ReportStrategyCarrier.winbid_value'
        db.rename_column(u'report_reportstrategycarrier', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyCarrier.winbid'
        db.delete_column(u'report_reportstrategycarrier', 'winbid')

        # Renaming field 'ReportCampaignOs.winbid_value'
        db.rename_column(u'report_reportcampaignos', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignOs.winbid'
        db.delete_column(u'report_reportcampaignos', 'winbid')

        # Renaming field 'ReportStrategyPeer39Brand.winbid_value'
        db.rename_column(u'report_reportstrategypeer39brand', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyPeer39Brand.winbid'
        db.delete_column(u'report_reportstrategypeer39brand', 'winbid')

        # Renaming field 'ReportStrategyProximicSafety.winbid_value'
        db.rename_column(u'report_reportstrategyproximicsafety', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyProximicSafety.winbid'
        db.delete_column(u'report_reportstrategyproximicsafety', 'winbid')

        # Renaming field 'ReportStrategyPublisher.winbid_value'
        db.rename_column(u'report_reportstrategypublisher', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyPublisher.winbid'
        db.delete_column(u'report_reportstrategypublisher', 'winbid')

        # Renaming field 'ReportStrategy.winbid_value'
        db.rename_column(u'report_reportstrategy', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategy.winbid'
        db.delete_column(u'report_reportstrategy', 'winbid')

        # Renaming field 'ReportStrategyModel.winbid_value'
        db.rename_column(u'report_reportstrategymodel', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyModel.winbid'
        db.delete_column(u'report_reportstrategymodel', 'winbid')

        # Renaming field 'ReportCampaignPeer39Contextual.winbid_value'
        db.rename_column(u'report_reportcampaignpeer39contextual', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignPeer39Contextual.winbid'
        db.delete_column(u'report_reportcampaignpeer39contextual', 'winbid')

        # Renaming field 'ReportStrategyPeer39Quality.winbid_value'
        db.rename_column(u'report_reportstrategypeer39quality', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyPeer39Quality.winbid'
        db.delete_column(u'report_reportstrategypeer39quality', 'winbid')

        # Renaming field 'ReportStrategyProximicNotice.winbid_value'
        db.rename_column(u'report_reportstrategyproximicnotice', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyProximicNotice.winbid'
        db.delete_column(u'report_reportstrategyproximicnotice', 'winbid')

        # Renaming field 'ReportCampaignModel.winbid_value'
        db.rename_column(u'report_reportcampaignmodel', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignModel.winbid'
        db.delete_column(u'report_reportcampaignmodel', 'winbid')

        # Renaming field 'ReportCampaignCity.winbid_value'
        db.rename_column(u'report_reportcampaigncity', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignCity.winbid'
        db.delete_column(u'report_reportcampaigncity', 'winbid')

        # Renaming field 'ReportCampaignPeer39Quality.winbid_value'
        db.rename_column(u'report_reportcampaignpeer39quality', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignPeer39Quality.winbid'
        db.delete_column(u'report_reportcampaignpeer39quality', 'winbid')

        # Renaming field 'ReportCampaignRegion.winbid_value'
        db.rename_column(u'report_reportcampaignregion', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignRegion.winbid'
        db.delete_column(u'report_reportcampaignregion', 'winbid')

        # Renaming field 'ReportStrategyMake.winbid_value'
        db.rename_column(u'report_reportstrategymake', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyMake.winbid'
        db.delete_column(u'report_reportstrategymake', 'winbid')

        # Renaming field 'ReportStrategyCity.winbid_value'
        db.rename_column(u'report_reportstrategycity', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyCity.winbid'
        db.delete_column(u'report_reportstrategycity', 'winbid')

        # Renaming field 'ReportStrategyProximicLanguage.winbid_value'
        db.rename_column(u'report_reportstrategyproximiclanguage', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyProximicLanguage.winbid'
        db.delete_column(u'report_reportstrategyproximiclanguage', 'winbid')

        # Renaming field 'ReportCampaignProximicPlace.winbid_value'
        db.rename_column(u'report_reportcampaignproximicplace', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignProximicPlace.winbid'
        db.delete_column(u'report_reportcampaignproximicplace', 'winbid')

        # Renaming field 'ReportCampaignProximicLanguage.winbid_value'
        db.rename_column(u'report_reportcampaignproximiclanguage', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignProximicLanguage.winbid'
        db.delete_column(u'report_reportcampaignproximiclanguage', 'winbid')

        # Renaming field 'ReportCampaignProximicSafety.winbid_value'
        db.rename_column(u'report_reportcampaignproximicsafety', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignProximicSafety.winbid'
        db.delete_column(u'report_reportcampaignproximicsafety', 'winbid')

        # Renaming field 'ReportStrategyPosition.winbid_value'
        db.rename_column(u'report_reportstrategyposition', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyPosition.winbid'
        db.delete_column(u'report_reportstrategyposition', 'winbid')

        # Renaming field 'ReportCampaignPeer39Brand.winbid_value'
        db.rename_column(u'report_reportcampaignpeer39brand', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignPeer39Brand.winbid'
        db.delete_column(u'report_reportcampaignpeer39brand', 'winbid')

        # Renaming field 'ReportCampaignProximicQuality.winbid_value'
        db.rename_column(u'report_reportcampaignproximicquality', 'winbid_value', 'imp_value')

        # Deleting field 'ReportCampaignProximicQuality.winbid'
        db.delete_column(u'report_reportcampaignproximicquality', 'winbid')

        # Renaming field 'ReportStrategyProximicPlace.winbid_value'
        db.rename_column(u'report_reportstrategyproximicplace', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategyProximicPlace.winbid'
        db.delete_column(u'report_reportstrategyproximicplace', 'winbid')

        # Renaming field 'ReportStrategySite.winbid_value'
        db.rename_column(u'report_reportstrategysite', 'winbid_value', 'imp_value')

        # Deleting field 'ReportStrategySite.winbid'
        db.delete_column(u'report_reportstrategysite', 'winbid')


    def backwards(self, orm):
        # Adding field 'ReportStrategyAge.winbid'
        db.add_column(u'report_reportstrategyage', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyAge.imp_value'
        db.rename_column(u'report_reportstrategyage', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyPublisherNetwork.winbid'
        db.add_column(u'report_reportstrategypublishernetwork', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyPublisherNetwork.imp_value'
        db.rename_column(u'report_reportstrategypublishernetwork', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyPeer39Language.winbid'
        db.add_column(u'report_reportstrategypeer39language', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyPeer39Language.imp_value'
        db.rename_column(u'report_reportstrategypeer39language', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignCategory.winbid'
        db.add_column(u'report_reportcampaigncategory', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignCategory.imp_value'
        db.rename_column(u'report_reportcampaigncategory', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignDomain.winbid'
        db.add_column(u'report_reportcampaigndomain', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignDomain.imp_value'
        db.rename_column(u'report_reportcampaigndomain', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyDomain.winbid'
        db.add_column(u'report_reportstrategydomain', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyDomain.imp_value'
        db.rename_column(u'report_reportstrategydomain', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignProximicNotice.winbid'
        db.add_column(u'report_reportcampaignproximicnotice', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignProximicNotice.imp_value'
        db.rename_column(u'report_reportcampaignproximicnotice', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignPosition.winbid'
        db.add_column(u'report_reportcampaignposition', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignPosition.imp_value'
        db.rename_column(u'report_reportcampaignposition', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyProximicContext.winbid'
        db.add_column(u'report_reportstrategyproximiccontext', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyProximicContext.imp_value'
        db.rename_column(u'report_reportstrategyproximiccontext', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignProximicContextual.winbid'
        db.add_column(u'report_reportcampaignproximiccontextual', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignProximicContextual.imp_value'
        db.rename_column(u'report_reportcampaignproximiccontextual', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyCategory.winbid'
        db.add_column(u'report_reportstrategycategory', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyCategory.imp_value'
        db.rename_column(u'report_reportstrategycategory', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaign.winbid'
        db.add_column(u'report_reportcampaign', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaign.imp_value'
        db.rename_column(u'report_reportcampaign', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignPublisher.winbid'
        db.add_column(u'report_reportcampaignpublisher', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignPublisher.imp_value'
        db.rename_column(u'report_reportcampaignpublisher', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyProximicQuality.winbid'
        db.add_column(u'report_reportstrategyproximicquality', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyProximicQuality.imp_value'
        db.rename_column(u'report_reportstrategyproximicquality', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignCarrier.winbid'
        db.add_column(u'report_reportcampaigncarrier', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignCarrier.imp_value'
        db.rename_column(u'report_reportcampaigncarrier', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyRegion.winbid'
        db.add_column(u'report_reportstrategyregion', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyRegion.imp_value'
        db.rename_column(u'report_reportstrategyregion', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignAge.winbid'
        db.add_column(u'report_reportcampaignage', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignAge.imp_value'
        db.rename_column(u'report_reportcampaignage', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignMake.winbid'
        db.add_column(u'report_reportcampaignmake', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignMake.imp_value'
        db.rename_column(u'report_reportcampaignmake', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyCountry.winbid'
        db.add_column(u'report_reportstrategycountry', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyCountry.imp_value'
        db.rename_column(u'report_reportstrategycountry', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignGender.winbid'
        db.add_column(u'report_reportcampaigngender', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignGender.imp_value'
        db.rename_column(u'report_reportcampaigngender', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyOs.winbid'
        db.add_column(u'report_reportstrategyos', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyOs.imp_value'
        db.rename_column(u'report_reportstrategyos', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignSite.winbid'
        db.add_column(u'report_reportcampaignsite', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignSite.imp_value'
        db.rename_column(u'report_reportcampaignsite', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyPeer39Contextual.winbid'
        db.add_column(u'report_reportstrategypeer39contextual', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyPeer39Contextual.imp_value'
        db.rename_column(u'report_reportstrategypeer39contextual', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignProximicMaturity.winbid'
        db.add_column(u'report_reportcampaignproximicmaturity', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignProximicMaturity.imp_value'
        db.rename_column(u'report_reportcampaignproximicmaturity', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignPublisherNetwork.winbid'
        db.add_column(u'report_reportcampaignpublishernetwork', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignPublisherNetwork.imp_value'
        db.rename_column(u'report_reportcampaignpublishernetwork', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignCountry.winbid'
        db.add_column(u'report_reportcampaigncountry', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignCountry.imp_value'
        db.rename_column(u'report_reportcampaigncountry', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyProximicMaturity.winbid'
        db.add_column(u'report_reportstrategyproximicmaturity', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyProximicMaturity.imp_value'
        db.rename_column(u'report_reportstrategyproximicmaturity', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyGender.winbid'
        db.add_column(u'report_reportstrategygender', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyGender.imp_value'
        db.rename_column(u'report_reportstrategygender', 'imp_value', 'winbid_value')

        # Adding field 'ReportAdvert.winbid'
        db.add_column(u'report_reportadvert', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportAdvert.imp_value'
        db.rename_column(u'report_reportadvert', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignPeer39Language.winbid'
        db.add_column(u'report_reportcampaignpeer39language', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignPeer39Language.imp_value'
        db.rename_column(u'report_reportcampaignpeer39language', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyCarrier.winbid'
        db.add_column(u'report_reportstrategycarrier', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyCarrier.imp_value'
        db.rename_column(u'report_reportstrategycarrier', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignOs.winbid'
        db.add_column(u'report_reportcampaignos', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignOs.imp_value'
        db.rename_column(u'report_reportcampaignos', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyPeer39Brand.winbid'
        db.add_column(u'report_reportstrategypeer39brand', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyPeer39Brand.imp_value'
        db.rename_column(u'report_reportstrategypeer39brand', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyProximicSafety.winbid'
        db.add_column(u'report_reportstrategyproximicsafety', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyProximicSafety.imp_value'
        db.rename_column(u'report_reportstrategyproximicsafety', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyPublisher.winbid'
        db.add_column(u'report_reportstrategypublisher', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyPublisher.imp_value'
        db.rename_column(u'report_reportstrategypublisher', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategy.winbid'
        db.add_column(u'report_reportstrategy', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategy.imp_value'
        db.rename_column(u'report_reportstrategy', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyModel.winbid'
        db.add_column(u'report_reportstrategymodel', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyModel.imp_value'
        db.rename_column(u'report_reportstrategymodel', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignPeer39Contextual.winbid'
        db.add_column(u'report_reportcampaignpeer39contextual', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignPeer39Contextual.imp_value'
        db.rename_column(u'report_reportcampaignpeer39contextual', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyPeer39Quality.winbid'
        db.add_column(u'report_reportstrategypeer39quality', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyPeer39Quality.imp_value'
        db.rename_column(u'report_reportstrategypeer39quality', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyProximicNotice.winbid'
        db.add_column(u'report_reportstrategyproximicnotice', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyProximicNotice.imp_value'
        db.rename_column(u'report_reportstrategyproximicnotice', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignModel.winbid'
        db.add_column(u'report_reportcampaignmodel', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignModel.imp_value'
        db.rename_column(u'report_reportcampaignmodel', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignCity.winbid'
        db.add_column(u'report_reportcampaigncity', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignCity.imp_value'
        db.rename_column(u'report_reportcampaigncity', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignPeer39Quality.winbid'
        db.add_column(u'report_reportcampaignpeer39quality', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignPeer39Quality.imp_value'
        db.rename_column(u'report_reportcampaignpeer39quality', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignRegion.winbid'
        db.add_column(u'report_reportcampaignregion', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignRegion.imp_value'
        db.rename_column(u'report_reportcampaignregion', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyMake.winbid'
        db.add_column(u'report_reportstrategymake', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyMake.imp_value'
        db.rename_column(u'report_reportstrategymake', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyCity.winbid'
        db.add_column(u'report_reportstrategycity', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyCity.imp_value'
        db.rename_column(u'report_reportstrategycity', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyProximicLanguage.winbid'
        db.add_column(u'report_reportstrategyproximiclanguage', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyProximicLanguage.imp_value'
        db.rename_column(u'report_reportstrategyproximiclanguage', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignProximicPlace.winbid'
        db.add_column(u'report_reportcampaignproximicplace', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignProximicPlace.imp_value'
        db.rename_column(u'report_reportcampaignproximicplace', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignProximicLanguage.winbid'
        db.add_column(u'report_reportcampaignproximiclanguage', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignProximicLanguage.imp_value'
        db.rename_column(u'report_reportcampaignproximiclanguage', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignProximicSafety.winbid'
        db.add_column(u'report_reportcampaignproximicsafety', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignProximicSafety.imp_value'
        db.rename_column(u'report_reportcampaignproximicsafety', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyPosition.winbid'
        db.add_column(u'report_reportstrategyposition', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyPosition.imp_value'
        db.rename_column(u'report_reportstrategyposition', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignPeer39Brand.winbid'
        db.add_column(u'report_reportcampaignpeer39brand', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignPeer39Brand.imp_value'
        db.rename_column(u'report_reportcampaignpeer39brand', 'imp_value', 'winbid_value')

        # Adding field 'ReportCampaignProximicQuality.winbid'
        db.add_column(u'report_reportcampaignproximicquality', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportCampaignProximicQuality.imp_value'
        db.rename_column(u'report_reportcampaignproximicquality', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategyProximicPlace.winbid'
        db.add_column(u'report_reportstrategyproximicplace', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategyProximicPlace.imp_value'
        db.rename_column(u'report_reportstrategyproximicplace', 'imp_value', 'winbid_value')

        # Adding field 'ReportStrategySite.winbid'
        db.add_column(u'report_reportstrategysite', 'winbid',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Renaming field 'ReportStrategySite.imp_value'
        db.rename_column(u'report_reportstrategysite', 'imp_value', 'winbid_value')


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
