# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.models import Model
from schematics.types.base import IntType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly


class CopyStats(Model):
    copies = IntType(default=0)


class CopyBase(BaseStatsModel):
    use_indexes = False
    type_name = 'copy'
    stats_class = CopyStats


class CopyAll(BaseAll, CopyBase):
    pass


class CopyDaily(BaseDaily, CopyBase):
    pass


class CopyMonthly(BaseMonthly, CopyBase):
    pass


class CopyYearly(BaseYearly, CopyBase):
    pass
