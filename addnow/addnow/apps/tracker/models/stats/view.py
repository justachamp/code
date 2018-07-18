# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.models import Model
from schematics.types.base import IntType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly


class ViewStats(Model):
    views = IntType(default=0)


class ViewBase(BaseStatsModel):
    use_indexes = False
    type_name = 'view'
    stats_class = ViewStats


class ViewAll(BaseAll, ViewBase):
    pass


class ViewDaily(BaseDaily, ViewBase):
    pass


class ViewMonthly(BaseMonthly, ViewBase):
    pass


class ViewYearly(BaseYearly, ViewBase):
    pass
