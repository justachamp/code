# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ReportStrategyAge.bids_lost'
        db.delete_column(u'report_reportstrategyage', 'bids_lost')

        # Deleting field 'ReportStrategyAge.winbid_value_total'
        db.delete_column(u'report_reportstrategyage', 'winbid_value_total')

        # Deleting field 'ReportStrategyAge.net_earned'
        db.delete_column(u'report_reportstrategyage', 'net_earned')

        # Deleting field 'ReportStrategyPublisherNetwork.bids_lost'
        db.delete_column(u'report_reportstrategypublishernetwork', 'bids_lost')

        # Deleting field 'ReportStrategyPublisherNetwork.winbid_value_total'
        db.delete_column(u'report_reportstrategypublishernetwork', 'winbid_value_total')

        # Deleting field 'ReportStrategyPublisherNetwork.net_earned'
        db.delete_column(u'report_reportstrategypublishernetwork', 'net_earned')

        # Deleting field 'ReportStrategyPeer39Language.bids_lost'
        db.delete_column(u'report_reportstrategypeer39language', 'bids_lost')

        # Deleting field 'ReportStrategyPeer39Language.winbid_value_total'
        db.delete_column(u'report_reportstrategypeer39language', 'winbid_value_total')

        # Deleting field 'ReportStrategyPeer39Language.net_earned'
        db.delete_column(u'report_reportstrategypeer39language', 'net_earned')

        # Deleting field 'ReportCampaignCategory.bids_lost'
        db.delete_column(u'report_reportcampaigncategory', 'bids_lost')

        # Deleting field 'ReportCampaignCategory.winbid_value_total'
        db.delete_column(u'report_reportcampaigncategory', 'winbid_value_total')

        # Deleting field 'ReportCampaignCategory.net_earned'
        db.delete_column(u'report_reportcampaigncategory', 'net_earned')

        # Deleting field 'ReportCampaignDomain.bids_lost'
        db.delete_column(u'report_reportcampaigndomain', 'bids_lost')

        # Deleting field 'ReportCampaignDomain.winbid_value_total'
        db.delete_column(u'report_reportcampaigndomain', 'winbid_value_total')

        # Deleting field 'ReportCampaignDomain.net_earned'
        db.delete_column(u'report_reportcampaigndomain', 'net_earned')

        # Deleting field 'ReportStrategyDomain.bids_lost'
        db.delete_column(u'report_reportstrategydomain', 'bids_lost')

        # Deleting field 'ReportStrategyDomain.winbid_value_total'
        db.delete_column(u'report_reportstrategydomain', 'winbid_value_total')

        # Deleting field 'ReportStrategyDomain.net_earned'
        db.delete_column(u'report_reportstrategydomain', 'net_earned')

        # Deleting field 'ReportCampaignProximicNotice.bids_lost'
        db.delete_column(u'report_reportcampaignproximicnotice', 'bids_lost')

        # Deleting field 'ReportCampaignProximicNotice.winbid_value_total'
        db.delete_column(u'report_reportcampaignproximicnotice', 'winbid_value_total')

        # Deleting field 'ReportCampaignProximicNotice.net_earned'
        db.delete_column(u'report_reportcampaignproximicnotice', 'net_earned')

        # Deleting field 'ReportCampaignPosition.bids_lost'
        db.delete_column(u'report_reportcampaignposition', 'bids_lost')

        # Deleting field 'ReportCampaignPosition.winbid_value_total'
        db.delete_column(u'report_reportcampaignposition', 'winbid_value_total')

        # Deleting field 'ReportCampaignPosition.net_earned'
        db.delete_column(u'report_reportcampaignposition', 'net_earned')

        # Deleting field 'ReportStrategyProximicContext.bids_lost'
        db.delete_column(u'report_reportstrategyproximiccontext', 'bids_lost')

        # Deleting field 'ReportStrategyProximicContext.winbid_value_total'
        db.delete_column(u'report_reportstrategyproximiccontext', 'winbid_value_total')

        # Deleting field 'ReportStrategyProximicContext.net_earned'
        db.delete_column(u'report_reportstrategyproximiccontext', 'net_earned')

        # Deleting field 'ReportCampaignProximicContextual.bids_lost'
        db.delete_column(u'report_reportcampaignproximiccontextual', 'bids_lost')

        # Deleting field 'ReportCampaignProximicContextual.winbid_value_total'
        db.delete_column(u'report_reportcampaignproximiccontextual', 'winbid_value_total')

        # Deleting field 'ReportCampaignProximicContextual.net_earned'
        db.delete_column(u'report_reportcampaignproximiccontextual', 'net_earned')

        # Deleting field 'ReportStrategyCategory.bids_lost'
        db.delete_column(u'report_reportstrategycategory', 'bids_lost')

        # Deleting field 'ReportStrategyCategory.winbid_value_total'
        db.delete_column(u'report_reportstrategycategory', 'winbid_value_total')

        # Deleting field 'ReportStrategyCategory.net_earned'
        db.delete_column(u'report_reportstrategycategory', 'net_earned')

        # Deleting field 'ReportCampaign.bids_lost'
        db.delete_column(u'report_reportcampaign', 'bids_lost')

        # Deleting field 'ReportCampaign.winbid_value_total'
        db.delete_column(u'report_reportcampaign', 'winbid_value_total')

        # Deleting field 'ReportCampaign.net_earned'
        db.delete_column(u'report_reportcampaign', 'net_earned')

        # Deleting field 'ReportCampaignPublisher.bids_lost'
        db.delete_column(u'report_reportcampaignpublisher', 'bids_lost')

        # Deleting field 'ReportCampaignPublisher.winbid_value_total'
        db.delete_column(u'report_reportcampaignpublisher', 'winbid_value_total')

        # Deleting field 'ReportCampaignPublisher.net_earned'
        db.delete_column(u'report_reportcampaignpublisher', 'net_earned')

        # Deleting field 'ReportStrategyProximicQuality.bids_lost'
        db.delete_column(u'report_reportstrategyproximicquality', 'bids_lost')

        # Deleting field 'ReportStrategyProximicQuality.winbid_value_total'
        db.delete_column(u'report_reportstrategyproximicquality', 'winbid_value_total')

        # Deleting field 'ReportStrategyProximicQuality.net_earned'
        db.delete_column(u'report_reportstrategyproximicquality', 'net_earned')

        # Deleting field 'ReportCampaignCarrier.bids_lost'
        db.delete_column(u'report_reportcampaigncarrier', 'bids_lost')

        # Deleting field 'ReportCampaignCarrier.winbid_value_total'
        db.delete_column(u'report_reportcampaigncarrier', 'winbid_value_total')

        # Deleting field 'ReportCampaignCarrier.net_earned'
        db.delete_column(u'report_reportcampaigncarrier', 'net_earned')

        # Deleting field 'ReportStrategyRegion.bids_lost'
        db.delete_column(u'report_reportstrategyregion', 'bids_lost')

        # Deleting field 'ReportStrategyRegion.winbid_value_total'
        db.delete_column(u'report_reportstrategyregion', 'winbid_value_total')

        # Deleting field 'ReportStrategyRegion.net_earned'
        db.delete_column(u'report_reportstrategyregion', 'net_earned')

        # Deleting field 'ReportCampaignAge.bids_lost'
        db.delete_column(u'report_reportcampaignage', 'bids_lost')

        # Deleting field 'ReportCampaignAge.winbid_value_total'
        db.delete_column(u'report_reportcampaignage', 'winbid_value_total')

        # Deleting field 'ReportCampaignAge.net_earned'
        db.delete_column(u'report_reportcampaignage', 'net_earned')

        # Deleting field 'ReportCampaignMake.bids_lost'
        db.delete_column(u'report_reportcampaignmake', 'bids_lost')

        # Deleting field 'ReportCampaignMake.winbid_value_total'
        db.delete_column(u'report_reportcampaignmake', 'winbid_value_total')

        # Deleting field 'ReportCampaignMake.net_earned'
        db.delete_column(u'report_reportcampaignmake', 'net_earned')

        # Deleting field 'ReportStrategyCountry.bids_lost'
        db.delete_column(u'report_reportstrategycountry', 'bids_lost')

        # Deleting field 'ReportStrategyCountry.winbid_value_total'
        db.delete_column(u'report_reportstrategycountry', 'winbid_value_total')

        # Deleting field 'ReportStrategyCountry.net_earned'
        db.delete_column(u'report_reportstrategycountry', 'net_earned')

        # Deleting field 'ReportCampaignGender.bids_lost'
        db.delete_column(u'report_reportcampaigngender', 'bids_lost')

        # Deleting field 'ReportCampaignGender.winbid_value_total'
        db.delete_column(u'report_reportcampaigngender', 'winbid_value_total')

        # Deleting field 'ReportCampaignGender.net_earned'
        db.delete_column(u'report_reportcampaigngender', 'net_earned')

        # Deleting field 'ReportStrategyOs.bids_lost'
        db.delete_column(u'report_reportstrategyos', 'bids_lost')

        # Deleting field 'ReportStrategyOs.winbid_value_total'
        db.delete_column(u'report_reportstrategyos', 'winbid_value_total')

        # Deleting field 'ReportStrategyOs.net_earned'
        db.delete_column(u'report_reportstrategyos', 'net_earned')

        # Deleting field 'ReportCampaignSite.bids_lost'
        db.delete_column(u'report_reportcampaignsite', 'bids_lost')

        # Deleting field 'ReportCampaignSite.winbid_value_total'
        db.delete_column(u'report_reportcampaignsite', 'winbid_value_total')

        # Deleting field 'ReportCampaignSite.net_earned'
        db.delete_column(u'report_reportcampaignsite', 'net_earned')

        # Deleting field 'ReportStrategyPeer39Contextual.bids_lost'
        db.delete_column(u'report_reportstrategypeer39contextual', 'bids_lost')

        # Deleting field 'ReportStrategyPeer39Contextual.winbid_value_total'
        db.delete_column(u'report_reportstrategypeer39contextual', 'winbid_value_total')

        # Deleting field 'ReportStrategyPeer39Contextual.net_earned'
        db.delete_column(u'report_reportstrategypeer39contextual', 'net_earned')

        # Deleting field 'ReportCampaignProximicMaturity.bids_lost'
        db.delete_column(u'report_reportcampaignproximicmaturity', 'bids_lost')

        # Deleting field 'ReportCampaignProximicMaturity.winbid_value_total'
        db.delete_column(u'report_reportcampaignproximicmaturity', 'winbid_value_total')

        # Deleting field 'ReportCampaignProximicMaturity.net_earned'
        db.delete_column(u'report_reportcampaignproximicmaturity', 'net_earned')

        # Deleting field 'ReportCampaignPublisherNetwork.bids_lost'
        db.delete_column(u'report_reportcampaignpublishernetwork', 'bids_lost')

        # Deleting field 'ReportCampaignPublisherNetwork.winbid_value_total'
        db.delete_column(u'report_reportcampaignpublishernetwork', 'winbid_value_total')

        # Deleting field 'ReportCampaignPublisherNetwork.net_earned'
        db.delete_column(u'report_reportcampaignpublishernetwork', 'net_earned')

        # Deleting field 'ReportCampaignCountry.bids_lost'
        db.delete_column(u'report_reportcampaigncountry', 'bids_lost')

        # Deleting field 'ReportCampaignCountry.winbid_value_total'
        db.delete_column(u'report_reportcampaigncountry', 'winbid_value_total')

        # Deleting field 'ReportCampaignCountry.net_earned'
        db.delete_column(u'report_reportcampaigncountry', 'net_earned')

        # Deleting field 'ReportStrategyProximicMaturity.bids_lost'
        db.delete_column(u'report_reportstrategyproximicmaturity', 'bids_lost')

        # Deleting field 'ReportStrategyProximicMaturity.winbid_value_total'
        db.delete_column(u'report_reportstrategyproximicmaturity', 'winbid_value_total')

        # Deleting field 'ReportStrategyProximicMaturity.net_earned'
        db.delete_column(u'report_reportstrategyproximicmaturity', 'net_earned')

        # Deleting field 'ReportStrategyGender.bids_lost'
        db.delete_column(u'report_reportstrategygender', 'bids_lost')

        # Deleting field 'ReportStrategyGender.winbid_value_total'
        db.delete_column(u'report_reportstrategygender', 'winbid_value_total')

        # Deleting field 'ReportStrategyGender.net_earned'
        db.delete_column(u'report_reportstrategygender', 'net_earned')

        # Deleting field 'ReportAdvert.bids_lost'
        db.delete_column(u'report_reportadvert', 'bids_lost')

        # Deleting field 'ReportAdvert.winbid_value_total'
        db.delete_column(u'report_reportadvert', 'winbid_value_total')

        # Deleting field 'ReportAdvert.net_earned'
        db.delete_column(u'report_reportadvert', 'net_earned')

        # Deleting field 'ReportCampaignPeer39Language.bids_lost'
        db.delete_column(u'report_reportcampaignpeer39language', 'bids_lost')

        # Deleting field 'ReportCampaignPeer39Language.winbid_value_total'
        db.delete_column(u'report_reportcampaignpeer39language', 'winbid_value_total')

        # Deleting field 'ReportCampaignPeer39Language.net_earned'
        db.delete_column(u'report_reportcampaignpeer39language', 'net_earned')

        # Deleting field 'ReportStrategyCarrier.bids_lost'
        db.delete_column(u'report_reportstrategycarrier', 'bids_lost')

        # Deleting field 'ReportStrategyCarrier.winbid_value_total'
        db.delete_column(u'report_reportstrategycarrier', 'winbid_value_total')

        # Deleting field 'ReportStrategyCarrier.net_earned'
        db.delete_column(u'report_reportstrategycarrier', 'net_earned')

        # Deleting field 'ReportCampaignOs.bids_lost'
        db.delete_column(u'report_reportcampaignos', 'bids_lost')

        # Deleting field 'ReportCampaignOs.winbid_value_total'
        db.delete_column(u'report_reportcampaignos', 'winbid_value_total')

        # Deleting field 'ReportCampaignOs.net_earned'
        db.delete_column(u'report_reportcampaignos', 'net_earned')

        # Deleting field 'ReportStrategyPeer39Brand.bids_lost'
        db.delete_column(u'report_reportstrategypeer39brand', 'bids_lost')

        # Deleting field 'ReportStrategyPeer39Brand.winbid_value_total'
        db.delete_column(u'report_reportstrategypeer39brand', 'winbid_value_total')

        # Deleting field 'ReportStrategyPeer39Brand.net_earned'
        db.delete_column(u'report_reportstrategypeer39brand', 'net_earned')

        # Deleting field 'ReportStrategyProximicSafety.bids_lost'
        db.delete_column(u'report_reportstrategyproximicsafety', 'bids_lost')

        # Deleting field 'ReportStrategyProximicSafety.winbid_value_total'
        db.delete_column(u'report_reportstrategyproximicsafety', 'winbid_value_total')

        # Deleting field 'ReportStrategyProximicSafety.net_earned'
        db.delete_column(u'report_reportstrategyproximicsafety', 'net_earned')

        # Deleting field 'ReportStrategyPublisher.bids_lost'
        db.delete_column(u'report_reportstrategypublisher', 'bids_lost')

        # Deleting field 'ReportStrategyPublisher.winbid_value_total'
        db.delete_column(u'report_reportstrategypublisher', 'winbid_value_total')

        # Deleting field 'ReportStrategyPublisher.net_earned'
        db.delete_column(u'report_reportstrategypublisher', 'net_earned')

        # Deleting field 'ReportStrategy.bids_lost'
        db.delete_column(u'report_reportstrategy', 'bids_lost')

        # Deleting field 'ReportStrategy.winbid_value_total'
        db.delete_column(u'report_reportstrategy', 'winbid_value_total')

        # Deleting field 'ReportStrategy.net_earned'
        db.delete_column(u'report_reportstrategy', 'net_earned')

        # Deleting field 'ReportStrategyModel.bids_lost'
        db.delete_column(u'report_reportstrategymodel', 'bids_lost')

        # Deleting field 'ReportStrategyModel.winbid_value_total'
        db.delete_column(u'report_reportstrategymodel', 'winbid_value_total')

        # Deleting field 'ReportStrategyModel.net_earned'
        db.delete_column(u'report_reportstrategymodel', 'net_earned')

        # Deleting field 'ReportCampaignPeer39Contextual.bids_lost'
        db.delete_column(u'report_reportcampaignpeer39contextual', 'bids_lost')

        # Deleting field 'ReportCampaignPeer39Contextual.winbid_value_total'
        db.delete_column(u'report_reportcampaignpeer39contextual', 'winbid_value_total')

        # Deleting field 'ReportCampaignPeer39Contextual.net_earned'
        db.delete_column(u'report_reportcampaignpeer39contextual', 'net_earned')

        # Deleting field 'ReportStrategyPeer39Quality.bids_lost'
        db.delete_column(u'report_reportstrategypeer39quality', 'bids_lost')

        # Deleting field 'ReportStrategyPeer39Quality.winbid_value_total'
        db.delete_column(u'report_reportstrategypeer39quality', 'winbid_value_total')

        # Deleting field 'ReportStrategyPeer39Quality.net_earned'
        db.delete_column(u'report_reportstrategypeer39quality', 'net_earned')

        # Deleting field 'ReportStrategyProximicNotice.bids_lost'
        db.delete_column(u'report_reportstrategyproximicnotice', 'bids_lost')

        # Deleting field 'ReportStrategyProximicNotice.winbid_value_total'
        db.delete_column(u'report_reportstrategyproximicnotice', 'winbid_value_total')

        # Deleting field 'ReportStrategyProximicNotice.net_earned'
        db.delete_column(u'report_reportstrategyproximicnotice', 'net_earned')

        # Deleting field 'ReportCampaignModel.bids_lost'
        db.delete_column(u'report_reportcampaignmodel', 'bids_lost')

        # Deleting field 'ReportCampaignModel.winbid_value_total'
        db.delete_column(u'report_reportcampaignmodel', 'winbid_value_total')

        # Deleting field 'ReportCampaignModel.net_earned'
        db.delete_column(u'report_reportcampaignmodel', 'net_earned')

        # Deleting field 'ReportCampaignCity.bids_lost'
        db.delete_column(u'report_reportcampaigncity', 'bids_lost')

        # Deleting field 'ReportCampaignCity.winbid_value_total'
        db.delete_column(u'report_reportcampaigncity', 'winbid_value_total')

        # Deleting field 'ReportCampaignCity.net_earned'
        db.delete_column(u'report_reportcampaigncity', 'net_earned')

        # Deleting field 'ReportCampaignPeer39Quality.bids_lost'
        db.delete_column(u'report_reportcampaignpeer39quality', 'bids_lost')

        # Deleting field 'ReportCampaignPeer39Quality.winbid_value_total'
        db.delete_column(u'report_reportcampaignpeer39quality', 'winbid_value_total')

        # Deleting field 'ReportCampaignPeer39Quality.net_earned'
        db.delete_column(u'report_reportcampaignpeer39quality', 'net_earned')

        # Deleting field 'ReportCampaignRegion.bids_lost'
        db.delete_column(u'report_reportcampaignregion', 'bids_lost')

        # Deleting field 'ReportCampaignRegion.winbid_value_total'
        db.delete_column(u'report_reportcampaignregion', 'winbid_value_total')

        # Deleting field 'ReportCampaignRegion.net_earned'
        db.delete_column(u'report_reportcampaignregion', 'net_earned')

        # Deleting field 'ReportStrategyMake.bids_lost'
        db.delete_column(u'report_reportstrategymake', 'bids_lost')

        # Deleting field 'ReportStrategyMake.winbid_value_total'
        db.delete_column(u'report_reportstrategymake', 'winbid_value_total')

        # Deleting field 'ReportStrategyMake.net_earned'
        db.delete_column(u'report_reportstrategymake', 'net_earned')

        # Deleting field 'ReportStrategyCity.bids_lost'
        db.delete_column(u'report_reportstrategycity', 'bids_lost')

        # Deleting field 'ReportStrategyCity.winbid_value_total'
        db.delete_column(u'report_reportstrategycity', 'winbid_value_total')

        # Deleting field 'ReportStrategyCity.net_earned'
        db.delete_column(u'report_reportstrategycity', 'net_earned')

        # Deleting field 'ReportStrategyProximicLanguage.bids_lost'
        db.delete_column(u'report_reportstrategyproximiclanguage', 'bids_lost')

        # Deleting field 'ReportStrategyProximicLanguage.winbid_value_total'
        db.delete_column(u'report_reportstrategyproximiclanguage', 'winbid_value_total')

        # Deleting field 'ReportStrategyProximicLanguage.net_earned'
        db.delete_column(u'report_reportstrategyproximiclanguage', 'net_earned')

        # Deleting field 'ReportCampaignProximicPlace.bids_lost'
        db.delete_column(u'report_reportcampaignproximicplace', 'bids_lost')

        # Deleting field 'ReportCampaignProximicPlace.winbid_value_total'
        db.delete_column(u'report_reportcampaignproximicplace', 'winbid_value_total')

        # Deleting field 'ReportCampaignProximicPlace.net_earned'
        db.delete_column(u'report_reportcampaignproximicplace', 'net_earned')

        # Deleting field 'ReportCampaignProximicLanguage.bids_lost'
        db.delete_column(u'report_reportcampaignproximiclanguage', 'bids_lost')

        # Deleting field 'ReportCampaignProximicLanguage.winbid_value_total'
        db.delete_column(u'report_reportcampaignproximiclanguage', 'winbid_value_total')

        # Deleting field 'ReportCampaignProximicLanguage.net_earned'
        db.delete_column(u'report_reportcampaignproximiclanguage', 'net_earned')

        # Deleting field 'ReportCampaignProximicSafety.bids_lost'
        db.delete_column(u'report_reportcampaignproximicsafety', 'bids_lost')

        # Deleting field 'ReportCampaignProximicSafety.winbid_value_total'
        db.delete_column(u'report_reportcampaignproximicsafety', 'winbid_value_total')

        # Deleting field 'ReportCampaignProximicSafety.net_earned'
        db.delete_column(u'report_reportcampaignproximicsafety', 'net_earned')

        # Deleting field 'ReportStrategyPosition.bids_lost'
        db.delete_column(u'report_reportstrategyposition', 'bids_lost')

        # Deleting field 'ReportStrategyPosition.winbid_value_total'
        db.delete_column(u'report_reportstrategyposition', 'winbid_value_total')

        # Deleting field 'ReportStrategyPosition.net_earned'
        db.delete_column(u'report_reportstrategyposition', 'net_earned')

        # Deleting field 'ReportCampaignPeer39Brand.bids_lost'
        db.delete_column(u'report_reportcampaignpeer39brand', 'bids_lost')

        # Deleting field 'ReportCampaignPeer39Brand.winbid_value_total'
        db.delete_column(u'report_reportcampaignpeer39brand', 'winbid_value_total')

        # Deleting field 'ReportCampaignPeer39Brand.net_earned'
        db.delete_column(u'report_reportcampaignpeer39brand', 'net_earned')

        # Deleting field 'ReportCampaignProximicQuality.bids_lost'
        db.delete_column(u'report_reportcampaignproximicquality', 'bids_lost')

        # Deleting field 'ReportCampaignProximicQuality.winbid_value_total'
        db.delete_column(u'report_reportcampaignproximicquality', 'winbid_value_total')

        # Deleting field 'ReportCampaignProximicQuality.net_earned'
        db.delete_column(u'report_reportcampaignproximicquality', 'net_earned')

        # Deleting field 'ReportStrategyProximicPlace.bids_lost'
        db.delete_column(u'report_reportstrategyproximicplace', 'bids_lost')

        # Deleting field 'ReportStrategyProximicPlace.winbid_value_total'
        db.delete_column(u'report_reportstrategyproximicplace', 'winbid_value_total')

        # Deleting field 'ReportStrategyProximicPlace.net_earned'
        db.delete_column(u'report_reportstrategyproximicplace', 'net_earned')

        # Deleting field 'ReportStrategySite.bids_lost'
        db.delete_column(u'report_reportstrategysite', 'bids_lost')

        # Deleting field 'ReportStrategySite.winbid_value_total'
        db.delete_column(u'report_reportstrategysite', 'winbid_value_total')

        # Deleting field 'ReportStrategySite.net_earned'
        db.delete_column(u'report_reportstrategysite', 'net_earned')


    def backwards(self, orm):
        # Adding field 'ReportStrategyAge.bids_lost'
        db.add_column(u'report_reportstrategyage', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyAge.winbid_value_total'
        db.add_column(u'report_reportstrategyage', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyAge.net_earned'
        db.add_column(u'report_reportstrategyage', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPublisherNetwork.bids_lost'
        db.add_column(u'report_reportstrategypublishernetwork', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPublisherNetwork.winbid_value_total'
        db.add_column(u'report_reportstrategypublishernetwork', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPublisherNetwork.net_earned'
        db.add_column(u'report_reportstrategypublishernetwork', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Language.bids_lost'
        db.add_column(u'report_reportstrategypeer39language', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Language.winbid_value_total'
        db.add_column(u'report_reportstrategypeer39language', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Language.net_earned'
        db.add_column(u'report_reportstrategypeer39language', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCategory.bids_lost'
        db.add_column(u'report_reportcampaigncategory', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCategory.winbid_value_total'
        db.add_column(u'report_reportcampaigncategory', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCategory.net_earned'
        db.add_column(u'report_reportcampaigncategory', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignDomain.bids_lost'
        db.add_column(u'report_reportcampaigndomain', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignDomain.winbid_value_total'
        db.add_column(u'report_reportcampaigndomain', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignDomain.net_earned'
        db.add_column(u'report_reportcampaigndomain', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyDomain.bids_lost'
        db.add_column(u'report_reportstrategydomain', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyDomain.winbid_value_total'
        db.add_column(u'report_reportstrategydomain', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyDomain.net_earned'
        db.add_column(u'report_reportstrategydomain', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicNotice.bids_lost'
        db.add_column(u'report_reportcampaignproximicnotice', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicNotice.winbid_value_total'
        db.add_column(u'report_reportcampaignproximicnotice', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicNotice.net_earned'
        db.add_column(u'report_reportcampaignproximicnotice', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPosition.bids_lost'
        db.add_column(u'report_reportcampaignposition', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPosition.winbid_value_total'
        db.add_column(u'report_reportcampaignposition', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPosition.net_earned'
        db.add_column(u'report_reportcampaignposition', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicContext.bids_lost'
        db.add_column(u'report_reportstrategyproximiccontext', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicContext.winbid_value_total'
        db.add_column(u'report_reportstrategyproximiccontext', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicContext.net_earned'
        db.add_column(u'report_reportstrategyproximiccontext', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicContextual.bids_lost'
        db.add_column(u'report_reportcampaignproximiccontextual', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicContextual.winbid_value_total'
        db.add_column(u'report_reportcampaignproximiccontextual', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicContextual.net_earned'
        db.add_column(u'report_reportcampaignproximiccontextual', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCategory.bids_lost'
        db.add_column(u'report_reportstrategycategory', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCategory.winbid_value_total'
        db.add_column(u'report_reportstrategycategory', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCategory.net_earned'
        db.add_column(u'report_reportstrategycategory', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaign.bids_lost'
        db.add_column(u'report_reportcampaign', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaign.winbid_value_total'
        db.add_column(u'report_reportcampaign', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaign.net_earned'
        db.add_column(u'report_reportcampaign', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPublisher.bids_lost'
        db.add_column(u'report_reportcampaignpublisher', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPublisher.winbid_value_total'
        db.add_column(u'report_reportcampaignpublisher', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPublisher.net_earned'
        db.add_column(u'report_reportcampaignpublisher', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicQuality.bids_lost'
        db.add_column(u'report_reportstrategyproximicquality', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicQuality.winbid_value_total'
        db.add_column(u'report_reportstrategyproximicquality', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicQuality.net_earned'
        db.add_column(u'report_reportstrategyproximicquality', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCarrier.bids_lost'
        db.add_column(u'report_reportcampaigncarrier', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCarrier.winbid_value_total'
        db.add_column(u'report_reportcampaigncarrier', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCarrier.net_earned'
        db.add_column(u'report_reportcampaigncarrier', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyRegion.bids_lost'
        db.add_column(u'report_reportstrategyregion', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyRegion.winbid_value_total'
        db.add_column(u'report_reportstrategyregion', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyRegion.net_earned'
        db.add_column(u'report_reportstrategyregion', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignAge.bids_lost'
        db.add_column(u'report_reportcampaignage', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignAge.winbid_value_total'
        db.add_column(u'report_reportcampaignage', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignAge.net_earned'
        db.add_column(u'report_reportcampaignage', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignMake.bids_lost'
        db.add_column(u'report_reportcampaignmake', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignMake.winbid_value_total'
        db.add_column(u'report_reportcampaignmake', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignMake.net_earned'
        db.add_column(u'report_reportcampaignmake', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCountry.bids_lost'
        db.add_column(u'report_reportstrategycountry', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCountry.winbid_value_total'
        db.add_column(u'report_reportstrategycountry', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCountry.net_earned'
        db.add_column(u'report_reportstrategycountry', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignGender.bids_lost'
        db.add_column(u'report_reportcampaigngender', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignGender.winbid_value_total'
        db.add_column(u'report_reportcampaigngender', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignGender.net_earned'
        db.add_column(u'report_reportcampaigngender', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyOs.bids_lost'
        db.add_column(u'report_reportstrategyos', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyOs.winbid_value_total'
        db.add_column(u'report_reportstrategyos', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyOs.net_earned'
        db.add_column(u'report_reportstrategyos', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignSite.bids_lost'
        db.add_column(u'report_reportcampaignsite', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignSite.winbid_value_total'
        db.add_column(u'report_reportcampaignsite', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignSite.net_earned'
        db.add_column(u'report_reportcampaignsite', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Contextual.bids_lost'
        db.add_column(u'report_reportstrategypeer39contextual', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Contextual.winbid_value_total'
        db.add_column(u'report_reportstrategypeer39contextual', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Contextual.net_earned'
        db.add_column(u'report_reportstrategypeer39contextual', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicMaturity.bids_lost'
        db.add_column(u'report_reportcampaignproximicmaturity', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicMaturity.winbid_value_total'
        db.add_column(u'report_reportcampaignproximicmaturity', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicMaturity.net_earned'
        db.add_column(u'report_reportcampaignproximicmaturity', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPublisherNetwork.bids_lost'
        db.add_column(u'report_reportcampaignpublishernetwork', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPublisherNetwork.winbid_value_total'
        db.add_column(u'report_reportcampaignpublishernetwork', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPublisherNetwork.net_earned'
        db.add_column(u'report_reportcampaignpublishernetwork', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCountry.bids_lost'
        db.add_column(u'report_reportcampaigncountry', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCountry.winbid_value_total'
        db.add_column(u'report_reportcampaigncountry', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCountry.net_earned'
        db.add_column(u'report_reportcampaigncountry', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicMaturity.bids_lost'
        db.add_column(u'report_reportstrategyproximicmaturity', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicMaturity.winbid_value_total'
        db.add_column(u'report_reportstrategyproximicmaturity', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicMaturity.net_earned'
        db.add_column(u'report_reportstrategyproximicmaturity', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyGender.bids_lost'
        db.add_column(u'report_reportstrategygender', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyGender.winbid_value_total'
        db.add_column(u'report_reportstrategygender', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyGender.net_earned'
        db.add_column(u'report_reportstrategygender', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportAdvert.bids_lost'
        db.add_column(u'report_reportadvert', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportAdvert.winbid_value_total'
        db.add_column(u'report_reportadvert', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportAdvert.net_earned'
        db.add_column(u'report_reportadvert', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Language.bids_lost'
        db.add_column(u'report_reportcampaignpeer39language', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Language.winbid_value_total'
        db.add_column(u'report_reportcampaignpeer39language', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Language.net_earned'
        db.add_column(u'report_reportcampaignpeer39language', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCarrier.bids_lost'
        db.add_column(u'report_reportstrategycarrier', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCarrier.winbid_value_total'
        db.add_column(u'report_reportstrategycarrier', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCarrier.net_earned'
        db.add_column(u'report_reportstrategycarrier', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignOs.bids_lost'
        db.add_column(u'report_reportcampaignos', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignOs.winbid_value_total'
        db.add_column(u'report_reportcampaignos', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignOs.net_earned'
        db.add_column(u'report_reportcampaignos', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Brand.bids_lost'
        db.add_column(u'report_reportstrategypeer39brand', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Brand.winbid_value_total'
        db.add_column(u'report_reportstrategypeer39brand', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Brand.net_earned'
        db.add_column(u'report_reportstrategypeer39brand', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicSafety.bids_lost'
        db.add_column(u'report_reportstrategyproximicsafety', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicSafety.winbid_value_total'
        db.add_column(u'report_reportstrategyproximicsafety', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicSafety.net_earned'
        db.add_column(u'report_reportstrategyproximicsafety', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPublisher.bids_lost'
        db.add_column(u'report_reportstrategypublisher', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPublisher.winbid_value_total'
        db.add_column(u'report_reportstrategypublisher', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPublisher.net_earned'
        db.add_column(u'report_reportstrategypublisher', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategy.bids_lost'
        db.add_column(u'report_reportstrategy', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategy.winbid_value_total'
        db.add_column(u'report_reportstrategy', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategy.net_earned'
        db.add_column(u'report_reportstrategy', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyModel.bids_lost'
        db.add_column(u'report_reportstrategymodel', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyModel.winbid_value_total'
        db.add_column(u'report_reportstrategymodel', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyModel.net_earned'
        db.add_column(u'report_reportstrategymodel', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Contextual.bids_lost'
        db.add_column(u'report_reportcampaignpeer39contextual', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Contextual.winbid_value_total'
        db.add_column(u'report_reportcampaignpeer39contextual', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Contextual.net_earned'
        db.add_column(u'report_reportcampaignpeer39contextual', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Quality.bids_lost'
        db.add_column(u'report_reportstrategypeer39quality', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Quality.winbid_value_total'
        db.add_column(u'report_reportstrategypeer39quality', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPeer39Quality.net_earned'
        db.add_column(u'report_reportstrategypeer39quality', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicNotice.bids_lost'
        db.add_column(u'report_reportstrategyproximicnotice', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicNotice.winbid_value_total'
        db.add_column(u'report_reportstrategyproximicnotice', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicNotice.net_earned'
        db.add_column(u'report_reportstrategyproximicnotice', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignModel.bids_lost'
        db.add_column(u'report_reportcampaignmodel', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignModel.winbid_value_total'
        db.add_column(u'report_reportcampaignmodel', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignModel.net_earned'
        db.add_column(u'report_reportcampaignmodel', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCity.bids_lost'
        db.add_column(u'report_reportcampaigncity', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCity.winbid_value_total'
        db.add_column(u'report_reportcampaigncity', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignCity.net_earned'
        db.add_column(u'report_reportcampaigncity', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Quality.bids_lost'
        db.add_column(u'report_reportcampaignpeer39quality', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Quality.winbid_value_total'
        db.add_column(u'report_reportcampaignpeer39quality', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Quality.net_earned'
        db.add_column(u'report_reportcampaignpeer39quality', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignRegion.bids_lost'
        db.add_column(u'report_reportcampaignregion', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignRegion.winbid_value_total'
        db.add_column(u'report_reportcampaignregion', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignRegion.net_earned'
        db.add_column(u'report_reportcampaignregion', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyMake.bids_lost'
        db.add_column(u'report_reportstrategymake', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyMake.winbid_value_total'
        db.add_column(u'report_reportstrategymake', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyMake.net_earned'
        db.add_column(u'report_reportstrategymake', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCity.bids_lost'
        db.add_column(u'report_reportstrategycity', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCity.winbid_value_total'
        db.add_column(u'report_reportstrategycity', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyCity.net_earned'
        db.add_column(u'report_reportstrategycity', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicLanguage.bids_lost'
        db.add_column(u'report_reportstrategyproximiclanguage', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicLanguage.winbid_value_total'
        db.add_column(u'report_reportstrategyproximiclanguage', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicLanguage.net_earned'
        db.add_column(u'report_reportstrategyproximiclanguage', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicPlace.bids_lost'
        db.add_column(u'report_reportcampaignproximicplace', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicPlace.winbid_value_total'
        db.add_column(u'report_reportcampaignproximicplace', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicPlace.net_earned'
        db.add_column(u'report_reportcampaignproximicplace', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicLanguage.bids_lost'
        db.add_column(u'report_reportcampaignproximiclanguage', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicLanguage.winbid_value_total'
        db.add_column(u'report_reportcampaignproximiclanguage', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicLanguage.net_earned'
        db.add_column(u'report_reportcampaignproximiclanguage', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicSafety.bids_lost'
        db.add_column(u'report_reportcampaignproximicsafety', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicSafety.winbid_value_total'
        db.add_column(u'report_reportcampaignproximicsafety', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicSafety.net_earned'
        db.add_column(u'report_reportcampaignproximicsafety', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPosition.bids_lost'
        db.add_column(u'report_reportstrategyposition', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPosition.winbid_value_total'
        db.add_column(u'report_reportstrategyposition', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyPosition.net_earned'
        db.add_column(u'report_reportstrategyposition', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Brand.bids_lost'
        db.add_column(u'report_reportcampaignpeer39brand', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Brand.winbid_value_total'
        db.add_column(u'report_reportcampaignpeer39brand', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignPeer39Brand.net_earned'
        db.add_column(u'report_reportcampaignpeer39brand', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicQuality.bids_lost'
        db.add_column(u'report_reportcampaignproximicquality', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicQuality.winbid_value_total'
        db.add_column(u'report_reportcampaignproximicquality', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportCampaignProximicQuality.net_earned'
        db.add_column(u'report_reportcampaignproximicquality', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicPlace.bids_lost'
        db.add_column(u'report_reportstrategyproximicplace', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicPlace.winbid_value_total'
        db.add_column(u'report_reportstrategyproximicplace', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategyProximicPlace.net_earned'
        db.add_column(u'report_reportstrategyproximicplace', 'net_earned',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategySite.bids_lost'
        db.add_column(u'report_reportstrategysite', 'bids_lost',
                      self.gf('ui.fields.BigDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategySite.winbid_value_total'
        db.add_column(u'report_reportstrategysite', 'winbid_value_total',
                      self.gf('ui.fields.BudgetSpentDecimalField')(default=0),
                      keep_default=False)

        # Adding field 'ReportStrategySite.net_earned'
        db.add_column(u'report_reportstrategysite', 'net_earned',
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
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