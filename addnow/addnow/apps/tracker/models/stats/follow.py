# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.models import Model
from schematics.types.base import IntType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly


class FollowStats(Model):
    follows = IntType(default=0)


class FollowBase(BaseStatsModel):
    use_indexes = False
    type_name = 'follow'
    stats_class = FollowStats


class FollowAll(BaseAll, FollowBase):
    pass


class FollowDaily(BaseDaily, FollowBase):
    pass


class FollowMonthly(BaseMonthly, FollowBase):
    pass


class FollowYearly(BaseYearly, FollowBase):
    pass
