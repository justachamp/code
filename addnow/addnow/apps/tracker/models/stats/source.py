# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.types.base import StringType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.stats.click import ClickStats
from addnow.apps.tracker.models.stats.follow import FollowStats
from addnow.apps.tracker.models.stats.share import ShareStats


class SourceStats(ShareStats, ClickStats, FollowStats):
    pass


class SourceBase(BaseStatsModel):
    use_indexes = False
    type_name = 'source'
    stats_class = SourceStats
    data_fields = ['source']

    source = StringType(required=True)


class SourceAll(BaseAll, SourceBase):
    pass


class SourceDaily(BaseDaily, SourceBase):
    pass


class SourceMonthly(BaseMonthly, SourceBase):
    pass


class SourceYearly(BaseYearly, SourceBase):
    pass
