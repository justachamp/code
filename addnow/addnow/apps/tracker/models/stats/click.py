# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.models import Model
from schematics.types.base import IntType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly


class ClickStats(Model):
    clicks = IntType(default=0)


class ClickBase(BaseStatsModel):
    use_indexes = False
    type_name = 'click'
    stats_class = ClickStats


class ClickAll(BaseAll, ClickBase):
    pass


class ClickDaily(BaseDaily, ClickBase):
    pass


class ClickMonthly(BaseMonthly, ClickBase):
    pass


class ClickYearly(BaseYearly, ClickBase):
    pass
