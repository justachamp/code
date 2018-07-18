# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.types.base import StringType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.stats.click import ClickStats
from addnow.apps.tracker.models.stats.share import ShareStats
from addnow.apps.tracker.models.stats.view import ViewStats


class CountryStats(ShareStats, ClickStats, ViewStats):
    pass


class CountryBase(BaseStatsModel):
    use_indexes = False
    type_name = 'country'
    stats_class = CountryStats
    data_fields = ['country']

    country = StringType(required=True)


class CountryAll(BaseAll, CountryBase):
    pass


class CountryDaily(BaseDaily, CountryBase):
    pass


class CountryMonthly(BaseMonthly, CountryBase):
    pass


class CountryYearly(BaseYearly, CountryBase):
    pass
