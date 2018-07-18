# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'ReportAdvertModel', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertmodel', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertOs', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertos', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertPublisherNetwork', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertpublishernetwork', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertCarrier', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertcarrier', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertProximicMaturity', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertproximicmaturity', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertProximicQuality', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertproximicquality', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertProximicContextual', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertproximiccontextual', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertDomain', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertdomain', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertProximicPlace', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertproximicplace', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertCategory', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertcategory', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertProximicNotice', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertproximicnotice', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertPeer39Contextual', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertpeer39contextual', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertGender', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertgender', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertRegion', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertregion', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertCity', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertcity', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertAge', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertage', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertSite', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertsite', ['dimension', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertPeer39Quality', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertpeer39quality', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertPublisher', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertpublisher', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertPeer39Language', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertpeer39language', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertCountry', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertcountry', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertPeer39Brand', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertpeer39brand', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertProximicLanguage', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertproximiclanguage', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertMake', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertmake', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertOsVersion', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertosversion', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertPosition', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertposition', ['dimension_id', 'related_id', 'time'])

        # Removing unique constraint on 'ReportAdvertProximicSafety', fields ['dimension', 'related', 'time']
        db.delete_unique(u'report_reportadvertproximicsafety', ['dimension_id', 'related_id', 'time'])

        # Deleting model 'ReportAdvertProximicSafety'
        db.delete_table(u'report_reportadvertproximicsafety')

        # Deleting model 'ReportAdvertPosition'
        db.delete_table(u'report_reportadvertposition')

        # Deleting model 'ReportAdvertOsVersion'
        db.delete_table(u'report_reportadvertosversion')

        # Deleting model 'ReportAdvertMake'
        db.delete_table(u'report_reportadvertmake')

        # Deleting model 'ReportAdvertProximicLanguage'
        db.delete_table(u'report_reportadvertproximiclanguage')

        # Deleting model 'ReportAdvertPeer39Brand'
        db.delete_table(u'report_reportadvertpeer39brand')

        # Deleting model 'ReportAdvertCountry'
        db.delete_table(u'report_reportadvertcountry')

        # Deleting model 'ReportAdvertPeer39Language'
        db.delete_table(u'report_reportadvertpeer39language')

        # Deleting model 'ReportAdvertPublisher'
        db.delete_table(u'report_reportadvertpublisher')

        # Deleting model 'ReportAdvertPeer39Quality'
        db.delete_table(u'report_reportadvertpeer39quality')

        # Deleting model 'ReportAdvertSite'
        db.delete_table(u'report_reportadvertsite')

        # Deleting model 'ReportAdvertAge'
        db.delete_table(u'report_reportadvertage')

        # Deleting model 'ReportAdvertCity'
        db.delete_table(u'report_reportadvertcity')

        # Deleting model 'ReportAdvertRegion'
        db.delete_table(u'report_reportadvertregion')

        # Deleting model 'ReportAdvertGender'
        db.delete_table(u'report_reportadvertgender')

        # Deleting model 'ReportAdvertPeer39Contextual'
        db.delete_table(u'report_reportadvertpeer39contextual')

        # Deleting model 'ReportAdvertProximicNotice'
        db.delete_table(u'report_reportadvertproximicnotice')

        # Deleting model 'ReportAdvertCategory'
        db.delete_table(u'report_reportadvertcategory')

        # Deleting model 'ReportAdvertProximicPlace'
        db.delete_table(u'report_reportadvertproximicplace')

        # Deleting model 'ReportAdvertDomain'
        db.delete_table(u'report_reportadvertdomain')

        # Deleting model 'ReportAdvertProximicContextual'
        db.delete_table(u'report_reportadvertproximiccontextual')

        # Deleting model 'ReportAdvertProximicQuality'
        db.delete_table(u'report_reportadvertproximicquality')

        # Deleting model 'ReportAdvertProximicMaturity'
        db.delete_table(u'report_reportadvertproximicmaturity')

        # Deleting model 'ReportAdvertCarrier'
        db.delete_table(u'report_reportadvertcarrier')

        # Deleting model 'ReportAdvertPublisherNetwork'
        db.delete_table(u'report_reportadvertpublishernetwork')

        # Deleting model 'ReportAdvertOs'
        db.delete_table(u'report_reportadvertos')

        # Deleting model 'ReportAdvertModel'
        db.delete_table(u'report_reportadvertmodel')


    def backwards(self, orm):
        # Adding model 'ReportAdvertProximicSafety'
        db.create_table(u'report_reportadvertproximicsafety', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_safety', null=True, to=orm['targeting.SegmentProximicSafetyLevel'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertProximicSafety'])

        # Adding unique constraint on 'ReportAdvertProximicSafety', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertproximicsafety', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertPosition'
        db.create_table(u'report_reportadvertposition', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_position', null=True, to=orm['targeting.TargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertPosition'])

        # Adding unique constraint on 'ReportAdvertPosition', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertposition', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertOsVersion'
        db.create_table(u'report_reportadvertosversion', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_os_version', null=True, to=orm['targeting.TargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertOsVersion'])

        # Adding unique constraint on 'ReportAdvertOsVersion', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertosversion', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertMake'
        db.create_table(u'report_reportadvertmake', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_make', null=True, to=orm['targeting.TargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertMake'])

        # Adding unique constraint on 'ReportAdvertMake', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertmake', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertProximicLanguage'
        db.create_table(u'report_reportadvertproximiclanguage', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_pagelanguage', null=True, to=orm['targeting.SegmentProximicPageLanguage'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertProximicLanguage'])

        # Adding unique constraint on 'ReportAdvertProximicLanguage', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertproximiclanguage', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertPeer39Brand'
        db.create_table(u'report_reportadvertpeer39brand', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_brandprotection', null=True, to=orm['targeting.Peer39BrandProtection'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertPeer39Brand'])

        # Adding unique constraint on 'ReportAdvertPeer39Brand', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertpeer39brand', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertCountry'
        db.create_table(u'report_reportadvertcountry', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_country', null=True, to=orm['targeting.TargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertCountry'])

        # Adding unique constraint on 'ReportAdvertCountry', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertcountry', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertPeer39Language'
        db.create_table(u'report_reportadvertpeer39language', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_pagelanguage', null=True, to=orm['targeting.Peer39PageLanguage'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertPeer39Language'])

        # Adding unique constraint on 'ReportAdvertPeer39Language', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertpeer39language', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertPublisher'
        db.create_table(u'report_reportadvertpublisher', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_publisher', null=True, to=orm['targeting.PublisherTargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertPublisher'])

        # Adding unique constraint on 'ReportAdvertPublisher', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertpublisher', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertPeer39Quality'
        db.create_table(u'report_reportadvertpeer39quality', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_pagequality', null=True, to=orm['targeting.Peer39PageQuality'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertPeer39Quality'])

        # Adding unique constraint on 'ReportAdvertPeer39Quality', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertpeer39quality', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertSite'
        db.create_table(u'report_reportadvertsite', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertSite'])

        # Adding unique constraint on 'ReportAdvertSite', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertsite', ['dimension', 'related_id', 'time'])

        # Adding model 'ReportAdvertAge'
        db.create_table(u'report_reportadvertage', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_age', null=True, to=orm['targeting.TargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertAge'])

        # Adding unique constraint on 'ReportAdvertAge', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertage', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertCity'
        db.create_table(u'report_reportadvertcity', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_city', null=True, to=orm['targeting.TargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertCity'])

        # Adding unique constraint on 'ReportAdvertCity', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertcity', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertRegion'
        db.create_table(u'report_reportadvertregion', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_region', null=True, to=orm['targeting.TargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertRegion'])

        # Adding unique constraint on 'ReportAdvertRegion', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertregion', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertGender'
        db.create_table(u'report_reportadvertgender', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_gender', null=True, to=orm['targeting.TargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertGender'])

        # Adding unique constraint on 'ReportAdvertGender', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertgender', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertPeer39Contextual'
        db.create_table(u'report_reportadvertpeer39contextual', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_contextual', null=True, to=orm['targeting.Peer39ContextualSegment'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertPeer39Contextual'])

        # Adding unique constraint on 'ReportAdvertPeer39Contextual', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertpeer39contextual', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertProximicNotice'
        db.create_table(u'report_reportadvertproximicnotice', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_pagenoticeability', null=True, to=orm['targeting.SegmentProximicPageNoticeability'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertProximicNotice'])

        # Adding unique constraint on 'ReportAdvertProximicNotice', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertproximicnotice', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertCategory'
        db.create_table(u'report_reportadvertcategory', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_category', null=True, to=orm['targeting.ContentCategoryValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertCategory'])

        # Adding unique constraint on 'ReportAdvertCategory', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertcategory', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertProximicPlace'
        db.create_table(u'report_reportadvertproximicplace', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_pageplacement', null=True, to=orm['targeting.SegmentProximicPagePlacement'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertProximicPlace'])

        # Adding unique constraint on 'ReportAdvertProximicPlace', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertproximicplace', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertDomain'
        db.create_table(u'report_reportadvertdomain', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_domain', null=True, to=orm['targeting.TargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertDomain'])

        # Adding unique constraint on 'ReportAdvertDomain', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertdomain', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertProximicContextual'
        db.create_table(u'report_reportadvertproximiccontextual', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_contextual', null=True, to=orm['targeting.SegmentProximicContextual'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertProximicContextual'])

        # Adding unique constraint on 'ReportAdvertProximicContextual', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertproximiccontextual', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertProximicQuality'
        db.create_table(u'report_reportadvertproximicquality', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_pagequality', null=True, to=orm['targeting.SegmentProximicPageQuality'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertProximicQuality'])

        # Adding unique constraint on 'ReportAdvertProximicQuality', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertproximicquality', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertProximicMaturity'
        db.create_table(u'report_reportadvertproximicmaturity', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_maturity', null=True, to=orm['targeting.SegmentProximicMaturityRating'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertProximicMaturity'])

        # Adding unique constraint on 'ReportAdvertProximicMaturity', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertproximicmaturity', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertCarrier'
        db.create_table(u'report_reportadvertcarrier', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_carrier', null=True, to=orm['targeting.TargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertCarrier'])

        # Adding unique constraint on 'ReportAdvertCarrier', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertcarrier', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertPublisherNetwork'
        db.create_table(u'report_reportadvertpublishernetwork', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_network', null=True, to=orm['targeting.PublisherTargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertPublisherNetwork'])

        # Adding unique constraint on 'ReportAdvertPublisherNetwork', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertpublishernetwork', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertOs'
        db.create_table(u'report_reportadvertos', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_os', null=True, to=orm['targeting.TargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertOs'])

        # Adding unique constraint on 'ReportAdvertOs', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertos', ['dimension_id', 'related_id', 'time'])

        # Adding model 'ReportAdvertModel'
        db.create_table(u'report_reportadvertmodel', (
            ('bids_lost', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('data_cost_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('clk', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value_total', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('bid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('bid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commission_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('conv_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('imp', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('winbid', self.gf('ui.fields.BigDecimalField')(default=0, db_index=True)),
            ('winbid_value', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
            ('dimension', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reports_advert_model', null=True, to=orm['targeting.TargetValue'])),
            ('related', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'], to_field='id_random')),
            ('net_earned', self.gf('ui.fields.BudgetSpentDecimalField')(default=0, db_index=True)),
        ))
        db.send_create_signal(u'report', ['ReportAdvertModel'])

        # Adding unique constraint on 'ReportAdvertModel', fields ['dimension', 'related', 'time']
        db.create_unique(u'report_reportadvertmodel', ['dimension_id', 'related_id', 'time'])


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
        u'report.reportcampaignage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignAge'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_age'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaigncarrier': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCarrier'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_carrier'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaigncategory': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCategory'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_category'", 'null': 'True', 'to': u"orm['targeting.ContentCategoryValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaigncity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_city'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaigncountry': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignCountry'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_country'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaigndomain': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignDomain'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_domain'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaigngender': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignGender'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_gender'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignmake': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignMake'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_make'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignmodel': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignModel'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_model'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignos': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignOs'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_os'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignosversion': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignOsVersion'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_os_version'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignpeer39brand': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Brand'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_brandprotection'", 'null': 'True', 'to': u"orm['targeting.Peer39BrandProtection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignpeer39contextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Contextual'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_contextual'", 'null': 'True', 'to': u"orm['targeting.Peer39ContextualSegment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignpeer39language': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Language'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.Peer39PageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignpeer39quality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPeer39Quality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagequality'", 'null': 'True', 'to': u"orm['targeting.Peer39PageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignposition': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPosition'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_position'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignproximiccontextual': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicContextual'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_contextual'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignproximiclanguage': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicLanguage'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagelanguage'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignproximicmaturity': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicMaturity'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_maturity'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicMaturityRating']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignproximicnotice': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicNotice'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagenoticeability'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignproximicplace': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicPlace'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pageplacement'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignproximicquality': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicQuality'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_pagequality'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignproximicsafety': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignProximicSafety'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_safety'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicSafetyLevel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignpublisher': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPublisher'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_publisher'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignpublishernetwork': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignPublisherNetwork'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_network'", 'null': 'True', 'to': u"orm['targeting.PublisherTargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignregion': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignRegion'},
            'bid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'bids_lost': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'clk': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'commission_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'conv_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'data_cost_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'dimension': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_campaign_region'", 'null': 'True', 'to': u"orm['targeting.TargetValue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'net_earned': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'winbid': ('ui.fields.BigDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'}),
            'winbid_value_total': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0', 'db_index': 'True'})
        },
        u'report.reportcampaignsite': {
            'Meta': {'unique_together': "(('dimension', 'related', 'time'),)", 'object_name': 'ReportCampaignSite'},
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
            'related': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']", 'to_field': "'id_random'"}),
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