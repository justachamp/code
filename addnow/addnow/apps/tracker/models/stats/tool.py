# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.types.base import StringType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.stats.click import ClickStats
from addnow.apps.tracker.models.stats.share import ShareStats


class ToolStats(ShareStats, ClickStats):
    pass


class ToolBase(BaseStatsModel):
    type_name = 'tool'
    stats_class = ToolStats
    data_fields = ['tool']

    tool = StringType(required=True)


class ToolAll(BaseAll, ToolBase):
    pass


class ToolDaily(BaseDaily, ToolBase):
    pass


class ToolMonthly(BaseMonthly, ToolBase):
    pass


class ToolYearly(BaseYearly, ToolBase):
    pass
