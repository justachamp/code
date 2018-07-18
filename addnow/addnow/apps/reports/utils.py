# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import calendar
from datetime import timedelta
from itertools import groupby
from operator import itemgetter


class DateRangeSplitter(object):
    period = None

    @classmethod
    def get_first_period(cls, date):
        raise NotImplementedError

    @classmethod
    def get_last_period(cls, date):
        raise NotImplementedError

    @classmethod
    def is_first_period(cls, date):
        for period, value in cls.get_first_period(date).items():
            if getattr(date, period) != value:
                return False
        return True

    @classmethod
    def is_last_period(cls, date):
        for period, value in cls.get_last_period(date).items():
            if getattr(date, period) != value:
                return False
        return True

    @classmethod
    def split(cls, begin_date, end_date):
        date_ranges = []
        cut_left = False

        # cut date range from the left
        if not cls.is_first_period(begin_date):
            begin_date_right = begin_date.replace(**cls.get_last_period(begin_date))
            if begin_date_right < end_date:
                date_ranges.append((begin_date, begin_date_right))
                begin_date = begin_date_right + timedelta(days=1)
                cut_left = True
        # cut date range from the right
        if not cls.is_last_period(end_date):
            end_date_left = end_date.replace(**cls.get_first_period(end_date))
            if end_date_left > begin_date:
                date_ranges.append((end_date_left, end_date))
                end_date = end_date_left - timedelta(days=1)
        # remaining range
        if begin_date < end_date:
            if cut_left:
                date_ranges.insert(1, (begin_date, end_date))
            else:
                date_ranges.insert(0, (begin_date, end_date))

        return date_ranges


class DayRangeSplitter(DateRangeSplitter):
    period = 'day'

    @classmethod
    def get_first_period(cls, date):
        return {'day': 1}

    @classmethod
    def get_last_period(cls, date):
        return {'day': calendar.monthrange(date.year, date.month)[1]}


class MonthRangeSplitter(DateRangeSplitter):
    period = 'month'

    @classmethod
    def get_first_period(cls, date):
        return {'month': 1, 'day': 1}

    @classmethod
    def get_last_period(cls, date):
        return {'month': 12, 'day': 31}


def combine_lists_by_fields(l1, l2, group_fields):
    merged_list = l1 + l2
    all_keys = set([key for item in merged_list for key in item])
    key_func = itemgetter(*group_fields)
    result = []

    for key, grouper in groupby(sorted(merged_list, key=key_func), key_func):
        result_item = {}
        for item in grouper:
            result_item.update(item)
        skipped_keys = {key: 0 for key in all_keys if key not in result_item}
        result_item.update(skipped_keys)
        result.append(result_item)

    return result
