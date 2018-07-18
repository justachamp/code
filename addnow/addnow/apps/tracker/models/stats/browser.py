# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.types.base import StringType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.stats.click import ClickStats
from addnow.apps.tracker.models.stats.share import ShareStats
from addnow.apps.tracker.models.stats.view import ViewStats


class BrowserStats(ShareStats, ClickStats, ViewStats):
    pass


class BrowserBase(BaseStatsModel):
    type_name = 'browser'
    stats_class = BrowserStats
    data_fields = ['browser']

    browser = StringType(required=True)


class BrowserAll(BaseAll, BrowserBase):
    pass


class BrowserDaily(BaseDaily, BrowserBase):
    pass


class BrowserMonthly(BaseMonthly, BrowserBase):
    pass


class BrowserYearly(BaseYearly, BrowserBase):
    pass
