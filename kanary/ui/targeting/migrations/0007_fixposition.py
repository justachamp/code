# -*- coding: utf-8 -*-
from functools import partial

from south.v2 import DataMigration
from django.core import management


class Migration(DataMigration):

    def forwards(self, orm):
        TargetValue = orm['targeting.TargetValue']
        Exchange = orm['targeting.Exchange']

        gender = partial(TargetValue.objects.get_or_create, category='gender')
        age_groups = partial(TargetValue.objects.get_or_create,
                             category='age_groups')
        position = partial(TargetValue.objects.get_or_create,
                           category='position')
        inventory = partial(TargetValue.objects.get_or_create,
                            category='inventory')

        nexage = Exchange.objects \
            .get_or_create(code='nexage', name='nexage')[0]
        appnexus = Exchange.objects\
            .get_or_create(code='appnexus', name='appnexus')[0]

        male = gender(value='Male')[0]
        female = gender(value='Female')[0]
        other = gender(value='Other')[0]
        unspecified = gender(value='Unspecified')[0]

        gender(value='male', exchange=appnexus, representant=male)
        gender(value='female', exchange=appnexus, representant=female)
        gender(value='', exchange=appnexus, representant=unspecified)

        gender(value='M', exchange=nexage, representant=male)
        gender(value='F', exchange=nexage, representant=female)
        gender(value='O', exchange=nexage, representant=other)
        gender(value='', exchange=nexage, representant=unspecified)

        age_15 = age_groups(value='Under 15', exchange=nexage)[0]
        age_15_24 = age_groups(value='15 to 24', exchange=nexage)[0]
        age_25_44 = age_groups(value='25 to 44', exchange=nexage)[0]
        age_45_64 = age_groups(value='45 to 64', exchange=nexage)[0]
        age_65 = age_groups(value='65 and upwards', exchange=nexage)[0]
        age_un = age_groups(value='Unspecified', exchange=nexage)[0]

        age_groups(value='Under 15', exchange=appnexus, representant=age_15)
        age_groups(value='15 to 24', exchange=appnexus, representant=age_15_24)
        age_groups(value='25 to 44', exchange=appnexus, representant=age_25_44)
        age_groups(value='45 to 64', exchange=appnexus, representant=age_45_64)
        age_groups(value='65 and upwards', exchange=appnexus,
                   representant=age_65)
        age_groups(value='Unspecified', exchange=appnexus, representant=age_un)

        above = position(value='Above the fold')[0]
        below = position(value='Below the fold')[0]
        unknown = position(value='Unknown')[0]
        unspecified = position(value='Unspecified')[0]

        position(value='1', exchange=nexage, representant=above)
        position(value='2', exchange=nexage, representant=unknown)
        position(value='3', exchange=nexage, representant=below)
        position(value='', exchange=nexage, representant=unspecified)

        position(value='above', exchange=appnexus, representant=above)
        position(value='below', exchange=appnexus, representant=below)
        position(value='unkown', exchange=appnexus, representant=unknown)
        position(value='', exchange=appnexus, representant=unspecified)

        app = inventory(value='Application')[0]
        web = inventory(value='Web')[0]
        unspecified = inventory(value='Unspecified')[0]

        inventory(value='app', exchange=nexage, representant=app)
        inventory(value='site', exchange=nexage, representant=web)
        inventory(value='', exchange=nexage, representant=unspecified)

    def backwards(self, orm):
        raise Exception('Missing backwards migration')

    models = {
        'targeting.appnexusbrand': {
            'Meta': {'object_name': 'AppNexusBrand'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['targeting.AppNexusCategory']", 'null': 'True'}),
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
        'targeting.appnexuscategory': {
            'Meta': {'object_name': 'AppNexusCategory'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_sensitive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['targeting.AppNexusContentCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
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
        'targeting.appnexustechnicalattr': {
            'Meta': {'object_name': 'AppNexusTechnicalAttr'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        u'targeting.exchange': {
            'Meta': {'object_name': 'Exchange'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'targeting.targetvalue': {
            'Meta': {'ordering': "('id',)", 'unique_together': "[('exchange', 'category', 'value')]", 'object_name': 'TargetValue'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targeting.Exchange']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inserted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'representant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'represented'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['targeting.TargetValue']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'})
        }
    }

    complete_apps = ['targeting']
    symmetrical = True
