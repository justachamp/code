from datetime import datetime


def get_events(site_id, date):
    return [
        {
            'event': 'share',
            'data': {
                'site': site_id,
                'date': date,
                'source': 'twitter',
                'tool': 'sharing-buttons',
                'url': 'http://gravity4.com/contact/',
                'browser': 'Chrome',
                'country': 'US'
            }
        },
        {
            'event': 'click',
            'data': {
                'site': site_id,
                'date': date,
                'source': 'facebook',
                'tool': 'sharing-buttons',
                'url': 'http://gravity4.com/press/',
                'domain': 'gravity4.com',
                'browser': 'Firefox',
                'country': 'AR',
                'search_engine': 'Bing',
                'search_term': 'test'
            }
        },
        {
            'event': 'view',
            'data': {
                'site': site_id,
                'date': date,
                'url': 'http://gravity4.com/press/',
                'domain': 'gravity4.com',
                'browser': 'Safari',
                'country': 'RU'
            }
        },
        {
            'event': 'follow',
            'data': {
                'site': site_id,
                'date': date,
                'source': 'twitter'
            }
        },
        {
            'event': 'copy',
            'data': {
                'site': site_id,
                'date': date,
                'copied_keywords': ['keyword1', 'keyword2', 'keyword1']
            }
        }
    ]


def get_data(site_id, date_range=None):
    date_range = date_range or [datetime.now()]
    data = []

    for date in date_range:
        data += get_events(site_id, date)

    return data
