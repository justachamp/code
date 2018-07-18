# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from addnow.apps.tracker.models.stats.base import BaseAll, BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.stats.url import UrlBase
from addnow.apps.tracker.models.stats.source import SourceBase
from addnow.apps.tracker.models.stats.click import ClickStats
from addnow.apps.tracker.models.stats.share import ShareStats


class UrlSourceStats(ShareStats, ClickStats):
    pass


class UrlSourceBase(UrlBase, SourceBase):
    use_indexes = True
    type_name = 'url_source'
    stats_class = UrlSourceStats
    data_fields = SourceBase.data_fields + UrlBase.data_fields
    index_fields = SourceBase.data_fields + UrlBase.index_fields


class UrlSourceAll(BaseAll, UrlSourceBase):
    pass


class UrlSourceDaily(BaseDaily, UrlSourceBase):
    pass


class UrlSourceMonthly(BaseMonthly, UrlSourceBase):
    pass


class UrlSourceYearly(BaseYearly, UrlSourceBase):
    pass
