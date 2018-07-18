from datetime import datetime

from django.test import TestCase

from addnow.apps.reports.utils import DayRangeSplitter, MonthRangeSplitter


class TestDayRangeSplitter(TestCase):
    def test__split_within_one_month(self):
        date_ranges = DayRangeSplitter.split(datetime(2015, 12, 3), datetime(2015, 12, 15))
        self.assertEqual(date_ranges, [
            (datetime(2015, 12, 3), datetime(2015, 12, 15))
        ])

    def test__split_entire_month(self):
        date_ranges = DayRangeSplitter.split(datetime(2015, 12, 1), datetime(2015, 12, 31))
        self.assertEqual(date_ranges, [
            (datetime(2015, 12, 1), datetime(2015, 12, 31))
        ])

    def test__split_cut_left(self):
        date_ranges = DayRangeSplitter.split(datetime(2015, 9, 15), datetime(2015, 11, 30))
        self.assertEqual(date_ranges, [
            (datetime(2015, 9, 15), datetime(2015, 9, 30)),
            (datetime(2015, 10, 1), datetime(2015, 11, 30))
        ])

    def test__split_cut_right(self):
        date_ranges = DayRangeSplitter.split(datetime(2015, 10, 1), datetime(2015, 12, 15))
        self.assertEqual(date_ranges, [
            (datetime(2015, 10, 1), datetime(2015, 11, 30)),
            (datetime(2015, 12, 1), datetime(2015, 12, 15))
        ])

    def test__split_cut_left_and_right(self):
        date_ranges = DayRangeSplitter.split(datetime(2015, 9, 15), datetime(2015, 12, 15))
        self.assertEqual(date_ranges, [
            (datetime(2015, 9, 15), datetime(2015, 9, 30)),
            (datetime(2015, 10, 1), datetime(2015, 11, 30)),
            (datetime(2015, 12, 1), datetime(2015, 12, 15))
        ])

    def test__is_first_period(self):
        self.assertTrue(DayRangeSplitter.is_first_period(datetime(2015, 10, 1)))
        self.assertFalse(DayRangeSplitter.is_first_period(datetime(2015, 10, 15)))

    def test__is_last_period(self):
        self.assertTrue(DayRangeSplitter.is_last_period(datetime(2015, 10, 31)))
        self.assertFalse(DayRangeSplitter.is_last_period(datetime(2015, 10, 15)))


class TestMonthRangeSplitter(TestCase):
    def test__split_within_one_year(self):
        date_ranges = MonthRangeSplitter.split(datetime(2015, 10, 1), datetime(2015, 12, 31))
        self.assertEqual(date_ranges, [
            (datetime(2015, 10, 1), datetime(2015, 12, 31))
        ])

    def test__split_entire_year(self):
        date_ranges = MonthRangeSplitter.split(datetime(2015, 1, 1), datetime(2015, 12, 31))
        self.assertEqual(date_ranges, [
            (datetime(2015, 1, 1), datetime(2015, 12, 31))
        ])

    def test__split_cut_left(self):
        date_ranges = MonthRangeSplitter.split(datetime(2014, 9, 1), datetime(2015, 12, 31))
        self.assertEqual(date_ranges, [
            (datetime(2014, 9, 1), datetime(2014, 12, 31)),
            (datetime(2015, 1, 1), datetime(2015, 12, 31))
        ])

    def test__split_cut_right(self):
        date_ranges = MonthRangeSplitter.split(datetime(2015, 1, 1), datetime(2016, 3, 31))
        self.assertEqual(date_ranges, [
            (datetime(2015, 1, 1), datetime(2015, 12, 31)),
            (datetime(2016, 1, 1), datetime(2016, 3, 31))
        ])

    def test__split_cut_left_and_right(self):
        date_ranges = MonthRangeSplitter.split(datetime(2014, 9, 1), datetime(2016, 3, 31))
        self.assertEqual(date_ranges, [
            (datetime(2014, 9, 1), datetime(2014, 12, 31)),
            (datetime(2015, 1, 1), datetime(2015, 12, 31)),
            (datetime(2016, 1, 1), datetime(2016, 3, 31))
        ])

    def test__is_first_period(self):
        self.assertTrue(MonthRangeSplitter.is_first_period(datetime(2015, 1, 1)))
        self.assertFalse(MonthRangeSplitter.is_first_period(datetime(2015, 1, 15)))
        self.assertFalse(MonthRangeSplitter.is_first_period(datetime(2015, 2, 1)))

    def test__is_last_period(self):
        self.assertTrue(MonthRangeSplitter.is_last_period(datetime(2015, 12, 31)))
        self.assertFalse(MonthRangeSplitter.is_last_period(datetime(2015, 12, 15)))
        self.assertFalse(MonthRangeSplitter.is_last_period(datetime(2015, 10, 31)))
