# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.types.base import StringType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.stats.copy import CopyStats


class KeywordStats(CopyStats):
    pass


class KeywordBase(BaseStatsModel):
    type_name = 'keyword'
    stats_class = KeywordStats
    data_fields = ['keyword']

    keyword = StringType(required=True)


class KeywordAll(BaseAll, KeywordBase):
    pass


class KeywordDaily(BaseDaily, KeywordBase):
    pass


class KeywordMonthly(BaseMonthly, KeywordBase):
    pass


class KeywordYearly(BaseYearly, KeywordBase):
    pass
