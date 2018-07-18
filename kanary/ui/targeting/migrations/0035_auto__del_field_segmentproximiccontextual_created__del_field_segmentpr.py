# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Heavy migration!
        # It took 5 minutes locally to alter columns on productional sql dump.

        # Deleting field 'SegmentProximicContextual.created'
        db.delete_column(u'targeting_segmentproximiccontextual', 'created')

        # Deleting field 'SegmentProximicContextual.modified'
        db.delete_column(u'targeting_segmentproximiccontextual', 'modified')


        # Changing field 'SegmentProximicContextual.name'
        db.alter_column(u'targeting_segmentproximiccontextual', 'name', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'SegmentProximicPageLanguage.created'
        db.delete_column(u'targeting_segmentproximicpagelanguage', 'created')

        # Deleting field 'SegmentProximicPageLanguage.modified'
        db.delete_column(u'targeting_segmentproximicpagelanguage', 'modified')


        # Changing field 'SegmentProximicPageLanguage.name'
        db.alter_column(u'targeting_segmentproximicpagelanguage', 'name', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'TargetValue.created'
        db.delete_column(u'targeting_targetvalue', 'created')

        # Deleting field 'TargetValue.modified'
        db.delete_column(u'targeting_targetvalue', 'modified')


        # Changing field 'TargetValue.value'
        db.alter_column(u'targeting_targetvalue', 'value', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'ContentCategoryValue.created'
        db.delete_column(u'targeting_contentcategoryvalue', 'created')

        # Deleting field 'ContentCategoryValue.modified'
        db.delete_column(u'targeting_contentcategoryvalue', 'modified')


        # Changing field 'ContentCategoryValue.name'
        db.alter_column(u'targeting_contentcategoryvalue', 'name', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'Peer39PageLanguage.created'
        db.delete_column(u'targeting_peer39pagelanguage', 'created')

        # Deleting field 'Peer39PageLanguage.modified'
        db.delete_column(u'targeting_peer39pagelanguage', 'modified')

        # Deleting field 'SegmentProximicPagePlacement.created'
        db.delete_column(u'targeting_segmentproximicpageplacement', 'created')

        # Deleting field 'SegmentProximicPagePlacement.modified'
        db.delete_column(u'targeting_segmentproximicpageplacement', 'modified')


        # Changing field 'SegmentProximicPagePlacement.name'
        db.alter_column(u'targeting_segmentproximicpageplacement', 'name', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'Peer39ContextualSegment.created'
        db.delete_column(u'targeting_peer39contextualsegment', 'created')

        # Deleting field 'Peer39ContextualSegment.modified'
        db.delete_column(u'targeting_peer39contextualsegment', 'modified')


        # Changing field 'Peer39ContextualSegment.name'
        db.alter_column(u'targeting_peer39contextualsegment', 'name', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'ContentCategory.created'
        db.delete_column(u'targeting_contentcategory', 'created')

        # Deleting field 'ContentCategory.modified'
        db.delete_column(u'targeting_contentcategory', 'modified')


        # Changing field 'ContentCategory.name'
        db.alter_column(u'targeting_contentcategory', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Exchange.code'
        db.alter_column(u'targeting_exchange', 'code', self.gf('django.db.models.fields.TextField')(unique=True))
        # Removing index on 'Exchange', fields ['code']
        db.delete_index(u'targeting_exchange', ['code'])

        # Adding unique constraint on 'Exchange', fields ['code']
        db.create_unique(u'targeting_exchange', ['code'])


        # Changing field 'Exchange.name'
        db.alter_column(u'targeting_exchange', 'name', self.gf('django.db.models.fields.TextField')(unique=True))
        # Adding unique constraint on 'Exchange', fields ['name']
        db.create_unique(u'targeting_exchange', ['name'])

        # Deleting field 'Peer39BrandProtection.created'
        db.delete_column(u'targeting_peer39brandprotection', 'created')

        # Deleting field 'Peer39BrandProtection.modified'
        db.delete_column(u'targeting_peer39brandprotection', 'modified')

        # Deleting field 'SegmentProximicPageQuality.created'
        db.delete_column(u'targeting_segmentproximicpagequality', 'created')

        # Deleting field 'SegmentProximicPageQuality.modified'
        db.delete_column(u'targeting_segmentproximicpagequality', 'modified')


        # Changing field 'SegmentProximicPageQuality.name'
        db.alter_column(u'targeting_segmentproximicpagequality', 'name', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'SegmentProximicMaturityRating.created'
        db.delete_column(u'targeting_segmentproximicmaturityrating', 'created')

        # Deleting field 'SegmentProximicMaturityRating.modified'
        db.delete_column(u'targeting_segmentproximicmaturityrating', 'modified')

        # Deleting field 'Peer39PageQuality.created'
        db.delete_column(u'targeting_peer39pagequality', 'created')

        # Deleting field 'Peer39PageQuality.modified'
        db.delete_column(u'targeting_peer39pagequality', 'modified')


        # Changing field 'Peer39PageQuality.name'
        db.alter_column(u'targeting_peer39pagequality', 'name', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'SegmentProximicPageNoticeability.created'
        db.delete_column(u'targeting_segmentproximicpagenoticeability', 'created')

        # Deleting field 'SegmentProximicPageNoticeability.modified'
        db.delete_column(u'targeting_segmentproximicpagenoticeability', 'modified')


        # Changing field 'SegmentProximicPageNoticeability.name'
        db.alter_column(u'targeting_segmentproximicpagenoticeability', 'name', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'SegmentProximicSafetyLevel.created'
        db.delete_column(u'targeting_segmentproximicsafetylevel', 'created')

        # Deleting field 'SegmentProximicSafetyLevel.modified'
        db.delete_column(u'targeting_segmentproximicsafetylevel', 'modified')


    def backwards(self, orm):
        # Removing unique constraint on 'Exchange', fields ['name']
        db.delete_unique(u'targeting_exchange', ['name'])

        # Removing unique constraint on 'Exchange', fields ['code']
        db.delete_unique(u'targeting_exchange', ['code'])

        # Adding index on 'Exchange', fields ['code']
        db.create_index(u'targeting_exchange', ['code'])

        # Adding field 'SegmentProximicContextual.created'
        db.add_column(u'targeting_segmentproximiccontextual', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'SegmentProximicContextual.modified'
        db.add_column(u'targeting_segmentproximiccontextual', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


        # Changing field 'SegmentProximicContextual.name'
        db.alter_column(u'targeting_segmentproximiccontextual', 'name', self.gf('django.db.models.fields.CharField')(max_length=900))
        # Adding field 'SegmentProximicPageLanguage.created'
        db.add_column(u'targeting_segmentproximicpagelanguage', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'SegmentProximicPageLanguage.modified'
        db.add_column(u'targeting_segmentproximicpagelanguage', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


        # Changing field 'SegmentProximicPageLanguage.name'
        db.alter_column(u'targeting_segmentproximicpagelanguage', 'name', self.gf('django.db.models.fields.CharField')(max_length=900))
        # Adding field 'TargetValue.created'
        db.add_column(u'targeting_targetvalue', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'TargetValue.modified'
        db.add_column(u'targeting_targetvalue', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


        # Changing field 'TargetValue.value'
        db.alter_column(u'targeting_targetvalue', 'value', self.gf('django.db.models.fields.CharField')(max_length=900))
        # Adding field 'ContentCategoryValue.created'
        db.add_column(u'targeting_contentcategoryvalue', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'ContentCategoryValue.modified'
        db.add_column(u'targeting_contentcategoryvalue', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


        # Changing field 'ContentCategoryValue.name'
        db.alter_column(u'targeting_contentcategoryvalue', 'name', self.gf('django.db.models.fields.CharField')(max_length=900))
        # Adding field 'Peer39PageLanguage.created'
        db.add_column(u'targeting_peer39pagelanguage', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Peer39PageLanguage.modified'
        db.add_column(u'targeting_peer39pagelanguage', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'SegmentProximicPagePlacement.created'
        db.add_column(u'targeting_segmentproximicpageplacement', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'SegmentProximicPagePlacement.modified'
        db.add_column(u'targeting_segmentproximicpageplacement', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


        # Changing field 'SegmentProximicPagePlacement.name'
        db.alter_column(u'targeting_segmentproximicpageplacement', 'name', self.gf('django.db.models.fields.CharField')(max_length=900))
        # Adding field 'Peer39ContextualSegment.created'
        db.add_column(u'targeting_peer39contextualsegment', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Peer39ContextualSegment.modified'
        db.add_column(u'targeting_peer39contextualsegment', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


        # Changing field 'Peer39ContextualSegment.name'
        db.alter_column(u'targeting_peer39contextualsegment', 'name', self.gf('django.db.models.fields.CharField')(max_length=900))
        # Adding field 'ContentCategory.created'
        db.add_column(u'targeting_contentcategory', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'ContentCategory.modified'
        db.add_column(u'targeting_contentcategory', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


        # Changing field 'ContentCategory.name'
        db.alter_column(u'targeting_contentcategory', 'name', self.gf('django.db.models.fields.CharField')(max_length=900))

        # Changing field 'Exchange.code'
        db.alter_column(u'targeting_exchange', 'code', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Exchange.name'
        db.alter_column(u'targeting_exchange', 'name', self.gf('django.db.models.fields.CharField')(max_length=160))
        # Adding field 'Peer39BrandProtection.created'
        db.add_column(u'targeting_peer39brandprotection', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Peer39BrandProtection.modified'
        db.add_column(u'targeting_peer39brandprotection', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'SegmentProximicPageQuality.created'
        db.add_column(u'targeting_segmentproximicpagequality', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'SegmentProximicPageQuality.modified'
        db.add_column(u'targeting_segmentproximicpagequality', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


        # Changing field 'SegmentProximicPageQuality.name'
        db.alter_column(u'targeting_segmentproximicpagequality', 'name', self.gf('django.db.models.fields.CharField')(max_length=900))
        # Adding field 'SegmentProximicMaturityRating.created'
        db.add_column(u'targeting_segmentproximicmaturityrating', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'SegmentProximicMaturityRating.modified'
        db.add_column(u'targeting_segmentproximicmaturityrating', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Peer39PageQuality.created'
        db.add_column(u'targeting_peer39pagequality', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Peer39PageQuality.modified'
        db.add_column(u'targeting_peer39pagequality', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


        # Changing field 'Peer39PageQuality.name'
        db.alter_column(u'targeting_peer39pagequality', 'name', self.gf('django.db.models.fields.CharField')(max_length=900))
        # Adding field 'SegmentProximicPageNoticeability.created'
        db.add_column(u'targeting_segmentproximicpagenoticeability', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'SegmentProximicPageNoticeability.modified'
        db.add_column(u'targeting_segmentproximicpagenoticeability', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


        # Changing field 'SegmentProximicPageNoticeability.name'
        db.alter_column(u'targeting_segmentproximicpagenoticeability', 'name', self.gf('django.db.models.fields.CharField')(max_length=900))
        # Adding field 'SegmentProximicSafetyLevel.created'
        db.add_column(u'targeting_segmentproximicsafetylevel', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'SegmentProximicSafetyLevel.modified'
        db.add_column(u'targeting_segmentproximicsafetylevel', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


    models = {
        'targeting.appnexusbrand': {
            'Meta': {'object_name': 'AppNexusBrand'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'num_creatives': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'urls': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'targeting.appnexusbrowser': {
            'Meta': {'object_name': 'AppNexusBrowser'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'platform_type': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'targeting.appnexuscarrier': {
            'Meta': {'object_name': 'AppNexusCarrier'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'country_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexuscontentcategory': {
            'Meta': {'object_name': 'AppNexusContentCategory'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_system': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['targeting.AppNexusContentCategory']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'targeting.appnexusdevicemake': {
            'Meta': {'object_name': 'AppNexusDeviceMake'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexusdevicemodel': {
            'Meta': {'unique_together': "(('name', 'make_appnexus_id'),)", 'object_name': 'AppNexusDeviceModel'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'device_type': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'make_appnexus_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'screen_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'screen_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'})
        },
        'targeting.appnexusinventoryattr': {
            'Meta': {'object_name': 'AppNexusInventoryAttr'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexuslanguage': {
            'Meta': {'object_name': 'AppNexusLanguage'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexusos': {
            'Meta': {'object_name': 'AppNexusOS'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'platform_type': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'targeting.appnexussegment': {
            'Meta': {'object_name': 'AppNexusSegment'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexustechnicalattr': {
            'Meta': {'object_name': 'AppNexusTechnicalAttr'},
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

    complete_apps = ['targeting']
