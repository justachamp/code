# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.models import Model
from schematics.types.base import IntType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly


class ShareStats(Model):
    shares = IntType(default=0)


class ShareBase(BaseStatsModel):
    use_indexes = False
    type_name = 'share'
    stats_class = ShareStats


class ShareAll(BaseAll, ShareBase):
    pass


class ShareDaily(BaseDaily, ShareBase):
    pass


class ShareMonthly(BaseMonthly, ShareBase):
    pass


class ShareYearly(BaseYearly, ShareBase):
    pass
