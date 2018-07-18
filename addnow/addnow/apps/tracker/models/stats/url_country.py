# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from addnow.apps.tracker.models.stats.base import BaseAll, BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.stats.url import UrlBase
from addnow.apps.tracker.models.stats.country import CountryBase
from addnow.apps.tracker.models.stats.click import ClickStats
from addnow.apps.tracker.models.stats.share import ShareStats
from addnow.apps.tracker.models.stats.view import ViewStats


class UrlCountryStats(ShareStats, ClickStats, ViewStats):
    pass


class UrlCountryBase(UrlBase, CountryBase):
    use_indexes = True
    type_name = 'url_country'
    stats_class = UrlCountryStats
    data_fields = CountryBase.data_fields + UrlBase.data_fields
    index_fields = CountryBase.data_fields + UrlBase.index_fields


class UrlCountryAll(BaseAll, UrlCountryBase):
    pass


class UrlCountryDaily(BaseDaily, UrlCountryBase):
    pass


class UrlCountryMonthly(BaseMonthly, UrlCountryBase):
    pass


class UrlCountryYearly(BaseYearly, UrlCountryBase):
    pass
