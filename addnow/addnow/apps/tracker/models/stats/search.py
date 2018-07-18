# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.types.base import StringType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.stats.click import ClickStats


class SearchStats(ClickStats):
    pass


class SearchBase(BaseStatsModel):
    type_name = 'search'
    stats_class = SearchStats
    data_fields = ['search_engine', 'search_term']

    search_engine = StringType(default='')
    search_term = StringType(default='')


class SearchAll(BaseAll, SearchBase):
    pass


class SearchDaily(BaseDaily, SearchBase):
    pass


class SearchMonthly(BaseMonthly, SearchBase):
    pass


class SearchYearly(BaseYearly, SearchBase):
    pass
