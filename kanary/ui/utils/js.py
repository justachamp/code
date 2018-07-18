import simplejson
from django.conf import settings

from etc.constants import (
    FRONTEND_DATE_FORMAT, FRONTEND_TIME_FORMAT, FRONTEND_FLOAT_PRECISION,
    TARGETING_ADDITIONAL_DATA_COSTS, METRICS, OVERVIEW_METRICS,
    FRONTEND_REPORTS_DEFAULT_SELECTED_ENTRIES, FRONTEND_REPORTS_ITEMS_LIMIT
)
from etc.dimensions import named_dimensions_report, mobile_dimensions


js_config = simplejson.dumps({
    'AJAX_HEADER_X_VERSION': settings.AJAX_HEADER_X_VERSION,
    'AJAX_HEADER_USER_INFO': settings.AJAX_HEADER_USER_INFO,
    'BE_QUIET': settings.JS_BE_QUIET,
    'JS_DATE_FORMAT': FRONTEND_DATE_FORMAT['LONG'],
    'JS_DATE_FORMAT_SHORT': FRONTEND_DATE_FORMAT['SHORT'],
    'JS_DATE_FORMAT_DATEPICKER': FRONTEND_DATE_FORMAT['DATEPICKER'],
    'JS_DATE_FORMAT_DATERAGEPICKER': FRONTEND_DATE_FORMAT['DATERAGEPICKER'],
    'JS_DATE_FORMAT_URL': FRONTEND_DATE_FORMAT['URL'],
    'JS_TIME_FORMAT': FRONTEND_TIME_FORMAT,
    'REQUIRE_TIMEOUT': settings.REQUIRE_TIMEOUT,
    'LIVE_VIEW_POLLING_INTERVAL': settings.LIVE_VIEW_POLLING_INTERVAL,
    'LIVE_VIEW_IS_ENABLED': settings.LIVE_VIEW_IS_ENABLED,
    'REPORT_FLOAT_PRECISION': FRONTEND_FLOAT_PRECISION,
    'REPORT_ITEMS_LIMIT': FRONTEND_REPORTS_ITEMS_LIMIT,
    'TARGETING_ADDITIONAL_DATA_COSTS': TARGETING_ADDITIONAL_DATA_COSTS,
    'METRICS': [
        {
            'slug': slug,
            'name': name,
            'short_name': short_name,
            'checked': slug in OVERVIEW_METRICS
        } for slug, (name, short_name) in METRICS.items()
    ],
    'REPORT_DIMENSIONS': [
        {
            'slug': dim,
            'name': name,
            'is_mobile': dim in mobile_dimensions,
        } for dim, name in named_dimensions_report.items()
    ],
    'REPORTS_DEFAULT_SELECTED_ENTRIES': FRONTEND_REPORTS_DEFAULT_SELECTED_ENTRIES,
    'VERSION': settings.VERSION,
})
