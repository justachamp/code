# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.models import Model
from schematics.types.base import IntType, FloatType, StringType, DateTimeType, URLType, SHA1Type
from schematics.types.compound import ModelType

from addnow.apps.tracker.models.base import BaseModel
from addnow.apps.tracker.utils import get_checksum


GEO_IP_TTL = 60 * 60 * 24


class OutsideShares(BaseModel):
    collection_name = 'outside_shares'
    indexes = [
        {
            'index': [('site', 1), ('checksum', 1), ('source', 1)],
            'args': {'unique': True}
        }
    ]

    site = IntType(required=True)
    url = URLType(required=True)
    checksum = SHA1Type()
    source = StringType(required=True)
    shares = IntType()

    data_fields = ['url', 'checksum', 'source']

    def _add_checksum(self, query):
        query = query or {}
        if 'url' in query:
            query['checksum'] = get_checksum(query['url'])

    def validate_checksum(self, data, value):
        checksum = get_checksum(data['url'])
        data['checksum'] = checksum
        return checksum

    def find(self, query=None, *args, **kwargs):
        self._add_checksum(query)
        return super(OutsideShares, self).find(query, *args, **kwargs)

    def find_one(self, query=None, *args, **kwargs):
        self._add_checksum(query)
        return super(OutsideShares, self).find_one(query, *args, **kwargs)

    def get_totals(self, site_id, group_fields=None, limit=None):
        match = {'site': site_id}
        group = {'_id': {}, 'shares': {'$sum': '$shares'}}
        sort = {'shares': -1}

        if group_fields is None:
            group_fields = self.data_fields
        for field in group_fields:
            group['_id'][field] = '$%s' % field
        pipeline = [{'$match': match}, {'$group': group}, {'$sort': sort}]
        if limit is not None:
            pipeline.append({'$limit': limit})
        result = list(self.collection.aggregate(pipeline))
        return self._replace_id(result)

    def get_totals_without_group(self, site_id):
        totals = self.get_totals(site_id, group_fields=[])
        if not totals:
            return {'shares': 0}
        return totals[0]

    def set_counter(self, site, url, source, value):
        checksum = get_checksum(url)
        query = dict(site=site, url=url, checksum=checksum, source=source)
        self.set(query, {'shares': value}, upsert=True)


class UpdateCounters(BaseModel):
    collection_name = 'update_counters'


class GeoData(Model):
    country = StringType(required=True)
    city = StringType(required=False)
    latitude = FloatType(required=True)
    longitude = FloatType(required=True)


class GeoIPModel(BaseModel):
    collection_name = 'geoip'
    indexes = [
        {
            'index': [('timestamp', 1)],
            'args': {'expireAfterSeconds': GEO_IP_TTL}
        }
    ]

    site = IntType(required=True)
    timestamp = DateTimeType(required=True)
    geo = ModelType(GeoData, strict=False)
