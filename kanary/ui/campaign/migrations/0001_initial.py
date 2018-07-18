# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("targeting", "0001_initial"),
        ("storage", "0001_initial"),
    )

    def forwards(self, orm):
        # Adding model 'Campaign'
        db.create_table(u'campaign_campaign', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_random', self.gf('django.db.models.fields.CharField')(
                default='45faac968a078766d864f6473026366b120d58aa', unique=True, max_length=128)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('cache_is_dirty', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('budget_spent', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('budget_last_update', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start_UTC', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_UTC', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_archived', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('budget_total', self.gf('ui.fields.BudgetDecimalField')()),
            ('daily_budget_limit', self.gf('ui.fields.BudgetDecimalField')(null=True, blank=True)),
            ('is_budget_distributed_evenly', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cap_campaign_selected', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cap_strategy_selected', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cap_creative_selected', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cap_total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cap_strategy', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cap_creative', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cap_total_period', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('cap_strategy_period', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('cap_creative_period', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('cap_total_presented', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cap_strategy_presented', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cap_creative_presented', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cap_total_period_presented', self.gf(
                'django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('cap_strategy_period_presented', self.gf(
                'django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('cap_creative_period_presented', self.gf(
                'django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('landing_site', self.gf('django.db.models.fields.related.ForeignKey')(
                to=orm['storage.Site'], on_delete=models.PROTECT)),
        ))
        db.send_create_signal(u'campaign', ['Campaign'])

        # Adding unique constraint on 'Campaign', fields ['account', 'slug']
        db.create_unique(u'campaign_campaign', ['account_id', 'slug'])

        # Adding model 'SiteRatio'
        db.create_table(u'campaign_siteratio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(
                to=orm['storage.Site'], on_delete=models.PROTECT)),
            ('ratio', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('custom_variable', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'campaign', ['SiteRatio'])

        # Adding model 'Strategy'
        db.create_table(u'campaign_strategy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_random', self.gf('django.db.models.fields.CharField')(
                default='7b8dc0dfc7894fbe72ceed2d95b793fd59e615ed', unique=True, max_length=128)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('cache_is_dirty', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('budget_spent', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('budget_last_update', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Campaign'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.CharField')(default='Web', max_length=6)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_reviewed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('budget_total', self.gf('ui.fields.BudgetDecimalField')()),
            ('budget_daily', self.gf('ui.fields.BudgetDecimalField')(null=True, blank=True)),
            ('budget_daily_spent', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('budget_bid_CPM', self.gf('ui.fields.CPMDecimalField')()),
            ('capping_day', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('capping_total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('capping_day_spent', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('capping_total_spent', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_targeted_local', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_targeted_devices', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_targeted_keywords', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_targeted_publisher', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_targeted_user_profile', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('keywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('keywords_exclude', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('landing_site_variable', self.gf('django.db.models.fields.CharField')(
                max_length=511, null=True, blank=True)),
            ('is_UTM_tags', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_day_parted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'campaign', ['Strategy'])

        # Adding unique constraint on 'Strategy', fields ['campaign', 'slug']
        db.create_unique(u'campaign_strategy', ['campaign_id', 'slug'])

        # Adding M2M table for field exchanges on 'Strategy'
        db.create_table(u'campaign_strategy_exchanges', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('strategy', models.ForeignKey(orm[u'campaign.strategy'], null=False)),
            ('exchange', models.ForeignKey(orm[u'targeting.exchange'], null=False))
        ))
        db.create_unique(u'campaign_strategy_exchanges', ['strategy_id', 'exchange_id'])

        # Adding M2M table for field targeting_values on 'Strategy'
        db.create_table(u'campaign_strategy_targeting_values', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('strategy', models.ForeignKey(orm[u'campaign.strategy'], null=False)),
            ('targetvalue', models.ForeignKey(orm[u'targeting.targetvalue'], null=False))
        ))
        db.create_unique(u'campaign_strategy_targeting_values', ['strategy_id', 'targetvalue_id'])

        # Adding M2M table for field targeting_values_exclude on 'Strategy'
        db.create_table(u'campaign_strategy_targeting_values_exclude', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('strategy', models.ForeignKey(orm[u'campaign.strategy'], null=False)),
            ('targetvalue', models.ForeignKey(orm[u'targeting.targetvalue'], null=False))
        ))
        db.create_unique(u'campaign_strategy_targeting_values_exclude', ['strategy_id', 'targetvalue_id'])

        # Adding M2M table for field ad_positions on 'Strategy'
        db.create_table(u'campaign_strategy_ad_positions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('strategy', models.ForeignKey(orm[u'campaign.strategy'], null=False)),
            ('publisheradpositions', models.ForeignKey(orm[u'targeting.publisheradpositions'], null=False))
        ))
        db.create_unique(u'campaign_strategy_ad_positions', ['strategy_id', 'publisheradpositions_id'])

        # Adding M2M table for field ad_positions_exclude on 'Strategy'
        db.create_table(u'campaign_strategy_ad_positions_exclude', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('strategy', models.ForeignKey(orm[u'campaign.strategy'], null=False)),
            ('publisheradpositions', models.ForeignKey(orm[u'targeting.publisheradpositions'], null=False))
        ))
        db.create_unique(u'campaign_strategy_ad_positions_exclude', ['strategy_id', 'publisheradpositions_id'])

        # Adding M2M table for field inventory_type on 'Strategy'
        db.create_table(u'campaign_strategy_inventory_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('strategy', models.ForeignKey(orm[u'campaign.strategy'], null=False)),
            ('publishersinventorytype', models.ForeignKey(orm[u'targeting.publishersinventorytype'], null=False))
        ))
        db.create_unique(u'campaign_strategy_inventory_type', ['strategy_id', 'publishersinventorytype_id'])

        # Adding M2M table for field inventory_type_exclude on 'Strategy'
        db.create_table(u'campaign_strategy_inventory_type_exclude', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('strategy', models.ForeignKey(orm[u'campaign.strategy'], null=False)),
            ('publishersinventorytype', models.ForeignKey(orm[u'targeting.publishersinventorytype'], null=False))
        ))
        db.create_unique(u'campaign_strategy_inventory_type_exclude', ['strategy_id', 'publishersinventorytype_id'])

        # Adding M2M table for field age_groups on 'Strategy'
        db.create_table(u'campaign_strategy_age_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('strategy', models.ForeignKey(orm[u'campaign.strategy'], null=False)),
            ('agegroup', models.ForeignKey(orm[u'targeting.agegroup'], null=False))
        ))
        db.create_unique(u'campaign_strategy_age_groups', ['strategy_id', 'agegroup_id'])

        # Adding M2M table for field age_groups_exclude on 'Strategy'
        db.create_table(u'campaign_strategy_age_groups_exclude', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('strategy', models.ForeignKey(orm[u'campaign.strategy'], null=False)),
            ('agegroup', models.ForeignKey(orm[u'targeting.agegroup'], null=False))
        ))
        db.create_unique(u'campaign_strategy_age_groups_exclude', ['strategy_id', 'agegroup_id'])

        # Adding M2M table for field genders on 'Strategy'
        db.create_table(u'campaign_strategy_genders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('strategy', models.ForeignKey(orm[u'campaign.strategy'], null=False)),
            ('gender', models.ForeignKey(orm[u'targeting.gender'], null=False))
        ))
        db.create_unique(u'campaign_strategy_genders', ['strategy_id', 'gender_id'])

        # Adding M2M table for field genders_exclude on 'Strategy'
        db.create_table(u'campaign_strategy_genders_exclude', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('strategy', models.ForeignKey(orm[u'campaign.strategy'], null=False)),
            ('gender', models.ForeignKey(orm[u'targeting.gender'], null=False))
        ))
        db.create_unique(u'campaign_strategy_genders_exclude', ['strategy_id', 'gender_id'])

        # Adding M2M table for field landing_sites on 'Strategy'
        db.create_table(u'campaign_strategy_landing_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('strategy', models.ForeignKey(orm[u'campaign.strategy'], null=False)),
            ('siteratio', models.ForeignKey(orm[u'campaign.siteratio'], null=False))
        ))
        db.create_unique(u'campaign_strategy_landing_sites', ['strategy_id', 'siteratio_id'])

        # Adding model 'BiddingPeriod'
        db.create_table(u'campaign_biddingperiod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('start', self.gf('django.db.models.fields.TimeField')()),
            ('end', self.gf('django.db.models.fields.TimeField')()),
            ('strategy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Strategy'])),
        ))
        db.send_create_signal(u'campaign', ['BiddingPeriod'])

        # Adding model 'Advert'
        db.create_table(u'campaign_advert', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_random', self.gf('django.db.models.fields.CharField')(
                default='3edd6996fe3f47e646d1dd3105549ede575bf01d', unique=True, max_length=128)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('cache_is_dirty', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('budget_spent', self.gf('ui.fields.BudgetSpentDecimalField')(default=0)),
            ('budget_last_update', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('strategy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Strategy'])),
            ('creative', self.gf('django.db.models.fields.related.ForeignKey')(
                to=orm['storage.Creative'], on_delete=models.PROTECT)),
            ('landing_site', self.gf('django.db.models.fields.related.ForeignKey')(
                to=orm['storage.Site'], null=True, on_delete=models.PROTECT)),
            ('custom_variable', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('custom_bid_CPM', self.gf('ui.fields.CPMDecimalField')(null=True)),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'campaign', ['Advert'])

        # Adding model 'AdvertPeriod'
        db.create_table(u'campaign_advertperiod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('advert', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.Advert'])),
            ('period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaign.BiddingPeriod'])),
            ('custom_bid_CPM', self.gf('ui.fields.CPMDecimalField')()),
        ))
        db.send_create_signal(u'campaign', ['AdvertPeriod'])

    def backwards(self, orm):
        # Removing unique constraint on 'Strategy', fields ['campaign', 'slug']
        db.delete_unique(u'campaign_strategy', ['campaign_id', 'slug'])

        # Removing unique constraint on 'Campaign', fields ['account', 'slug']
        db.delete_unique(u'campaign_campaign', ['account_id', 'slug'])

        # Deleting model 'Campaign'
        db.delete_table(u'campaign_campaign')

        # Deleting model 'SiteRatio'
        db.delete_table(u'campaign_siteratio')

        # Deleting model 'Strategy'
        db.delete_table(u'campaign_strategy')

        # Removing M2M table for field exchanges on 'Strategy'
        db.delete_table('campaign_strategy_exchanges')

        # Removing M2M table for field targeting_values on 'Strategy'
        db.delete_table('campaign_strategy_targeting_values')

        # Removing M2M table for field targeting_values_exclude on 'Strategy'
        db.delete_table('campaign_strategy_targeting_values_exclude')

        # Removing M2M table for field ad_positions on 'Strategy'
        db.delete_table('campaign_strategy_ad_positions')

        # Removing M2M table for field ad_positions_exclude on 'Strategy'
        db.delete_table('campaign_strategy_ad_positions_exclude')

        # Removing M2M table for field inventory_type on 'Strategy'
        db.delete_table('campaign_strategy_inventory_type')

        # Removing M2M table for field inventory_type_exclude on 'Strategy'
        db.delete_table('campaign_strategy_inventory_type_exclude')

        # Removing M2M table for field age_groups on 'Strategy'
        db.delete_table('campaign_strategy_age_groups')

        # Removing M2M table for field age_groups_exclude on 'Strategy'
        db.delete_table('campaign_strategy_age_groups_exclude')

        # Removing M2M table for field genders on 'Strategy'
        db.delete_table('campaign_strategy_genders')

        # Removing M2M table for field genders_exclude on 'Strategy'
        db.delete_table('campaign_strategy_genders_exclude')

        # Removing M2M table for field landing_sites on 'Strategy'
        db.delete_table('campaign_strategy_landing_sites')

        # Deleting model 'BiddingPeriod'
        db.delete_table(u'campaign_biddingperiod')

        # Deleting model 'Advert'
        db.delete_table(u'campaign_advert')

        # Deleting model 'AdvertPeriod'
        db.delete_table(u'campaign_advertperiod')

    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '40'})
        },
        u'campaign.advert': {
            'Meta': {'object_name': 'Advert'},
            'budget_last_update': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'budget_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'cache_is_dirty': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'creative': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['storage.Creative']", 'on_delete': 'models.PROTECT'}),
            'custom_bid_CPM': ('ui.fields.CPMDecimalField', [], {'null': 'True'}),
            'custom_variable': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'default': "'ba7d40899c8833005991f01eaf7001a0b54610c4'", 'unique': 'True', 'max_length': '128'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landing_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['storage.Site']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'strategy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']"})
        },
        u'campaign.advertperiod': {
            'Meta': {'object_name': 'AdvertPeriod'},
            'advert': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Advert']"}),
            'custom_bid_CPM': ('ui.fields.CPMDecimalField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.BiddingPeriod']"})
        },
        u'campaign.biddingperiod': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'BiddingPeriod'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'strategy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Strategy']"})
        },
        u'campaign.campaign': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('account', 'slug'),)", 'object_name': 'Campaign'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'budget_last_update': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'budget_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
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
            'daily_budget_limit': ('ui.fields.BudgetDecimalField', [], {'null': 'True', 'blank': 'True'}),
            'end_UTC': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'default': "'c67043dcb2c4055ee1c1b7aaed41cc6e47bdf90b'", 'unique': 'True', 'max_length': '128'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_budget_distributed_evenly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landing_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['storage.Site']", 'on_delete': 'models.PROTECT'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_UTC': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'campaign.siteratio': {
            'Meta': {'object_name': 'SiteRatio'},
            'custom_variable': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ratio': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['storage.Site']", 'on_delete': 'models.PROTECT'})
        },
        u'campaign.strategy': {
            'Meta': {'ordering': "['name']", 'unique_together': "[('campaign', 'slug')]", 'object_name': 'Strategy'},
            'ad_positions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.PublisherAdPositions']", 'symmetrical': 'False', 'blank': 'True'}),
            'ad_positions_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.PublisherAdPositions']"}),
            'age_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.AgeGroup']", 'symmetrical': 'False', 'blank': 'True'}),
            'age_groups_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.AgeGroup']"}),
            'budget_bid_CPM': ('ui.fields.CPMDecimalField', [], {}),
            'budget_daily': ('ui.fields.BudgetDecimalField', [], {'null': 'True', 'blank': 'True'}),
            'budget_daily_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_last_update': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'budget_spent': ('ui.fields.BudgetSpentDecimalField', [], {'default': '0'}),
            'budget_total': ('ui.fields.BudgetDecimalField', [], {}),
            'cache_is_dirty': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campaign.Campaign']"}),
            'capping_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'capping_day_spent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'capping_total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'capping_total_spent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'exchanges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.Exchange']", 'symmetrical': 'False', 'blank': 'True'}),
            'genders': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.Gender']", 'symmetrical': 'False', 'blank': 'True'}),
            'genders_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.Gender']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'default': "'ae3c8610a939ce461b0661df92a9400ed3f3a0c2'", 'unique': 'True', 'max_length': '128'}),
            'inventory_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.PublishersInventoryType']", 'symmetrical': 'False', 'blank': 'True'}),
            'inventory_type_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.PublishersInventoryType']"}),
            'is_UTM_tags': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_day_parted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_targeted_devices': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_targeted_keywords': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_targeted_local': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_targeted_publisher': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_targeted_user_profile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'keywords_exclude': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'landing_site_variable': ('django.db.models.fields.CharField', [], {'max_length': '511', 'null': 'True', 'blank': 'True'}),
            'landing_sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['campaign.SiteRatio']", 'symmetrical': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'targeting_values': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targeting.TargetValue']", 'symmetrical': 'False', 'blank': 'True'}),
            'targeting_values_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': u"orm['targeting.TargetValue']"}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Web'", 'max_length': '6'})
        },
        u'storage.creative': {
            'Meta': {'object_name': 'Creative'},
            'appnexus_feedback': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'appnexus_sla_eta': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'appnexus_status': ('django.db.models.fields.CharField', [], {'default': "'n'", 'max_length': '1'}),
            'cache_is_dirty': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'default': "'194911010ac53c9d73d8f15e0dd7f701b78890a1'", 'unique': 'True', 'max_length': '128'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_folder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landing_site_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['storage.Creative']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'storage.site': {
            'Meta': {'object_name': 'Site'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_random': ('django.db.models.fields.CharField', [], {'default': "'bce904776aea6cf05f7a9600754ca3191431865b'", 'unique': 'True', 'max_length': '128'}),
            'is_folder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['storage.Site']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'targeting.agegroup': {
            'Meta': {'object_name': 'AgeGroup'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        u'targeting.exchange': {
            'Meta': {'object_name': 'Exchange'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'targeting.gender': {
            'Meta': {'object_name': 'Gender'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'targeting.publisheradpositions': {
            'Meta': {'ordering': "('name',)", 'object_name': 'PublisherAdPositions'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'targeting.publishersinventorytype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'PublishersInventoryType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'targeting.targetvalue': {
            'Meta': {'unique_together': "[('exchange', 'category', 'value')]", 'object_name': 'TargetValue'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targeting.Exchange']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inserted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'representant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'represented'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['targeting.TargetValue']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'})
        }
    }

    complete_apps = ['campaign']
