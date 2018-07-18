from datetime import datetime

from addnow.apps.tracker.models.stats.base import BaseDaily, BaseMonthly, BaseYearly
from addnow.apps.tracker.models.reports import ALL_REPORTS, ALL_DIMENSIONS
from addnow.apps.tracker.tests.base import MongoTestCase


SUMMARY_EVENTS = ['shares', 'clicks', 'views', 'follows', 'copies']


class TestModels(MongoTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestModels, cls).setUpClass()
        cls.date_ranges = [
            {
                'base_model': BaseDaily,
                'date_range': [datetime(2015, 1, i) for i in range(1, 32)],
                'begin_date': datetime(2015, 1, 1),
                'end_date': datetime(2015, 1, 10),
            },
            {
                'base_model': BaseMonthly,
                'date_range': [datetime(2015, i, 1) for i in range(1, 13)],
                'begin_date': datetime(2015, 1, 1),
                'end_date': datetime(2015, 10, 1),
            },
            {
                'base_model': BaseYearly,
                'date_range': [datetime(i, 1, 1) for i in range(2015, 2026)],
                'begin_date': datetime(2015, 1, 1),
                'end_date': datetime(2024, 1, 1),
            }
        ]
        cls.date_ranges_with_values_granularity = [
            {
                'base_model': BaseDaily,
                'date_range': [datetime(2015, 1, 1, hour=i) for i in range(0, 24)],
                'begin_date': datetime(2015, 1, 1),
                'end_date': datetime(2015, 1, 1),
            },
            {
                'base_model': BaseMonthly,
                'date_range': [datetime(2015, 1, i) for i in range(1, 32)],
                'begin_date': datetime(2015, 1, 1),
                'end_date': datetime(2015, 1, 31),
            },
            {
                'base_model': BaseYearly,
                'date_range': [datetime(2015, i, 1) for i in range(1, 13)],
                'begin_date': datetime(2015, 1, 1),
                'end_date': datetime(2024, 12, 1),
            },
        ]

    def setUp(self):
        super(TestModels, self).setUp()
        self.data = dict(
            site=1,
            browser='Firefox',
            country='RU',
            domain='example.com',
            url='http://example.com/test',
            title='page title',
            keyword='keyword',
            search_engine='Google',
            search_term='term',
            source='facebook',
            tool='sharing-buttons',
            date=datetime(2015, 1, 31, hour=1)
        )

    def inc_all_counters(self, date_range, inc_value):
        for report_class in ALL_REPORTS:
            for dimension in report_class.dimensions:
                for model_class in dimension.models:
                    for date in date_range:
                        self.data['date'] = date
                        model_class().inc_counter(report_class.event, value=inc_value, **self.data)

    def _test_inc_counter(self, model_class, event, inc_value=1, expected_value=1):
        model_instance = model_class()
        model_instance.inc_counter(event, value=inc_value, **self.data)
        site = self.data['site']
        date = self.data['date']
        model_events = set(model_class.get_events())

        doc = model_instance.find_one({'site': site})
        totals = doc['totals']
        self.assertEqual(model_events, set(totals.keys()))
        self.assertEqual(totals[event], expected_value)

        # check data fields
        self.assertEqual(doc['type'], model_class.type_name)
        for data_field_name in model_instance.data_fields:
            if data_field_name in self.data:
                self.assertEqual(doc[data_field_name], self.data[data_field_name])

        # check that other totals are equal to zero
        del totals[event]
        for value in totals.values():
            self.assertEqual(value, 0)

        if model_instance.has_granularity:
            granularity_range = model_instance.granularity_range(date)
            granularity_name = model_instance.granularity_name
            granularity_value = getattr(date, granularity_name)
            expected_date = model_instance.get_min_date(date)

            self.assertEqual(doc['date'], expected_date)
            values = doc['values']
            for i, item in zip(range(*granularity_range), values):
                events = set(key for key in item.keys() if key != granularity_name)
                self.assertEqual(model_events, events)
                if i == granularity_value:
                    self.assertEqual(item[granularity_name], granularity_value)
                    self.assertEqual(item[event], expected_value)
                    del item[event]
                # all other values are equal to zero
                del item[granularity_name]
                for value in item.values():
                    self.assertEqual(value, 0)

    def test__inc_counter(self):
        for report_class in ALL_REPORTS:
            for dimension in report_class.dimensions:
                for model_class in dimension.models:
                    self._test_inc_counter(model_class, report_class.event, 1, 1)
                    self._test_inc_counter(model_class, report_class.event, 10, 11)
                self.drop_collections()

    def test__get_totals_empty(self):
        begin_date = datetime(2015, 1, 1)
        end_date = datetime(2015, 1, 2)

        for dimension in ALL_DIMENSIONS.values():
            for model_class in dimension.models:
                totals = model_class().get_totals(self.data['site'], begin_date, end_date)
                self.assertEqual(totals, [])

    def _test_get_totals(self, base_model, begin_date, end_date, expected_value, aggregate_by_values=False):
        for dimension in ALL_DIMENSIONS.values():
            for model_class in dimension.models:
                model_instance = model_class()
                if isinstance(model_instance, base_model):
                    events = model_instance.get_events()
                    totals = model_instance.get_totals(self.data['site'], begin_date, end_date,
                                                       events=events, aggregate_by_values=aggregate_by_values)[0]
                    for data_field_name in model_instance.data_fields:
                        if data_field_name in self.data:
                            self.assertEqual(totals[data_field_name], self.data[data_field_name])
                    for event in events:
                        self.assertEqual(totals[event], expected_value)

    def test__get_totals(self):
        inc_value = 10
        expected_value = 100

        for item in self.date_ranges:
            self.inc_all_counters(item['date_range'], inc_value)
            self._test_get_totals(item['base_model'], item['begin_date'], item['end_date'], expected_value)
            self.drop_collections()

    def test__get_totals_aggregate_by_values(self):
        inc_value = 10
        expected_values = [240, 310, 120]

        for item, expected_value in zip(self.date_ranges_with_values_granularity, expected_values):
            self.inc_all_counters(item['date_range'], inc_value)
            self._test_get_totals(item['base_model'], item['begin_date'], item['end_date'], expected_value,
                                  aggregate_by_values=True)
            self.drop_collections()

    def test__get_events_summary_empty(self):
        models = [BaseDaily, BaseMonthly, BaseYearly]
        begin_date = datetime(2015, 1, 1)
        end_date = datetime(2015, 1, 2)

        for model in models:
            events_summary = model().get_events_summary(self.data['site'], begin_date, end_date, SUMMARY_EVENTS)
            self.assertEqual(events_summary, [])

    def _test_get_events_summary(self, base_model, begin_date, end_date, date_range, events, expected_value):
        events_summary = base_model().get_events_summary(self.data['site'], begin_date, end_date, events)

        for item, date in zip(events_summary, date_range):
            self.assertEqual(item['date'], date)
            for event in events:
                self.assertEqual(item[event], expected_value)

    def test__get_events_summary(self):
        inc_value = 10
        expected_value = 10

        for item in self.date_ranges:
            date_range = item['date_range']
            selected_date_range = date_range[:10]
            self.inc_all_counters(date_range, inc_value)
            self._test_get_events_summary(item['base_model'], item['begin_date'], item['end_date'],
                                          selected_date_range, SUMMARY_EVENTS, expected_value)
            self.drop_collections()

    def _test_get_events_summary_aggregate_by_values(self, base_model, begin_date, end_date, events, expected_value):
        model_instance = base_model()
        granularity_range = range(*model_instance.granularity_range(begin_date))
        events_summary = model_instance.get_events_summary(self.data['site'], begin_date, end_date, events,
                                                           aggregate_by_values=True)

        for i, item in enumerate(events_summary):
            self.assertNotIn(model_instance.granularity_name, item)
            expected_date = model_instance.get_min_date(begin_date).replace(
                **{model_instance.granularity_name: granularity_range[i]})
            self.assertEqual(item['date'], expected_date)
            for event in events:
                self.assertEqual(item[event], expected_value)

    def test__get_events_summary_aggregate_by_values(self):
        inc_value = 10
        expected_value = 10

        for item in self.date_ranges_with_values_granularity:
            date_range = item['date_range']
            self.inc_all_counters(date_range, inc_value)
            self._test_get_events_summary_aggregate_by_values(
                item['base_model'], item['begin_date'], item['end_date'],
                SUMMARY_EVENTS, expected_value
            )
            self.drop_collections()

    def test__get_report_empty(self):
        site_id = self.data['site']
        models = [BaseDaily, BaseMonthly, BaseYearly]
        begin_date = datetime(2015, 1, 1)
        end_date = datetime(2015, 1, 2)
        all_dimensions = ALL_DIMENSIONS.keys()

        for model in models:
            report_data = model().get_report(site_id, begin_date, end_date, SUMMARY_EVENTS, all_dimensions)
            self.assertEqual(report_data, [])
            report_data = model().get_report(site_id, begin_date, end_date, SUMMARY_EVENTS, all_dimensions,
                                             summary=True)
            self.assertEqual(report_data, [])
            report_data = model().get_report(site_id, begin_date, end_date, SUMMARY_EVENTS, all_dimensions,
                                             aggregate_by_values=True)
            self.assertEqual(report_data, [])

    def _test_get_report(self, base_model, begin_date, end_date, date_range, events, dimensions, expected_value,
                         summary):
        report_data = base_model().get_report(self.data['site'], begin_date, end_date, events, dimensions,
                                              summary=summary)
        report_dimensions = set()

        for i, item in enumerate(report_data):
            dimension_name = item['dimension']
            dimension_class = ALL_DIMENSIONS[dimension_name]
            report_dimensions.add(dimension_name)
            dimension_events = dimension_class.get_events()

            self.assertEqual(item['date'], date_range[i / len(dimensions)])
            self.assertIn(dimension_name, dimensions)
            if not summary:
                for data_field_name in dimension_class.get_data_fields():
                    if data_field_name in self.data:
                        self.assertEqual(item[data_field_name], self.data[data_field_name])
            for event in events:
                if event in dimension_events:
                    self.assertEqual(item[event], expected_value)
                else:
                    self.assertEqual(item[event], 0)
        self.assertEqual(report_dimensions, set(dimensions))

    def test__get_report(self):
        inc_value = 10
        expected_value = 10

        for item in self.date_ranges:
            date_range = item['date_range']
            selected_date_range = date_range[:10]
            self.inc_all_counters(date_range, inc_value)
            self._test_get_report(item['base_model'], item['begin_date'], item['end_date'], selected_date_range,
                                  SUMMARY_EVENTS, ALL_DIMENSIONS.keys(), expected_value, summary=False)
            self._test_get_report(item['base_model'], item['begin_date'], item['end_date'], selected_date_range,
                                  SUMMARY_EVENTS, ALL_DIMENSIONS.keys(), expected_value, summary=True)
            self.drop_collections()

    def _test_get_report_aggregate_by_values(self, base_model, begin_date, end_date, events, dimensions,
                                             expected_value, summary):
        model_instance = base_model()
        granularity_range = range(*model_instance.granularity_range(begin_date))
        report_data = model_instance.get_report(self.data['site'], begin_date, end_date, events, dimensions,
                                                summary=summary, aggregate_by_values=True)
        report_dimensions = set()

        for i, item in enumerate(report_data):
            dimension_name = item['dimension']
            dimension_class = ALL_DIMENSIONS[dimension_name]
            report_dimensions.add(dimension_name)
            dimension_events = dimension_class.get_events()
            expected_date = model_instance.get_min_date(begin_date).replace(
                **{model_instance.granularity_name: granularity_range[i / len(dimensions)]})

            self.assertNotIn(model_instance.granularity_name, item)
            self.assertEqual(item['date'], expected_date)
            self.assertIn(dimension_name, dimensions)
            if not summary:
                for data_field_name in dimension_class.get_data_fields():
                    if data_field_name in self.data:
                        self.assertEqual(item[data_field_name], self.data[data_field_name])
            for event in events:
                if event in dimension_events:
                    self.assertEqual(item[event], expected_value)
                else:
                    self.assertEqual(item[event], 0)
        self.assertEqual(report_dimensions, set(dimensions))

    def test__get_report_aggregate_by_values(self):
        inc_value = 10
        expected_value = 10

        for item in self.date_ranges_with_values_granularity:
            date_range = item['date_range']
            self.inc_all_counters(date_range, inc_value)
            self._test_get_report_aggregate_by_values(
                item['base_model'], item['begin_date'], item['end_date'],
                SUMMARY_EVENTS, ALL_DIMENSIONS.keys(), expected_value, summary=False
            )
            self._test_get_report_aggregate_by_values(
                item['base_model'], item['begin_date'], item['end_date'],
                SUMMARY_EVENTS, ALL_DIMENSIONS.keys(), expected_value, summary=True
            )
            self.drop_collections()
