from datetime import datetime, timedelta

from pytz import timezone

from addnow.apps.tracker.models.collections import GeoIPModel


ANALYTICS_TIME_LIMIT = 1 * 60 * 60  # 1 hour
ANALYTICS_RT_TIME_LIMIT = 60


def get_active_visitors_report(user, site, history):
    end_date = datetime.utcnow()

    if history:
        if not isinstance(history, int):
            history = ANALYTICS_TIME_LIMIT
        begin_date = end_date - timedelta(seconds=history)
    else:
        begin_date = end_date - timedelta(seconds=ANALYTICS_RT_TIME_LIMIT)

    query = {
        'site': site.pk,
        'timestamp': {'$gte': begin_date, '$lte': end_date}
    }

    data = GeoIPModel().find(query)
    ret = []

    utc = timezone('UTC')

    for item in data:
        ret.append(
            {
                'id': str(item['_id']),
                'geo': item['geo'],
                'source': None,
                'ts': utc.localize(item['timestamp']).isoformat(),
                'elapsed': 0
            }
        )

    return ret
