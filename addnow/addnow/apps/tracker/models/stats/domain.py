# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from schematics.types.base import StringType

from addnow.apps.tracker.models.stats.base import BaseStatsModel, BaseAll, BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.stats.click import ClickStats
from addnow.apps.tracker.models.stats.view import ViewStats


class DomainStats(ClickStats, ViewStats):
    pass


class DomainBase(BaseStatsModel):
    use_indexes = False
    type_name = 'domain'
    stats_class = DomainStats
    data_fields = ['domain']

    domain = StringType(default='')


class DomainAll(BaseAll, DomainBase):
    pass


class DomainDaily(BaseDaily, DomainBase):
    pass


class DomainMonthly(BaseMonthly, DomainBase):
    pass


class DomainYearly(BaseYearly, DomainBase):
    pass
