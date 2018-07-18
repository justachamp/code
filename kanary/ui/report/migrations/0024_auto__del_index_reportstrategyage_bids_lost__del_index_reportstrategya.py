# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing index on 'ReportStrategyAge', fields ['bids_lost']
        db.delete_index(u'report_reportstrategyage', ['bids_lost'])

        # Removing index on 'ReportStrategyAge', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategyage', ['data_cost_value'])

        # Removing index on 'ReportStrategyAge', fields ['conv']
        db.delete_index(u'report_reportstrategyage', ['conv'])

        # Removing index on 'ReportStrategyAge', fields ['clk']
        db.delete_index(u'report_reportstrategyage', ['clk'])

        # Removing index on 'ReportStrategyAge', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategyage', ['winbid_value_total'])

        # Removing index on 'ReportStrategyAge', fields ['bid']
        db.delete_index(u'report_reportstrategyage', ['bid'])

        # Removing index on 'ReportStrategyAge', fields ['conv_value']
        db.delete_index(u'report_reportstrategyage', ['conv_value'])

        # Removing index on 'ReportStrategyAge', fields ['bid_value']
        db.delete_index(u'report_reportstrategyage', ['bid_value'])

        # Removing index on 'ReportStrategyAge', fields ['imp']
        db.delete_index(u'report_reportstrategyage', ['imp'])

        # Removing index on 'ReportStrategyAge', fields ['commission_value']
        db.delete_index(u'report_reportstrategyage', ['commission_value'])

        # Removing index on 'ReportStrategyAge', fields ['winbid']
        db.delete_index(u'report_reportstrategyage', ['winbid'])

        # Removing index on 'ReportStrategyAge', fields ['winbid_value']
        db.delete_index(u'report_reportstrategyage', ['winbid_value'])

        # Removing index on 'ReportStrategyAge', fields ['net_earned']
        db.delete_index(u'report_reportstrategyage', ['net_earned'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['bids_lost']
        db.delete_index(u'report_reportstrategypublishernetwork', ['bids_lost'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategypublishernetwork', ['data_cost_value'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['conv']
        db.delete_index(u'report_reportstrategypublishernetwork', ['conv'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['clk']
        db.delete_index(u'report_reportstrategypublishernetwork', ['clk'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategypublishernetwork', ['winbid_value_total'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['bid']
        db.delete_index(u'report_reportstrategypublishernetwork', ['bid'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['conv_value']
        db.delete_index(u'report_reportstrategypublishernetwork', ['conv_value'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['bid_value']
        db.delete_index(u'report_reportstrategypublishernetwork', ['bid_value'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['imp']
        db.delete_index(u'report_reportstrategypublishernetwork', ['imp'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['commission_value']
        db.delete_index(u'report_reportstrategypublishernetwork', ['commission_value'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['winbid']
        db.delete_index(u'report_reportstrategypublishernetwork', ['winbid'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['winbid_value']
        db.delete_index(u'report_reportstrategypublishernetwork', ['winbid_value'])

        # Removing index on 'ReportStrategyPublisherNetwork', fields ['net_earned']
        db.delete_index(u'report_reportstrategypublishernetwork', ['net_earned'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['bids_lost']
        db.delete_index(u'report_reportstrategypeer39language', ['bids_lost'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategypeer39language', ['data_cost_value'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['conv']
        db.delete_index(u'report_reportstrategypeer39language', ['conv'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['clk']
        db.delete_index(u'report_reportstrategypeer39language', ['clk'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategypeer39language', ['winbid_value_total'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['bid']
        db.delete_index(u'report_reportstrategypeer39language', ['bid'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['conv_value']
        db.delete_index(u'report_reportstrategypeer39language', ['conv_value'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['bid_value']
        db.delete_index(u'report_reportstrategypeer39language', ['bid_value'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['imp']
        db.delete_index(u'report_reportstrategypeer39language', ['imp'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['commission_value']
        db.delete_index(u'report_reportstrategypeer39language', ['commission_value'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['winbid']
        db.delete_index(u'report_reportstrategypeer39language', ['winbid'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['winbid_value']
        db.delete_index(u'report_reportstrategypeer39language', ['winbid_value'])

        # Removing index on 'ReportStrategyPeer39Language', fields ['net_earned']
        db.delete_index(u'report_reportstrategypeer39language', ['net_earned'])

        # Removing index on 'ReportCampaignCategory', fields ['bids_lost']
        db.delete_index(u'report_reportcampaigncategory', ['bids_lost'])

        # Removing index on 'ReportCampaignCategory', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaigncategory', ['data_cost_value'])

        # Removing index on 'ReportCampaignCategory', fields ['conv']
        db.delete_index(u'report_reportcampaigncategory', ['conv'])

        # Removing index on 'ReportCampaignCategory', fields ['clk']
        db.delete_index(u'report_reportcampaigncategory', ['clk'])

        # Removing index on 'ReportCampaignCategory', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaigncategory', ['winbid_value_total'])

        # Removing index on 'ReportCampaignCategory', fields ['bid']
        db.delete_index(u'report_reportcampaigncategory', ['bid'])

        # Removing index on 'ReportCampaignCategory', fields ['conv_value']
        db.delete_index(u'report_reportcampaigncategory', ['conv_value'])

        # Removing index on 'ReportCampaignCategory', fields ['bid_value']
        db.delete_index(u'report_reportcampaigncategory', ['bid_value'])

        # Removing index on 'ReportCampaignCategory', fields ['imp']
        db.delete_index(u'report_reportcampaigncategory', ['imp'])

        # Removing index on 'ReportCampaignCategory', fields ['commission_value']
        db.delete_index(u'report_reportcampaigncategory', ['commission_value'])

        # Removing index on 'ReportCampaignCategory', fields ['winbid']
        db.delete_index(u'report_reportcampaigncategory', ['winbid'])

        # Removing index on 'ReportCampaignCategory', fields ['winbid_value']
        db.delete_index(u'report_reportcampaigncategory', ['winbid_value'])

        # Removing index on 'ReportCampaignCategory', fields ['net_earned']
        db.delete_index(u'report_reportcampaigncategory', ['net_earned'])

        # Removing index on 'ReportCampaignDomain', fields ['bids_lost']
        db.delete_index(u'report_reportcampaigndomain', ['bids_lost'])

        # Removing index on 'ReportCampaignDomain', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaigndomain', ['data_cost_value'])

        # Removing index on 'ReportCampaignDomain', fields ['conv']
        db.delete_index(u'report_reportcampaigndomain', ['conv'])

        # Removing index on 'ReportCampaignDomain', fields ['clk']
        db.delete_index(u'report_reportcampaigndomain', ['clk'])

        # Removing index on 'ReportCampaignDomain', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaigndomain', ['winbid_value_total'])

        # Removing index on 'ReportCampaignDomain', fields ['bid']
        db.delete_index(u'report_reportcampaigndomain', ['bid'])

        # Removing index on 'ReportCampaignDomain', fields ['conv_value']
        db.delete_index(u'report_reportcampaigndomain', ['conv_value'])

        # Removing index on 'ReportCampaignDomain', fields ['bid_value']
        db.delete_index(u'report_reportcampaigndomain', ['bid_value'])

        # Removing index on 'ReportCampaignDomain', fields ['imp']
        db.delete_index(u'report_reportcampaigndomain', ['imp'])

        # Removing index on 'ReportCampaignDomain', fields ['commission_value']
        db.delete_index(u'report_reportcampaigndomain', ['commission_value'])

        # Removing index on 'ReportCampaignDomain', fields ['winbid']
        db.delete_index(u'report_reportcampaigndomain', ['winbid'])

        # Removing index on 'ReportCampaignDomain', fields ['winbid_value']
        db.delete_index(u'report_reportcampaigndomain', ['winbid_value'])

        # Removing index on 'ReportCampaignDomain', fields ['net_earned']
        db.delete_index(u'report_reportcampaigndomain', ['net_earned'])

        # Removing index on 'ReportStrategyDomain', fields ['bids_lost']
        db.delete_index(u'report_reportstrategydomain', ['bids_lost'])

        # Removing index on 'ReportStrategyDomain', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategydomain', ['data_cost_value'])

        # Removing index on 'ReportStrategyDomain', fields ['conv']
        db.delete_index(u'report_reportstrategydomain', ['conv'])

        # Removing index on 'ReportStrategyDomain', fields ['clk']
        db.delete_index(u'report_reportstrategydomain', ['clk'])

        # Removing index on 'ReportStrategyDomain', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategydomain', ['winbid_value_total'])

        # Removing index on 'ReportStrategyDomain', fields ['bid']
        db.delete_index(u'report_reportstrategydomain', ['bid'])

        # Removing index on 'ReportStrategyDomain', fields ['conv_value']
        db.delete_index(u'report_reportstrategydomain', ['conv_value'])

        # Removing index on 'ReportStrategyDomain', fields ['bid_value']
        db.delete_index(u'report_reportstrategydomain', ['bid_value'])

        # Removing index on 'ReportStrategyDomain', fields ['imp']
        db.delete_index(u'report_reportstrategydomain', ['imp'])

        # Removing index on 'ReportStrategyDomain', fields ['commission_value']
        db.delete_index(u'report_reportstrategydomain', ['commission_value'])

        # Removing index on 'ReportStrategyDomain', fields ['winbid']
        db.delete_index(u'report_reportstrategydomain', ['winbid'])

        # Removing index on 'ReportStrategyDomain', fields ['winbid_value']
        db.delete_index(u'report_reportstrategydomain', ['winbid_value'])

        # Removing index on 'ReportStrategyDomain', fields ['net_earned']
        db.delete_index(u'report_reportstrategydomain', ['net_earned'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignproximicnotice', ['bids_lost'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignproximicnotice', ['data_cost_value'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['conv']
        db.delete_index(u'report_reportcampaignproximicnotice', ['conv'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['clk']
        db.delete_index(u'report_reportcampaignproximicnotice', ['clk'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignproximicnotice', ['winbid_value_total'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['bid']
        db.delete_index(u'report_reportcampaignproximicnotice', ['bid'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['conv_value']
        db.delete_index(u'report_reportcampaignproximicnotice', ['conv_value'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['bid_value']
        db.delete_index(u'report_reportcampaignproximicnotice', ['bid_value'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['imp']
        db.delete_index(u'report_reportcampaignproximicnotice', ['imp'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['commission_value']
        db.delete_index(u'report_reportcampaignproximicnotice', ['commission_value'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['winbid']
        db.delete_index(u'report_reportcampaignproximicnotice', ['winbid'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignproximicnotice', ['winbid_value'])

        # Removing index on 'ReportCampaignProximicNotice', fields ['net_earned']
        db.delete_index(u'report_reportcampaignproximicnotice', ['net_earned'])

        # Removing index on 'ReportCampaignPosition', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignposition', ['bids_lost'])

        # Removing index on 'ReportCampaignPosition', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignposition', ['data_cost_value'])

        # Removing index on 'ReportCampaignPosition', fields ['conv']
        db.delete_index(u'report_reportcampaignposition', ['conv'])

        # Removing index on 'ReportCampaignPosition', fields ['clk']
        db.delete_index(u'report_reportcampaignposition', ['clk'])

        # Removing index on 'ReportCampaignPosition', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignposition', ['winbid_value_total'])

        # Removing index on 'ReportCampaignPosition', fields ['bid']
        db.delete_index(u'report_reportcampaignposition', ['bid'])

        # Removing index on 'ReportCampaignPosition', fields ['conv_value']
        db.delete_index(u'report_reportcampaignposition', ['conv_value'])

        # Removing index on 'ReportCampaignPosition', fields ['bid_value']
        db.delete_index(u'report_reportcampaignposition', ['bid_value'])

        # Removing index on 'ReportCampaignPosition', fields ['imp']
        db.delete_index(u'report_reportcampaignposition', ['imp'])

        # Removing index on 'ReportCampaignPosition', fields ['commission_value']
        db.delete_index(u'report_reportcampaignposition', ['commission_value'])

        # Removing index on 'ReportCampaignPosition', fields ['winbid']
        db.delete_index(u'report_reportcampaignposition', ['winbid'])

        # Removing index on 'ReportCampaignPosition', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignposition', ['winbid_value'])

        # Removing index on 'ReportCampaignPosition', fields ['net_earned']
        db.delete_index(u'report_reportcampaignposition', ['net_earned'])

        # Removing index on 'ReportStrategyProximicContext', fields ['bids_lost']
        db.delete_index(u'report_reportstrategyproximiccontext', ['bids_lost'])

        # Removing index on 'ReportStrategyProximicContext', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategyproximiccontext', ['data_cost_value'])

        # Removing index on 'ReportStrategyProximicContext', fields ['conv']
        db.delete_index(u'report_reportstrategyproximiccontext', ['conv'])

        # Removing index on 'ReportStrategyProximicContext', fields ['clk']
        db.delete_index(u'report_reportstrategyproximiccontext', ['clk'])

        # Removing index on 'ReportStrategyProximicContext', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategyproximiccontext', ['winbid_value_total'])

        # Removing index on 'ReportStrategyProximicContext', fields ['bid']
        db.delete_index(u'report_reportstrategyproximiccontext', ['bid'])

        # Removing index on 'ReportStrategyProximicContext', fields ['conv_value']
        db.delete_index(u'report_reportstrategyproximiccontext', ['conv_value'])

        # Removing index on 'ReportStrategyProximicContext', fields ['bid_value']
        db.delete_index(u'report_reportstrategyproximiccontext', ['bid_value'])

        # Removing index on 'ReportStrategyProximicContext', fields ['imp']
        db.delete_index(u'report_reportstrategyproximiccontext', ['imp'])

        # Removing index on 'ReportStrategyProximicContext', fields ['commission_value']
        db.delete_index(u'report_reportstrategyproximiccontext', ['commission_value'])

        # Removing index on 'ReportStrategyProximicContext', fields ['winbid']
        db.delete_index(u'report_reportstrategyproximiccontext', ['winbid'])

        # Removing index on 'ReportStrategyProximicContext', fields ['winbid_value']
        db.delete_index(u'report_reportstrategyproximiccontext', ['winbid_value'])

        # Removing index on 'ReportStrategyProximicContext', fields ['net_earned']
        db.delete_index(u'report_reportstrategyproximiccontext', ['net_earned'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['bids_lost'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['data_cost_value'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['conv']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['conv'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['clk']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['clk'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['winbid_value_total'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['bid']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['bid'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['conv_value']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['conv_value'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['bid_value']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['bid_value'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['imp']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['imp'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['commission_value']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['commission_value'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['winbid']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['winbid'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['winbid_value'])

        # Removing index on 'ReportCampaignProximicContextual', fields ['net_earned']
        db.delete_index(u'report_reportcampaignproximiccontextual', ['net_earned'])

        # Removing index on 'ReportStrategyCategory', fields ['bids_lost']
        db.delete_index(u'report_reportstrategycategory', ['bids_lost'])

        # Removing index on 'ReportStrategyCategory', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategycategory', ['data_cost_value'])

        # Removing index on 'ReportStrategyCategory', fields ['conv']
        db.delete_index(u'report_reportstrategycategory', ['conv'])

        # Removing index on 'ReportStrategyCategory', fields ['clk']
        db.delete_index(u'report_reportstrategycategory', ['clk'])

        # Removing index on 'ReportStrategyCategory', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategycategory', ['winbid_value_total'])

        # Removing index on 'ReportStrategyCategory', fields ['bid']
        db.delete_index(u'report_reportstrategycategory', ['bid'])

        # Removing index on 'ReportStrategyCategory', fields ['conv_value']
        db.delete_index(u'report_reportstrategycategory', ['conv_value'])

        # Removing index on 'ReportStrategyCategory', fields ['bid_value']
        db.delete_index(u'report_reportstrategycategory', ['bid_value'])

        # Removing index on 'ReportStrategyCategory', fields ['imp']
        db.delete_index(u'report_reportstrategycategory', ['imp'])

        # Removing index on 'ReportStrategyCategory', fields ['commission_value']
        db.delete_index(u'report_reportstrategycategory', ['commission_value'])

        # Removing index on 'ReportStrategyCategory', fields ['winbid']
        db.delete_index(u'report_reportstrategycategory', ['winbid'])

        # Removing index on 'ReportStrategyCategory', fields ['winbid_value']
        db.delete_index(u'report_reportstrategycategory', ['winbid_value'])

        # Removing index on 'ReportStrategyCategory', fields ['net_earned']
        db.delete_index(u'report_reportstrategycategory', ['net_earned'])

        # Removing index on 'ReportCampaign', fields ['bids_lost']
        db.delete_index(u'report_reportcampaign', ['bids_lost'])

        # Removing index on 'ReportCampaign', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaign', ['data_cost_value'])

        # Removing index on 'ReportCampaign', fields ['conv']
        db.delete_index(u'report_reportcampaign', ['conv'])

        # Removing index on 'ReportCampaign', fields ['clk']
        db.delete_index(u'report_reportcampaign', ['clk'])

        # Removing index on 'ReportCampaign', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaign', ['winbid_value_total'])

        # Removing index on 'ReportCampaign', fields ['bid']
        db.delete_index(u'report_reportcampaign', ['bid'])

        # Removing index on 'ReportCampaign', fields ['conv_value']
        db.delete_index(u'report_reportcampaign', ['conv_value'])

        # Removing index on 'ReportCampaign', fields ['bid_value']
        db.delete_index(u'report_reportcampaign', ['bid_value'])

        # Removing index on 'ReportCampaign', fields ['imp']
        db.delete_index(u'report_reportcampaign', ['imp'])

        # Removing index on 'ReportCampaign', fields ['commission_value']
        db.delete_index(u'report_reportcampaign', ['commission_value'])

        # Removing index on 'ReportCampaign', fields ['winbid']
        db.delete_index(u'report_reportcampaign', ['winbid'])

        # Removing index on 'ReportCampaign', fields ['winbid_value']
        db.delete_index(u'report_reportcampaign', ['winbid_value'])

        # Removing index on 'ReportCampaign', fields ['net_earned']
        db.delete_index(u'report_reportcampaign', ['net_earned'])

        # Removing index on 'ReportCampaignPublisher', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignpublisher', ['bids_lost'])

        # Removing index on 'ReportCampaignPublisher', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignpublisher', ['data_cost_value'])

        # Removing index on 'ReportCampaignPublisher', fields ['conv']
        db.delete_index(u'report_reportcampaignpublisher', ['conv'])

        # Removing index on 'ReportCampaignPublisher', fields ['clk']
        db.delete_index(u'report_reportcampaignpublisher', ['clk'])

        # Removing index on 'ReportCampaignPublisher', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignpublisher', ['winbid_value_total'])

        # Removing index on 'ReportCampaignPublisher', fields ['bid']
        db.delete_index(u'report_reportcampaignpublisher', ['bid'])

        # Removing index on 'ReportCampaignPublisher', fields ['conv_value']
        db.delete_index(u'report_reportcampaignpublisher', ['conv_value'])

        # Removing index on 'ReportCampaignPublisher', fields ['bid_value']
        db.delete_index(u'report_reportcampaignpublisher', ['bid_value'])

        # Removing index on 'ReportCampaignPublisher', fields ['imp']
        db.delete_index(u'report_reportcampaignpublisher', ['imp'])

        # Removing index on 'ReportCampaignPublisher', fields ['commission_value']
        db.delete_index(u'report_reportcampaignpublisher', ['commission_value'])

        # Removing index on 'ReportCampaignPublisher', fields ['winbid']
        db.delete_index(u'report_reportcampaignpublisher', ['winbid'])

        # Removing index on 'ReportCampaignPublisher', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignpublisher', ['winbid_value'])

        # Removing index on 'ReportCampaignPublisher', fields ['net_earned']
        db.delete_index(u'report_reportcampaignpublisher', ['net_earned'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['bids_lost']
        db.delete_index(u'report_reportstrategyproximicquality', ['bids_lost'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategyproximicquality', ['data_cost_value'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['conv']
        db.delete_index(u'report_reportstrategyproximicquality', ['conv'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['clk']
        db.delete_index(u'report_reportstrategyproximicquality', ['clk'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategyproximicquality', ['winbid_value_total'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['bid']
        db.delete_index(u'report_reportstrategyproximicquality', ['bid'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['conv_value']
        db.delete_index(u'report_reportstrategyproximicquality', ['conv_value'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['bid_value']
        db.delete_index(u'report_reportstrategyproximicquality', ['bid_value'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['imp']
        db.delete_index(u'report_reportstrategyproximicquality', ['imp'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['commission_value']
        db.delete_index(u'report_reportstrategyproximicquality', ['commission_value'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['winbid']
        db.delete_index(u'report_reportstrategyproximicquality', ['winbid'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['winbid_value']
        db.delete_index(u'report_reportstrategyproximicquality', ['winbid_value'])

        # Removing index on 'ReportStrategyProximicQuality', fields ['net_earned']
        db.delete_index(u'report_reportstrategyproximicquality', ['net_earned'])

        # Removing index on 'ReportCampaignCarrier', fields ['bids_lost']
        db.delete_index(u'report_reportcampaigncarrier', ['bids_lost'])

        # Removing index on 'ReportCampaignCarrier', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaigncarrier', ['data_cost_value'])

        # Removing index on 'ReportCampaignCarrier', fields ['conv']
        db.delete_index(u'report_reportcampaigncarrier', ['conv'])

        # Removing index on 'ReportCampaignCarrier', fields ['clk']
        db.delete_index(u'report_reportcampaigncarrier', ['clk'])

        # Removing index on 'ReportCampaignCarrier', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaigncarrier', ['winbid_value_total'])

        # Removing index on 'ReportCampaignCarrier', fields ['bid']
        db.delete_index(u'report_reportcampaigncarrier', ['bid'])

        # Removing index on 'ReportCampaignCarrier', fields ['conv_value']
        db.delete_index(u'report_reportcampaigncarrier', ['conv_value'])

        # Removing index on 'ReportCampaignCarrier', fields ['bid_value']
        db.delete_index(u'report_reportcampaigncarrier', ['bid_value'])

        # Removing index on 'ReportCampaignCarrier', fields ['imp']
        db.delete_index(u'report_reportcampaigncarrier', ['imp'])

        # Removing index on 'ReportCampaignCarrier', fields ['commission_value']
        db.delete_index(u'report_reportcampaigncarrier', ['commission_value'])

        # Removing index on 'ReportCampaignCarrier', fields ['winbid']
        db.delete_index(u'report_reportcampaigncarrier', ['winbid'])

        # Removing index on 'ReportCampaignCarrier', fields ['winbid_value']
        db.delete_index(u'report_reportcampaigncarrier', ['winbid_value'])

        # Removing index on 'ReportCampaignCarrier', fields ['net_earned']
        db.delete_index(u'report_reportcampaigncarrier', ['net_earned'])

        # Removing index on 'ReportStrategyRegion', fields ['bids_lost']
        db.delete_index(u'report_reportstrategyregion', ['bids_lost'])

        # Removing index on 'ReportStrategyRegion', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategyregion', ['data_cost_value'])

        # Removing index on 'ReportStrategyRegion', fields ['conv']
        db.delete_index(u'report_reportstrategyregion', ['conv'])

        # Removing index on 'ReportStrategyRegion', fields ['clk']
        db.delete_index(u'report_reportstrategyregion', ['clk'])

        # Removing index on 'ReportStrategyRegion', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategyregion', ['winbid_value_total'])

        # Removing index on 'ReportStrategyRegion', fields ['bid']
        db.delete_index(u'report_reportstrategyregion', ['bid'])

        # Removing index on 'ReportStrategyRegion', fields ['conv_value']
        db.delete_index(u'report_reportstrategyregion', ['conv_value'])

        # Removing index on 'ReportStrategyRegion', fields ['bid_value']
        db.delete_index(u'report_reportstrategyregion', ['bid_value'])

        # Removing index on 'ReportStrategyRegion', fields ['imp']
        db.delete_index(u'report_reportstrategyregion', ['imp'])

        # Removing index on 'ReportStrategyRegion', fields ['commission_value']
        db.delete_index(u'report_reportstrategyregion', ['commission_value'])

        # Removing index on 'ReportStrategyRegion', fields ['winbid']
        db.delete_index(u'report_reportstrategyregion', ['winbid'])

        # Removing index on 'ReportStrategyRegion', fields ['winbid_value']
        db.delete_index(u'report_reportstrategyregion', ['winbid_value'])

        # Removing index on 'ReportStrategyRegion', fields ['net_earned']
        db.delete_index(u'report_reportstrategyregion', ['net_earned'])

        # Removing index on 'ReportCampaignAge', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignage', ['bids_lost'])

        # Removing index on 'ReportCampaignAge', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignage', ['data_cost_value'])

        # Removing index on 'ReportCampaignAge', fields ['conv']
        db.delete_index(u'report_reportcampaignage', ['conv'])

        # Removing index on 'ReportCampaignAge', fields ['clk']
        db.delete_index(u'report_reportcampaignage', ['clk'])

        # Removing index on 'ReportCampaignAge', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignage', ['winbid_value_total'])

        # Removing index on 'ReportCampaignAge', fields ['bid']
        db.delete_index(u'report_reportcampaignage', ['bid'])

        # Removing index on 'ReportCampaignAge', fields ['conv_value']
        db.delete_index(u'report_reportcampaignage', ['conv_value'])

        # Removing index on 'ReportCampaignAge', fields ['bid_value']
        db.delete_index(u'report_reportcampaignage', ['bid_value'])

        # Removing index on 'ReportCampaignAge', fields ['imp']
        db.delete_index(u'report_reportcampaignage', ['imp'])

        # Removing index on 'ReportCampaignAge', fields ['commission_value']
        db.delete_index(u'report_reportcampaignage', ['commission_value'])

        # Removing index on 'ReportCampaignAge', fields ['winbid']
        db.delete_index(u'report_reportcampaignage', ['winbid'])

        # Removing index on 'ReportCampaignAge', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignage', ['winbid_value'])

        # Removing index on 'ReportCampaignAge', fields ['net_earned']
        db.delete_index(u'report_reportcampaignage', ['net_earned'])

        # Removing index on 'ReportCampaignMake', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignmake', ['bids_lost'])

        # Removing index on 'ReportCampaignMake', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignmake', ['data_cost_value'])

        # Removing index on 'ReportCampaignMake', fields ['conv']
        db.delete_index(u'report_reportcampaignmake', ['conv'])

        # Removing index on 'ReportCampaignMake', fields ['clk']
        db.delete_index(u'report_reportcampaignmake', ['clk'])

        # Removing index on 'ReportCampaignMake', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignmake', ['winbid_value_total'])

        # Removing index on 'ReportCampaignMake', fields ['bid']
        db.delete_index(u'report_reportcampaignmake', ['bid'])

        # Removing index on 'ReportCampaignMake', fields ['conv_value']
        db.delete_index(u'report_reportcampaignmake', ['conv_value'])

        # Removing index on 'ReportCampaignMake', fields ['bid_value']
        db.delete_index(u'report_reportcampaignmake', ['bid_value'])

        # Removing index on 'ReportCampaignMake', fields ['imp']
        db.delete_index(u'report_reportcampaignmake', ['imp'])

        # Removing index on 'ReportCampaignMake', fields ['commission_value']
        db.delete_index(u'report_reportcampaignmake', ['commission_value'])

        # Removing index on 'ReportCampaignMake', fields ['winbid']
        db.delete_index(u'report_reportcampaignmake', ['winbid'])

        # Removing index on 'ReportCampaignMake', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignmake', ['winbid_value'])

        # Removing index on 'ReportCampaignMake', fields ['net_earned']
        db.delete_index(u'report_reportcampaignmake', ['net_earned'])

        # Removing index on 'ReportStrategyCountry', fields ['bids_lost']
        db.delete_index(u'report_reportstrategycountry', ['bids_lost'])

        # Removing index on 'ReportStrategyCountry', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategycountry', ['data_cost_value'])

        # Removing index on 'ReportStrategyCountry', fields ['conv']
        db.delete_index(u'report_reportstrategycountry', ['conv'])

        # Removing index on 'ReportStrategyCountry', fields ['clk']
        db.delete_index(u'report_reportstrategycountry', ['clk'])

        # Removing index on 'ReportStrategyCountry', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategycountry', ['winbid_value_total'])

        # Removing index on 'ReportStrategyCountry', fields ['bid']
        db.delete_index(u'report_reportstrategycountry', ['bid'])

        # Removing index on 'ReportStrategyCountry', fields ['conv_value']
        db.delete_index(u'report_reportstrategycountry', ['conv_value'])

        # Removing index on 'ReportStrategyCountry', fields ['bid_value']
        db.delete_index(u'report_reportstrategycountry', ['bid_value'])

        # Removing index on 'ReportStrategyCountry', fields ['imp']
        db.delete_index(u'report_reportstrategycountry', ['imp'])

        # Removing index on 'ReportStrategyCountry', fields ['commission_value']
        db.delete_index(u'report_reportstrategycountry', ['commission_value'])

        # Removing index on 'ReportStrategyCountry', fields ['winbid']
        db.delete_index(u'report_reportstrategycountry', ['winbid'])

        # Removing index on 'ReportStrategyCountry', fields ['winbid_value']
        db.delete_index(u'report_reportstrategycountry', ['winbid_value'])

        # Removing index on 'ReportStrategyCountry', fields ['net_earned']
        db.delete_index(u'report_reportstrategycountry', ['net_earned'])

        # Removing index on 'ReportCampaignGender', fields ['bids_lost']
        db.delete_index(u'report_reportcampaigngender', ['bids_lost'])

        # Removing index on 'ReportCampaignGender', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaigngender', ['data_cost_value'])

        # Removing index on 'ReportCampaignGender', fields ['conv']
        db.delete_index(u'report_reportcampaigngender', ['conv'])

        # Removing index on 'ReportCampaignGender', fields ['clk']
        db.delete_index(u'report_reportcampaigngender', ['clk'])

        # Removing index on 'ReportCampaignGender', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaigngender', ['winbid_value_total'])

        # Removing index on 'ReportCampaignGender', fields ['bid']
        db.delete_index(u'report_reportcampaigngender', ['bid'])

        # Removing index on 'ReportCampaignGender', fields ['conv_value']
        db.delete_index(u'report_reportcampaigngender', ['conv_value'])

        # Removing index on 'ReportCampaignGender', fields ['bid_value']
        db.delete_index(u'report_reportcampaigngender', ['bid_value'])

        # Removing index on 'ReportCampaignGender', fields ['imp']
        db.delete_index(u'report_reportcampaigngender', ['imp'])

        # Removing index on 'ReportCampaignGender', fields ['commission_value']
        db.delete_index(u'report_reportcampaigngender', ['commission_value'])

        # Removing index on 'ReportCampaignGender', fields ['winbid']
        db.delete_index(u'report_reportcampaigngender', ['winbid'])

        # Removing index on 'ReportCampaignGender', fields ['winbid_value']
        db.delete_index(u'report_reportcampaigngender', ['winbid_value'])

        # Removing index on 'ReportCampaignGender', fields ['net_earned']
        db.delete_index(u'report_reportcampaigngender', ['net_earned'])

        # Removing index on 'ReportStrategyOs', fields ['bids_lost']
        db.delete_index(u'report_reportstrategyos', ['bids_lost'])

        # Removing index on 'ReportStrategyOs', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategyos', ['data_cost_value'])

        # Removing index on 'ReportStrategyOs', fields ['conv']
        db.delete_index(u'report_reportstrategyos', ['conv'])

        # Removing index on 'ReportStrategyOs', fields ['clk']
        db.delete_index(u'report_reportstrategyos', ['clk'])

        # Removing index on 'ReportStrategyOs', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategyos', ['winbid_value_total'])

        # Removing index on 'ReportStrategyOs', fields ['bid']
        db.delete_index(u'report_reportstrategyos', ['bid'])

        # Removing index on 'ReportStrategyOs', fields ['conv_value']
        db.delete_index(u'report_reportstrategyos', ['conv_value'])

        # Removing index on 'ReportStrategyOs', fields ['bid_value']
        db.delete_index(u'report_reportstrategyos', ['bid_value'])

        # Removing index on 'ReportStrategyOs', fields ['imp']
        db.delete_index(u'report_reportstrategyos', ['imp'])

        # Removing index on 'ReportStrategyOs', fields ['commission_value']
        db.delete_index(u'report_reportstrategyos', ['commission_value'])

        # Removing index on 'ReportStrategyOs', fields ['winbid']
        db.delete_index(u'report_reportstrategyos', ['winbid'])

        # Removing index on 'ReportStrategyOs', fields ['winbid_value']
        db.delete_index(u'report_reportstrategyos', ['winbid_value'])

        # Removing index on 'ReportStrategyOs', fields ['net_earned']
        db.delete_index(u'report_reportstrategyos', ['net_earned'])

        # Removing index on 'ReportCampaignSite', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignsite', ['bids_lost'])

        # Removing index on 'ReportCampaignSite', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignsite', ['data_cost_value'])

        # Removing index on 'ReportCampaignSite', fields ['conv']
        db.delete_index(u'report_reportcampaignsite', ['conv'])

        # Removing index on 'ReportCampaignSite', fields ['clk']
        db.delete_index(u'report_reportcampaignsite', ['clk'])

        # Removing index on 'ReportCampaignSite', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignsite', ['winbid_value_total'])

        # Removing index on 'ReportCampaignSite', fields ['bid']
        db.delete_index(u'report_reportcampaignsite', ['bid'])

        # Removing index on 'ReportCampaignSite', fields ['conv_value']
        db.delete_index(u'report_reportcampaignsite', ['conv_value'])

        # Removing index on 'ReportCampaignSite', fields ['bid_value']
        db.delete_index(u'report_reportcampaignsite', ['bid_value'])

        # Removing index on 'ReportCampaignSite', fields ['imp']
        db.delete_index(u'report_reportcampaignsite', ['imp'])

        # Removing index on 'ReportCampaignSite', fields ['commission_value']
        db.delete_index(u'report_reportcampaignsite', ['commission_value'])

        # Removing index on 'ReportCampaignSite', fields ['winbid']
        db.delete_index(u'report_reportcampaignsite', ['winbid'])

        # Removing index on 'ReportCampaignSite', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignsite', ['winbid_value'])

        # Removing index on 'ReportCampaignSite', fields ['net_earned']
        db.delete_index(u'report_reportcampaignsite', ['net_earned'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['bids_lost']
        db.delete_index(u'report_reportstrategypeer39contextual', ['bids_lost'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategypeer39contextual', ['data_cost_value'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['conv']
        db.delete_index(u'report_reportstrategypeer39contextual', ['conv'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['clk']
        db.delete_index(u'report_reportstrategypeer39contextual', ['clk'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategypeer39contextual', ['winbid_value_total'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['bid']
        db.delete_index(u'report_reportstrategypeer39contextual', ['bid'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['conv_value']
        db.delete_index(u'report_reportstrategypeer39contextual', ['conv_value'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['bid_value']
        db.delete_index(u'report_reportstrategypeer39contextual', ['bid_value'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['imp']
        db.delete_index(u'report_reportstrategypeer39contextual', ['imp'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['commission_value']
        db.delete_index(u'report_reportstrategypeer39contextual', ['commission_value'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['winbid']
        db.delete_index(u'report_reportstrategypeer39contextual', ['winbid'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['winbid_value']
        db.delete_index(u'report_reportstrategypeer39contextual', ['winbid_value'])

        # Removing index on 'ReportStrategyPeer39Contextual', fields ['net_earned']
        db.delete_index(u'report_reportstrategypeer39contextual', ['net_earned'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['bids_lost'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['data_cost_value'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['conv']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['conv'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['clk']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['clk'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['winbid_value_total'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['bid']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['bid'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['conv_value']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['conv_value'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['bid_value']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['bid_value'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['imp']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['imp'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['commission_value']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['commission_value'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['winbid']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['winbid'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['winbid_value'])

        # Removing index on 'ReportCampaignProximicMaturity', fields ['net_earned']
        db.delete_index(u'report_reportcampaignproximicmaturity', ['net_earned'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['bids_lost'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['data_cost_value'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['conv']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['conv'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['clk']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['clk'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['winbid_value_total'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['bid']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['bid'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['conv_value']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['conv_value'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['bid_value']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['bid_value'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['imp']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['imp'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['commission_value']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['commission_value'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['winbid']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['winbid'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['winbid_value'])

        # Removing index on 'ReportCampaignPublisherNetwork', fields ['net_earned']
        db.delete_index(u'report_reportcampaignpublishernetwork', ['net_earned'])

        # Removing index on 'ReportCampaignCountry', fields ['bids_lost']
        db.delete_index(u'report_reportcampaigncountry', ['bids_lost'])

        # Removing index on 'ReportCampaignCountry', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaigncountry', ['data_cost_value'])

        # Removing index on 'ReportCampaignCountry', fields ['conv']
        db.delete_index(u'report_reportcampaigncountry', ['conv'])

        # Removing index on 'ReportCampaignCountry', fields ['clk']
        db.delete_index(u'report_reportcampaigncountry', ['clk'])

        # Removing index on 'ReportCampaignCountry', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaigncountry', ['winbid_value_total'])

        # Removing index on 'ReportCampaignCountry', fields ['bid']
        db.delete_index(u'report_reportcampaigncountry', ['bid'])

        # Removing index on 'ReportCampaignCountry', fields ['conv_value']
        db.delete_index(u'report_reportcampaigncountry', ['conv_value'])

        # Removing index on 'ReportCampaignCountry', fields ['bid_value']
        db.delete_index(u'report_reportcampaigncountry', ['bid_value'])

        # Removing index on 'ReportCampaignCountry', fields ['imp']
        db.delete_index(u'report_reportcampaigncountry', ['imp'])

        # Removing index on 'ReportCampaignCountry', fields ['commission_value']
        db.delete_index(u'report_reportcampaigncountry', ['commission_value'])

        # Removing index on 'ReportCampaignCountry', fields ['winbid']
        db.delete_index(u'report_reportcampaigncountry', ['winbid'])

        # Removing index on 'ReportCampaignCountry', fields ['winbid_value']
        db.delete_index(u'report_reportcampaigncountry', ['winbid_value'])

        # Removing index on 'ReportCampaignCountry', fields ['net_earned']
        db.delete_index(u'report_reportcampaigncountry', ['net_earned'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['bids_lost']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['bids_lost'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['data_cost_value'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['conv']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['conv'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['clk']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['clk'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['winbid_value_total'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['bid']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['bid'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['conv_value']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['conv_value'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['bid_value']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['bid_value'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['imp']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['imp'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['commission_value']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['commission_value'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['winbid']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['winbid'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['winbid_value']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['winbid_value'])

        # Removing index on 'ReportStrategyProximicMaturity', fields ['net_earned']
        db.delete_index(u'report_reportstrategyproximicmaturity', ['net_earned'])

        # Removing index on 'ReportStrategyGender', fields ['bids_lost']
        db.delete_index(u'report_reportstrategygender', ['bids_lost'])

        # Removing index on 'ReportStrategyGender', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategygender', ['data_cost_value'])

        # Removing index on 'ReportStrategyGender', fields ['conv']
        db.delete_index(u'report_reportstrategygender', ['conv'])

        # Removing index on 'ReportStrategyGender', fields ['clk']
        db.delete_index(u'report_reportstrategygender', ['clk'])

        # Removing index on 'ReportStrategyGender', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategygender', ['winbid_value_total'])

        # Removing index on 'ReportStrategyGender', fields ['bid']
        db.delete_index(u'report_reportstrategygender', ['bid'])

        # Removing index on 'ReportStrategyGender', fields ['conv_value']
        db.delete_index(u'report_reportstrategygender', ['conv_value'])

        # Removing index on 'ReportStrategyGender', fields ['bid_value']
        db.delete_index(u'report_reportstrategygender', ['bid_value'])

        # Removing index on 'ReportStrategyGender', fields ['imp']
        db.delete_index(u'report_reportstrategygender', ['imp'])

        # Removing index on 'ReportStrategyGender', fields ['commission_value']
        db.delete_index(u'report_reportstrategygender', ['commission_value'])

        # Removing index on 'ReportStrategyGender', fields ['winbid']
        db.delete_index(u'report_reportstrategygender', ['winbid'])

        # Removing index on 'ReportStrategyGender', fields ['winbid_value']
        db.delete_index(u'report_reportstrategygender', ['winbid_value'])

        # Removing index on 'ReportStrategyGender', fields ['net_earned']
        db.delete_index(u'report_reportstrategygender', ['net_earned'])

        # Removing index on 'ReportAdvert', fields ['bids_lost']
        db.delete_index(u'report_reportadvert', ['bids_lost'])

        # Removing index on 'ReportAdvert', fields ['data_cost_value']
        db.delete_index(u'report_reportadvert', ['data_cost_value'])

        # Removing index on 'ReportAdvert', fields ['conv']
        db.delete_index(u'report_reportadvert', ['conv'])

        # Removing index on 'ReportAdvert', fields ['clk']
        db.delete_index(u'report_reportadvert', ['clk'])

        # Removing index on 'ReportAdvert', fields ['winbid_value_total']
        db.delete_index(u'report_reportadvert', ['winbid_value_total'])

        # Removing index on 'ReportAdvert', fields ['bid']
        db.delete_index(u'report_reportadvert', ['bid'])

        # Removing index on 'ReportAdvert', fields ['conv_value']
        db.delete_index(u'report_reportadvert', ['conv_value'])

        # Removing index on 'ReportAdvert', fields ['bid_value']
        db.delete_index(u'report_reportadvert', ['bid_value'])

        # Removing index on 'ReportAdvert', fields ['imp']
        db.delete_index(u'report_reportadvert', ['imp'])

        # Removing index on 'ReportAdvert', fields ['commission_value']
        db.delete_index(u'report_reportadvert', ['commission_value'])

        # Removing index on 'ReportAdvert', fields ['winbid']
        db.delete_index(u'report_reportadvert', ['winbid'])

        # Removing index on 'ReportAdvert', fields ['winbid_value']
        db.delete_index(u'report_reportadvert', ['winbid_value'])

        # Removing index on 'ReportAdvert', fields ['net_earned']
        db.delete_index(u'report_reportadvert', ['net_earned'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignpeer39language', ['bids_lost'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignpeer39language', ['data_cost_value'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['conv']
        db.delete_index(u'report_reportcampaignpeer39language', ['conv'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['clk']
        db.delete_index(u'report_reportcampaignpeer39language', ['clk'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignpeer39language', ['winbid_value_total'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['bid']
        db.delete_index(u'report_reportcampaignpeer39language', ['bid'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['conv_value']
        db.delete_index(u'report_reportcampaignpeer39language', ['conv_value'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['bid_value']
        db.delete_index(u'report_reportcampaignpeer39language', ['bid_value'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['imp']
        db.delete_index(u'report_reportcampaignpeer39language', ['imp'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['commission_value']
        db.delete_index(u'report_reportcampaignpeer39language', ['commission_value'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['winbid']
        db.delete_index(u'report_reportcampaignpeer39language', ['winbid'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignpeer39language', ['winbid_value'])

        # Removing index on 'ReportCampaignPeer39Language', fields ['net_earned']
        db.delete_index(u'report_reportcampaignpeer39language', ['net_earned'])

        # Removing index on 'ReportStrategyCarrier', fields ['bids_lost']
        db.delete_index(u'report_reportstrategycarrier', ['bids_lost'])

        # Removing index on 'ReportStrategyCarrier', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategycarrier', ['data_cost_value'])

        # Removing index on 'ReportStrategyCarrier', fields ['conv']
        db.delete_index(u'report_reportstrategycarrier', ['conv'])

        # Removing index on 'ReportStrategyCarrier', fields ['clk']
        db.delete_index(u'report_reportstrategycarrier', ['clk'])

        # Removing index on 'ReportStrategyCarrier', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategycarrier', ['winbid_value_total'])

        # Removing index on 'ReportStrategyCarrier', fields ['bid']
        db.delete_index(u'report_reportstrategycarrier', ['bid'])

        # Removing index on 'ReportStrategyCarrier', fields ['conv_value']
        db.delete_index(u'report_reportstrategycarrier', ['conv_value'])

        # Removing index on 'ReportStrategyCarrier', fields ['bid_value']
        db.delete_index(u'report_reportstrategycarrier', ['bid_value'])

        # Removing index on 'ReportStrategyCarrier', fields ['imp']
        db.delete_index(u'report_reportstrategycarrier', ['imp'])

        # Removing index on 'ReportStrategyCarrier', fields ['commission_value']
        db.delete_index(u'report_reportstrategycarrier', ['commission_value'])

        # Removing index on 'ReportStrategyCarrier', fields ['winbid']
        db.delete_index(u'report_reportstrategycarrier', ['winbid'])

        # Removing index on 'ReportStrategyCarrier', fields ['winbid_value']
        db.delete_index(u'report_reportstrategycarrier', ['winbid_value'])

        # Removing index on 'ReportStrategyCarrier', fields ['net_earned']
        db.delete_index(u'report_reportstrategycarrier', ['net_earned'])

        # Removing index on 'ReportCampaignOs', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignos', ['bids_lost'])

        # Removing index on 'ReportCampaignOs', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignos', ['data_cost_value'])

        # Removing index on 'ReportCampaignOs', fields ['conv']
        db.delete_index(u'report_reportcampaignos', ['conv'])

        # Removing index on 'ReportCampaignOs', fields ['clk']
        db.delete_index(u'report_reportcampaignos', ['clk'])

        # Removing index on 'ReportCampaignOs', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignos', ['winbid_value_total'])

        # Removing index on 'ReportCampaignOs', fields ['bid']
        db.delete_index(u'report_reportcampaignos', ['bid'])

        # Removing index on 'ReportCampaignOs', fields ['conv_value']
        db.delete_index(u'report_reportcampaignos', ['conv_value'])

        # Removing index on 'ReportCampaignOs', fields ['bid_value']
        db.delete_index(u'report_reportcampaignos', ['bid_value'])

        # Removing index on 'ReportCampaignOs', fields ['imp']
        db.delete_index(u'report_reportcampaignos', ['imp'])

        # Removing index on 'ReportCampaignOs', fields ['commission_value']
        db.delete_index(u'report_reportcampaignos', ['commission_value'])

        # Removing index on 'ReportCampaignOs', fields ['winbid']
        db.delete_index(u'report_reportcampaignos', ['winbid'])

        # Removing index on 'ReportCampaignOs', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignos', ['winbid_value'])

        # Removing index on 'ReportCampaignOs', fields ['net_earned']
        db.delete_index(u'report_reportcampaignos', ['net_earned'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['bids_lost']
        db.delete_index(u'report_reportstrategypeer39brand', ['bids_lost'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategypeer39brand', ['data_cost_value'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['conv']
        db.delete_index(u'report_reportstrategypeer39brand', ['conv'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['clk']
        db.delete_index(u'report_reportstrategypeer39brand', ['clk'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategypeer39brand', ['winbid_value_total'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['bid']
        db.delete_index(u'report_reportstrategypeer39brand', ['bid'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['conv_value']
        db.delete_index(u'report_reportstrategypeer39brand', ['conv_value'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['bid_value']
        db.delete_index(u'report_reportstrategypeer39brand', ['bid_value'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['imp']
        db.delete_index(u'report_reportstrategypeer39brand', ['imp'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['commission_value']
        db.delete_index(u'report_reportstrategypeer39brand', ['commission_value'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['winbid']
        db.delete_index(u'report_reportstrategypeer39brand', ['winbid'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['winbid_value']
        db.delete_index(u'report_reportstrategypeer39brand', ['winbid_value'])

        # Removing index on 'ReportStrategyPeer39Brand', fields ['net_earned']
        db.delete_index(u'report_reportstrategypeer39brand', ['net_earned'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['bids_lost']
        db.delete_index(u'report_reportstrategyproximicsafety', ['bids_lost'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategyproximicsafety', ['data_cost_value'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['conv']
        db.delete_index(u'report_reportstrategyproximicsafety', ['conv'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['clk']
        db.delete_index(u'report_reportstrategyproximicsafety', ['clk'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategyproximicsafety', ['winbid_value_total'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['bid']
        db.delete_index(u'report_reportstrategyproximicsafety', ['bid'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['conv_value']
        db.delete_index(u'report_reportstrategyproximicsafety', ['conv_value'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['bid_value']
        db.delete_index(u'report_reportstrategyproximicsafety', ['bid_value'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['imp']
        db.delete_index(u'report_reportstrategyproximicsafety', ['imp'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['commission_value']
        db.delete_index(u'report_reportstrategyproximicsafety', ['commission_value'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['winbid']
        db.delete_index(u'report_reportstrategyproximicsafety', ['winbid'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['winbid_value']
        db.delete_index(u'report_reportstrategyproximicsafety', ['winbid_value'])

        # Removing index on 'ReportStrategyProximicSafety', fields ['net_earned']
        db.delete_index(u'report_reportstrategyproximicsafety', ['net_earned'])

        # Removing index on 'ReportStrategyPublisher', fields ['bids_lost']
        db.delete_index(u'report_reportstrategypublisher', ['bids_lost'])

        # Removing index on 'ReportStrategyPublisher', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategypublisher', ['data_cost_value'])

        # Removing index on 'ReportStrategyPublisher', fields ['conv']
        db.delete_index(u'report_reportstrategypublisher', ['conv'])

        # Removing index on 'ReportStrategyPublisher', fields ['clk']
        db.delete_index(u'report_reportstrategypublisher', ['clk'])

        # Removing index on 'ReportStrategyPublisher', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategypublisher', ['winbid_value_total'])

        # Removing index on 'ReportStrategyPublisher', fields ['bid']
        db.delete_index(u'report_reportstrategypublisher', ['bid'])

        # Removing index on 'ReportStrategyPublisher', fields ['conv_value']
        db.delete_index(u'report_reportstrategypublisher', ['conv_value'])

        # Removing index on 'ReportStrategyPublisher', fields ['bid_value']
        db.delete_index(u'report_reportstrategypublisher', ['bid_value'])

        # Removing index on 'ReportStrategyPublisher', fields ['imp']
        db.delete_index(u'report_reportstrategypublisher', ['imp'])

        # Removing index on 'ReportStrategyPublisher', fields ['commission_value']
        db.delete_index(u'report_reportstrategypublisher', ['commission_value'])

        # Removing index on 'ReportStrategyPublisher', fields ['winbid']
        db.delete_index(u'report_reportstrategypublisher', ['winbid'])

        # Removing index on 'ReportStrategyPublisher', fields ['winbid_value']
        db.delete_index(u'report_reportstrategypublisher', ['winbid_value'])

        # Removing index on 'ReportStrategyPublisher', fields ['net_earned']
        db.delete_index(u'report_reportstrategypublisher', ['net_earned'])

        # Removing index on 'ReportStrategy', fields ['bids_lost']
        db.delete_index(u'report_reportstrategy', ['bids_lost'])

        # Removing index on 'ReportStrategy', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategy', ['data_cost_value'])

        # Removing index on 'ReportStrategy', fields ['conv']
        db.delete_index(u'report_reportstrategy', ['conv'])

        # Removing index on 'ReportStrategy', fields ['clk']
        db.delete_index(u'report_reportstrategy', ['clk'])

        # Removing index on 'ReportStrategy', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategy', ['winbid_value_total'])

        # Removing index on 'ReportStrategy', fields ['bid']
        db.delete_index(u'report_reportstrategy', ['bid'])

        # Removing index on 'ReportStrategy', fields ['conv_value']
        db.delete_index(u'report_reportstrategy', ['conv_value'])

        # Removing index on 'ReportStrategy', fields ['bid_value']
        db.delete_index(u'report_reportstrategy', ['bid_value'])

        # Removing index on 'ReportStrategy', fields ['imp']
        db.delete_index(u'report_reportstrategy', ['imp'])

        # Removing index on 'ReportStrategy', fields ['commission_value']
        db.delete_index(u'report_reportstrategy', ['commission_value'])

        # Removing index on 'ReportStrategy', fields ['winbid']
        db.delete_index(u'report_reportstrategy', ['winbid'])

        # Removing index on 'ReportStrategy', fields ['winbid_value']
        db.delete_index(u'report_reportstrategy', ['winbid_value'])

        # Removing index on 'ReportStrategy', fields ['net_earned']
        db.delete_index(u'report_reportstrategy', ['net_earned'])

        # Removing index on 'ReportStrategyModel', fields ['bids_lost']
        db.delete_index(u'report_reportstrategymodel', ['bids_lost'])

        # Removing index on 'ReportStrategyModel', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategymodel', ['data_cost_value'])

        # Removing index on 'ReportStrategyModel', fields ['conv']
        db.delete_index(u'report_reportstrategymodel', ['conv'])

        # Removing index on 'ReportStrategyModel', fields ['clk']
        db.delete_index(u'report_reportstrategymodel', ['clk'])

        # Removing index on 'ReportStrategyModel', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategymodel', ['winbid_value_total'])

        # Removing index on 'ReportStrategyModel', fields ['bid']
        db.delete_index(u'report_reportstrategymodel', ['bid'])

        # Removing index on 'ReportStrategyModel', fields ['conv_value']
        db.delete_index(u'report_reportstrategymodel', ['conv_value'])

        # Removing index on 'ReportStrategyModel', fields ['bid_value']
        db.delete_index(u'report_reportstrategymodel', ['bid_value'])

        # Removing index on 'ReportStrategyModel', fields ['imp']
        db.delete_index(u'report_reportstrategymodel', ['imp'])

        # Removing index on 'ReportStrategyModel', fields ['commission_value']
        db.delete_index(u'report_reportstrategymodel', ['commission_value'])

        # Removing index on 'ReportStrategyModel', fields ['winbid']
        db.delete_index(u'report_reportstrategymodel', ['winbid'])

        # Removing index on 'ReportStrategyModel', fields ['winbid_value']
        db.delete_index(u'report_reportstrategymodel', ['winbid_value'])

        # Removing index on 'ReportStrategyModel', fields ['net_earned']
        db.delete_index(u'report_reportstrategymodel', ['net_earned'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['bids_lost'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['data_cost_value'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['conv']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['conv'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['clk']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['clk'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['winbid_value_total'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['bid']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['bid'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['conv_value']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['conv_value'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['bid_value']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['bid_value'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['imp']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['imp'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['commission_value']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['commission_value'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['winbid']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['winbid'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['winbid_value'])

        # Removing index on 'ReportCampaignPeer39Contextual', fields ['net_earned']
        db.delete_index(u'report_reportcampaignpeer39contextual', ['net_earned'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['bids_lost']
        db.delete_index(u'report_reportstrategypeer39quality', ['bids_lost'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategypeer39quality', ['data_cost_value'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['conv']
        db.delete_index(u'report_reportstrategypeer39quality', ['conv'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['clk']
        db.delete_index(u'report_reportstrategypeer39quality', ['clk'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategypeer39quality', ['winbid_value_total'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['bid']
        db.delete_index(u'report_reportstrategypeer39quality', ['bid'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['conv_value']
        db.delete_index(u'report_reportstrategypeer39quality', ['conv_value'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['bid_value']
        db.delete_index(u'report_reportstrategypeer39quality', ['bid_value'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['imp']
        db.delete_index(u'report_reportstrategypeer39quality', ['imp'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['commission_value']
        db.delete_index(u'report_reportstrategypeer39quality', ['commission_value'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['winbid']
        db.delete_index(u'report_reportstrategypeer39quality', ['winbid'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['winbid_value']
        db.delete_index(u'report_reportstrategypeer39quality', ['winbid_value'])

        # Removing index on 'ReportStrategyPeer39Quality', fields ['net_earned']
        db.delete_index(u'report_reportstrategypeer39quality', ['net_earned'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['bids_lost']
        db.delete_index(u'report_reportstrategyproximicnotice', ['bids_lost'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategyproximicnotice', ['data_cost_value'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['conv']
        db.delete_index(u'report_reportstrategyproximicnotice', ['conv'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['clk']
        db.delete_index(u'report_reportstrategyproximicnotice', ['clk'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategyproximicnotice', ['winbid_value_total'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['bid']
        db.delete_index(u'report_reportstrategyproximicnotice', ['bid'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['conv_value']
        db.delete_index(u'report_reportstrategyproximicnotice', ['conv_value'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['bid_value']
        db.delete_index(u'report_reportstrategyproximicnotice', ['bid_value'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['imp']
        db.delete_index(u'report_reportstrategyproximicnotice', ['imp'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['commission_value']
        db.delete_index(u'report_reportstrategyproximicnotice', ['commission_value'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['winbid']
        db.delete_index(u'report_reportstrategyproximicnotice', ['winbid'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['winbid_value']
        db.delete_index(u'report_reportstrategyproximicnotice', ['winbid_value'])

        # Removing index on 'ReportStrategyProximicNotice', fields ['net_earned']
        db.delete_index(u'report_reportstrategyproximicnotice', ['net_earned'])

        # Removing index on 'ReportCampaignModel', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignmodel', ['bids_lost'])

        # Removing index on 'ReportCampaignModel', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignmodel', ['data_cost_value'])

        # Removing index on 'ReportCampaignModel', fields ['conv']
        db.delete_index(u'report_reportcampaignmodel', ['conv'])

        # Removing index on 'ReportCampaignModel', fields ['clk']
        db.delete_index(u'report_reportcampaignmodel', ['clk'])

        # Removing index on 'ReportCampaignModel', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignmodel', ['winbid_value_total'])

        # Removing index on 'ReportCampaignModel', fields ['bid']
        db.delete_index(u'report_reportcampaignmodel', ['bid'])

        # Removing index on 'ReportCampaignModel', fields ['conv_value']
        db.delete_index(u'report_reportcampaignmodel', ['conv_value'])

        # Removing index on 'ReportCampaignModel', fields ['bid_value']
        db.delete_index(u'report_reportcampaignmodel', ['bid_value'])

        # Removing index on 'ReportCampaignModel', fields ['imp']
        db.delete_index(u'report_reportcampaignmodel', ['imp'])

        # Removing index on 'ReportCampaignModel', fields ['commission_value']
        db.delete_index(u'report_reportcampaignmodel', ['commission_value'])

        # Removing index on 'ReportCampaignModel', fields ['winbid']
        db.delete_index(u'report_reportcampaignmodel', ['winbid'])

        # Removing index on 'ReportCampaignModel', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignmodel', ['winbid_value'])

        # Removing index on 'ReportCampaignModel', fields ['net_earned']
        db.delete_index(u'report_reportcampaignmodel', ['net_earned'])

        # Removing index on 'ReportCampaignCity', fields ['bids_lost']
        db.delete_index(u'report_reportcampaigncity', ['bids_lost'])

        # Removing index on 'ReportCampaignCity', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaigncity', ['data_cost_value'])

        # Removing index on 'ReportCampaignCity', fields ['conv']
        db.delete_index(u'report_reportcampaigncity', ['conv'])

        # Removing index on 'ReportCampaignCity', fields ['clk']
        db.delete_index(u'report_reportcampaigncity', ['clk'])

        # Removing index on 'ReportCampaignCity', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaigncity', ['winbid_value_total'])

        # Removing index on 'ReportCampaignCity', fields ['bid']
        db.delete_index(u'report_reportcampaigncity', ['bid'])

        # Removing index on 'ReportCampaignCity', fields ['conv_value']
        db.delete_index(u'report_reportcampaigncity', ['conv_value'])

        # Removing index on 'ReportCampaignCity', fields ['bid_value']
        db.delete_index(u'report_reportcampaigncity', ['bid_value'])

        # Removing index on 'ReportCampaignCity', fields ['imp']
        db.delete_index(u'report_reportcampaigncity', ['imp'])

        # Removing index on 'ReportCampaignCity', fields ['commission_value']
        db.delete_index(u'report_reportcampaigncity', ['commission_value'])

        # Removing index on 'ReportCampaignCity', fields ['winbid']
        db.delete_index(u'report_reportcampaigncity', ['winbid'])

        # Removing index on 'ReportCampaignCity', fields ['winbid_value']
        db.delete_index(u'report_reportcampaigncity', ['winbid_value'])

        # Removing index on 'ReportCampaignCity', fields ['net_earned']
        db.delete_index(u'report_reportcampaigncity', ['net_earned'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignpeer39quality', ['bids_lost'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignpeer39quality', ['data_cost_value'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['conv']
        db.delete_index(u'report_reportcampaignpeer39quality', ['conv'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['clk']
        db.delete_index(u'report_reportcampaignpeer39quality', ['clk'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignpeer39quality', ['winbid_value_total'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['bid']
        db.delete_index(u'report_reportcampaignpeer39quality', ['bid'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['conv_value']
        db.delete_index(u'report_reportcampaignpeer39quality', ['conv_value'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['bid_value']
        db.delete_index(u'report_reportcampaignpeer39quality', ['bid_value'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['imp']
        db.delete_index(u'report_reportcampaignpeer39quality', ['imp'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['commission_value']
        db.delete_index(u'report_reportcampaignpeer39quality', ['commission_value'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['winbid']
        db.delete_index(u'report_reportcampaignpeer39quality', ['winbid'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignpeer39quality', ['winbid_value'])

        # Removing index on 'ReportCampaignPeer39Quality', fields ['net_earned']
        db.delete_index(u'report_reportcampaignpeer39quality', ['net_earned'])

        # Removing index on 'ReportCampaignRegion', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignregion', ['bids_lost'])

        # Removing index on 'ReportCampaignRegion', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignregion', ['data_cost_value'])

        # Removing index on 'ReportCampaignRegion', fields ['conv']
        db.delete_index(u'report_reportcampaignregion', ['conv'])

        # Removing index on 'ReportCampaignRegion', fields ['clk']
        db.delete_index(u'report_reportcampaignregion', ['clk'])

        # Removing index on 'ReportCampaignRegion', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignregion', ['winbid_value_total'])

        # Removing index on 'ReportCampaignRegion', fields ['bid']
        db.delete_index(u'report_reportcampaignregion', ['bid'])

        # Removing index on 'ReportCampaignRegion', fields ['conv_value']
        db.delete_index(u'report_reportcampaignregion', ['conv_value'])

        # Removing index on 'ReportCampaignRegion', fields ['bid_value']
        db.delete_index(u'report_reportcampaignregion', ['bid_value'])

        # Removing index on 'ReportCampaignRegion', fields ['imp']
        db.delete_index(u'report_reportcampaignregion', ['imp'])

        # Removing index on 'ReportCampaignRegion', fields ['commission_value']
        db.delete_index(u'report_reportcampaignregion', ['commission_value'])

        # Removing index on 'ReportCampaignRegion', fields ['winbid']
        db.delete_index(u'report_reportcampaignregion', ['winbid'])

        # Removing index on 'ReportCampaignRegion', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignregion', ['winbid_value'])

        # Removing index on 'ReportCampaignRegion', fields ['net_earned']
        db.delete_index(u'report_reportcampaignregion', ['net_earned'])

        # Removing index on 'ReportStrategyMake', fields ['bids_lost']
        db.delete_index(u'report_reportstrategymake', ['bids_lost'])

        # Removing index on 'ReportStrategyMake', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategymake', ['data_cost_value'])

        # Removing index on 'ReportStrategyMake', fields ['conv']
        db.delete_index(u'report_reportstrategymake', ['conv'])

        # Removing index on 'ReportStrategyMake', fields ['clk']
        db.delete_index(u'report_reportstrategymake', ['clk'])

        # Removing index on 'ReportStrategyMake', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategymake', ['winbid_value_total'])

        # Removing index on 'ReportStrategyMake', fields ['bid']
        db.delete_index(u'report_reportstrategymake', ['bid'])

        # Removing index on 'ReportStrategyMake', fields ['conv_value']
        db.delete_index(u'report_reportstrategymake', ['conv_value'])

        # Removing index on 'ReportStrategyMake', fields ['bid_value']
        db.delete_index(u'report_reportstrategymake', ['bid_value'])

        # Removing index on 'ReportStrategyMake', fields ['imp']
        db.delete_index(u'report_reportstrategymake', ['imp'])

        # Removing index on 'ReportStrategyMake', fields ['commission_value']
        db.delete_index(u'report_reportstrategymake', ['commission_value'])

        # Removing index on 'ReportStrategyMake', fields ['winbid']
        db.delete_index(u'report_reportstrategymake', ['winbid'])

        # Removing index on 'ReportStrategyMake', fields ['winbid_value']
        db.delete_index(u'report_reportstrategymake', ['winbid_value'])

        # Removing index on 'ReportStrategyMake', fields ['net_earned']
        db.delete_index(u'report_reportstrategymake', ['net_earned'])

        # Removing index on 'ReportStrategyCity', fields ['bids_lost']
        db.delete_index(u'report_reportstrategycity', ['bids_lost'])

        # Removing index on 'ReportStrategyCity', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategycity', ['data_cost_value'])

        # Removing index on 'ReportStrategyCity', fields ['conv']
        db.delete_index(u'report_reportstrategycity', ['conv'])

        # Removing index on 'ReportStrategyCity', fields ['clk']
        db.delete_index(u'report_reportstrategycity', ['clk'])

        # Removing index on 'ReportStrategyCity', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategycity', ['winbid_value_total'])

        # Removing index on 'ReportStrategyCity', fields ['bid']
        db.delete_index(u'report_reportstrategycity', ['bid'])

        # Removing index on 'ReportStrategyCity', fields ['conv_value']
        db.delete_index(u'report_reportstrategycity', ['conv_value'])

        # Removing index on 'ReportStrategyCity', fields ['bid_value']
        db.delete_index(u'report_reportstrategycity', ['bid_value'])

        # Removing index on 'ReportStrategyCity', fields ['imp']
        db.delete_index(u'report_reportstrategycity', ['imp'])

        # Removing index on 'ReportStrategyCity', fields ['commission_value']
        db.delete_index(u'report_reportstrategycity', ['commission_value'])

        # Removing index on 'ReportStrategyCity', fields ['winbid']
        db.delete_index(u'report_reportstrategycity', ['winbid'])

        # Removing index on 'ReportStrategyCity', fields ['winbid_value']
        db.delete_index(u'report_reportstrategycity', ['winbid_value'])

        # Removing index on 'ReportStrategyCity', fields ['net_earned']
        db.delete_index(u'report_reportstrategycity', ['net_earned'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['bids_lost']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['bids_lost'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['data_cost_value'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['conv']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['conv'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['clk']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['clk'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['winbid_value_total'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['bid']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['bid'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['conv_value']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['conv_value'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['bid_value']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['bid_value'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['imp']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['imp'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['commission_value']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['commission_value'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['winbid']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['winbid'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['winbid_value']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['winbid_value'])

        # Removing index on 'ReportStrategyProximicLanguage', fields ['net_earned']
        db.delete_index(u'report_reportstrategyproximiclanguage', ['net_earned'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignproximicplace', ['bids_lost'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignproximicplace', ['data_cost_value'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['conv']
        db.delete_index(u'report_reportcampaignproximicplace', ['conv'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['clk']
        db.delete_index(u'report_reportcampaignproximicplace', ['clk'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignproximicplace', ['winbid_value_total'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['bid']
        db.delete_index(u'report_reportcampaignproximicplace', ['bid'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['conv_value']
        db.delete_index(u'report_reportcampaignproximicplace', ['conv_value'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['bid_value']
        db.delete_index(u'report_reportcampaignproximicplace', ['bid_value'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['imp']
        db.delete_index(u'report_reportcampaignproximicplace', ['imp'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['commission_value']
        db.delete_index(u'report_reportcampaignproximicplace', ['commission_value'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['winbid']
        db.delete_index(u'report_reportcampaignproximicplace', ['winbid'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignproximicplace', ['winbid_value'])

        # Removing index on 'ReportCampaignProximicPlace', fields ['net_earned']
        db.delete_index(u'report_reportcampaignproximicplace', ['net_earned'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['bids_lost'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['data_cost_value'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['conv']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['conv'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['clk']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['clk'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['winbid_value_total'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['bid']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['bid'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['conv_value']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['conv_value'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['bid_value']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['bid_value'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['imp']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['imp'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['commission_value']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['commission_value'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['winbid']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['winbid'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['winbid_value'])

        # Removing index on 'ReportCampaignProximicLanguage', fields ['net_earned']
        db.delete_index(u'report_reportcampaignproximiclanguage', ['net_earned'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignproximicsafety', ['bids_lost'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignproximicsafety', ['data_cost_value'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['conv']
        db.delete_index(u'report_reportcampaignproximicsafety', ['conv'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['clk']
        db.delete_index(u'report_reportcampaignproximicsafety', ['clk'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignproximicsafety', ['winbid_value_total'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['bid']
        db.delete_index(u'report_reportcampaignproximicsafety', ['bid'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['conv_value']
        db.delete_index(u'report_reportcampaignproximicsafety', ['conv_value'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['bid_value']
        db.delete_index(u'report_reportcampaignproximicsafety', ['bid_value'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['imp']
        db.delete_index(u'report_reportcampaignproximicsafety', ['imp'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['commission_value']
        db.delete_index(u'report_reportcampaignproximicsafety', ['commission_value'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['winbid']
        db.delete_index(u'report_reportcampaignproximicsafety', ['winbid'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignproximicsafety', ['winbid_value'])

        # Removing index on 'ReportCampaignProximicSafety', fields ['net_earned']
        db.delete_index(u'report_reportcampaignproximicsafety', ['net_earned'])

        # Removing index on 'ReportStrategyPosition', fields ['bids_lost']
        db.delete_index(u'report_reportstrategyposition', ['bids_lost'])

        # Removing index on 'ReportStrategyPosition', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategyposition', ['data_cost_value'])

        # Removing index on 'ReportStrategyPosition', fields ['conv']
        db.delete_index(u'report_reportstrategyposition', ['conv'])

        # Removing index on 'ReportStrategyPosition', fields ['clk']
        db.delete_index(u'report_reportstrategyposition', ['clk'])

        # Removing index on 'ReportStrategyPosition', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategyposition', ['winbid_value_total'])

        # Removing index on 'ReportStrategyPosition', fields ['bid']
        db.delete_index(u'report_reportstrategyposition', ['bid'])

        # Removing index on 'ReportStrategyPosition', fields ['conv_value']
        db.delete_index(u'report_reportstrategyposition', ['conv_value'])

        # Removing index on 'ReportStrategyPosition', fields ['bid_value']
        db.delete_index(u'report_reportstrategyposition', ['bid_value'])

        # Removing index on 'ReportStrategyPosition', fields ['imp']
        db.delete_index(u'report_reportstrategyposition', ['imp'])

        # Removing index on 'ReportStrategyPosition', fields ['commission_value']
        db.delete_index(u'report_reportstrategyposition', ['commission_value'])

        # Removing index on 'ReportStrategyPosition', fields ['winbid']
        db.delete_index(u'report_reportstrategyposition', ['winbid'])

        # Removing index on 'ReportStrategyPosition', fields ['winbid_value']
        db.delete_index(u'report_reportstrategyposition', ['winbid_value'])

        # Removing index on 'ReportStrategyPosition', fields ['net_earned']
        db.delete_index(u'report_reportstrategyposition', ['net_earned'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignpeer39brand', ['bids_lost'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignpeer39brand', ['data_cost_value'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['conv']
        db.delete_index(u'report_reportcampaignpeer39brand', ['conv'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['clk']
        db.delete_index(u'report_reportcampaignpeer39brand', ['clk'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignpeer39brand', ['winbid_value_total'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['bid']
        db.delete_index(u'report_reportcampaignpeer39brand', ['bid'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['conv_value']
        db.delete_index(u'report_reportcampaignpeer39brand', ['conv_value'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['bid_value']
        db.delete_index(u'report_reportcampaignpeer39brand', ['bid_value'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['imp']
        db.delete_index(u'report_reportcampaignpeer39brand', ['imp'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['commission_value']
        db.delete_index(u'report_reportcampaignpeer39brand', ['commission_value'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['winbid']
        db.delete_index(u'report_reportcampaignpeer39brand', ['winbid'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignpeer39brand', ['winbid_value'])

        # Removing index on 'ReportCampaignPeer39Brand', fields ['net_earned']
        db.delete_index(u'report_reportcampaignpeer39brand', ['net_earned'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['bids_lost']
        db.delete_index(u'report_reportcampaignproximicquality', ['bids_lost'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['data_cost_value']
        db.delete_index(u'report_reportcampaignproximicquality', ['data_cost_value'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['conv']
        db.delete_index(u'report_reportcampaignproximicquality', ['conv'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['clk']
        db.delete_index(u'report_reportcampaignproximicquality', ['clk'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['winbid_value_total']
        db.delete_index(u'report_reportcampaignproximicquality', ['winbid_value_total'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['bid']
        db.delete_index(u'report_reportcampaignproximicquality', ['bid'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['conv_value']
        db.delete_index(u'report_reportcampaignproximicquality', ['conv_value'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['bid_value']
        db.delete_index(u'report_reportcampaignproximicquality', ['bid_value'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['imp']
        db.delete_index(u'report_reportcampaignproximicquality', ['imp'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['commission_value']
        db.delete_index(u'report_reportcampaignproximicquality', ['commission_value'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['winbid']
        db.delete_index(u'report_reportcampaignproximicquality', ['winbid'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['winbid_value']
        db.delete_index(u'report_reportcampaignproximicquality', ['winbid_value'])

        # Removing index on 'ReportCampaignProximicQuality', fields ['net_earned']
        db.delete_index(u'report_reportcampaignproximicquality', ['net_earned'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['bids_lost']
        db.delete_index(u'report_reportstrategyproximicplace', ['bids_lost'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategyproximicplace', ['data_cost_value'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['conv']
        db.delete_index(u'report_reportstrategyproximicplace', ['conv'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['clk']
        db.delete_index(u'report_reportstrategyproximicplace', ['clk'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategyproximicplace', ['winbid_value_total'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['bid']
        db.delete_index(u'report_reportstrategyproximicplace', ['bid'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['conv_value']
        db.delete_index(u'report_reportstrategyproximicplace', ['conv_value'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['bid_value']
        db.delete_index(u'report_reportstrategyproximicplace', ['bid_value'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['imp']
        db.delete_index(u'report_reportstrategyproximicplace', ['imp'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['commission_value']
        db.delete_index(u'report_reportstrategyproximicplace', ['commission_value'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['winbid']
        db.delete_index(u'report_reportstrategyproximicplace', ['winbid'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['winbid_value']
        db.delete_index(u'report_reportstrategyproximicplace', ['winbid_value'])

        # Removing index on 'ReportStrategyProximicPlace', fields ['net_earned']
        db.delete_index(u'report_reportstrategyproximicplace', ['net_earned'])

        # Removing index on 'ReportStrategySite', fields ['bids_lost']
        db.delete_index(u'report_reportstrategysite', ['bids_lost'])

        # Removing index on 'ReportStrategySite', fields ['data_cost_value']
        db.delete_index(u'report_reportstrategysite', ['data_cost_value'])

        # Removing index on 'ReportStrategySite', fields ['conv']
        db.delete_index(u'report_reportstrategysite', ['conv'])

        # Removing index on 'ReportStrategySite', fields ['clk']
        db.delete_index(u'report_reportstrategysite', ['clk'])

        # Removing index on 'ReportStrategySite', fields ['winbid_value_total']
        db.delete_index(u'report_reportstrategysite', ['winbid_value_total'])

        # Removing index on 'ReportStrategySite', fields ['bid']
        db.delete_index(u'report_reportstrategysite', ['bid'])

        # Removing index on 'ReportStrategySite', fields ['conv_value']
        db.delete_index(u'report_reportstrategysite', ['conv_value'])

        # Removing index on 'ReportStrategySite', fields ['bid_value']
        db.delete_index(u'report_reportstrategysite', ['bid_value'])

        # Removing index on 'ReportStrategySite', fields ['imp']
        db.delete_index(u'report_reportstrategysite', ['imp'])

        # Removing index on 'ReportStrategySite', fields ['commission_value']
        db.delete_index(u'report_reportstrategysite', ['commission_value'])

        # Removing index on 'ReportStrategySite', fields ['winbid']
        db.delete_index(u'report_reportstrategysite', ['winbid'])

        # Removing index on 'ReportStrategySite', fields ['winbid_value']
        db.delete_index(u'report_reportstrategysite', ['winbid_value'])

        # Removing index on 'ReportStrategySite', fields ['net_earned']
        db.delete_index(u'report_reportstrategysite', ['net_earned'])


    def backwards(self, orm):
        # Adding index on 'ReportStrategySite', fields ['net_earned']
        db.create_index(u'report_reportstrategysite', ['net_earned'])

        # Adding index on 'ReportStrategySite', fields ['winbid_value']
        db.create_index(u'report_reportstrategysite', ['winbid_value'])

        # Adding index on 'ReportStrategySite', fields ['winbid']
        db.create_index(u'report_reportstrategysite', ['winbid'])

        # Adding index on 'ReportStrategySite', fields ['commission_value']
        db.create_index(u'report_reportstrategysite', ['commission_value'])

        # Adding index on 'ReportStrategySite', fields ['imp']
        db.create_index(u'report_reportstrategysite', ['imp'])

        # Adding index on 'ReportStrategySite', fields ['bid_value']
        db.create_index(u'report_reportstrategysite', ['bid_value'])

        # Adding index on 'ReportStrategySite', fields ['conv_value']
        db.create_index(u'report_reportstrategysite', ['conv_value'])

        # Adding index on 'ReportStrategySite', fields ['bid']
        db.create_index(u'report_reportstrategysite', ['bid'])

        # Adding index on 'ReportStrategySite', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategysite', ['winbid_value_total'])

        # Adding index on 'ReportStrategySite', fields ['clk']
        db.create_index(u'report_reportstrategysite', ['clk'])

        # Adding index on 'ReportStrategySite', fields ['conv']
        db.create_index(u'report_reportstrategysite', ['conv'])

        # Adding index on 'ReportStrategySite', fields ['data_cost_value']
        db.create_index(u'report_reportstrategysite', ['data_cost_value'])

        # Adding index on 'ReportStrategySite', fields ['bids_lost']
        db.create_index(u'report_reportstrategysite', ['bids_lost'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['net_earned']
        db.create_index(u'report_reportstrategyproximicplace', ['net_earned'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['winbid_value']
        db.create_index(u'report_reportstrategyproximicplace', ['winbid_value'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['winbid']
        db.create_index(u'report_reportstrategyproximicplace', ['winbid'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['commission_value']
        db.create_index(u'report_reportstrategyproximicplace', ['commission_value'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['imp']
        db.create_index(u'report_reportstrategyproximicplace', ['imp'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['bid_value']
        db.create_index(u'report_reportstrategyproximicplace', ['bid_value'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['conv_value']
        db.create_index(u'report_reportstrategyproximicplace', ['conv_value'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['bid']
        db.create_index(u'report_reportstrategyproximicplace', ['bid'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategyproximicplace', ['winbid_value_total'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['clk']
        db.create_index(u'report_reportstrategyproximicplace', ['clk'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['conv']
        db.create_index(u'report_reportstrategyproximicplace', ['conv'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['data_cost_value']
        db.create_index(u'report_reportstrategyproximicplace', ['data_cost_value'])

        # Adding index on 'ReportStrategyProximicPlace', fields ['bids_lost']
        db.create_index(u'report_reportstrategyproximicplace', ['bids_lost'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['net_earned']
        db.create_index(u'report_reportcampaignproximicquality', ['net_earned'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['winbid_value']
        db.create_index(u'report_reportcampaignproximicquality', ['winbid_value'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['winbid']
        db.create_index(u'report_reportcampaignproximicquality', ['winbid'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['commission_value']
        db.create_index(u'report_reportcampaignproximicquality', ['commission_value'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['imp']
        db.create_index(u'report_reportcampaignproximicquality', ['imp'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['bid_value']
        db.create_index(u'report_reportcampaignproximicquality', ['bid_value'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['conv_value']
        db.create_index(u'report_reportcampaignproximicquality', ['conv_value'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['bid']
        db.create_index(u'report_reportcampaignproximicquality', ['bid'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignproximicquality', ['winbid_value_total'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['clk']
        db.create_index(u'report_reportcampaignproximicquality', ['clk'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['conv']
        db.create_index(u'report_reportcampaignproximicquality', ['conv'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignproximicquality', ['data_cost_value'])

        # Adding index on 'ReportCampaignProximicQuality', fields ['bids_lost']
        db.create_index(u'report_reportcampaignproximicquality', ['bids_lost'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['net_earned']
        db.create_index(u'report_reportcampaignpeer39brand', ['net_earned'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['winbid_value']
        db.create_index(u'report_reportcampaignpeer39brand', ['winbid_value'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['winbid']
        db.create_index(u'report_reportcampaignpeer39brand', ['winbid'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['commission_value']
        db.create_index(u'report_reportcampaignpeer39brand', ['commission_value'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['imp']
        db.create_index(u'report_reportcampaignpeer39brand', ['imp'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['bid_value']
        db.create_index(u'report_reportcampaignpeer39brand', ['bid_value'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['conv_value']
        db.create_index(u'report_reportcampaignpeer39brand', ['conv_value'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['bid']
        db.create_index(u'report_reportcampaignpeer39brand', ['bid'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignpeer39brand', ['winbid_value_total'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['clk']
        db.create_index(u'report_reportcampaignpeer39brand', ['clk'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['conv']
        db.create_index(u'report_reportcampaignpeer39brand', ['conv'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignpeer39brand', ['data_cost_value'])

        # Adding index on 'ReportCampaignPeer39Brand', fields ['bids_lost']
        db.create_index(u'report_reportcampaignpeer39brand', ['bids_lost'])

        # Adding index on 'ReportStrategyPosition', fields ['net_earned']
        db.create_index(u'report_reportstrategyposition', ['net_earned'])

        # Adding index on 'ReportStrategyPosition', fields ['winbid_value']
        db.create_index(u'report_reportstrategyposition', ['winbid_value'])

        # Adding index on 'ReportStrategyPosition', fields ['winbid']
        db.create_index(u'report_reportstrategyposition', ['winbid'])

        # Adding index on 'ReportStrategyPosition', fields ['commission_value']
        db.create_index(u'report_reportstrategyposition', ['commission_value'])

        # Adding index on 'ReportStrategyPosition', fields ['imp']
        db.create_index(u'report_reportstrategyposition', ['imp'])

        # Adding index on 'ReportStrategyPosition', fields ['bid_value']
        db.create_index(u'report_reportstrategyposition', ['bid_value'])

        # Adding index on 'ReportStrategyPosition', fields ['conv_value']
        db.create_index(u'report_reportstrategyposition', ['conv_value'])

        # Adding index on 'ReportStrategyPosition', fields ['bid']
        db.create_index(u'report_reportstrategyposition', ['bid'])

        # Adding index on 'ReportStrategyPosition', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategyposition', ['winbid_value_total'])

        # Adding index on 'ReportStrategyPosition', fields ['clk']
        db.create_index(u'report_reportstrategyposition', ['clk'])

        # Adding index on 'ReportStrategyPosition', fields ['conv']
        db.create_index(u'report_reportstrategyposition', ['conv'])

        # Adding index on 'ReportStrategyPosition', fields ['data_cost_value']
        db.create_index(u'report_reportstrategyposition', ['data_cost_value'])

        # Adding index on 'ReportStrategyPosition', fields ['bids_lost']
        db.create_index(u'report_reportstrategyposition', ['bids_lost'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['net_earned']
        db.create_index(u'report_reportcampaignproximicsafety', ['net_earned'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['winbid_value']
        db.create_index(u'report_reportcampaignproximicsafety', ['winbid_value'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['winbid']
        db.create_index(u'report_reportcampaignproximicsafety', ['winbid'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['commission_value']
        db.create_index(u'report_reportcampaignproximicsafety', ['commission_value'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['imp']
        db.create_index(u'report_reportcampaignproximicsafety', ['imp'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['bid_value']
        db.create_index(u'report_reportcampaignproximicsafety', ['bid_value'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['conv_value']
        db.create_index(u'report_reportcampaignproximicsafety', ['conv_value'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['bid']
        db.create_index(u'report_reportcampaignproximicsafety', ['bid'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignproximicsafety', ['winbid_value_total'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['clk']
        db.create_index(u'report_reportcampaignproximicsafety', ['clk'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['conv']
        db.create_index(u'report_reportcampaignproximicsafety', ['conv'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignproximicsafety', ['data_cost_value'])

        # Adding index on 'ReportCampaignProximicSafety', fields ['bids_lost']
        db.create_index(u'report_reportcampaignproximicsafety', ['bids_lost'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['net_earned']
        db.create_index(u'report_reportcampaignproximiclanguage', ['net_earned'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['winbid_value']
        db.create_index(u'report_reportcampaignproximiclanguage', ['winbid_value'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['winbid']
        db.create_index(u'report_reportcampaignproximiclanguage', ['winbid'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['commission_value']
        db.create_index(u'report_reportcampaignproximiclanguage', ['commission_value'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['imp']
        db.create_index(u'report_reportcampaignproximiclanguage', ['imp'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['bid_value']
        db.create_index(u'report_reportcampaignproximiclanguage', ['bid_value'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['conv_value']
        db.create_index(u'report_reportcampaignproximiclanguage', ['conv_value'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['bid']
        db.create_index(u'report_reportcampaignproximiclanguage', ['bid'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignproximiclanguage', ['winbid_value_total'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['clk']
        db.create_index(u'report_reportcampaignproximiclanguage', ['clk'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['conv']
        db.create_index(u'report_reportcampaignproximiclanguage', ['conv'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignproximiclanguage', ['data_cost_value'])

        # Adding index on 'ReportCampaignProximicLanguage', fields ['bids_lost']
        db.create_index(u'report_reportcampaignproximiclanguage', ['bids_lost'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['net_earned']
        db.create_index(u'report_reportcampaignproximicplace', ['net_earned'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['winbid_value']
        db.create_index(u'report_reportcampaignproximicplace', ['winbid_value'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['winbid']
        db.create_index(u'report_reportcampaignproximicplace', ['winbid'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['commission_value']
        db.create_index(u'report_reportcampaignproximicplace', ['commission_value'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['imp']
        db.create_index(u'report_reportcampaignproximicplace', ['imp'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['bid_value']
        db.create_index(u'report_reportcampaignproximicplace', ['bid_value'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['conv_value']
        db.create_index(u'report_reportcampaignproximicplace', ['conv_value'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['bid']
        db.create_index(u'report_reportcampaignproximicplace', ['bid'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignproximicplace', ['winbid_value_total'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['clk']
        db.create_index(u'report_reportcampaignproximicplace', ['clk'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['conv']
        db.create_index(u'report_reportcampaignproximicplace', ['conv'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignproximicplace', ['data_cost_value'])

        # Adding index on 'ReportCampaignProximicPlace', fields ['bids_lost']
        db.create_index(u'report_reportcampaignproximicplace', ['bids_lost'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['net_earned']
        db.create_index(u'report_reportstrategyproximiclanguage', ['net_earned'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['winbid_value']
        db.create_index(u'report_reportstrategyproximiclanguage', ['winbid_value'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['winbid']
        db.create_index(u'report_reportstrategyproximiclanguage', ['winbid'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['commission_value']
        db.create_index(u'report_reportstrategyproximiclanguage', ['commission_value'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['imp']
        db.create_index(u'report_reportstrategyproximiclanguage', ['imp'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['bid_value']
        db.create_index(u'report_reportstrategyproximiclanguage', ['bid_value'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['conv_value']
        db.create_index(u'report_reportstrategyproximiclanguage', ['conv_value'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['bid']
        db.create_index(u'report_reportstrategyproximiclanguage', ['bid'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategyproximiclanguage', ['winbid_value_total'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['clk']
        db.create_index(u'report_reportstrategyproximiclanguage', ['clk'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['conv']
        db.create_index(u'report_reportstrategyproximiclanguage', ['conv'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['data_cost_value']
        db.create_index(u'report_reportstrategyproximiclanguage', ['data_cost_value'])

        # Adding index on 'ReportStrategyProximicLanguage', fields ['bids_lost']
        db.create_index(u'report_reportstrategyproximiclanguage', ['bids_lost'])

        # Adding index on 'ReportStrategyCity', fields ['net_earned']
        db.create_index(u'report_reportstrategycity', ['net_earned'])

        # Adding index on 'ReportStrategyCity', fields ['winbid_value']
        db.create_index(u'report_reportstrategycity', ['winbid_value'])

        # Adding index on 'ReportStrategyCity', fields ['winbid']
        db.create_index(u'report_reportstrategycity', ['winbid'])

        # Adding index on 'ReportStrategyCity', fields ['commission_value']
        db.create_index(u'report_reportstrategycity', ['commission_value'])

        # Adding index on 'ReportStrategyCity', fields ['imp']
        db.create_index(u'report_reportstrategycity', ['imp'])

        # Adding index on 'ReportStrategyCity', fields ['bid_value']
        db.create_index(u'report_reportstrategycity', ['bid_value'])

        # Adding index on 'ReportStrategyCity', fields ['conv_value']
        db.create_index(u'report_reportstrategycity', ['conv_value'])

        # Adding index on 'ReportStrategyCity', fields ['bid']
        db.create_index(u'report_reportstrategycity', ['bid'])

        # Adding index on 'ReportStrategyCity', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategycity', ['winbid_value_total'])

        # Adding index on 'ReportStrategyCity', fields ['clk']
        db.create_index(u'report_reportstrategycity', ['clk'])

        # Adding index on 'ReportStrategyCity', fields ['conv']
        db.create_index(u'report_reportstrategycity', ['conv'])

        # Adding index on 'ReportStrategyCity', fields ['data_cost_value']
        db.create_index(u'report_reportstrategycity', ['data_cost_value'])

        # Adding index on 'ReportStrategyCity', fields ['bids_lost']
        db.create_index(u'report_reportstrategycity', ['bids_lost'])

        # Adding index on 'ReportStrategyMake', fields ['net_earned']
        db.create_index(u'report_reportstrategymake', ['net_earned'])

        # Adding index on 'ReportStrategyMake', fields ['winbid_value']
        db.create_index(u'report_reportstrategymake', ['winbid_value'])

        # Adding index on 'ReportStrategyMake', fields ['winbid']
        db.create_index(u'report_reportstrategymake', ['winbid'])

        # Adding index on 'ReportStrategyMake', fields ['commission_value']
        db.create_index(u'report_reportstrategymake', ['commission_value'])

        # Adding index on 'ReportStrategyMake', fields ['imp']
        db.create_index(u'report_reportstrategymake', ['imp'])

        # Adding index on 'ReportStrategyMake', fields ['bid_value']
        db.create_index(u'report_reportstrategymake', ['bid_value'])

        # Adding index on 'ReportStrategyMake', fields ['conv_value']
        db.create_index(u'report_reportstrategymake', ['conv_value'])

        # Adding index on 'ReportStrategyMake', fields ['bid']
        db.create_index(u'report_reportstrategymake', ['bid'])

        # Adding index on 'ReportStrategyMake', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategymake', ['winbid_value_total'])

        # Adding index on 'ReportStrategyMake', fields ['clk']
        db.create_index(u'report_reportstrategymake', ['clk'])

        # Adding index on 'ReportStrategyMake', fields ['conv']
        db.create_index(u'report_reportstrategymake', ['conv'])

        # Adding index on 'ReportStrategyMake', fields ['data_cost_value']
        db.create_index(u'report_reportstrategymake', ['data_cost_value'])

        # Adding index on 'ReportStrategyMake', fields ['bids_lost']
        db.create_index(u'report_reportstrategymake', ['bids_lost'])

        # Adding index on 'ReportCampaignRegion', fields ['net_earned']
        db.create_index(u'report_reportcampaignregion', ['net_earned'])

        # Adding index on 'ReportCampaignRegion', fields ['winbid_value']
        db.create_index(u'report_reportcampaignregion', ['winbid_value'])

        # Adding index on 'ReportCampaignRegion', fields ['winbid']
        db.create_index(u'report_reportcampaignregion', ['winbid'])

        # Adding index on 'ReportCampaignRegion', fields ['commission_value']
        db.create_index(u'report_reportcampaignregion', ['commission_value'])

        # Adding index on 'ReportCampaignRegion', fields ['imp']
        db.create_index(u'report_reportcampaignregion', ['imp'])

        # Adding index on 'ReportCampaignRegion', fields ['bid_value']
        db.create_index(u'report_reportcampaignregion', ['bid_value'])

        # Adding index on 'ReportCampaignRegion', fields ['conv_value']
        db.create_index(u'report_reportcampaignregion', ['conv_value'])

        # Adding index on 'ReportCampaignRegion', fields ['bid']
        db.create_index(u'report_reportcampaignregion', ['bid'])

        # Adding index on 'ReportCampaignRegion', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignregion', ['winbid_value_total'])

        # Adding index on 'ReportCampaignRegion', fields ['clk']
        db.create_index(u'report_reportcampaignregion', ['clk'])

        # Adding index on 'ReportCampaignRegion', fields ['conv']
        db.create_index(u'report_reportcampaignregion', ['conv'])

        # Adding index on 'ReportCampaignRegion', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignregion', ['data_cost_value'])

        # Adding index on 'ReportCampaignRegion', fields ['bids_lost']
        db.create_index(u'report_reportcampaignregion', ['bids_lost'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['net_earned']
        db.create_index(u'report_reportcampaignpeer39quality', ['net_earned'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['winbid_value']
        db.create_index(u'report_reportcampaignpeer39quality', ['winbid_value'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['winbid']
        db.create_index(u'report_reportcampaignpeer39quality', ['winbid'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['commission_value']
        db.create_index(u'report_reportcampaignpeer39quality', ['commission_value'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['imp']
        db.create_index(u'report_reportcampaignpeer39quality', ['imp'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['bid_value']
        db.create_index(u'report_reportcampaignpeer39quality', ['bid_value'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['conv_value']
        db.create_index(u'report_reportcampaignpeer39quality', ['conv_value'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['bid']
        db.create_index(u'report_reportcampaignpeer39quality', ['bid'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignpeer39quality', ['winbid_value_total'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['clk']
        db.create_index(u'report_reportcampaignpeer39quality', ['clk'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['conv']
        db.create_index(u'report_reportcampaignpeer39quality', ['conv'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignpeer39quality', ['data_cost_value'])

        # Adding index on 'ReportCampaignPeer39Quality', fields ['bids_lost']
        db.create_index(u'report_reportcampaignpeer39quality', ['bids_lost'])

        # Adding index on 'ReportCampaignCity', fields ['net_earned']
        db.create_index(u'report_reportcampaigncity', ['net_earned'])

        # Adding index on 'ReportCampaignCity', fields ['winbid_value']
        db.create_index(u'report_reportcampaigncity', ['winbid_value'])

        # Adding index on 'ReportCampaignCity', fields ['winbid']
        db.create_index(u'report_reportcampaigncity', ['winbid'])

        # Adding index on 'ReportCampaignCity', fields ['commission_value']
        db.create_index(u'report_reportcampaigncity', ['commission_value'])

        # Adding index on 'ReportCampaignCity', fields ['imp']
        db.create_index(u'report_reportcampaigncity', ['imp'])

        # Adding index on 'ReportCampaignCity', fields ['bid_value']
        db.create_index(u'report_reportcampaigncity', ['bid_value'])

        # Adding index on 'ReportCampaignCity', fields ['conv_value']
        db.create_index(u'report_reportcampaigncity', ['conv_value'])

        # Adding index on 'ReportCampaignCity', fields ['bid']
        db.create_index(u'report_reportcampaigncity', ['bid'])

        # Adding index on 'ReportCampaignCity', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaigncity', ['winbid_value_total'])

        # Adding index on 'ReportCampaignCity', fields ['clk']
        db.create_index(u'report_reportcampaigncity', ['clk'])

        # Adding index on 'ReportCampaignCity', fields ['conv']
        db.create_index(u'report_reportcampaigncity', ['conv'])

        # Adding index on 'ReportCampaignCity', fields ['data_cost_value']
        db.create_index(u'report_reportcampaigncity', ['data_cost_value'])

        # Adding index on 'ReportCampaignCity', fields ['bids_lost']
        db.create_index(u'report_reportcampaigncity', ['bids_lost'])

        # Adding index on 'ReportCampaignModel', fields ['net_earned']
        db.create_index(u'report_reportcampaignmodel', ['net_earned'])

        # Adding index on 'ReportCampaignModel', fields ['winbid_value']
        db.create_index(u'report_reportcampaignmodel', ['winbid_value'])

        # Adding index on 'ReportCampaignModel', fields ['winbid']
        db.create_index(u'report_reportcampaignmodel', ['winbid'])

        # Adding index on 'ReportCampaignModel', fields ['commission_value']
        db.create_index(u'report_reportcampaignmodel', ['commission_value'])

        # Adding index on 'ReportCampaignModel', fields ['imp']
        db.create_index(u'report_reportcampaignmodel', ['imp'])

        # Adding index on 'ReportCampaignModel', fields ['bid_value']
        db.create_index(u'report_reportcampaignmodel', ['bid_value'])

        # Adding index on 'ReportCampaignModel', fields ['conv_value']
        db.create_index(u'report_reportcampaignmodel', ['conv_value'])

        # Adding index on 'ReportCampaignModel', fields ['bid']
        db.create_index(u'report_reportcampaignmodel', ['bid'])

        # Adding index on 'ReportCampaignModel', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignmodel', ['winbid_value_total'])

        # Adding index on 'ReportCampaignModel', fields ['clk']
        db.create_index(u'report_reportcampaignmodel', ['clk'])

        # Adding index on 'ReportCampaignModel', fields ['conv']
        db.create_index(u'report_reportcampaignmodel', ['conv'])

        # Adding index on 'ReportCampaignModel', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignmodel', ['data_cost_value'])

        # Adding index on 'ReportCampaignModel', fields ['bids_lost']
        db.create_index(u'report_reportcampaignmodel', ['bids_lost'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['net_earned']
        db.create_index(u'report_reportstrategyproximicnotice', ['net_earned'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['winbid_value']
        db.create_index(u'report_reportstrategyproximicnotice', ['winbid_value'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['winbid']
        db.create_index(u'report_reportstrategyproximicnotice', ['winbid'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['commission_value']
        db.create_index(u'report_reportstrategyproximicnotice', ['commission_value'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['imp']
        db.create_index(u'report_reportstrategyproximicnotice', ['imp'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['bid_value']
        db.create_index(u'report_reportstrategyproximicnotice', ['bid_value'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['conv_value']
        db.create_index(u'report_reportstrategyproximicnotice', ['conv_value'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['bid']
        db.create_index(u'report_reportstrategyproximicnotice', ['bid'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategyproximicnotice', ['winbid_value_total'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['clk']
        db.create_index(u'report_reportstrategyproximicnotice', ['clk'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['conv']
        db.create_index(u'report_reportstrategyproximicnotice', ['conv'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['data_cost_value']
        db.create_index(u'report_reportstrategyproximicnotice', ['data_cost_value'])

        # Adding index on 'ReportStrategyProximicNotice', fields ['bids_lost']
        db.create_index(u'report_reportstrategyproximicnotice', ['bids_lost'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['net_earned']
        db.create_index(u'report_reportstrategypeer39quality', ['net_earned'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['winbid_value']
        db.create_index(u'report_reportstrategypeer39quality', ['winbid_value'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['winbid']
        db.create_index(u'report_reportstrategypeer39quality', ['winbid'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['commission_value']
        db.create_index(u'report_reportstrategypeer39quality', ['commission_value'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['imp']
        db.create_index(u'report_reportstrategypeer39quality', ['imp'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['bid_value']
        db.create_index(u'report_reportstrategypeer39quality', ['bid_value'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['conv_value']
        db.create_index(u'report_reportstrategypeer39quality', ['conv_value'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['bid']
        db.create_index(u'report_reportstrategypeer39quality', ['bid'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategypeer39quality', ['winbid_value_total'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['clk']
        db.create_index(u'report_reportstrategypeer39quality', ['clk'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['conv']
        db.create_index(u'report_reportstrategypeer39quality', ['conv'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['data_cost_value']
        db.create_index(u'report_reportstrategypeer39quality', ['data_cost_value'])

        # Adding index on 'ReportStrategyPeer39Quality', fields ['bids_lost']
        db.create_index(u'report_reportstrategypeer39quality', ['bids_lost'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['net_earned']
        db.create_index(u'report_reportcampaignpeer39contextual', ['net_earned'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['winbid_value']
        db.create_index(u'report_reportcampaignpeer39contextual', ['winbid_value'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['winbid']
        db.create_index(u'report_reportcampaignpeer39contextual', ['winbid'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['commission_value']
        db.create_index(u'report_reportcampaignpeer39contextual', ['commission_value'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['imp']
        db.create_index(u'report_reportcampaignpeer39contextual', ['imp'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['bid_value']
        db.create_index(u'report_reportcampaignpeer39contextual', ['bid_value'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['conv_value']
        db.create_index(u'report_reportcampaignpeer39contextual', ['conv_value'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['bid']
        db.create_index(u'report_reportcampaignpeer39contextual', ['bid'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignpeer39contextual', ['winbid_value_total'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['clk']
        db.create_index(u'report_reportcampaignpeer39contextual', ['clk'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['conv']
        db.create_index(u'report_reportcampaignpeer39contextual', ['conv'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignpeer39contextual', ['data_cost_value'])

        # Adding index on 'ReportCampaignPeer39Contextual', fields ['bids_lost']
        db.create_index(u'report_reportcampaignpeer39contextual', ['bids_lost'])

        # Adding index on 'ReportStrategyModel', fields ['net_earned']
        db.create_index(u'report_reportstrategymodel', ['net_earned'])

        # Adding index on 'ReportStrategyModel', fields ['winbid_value']
        db.create_index(u'report_reportstrategymodel', ['winbid_value'])

        # Adding index on 'ReportStrategyModel', fields ['winbid']
        db.create_index(u'report_reportstrategymodel', ['winbid'])

        # Adding index on 'ReportStrategyModel', fields ['commission_value']
        db.create_index(u'report_reportstrategymodel', ['commission_value'])

        # Adding index on 'ReportStrategyModel', fields ['imp']
        db.create_index(u'report_reportstrategymodel', ['imp'])

        # Adding index on 'ReportStrategyModel', fields ['bid_value']
        db.create_index(u'report_reportstrategymodel', ['bid_value'])

        # Adding index on 'ReportStrategyModel', fields ['conv_value']
        db.create_index(u'report_reportstrategymodel', ['conv_value'])

        # Adding index on 'ReportStrategyModel', fields ['bid']
        db.create_index(u'report_reportstrategymodel', ['bid'])

        # Adding index on 'ReportStrategyModel', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategymodel', ['winbid_value_total'])

        # Adding index on 'ReportStrategyModel', fields ['clk']
        db.create_index(u'report_reportstrategymodel', ['clk'])

        # Adding index on 'ReportStrategyModel', fields ['conv']
        db.create_index(u'report_reportstrategymodel', ['conv'])

        # Adding index on 'ReportStrategyModel', fields ['data_cost_value']
        db.create_index(u'report_reportstrategymodel', ['data_cost_value'])

        # Adding index on 'ReportStrategyModel', fields ['bids_lost']
        db.create_index(u'report_reportstrategymodel', ['bids_lost'])

        # Adding index on 'ReportStrategy', fields ['net_earned']
        db.create_index(u'report_reportstrategy', ['net_earned'])

        # Adding index on 'ReportStrategy', fields ['winbid_value']
        db.create_index(u'report_reportstrategy', ['winbid_value'])

        # Adding index on 'ReportStrategy', fields ['winbid']
        db.create_index(u'report_reportstrategy', ['winbid'])

        # Adding index on 'ReportStrategy', fields ['commission_value']
        db.create_index(u'report_reportstrategy', ['commission_value'])

        # Adding index on 'ReportStrategy', fields ['imp']
        db.create_index(u'report_reportstrategy', ['imp'])

        # Adding index on 'ReportStrategy', fields ['bid_value']
        db.create_index(u'report_reportstrategy', ['bid_value'])

        # Adding index on 'ReportStrategy', fields ['conv_value']
        db.create_index(u'report_reportstrategy', ['conv_value'])

        # Adding index on 'ReportStrategy', fields ['bid']
        db.create_index(u'report_reportstrategy', ['bid'])

        # Adding index on 'ReportStrategy', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategy', ['winbid_value_total'])

        # Adding index on 'ReportStrategy', fields ['clk']
        db.create_index(u'report_reportstrategy', ['clk'])

        # Adding index on 'ReportStrategy', fields ['conv']
        db.create_index(u'report_reportstrategy', ['conv'])

        # Adding index on 'ReportStrategy', fields ['data_cost_value']
        db.create_index(u'report_reportstrategy', ['data_cost_value'])

        # Adding index on 'ReportStrategy', fields ['bids_lost']
        db.create_index(u'report_reportstrategy', ['bids_lost'])

        # Adding index on 'ReportStrategyPublisher', fields ['net_earned']
        db.create_index(u'report_reportstrategypublisher', ['net_earned'])

        # Adding index on 'ReportStrategyPublisher', fields ['winbid_value']
        db.create_index(u'report_reportstrategypublisher', ['winbid_value'])

        # Adding index on 'ReportStrategyPublisher', fields ['winbid']
        db.create_index(u'report_reportstrategypublisher', ['winbid'])

        # Adding index on 'ReportStrategyPublisher', fields ['commission_value']
        db.create_index(u'report_reportstrategypublisher', ['commission_value'])

        # Adding index on 'ReportStrategyPublisher', fields ['imp']
        db.create_index(u'report_reportstrategypublisher', ['imp'])

        # Adding index on 'ReportStrategyPublisher', fields ['bid_value']
        db.create_index(u'report_reportstrategypublisher', ['bid_value'])

        # Adding index on 'ReportStrategyPublisher', fields ['conv_value']
        db.create_index(u'report_reportstrategypublisher', ['conv_value'])

        # Adding index on 'ReportStrategyPublisher', fields ['bid']
        db.create_index(u'report_reportstrategypublisher', ['bid'])

        # Adding index on 'ReportStrategyPublisher', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategypublisher', ['winbid_value_total'])

        # Adding index on 'ReportStrategyPublisher', fields ['clk']
        db.create_index(u'report_reportstrategypublisher', ['clk'])

        # Adding index on 'ReportStrategyPublisher', fields ['conv']
        db.create_index(u'report_reportstrategypublisher', ['conv'])

        # Adding index on 'ReportStrategyPublisher', fields ['data_cost_value']
        db.create_index(u'report_reportstrategypublisher', ['data_cost_value'])

        # Adding index on 'ReportStrategyPublisher', fields ['bids_lost']
        db.create_index(u'report_reportstrategypublisher', ['bids_lost'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['net_earned']
        db.create_index(u'report_reportstrategyproximicsafety', ['net_earned'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['winbid_value']
        db.create_index(u'report_reportstrategyproximicsafety', ['winbid_value'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['winbid']
        db.create_index(u'report_reportstrategyproximicsafety', ['winbid'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['commission_value']
        db.create_index(u'report_reportstrategyproximicsafety', ['commission_value'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['imp']
        db.create_index(u'report_reportstrategyproximicsafety', ['imp'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['bid_value']
        db.create_index(u'report_reportstrategyproximicsafety', ['bid_value'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['conv_value']
        db.create_index(u'report_reportstrategyproximicsafety', ['conv_value'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['bid']
        db.create_index(u'report_reportstrategyproximicsafety', ['bid'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategyproximicsafety', ['winbid_value_total'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['clk']
        db.create_index(u'report_reportstrategyproximicsafety', ['clk'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['conv']
        db.create_index(u'report_reportstrategyproximicsafety', ['conv'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['data_cost_value']
        db.create_index(u'report_reportstrategyproximicsafety', ['data_cost_value'])

        # Adding index on 'ReportStrategyProximicSafety', fields ['bids_lost']
        db.create_index(u'report_reportstrategyproximicsafety', ['bids_lost'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['net_earned']
        db.create_index(u'report_reportstrategypeer39brand', ['net_earned'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['winbid_value']
        db.create_index(u'report_reportstrategypeer39brand', ['winbid_value'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['winbid']
        db.create_index(u'report_reportstrategypeer39brand', ['winbid'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['commission_value']
        db.create_index(u'report_reportstrategypeer39brand', ['commission_value'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['imp']
        db.create_index(u'report_reportstrategypeer39brand', ['imp'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['bid_value']
        db.create_index(u'report_reportstrategypeer39brand', ['bid_value'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['conv_value']
        db.create_index(u'report_reportstrategypeer39brand', ['conv_value'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['bid']
        db.create_index(u'report_reportstrategypeer39brand', ['bid'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategypeer39brand', ['winbid_value_total'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['clk']
        db.create_index(u'report_reportstrategypeer39brand', ['clk'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['conv']
        db.create_index(u'report_reportstrategypeer39brand', ['conv'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['data_cost_value']
        db.create_index(u'report_reportstrategypeer39brand', ['data_cost_value'])

        # Adding index on 'ReportStrategyPeer39Brand', fields ['bids_lost']
        db.create_index(u'report_reportstrategypeer39brand', ['bids_lost'])

        # Adding index on 'ReportCampaignOs', fields ['net_earned']
        db.create_index(u'report_reportcampaignos', ['net_earned'])

        # Adding index on 'ReportCampaignOs', fields ['winbid_value']
        db.create_index(u'report_reportcampaignos', ['winbid_value'])

        # Adding index on 'ReportCampaignOs', fields ['winbid']
        db.create_index(u'report_reportcampaignos', ['winbid'])

        # Adding index on 'ReportCampaignOs', fields ['commission_value']
        db.create_index(u'report_reportcampaignos', ['commission_value'])

        # Adding index on 'ReportCampaignOs', fields ['imp']
        db.create_index(u'report_reportcampaignos', ['imp'])

        # Adding index on 'ReportCampaignOs', fields ['bid_value']
        db.create_index(u'report_reportcampaignos', ['bid_value'])

        # Adding index on 'ReportCampaignOs', fields ['conv_value']
        db.create_index(u'report_reportcampaignos', ['conv_value'])

        # Adding index on 'ReportCampaignOs', fields ['bid']
        db.create_index(u'report_reportcampaignos', ['bid'])

        # Adding index on 'ReportCampaignOs', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignos', ['winbid_value_total'])

        # Adding index on 'ReportCampaignOs', fields ['clk']
        db.create_index(u'report_reportcampaignos', ['clk'])

        # Adding index on 'ReportCampaignOs', fields ['conv']
        db.create_index(u'report_reportcampaignos', ['conv'])

        # Adding index on 'ReportCampaignOs', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignos', ['data_cost_value'])

        # Adding index on 'ReportCampaignOs', fields ['bids_lost']
        db.create_index(u'report_reportcampaignos', ['bids_lost'])

        # Adding index on 'ReportStrategyCarrier', fields ['net_earned']
        db.create_index(u'report_reportstrategycarrier', ['net_earned'])

        # Adding index on 'ReportStrategyCarrier', fields ['winbid_value']
        db.create_index(u'report_reportstrategycarrier', ['winbid_value'])

        # Adding index on 'ReportStrategyCarrier', fields ['winbid']
        db.create_index(u'report_reportstrategycarrier', ['winbid'])

        # Adding index on 'ReportStrategyCarrier', fields ['commission_value']
        db.create_index(u'report_reportstrategycarrier', ['commission_value'])

        # Adding index on 'ReportStrategyCarrier', fields ['imp']
        db.create_index(u'report_reportstrategycarrier', ['imp'])

        # Adding index on 'ReportStrategyCarrier', fields ['bid_value']
        db.create_index(u'report_reportstrategycarrier', ['bid_value'])

        # Adding index on 'ReportStrategyCarrier', fields ['conv_value']
        db.create_index(u'report_reportstrategycarrier', ['conv_value'])

        # Adding index on 'ReportStrategyCarrier', fields ['bid']
        db.create_index(u'report_reportstrategycarrier', ['bid'])

        # Adding index on 'ReportStrategyCarrier', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategycarrier', ['winbid_value_total'])

        # Adding index on 'ReportStrategyCarrier', fields ['clk']
        db.create_index(u'report_reportstrategycarrier', ['clk'])

        # Adding index on 'ReportStrategyCarrier', fields ['conv']
        db.create_index(u'report_reportstrategycarrier', ['conv'])

        # Adding index on 'ReportStrategyCarrier', fields ['data_cost_value']
        db.create_index(u'report_reportstrategycarrier', ['data_cost_value'])

        # Adding index on 'ReportStrategyCarrier', fields ['bids_lost']
        db.create_index(u'report_reportstrategycarrier', ['bids_lost'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['net_earned']
        db.create_index(u'report_reportcampaignpeer39language', ['net_earned'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['winbid_value']
        db.create_index(u'report_reportcampaignpeer39language', ['winbid_value'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['winbid']
        db.create_index(u'report_reportcampaignpeer39language', ['winbid'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['commission_value']
        db.create_index(u'report_reportcampaignpeer39language', ['commission_value'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['imp']
        db.create_index(u'report_reportcampaignpeer39language', ['imp'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['bid_value']
        db.create_index(u'report_reportcampaignpeer39language', ['bid_value'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['conv_value']
        db.create_index(u'report_reportcampaignpeer39language', ['conv_value'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['bid']
        db.create_index(u'report_reportcampaignpeer39language', ['bid'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignpeer39language', ['winbid_value_total'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['clk']
        db.create_index(u'report_reportcampaignpeer39language', ['clk'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['conv']
        db.create_index(u'report_reportcampaignpeer39language', ['conv'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignpeer39language', ['data_cost_value'])

        # Adding index on 'ReportCampaignPeer39Language', fields ['bids_lost']
        db.create_index(u'report_reportcampaignpeer39language', ['bids_lost'])

        # Adding index on 'ReportAdvert', fields ['net_earned']
        db.create_index(u'report_reportadvert', ['net_earned'])

        # Adding index on 'ReportAdvert', fields ['winbid_value']
        db.create_index(u'report_reportadvert', ['winbid_value'])

        # Adding index on 'ReportAdvert', fields ['winbid']
        db.create_index(u'report_reportadvert', ['winbid'])

        # Adding index on 'ReportAdvert', fields ['commission_value']
        db.create_index(u'report_reportadvert', ['commission_value'])

        # Adding index on 'ReportAdvert', fields ['imp']
        db.create_index(u'report_reportadvert', ['imp'])

        # Adding index on 'ReportAdvert', fields ['bid_value']
        db.create_index(u'report_reportadvert', ['bid_value'])

        # Adding index on 'ReportAdvert', fields ['conv_value']
        db.create_index(u'report_reportadvert', ['conv_value'])

        # Adding index on 'ReportAdvert', fields ['bid']
        db.create_index(u'report_reportadvert', ['bid'])

        # Adding index on 'ReportAdvert', fields ['winbid_value_total']
        db.create_index(u'report_reportadvert', ['winbid_value_total'])

        # Adding index on 'ReportAdvert', fields ['clk']
        db.create_index(u'report_reportadvert', ['clk'])

        # Adding index on 'ReportAdvert', fields ['conv']
        db.create_index(u'report_reportadvert', ['conv'])

        # Adding index on 'ReportAdvert', fields ['data_cost_value']
        db.create_index(u'report_reportadvert', ['data_cost_value'])

        # Adding index on 'ReportAdvert', fields ['bids_lost']
        db.create_index(u'report_reportadvert', ['bids_lost'])

        # Adding index on 'ReportStrategyGender', fields ['net_earned']
        db.create_index(u'report_reportstrategygender', ['net_earned'])

        # Adding index on 'ReportStrategyGender', fields ['winbid_value']
        db.create_index(u'report_reportstrategygender', ['winbid_value'])

        # Adding index on 'ReportStrategyGender', fields ['winbid']
        db.create_index(u'report_reportstrategygender', ['winbid'])

        # Adding index on 'ReportStrategyGender', fields ['commission_value']
        db.create_index(u'report_reportstrategygender', ['commission_value'])

        # Adding index on 'ReportStrategyGender', fields ['imp']
        db.create_index(u'report_reportstrategygender', ['imp'])

        # Adding index on 'ReportStrategyGender', fields ['bid_value']
        db.create_index(u'report_reportstrategygender', ['bid_value'])

        # Adding index on 'ReportStrategyGender', fields ['conv_value']
        db.create_index(u'report_reportstrategygender', ['conv_value'])

        # Adding index on 'ReportStrategyGender', fields ['bid']
        db.create_index(u'report_reportstrategygender', ['bid'])

        # Adding index on 'ReportStrategyGender', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategygender', ['winbid_value_total'])

        # Adding index on 'ReportStrategyGender', fields ['clk']
        db.create_index(u'report_reportstrategygender', ['clk'])

        # Adding index on 'ReportStrategyGender', fields ['conv']
        db.create_index(u'report_reportstrategygender', ['conv'])

        # Adding index on 'ReportStrategyGender', fields ['data_cost_value']
        db.create_index(u'report_reportstrategygender', ['data_cost_value'])

        # Adding index on 'ReportStrategyGender', fields ['bids_lost']
        db.create_index(u'report_reportstrategygender', ['bids_lost'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['net_earned']
        db.create_index(u'report_reportstrategyproximicmaturity', ['net_earned'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['winbid_value']
        db.create_index(u'report_reportstrategyproximicmaturity', ['winbid_value'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['winbid']
        db.create_index(u'report_reportstrategyproximicmaturity', ['winbid'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['commission_value']
        db.create_index(u'report_reportstrategyproximicmaturity', ['commission_value'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['imp']
        db.create_index(u'report_reportstrategyproximicmaturity', ['imp'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['bid_value']
        db.create_index(u'report_reportstrategyproximicmaturity', ['bid_value'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['conv_value']
        db.create_index(u'report_reportstrategyproximicmaturity', ['conv_value'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['bid']
        db.create_index(u'report_reportstrategyproximicmaturity', ['bid'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategyproximicmaturity', ['winbid_value_total'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['clk']
        db.create_index(u'report_reportstrategyproximicmaturity', ['clk'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['conv']
        db.create_index(u'report_reportstrategyproximicmaturity', ['conv'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['data_cost_value']
        db.create_index(u'report_reportstrategyproximicmaturity', ['data_cost_value'])

        # Adding index on 'ReportStrategyProximicMaturity', fields ['bids_lost']
        db.create_index(u'report_reportstrategyproximicmaturity', ['bids_lost'])

        # Adding index on 'ReportCampaignCountry', fields ['net_earned']
        db.create_index(u'report_reportcampaigncountry', ['net_earned'])

        # Adding index on 'ReportCampaignCountry', fields ['winbid_value']
        db.create_index(u'report_reportcampaigncountry', ['winbid_value'])

        # Adding index on 'ReportCampaignCountry', fields ['winbid']
        db.create_index(u'report_reportcampaigncountry', ['winbid'])

        # Adding index on 'ReportCampaignCountry', fields ['commission_value']
        db.create_index(u'report_reportcampaigncountry', ['commission_value'])

        # Adding index on 'ReportCampaignCountry', fields ['imp']
        db.create_index(u'report_reportcampaigncountry', ['imp'])

        # Adding index on 'ReportCampaignCountry', fields ['bid_value']
        db.create_index(u'report_reportcampaigncountry', ['bid_value'])

        # Adding index on 'ReportCampaignCountry', fields ['conv_value']
        db.create_index(u'report_reportcampaigncountry', ['conv_value'])

        # Adding index on 'ReportCampaignCountry', fields ['bid']
        db.create_index(u'report_reportcampaigncountry', ['bid'])

        # Adding index on 'ReportCampaignCountry', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaigncountry', ['winbid_value_total'])

        # Adding index on 'ReportCampaignCountry', fields ['clk']
        db.create_index(u'report_reportcampaigncountry', ['clk'])

        # Adding index on 'ReportCampaignCountry', fields ['conv']
        db.create_index(u'report_reportcampaigncountry', ['conv'])

        # Adding index on 'ReportCampaignCountry', fields ['data_cost_value']
        db.create_index(u'report_reportcampaigncountry', ['data_cost_value'])

        # Adding index on 'ReportCampaignCountry', fields ['bids_lost']
        db.create_index(u'report_reportcampaigncountry', ['bids_lost'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['net_earned']
        db.create_index(u'report_reportcampaignpublishernetwork', ['net_earned'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['winbid_value']
        db.create_index(u'report_reportcampaignpublishernetwork', ['winbid_value'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['winbid']
        db.create_index(u'report_reportcampaignpublishernetwork', ['winbid'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['commission_value']
        db.create_index(u'report_reportcampaignpublishernetwork', ['commission_value'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['imp']
        db.create_index(u'report_reportcampaignpublishernetwork', ['imp'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['bid_value']
        db.create_index(u'report_reportcampaignpublishernetwork', ['bid_value'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['conv_value']
        db.create_index(u'report_reportcampaignpublishernetwork', ['conv_value'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['bid']
        db.create_index(u'report_reportcampaignpublishernetwork', ['bid'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignpublishernetwork', ['winbid_value_total'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['clk']
        db.create_index(u'report_reportcampaignpublishernetwork', ['clk'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['conv']
        db.create_index(u'report_reportcampaignpublishernetwork', ['conv'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignpublishernetwork', ['data_cost_value'])

        # Adding index on 'ReportCampaignPublisherNetwork', fields ['bids_lost']
        db.create_index(u'report_reportcampaignpublishernetwork', ['bids_lost'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['net_earned']
        db.create_index(u'report_reportcampaignproximicmaturity', ['net_earned'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['winbid_value']
        db.create_index(u'report_reportcampaignproximicmaturity', ['winbid_value'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['winbid']
        db.create_index(u'report_reportcampaignproximicmaturity', ['winbid'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['commission_value']
        db.create_index(u'report_reportcampaignproximicmaturity', ['commission_value'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['imp']
        db.create_index(u'report_reportcampaignproximicmaturity', ['imp'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['bid_value']
        db.create_index(u'report_reportcampaignproximicmaturity', ['bid_value'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['conv_value']
        db.create_index(u'report_reportcampaignproximicmaturity', ['conv_value'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['bid']
        db.create_index(u'report_reportcampaignproximicmaturity', ['bid'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignproximicmaturity', ['winbid_value_total'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['clk']
        db.create_index(u'report_reportcampaignproximicmaturity', ['clk'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['conv']
        db.create_index(u'report_reportcampaignproximicmaturity', ['conv'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignproximicmaturity', ['data_cost_value'])

        # Adding index on 'ReportCampaignProximicMaturity', fields ['bids_lost']
        db.create_index(u'report_reportcampaignproximicmaturity', ['bids_lost'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['net_earned']
        db.create_index(u'report_reportstrategypeer39contextual', ['net_earned'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['winbid_value']
        db.create_index(u'report_reportstrategypeer39contextual', ['winbid_value'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['winbid']
        db.create_index(u'report_reportstrategypeer39contextual', ['winbid'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['commission_value']
        db.create_index(u'report_reportstrategypeer39contextual', ['commission_value'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['imp']
        db.create_index(u'report_reportstrategypeer39contextual', ['imp'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['bid_value']
        db.create_index(u'report_reportstrategypeer39contextual', ['bid_value'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['conv_value']
        db.create_index(u'report_reportstrategypeer39contextual', ['conv_value'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['bid']
        db.create_index(u'report_reportstrategypeer39contextual', ['bid'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategypeer39contextual', ['winbid_value_total'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['clk']
        db.create_index(u'report_reportstrategypeer39contextual', ['clk'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['conv']
        db.create_index(u'report_reportstrategypeer39contextual', ['conv'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['data_cost_value']
        db.create_index(u'report_reportstrategypeer39contextual', ['data_cost_value'])

        # Adding index on 'ReportStrategyPeer39Contextual', fields ['bids_lost']
        db.create_index(u'report_reportstrategypeer39contextual', ['bids_lost'])

        # Adding index on 'ReportCampaignSite', fields ['net_earned']
        db.create_index(u'report_reportcampaignsite', ['net_earned'])

        # Adding index on 'ReportCampaignSite', fields ['winbid_value']
        db.create_index(u'report_reportcampaignsite', ['winbid_value'])

        # Adding index on 'ReportCampaignSite', fields ['winbid']
        db.create_index(u'report_reportcampaignsite', ['winbid'])

        # Adding index on 'ReportCampaignSite', fields ['commission_value']
        db.create_index(u'report_reportcampaignsite', ['commission_value'])

        # Adding index on 'ReportCampaignSite', fields ['imp']
        db.create_index(u'report_reportcampaignsite', ['imp'])

        # Adding index on 'ReportCampaignSite', fields ['bid_value']
        db.create_index(u'report_reportcampaignsite', ['bid_value'])

        # Adding index on 'ReportCampaignSite', fields ['conv_value']
        db.create_index(u'report_reportcampaignsite', ['conv_value'])

        # Adding index on 'ReportCampaignSite', fields ['bid']
        db.create_index(u'report_reportcampaignsite', ['bid'])

        # Adding index on 'ReportCampaignSite', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignsite', ['winbid_value_total'])

        # Adding index on 'ReportCampaignSite', fields ['clk']
        db.create_index(u'report_reportcampaignsite', ['clk'])

        # Adding index on 'ReportCampaignSite', fields ['conv']
        db.create_index(u'report_reportcampaignsite', ['conv'])

        # Adding index on 'ReportCampaignSite', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignsite', ['data_cost_value'])

        # Adding index on 'ReportCampaignSite', fields ['bids_lost']
        db.create_index(u'report_reportcampaignsite', ['bids_lost'])

        # Adding index on 'ReportStrategyOs', fields ['net_earned']
        db.create_index(u'report_reportstrategyos', ['net_earned'])

        # Adding index on 'ReportStrategyOs', fields ['winbid_value']
        db.create_index(u'report_reportstrategyos', ['winbid_value'])

        # Adding index on 'ReportStrategyOs', fields ['winbid']
        db.create_index(u'report_reportstrategyos', ['winbid'])

        # Adding index on 'ReportStrategyOs', fields ['commission_value']
        db.create_index(u'report_reportstrategyos', ['commission_value'])

        # Adding index on 'ReportStrategyOs', fields ['imp']
        db.create_index(u'report_reportstrategyos', ['imp'])

        # Adding index on 'ReportStrategyOs', fields ['bid_value']
        db.create_index(u'report_reportstrategyos', ['bid_value'])

        # Adding index on 'ReportStrategyOs', fields ['conv_value']
        db.create_index(u'report_reportstrategyos', ['conv_value'])

        # Adding index on 'ReportStrategyOs', fields ['bid']
        db.create_index(u'report_reportstrategyos', ['bid'])

        # Adding index on 'ReportStrategyOs', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategyos', ['winbid_value_total'])

        # Adding index on 'ReportStrategyOs', fields ['clk']
        db.create_index(u'report_reportstrategyos', ['clk'])

        # Adding index on 'ReportStrategyOs', fields ['conv']
        db.create_index(u'report_reportstrategyos', ['conv'])

        # Adding index on 'ReportStrategyOs', fields ['data_cost_value']
        db.create_index(u'report_reportstrategyos', ['data_cost_value'])

        # Adding index on 'ReportStrategyOs', fields ['bids_lost']
        db.create_index(u'report_reportstrategyos', ['bids_lost'])

        # Adding index on 'ReportCampaignGender', fields ['net_earned']
        db.create_index(u'report_reportcampaigngender', ['net_earned'])

        # Adding index on 'ReportCampaignGender', fields ['winbid_value']
        db.create_index(u'report_reportcampaigngender', ['winbid_value'])

        # Adding index on 'ReportCampaignGender', fields ['winbid']
        db.create_index(u'report_reportcampaigngender', ['winbid'])

        # Adding index on 'ReportCampaignGender', fields ['commission_value']
        db.create_index(u'report_reportcampaigngender', ['commission_value'])

        # Adding index on 'ReportCampaignGender', fields ['imp']
        db.create_index(u'report_reportcampaigngender', ['imp'])

        # Adding index on 'ReportCampaignGender', fields ['bid_value']
        db.create_index(u'report_reportcampaigngender', ['bid_value'])

        # Adding index on 'ReportCampaignGender', fields ['conv_value']
        db.create_index(u'report_reportcampaigngender', ['conv_value'])

        # Adding index on 'ReportCampaignGender', fields ['bid']
        db.create_index(u'report_reportcampaigngender', ['bid'])

        # Adding index on 'ReportCampaignGender', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaigngender', ['winbid_value_total'])

        # Adding index on 'ReportCampaignGender', fields ['clk']
        db.create_index(u'report_reportcampaigngender', ['clk'])

        # Adding index on 'ReportCampaignGender', fields ['conv']
        db.create_index(u'report_reportcampaigngender', ['conv'])

        # Adding index on 'ReportCampaignGender', fields ['data_cost_value']
        db.create_index(u'report_reportcampaigngender', ['data_cost_value'])

        # Adding index on 'ReportCampaignGender', fields ['bids_lost']
        db.create_index(u'report_reportcampaigngender', ['bids_lost'])

        # Adding index on 'ReportStrategyCountry', fields ['net_earned']
        db.create_index(u'report_reportstrategycountry', ['net_earned'])

        # Adding index on 'ReportStrategyCountry', fields ['winbid_value']
        db.create_index(u'report_reportstrategycountry', ['winbid_value'])

        # Adding index on 'ReportStrategyCountry', fields ['winbid']
        db.create_index(u'report_reportstrategycountry', ['winbid'])

        # Adding index on 'ReportStrategyCountry', fields ['commission_value']
        db.create_index(u'report_reportstrategycountry', ['commission_value'])

        # Adding index on 'ReportStrategyCountry', fields ['imp']
        db.create_index(u'report_reportstrategycountry', ['imp'])

        # Adding index on 'ReportStrategyCountry', fields ['bid_value']
        db.create_index(u'report_reportstrategycountry', ['bid_value'])

        # Adding index on 'ReportStrategyCountry', fields ['conv_value']
        db.create_index(u'report_reportstrategycountry', ['conv_value'])

        # Adding index on 'ReportStrategyCountry', fields ['bid']
        db.create_index(u'report_reportstrategycountry', ['bid'])

        # Adding index on 'ReportStrategyCountry', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategycountry', ['winbid_value_total'])

        # Adding index on 'ReportStrategyCountry', fields ['clk']
        db.create_index(u'report_reportstrategycountry', ['clk'])

        # Adding index on 'ReportStrategyCountry', fields ['conv']
        db.create_index(u'report_reportstrategycountry', ['conv'])

        # Adding index on 'ReportStrategyCountry', fields ['data_cost_value']
        db.create_index(u'report_reportstrategycountry', ['data_cost_value'])

        # Adding index on 'ReportStrategyCountry', fields ['bids_lost']
        db.create_index(u'report_reportstrategycountry', ['bids_lost'])

        # Adding index on 'ReportCampaignMake', fields ['net_earned']
        db.create_index(u'report_reportcampaignmake', ['net_earned'])

        # Adding index on 'ReportCampaignMake', fields ['winbid_value']
        db.create_index(u'report_reportcampaignmake', ['winbid_value'])

        # Adding index on 'ReportCampaignMake', fields ['winbid']
        db.create_index(u'report_reportcampaignmake', ['winbid'])

        # Adding index on 'ReportCampaignMake', fields ['commission_value']
        db.create_index(u'report_reportcampaignmake', ['commission_value'])

        # Adding index on 'ReportCampaignMake', fields ['imp']
        db.create_index(u'report_reportcampaignmake', ['imp'])

        # Adding index on 'ReportCampaignMake', fields ['bid_value']
        db.create_index(u'report_reportcampaignmake', ['bid_value'])

        # Adding index on 'ReportCampaignMake', fields ['conv_value']
        db.create_index(u'report_reportcampaignmake', ['conv_value'])

        # Adding index on 'ReportCampaignMake', fields ['bid']
        db.create_index(u'report_reportcampaignmake', ['bid'])

        # Adding index on 'ReportCampaignMake', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignmake', ['winbid_value_total'])

        # Adding index on 'ReportCampaignMake', fields ['clk']
        db.create_index(u'report_reportcampaignmake', ['clk'])

        # Adding index on 'ReportCampaignMake', fields ['conv']
        db.create_index(u'report_reportcampaignmake', ['conv'])

        # Adding index on 'ReportCampaignMake', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignmake', ['data_cost_value'])

        # Adding index on 'ReportCampaignMake', fields ['bids_lost']
        db.create_index(u'report_reportcampaignmake', ['bids_lost'])

        # Adding index on 'ReportCampaignAge', fields ['net_earned']
        db.create_index(u'report_reportcampaignage', ['net_earned'])

        # Adding index on 'ReportCampaignAge', fields ['winbid_value']
        db.create_index(u'report_reportcampaignage', ['winbid_value'])

        # Adding index on 'ReportCampaignAge', fields ['winbid']
        db.create_index(u'report_reportcampaignage', ['winbid'])

        # Adding index on 'ReportCampaignAge', fields ['commission_value']
        db.create_index(u'report_reportcampaignage', ['commission_value'])

        # Adding index on 'ReportCampaignAge', fields ['imp']
        db.create_index(u'report_reportcampaignage', ['imp'])

        # Adding index on 'ReportCampaignAge', fields ['bid_value']
        db.create_index(u'report_reportcampaignage', ['bid_value'])

        # Adding index on 'ReportCampaignAge', fields ['conv_value']
        db.create_index(u'report_reportcampaignage', ['conv_value'])

        # Adding index on 'ReportCampaignAge', fields ['bid']
        db.create_index(u'report_reportcampaignage', ['bid'])

        # Adding index on 'ReportCampaignAge', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignage', ['winbid_value_total'])

        # Adding index on 'ReportCampaignAge', fields ['clk']
        db.create_index(u'report_reportcampaignage', ['clk'])

        # Adding index on 'ReportCampaignAge', fields ['conv']
        db.create_index(u'report_reportcampaignage', ['conv'])

        # Adding index on 'ReportCampaignAge', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignage', ['data_cost_value'])

        # Adding index on 'ReportCampaignAge', fields ['bids_lost']
        db.create_index(u'report_reportcampaignage', ['bids_lost'])

        # Adding index on 'ReportStrategyRegion', fields ['net_earned']
        db.create_index(u'report_reportstrategyregion', ['net_earned'])

        # Adding index on 'ReportStrategyRegion', fields ['winbid_value']
        db.create_index(u'report_reportstrategyregion', ['winbid_value'])

        # Adding index on 'ReportStrategyRegion', fields ['winbid']
        db.create_index(u'report_reportstrategyregion', ['winbid'])

        # Adding index on 'ReportStrategyRegion', fields ['commission_value']
        db.create_index(u'report_reportstrategyregion', ['commission_value'])

        # Adding index on 'ReportStrategyRegion', fields ['imp']
        db.create_index(u'report_reportstrategyregion', ['imp'])

        # Adding index on 'ReportStrategyRegion', fields ['bid_value']
        db.create_index(u'report_reportstrategyregion', ['bid_value'])

        # Adding index on 'ReportStrategyRegion', fields ['conv_value']
        db.create_index(u'report_reportstrategyregion', ['conv_value'])

        # Adding index on 'ReportStrategyRegion', fields ['bid']
        db.create_index(u'report_reportstrategyregion', ['bid'])

        # Adding index on 'ReportStrategyRegion', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategyregion', ['winbid_value_total'])

        # Adding index on 'ReportStrategyRegion', fields ['clk']
        db.create_index(u'report_reportstrategyregion', ['clk'])

        # Adding index on 'ReportStrategyRegion', fields ['conv']
        db.create_index(u'report_reportstrategyregion', ['conv'])

        # Adding index on 'ReportStrategyRegion', fields ['data_cost_value']
        db.create_index(u'report_reportstrategyregion', ['data_cost_value'])

        # Adding index on 'ReportStrategyRegion', fields ['bids_lost']
        db.create_index(u'report_reportstrategyregion', ['bids_lost'])

        # Adding index on 'ReportCampaignCarrier', fields ['net_earned']
        db.create_index(u'report_reportcampaigncarrier', ['net_earned'])

        # Adding index on 'ReportCampaignCarrier', fields ['winbid_value']
        db.create_index(u'report_reportcampaigncarrier', ['winbid_value'])

        # Adding index on 'ReportCampaignCarrier', fields ['winbid']
        db.create_index(u'report_reportcampaigncarrier', ['winbid'])

        # Adding index on 'ReportCampaignCarrier', fields ['commission_value']
        db.create_index(u'report_reportcampaigncarrier', ['commission_value'])

        # Adding index on 'ReportCampaignCarrier', fields ['imp']
        db.create_index(u'report_reportcampaigncarrier', ['imp'])

        # Adding index on 'ReportCampaignCarrier', fields ['bid_value']
        db.create_index(u'report_reportcampaigncarrier', ['bid_value'])

        # Adding index on 'ReportCampaignCarrier', fields ['conv_value']
        db.create_index(u'report_reportcampaigncarrier', ['conv_value'])

        # Adding index on 'ReportCampaignCarrier', fields ['bid']
        db.create_index(u'report_reportcampaigncarrier', ['bid'])

        # Adding index on 'ReportCampaignCarrier', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaigncarrier', ['winbid_value_total'])

        # Adding index on 'ReportCampaignCarrier', fields ['clk']
        db.create_index(u'report_reportcampaigncarrier', ['clk'])

        # Adding index on 'ReportCampaignCarrier', fields ['conv']
        db.create_index(u'report_reportcampaigncarrier', ['conv'])

        # Adding index on 'ReportCampaignCarrier', fields ['data_cost_value']
        db.create_index(u'report_reportcampaigncarrier', ['data_cost_value'])

        # Adding index on 'ReportCampaignCarrier', fields ['bids_lost']
        db.create_index(u'report_reportcampaigncarrier', ['bids_lost'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['net_earned']
        db.create_index(u'report_reportstrategyproximicquality', ['net_earned'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['winbid_value']
        db.create_index(u'report_reportstrategyproximicquality', ['winbid_value'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['winbid']
        db.create_index(u'report_reportstrategyproximicquality', ['winbid'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['commission_value']
        db.create_index(u'report_reportstrategyproximicquality', ['commission_value'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['imp']
        db.create_index(u'report_reportstrategyproximicquality', ['imp'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['bid_value']
        db.create_index(u'report_reportstrategyproximicquality', ['bid_value'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['conv_value']
        db.create_index(u'report_reportstrategyproximicquality', ['conv_value'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['bid']
        db.create_index(u'report_reportstrategyproximicquality', ['bid'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategyproximicquality', ['winbid_value_total'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['clk']
        db.create_index(u'report_reportstrategyproximicquality', ['clk'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['conv']
        db.create_index(u'report_reportstrategyproximicquality', ['conv'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['data_cost_value']
        db.create_index(u'report_reportstrategyproximicquality', ['data_cost_value'])

        # Adding index on 'ReportStrategyProximicQuality', fields ['bids_lost']
        db.create_index(u'report_reportstrategyproximicquality', ['bids_lost'])

        # Adding index on 'ReportCampaignPublisher', fields ['net_earned']
        db.create_index(u'report_reportcampaignpublisher', ['net_earned'])

        # Adding index on 'ReportCampaignPublisher', fields ['winbid_value']
        db.create_index(u'report_reportcampaignpublisher', ['winbid_value'])

        # Adding index on 'ReportCampaignPublisher', fields ['winbid']
        db.create_index(u'report_reportcampaignpublisher', ['winbid'])

        # Adding index on 'ReportCampaignPublisher', fields ['commission_value']
        db.create_index(u'report_reportcampaignpublisher', ['commission_value'])

        # Adding index on 'ReportCampaignPublisher', fields ['imp']
        db.create_index(u'report_reportcampaignpublisher', ['imp'])

        # Adding index on 'ReportCampaignPublisher', fields ['bid_value']
        db.create_index(u'report_reportcampaignpublisher', ['bid_value'])

        # Adding index on 'ReportCampaignPublisher', fields ['conv_value']
        db.create_index(u'report_reportcampaignpublisher', ['conv_value'])

        # Adding index on 'ReportCampaignPublisher', fields ['bid']
        db.create_index(u'report_reportcampaignpublisher', ['bid'])

        # Adding index on 'ReportCampaignPublisher', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignpublisher', ['winbid_value_total'])

        # Adding index on 'ReportCampaignPublisher', fields ['clk']
        db.create_index(u'report_reportcampaignpublisher', ['clk'])

        # Adding index on 'ReportCampaignPublisher', fields ['conv']
        db.create_index(u'report_reportcampaignpublisher', ['conv'])

        # Adding index on 'ReportCampaignPublisher', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignpublisher', ['data_cost_value'])

        # Adding index on 'ReportCampaignPublisher', fields ['bids_lost']
        db.create_index(u'report_reportcampaignpublisher', ['bids_lost'])

        # Adding index on 'ReportCampaign', fields ['net_earned']
        db.create_index(u'report_reportcampaign', ['net_earned'])

        # Adding index on 'ReportCampaign', fields ['winbid_value']
        db.create_index(u'report_reportcampaign', ['winbid_value'])

        # Adding index on 'ReportCampaign', fields ['winbid']
        db.create_index(u'report_reportcampaign', ['winbid'])

        # Adding index on 'ReportCampaign', fields ['commission_value']
        db.create_index(u'report_reportcampaign', ['commission_value'])

        # Adding index on 'ReportCampaign', fields ['imp']
        db.create_index(u'report_reportcampaign', ['imp'])

        # Adding index on 'ReportCampaign', fields ['bid_value']
        db.create_index(u'report_reportcampaign', ['bid_value'])

        # Adding index on 'ReportCampaign', fields ['conv_value']
        db.create_index(u'report_reportcampaign', ['conv_value'])

        # Adding index on 'ReportCampaign', fields ['bid']
        db.create_index(u'report_reportcampaign', ['bid'])

        # Adding index on 'ReportCampaign', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaign', ['winbid_value_total'])

        # Adding index on 'ReportCampaign', fields ['clk']
        db.create_index(u'report_reportcampaign', ['clk'])

        # Adding index on 'ReportCampaign', fields ['conv']
        db.create_index(u'report_reportcampaign', ['conv'])

        # Adding index on 'ReportCampaign', fields ['data_cost_value']
        db.create_index(u'report_reportcampaign', ['data_cost_value'])

        # Adding index on 'ReportCampaign', fields ['bids_lost']
        db.create_index(u'report_reportcampaign', ['bids_lost'])

        # Adding index on 'ReportStrategyCategory', fields ['net_earned']
        db.create_index(u'report_reportstrategycategory', ['net_earned'])

        # Adding index on 'ReportStrategyCategory', fields ['winbid_value']
        db.create_index(u'report_reportstrategycategory', ['winbid_value'])

        # Adding index on 'ReportStrategyCategory', fields ['winbid']
        db.create_index(u'report_reportstrategycategory', ['winbid'])

        # Adding index on 'ReportStrategyCategory', fields ['commission_value']
        db.create_index(u'report_reportstrategycategory', ['commission_value'])

        # Adding index on 'ReportStrategyCategory', fields ['imp']
        db.create_index(u'report_reportstrategycategory', ['imp'])

        # Adding index on 'ReportStrategyCategory', fields ['bid_value']
        db.create_index(u'report_reportstrategycategory', ['bid_value'])

        # Adding index on 'ReportStrategyCategory', fields ['conv_value']
        db.create_index(u'report_reportstrategycategory', ['conv_value'])

        # Adding index on 'ReportStrategyCategory', fields ['bid']
        db.create_index(u'report_reportstrategycategory', ['bid'])

        # Adding index on 'ReportStrategyCategory', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategycategory', ['winbid_value_total'])

        # Adding index on 'ReportStrategyCategory', fields ['clk']
        db.create_index(u'report_reportstrategycategory', ['clk'])

        # Adding index on 'ReportStrategyCategory', fields ['conv']
        db.create_index(u'report_reportstrategycategory', ['conv'])

        # Adding index on 'ReportStrategyCategory', fields ['data_cost_value']
        db.create_index(u'report_reportstrategycategory', ['data_cost_value'])

        # Adding index on 'ReportStrategyCategory', fields ['bids_lost']
        db.create_index(u'report_reportstrategycategory', ['bids_lost'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['net_earned']
        db.create_index(u'report_reportcampaignproximiccontextual', ['net_earned'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['winbid_value']
        db.create_index(u'report_reportcampaignproximiccontextual', ['winbid_value'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['winbid']
        db.create_index(u'report_reportcampaignproximiccontextual', ['winbid'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['commission_value']
        db.create_index(u'report_reportcampaignproximiccontextual', ['commission_value'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['imp']
        db.create_index(u'report_reportcampaignproximiccontextual', ['imp'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['bid_value']
        db.create_index(u'report_reportcampaignproximiccontextual', ['bid_value'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['conv_value']
        db.create_index(u'report_reportcampaignproximiccontextual', ['conv_value'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['bid']
        db.create_index(u'report_reportcampaignproximiccontextual', ['bid'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignproximiccontextual', ['winbid_value_total'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['clk']
        db.create_index(u'report_reportcampaignproximiccontextual', ['clk'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['conv']
        db.create_index(u'report_reportcampaignproximiccontextual', ['conv'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignproximiccontextual', ['data_cost_value'])

        # Adding index on 'ReportCampaignProximicContextual', fields ['bids_lost']
        db.create_index(u'report_reportcampaignproximiccontextual', ['bids_lost'])

        # Adding index on 'ReportStrategyProximicContext', fields ['net_earned']
        db.create_index(u'report_reportstrategyproximiccontext', ['net_earned'])

        # Adding index on 'ReportStrategyProximicContext', fields ['winbid_value']
        db.create_index(u'report_reportstrategyproximiccontext', ['winbid_value'])

        # Adding index on 'ReportStrategyProximicContext', fields ['winbid']
        db.create_index(u'report_reportstrategyproximiccontext', ['winbid'])

        # Adding index on 'ReportStrategyProximicContext', fields ['commission_value']
        db.create_index(u'report_reportstrategyproximiccontext', ['commission_value'])

        # Adding index on 'ReportStrategyProximicContext', fields ['imp']
        db.create_index(u'report_reportstrategyproximiccontext', ['imp'])

        # Adding index on 'ReportStrategyProximicContext', fields ['bid_value']
        db.create_index(u'report_reportstrategyproximiccontext', ['bid_value'])

        # Adding index on 'ReportStrategyProximicContext', fields ['conv_value']
        db.create_index(u'report_reportstrategyproximiccontext', ['conv_value'])

        # Adding index on 'ReportStrategyProximicContext', fields ['bid']
        db.create_index(u'report_reportstrategyproximiccontext', ['bid'])

        # Adding index on 'ReportStrategyProximicContext', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategyproximiccontext', ['winbid_value_total'])

        # Adding index on 'ReportStrategyProximicContext', fields ['clk']
        db.create_index(u'report_reportstrategyproximiccontext', ['clk'])

        # Adding index on 'ReportStrategyProximicContext', fields ['conv']
        db.create_index(u'report_reportstrategyproximiccontext', ['conv'])

        # Adding index on 'ReportStrategyProximicContext', fields ['data_cost_value']
        db.create_index(u'report_reportstrategyproximiccontext', ['data_cost_value'])

        # Adding index on 'ReportStrategyProximicContext', fields ['bids_lost']
        db.create_index(u'report_reportstrategyproximiccontext', ['bids_lost'])

        # Adding index on 'ReportCampaignPosition', fields ['net_earned']
        db.create_index(u'report_reportcampaignposition', ['net_earned'])

        # Adding index on 'ReportCampaignPosition', fields ['winbid_value']
        db.create_index(u'report_reportcampaignposition', ['winbid_value'])

        # Adding index on 'ReportCampaignPosition', fields ['winbid']
        db.create_index(u'report_reportcampaignposition', ['winbid'])

        # Adding index on 'ReportCampaignPosition', fields ['commission_value']
        db.create_index(u'report_reportcampaignposition', ['commission_value'])

        # Adding index on 'ReportCampaignPosition', fields ['imp']
        db.create_index(u'report_reportcampaignposition', ['imp'])

        # Adding index on 'ReportCampaignPosition', fields ['bid_value']
        db.create_index(u'report_reportcampaignposition', ['bid_value'])

        # Adding index on 'ReportCampaignPosition', fields ['conv_value']
        db.create_index(u'report_reportcampaignposition', ['conv_value'])

        # Adding index on 'ReportCampaignPosition', fields ['bid']
        db.create_index(u'report_reportcampaignposition', ['bid'])

        # Adding index on 'ReportCampaignPosition', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignposition', ['winbid_value_total'])

        # Adding index on 'ReportCampaignPosition', fields ['clk']
        db.create_index(u'report_reportcampaignposition', ['clk'])

        # Adding index on 'ReportCampaignPosition', fields ['conv']
        db.create_index(u'report_reportcampaignposition', ['conv'])

        # Adding index on 'ReportCampaignPosition', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignposition', ['data_cost_value'])

        # Adding index on 'ReportCampaignPosition', fields ['bids_lost']
        db.create_index(u'report_reportcampaignposition', ['bids_lost'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['net_earned']
        db.create_index(u'report_reportcampaignproximicnotice', ['net_earned'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['winbid_value']
        db.create_index(u'report_reportcampaignproximicnotice', ['winbid_value'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['winbid']
        db.create_index(u'report_reportcampaignproximicnotice', ['winbid'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['commission_value']
        db.create_index(u'report_reportcampaignproximicnotice', ['commission_value'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['imp']
        db.create_index(u'report_reportcampaignproximicnotice', ['imp'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['bid_value']
        db.create_index(u'report_reportcampaignproximicnotice', ['bid_value'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['conv_value']
        db.create_index(u'report_reportcampaignproximicnotice', ['conv_value'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['bid']
        db.create_index(u'report_reportcampaignproximicnotice', ['bid'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaignproximicnotice', ['winbid_value_total'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['clk']
        db.create_index(u'report_reportcampaignproximicnotice', ['clk'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['conv']
        db.create_index(u'report_reportcampaignproximicnotice', ['conv'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['data_cost_value']
        db.create_index(u'report_reportcampaignproximicnotice', ['data_cost_value'])

        # Adding index on 'ReportCampaignProximicNotice', fields ['bids_lost']
        db.create_index(u'report_reportcampaignproximicnotice', ['bids_lost'])

        # Adding index on 'ReportStrategyDomain', fields ['net_earned']
        db.create_index(u'report_reportstrategydomain', ['net_earned'])

        # Adding index on 'ReportStrategyDomain', fields ['winbid_value']
        db.create_index(u'report_reportstrategydomain', ['winbid_value'])

        # Adding index on 'ReportStrategyDomain', fields ['winbid']
        db.create_index(u'report_reportstrategydomain', ['winbid'])

        # Adding index on 'ReportStrategyDomain', fields ['commission_value']
        db.create_index(u'report_reportstrategydomain', ['commission_value'])

        # Adding index on 'ReportStrategyDomain', fields ['imp']
        db.create_index(u'report_reportstrategydomain', ['imp'])

        # Adding index on 'ReportStrategyDomain', fields ['bid_value']
        db.create_index(u'report_reportstrategydomain', ['bid_value'])

        # Adding index on 'ReportStrategyDomain', fields ['conv_value']
        db.create_index(u'report_reportstrategydomain', ['conv_value'])

        # Adding index on 'ReportStrategyDomain', fields ['bid']
        db.create_index(u'report_reportstrategydomain', ['bid'])

        # Adding index on 'ReportStrategyDomain', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategydomain', ['winbid_value_total'])

        # Adding index on 'ReportStrategyDomain', fields ['clk']
        db.create_index(u'report_reportstrategydomain', ['clk'])

        # Adding index on 'ReportStrategyDomain', fields ['conv']
        db.create_index(u'report_reportstrategydomain', ['conv'])

        # Adding index on 'ReportStrategyDomain', fields ['data_cost_value']
        db.create_index(u'report_reportstrategydomain', ['data_cost_value'])

        # Adding index on 'ReportStrategyDomain', fields ['bids_lost']
        db.create_index(u'report_reportstrategydomain', ['bids_lost'])

        # Adding index on 'ReportCampaignDomain', fields ['net_earned']
        db.create_index(u'report_reportcampaigndomain', ['net_earned'])

        # Adding index on 'ReportCampaignDomain', fields ['winbid_value']
        db.create_index(u'report_reportcampaigndomain', ['winbid_value'])

        # Adding index on 'ReportCampaignDomain', fields ['winbid']
        db.create_index(u'report_reportcampaigndomain', ['winbid'])

        # Adding index on 'ReportCampaignDomain', fields ['commission_value']
        db.create_index(u'report_reportcampaigndomain', ['commission_value'])

        # Adding index on 'ReportCampaignDomain', fields ['imp']
        db.create_index(u'report_reportcampaigndomain', ['imp'])

        # Adding index on 'ReportCampaignDomain', fields ['bid_value']
        db.create_index(u'report_reportcampaigndomain', ['bid_value'])

        # Adding index on 'ReportCampaignDomain', fields ['conv_value']
        db.create_index(u'report_reportcampaigndomain', ['conv_value'])

        # Adding index on 'ReportCampaignDomain', fields ['bid']
        db.create_index(u'report_reportcampaigndomain', ['bid'])

        # Adding index on 'ReportCampaignDomain', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaigndomain', ['winbid_value_total'])

        # Adding index on 'ReportCampaignDomain', fields ['clk']
        db.create_index(u'report_reportcampaigndomain', ['clk'])

        # Adding index on 'ReportCampaignDomain', fields ['conv']
        db.create_index(u'report_reportcampaigndomain', ['conv'])

        # Adding index on 'ReportCampaignDomain', fields ['data_cost_value']
        db.create_index(u'report_reportcampaigndomain', ['data_cost_value'])

        # Adding index on 'ReportCampaignDomain', fields ['bids_lost']
        db.create_index(u'report_reportcampaigndomain', ['bids_lost'])

        # Adding index on 'ReportCampaignCategory', fields ['net_earned']
        db.create_index(u'report_reportcampaigncategory', ['net_earned'])

        # Adding index on 'ReportCampaignCategory', fields ['winbid_value']
        db.create_index(u'report_reportcampaigncategory', ['winbid_value'])

        # Adding index on 'ReportCampaignCategory', fields ['winbid']
        db.create_index(u'report_reportcampaigncategory', ['winbid'])

        # Adding index on 'ReportCampaignCategory', fields ['commission_value']
        db.create_index(u'report_reportcampaigncategory', ['commission_value'])

        # Adding index on 'ReportCampaignCategory', fields ['imp']
        db.create_index(u'report_reportcampaigncategory', ['imp'])

        # Adding index on 'ReportCampaignCategory', fields ['bid_value']
        db.create_index(u'report_reportcampaigncategory', ['bid_value'])

        # Adding index on 'ReportCampaignCategory', fields ['conv_value']
        db.create_index(u'report_reportcampaigncategory', ['conv_value'])

        # Adding index on 'ReportCampaignCategory', fields ['bid']
        db.create_index(u'report_reportcampaigncategory', ['bid'])

        # Adding index on 'ReportCampaignCategory', fields ['winbid_value_total']
        db.create_index(u'report_reportcampaigncategory', ['winbid_value_total'])

        # Adding index on 'ReportCampaignCategory', fields ['clk']
        db.create_index(u'report_reportcampaigncategory', ['clk'])

        # Adding index on 'ReportCampaignCategory', fields ['conv']
        db.create_index(u'report_reportcampaigncategory', ['conv'])

        # Adding index on 'ReportCampaignCategory', fields ['data_cost_value']
        db.create_index(u'report_reportcampaigncategory', ['data_cost_value'])

        # Adding index on 'ReportCampaignCategory', fields ['bids_lost']
        db.create_index(u'report_reportcampaigncategory', ['bids_lost'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['net_earned']
        db.create_index(u'report_reportstrategypeer39language', ['net_earned'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['winbid_value']
        db.create_index(u'report_reportstrategypeer39language', ['winbid_value'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['winbid']
        db.create_index(u'report_reportstrategypeer39language', ['winbid'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['commission_value']
        db.create_index(u'report_reportstrategypeer39language', ['commission_value'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['imp']
        db.create_index(u'report_reportstrategypeer39language', ['imp'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['bid_value']
        db.create_index(u'report_reportstrategypeer39language', ['bid_value'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['conv_value']
        db.create_index(u'report_reportstrategypeer39language', ['conv_value'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['bid']
        db.create_index(u'report_reportstrategypeer39language', ['bid'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategypeer39language', ['winbid_value_total'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['clk']
        db.create_index(u'report_reportstrategypeer39language', ['clk'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['conv']
        db.create_index(u'report_reportstrategypeer39language', ['conv'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['data_cost_value']
        db.create_index(u'report_reportstrategypeer39language', ['data_cost_value'])

        # Adding index on 'ReportStrategyPeer39Language', fields ['bids_lost']
        db.create_index(u'report_reportstrategypeer39language', ['bids_lost'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['net_earned']
        db.create_index(u'report_reportstrategypublishernetwork', ['net_earned'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['winbid_value']
        db.create_index(u'report_reportstrategypublishernetwork', ['winbid_value'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['winbid']
        db.create_index(u'report_reportstrategypublishernetwork', ['winbid'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['commission_value']
        db.create_index(u'report_reportstrategypublishernetwork', ['commission_value'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['imp']
        db.create_index(u'report_reportstrategypublishernetwork', ['imp'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['bid_value']
        db.create_index(u'report_reportstrategypublishernetwork', ['bid_value'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['conv_value']
        db.create_index(u'report_reportstrategypublishernetwork', ['conv_value'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['bid']
        db.create_index(u'report_reportstrategypublishernetwork', ['bid'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategypublishernetwork', ['winbid_value_total'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['clk']
        db.create_index(u'report_reportstrategypublishernetwork', ['clk'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['conv']
        db.create_index(u'report_reportstrategypublishernetwork', ['conv'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['data_cost_value']
        db.create_index(u'report_reportstrategypublishernetwork', ['data_cost_value'])

        # Adding index on 'ReportStrategyPublisherNetwork', fields ['bids_lost']
        db.create_index(u'report_reportstrategypublishernetwork', ['bids_lost'])

        # Adding index on 'ReportStrategyAge', fields ['net_earned']
        db.create_index(u'report_reportstrategyage', ['net_earned'])

        # Adding index on 'ReportStrategyAge', fields ['winbid_value']
        db.create_index(u'report_reportstrategyage', ['winbid_value'])

        # Adding index on 'ReportStrategyAge', fields ['winbid']
        db.create_index(u'report_reportstrategyage', ['winbid'])

        # Adding index on 'ReportStrategyAge', fields ['commission_value']
        db.create_index(u'report_reportstrategyage', ['commission_value'])

        # Adding index on 'ReportStrategyAge', fields ['imp']
        db.create_index(u'report_reportstrategyage', ['imp'])

        # Adding index on 'ReportStrategyAge', fields ['bid_value']
        db.create_index(u'report_reportstrategyage', ['bid_value'])

        # Adding index on 'ReportStrategyAge', fields ['conv_value']
        db.create_index(u'report_reportstrategyage', ['conv_value'])

        # Adding index on 'ReportStrategyAge', fields ['bid']
        db.create_index(u'report_reportstrategyage', ['bid'])

        # Adding index on 'ReportStrategyAge', fields ['winbid_value_total']
        db.create_index(u'report_reportstrategyage', ['winbid_value_total'])

        # Adding index on 'ReportStrategyAge', fields ['clk']
        db.create_index(u'report_reportstrategyage', ['clk'])

        # Adding index on 'ReportStrategyAge', fields ['conv']
        db.create_index(u'report_reportstrategyage', ['conv'])

        # Adding index on 'ReportStrategyAge', fields ['data_cost_value']
        db.create_index(u'report_reportstrategyage', ['data_cost_value'])

        # Adding index on 'ReportStrategyAge', fields ['bids_lost']
        db.create_index(u'report_reportstrategyage', ['bids_lost'])


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
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaign': {
            'Meta': {'unique_together': "(('related', 'time'),)", 'object_name': 'ReportCampaign'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignAge'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_age'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaigncarrier': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCarrier'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_carrier'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaigncategory': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCategory'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_category'", 'null': 'True', 'to': u"orm['targeting.ContentCategoryValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaigncity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_city'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaigncountry': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCountry'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_country'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaigndomain': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignDomain'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_domain'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaigngender': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignGender'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_gender'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignmake': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignMake'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_make'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignmodel': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignModel'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_model'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignos': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignOs'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_os'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignpeer39brand': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Brand'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_brandprotection'", 'null': 'True', 'to': u"orm['targeting.Peer39BrandProtection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignpeer39contextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Contextual'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_contextual'", 'null': 'True', 'to': u"orm['targeting.Peer39ContextualSegment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignpeer39language': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Language'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.Peer39PageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignpeer39quality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Quality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagequality'", 'null': 'True', 'to': u"orm['targeting.Peer39PageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignposition': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPosition'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_position'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximiccontextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicContextual'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_contextual'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximiclanguage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicLanguage'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximicmaturity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicMaturity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_maturity'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicMaturityRating']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximicnotice': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicNotice'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagenoticeability'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximicplace': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicPlace'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pageplacement'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximicquality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicQuality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagequality'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignproximicsafety': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicSafety'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_safety'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicSafetyLevel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignpublisher': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPublisher'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_publisher'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignpublishernetwork': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPublisherNetwork'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_network'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignregion': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignRegion'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_region'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportcampaignsite': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignSite'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategy': {
            'Meta': {'unique_together': "(('related', 'time'),)", 'object_name': 'ReportStrategy'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyAge'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_age'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategycarrier': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCarrier'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_carrier'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategycategory': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCategory'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_category'", 'null': 'True', 'to': u"orm['targeting.ContentCategoryValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategycity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_city'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategycountry': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyCountry'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_country'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategydomain': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyDomain'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_domain'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategygender': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyGender'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_gender'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategymake': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyMake'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_make'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategymodel': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyModel'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_model'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyos': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyOs'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_os'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategypeer39brand': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Brand'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_brandprotection'", 'null': 'True', 'to': u"orm['targeting.Peer39BrandProtection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategypeer39contextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Contextual'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_contextual'", 'null': 'True', 'to': u"orm['targeting.Peer39ContextualSegment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategypeer39language': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Language'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.Peer39PageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategypeer39quality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPeer39Quality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagequality'", 'null': 'True', 'to': u"orm['targeting.Peer39PageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyposition': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPosition'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_position'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximiccontext': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicContext'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_contextual'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximiclanguage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicLanguage'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximicmaturity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicMaturity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_maturity'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicMaturityRating']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximicnotice': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicNotice'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagenoticeability'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximicplace': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicPlace'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pageplacement'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximicquality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicQuality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_pagequality'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyproximicsafety': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyProximicSafety'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_safety'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicSafetyLevel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategypublisher': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPublisher'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_publisher'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategypublishernetwork': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyPublisherNetwork'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_network'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategyregion': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategyRegion'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_strategy_region'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
        },
        u'report.reportstrategysite': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportStrategySite'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'dimension': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'})
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