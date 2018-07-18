import datetime
import random

from addnow.apps.tracker.tasks import update_counters


def get_shares(site, day):
    hour = random.choice(range(1, 15))
    date = datetime.datetime.now() - datetime.timedelta(days=day, hours=hour)
    data = [
        ['share', {
            'site': site,
            'date': date,
            'url': 'http://gravity4.com/contact/',
            'source': 'twitter',
            'tool': 'sharing-buttons',
            'browser': 'Chrome',
            'country': 'US'}],
        ['share', {
            'site': site,
            'date': date,
            'url': 'http://gravity4.com/features/',
            'source': 'twitter',
            'tool': 'copy-paste',
            'browser': 'Firefox',
            'country': 'RU'}],
        ['share', {
            'site': site,
            'date': date,
            'url': 'http://gravity4.com/features/',
            'source': 'darkSocial',
            'tool': 'address-bar',
            'browser': 'Safari',
            'country': 'AR'}]
    ]
    return data


def get_views(site, day):
    hour = random.choice(range(1, 15))
    date = datetime.datetime.now() - datetime.timedelta(days=day, hours=hour)
    data = [
        ['view', {
            'site': site,
            'date': date,
            'url': 'http://gravity4.com/blog/article/',
            'browser': 'Safari',
            'domain': 'gravity4.com',
            'country': 'AR'}],
        ['view', {
            'site': site,
            'date': date,
            'url': 'http://gravity4.com/blog/article/',
            'browser': 'Safari',
            'domain': 'gravity4.com',
            'country': 'AR'}],
        ['view', {
            'site': site,
            'date': date,
            'url': 'http://gravity4.com/blog/article/',
            'browser': 'Safari',
            'domain': 'gravity4.com',
            'country': 'RU'}]
    ]
    return data


def get_clicks(site, day):
    hour = random.choice(range(1, 15))
    date = datetime.datetime.now() - datetime.timedelta(days=day, hours=hour)
    data = [
        ['click', {
            'site': site,
            'date': date,
            'url': 'http://gravity4.com/press/',
            'source': 'twitter',
            'tool': 'sharing-buttons',
            'browser': 'Other',
            'domain': 'gravity4.com',
            'search_engine': 'Bing',
            'search_term': 'test the bing',
            'country': 'US'}],
        ['click', {
            'site': site,
            'date': date,
            'url': 'http://addnow.com/blog/article-1/',
            'source': 'facebook',
            'tool': 'address-bar',
            'browser': 'Chrome',
            'domain': 'addnow.com',
            'search_engine': 'Bing',
            'search_term': 'test the bing',
            'country': 'US'}],
        ['click', {
            'site': site,
            'date': date,
            'url': 'http://addnow.com/blog/article-1/',
            'source': 'darkSocial',
            'tool': 'address-bar',
            'browser': 'Chrome',
            'domain': 'addnow.com',
            'search_engine': 'Bing',
            'search_term': 'test the bing',
            'country': 'AR'}]
    ]
    return data


def get_follows(site, day):
    hour = random.choice(range(1, 15))
    date = datetime.datetime.now() - datetime.timedelta(days=day, hours=hour)
    data = [
        ['follow', {
            'site': site,
            'date': date,
            'source': 'facebook'}],
        ['follow', {
            'site': site,
            'date': date,
            'source': 'twitter'}],
        ['follow', {
            'site': site,
            'date': date,
            'source': 'darkSocial'}]
    ]
    return data


def get_copies(site, day):
    hour = random.choice(range(1, 15))
    date = datetime.datetime.now() - datetime.timedelta(days=day, hours=hour)
    data = [
        ['copy', {
            'site': site,
            'date': date,
            'copied_keywords': ['keyword1', 'keyword2', 'keyword1']}],
        ['copy', {
            'site': site,
            'date': date,
            'copied_keywords': ['keyword1', 'keyword2', 'keyword1']}],
        ['copy', {
            'site': site,
            'date': date,
            'copied_keywords': ['keyword1', 'keyword2', 'keyword1']}]
    ]
    return data


def get_data(site, day):
    methods = {
        'shares': get_shares,
        'clicks': get_clicks,
        'views': get_views,
        'follows': get_follows,
        'copies': get_copies
    }
    data = []
    for i in range(10):
        key = random.choice(methods.keys())
        data += methods[key](site, day=day)
    return data


def save_data(from_day, to_day):
    for site in [1, 2]:
        for day in range(from_day, to_day):
            for i in get_data(site, day=day):
                update_counters(i[0], 1, **i[1])


def run():
    save_data(0, 31)

if __name__ == '__main__':
    run()
