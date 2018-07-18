import datetime
from optparse import make_option

from django.core.management.base import BaseCommand

from addnow.apps.tracker.models.collections import OutsideShares
from addnow.apps.tracker.tasks import update_counters


class Command(BaseCommand):
    help = 'Generate tracker fixtures to MongoDB'

    option_list = BaseCommand.option_list + (
        make_option('--site', action='store', dest='site', default=1, help='Specify site ID'),
    )

    def get_events(self, site_id, date):
        events = []
        events.append({
            'event': 'follow',
            'data': {
                'site': site_id,
                'date': date,
                'source': 'twitter'
            }
        })
        events.append({
            'event': 'copy',
            'data': {
                'site': site_id,
                'date': date,
                'copied_keywords': ['keyword1', 'keyword2', 'keyword1']
            }
        })
        events.append({
            'event': 'copy',
            'data': {
                'site': site_id,
                'date': date,
                'copied_keywords': ['keyword2', 'keyword2', 'keyword3', 'keyword4', 'keyword4']
            }
        })

        for i in range(10):
            events.append({
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
            })

        for i in range(15):
            events.append({
                'event': 'share',
                'data': {
                    'site': site_id,
                    'date': date,
                    'source': 'facebook',
                    'tool': 'sharing-buttons',
                    'url': 'http://gravity4.com/contact/',
                    'browser': 'Chrome',
                    'country': 'US'
                }
            })

        for i in range(10):
            events.append({
                'event': 'click',
                'data': {
                    'site': site_id,
                    'date': date,
                    'source': 'instagram',
                    'tool': 'sharing-buttons',
                    'url': 'http://gravity4.com/press/',
                    'domain': 'gravity4.com',
                    'browser': 'Firefox',
                    'country': 'AR',
                    'search_engine': 'Bing',
                    'search_term': 'test'
                }
            })

        for i in range(15):
            events.append({
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
            })

        # for sharing tools report
        events.append({
            'event': 'share',
            'data': {
                'site': site_id,
                'date': date,
                'tool': 'address-bar',
                'source': 'darkSocial',
                'url': 'http://gravity4.com/contact/',
                'browser': 'Chrome',
                'country': 'US'
            }
        })

        for i in range(5):
            events.append({
                'event': 'click',
                'data': {
                    'site': site_id,
                    'date': date,
                    'tool': 'address-bar',
                    'source': 'darkSocial',
                    'url': 'http://gravity4.com/contact/',
                    'browser': 'Chrome',
                    'country': 'US'
                }
            })

        for i in range(2):
            events.append({
                'event': 'share',
                'data': {
                    'site': site_id,
                    'date': date,
                    'source': 'facebook',
                    'tool': 'copy-paste',
                    'url': 'http://gravity4.com/press/',
                    'domain': 'gravity4.com',
                    'browser': 'Firefox',
                    'country': 'AR',
                    'search_engine': 'Bing',
                    'search_term': 'test'
                }
            })

        for i in range(13):
            events.append({
                'event': 'click',
                'data': {
                    'site': site_id,
                    'date': date,
                    'source': 'facebook',
                    'tool': 'copy-paste',
                    'url': 'http://gravity4.com/press/',
                    'domain': 'gravity4.com',
                    'browser': 'Firefox',
                    'country': 'AR',
                    'search_engine': 'Bing',
                    'search_term': 'test'
                }
            })

        return events

    def get_outside_shares(self, site_id):
        return [
            {
                'site': site_id,
                'source': 'facebook',
                'url': 'http://facebook.com/help/',
                'value': 1240
            },
            {
                'site': site_id,
                'source': 'googlePlus',
                'url': 'http://plus.google.com/help/',
                'value': 679
            },
            {
                'site': site_id,
                'source': 'linkedin',
                'url': 'http://linkedin.com/help/',
                'value': 2314
            }
        ]

    def handle(self, *args, **options):
        site_id = options['site']
        date_range = [datetime.datetime(datetime.date.today().year, i, 15) for i in range(1, 13)]
        data = []

        self.stdout.write('Adding MongoDB fixtures...')

        for date in date_range:
            data += self.get_events(site_id, date)

        for item in data:
            update_counters(item['event'], 1, **item['data'])

        outside_shares = self.get_outside_shares(site_id)

        for item in outside_shares:
            OutsideShares().set_counter(**item)

        self.stdout.write('Done.')
