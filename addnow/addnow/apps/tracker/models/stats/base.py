# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import inspect
from bson.son import SON
from calendar import monthrange
from copy import deepcopy

from schematics.models import ModelMeta
from schematics.types.base import IntType, DateTimeType, StringType
from schematics.types.compound import ModelType, DictType

from addnow.apps.tracker.models.base import BaseModel


class StatsModelMetaClass(ModelMeta):
    def __new__(mcs, name, bases, attrs):
        all_attrs = {}
        for base in reversed(bases):
            all_attrs.update(dict(inspect.getmembers(base)))
        all_attrs.update(attrs)
        type_name = all_attrs['type_name']
        stats_class = all_attrs['stats_class']
        has_granularity = all_attrs['has_granularity']
        if type_name:
            attrs['type'] = StringType(required=True, default=all_attrs['type_name'])
        if stats_class:
            attrs['totals'] = ModelType(stats_class)
            if has_granularity:
                attrs['values'] = DictType(ModelType(stats_class))
        new_class = super(StatsModelMetaClass, mcs).__new__(mcs, name, bases, attrs)
        index_fields = getattr(new_class, 'index_fields', new_class.data_fields)
        indexes = deepcopy(new_class.indexes)
        index = indexes[0]['index']
        # add specific fields to index
        for field in index_fields:
            index_entry = (field, 1)
            if index_entry not in index:
                index.append(index_entry)
        new_class.indexes = indexes
        return new_class


class BaseStatsModel(BaseModel):
    __metaclass__ = StatsModelMetaClass

    has_granularity = False
    granularity_name = None
    type_name = None
    stats_class = None
    data_fields = []

    site = IntType(required=True)

    indexes = [
        {
            'index': [('site', 1), ('type', 1)]
        }
    ]

    @classmethod
    def get_events(cls):
        return cls.totals.fields.keys()

    def find(self, query=None, *args, **kwargs):
        query = query or {}
        if self.type:
            query['type'] = self.type
        return super(BaseStatsModel, self).find(query, *args, **kwargs)

    def find_one(self, query=None, *args, **kwargs):
        query = query or {}
        if self.type:
            query['type'] = self.type
        return super(BaseStatsModel, self).find_one(query, *args, **kwargs)

    def get_totals(self, site_id, begin_date, end_date, events=None, group_fields=None,
                   aggregate_by_values=False, limit=None):
        events = events or self.get_events()
        if group_fields is None:
            group_fields = self.data_fields

        match = {
            'site': site_id,
            'type': self.type,
            'date': {
                '$gte': self.get_min_date(begin_date) if aggregate_by_values else begin_date,
                '$lte': end_date
            }
        }
        group = {'_id': {field: ('$%s' % field) for field in group_fields}}
        sort = SON([(event, -1) for event in events])

        result = self._aggregate(begin_date, end_date, events, aggregate_by_values,
                                 filter_values=True, match=match, group=group, sort=sort, limit=limit)
        return result

    def _replace_date(self, data, begin_date, end_date):
        for item in data:
            item['date'] = item['date'].replace(**{self.granularity_name: item[self.granularity_name]})
            del item[self.granularity_name]
        data = [item for item in data if begin_date <= item['date'] <= end_date]
        return data

    def _aggregate(self, begin_date, end_date, events, aggregate_by_values, filter_values,
                   match, group, sort=None, limit=None):
        pipeline = [{'$match': match}]
        sum_key = 'values' if aggregate_by_values else 'totals'
        for event in events:
            group[event] = {'$sum': '$%s.%s' % (sum_key, event)}
        if aggregate_by_values:
            pipeline.append({'$unwind': '$values'})
            if filter_values:
                granularity_range = self.granularity_range(begin_date)
                pipeline.append({
                    '$match': {
                        'values.%s' % self.granularity_name: {
                            '$gte': getattr(begin_date, self.granularity_name) or granularity_range[0],
                            '$lte': getattr(end_date, self.granularity_name) or granularity_range[1]
                        }
                    }
                })
        pipeline.append({'$group': group})
        # exclude zero values
        pipeline.append({
            '$match': {
                '$or': [{event: {'$ne': 0}} for event in events]
            }
        })
        if sort:
            pipeline.append({'$sort': sort})
        if limit:
            pipeline.append({'$limit': limit})
        result = list(self.collection.aggregate(pipeline, allowDiskUse=True))
        result = self._replace_id(result)
        return result

    def get_report(self, site_id, begin_date, end_date, events, dimensions, summary=False, aggregate_by_values=False):
        from addnow.apps.tracker.models.reports import ALL_DIMENSIONS

        match = {
            'site': site_id,
            'date': {
                '$gte': self.get_min_date(begin_date) if aggregate_by_values else begin_date,
                '$lte': end_date
            },
            'type': {'$in': dimensions}
        }
        group = {
            '_id': {'date': '$date', 'dimension': '$type'}
        }

        if not summary:
            for dimension in dimensions:
                dimension_class = ALL_DIMENSIONS[dimension]
                for field in dimension_class.get_data_fields():
                    group['_id'][field] = '$%s' % field
        if aggregate_by_values:
            group['_id'][self.granularity_name] = '$values.%s' % self.granularity_name
            sort = SON([('_id.date', 1), ('_id.%s' % self.granularity_name, 1)])
        else:
            sort = {'_id.date': 1}
        result = self._aggregate(begin_date, end_date, events, aggregate_by_values, filter_values=False,
                                 match=match, group=group, sort=sort)
        if aggregate_by_values:
            result = self._replace_date(result, begin_date, end_date)
        return result

    def get_events_summary(self, site_id, begin_date, end_date, events, aggregate_by_values=False):
        from addnow.apps.tracker.models.reports import REPORT_TYPES

        dimensions = [REPORT_TYPES[event].event_singular for event in events]
        match = {
            'site': site_id,
            'date': {
                '$gte': self.get_min_date(begin_date) if aggregate_by_values else begin_date,
                '$lte': end_date
            },
            'type': {'$in': dimensions}
        }
        group = {
            '_id': {'date': '$date'}
        }
        if aggregate_by_values:
            group['_id'][self.granularity_name] = '$values.%s' % self.granularity_name
            sort = SON([('_id.date', 1), ('_id.%s' % self.granularity_name, 1)])
        else:
            sort = {'_id.date': 1}
        result = self._aggregate(begin_date, end_date, events, aggregate_by_values,
                                 filter_values=False, match=match, group=group, sort=sort)
        if aggregate_by_values:
            result = self._replace_date(result, begin_date, end_date)
        return result

    def _prepare_query(self, kwargs):
        self.import_data(kwargs)
        self.validate()
        query = self.to_native()
        if 'date' in query:
            query['date'] = self.get_min_date(self.date)
        del query['totals']
        if 'values' in query:
            del query['values']
        return query

    def _prepare_update(self, event, value=1):
        fields = {'totals.%s' % event: value}
        if self.has_granularity:
            fields['values.$.%s' % event] = value
        return fields

    def _preallocate(self, query):
        doc = {
            'totals': {}
        }
        doc.update(query)
        events = self.get_events()

        for event in events:
            doc['totals'][event] = 0

        if self.has_granularity:
            doc['values'] = []
            granularity_range = self.granularity_range(self.date)
            for period in range(*granularity_range):
                counters = {event: 0 for event in events}
                counters[self.granularity_name] = period
                doc['values'].append(counters)

        self.collection.insert_one(doc)

    def inc_counter(self, event, value=1, **kwargs):
        query = self._prepare_query(kwargs)
        update_query = query.copy()
        fields = self._prepare_update(event, value)

        if self.has_granularity:
            update_query['values.%s' % self.granularity_name] = self.get_granularity_item_from_date(self.date)
        update_result = self.inc(update_query, fields, validate=False)
        if update_result.matched_count == 0:
            self._preallocate(query)
            # TODO: remove many=True after migration (merging counters)
            self.inc(update_query, fields, validate=False, many=True)


class BaseAll(BaseStatsModel):
    collection_name = 'stats.all'


class BasePeriod(BaseStatsModel):
    has_granularity = True
    date = DateTimeType(required=True)

    indexes = [
        {
            'index': [('site', 1), ('type', 1), ('date', 1)]
        }
    ]

    def get_granularity_item_from_date(self, date):
        raise NotImplementedError()

    def get_min_date(self, date):
        raise NotImplementedError()

    def granularity_range(self, date):
        raise NotImplementedError()


class BaseDaily(BasePeriod):
    collection_name = 'stats.daily'
    granularity_name = 'hour'

    def get_granularity_item_from_date(self, date):
        return date.hour

    def get_min_date(self, date):
        return date.replace(hour=0, minute=0, second=0, microsecond=0)

    def granularity_range(self, date):
        return 0, 24


class BaseMonthly(BasePeriod):
    collection_name = 'stats.monthly'
    granularity_name = 'day'

    def get_granularity_item_from_date(self, date):
        return date.day

    def get_min_date(self, date):
        return date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    def granularity_range(self, date):
        return 1, monthrange(date.year, date.month)[1] + 1


class BaseYearly(BasePeriod):
    collection_name = 'stats.yearly'
    granularity_name = 'month'

    def get_granularity_item_from_date(self, date):
        return date.month

    def get_min_date(self, date):
        return date.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

    def granularity_range(self, date):
        return 1, 13
