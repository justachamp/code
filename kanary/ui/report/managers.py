'''
Those managers are used for report querying.

See:
    ui/report/reference.rst
'''
from datetime import timedelta

from django.db import connection
from django.db.models import Manager
from django.db.utils import DatabaseError

from etc.constants import METRICS, BASE_METRICS, CALCULATE_METRICS


def quoted(literal_value):
    '''
    Convert literal_value to a string and return a string containing its SQL string literal.

    :param object literal_value: any object with __str__ that produces valid SQL string literal
        that will be wrapped in apostrophes.
    '''
    return "'%s'" % literal_value


def parenthesized(expr):
    '''
    Wrap SQL expression in parentheses if the expression is not an empty string.
    Guarantees proprer expression precedence.

    :param str expr: SQL expression or empty string
    '''
    return '(%s)' % expr if expr else ''


def nullable_in_expr(col_name, in_list):
    '''
    Build a SQL expression that will match each row where the value of `col_name` column
    matches one of the values in in_list.
    SQL uses ternary logic so we cannot just do `WHERE object IN (322, 543, null)`.
    We have to issue `OR object IS NULL` to include nulls.

    :param str col_name: column that the expression will be built for
    :param (list, tuple) in_list: list of values (str, unicode or NoneType) to filter for
    :return: parenthesized SQL expression to put in WHERE clause or empty string
    :rtype str:

    >>> nullable_in_expr('col', [])
    ''
    >>> nullable_in_expr('col', ['a'])
    "(col IN ('a'))"
    >>> nullable_in_expr('col', ['a', None])
    "(col IS NULL OR col IN ('a')"
    >>> nullable_in_expr('col', ['a', None, 'b'])
    "(col IS NULL OR col IN ('a', 'b'))"
    '''

    include_nulls_expr = ''
    if None in in_list:
        in_list.remove(None)
        include_nulls_expr = '{col_name} IS NULL'.format(col_name=col_name)

    in_list_expr = ''
    if in_list:
        in_list_expr = '{col_name} IN ({reported_related_ids})'.format(
            col_name=col_name,
            reported_related_ids=', '.join([quoted(i) for i in in_list]),
        )

    return parenthesized(
        ' OR '.join(filter(bool, [include_nulls_expr, in_list_expr]))
    )


class BaseReportManager(Manager):

    single_series_identifier = None
    """ Column name used to determine chart series / table rows. """
    report_base_identifier = None
    """
    Column names used to determine identity of chart series when single_series_identifier
    is in fact m2m.
    """

    def run_sql(self, sql_query):
        '''
        Runs sql given as a string.

        :rtype: list
        :return: list of dicts mapping columns names to row elements values,
            e.g.:
                [
                    {'id': 1, 'name': 'Bob'},
                    {'id': 2, 'name': 'Rob'},
                ]

        .. warning::
            All provided clauses must be already safe and clean from SQL
            injections!
        '''
        cursor = connection.cursor()

        def dictfetchall(cursor):
            ''' Returns all rows from a cursor as a dict. '''
            desc = cursor.description
            return [
                dict(zip([col[0] for col in desc], row))
                for row in cursor.fetchall()
            ]

        try:
            cursor.execute(sql_query)
        except DatabaseError as err:
            # Pass full issued SQL.
            raise DatabaseError(
                'Custom SQL failed:\n%s\nOriginal exception:%r' %
                (sql_query, err))

        return dictfetchall(cursor)

    @property
    def table(self):
        return self.model._meta.db_table

    @property
    def related_table(self):
        return self.model.related.field.related.parent_model._meta.db_table

    def metrics(self):
        return ', '.join(
            [v + ' AS ' + k for k, v in CALCULATE_METRICS.items()] +
            ['SUM({0}) AS {0}'.format(k) for k in METRICS.keys()
             if k not in CALCULATE_METRICS.keys()])

    def date_truncate(self, start_date, end_date):
        '''
        Returns date truncate type for given date range.
        '''
        delta = end_date - start_date
        if delta <= timedelta(days=2):
            return 'minute'  # max 4 * 24 * 2 periods
        if delta <= timedelta(days=7):
            return 'hour'  # max 7 * 24 periods
        elif delta <= timedelta(days=40):
            return 'day'  # max 40 periods
        elif delta <= timedelta(days=5 * 30):
            return 'week'  # ~max 5 * 4 periods
        elif delta <= timedelta(days=10 * 365):
            return 'month'  # ~max 12 * 10 periods
        return 'year'

    def daterange_filter(self, start_date=None, end_date=None):
        '''
        Basic date filtering clause for SQL. (Use it in 'WHERE'.)

        :param datetime start_date:
        :param datetime end_date:

        :rtype: string
        :return: date range filter for WHERE claus
        '''
        clauses = []

        if start_date is not None:
            clauses.append("r.time::date >= '%s'" % start_date.strftime('%Y-%m-%d'))
        if end_date is not None:
            end_date += timedelta(days=1)
            clauses.append("r.time::date < '%s'" % end_date.strftime('%Y-%m-%d'))

        if not clauses:
            return '1 = 1'

        return ' AND '.join(clauses)

    def get_sorting_command(self, sort_by):
        '''
        Getting proper SQL code for ordering.

        :param str sort_by: value provided by request.GET eg. clk, ~imp
        :rtype string
        :returns SQL code for ordering

        .. note::

            Param starting with '~' is in a descending order.
        '''
        if not sort_by:
            raise ValueError('no sort column specified')

        desc = False
        if sort_by.startswith('~'):
            desc = True
            sort_by = sort_by[1:]

        if sort_by not in METRICS.keys():
            raise ValueError('no such metric %s' % sort_by)

        return '{metric}{method}'.format(
            metric=sort_by,
            method=' DESC' if desc else ''
        )

    def limit(self, limit):
        '''
        Returns LIMIT value.
        '''
        return str(limit) if limit else 'ALL'

    def metric_expr(self, metric):
        if metric in CALCULATE_METRICS:
            return CALCULATE_METRICS[metric]
        elif metric in BASE_METRICS:
            return 'sum(%s)' % metric
        raise ValueError('Metric %r not allowed for user query.' % metric)

    def _report_chart_where(self, report_base_obj, reported_related_ids, start_date, end_date):
        '''
        Build WHERE clause for reports. See `report_chart` docstring.

        We need this method to have a little less redundancy between the two report_chart methods.
        '''

        where = []

        if reported_related_ids:
            where.append(
                nullable_in_expr(col_name=self.single_series_identifier, in_list=reported_related_ids)
            )

        if self.report_base_identifier is not None:
            where.append("{base_id_field} = '{base_id}'".format(
                base_id_field=self.report_base_identifier, base_id=report_base_obj.id_random))

        report_identity_expr = parenthesized(' AND '.join(where))
        return parenthesized(
            '{report_identity_expr} AND {daterange}'.format(
                report_identity_expr=report_identity_expr,
                daterange=self.daterange_filter(start_date, end_date)
            )
        )

    def report_chart(self, report_base_obj, reported_related_ids, metric, start_date, end_date):
        '''
        Issue report SQL for single-metric multiple-related-objects chart.

        :param (Strategy, Campaign) report_base_obj: instance of reportable object which page we are on
        :param list reported_related_ids: list of unique strings determining identity of related objects
        :param str metric: legal metric to query (one of CALCULATE_METRICS and BASE_METRICS)
        :param datetime start_date: date to start report on. Results will begin
            on datetime truncated to calculated date_truncate.
        :param datetime end_date: date to end report on. Will be truncated
            the same way as start_date.

        :return list: list of dicts, like:
            [
                # timestamp                 related_id
                {'dt': datetime('sth sth'), '1': 33},
                {'dt': datetime('sth sth'), '0': 1233},
                {'dt': datetime('sth sth'), '0': 123},
                {'dt': datetime('sth sth'), '1': 2},
            ]

        .. note::
            The density of returned data depends on density of actual metrics
            and date range (high values mean bigger grains).
            No zeros will be returned at the beginning and at the end of the
            series.
        '''
        if len(reported_related_ids) == 0:
            return {}

        report_where_expr = self._report_chart_where(report_base_obj, reported_related_ids, start_date, end_date)
        sql = """
            SELECT {metric_expr} AS v, {object_id} AS object_id, date_trunc('{date_trunc}', time) AS dt
            FROM {table} AS r
                WHERE {where}
            GROUP BY dt, object_id
        """.format(
            metric_expr=self.metric_expr(metric),
            date_trunc=self.date_truncate(start_date, end_date),
            table=self.model._meta.db_table,
            where=report_where_expr,
            object_id=self.single_series_identifier,
        )
        return self.run_sql(sql)


class ReportCampaignManager(BaseReportManager):

    single_series_identifier = 'related_id'
    report_base_identifier = None

    def report_overview(self, reported):
        '''
        Query overview row.

        :param Model reported: strategy or campaign instance
        :return: overview dict
        '''
        sql = """
        SELECT {metrics} FROM {table} AS r
            INNER JOIN {related_table} AS t ON t.id_random = r.related_id WHERE t.id = {item_id}
        """.format(
            metrics=self.metrics(),
            table=self.table,
            related_table=self.related_table,
            item_id=reported.pk,
        )
        return self.run_sql(sql)[0]


class ReportStrategyManager(ReportCampaignManager):

    def report_table(self, related_obj, sort_by='~imp', start_date=None, end_date=None, limit=None):
        '''
        Issue query for tabular report.
        '''
        sql = """
            SELECT s.name AS label, {object_id} AS object_id, {metrics}
                FROM {table} AS r
                INNER JOIN campaign_strategy AS s ON s.id_random = r.related_id
                WHERE s.campaign_id = {related_id} AND {daterange} GROUP BY object_id, label ORDER BY {sort_by}
                LIMIT {limit}
        """.format(
            metrics=self.metrics(),
            table=self.table,
            related_id=related_obj.pk,
            object_id=self.single_series_identifier,
            daterange=self.daterange_filter(start_date, end_date),
            sort_by=self.get_sorting_command(sort_by),
            limit=self.limit(limit),
        )
        return self.run_sql(sql)


class ReportAdvertManager(BaseReportManager):

    single_series_identifier = 'related_id'
    report_base_identifier = None

    def report_table(self, related_obj, sort_by='~imp', start_date=None, end_date=None, limit=None):
        sql = """
            SELECT c.name AS label, r.related_id AS object_id, {metrics}
                FROM {table} AS r
                INNER JOIN campaign_advert AS a ON a.id_random = r.related_id
                INNER JOIN storage_creative AS c ON c.id = a.creative_id
                WHERE a.strategy_id = {related_id} AND {daterange} GROUP BY related_id, label ORDER BY {sort_by}
                LIMIT {limit}
        """.format(
            metrics=self.metrics(),
            table=self.model._meta.db_table,
            related_id=related_obj.pk,
            daterange=self.daterange_filter(start_date, end_date),
            sort_by=self.get_sorting_command(sort_by),
            limit=self.limit(limit),
        )
        return self.run_sql(sql)


class ReportTargetValueManager(BaseReportManager):

    single_series_identifier = 'dimension_id'
    report_base_identifier = 'related_id'

    def report_table(self, related_obj, sort_by='~imp', start_date=None, end_date=None, limit=None):
        sql = """
            SELECT (CASE WHEN t1.representant_id IS NULL THEN t1.value ELSE t2.value END) AS label, * FROM
                (SELECT r.dimension_id AS object_id, {metrics} FROM {table} AS r
                 WHERE related_id = {related_id} AND {daterange} GROUP BY object_id ORDER BY {sort_by}
                 LIMIT {limit}) AS s
            LEFT JOIN targeting_targetvalue AS t1 ON object_id = t1.id
            LEFT OUTER JOIN targeting_targetvalue AS t2 ON t2.id = t1.representant_id
        """.format(
            metrics=self.metrics(),
            table=self.table,
            related_id=quoted(related_obj.id_random),
            daterange=self.daterange_filter(start_date, end_date),
            sort_by=self.get_sorting_command(sort_by),
            limit=self.limit(limit),
        )
        return self.run_sql(sql)


class ReportSiteManager(BaseReportManager):

    single_series_identifier = 'dimension'
    report_base_identifier = 'related_id'

    def report_table(self, related_obj, sort_by='~imp', start_date=None, end_date=None, limit=None):
        sql = """
            SELECT r.dimension AS label, r.dimension AS object_id, {metrics} FROM {table} AS r
                WHERE related_id = {related_id} AND {daterange} GROUP BY object_id ORDER BY {sort_by}
                LIMIT {limit}
        """.format(
            metrics=self.metrics(),
            table=self.table,
            related_id=quoted(related_obj.id_random),
            daterange=self.daterange_filter(start_date, end_date),
            sort_by=self.get_sorting_command(sort_by),
            limit=self.limit(limit),
        )
        return self.run_sql(sql)


class ReportCategoryManager(BaseReportManager):

    single_series_identifier = 'cc.id'
    report_base_identifier = 'related_id'

    def report_table(self, related_obj, sort_by='~imp', start_date=None, end_date=None, limit=None):
        sql = """
            SELECT cc.name AS label, {object_id} AS object_id, {metrics}
                FROM {table} AS r
                INNER JOIN {related_table} AS c ON c.id_random = r.related_id
                LEFT JOIN targeting_contentcategoryvalue AS ccv ON r.dimension_id = ccv.id
                LEFT JOIN targeting_contentcategory AS cc ON ccv.representant_id = cc.id
                WHERE c.id = {related_id} AND {daterange} GROUP BY object_id, label ORDER BY {sort_by}
                LIMIT {limit}
        """.format(
            metrics=self.metrics(),
            table=self.table,
            related_table=self.related_table,
            related_id=related_obj.pk,
            object_id=self.single_series_identifier,
            daterange=self.daterange_filter(start_date, end_date),
            sort_by=self.get_sorting_command(sort_by),
            limit=self.limit(limit),
        )
        return self.run_sql(sql)

    def report_chart(self, report_base_obj, reported_related_ids, metric, start_date, end_date):
        if len(reported_related_ids) == 0:
            return {}

        report_where_expr = self._report_chart_where(report_base_obj, reported_related_ids, start_date, end_date)
        sql = """
            SELECT {metric_expr} AS v, {object_id} AS object_id, date_trunc('{date_trunc}', time) AS dt
            FROM {table} AS r
                INNER JOIN {related_table} AS c ON c.id_random = r.related_id
                LEFT JOIN targeting_contentcategoryvalue AS ccv ON r.dimension_id = ccv.id
                LEFT JOIN targeting_contentcategory AS cc ON ccv.representant_id = cc.id
                WHERE {where}
            GROUP BY dt, object_id
        """.format(
            metric_expr=self.metric_expr(metric),
            date_trunc=self.date_truncate(start_date, end_date),
            table=self.model._meta.db_table,
            related_table=self.related_table,
            where=report_where_expr,
            object_id=self.single_series_identifier,
        )
        return self.run_sql(sql)


class ReportDataProviderManager(ReportTargetValueManager):

    label_map = {
        'targeting_segmentproximicmaturityrating': 't.description',
        'targeting_segmentproximicsafetylevel': 't.name',
        'targeting_segmentproximicpagequality': 't.name',
        'targeting_segmentproximicpagenoticeability': """
            (CASE WHEN t.parent_id IS NULL THEN t.name ELSE
                (SELECT name FROM targeting_segmentproximicpagenoticeability WHERE id=t.parent_id) || ' ' || t.name END)
            """,
        'targeting_segmentproximicpageplacement': """
            (CASE WHEN t.parent_id IS NULL THEN t.name ELSE
                (SELECT name FROM targeting_segmentproximicpageplacement WHERE id=t.parent_id) || ' ' || t.name END)
            """,
        'targeting_segmentproximiccontextual': """
            (CASE WHEN t.parent_id IS NULL THEN t.name ELSE
                (SELECT name FROM targeting_segmentproximiccontextual WHERE id=t.parent_id) || ' > ' || t.name END)
            """,
        'targeting_segmentproximicpagelanguage': 't.name',
        'targeting_peer39pagelanguage': 't.name',
        'targeting_peer39brandprotection': 't.name',
        'targeting_peer39contextualsegment': """
            (CASE WHEN t.parent_id IS NULL THEN t.name ELSE
                (SELECT name FROM targeting_peer39contextualsegment WHERE id=t.parent_id) || ' > ' || t.name END)
            """,
        'targeting_peer39pagequality': """
            (CASE WHEN t.parent_id IS NULL THEN t.name ELSE
                (SELECT name FROM targeting_peer39pagequality WHERE id=t.parent_id) || ' > ' || t.name END)
            """,
        'targeting_lotamedemographic': 't.name',
        'targeting_lotameadvanceddemographic': 't.name',
        'targeting_lotamebehavioralinterest': 't.name',
        'targeting_lotameinfluencers': 't.name',
        'targeting_lotameoffline': 't.name',
    }

    def report_table(self, related_obj, sort_by='~imp', start_date=None, end_date=None, limit=None):
        sql = """
            SELECT {label} AS label, * FROM
                (SELECT dimension_id AS object_id, {metrics} FROM {table} AS r
                 WHERE related_id = {related_id} AND {daterange} GROUP BY object_id ORDER BY {sort_by}
                 LIMIT {limit}) AS s
            LEFT JOIN {dimension_table} AS t ON object_id = t.id ORDER BY {sort_by}
        """.format(
            label=self.label_map[self.model.dimension.field.related.parent_model._meta.db_table],
            metrics=self.metrics(),
            table=self.table,
            dimension_table=self.model.dimension.field.related.parent_model._meta.db_table,
            related_id=quoted(related_obj.id_random),
            daterange=self.daterange_filter(start_date, end_date),
            sort_by=self.get_sorting_command(sort_by),
            limit=self.limit(limit),
        )
        return self.run_sql(sql)
