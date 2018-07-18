import hashlib
from datetime import datetime, timedelta

from django.core.cache import cache

import pytz

from addnow.apps.analytics import settings as analytics_settings, utils
from addnow.apps.analytics.exceptions import ProfileIDNotProvidedError


def get_id(latitude, longitude):
    hashlib.sha256(latitude + ':' + longitude).hexdigest()


def get_active_visitors_report(user, site, history):
    if not site.analytics_profile:
        raise ProfileIDNotProvidedError()

    timezone = cache.get(analytics_settings.TIMEZONE_CACHE_KEY_PLACEHOLDER % site.analytics_profile)
    if not timezone:
        profile = utils.get_profile(
            user, site.analytics_account, site.analytics_property, site.analytics_profile
        )
        timezone = profile.get('timezone')
        cache.set(analytics_settings.TIMEZONE_CACHE_KEY_PLACEHOLDER % site.analytics_profile, timezone)
    tz = pytz.timezone(timezone)
    today = datetime.now(tz=tz)
    if history:
        if not isinstance(history, int):
            history = analytics_settings.GA_TIME_ELAPSED

        tomorrow = today + timedelta(days=1)

        data = utils.get_report_data(
            user, site.analytics_profile,
            today, tomorrow,
            ['ga:users'],
            ['ga:latitude', 'ga:longitude', 'ga:country', 'ga:city', 'ga:source', 'ga:hour', 'ga:minute'],
            ['-ga:hour', '-ga:minute'],
            'ga:longitude!=0.0000'
        )

        def t1(ga_item):
            latitude, longitude, country, city, source, hour, minute, id = ga_item
            hour = int(hour)
            minute = int(minute)
            ts = tz.localize(datetime(today.year, today.month, today.day, hour, minute))

            return {
                'id': get_id(latitude, longitude),
                'geo': {
                    'latitude': latitude,
                    'longitude': longitude,
                    'country': country,
                    'city': city
                },
                'source': source,
                'ts': ts.isoformat(),
                'elapsed': hour * 3600 + minute * 60
            }

        intermediate = map(t1, data.get('rows', []))

        ret = []
        if intermediate:
            elapsed_max = intermediate[0].get('elapsed')
            for index, item in enumerate(intermediate):
                if item['elapsed'] >= elapsed_max - history:
                    item['elapsed'] = elapsed_max - item['elapsed']
                    ret.append(item)
        data = ret
    else:
        data = utils.get_realtime_data(
            user, site.analytics_profile,
            ['rt:activeUsers'],
            ['rt:latitude', 'rt:longitude', 'rt:country', 'rt:city', 'rt:source'],
            'ga:longitude!=0.000000'
        )

        def t2(rt_item):
            latitude, longitude, country, city, source, id = rt_item
            return {
                'id': get_id(latitude, longitude),
                'geo': {
                    'latitude': latitude,
                    'longitude': longitude,
                    'country': country,
                    'city': city
                },
                'source': source,
                'ts': today.isoformat(),
                'elapsed': 0
            }

        data = map(t2, data.get('rows', []))
    return data


def get_views(site, begin_date, end_date, aggregation):
    dimension = {
        'day': 'ga:date',
        'hour': 'ga:hour'
    }[aggregation]

    views_report = utils.get_report_data(
        site.user, site.analytics_profile,
        begin_date, end_date, ['ga:pageviews'], [dimension]
    )
    rows = views_report.get('rows', [])
    begin_date = begin_date.replace(hour=0, minute=0, second=0)
    result = []

    for item in rows:
        date, views = item
        if aggregation == 'day':
            date = datetime.strptime(date, '%Y%m%d')
        elif aggregation == 'hour':
            date = begin_date + timedelta(hours=int(date))
        result.append({'views': views, 'date': date})

    return result


def get_referring_domains(site, begin_date, end_date):
    referring_domains_report = utils.get_report_data(
        site.user, site.analytics_profile, begin_date, end_date,
        ['ga:entrances'], ['ga:source'], '-ga:entrances', 'ga:medium==referral'
    )
    rows = referring_domains_report.get('rows', [])
    referring_domains = []

    for item in rows:
        domain, entrances = item
        referring_domains.append({'domain': domain, 'count': entrances})

    return referring_domains


def get_search_terms(site, begin_date, end_date):
    search_terms_report = utils.get_report_data(
        site.user, site.analytics_profile, begin_date, end_date,
        ['ga:entrances'], ['ga:keyword'], '-ga:entrances',
        'ga:medium==organic;ga:keyword!=(not provided);ga:keyword!=(not set)'
    )
    rows = search_terms_report.get('rows', [])
    search_terms = []

    for item in rows:
        keyword, entrances = item
        entrances = int(entrances)
        totals = int(search_terms_report['totalsForAllResults']['ga:entrances'])
        percentage = round(entrances / totals * 100, 0) if totals > 0 else 0
        search_terms.append({'searchTerm': keyword, 'count': entrances, 'percentage': percentage})

    return search_terms


def get_search_engines(site, begin_date, end_date):
    search_engines_report = utils.get_report_data(
        site.user, site.analytics_profile, begin_date, end_date,
        ['ga:entrances'], ['ga:source'], '-ga:entrances', 'ga:medium==organic'
    )
    rows = search_engines_report.get('rows', [])
    search_engines = []

    for item in rows:
        domain, entrances = item
        entrances = int(entrances)
        totals = int(search_engines_report['totalsForAllResults']['ga:entrances'])
        percentage = round(entrances / totals * 100, 0) if totals > 0 else 0
        search_engines.append({'searchEngine': domain, 'count': entrances, 'percentage': percentage})

    return search_engines
