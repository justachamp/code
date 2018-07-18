# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from addnow.apps.tracker.models.stats.base import BaseAll, BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.stats.domain import DomainStats, DomainBase
from addnow.apps.tracker.models.stats.url import UrlBase


class DomainUrlStats(DomainStats):
    pass


class DomainUrlBase(DomainBase, UrlBase):
    use_indexes = True
    type_name = 'domain_url'
    stats_class = DomainUrlStats
    data_fields = DomainBase.data_fields + UrlBase.data_fields
    index_fields = DomainBase.data_fields + UrlBase.index_fields


class DomainUrlAll(BaseAll, DomainUrlBase):
    pass


class DomainUrlDaily(BaseDaily, DomainUrlBase):
    pass


class DomainUrlMonthly(BaseMonthly, DomainUrlBase):
    pass


class DomainUrlYearly(BaseYearly, DomainUrlBase):
    pass
