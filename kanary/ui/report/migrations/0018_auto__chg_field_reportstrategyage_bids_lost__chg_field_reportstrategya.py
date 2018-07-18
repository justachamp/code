# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ReportStrategyAge.bids_lost'
        db.alter_column(u'report_reportstrategyage', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyAge.conv'
        db.alter_column(u'report_reportstrategyage', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyAge.clk'
        db.alter_column(u'report_reportstrategyage', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyAge.bid'
        db.alter_column(u'report_reportstrategyage', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyAge.imp'
        db.alter_column(u'report_reportstrategyage', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyAge.winbid'
        db.alter_column(u'report_reportstrategyage', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyOsVersion.bids_lost'
        db.alter_column(u'report_reportstrategyosversion', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyOsVersion.conv'
        db.alter_column(u'report_reportstrategyosversion', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyOsVersion.clk'
        db.alter_column(u'report_reportstrategyosversion', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyOsVersion.bid'
        db.alter_column(u'report_reportstrategyosversion', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyOsVersion.imp'
        db.alter_column(u'report_reportstrategyosversion', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyOsVersion.winbid'
        db.alter_column(u'report_reportstrategyosversion', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicSafety.bids_lost'
        db.alter_column(u'report_reportadvertproximicsafety', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicSafety.conv'
        db.alter_column(u'report_reportadvertproximicsafety', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicSafety.clk'
        db.alter_column(u'report_reportadvertproximicsafety', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicSafety.bid'
        db.alter_column(u'report_reportadvertproximicsafety', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicSafety.imp'
        db.alter_column(u'report_reportadvertproximicsafety', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicSafety.winbid'
        db.alter_column(u'report_reportadvertproximicsafety', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPublisherNetwork.bids_lost'
        db.alter_column(u'report_reportstrategypublishernetwork', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPublisherNetwork.conv'
        db.alter_column(u'report_reportstrategypublishernetwork', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPublisherNetwork.clk'
        db.alter_column(u'report_reportstrategypublishernetwork', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPublisherNetwork.bid'
        db.alter_column(u'report_reportstrategypublishernetwork', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPublisherNetwork.imp'
        db.alter_column(u'report_reportstrategypublishernetwork', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPublisherNetwork.winbid'
        db.alter_column(u'report_reportstrategypublishernetwork', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Language.bids_lost'
        db.alter_column(u'report_reportstrategypeer39language', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Language.conv'
        db.alter_column(u'report_reportstrategypeer39language', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Language.clk'
        db.alter_column(u'report_reportstrategypeer39language', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Language.bid'
        db.alter_column(u'report_reportstrategypeer39language', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Language.imp'
        db.alter_column(u'report_reportstrategypeer39language', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Language.winbid'
        db.alter_column(u'report_reportstrategypeer39language', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCountry.bids_lost'
        db.alter_column(u'report_reportadvertcountry', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCountry.conv'
        db.alter_column(u'report_reportadvertcountry', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCountry.clk'
        db.alter_column(u'report_reportadvertcountry', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCountry.bid'
        db.alter_column(u'report_reportadvertcountry', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCountry.imp'
        db.alter_column(u'report_reportadvertcountry', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCountry.winbid'
        db.alter_column(u'report_reportadvertcountry', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicContextual.bids_lost'
        db.alter_column(u'report_reportadvertproximiccontextual', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicContextual.conv'
        db.alter_column(u'report_reportadvertproximiccontextual', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicContextual.clk'
        db.alter_column(u'report_reportadvertproximiccontextual', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicContextual.bid'
        db.alter_column(u'report_reportadvertproximiccontextual', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicContextual.imp'
        db.alter_column(u'report_reportadvertproximiccontextual', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicContextual.winbid'
        db.alter_column(u'report_reportadvertproximiccontextual', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCity.bids_lost'
        db.alter_column(u'report_reportstrategycity', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCity.conv'
        db.alter_column(u'report_reportstrategycity', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCity.clk'
        db.alter_column(u'report_reportstrategycity', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCity.bid'
        db.alter_column(u'report_reportstrategycity', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCity.imp'
        db.alter_column(u'report_reportstrategycity', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCity.winbid'
        db.alter_column(u'report_reportstrategycity', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPosition.bids_lost'
        db.alter_column(u'report_reportadvertposition', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPosition.conv'
        db.alter_column(u'report_reportadvertposition', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPosition.clk'
        db.alter_column(u'report_reportadvertposition', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPosition.bid'
        db.alter_column(u'report_reportadvertposition', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPosition.imp'
        db.alter_column(u'report_reportadvertposition', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPosition.winbid'
        db.alter_column(u'report_reportadvertposition', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCategory.bids_lost'
        db.alter_column(u'report_reportstrategycategory', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCategory.conv'
        db.alter_column(u'report_reportstrategycategory', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCategory.clk'
        db.alter_column(u'report_reportstrategycategory', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCategory.bid'
        db.alter_column(u'report_reportstrategycategory', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCategory.imp'
        db.alter_column(u'report_reportstrategycategory', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCategory.winbid'
        db.alter_column(u'report_reportstrategycategory', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertOsVersion.bids_lost'
        db.alter_column(u'report_reportadvertosversion', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertOsVersion.conv'
        db.alter_column(u'report_reportadvertosversion', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertOsVersion.clk'
        db.alter_column(u'report_reportadvertosversion', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertOsVersion.bid'
        db.alter_column(u'report_reportadvertosversion', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertOsVersion.imp'
        db.alter_column(u'report_reportadvertosversion', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertOsVersion.winbid'
        db.alter_column(u'report_reportadvertosversion', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicQuality.bids_lost'
        db.alter_column(u'report_reportstrategyproximicquality', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicQuality.conv'
        db.alter_column(u'report_reportstrategyproximicquality', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicQuality.clk'
        db.alter_column(u'report_reportstrategyproximicquality', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicQuality.bid'
        db.alter_column(u'report_reportstrategyproximicquality', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicQuality.imp'
        db.alter_column(u'report_reportstrategyproximicquality', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicQuality.winbid'
        db.alter_column(u'report_reportstrategyproximicquality', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyOs.bids_lost'
        db.alter_column(u'report_reportstrategyos', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyOs.conv'
        db.alter_column(u'report_reportstrategyos', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyOs.clk'
        db.alter_column(u'report_reportstrategyos', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyOs.bid'
        db.alter_column(u'report_reportstrategyos', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyOs.imp'
        db.alter_column(u'report_reportstrategyos', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyOs.winbid'
        db.alter_column(u'report_reportstrategyos', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicQuality.bids_lost'
        db.alter_column(u'report_reportadvertproximicquality', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicQuality.conv'
        db.alter_column(u'report_reportadvertproximicquality', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicQuality.clk'
        db.alter_column(u'report_reportadvertproximicquality', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicQuality.bid'
        db.alter_column(u'report_reportadvertproximicquality', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicQuality.imp'
        db.alter_column(u'report_reportadvertproximicquality', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicQuality.winbid'
        db.alter_column(u'report_reportadvertproximicquality', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyRegion.bids_lost'
        db.alter_column(u'report_reportstrategyregion', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyRegion.conv'
        db.alter_column(u'report_reportstrategyregion', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyRegion.clk'
        db.alter_column(u'report_reportstrategyregion', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyRegion.bid'
        db.alter_column(u'report_reportstrategyregion', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyRegion.imp'
        db.alter_column(u'report_reportstrategyregion', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyRegion.winbid'
        db.alter_column(u'report_reportstrategyregion', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicPlace.bids_lost'
        db.alter_column(u'report_reportstrategyproximicplace', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicPlace.conv'
        db.alter_column(u'report_reportstrategyproximicplace', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicPlace.clk'
        db.alter_column(u'report_reportstrategyproximicplace', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicPlace.bid'
        db.alter_column(u'report_reportstrategyproximicplace', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicPlace.imp'
        db.alter_column(u'report_reportstrategyproximicplace', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicPlace.winbid'
        db.alter_column(u'report_reportstrategyproximicplace', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertMake.bids_lost'
        db.alter_column(u'report_reportadvertmake', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertMake.conv'
        db.alter_column(u'report_reportadvertmake', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertMake.clk'
        db.alter_column(u'report_reportadvertmake', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertMake.bid'
        db.alter_column(u'report_reportadvertmake', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertMake.imp'
        db.alter_column(u'report_reportadvertmake', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertMake.winbid'
        db.alter_column(u'report_reportadvertmake', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicLanguage.bids_lost'
        db.alter_column(u'report_reportadvertproximiclanguage', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicLanguage.conv'
        db.alter_column(u'report_reportadvertproximiclanguage', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicLanguage.clk'
        db.alter_column(u'report_reportadvertproximiclanguage', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicLanguage.bid'
        db.alter_column(u'report_reportadvertproximiclanguage', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicLanguage.imp'
        db.alter_column(u'report_reportadvertproximiclanguage', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicLanguage.winbid'
        db.alter_column(u'report_reportadvertproximiclanguage', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Brand.bids_lost'
        db.alter_column(u'report_reportadvertpeer39brand', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Brand.conv'
        db.alter_column(u'report_reportadvertpeer39brand', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Brand.clk'
        db.alter_column(u'report_reportadvertpeer39brand', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Brand.bid'
        db.alter_column(u'report_reportadvertpeer39brand', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Brand.imp'
        db.alter_column(u'report_reportadvertpeer39brand', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Brand.winbid'
        db.alter_column(u'report_reportadvertpeer39brand', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCountry.bids_lost'
        db.alter_column(u'report_reportstrategycountry', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCountry.conv'
        db.alter_column(u'report_reportstrategycountry', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCountry.clk'
        db.alter_column(u'report_reportstrategycountry', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCountry.bid'
        db.alter_column(u'report_reportstrategycountry', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCountry.imp'
        db.alter_column(u'report_reportstrategycountry', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCountry.winbid'
        db.alter_column(u'report_reportstrategycountry', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPublisher.bids_lost'
        db.alter_column(u'report_reportadvertpublisher', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPublisher.conv'
        db.alter_column(u'report_reportadvertpublisher', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPublisher.clk'
        db.alter_column(u'report_reportadvertpublisher', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPublisher.bid'
        db.alter_column(u'report_reportadvertpublisher', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPublisher.imp'
        db.alter_column(u'report_reportadvertpublisher', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPublisher.winbid'
        db.alter_column(u'report_reportadvertpublisher', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Quality.bids_lost'
        db.alter_column(u'report_reportadvertpeer39quality', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Quality.conv'
        db.alter_column(u'report_reportadvertpeer39quality', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Quality.clk'
        db.alter_column(u'report_reportadvertpeer39quality', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Quality.bid'
        db.alter_column(u'report_reportadvertpeer39quality', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Quality.imp'
        db.alter_column(u'report_reportadvertpeer39quality', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Quality.winbid'
        db.alter_column(u'report_reportadvertpeer39quality', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Contextual.bids_lost'
        db.alter_column(u'report_reportstrategypeer39contextual', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Contextual.conv'
        db.alter_column(u'report_reportstrategypeer39contextual', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Contextual.clk'
        db.alter_column(u'report_reportstrategypeer39contextual', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Contextual.bid'
        db.alter_column(u'report_reportstrategypeer39contextual', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Contextual.imp'
        db.alter_column(u'report_reportstrategypeer39contextual', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Contextual.winbid'
        db.alter_column(u'report_reportstrategypeer39contextual', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyDomain.bids_lost'
        db.alter_column(u'report_reportstrategydomain', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyDomain.conv'
        db.alter_column(u'report_reportstrategydomain', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyDomain.clk'
        db.alter_column(u'report_reportstrategydomain', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyDomain.bid'
        db.alter_column(u'report_reportstrategydomain', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyDomain.imp'
        db.alter_column(u'report_reportstrategydomain', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyDomain.winbid'
        db.alter_column(u'report_reportstrategydomain', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Language.bids_lost'
        db.alter_column(u'report_reportadvertpeer39language', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Language.conv'
        db.alter_column(u'report_reportadvertpeer39language', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Language.clk'
        db.alter_column(u'report_reportadvertpeer39language', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Language.bid'
        db.alter_column(u'report_reportadvertpeer39language', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Language.imp'
        db.alter_column(u'report_reportadvertpeer39language', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Language.winbid'
        db.alter_column(u'report_reportadvertpeer39language', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyMake.bids_lost'
        db.alter_column(u'report_reportstrategymake', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyMake.conv'
        db.alter_column(u'report_reportstrategymake', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyMake.clk'
        db.alter_column(u'report_reportstrategymake', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyMake.bid'
        db.alter_column(u'report_reportstrategymake', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyMake.imp'
        db.alter_column(u'report_reportstrategymake', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyMake.winbid'
        db.alter_column(u'report_reportstrategymake', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertSite.bids_lost'
        db.alter_column(u'report_reportadvertsite', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertSite.conv'
        db.alter_column(u'report_reportadvertsite', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertSite.clk'
        db.alter_column(u'report_reportadvertsite', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertSite.bid'
        db.alter_column(u'report_reportadvertsite', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertSite.imp'
        db.alter_column(u'report_reportadvertsite', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertSite.winbid'
        db.alter_column(u'report_reportadvertsite', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertAge.bids_lost'
        db.alter_column(u'report_reportadvertage', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertAge.conv'
        db.alter_column(u'report_reportadvertage', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertAge.clk'
        db.alter_column(u'report_reportadvertage', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertAge.bid'
        db.alter_column(u'report_reportadvertage', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertAge.imp'
        db.alter_column(u'report_reportadvertage', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertAge.winbid'
        db.alter_column(u'report_reportadvertage', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategy.bids_lost'
        db.alter_column(u'report_reportstrategy', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategy.conv'
        db.alter_column(u'report_reportstrategy', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategy.clk'
        db.alter_column(u'report_reportstrategy', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategy.bid'
        db.alter_column(u'report_reportstrategy', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategy.imp'
        db.alter_column(u'report_reportstrategy', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategy.winbid'
        db.alter_column(u'report_reportstrategy', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyGender.bids_lost'
        db.alter_column(u'report_reportstrategygender', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyGender.conv'
        db.alter_column(u'report_reportstrategygender', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyGender.clk'
        db.alter_column(u'report_reportstrategygender', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyGender.bid'
        db.alter_column(u'report_reportstrategygender', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyGender.imp'
        db.alter_column(u'report_reportstrategygender', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyGender.winbid'
        db.alter_column(u'report_reportstrategygender', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCity.bids_lost'
        db.alter_column(u'report_reportadvertcity', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCity.conv'
        db.alter_column(u'report_reportadvertcity', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCity.clk'
        db.alter_column(u'report_reportadvertcity', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCity.bid'
        db.alter_column(u'report_reportadvertcity', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCity.imp'
        db.alter_column(u'report_reportadvertcity', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCity.winbid'
        db.alter_column(u'report_reportadvertcity', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvert.bids_lost'
        db.alter_column(u'report_reportadvert', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvert.conv'
        db.alter_column(u'report_reportadvert', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvert.clk'
        db.alter_column(u'report_reportadvert', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvert.bid'
        db.alter_column(u'report_reportadvert', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvert.imp'
        db.alter_column(u'report_reportadvert', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvert.winbid'
        db.alter_column(u'report_reportadvert', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertRegion.bids_lost'
        db.alter_column(u'report_reportadvertregion', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertRegion.conv'
        db.alter_column(u'report_reportadvertregion', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertRegion.clk'
        db.alter_column(u'report_reportadvertregion', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertRegion.bid'
        db.alter_column(u'report_reportadvertregion', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertRegion.imp'
        db.alter_column(u'report_reportadvertregion', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertRegion.winbid'
        db.alter_column(u'report_reportadvertregion', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertGender.bids_lost'
        db.alter_column(u'report_reportadvertgender', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertGender.conv'
        db.alter_column(u'report_reportadvertgender', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertGender.clk'
        db.alter_column(u'report_reportadvertgender', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertGender.bid'
        db.alter_column(u'report_reportadvertgender', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertGender.imp'
        db.alter_column(u'report_reportadvertgender', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertGender.winbid'
        db.alter_column(u'report_reportadvertgender', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Contextual.bids_lost'
        db.alter_column(u'report_reportadvertpeer39contextual', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Contextual.conv'
        db.alter_column(u'report_reportadvertpeer39contextual', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Contextual.clk'
        db.alter_column(u'report_reportadvertpeer39contextual', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Contextual.bid'
        db.alter_column(u'report_reportadvertpeer39contextual', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Contextual.imp'
        db.alter_column(u'report_reportadvertpeer39contextual', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPeer39Contextual.winbid'
        db.alter_column(u'report_reportadvertpeer39contextual', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCarrier.bids_lost'
        db.alter_column(u'report_reportstrategycarrier', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCarrier.conv'
        db.alter_column(u'report_reportstrategycarrier', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCarrier.clk'
        db.alter_column(u'report_reportstrategycarrier', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCarrier.bid'
        db.alter_column(u'report_reportstrategycarrier', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCarrier.imp'
        db.alter_column(u'report_reportstrategycarrier', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyCarrier.winbid'
        db.alter_column(u'report_reportstrategycarrier', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicNotice.bids_lost'
        db.alter_column(u'report_reportadvertproximicnotice', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicNotice.conv'
        db.alter_column(u'report_reportadvertproximicnotice', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicNotice.clk'
        db.alter_column(u'report_reportadvertproximicnotice', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicNotice.bid'
        db.alter_column(u'report_reportadvertproximicnotice', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicNotice.imp'
        db.alter_column(u'report_reportadvertproximicnotice', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicNotice.winbid'
        db.alter_column(u'report_reportadvertproximicnotice', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCategory.bids_lost'
        db.alter_column(u'report_reportadvertcategory', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCategory.conv'
        db.alter_column(u'report_reportadvertcategory', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCategory.clk'
        db.alter_column(u'report_reportadvertcategory', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCategory.bid'
        db.alter_column(u'report_reportadvertcategory', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCategory.imp'
        db.alter_column(u'report_reportadvertcategory', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCategory.winbid'
        db.alter_column(u'report_reportadvertcategory', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicSafety.bids_lost'
        db.alter_column(u'report_reportstrategyproximicsafety', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicSafety.conv'
        db.alter_column(u'report_reportstrategyproximicsafety', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicSafety.clk'
        db.alter_column(u'report_reportstrategyproximicsafety', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicSafety.bid'
        db.alter_column(u'report_reportstrategyproximicsafety', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicSafety.imp'
        db.alter_column(u'report_reportstrategyproximicsafety', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicSafety.winbid'
        db.alter_column(u'report_reportstrategyproximicsafety', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicPlace.bids_lost'
        db.alter_column(u'report_reportadvertproximicplace', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicPlace.conv'
        db.alter_column(u'report_reportadvertproximicplace', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicPlace.clk'
        db.alter_column(u'report_reportadvertproximicplace', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicPlace.bid'
        db.alter_column(u'report_reportadvertproximicplace', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicPlace.imp'
        db.alter_column(u'report_reportadvertproximicplace', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicPlace.winbid'
        db.alter_column(u'report_reportadvertproximicplace', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPublisher.bids_lost'
        db.alter_column(u'report_reportstrategypublisher', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPublisher.conv'
        db.alter_column(u'report_reportstrategypublisher', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPublisher.clk'
        db.alter_column(u'report_reportstrategypublisher', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPublisher.bid'
        db.alter_column(u'report_reportstrategypublisher', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPublisher.imp'
        db.alter_column(u'report_reportstrategypublisher', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPublisher.winbid'
        db.alter_column(u'report_reportstrategypublisher', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicMaturity.bids_lost'
        db.alter_column(u'report_reportstrategyproximicmaturity', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicMaturity.conv'
        db.alter_column(u'report_reportstrategyproximicmaturity', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicMaturity.clk'
        db.alter_column(u'report_reportstrategyproximicmaturity', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicMaturity.bid'
        db.alter_column(u'report_reportstrategyproximicmaturity', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicMaturity.imp'
        db.alter_column(u'report_reportstrategyproximicmaturity', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicMaturity.winbid'
        db.alter_column(u'report_reportstrategyproximicmaturity', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertOs.bids_lost'
        db.alter_column(u'report_reportadvertos', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertOs.conv'
        db.alter_column(u'report_reportadvertos', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertOs.clk'
        db.alter_column(u'report_reportadvertos', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertOs.bid'
        db.alter_column(u'report_reportadvertos', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertOs.imp'
        db.alter_column(u'report_reportadvertos', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertOs.winbid'
        db.alter_column(u'report_reportadvertos', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertDomain.bids_lost'
        db.alter_column(u'report_reportadvertdomain', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertDomain.conv'
        db.alter_column(u'report_reportadvertdomain', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertDomain.clk'
        db.alter_column(u'report_reportadvertdomain', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertDomain.bid'
        db.alter_column(u'report_reportadvertdomain', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertDomain.imp'
        db.alter_column(u'report_reportadvertdomain', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertDomain.winbid'
        db.alter_column(u'report_reportadvertdomain', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyModel.bids_lost'
        db.alter_column(u'report_reportstrategymodel', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyModel.conv'
        db.alter_column(u'report_reportstrategymodel', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyModel.clk'
        db.alter_column(u'report_reportstrategymodel', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyModel.bid'
        db.alter_column(u'report_reportstrategymodel', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyModel.imp'
        db.alter_column(u'report_reportstrategymodel', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyModel.winbid'
        db.alter_column(u'report_reportstrategymodel', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPublisherNetwork.bids_lost'
        db.alter_column(u'report_reportadvertpublishernetwork', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPublisherNetwork.conv'
        db.alter_column(u'report_reportadvertpublishernetwork', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPublisherNetwork.clk'
        db.alter_column(u'report_reportadvertpublishernetwork', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPublisherNetwork.bid'
        db.alter_column(u'report_reportadvertpublishernetwork', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPublisherNetwork.imp'
        db.alter_column(u'report_reportadvertpublishernetwork', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertPublisherNetwork.winbid'
        db.alter_column(u'report_reportadvertpublishernetwork', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Quality.bids_lost'
        db.alter_column(u'report_reportstrategypeer39quality', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Quality.conv'
        db.alter_column(u'report_reportstrategypeer39quality', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Quality.clk'
        db.alter_column(u'report_reportstrategypeer39quality', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Quality.bid'
        db.alter_column(u'report_reportstrategypeer39quality', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Quality.imp'
        db.alter_column(u'report_reportstrategypeer39quality', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Quality.winbid'
        db.alter_column(u'report_reportstrategypeer39quality', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicNotice.bids_lost'
        db.alter_column(u'report_reportstrategyproximicnotice', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicNotice.conv'
        db.alter_column(u'report_reportstrategyproximicnotice', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicNotice.clk'
        db.alter_column(u'report_reportstrategyproximicnotice', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicNotice.bid'
        db.alter_column(u'report_reportstrategyproximicnotice', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicNotice.imp'
        db.alter_column(u'report_reportstrategyproximicnotice', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicNotice.winbid'
        db.alter_column(u'report_reportstrategyproximicnotice', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicMaturity.bids_lost'
        db.alter_column(u'report_reportadvertproximicmaturity', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicMaturity.conv'
        db.alter_column(u'report_reportadvertproximicmaturity', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicMaturity.clk'
        db.alter_column(u'report_reportadvertproximicmaturity', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicMaturity.bid'
        db.alter_column(u'report_reportadvertproximicmaturity', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicMaturity.imp'
        db.alter_column(u'report_reportadvertproximicmaturity', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertProximicMaturity.winbid'
        db.alter_column(u'report_reportadvertproximicmaturity', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCarrier.bids_lost'
        db.alter_column(u'report_reportadvertcarrier', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCarrier.conv'
        db.alter_column(u'report_reportadvertcarrier', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCarrier.clk'
        db.alter_column(u'report_reportadvertcarrier', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCarrier.bid'
        db.alter_column(u'report_reportadvertcarrier', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCarrier.imp'
        db.alter_column(u'report_reportadvertcarrier', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertCarrier.winbid'
        db.alter_column(u'report_reportadvertcarrier', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicContext.bids_lost'
        db.alter_column(u'report_reportstrategyproximiccontext', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicContext.conv'
        db.alter_column(u'report_reportstrategyproximiccontext', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicContext.clk'
        db.alter_column(u'report_reportstrategyproximiccontext', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicContext.bid'
        db.alter_column(u'report_reportstrategyproximiccontext', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicContext.imp'
        db.alter_column(u'report_reportstrategyproximiccontext', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicContext.winbid'
        db.alter_column(u'report_reportstrategyproximiccontext', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicLanguage.bids_lost'
        db.alter_column(u'report_reportstrategyproximiclanguage', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicLanguage.conv'
        db.alter_column(u'report_reportstrategyproximiclanguage', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicLanguage.clk'
        db.alter_column(u'report_reportstrategyproximiclanguage', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicLanguage.bid'
        db.alter_column(u'report_reportstrategyproximiclanguage', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicLanguage.imp'
        db.alter_column(u'report_reportstrategyproximiclanguage', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyProximicLanguage.winbid'
        db.alter_column(u'report_reportstrategyproximiclanguage', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPosition.bids_lost'
        db.alter_column(u'report_reportstrategyposition', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPosition.conv'
        db.alter_column(u'report_reportstrategyposition', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPosition.clk'
        db.alter_column(u'report_reportstrategyposition', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPosition.bid'
        db.alter_column(u'report_reportstrategyposition', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPosition.imp'
        db.alter_column(u'report_reportstrategyposition', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPosition.winbid'
        db.alter_column(u'report_reportstrategyposition', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Brand.bids_lost'
        db.alter_column(u'report_reportstrategypeer39brand', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Brand.conv'
        db.alter_column(u'report_reportstrategypeer39brand', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Brand.clk'
        db.alter_column(u'report_reportstrategypeer39brand', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Brand.bid'
        db.alter_column(u'report_reportstrategypeer39brand', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Brand.imp'
        db.alter_column(u'report_reportstrategypeer39brand', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategyPeer39Brand.winbid'
        db.alter_column(u'report_reportstrategypeer39brand', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategySite.bids_lost'
        db.alter_column(u'report_reportstrategysite', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategySite.conv'
        db.alter_column(u'report_reportstrategysite', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategySite.clk'
        db.alter_column(u'report_reportstrategysite', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategySite.bid'
        db.alter_column(u'report_reportstrategysite', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategySite.imp'
        db.alter_column(u'report_reportstrategysite', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportStrategySite.winbid'
        db.alter_column(u'report_reportstrategysite', 'winbid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertModel.bids_lost'
        db.alter_column(u'report_reportadvertmodel', 'bids_lost', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertModel.conv'
        db.alter_column(u'report_reportadvertmodel', 'conv', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertModel.clk'
        db.alter_column(u'report_reportadvertmodel', 'clk', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertModel.bid'
        db.alter_column(u'report_reportadvertmodel', 'bid', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertModel.imp'
        db.alter_column(u'report_reportadvertmodel', 'imp', self.gf('ui.fields.BigDecimalField')())

        # Changing field 'ReportAdvertModel.winbid'
        db.alter_column(u'report_reportadvertmodel', 'winbid', self.gf('ui.fields.BigDecimalField')())

    def backwards(self, orm):

        # Changing field 'ReportStrategyAge.bids_lost'
        db.alter_column(u'report_reportstrategyage', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyAge.conv'
        db.alter_column(u'report_reportstrategyage', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyAge.clk'
        db.alter_column(u'report_reportstrategyage', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyAge.bid'
        db.alter_column(u'report_reportstrategyage', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyAge.imp'
        db.alter_column(u'report_reportstrategyage', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyAge.winbid'
        db.alter_column(u'report_reportstrategyage', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyOsVersion.bids_lost'
        db.alter_column(u'report_reportstrategyosversion', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyOsVersion.conv'
        db.alter_column(u'report_reportstrategyosversion', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyOsVersion.clk'
        db.alter_column(u'report_reportstrategyosversion', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyOsVersion.bid'
        db.alter_column(u'report_reportstrategyosversion', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyOsVersion.imp'
        db.alter_column(u'report_reportstrategyosversion', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyOsVersion.winbid'
        db.alter_column(u'report_reportstrategyosversion', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicSafety.bids_lost'
        db.alter_column(u'report_reportadvertproximicsafety', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicSafety.conv'
        db.alter_column(u'report_reportadvertproximicsafety', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicSafety.clk'
        db.alter_column(u'report_reportadvertproximicsafety', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicSafety.bid'
        db.alter_column(u'report_reportadvertproximicsafety', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicSafety.imp'
        db.alter_column(u'report_reportadvertproximicsafety', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicSafety.winbid'
        db.alter_column(u'report_reportadvertproximicsafety', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPublisherNetwork.bids_lost'
        db.alter_column(u'report_reportstrategypublishernetwork', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPublisherNetwork.conv'
        db.alter_column(u'report_reportstrategypublishernetwork', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPublisherNetwork.clk'
        db.alter_column(u'report_reportstrategypublishernetwork', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPublisherNetwork.bid'
        db.alter_column(u'report_reportstrategypublishernetwork', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPublisherNetwork.imp'
        db.alter_column(u'report_reportstrategypublishernetwork', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPublisherNetwork.winbid'
        db.alter_column(u'report_reportstrategypublishernetwork', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Language.bids_lost'
        db.alter_column(u'report_reportstrategypeer39language', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Language.conv'
        db.alter_column(u'report_reportstrategypeer39language', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPeer39Language.clk'
        db.alter_column(u'report_reportstrategypeer39language', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPeer39Language.bid'
        db.alter_column(u'report_reportstrategypeer39language', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Language.imp'
        db.alter_column(u'report_reportstrategypeer39language', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Language.winbid'
        db.alter_column(u'report_reportstrategypeer39language', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCountry.bids_lost'
        db.alter_column(u'report_reportadvertcountry', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCountry.conv'
        db.alter_column(u'report_reportadvertcountry', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertCountry.clk'
        db.alter_column(u'report_reportadvertcountry', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertCountry.bid'
        db.alter_column(u'report_reportadvertcountry', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCountry.imp'
        db.alter_column(u'report_reportadvertcountry', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCountry.winbid'
        db.alter_column(u'report_reportadvertcountry', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicContextual.bids_lost'
        db.alter_column(u'report_reportadvertproximiccontextual', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicContextual.conv'
        db.alter_column(u'report_reportadvertproximiccontextual', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicContextual.clk'
        db.alter_column(u'report_reportadvertproximiccontextual', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicContextual.bid'
        db.alter_column(u'report_reportadvertproximiccontextual', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicContextual.imp'
        db.alter_column(u'report_reportadvertproximiccontextual', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicContextual.winbid'
        db.alter_column(u'report_reportadvertproximiccontextual', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCity.bids_lost'
        db.alter_column(u'report_reportstrategycity', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCity.conv'
        db.alter_column(u'report_reportstrategycity', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyCity.clk'
        db.alter_column(u'report_reportstrategycity', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyCity.bid'
        db.alter_column(u'report_reportstrategycity', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCity.imp'
        db.alter_column(u'report_reportstrategycity', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCity.winbid'
        db.alter_column(u'report_reportstrategycity', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPosition.bids_lost'
        db.alter_column(u'report_reportadvertposition', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPosition.conv'
        db.alter_column(u'report_reportadvertposition', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPosition.clk'
        db.alter_column(u'report_reportadvertposition', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPosition.bid'
        db.alter_column(u'report_reportadvertposition', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPosition.imp'
        db.alter_column(u'report_reportadvertposition', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPosition.winbid'
        db.alter_column(u'report_reportadvertposition', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCategory.bids_lost'
        db.alter_column(u'report_reportstrategycategory', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCategory.conv'
        db.alter_column(u'report_reportstrategycategory', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyCategory.clk'
        db.alter_column(u'report_reportstrategycategory', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyCategory.bid'
        db.alter_column(u'report_reportstrategycategory', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCategory.imp'
        db.alter_column(u'report_reportstrategycategory', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCategory.winbid'
        db.alter_column(u'report_reportstrategycategory', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertOsVersion.bids_lost'
        db.alter_column(u'report_reportadvertosversion', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertOsVersion.conv'
        db.alter_column(u'report_reportadvertosversion', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertOsVersion.clk'
        db.alter_column(u'report_reportadvertosversion', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertOsVersion.bid'
        db.alter_column(u'report_reportadvertosversion', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertOsVersion.imp'
        db.alter_column(u'report_reportadvertosversion', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertOsVersion.winbid'
        db.alter_column(u'report_reportadvertosversion', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicQuality.bids_lost'
        db.alter_column(u'report_reportstrategyproximicquality', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicQuality.conv'
        db.alter_column(u'report_reportstrategyproximicquality', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicQuality.clk'
        db.alter_column(u'report_reportstrategyproximicquality', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicQuality.bid'
        db.alter_column(u'report_reportstrategyproximicquality', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicQuality.imp'
        db.alter_column(u'report_reportstrategyproximicquality', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicQuality.winbid'
        db.alter_column(u'report_reportstrategyproximicquality', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyOs.bids_lost'
        db.alter_column(u'report_reportstrategyos', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyOs.conv'
        db.alter_column(u'report_reportstrategyos', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyOs.clk'
        db.alter_column(u'report_reportstrategyos', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyOs.bid'
        db.alter_column(u'report_reportstrategyos', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyOs.imp'
        db.alter_column(u'report_reportstrategyos', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyOs.winbid'
        db.alter_column(u'report_reportstrategyos', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicQuality.bids_lost'
        db.alter_column(u'report_reportadvertproximicquality', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicQuality.conv'
        db.alter_column(u'report_reportadvertproximicquality', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicQuality.clk'
        db.alter_column(u'report_reportadvertproximicquality', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicQuality.bid'
        db.alter_column(u'report_reportadvertproximicquality', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicQuality.imp'
        db.alter_column(u'report_reportadvertproximicquality', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicQuality.winbid'
        db.alter_column(u'report_reportadvertproximicquality', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyRegion.bids_lost'
        db.alter_column(u'report_reportstrategyregion', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyRegion.conv'
        db.alter_column(u'report_reportstrategyregion', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyRegion.clk'
        db.alter_column(u'report_reportstrategyregion', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyRegion.bid'
        db.alter_column(u'report_reportstrategyregion', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyRegion.imp'
        db.alter_column(u'report_reportstrategyregion', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyRegion.winbid'
        db.alter_column(u'report_reportstrategyregion', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicPlace.bids_lost'
        db.alter_column(u'report_reportstrategyproximicplace', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicPlace.conv'
        db.alter_column(u'report_reportstrategyproximicplace', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicPlace.clk'
        db.alter_column(u'report_reportstrategyproximicplace', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicPlace.bid'
        db.alter_column(u'report_reportstrategyproximicplace', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicPlace.imp'
        db.alter_column(u'report_reportstrategyproximicplace', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicPlace.winbid'
        db.alter_column(u'report_reportstrategyproximicplace', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertMake.bids_lost'
        db.alter_column(u'report_reportadvertmake', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertMake.conv'
        db.alter_column(u'report_reportadvertmake', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertMake.clk'
        db.alter_column(u'report_reportadvertmake', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertMake.bid'
        db.alter_column(u'report_reportadvertmake', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertMake.imp'
        db.alter_column(u'report_reportadvertmake', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertMake.winbid'
        db.alter_column(u'report_reportadvertmake', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicLanguage.bids_lost'
        db.alter_column(u'report_reportadvertproximiclanguage', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicLanguage.conv'
        db.alter_column(u'report_reportadvertproximiclanguage', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicLanguage.clk'
        db.alter_column(u'report_reportadvertproximiclanguage', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicLanguage.bid'
        db.alter_column(u'report_reportadvertproximiclanguage', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicLanguage.imp'
        db.alter_column(u'report_reportadvertproximiclanguage', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicLanguage.winbid'
        db.alter_column(u'report_reportadvertproximiclanguage', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Brand.bids_lost'
        db.alter_column(u'report_reportadvertpeer39brand', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Brand.conv'
        db.alter_column(u'report_reportadvertpeer39brand', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPeer39Brand.clk'
        db.alter_column(u'report_reportadvertpeer39brand', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPeer39Brand.bid'
        db.alter_column(u'report_reportadvertpeer39brand', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Brand.imp'
        db.alter_column(u'report_reportadvertpeer39brand', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Brand.winbid'
        db.alter_column(u'report_reportadvertpeer39brand', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCountry.bids_lost'
        db.alter_column(u'report_reportstrategycountry', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCountry.conv'
        db.alter_column(u'report_reportstrategycountry', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyCountry.clk'
        db.alter_column(u'report_reportstrategycountry', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyCountry.bid'
        db.alter_column(u'report_reportstrategycountry', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCountry.imp'
        db.alter_column(u'report_reportstrategycountry', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCountry.winbid'
        db.alter_column(u'report_reportstrategycountry', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPublisher.bids_lost'
        db.alter_column(u'report_reportadvertpublisher', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPublisher.conv'
        db.alter_column(u'report_reportadvertpublisher', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPublisher.clk'
        db.alter_column(u'report_reportadvertpublisher', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPublisher.bid'
        db.alter_column(u'report_reportadvertpublisher', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPublisher.imp'
        db.alter_column(u'report_reportadvertpublisher', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPublisher.winbid'
        db.alter_column(u'report_reportadvertpublisher', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Quality.bids_lost'
        db.alter_column(u'report_reportadvertpeer39quality', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Quality.conv'
        db.alter_column(u'report_reportadvertpeer39quality', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPeer39Quality.clk'
        db.alter_column(u'report_reportadvertpeer39quality', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPeer39Quality.bid'
        db.alter_column(u'report_reportadvertpeer39quality', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Quality.imp'
        db.alter_column(u'report_reportadvertpeer39quality', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Quality.winbid'
        db.alter_column(u'report_reportadvertpeer39quality', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Contextual.bids_lost'
        db.alter_column(u'report_reportstrategypeer39contextual', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Contextual.conv'
        db.alter_column(u'report_reportstrategypeer39contextual', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPeer39Contextual.clk'
        db.alter_column(u'report_reportstrategypeer39contextual', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPeer39Contextual.bid'
        db.alter_column(u'report_reportstrategypeer39contextual', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Contextual.imp'
        db.alter_column(u'report_reportstrategypeer39contextual', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Contextual.winbid'
        db.alter_column(u'report_reportstrategypeer39contextual', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyDomain.bids_lost'
        db.alter_column(u'report_reportstrategydomain', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyDomain.conv'
        db.alter_column(u'report_reportstrategydomain', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyDomain.clk'
        db.alter_column(u'report_reportstrategydomain', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyDomain.bid'
        db.alter_column(u'report_reportstrategydomain', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyDomain.imp'
        db.alter_column(u'report_reportstrategydomain', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyDomain.winbid'
        db.alter_column(u'report_reportstrategydomain', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Language.bids_lost'
        db.alter_column(u'report_reportadvertpeer39language', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Language.conv'
        db.alter_column(u'report_reportadvertpeer39language', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPeer39Language.clk'
        db.alter_column(u'report_reportadvertpeer39language', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPeer39Language.bid'
        db.alter_column(u'report_reportadvertpeer39language', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Language.imp'
        db.alter_column(u'report_reportadvertpeer39language', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Language.winbid'
        db.alter_column(u'report_reportadvertpeer39language', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyMake.bids_lost'
        db.alter_column(u'report_reportstrategymake', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyMake.conv'
        db.alter_column(u'report_reportstrategymake', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyMake.clk'
        db.alter_column(u'report_reportstrategymake', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyMake.bid'
        db.alter_column(u'report_reportstrategymake', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyMake.imp'
        db.alter_column(u'report_reportstrategymake', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyMake.winbid'
        db.alter_column(u'report_reportstrategymake', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertSite.bids_lost'
        db.alter_column(u'report_reportadvertsite', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertSite.conv'
        db.alter_column(u'report_reportadvertsite', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertSite.clk'
        db.alter_column(u'report_reportadvertsite', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertSite.bid'
        db.alter_column(u'report_reportadvertsite', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertSite.imp'
        db.alter_column(u'report_reportadvertsite', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertSite.winbid'
        db.alter_column(u'report_reportadvertsite', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertAge.bids_lost'
        db.alter_column(u'report_reportadvertage', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertAge.conv'
        db.alter_column(u'report_reportadvertage', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertAge.clk'
        db.alter_column(u'report_reportadvertage', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertAge.bid'
        db.alter_column(u'report_reportadvertage', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertAge.imp'
        db.alter_column(u'report_reportadvertage', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertAge.winbid'
        db.alter_column(u'report_reportadvertage', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategy.bids_lost'
        db.alter_column(u'report_reportstrategy', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategy.conv'
        db.alter_column(u'report_reportstrategy', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategy.clk'
        db.alter_column(u'report_reportstrategy', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategy.bid'
        db.alter_column(u'report_reportstrategy', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategy.imp'
        db.alter_column(u'report_reportstrategy', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategy.winbid'
        db.alter_column(u'report_reportstrategy', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyGender.bids_lost'
        db.alter_column(u'report_reportstrategygender', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyGender.conv'
        db.alter_column(u'report_reportstrategygender', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyGender.clk'
        db.alter_column(u'report_reportstrategygender', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyGender.bid'
        db.alter_column(u'report_reportstrategygender', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyGender.imp'
        db.alter_column(u'report_reportstrategygender', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyGender.winbid'
        db.alter_column(u'report_reportstrategygender', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCity.bids_lost'
        db.alter_column(u'report_reportadvertcity', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCity.conv'
        db.alter_column(u'report_reportadvertcity', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertCity.clk'
        db.alter_column(u'report_reportadvertcity', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertCity.bid'
        db.alter_column(u'report_reportadvertcity', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCity.imp'
        db.alter_column(u'report_reportadvertcity', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCity.winbid'
        db.alter_column(u'report_reportadvertcity', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvert.bids_lost'
        db.alter_column(u'report_reportadvert', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvert.conv'
        db.alter_column(u'report_reportadvert', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvert.clk'
        db.alter_column(u'report_reportadvert', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvert.bid'
        db.alter_column(u'report_reportadvert', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvert.imp'
        db.alter_column(u'report_reportadvert', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvert.winbid'
        db.alter_column(u'report_reportadvert', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertRegion.bids_lost'
        db.alter_column(u'report_reportadvertregion', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertRegion.conv'
        db.alter_column(u'report_reportadvertregion', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertRegion.clk'
        db.alter_column(u'report_reportadvertregion', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertRegion.bid'
        db.alter_column(u'report_reportadvertregion', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertRegion.imp'
        db.alter_column(u'report_reportadvertregion', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertRegion.winbid'
        db.alter_column(u'report_reportadvertregion', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertGender.bids_lost'
        db.alter_column(u'report_reportadvertgender', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertGender.conv'
        db.alter_column(u'report_reportadvertgender', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertGender.clk'
        db.alter_column(u'report_reportadvertgender', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertGender.bid'
        db.alter_column(u'report_reportadvertgender', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertGender.imp'
        db.alter_column(u'report_reportadvertgender', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertGender.winbid'
        db.alter_column(u'report_reportadvertgender', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Contextual.bids_lost'
        db.alter_column(u'report_reportadvertpeer39contextual', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Contextual.conv'
        db.alter_column(u'report_reportadvertpeer39contextual', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPeer39Contextual.clk'
        db.alter_column(u'report_reportadvertpeer39contextual', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPeer39Contextual.bid'
        db.alter_column(u'report_reportadvertpeer39contextual', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Contextual.imp'
        db.alter_column(u'report_reportadvertpeer39contextual', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPeer39Contextual.winbid'
        db.alter_column(u'report_reportadvertpeer39contextual', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCarrier.bids_lost'
        db.alter_column(u'report_reportstrategycarrier', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCarrier.conv'
        db.alter_column(u'report_reportstrategycarrier', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyCarrier.clk'
        db.alter_column(u'report_reportstrategycarrier', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyCarrier.bid'
        db.alter_column(u'report_reportstrategycarrier', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCarrier.imp'
        db.alter_column(u'report_reportstrategycarrier', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyCarrier.winbid'
        db.alter_column(u'report_reportstrategycarrier', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicNotice.bids_lost'
        db.alter_column(u'report_reportadvertproximicnotice', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicNotice.conv'
        db.alter_column(u'report_reportadvertproximicnotice', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicNotice.clk'
        db.alter_column(u'report_reportadvertproximicnotice', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicNotice.bid'
        db.alter_column(u'report_reportadvertproximicnotice', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicNotice.imp'
        db.alter_column(u'report_reportadvertproximicnotice', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicNotice.winbid'
        db.alter_column(u'report_reportadvertproximicnotice', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCategory.bids_lost'
        db.alter_column(u'report_reportadvertcategory', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCategory.conv'
        db.alter_column(u'report_reportadvertcategory', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertCategory.clk'
        db.alter_column(u'report_reportadvertcategory', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertCategory.bid'
        db.alter_column(u'report_reportadvertcategory', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCategory.imp'
        db.alter_column(u'report_reportadvertcategory', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCategory.winbid'
        db.alter_column(u'report_reportadvertcategory', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicSafety.bids_lost'
        db.alter_column(u'report_reportstrategyproximicsafety', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicSafety.conv'
        db.alter_column(u'report_reportstrategyproximicsafety', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicSafety.clk'
        db.alter_column(u'report_reportstrategyproximicsafety', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicSafety.bid'
        db.alter_column(u'report_reportstrategyproximicsafety', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicSafety.imp'
        db.alter_column(u'report_reportstrategyproximicsafety', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicSafety.winbid'
        db.alter_column(u'report_reportstrategyproximicsafety', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicPlace.bids_lost'
        db.alter_column(u'report_reportadvertproximicplace', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicPlace.conv'
        db.alter_column(u'report_reportadvertproximicplace', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicPlace.clk'
        db.alter_column(u'report_reportadvertproximicplace', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicPlace.bid'
        db.alter_column(u'report_reportadvertproximicplace', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicPlace.imp'
        db.alter_column(u'report_reportadvertproximicplace', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicPlace.winbid'
        db.alter_column(u'report_reportadvertproximicplace', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPublisher.bids_lost'
        db.alter_column(u'report_reportstrategypublisher', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPublisher.conv'
        db.alter_column(u'report_reportstrategypublisher', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPublisher.clk'
        db.alter_column(u'report_reportstrategypublisher', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPublisher.bid'
        db.alter_column(u'report_reportstrategypublisher', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPublisher.imp'
        db.alter_column(u'report_reportstrategypublisher', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPublisher.winbid'
        db.alter_column(u'report_reportstrategypublisher', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicMaturity.bids_lost'
        db.alter_column(u'report_reportstrategyproximicmaturity', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicMaturity.conv'
        db.alter_column(u'report_reportstrategyproximicmaturity', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicMaturity.clk'
        db.alter_column(u'report_reportstrategyproximicmaturity', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicMaturity.bid'
        db.alter_column(u'report_reportstrategyproximicmaturity', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicMaturity.imp'
        db.alter_column(u'report_reportstrategyproximicmaturity', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicMaturity.winbid'
        db.alter_column(u'report_reportstrategyproximicmaturity', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertOs.bids_lost'
        db.alter_column(u'report_reportadvertos', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertOs.conv'
        db.alter_column(u'report_reportadvertos', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertOs.clk'
        db.alter_column(u'report_reportadvertos', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertOs.bid'
        db.alter_column(u'report_reportadvertos', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertOs.imp'
        db.alter_column(u'report_reportadvertos', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertOs.winbid'
        db.alter_column(u'report_reportadvertos', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertDomain.bids_lost'
        db.alter_column(u'report_reportadvertdomain', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertDomain.conv'
        db.alter_column(u'report_reportadvertdomain', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertDomain.clk'
        db.alter_column(u'report_reportadvertdomain', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertDomain.bid'
        db.alter_column(u'report_reportadvertdomain', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertDomain.imp'
        db.alter_column(u'report_reportadvertdomain', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertDomain.winbid'
        db.alter_column(u'report_reportadvertdomain', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyModel.bids_lost'
        db.alter_column(u'report_reportstrategymodel', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyModel.conv'
        db.alter_column(u'report_reportstrategymodel', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyModel.clk'
        db.alter_column(u'report_reportstrategymodel', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyModel.bid'
        db.alter_column(u'report_reportstrategymodel', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyModel.imp'
        db.alter_column(u'report_reportstrategymodel', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyModel.winbid'
        db.alter_column(u'report_reportstrategymodel', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPublisherNetwork.bids_lost'
        db.alter_column(u'report_reportadvertpublishernetwork', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPublisherNetwork.conv'
        db.alter_column(u'report_reportadvertpublishernetwork', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPublisherNetwork.clk'
        db.alter_column(u'report_reportadvertpublishernetwork', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertPublisherNetwork.bid'
        db.alter_column(u'report_reportadvertpublishernetwork', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPublisherNetwork.imp'
        db.alter_column(u'report_reportadvertpublishernetwork', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertPublisherNetwork.winbid'
        db.alter_column(u'report_reportadvertpublishernetwork', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Quality.bids_lost'
        db.alter_column(u'report_reportstrategypeer39quality', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Quality.conv'
        db.alter_column(u'report_reportstrategypeer39quality', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPeer39Quality.clk'
        db.alter_column(u'report_reportstrategypeer39quality', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPeer39Quality.bid'
        db.alter_column(u'report_reportstrategypeer39quality', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Quality.imp'
        db.alter_column(u'report_reportstrategypeer39quality', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Quality.winbid'
        db.alter_column(u'report_reportstrategypeer39quality', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicNotice.bids_lost'
        db.alter_column(u'report_reportstrategyproximicnotice', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicNotice.conv'
        db.alter_column(u'report_reportstrategyproximicnotice', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicNotice.clk'
        db.alter_column(u'report_reportstrategyproximicnotice', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicNotice.bid'
        db.alter_column(u'report_reportstrategyproximicnotice', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicNotice.imp'
        db.alter_column(u'report_reportstrategyproximicnotice', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicNotice.winbid'
        db.alter_column(u'report_reportstrategyproximicnotice', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicMaturity.bids_lost'
        db.alter_column(u'report_reportadvertproximicmaturity', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicMaturity.conv'
        db.alter_column(u'report_reportadvertproximicmaturity', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicMaturity.clk'
        db.alter_column(u'report_reportadvertproximicmaturity', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertProximicMaturity.bid'
        db.alter_column(u'report_reportadvertproximicmaturity', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicMaturity.imp'
        db.alter_column(u'report_reportadvertproximicmaturity', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertProximicMaturity.winbid'
        db.alter_column(u'report_reportadvertproximicmaturity', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCarrier.bids_lost'
        db.alter_column(u'report_reportadvertcarrier', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCarrier.conv'
        db.alter_column(u'report_reportadvertcarrier', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertCarrier.clk'
        db.alter_column(u'report_reportadvertcarrier', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertCarrier.bid'
        db.alter_column(u'report_reportadvertcarrier', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCarrier.imp'
        db.alter_column(u'report_reportadvertcarrier', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertCarrier.winbid'
        db.alter_column(u'report_reportadvertcarrier', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicContext.bids_lost'
        db.alter_column(u'report_reportstrategyproximiccontext', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicContext.conv'
        db.alter_column(u'report_reportstrategyproximiccontext', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicContext.clk'
        db.alter_column(u'report_reportstrategyproximiccontext', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicContext.bid'
        db.alter_column(u'report_reportstrategyproximiccontext', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicContext.imp'
        db.alter_column(u'report_reportstrategyproximiccontext', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicContext.winbid'
        db.alter_column(u'report_reportstrategyproximiccontext', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicLanguage.bids_lost'
        db.alter_column(u'report_reportstrategyproximiclanguage', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicLanguage.conv'
        db.alter_column(u'report_reportstrategyproximiclanguage', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicLanguage.clk'
        db.alter_column(u'report_reportstrategyproximiclanguage', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyProximicLanguage.bid'
        db.alter_column(u'report_reportstrategyproximiclanguage', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicLanguage.imp'
        db.alter_column(u'report_reportstrategyproximiclanguage', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyProximicLanguage.winbid'
        db.alter_column(u'report_reportstrategyproximiclanguage', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPosition.bids_lost'
        db.alter_column(u'report_reportstrategyposition', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPosition.conv'
        db.alter_column(u'report_reportstrategyposition', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPosition.clk'
        db.alter_column(u'report_reportstrategyposition', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPosition.bid'
        db.alter_column(u'report_reportstrategyposition', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPosition.imp'
        db.alter_column(u'report_reportstrategyposition', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPosition.winbid'
        db.alter_column(u'report_reportstrategyposition', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Brand.bids_lost'
        db.alter_column(u'report_reportstrategypeer39brand', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Brand.conv'
        db.alter_column(u'report_reportstrategypeer39brand', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPeer39Brand.clk'
        db.alter_column(u'report_reportstrategypeer39brand', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategyPeer39Brand.bid'
        db.alter_column(u'report_reportstrategypeer39brand', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Brand.imp'
        db.alter_column(u'report_reportstrategypeer39brand', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategyPeer39Brand.winbid'
        db.alter_column(u'report_reportstrategypeer39brand', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategySite.bids_lost'
        db.alter_column(u'report_reportstrategysite', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategySite.conv'
        db.alter_column(u'report_reportstrategysite', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategySite.clk'
        db.alter_column(u'report_reportstrategysite', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportStrategySite.bid'
        db.alter_column(u'report_reportstrategysite', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategySite.imp'
        db.alter_column(u'report_reportstrategysite', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportStrategySite.winbid'
        db.alter_column(u'report_reportstrategysite', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertModel.bids_lost'
        db.alter_column(u'report_reportadvertmodel', 'bids_lost', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertModel.conv'
        db.alter_column(u'report_reportadvertmodel', 'conv', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertModel.clk'
        db.alter_column(u'report_reportadvertmodel', 'clk', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ReportAdvertModel.bid'
        db.alter_column(u'report_reportadvertmodel', 'bid', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertModel.imp'
        db.alter_column(u'report_reportadvertmodel', 'imp', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'ReportAdvertModel.winbid'
        db.alter_column(u'report_reportadvertmodel', 'winbid', self.gf('django.db.models.fields.BigIntegerField')())

    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'account_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'commission': ('django.db.models.fields.SmallIntegerField', [], {'default': "'10'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '40'})
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
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertAge'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_age'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertcarrier': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertCarrier'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_carrier'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertcategory': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertCategory'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_category'", 'null': 'True', 'to': u"orm['targeting.ContentCategoryValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertcity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertCity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_city'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertcountry': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertCountry'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_country'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertdomain': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertDomain'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_domain'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertgender': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertGender'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_gender'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertmake': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertMake'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_make'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertmodel': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertModel'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_model'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertos': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertOs'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_os'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertosversion': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertOsVersion'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_os_version'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertpeer39brand': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertPeer39Brand'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_brandprotection'", 'null': 'True', 'to': u"orm['targeting.Peer39BrandProtection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertpeer39contextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertPeer39Contextual'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_contextual'", 'null': 'True', 'to': u"orm['targeting.Peer39ContextualSegment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertpeer39language': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertPeer39Language'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.Peer39PageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertpeer39quality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertPeer39Quality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_pagequality'", 'null': 'True', 'to': u"orm['targeting.Peer39PageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertposition': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertPosition'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_position'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertproximiccontextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertProximicContextual'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_contextual'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertproximiclanguage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertProximicLanguage'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertproximicmaturity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertProximicMaturity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_maturity'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicMaturityRating']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertproximicnotice': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertProximicNotice'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_pagenoticeability'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertproximicplace': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertProximicPlace'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_pageplacement'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertproximicquality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertProximicQuality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_pagequality'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertproximicsafety': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertProximicSafety'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_safety'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicSafetyLevel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertpublisher': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertPublisher'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_publisher'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertpublishernetwork': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertPublisherNetwork'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_network'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertregion': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertRegion'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_advert_region'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportadvertsite': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportAdvertSite'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategy': {
            'Meta': {'unique_together': "(('related', 'time'),)", 'object_name': 'ReportStrategy'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategyage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyAge'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_age'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategycarrier': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCarrier'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_carrier'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategycategory': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCategory'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_category'", 'null': 'True', 'to': u"orm['targeting.ContentCategoryValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategycity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_city'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategycountry': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCountry'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_country'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategydomain': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyDomain'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_domain'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategygender': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyGender'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_gender'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategymake': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyMake'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_make'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategymodel': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyModel'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_model'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategyos': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyOs'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_os'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategyosversion': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyOsVersion'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_os_version'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategypeer39brand': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Brand'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_brandprotection'", 'null': 'True', 'to': u"orm['targeting.Peer39BrandProtection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategypeer39contextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Contextual'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_contextual'", 'null': 'True', 'to': u"orm['targeting.Peer39ContextualSegment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategypeer39language': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Language'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.Peer39PageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategypeer39quality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Quality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagequality'", 'null': 'True', 'to': u"orm['targeting.Peer39PageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategyposition': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPosition'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_position'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategyproximiccontext': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicContext'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_contextual'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategyproximiclanguage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicLanguage'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategyproximicmaturity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicMaturity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_maturity'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicMaturityRating']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategyproximicnotice': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicNotice'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagenoticeability'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategyproximicplace': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicPlace'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pageplacement'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategyproximicquality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicQuality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagequality'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategyproximicsafety': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicSafety'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_safety'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicSafetyLevel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategypublisher': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPublisher'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_publisher'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategypublishernetwork': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPublisherNetwork'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_network'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategyregion': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyRegion'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_region'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportstrategysite': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategySite'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
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