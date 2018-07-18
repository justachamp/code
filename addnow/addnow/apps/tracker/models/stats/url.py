# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.types.base import StringType, SHA1Type, URLType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.stats.click import ClickStats
from addnow.apps.tracker.models.stats.share import ShareStats
from addnow.apps.tracker.models.stats.view import ViewStats
from addnow.apps.tracker.utils import get_checksum


class UrlStats(ShareStats, ClickStats, ViewStats):
    pass


class UrlBase(BaseStatsModel):
    type_name = 'url'
    stats_class = UrlStats
    data_fields = ['url', 'title', 'checksum']
    index_fields = ['checksum']

    url = URLType(required=True)
    title = StringType(default='')
    checksum = SHA1Type()

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
        return super(UrlBase, self).find(query, *args, **kwargs)

    def find_one(self, query=None, *args, **kwargs):
        self._add_checksum(query)
        return super(UrlBase, self).find_one(query, *args, **kwargs)


class UrlAll(BaseAll, UrlBase):
    pass


class UrlDaily(BaseDaily, UrlBase):
    pass


class UrlMonthly(BaseMonthly, UrlBase):
    pass


class UrlYearly(BaseYearly, UrlBase):
    pass
