import json
from urllib import urlencode

import pytest

from haystack.query import SearchQuerySet
from ui.tests.utils import DatabaseDataFactory
from ui.campaign.models import Site, Campaign, Strategy
from tests.integration.wait import wait_for


accounts = [
    {'name': 'a1', 'timezone': 'Europe/Warsaw'},
    {'name': 'a2', 'timezone': 'Europe/Warsaw'},
]

users = [
    {'username': 'me', 'email': 'me@email.em', 'password': 'pass',
     'account': 'a1', 'is_signup_complete': True},
    {'username': 'you', 'email': 'you@email.em', 'password': 'pass',
     'account': 'a2', 'is_signup_complete': True},
]

sites = [
    {'owner': 'a1', 'url': 'http://www.google.com/'},
    {'owner': 'a2', 'url': 'http://www.bing.com/'},
    {'owner': 'a1', 'url': 'http://www.example.com/doodle'},
    {'owner': 'a1', 'url': 'http://www.testing.com/doodle?param=pam'},
    {'owner': 'a1', 'url': 'http://www.otherquery.com/doodle?foo=bar&bar=foo'}
]

campaigns = [
    {'name': 'Awsome campaign',
     'account': 'a1',
     'budget_total': 0,
     'start_UTC': '2013-01-01T00:00',
     'end_UTC': '2013-01-31T00:00',
     'landing_site': 'http://www.google.com/'}
]

strategies = [
    {'name': 'Awsome strategy', 'campaign': campaigns[0]['name'],
     'budget_total': 12345, 'budget_bid_CPM': 0.1},
]


@pytest.fixture()
def site_data(db):
    data = DatabaseDataFactory()
    data.setup_accounts(accounts)
    data.setup_users(users)
    data.setup_landing_pages(sites)
    data.setup_campaigns(campaigns)
    data.setup_strategies(strategies)
    strategy = Strategy.objects.get(name=strategies[0]['name'])
    strategy.landing_sites_def = [
        {'url': sites[2]['url'],
         'weight': 1,
         'custom_variable': None
        }]
    strategy.save()
    return data


@pytest.mark.usefixtures('site_data', 'search_engine')
def test_searchengine_site_results(kclient):
    '''
        Tests that search results returns
        only sites owned by current user's account bind
    '''

    search_query = SearchQuerySet().filter(django_ct='campaign.site')
    assert len(search_query.all()) == len(Site.objects.all())
    res = kclient.post('/accounts/login/', users[0])
    assert res.status_code == 302

    res = kclient.get('/api/site/')
    data = json.loads(res.content)
    sites = data['objects']
    assert len(sites) == 4
    for site in sites:
        obj = Site.objects.get(id=site['id'])
        assert obj.owner.name == accounts[0]['name']


@pytest.mark.parametrize('site_url', (
        'http://www.google.com/',
        'http://www.example.com/doodle',
        'http://www.testing.com/doodle?param=pam',
        'http://www.otherquery.com/doodle?foo=bar&bar=foo',
        'http://www.otherquery.com/doodle?foo=bar',
        'http://www.otherquery.com/',
        'http://www.otherquery.com/doodle',
        'http://www.other',
))
@pytest.mark.django_db
@pytest.mark.usefixtures('site_data', 'search_engine')
def test_searchengine_search(kclient, site_url):
    '''
        Tests that searching for sites returns results
    '''

    res = kclient.post('/accounts/login/', users[0])
    assert res.status_code == 302

    res = kclient.get('/api/site/search/?' + urlencode({'q': site_url}))
    assert res.status_code == 200
    data = json.loads(res.content)
    api_sites = data['objects']

    # at least one object
    assert len(api_sites) > 0
    # should score higher
    assert api_sites[0]['url'].startswith(site_url)


@pytest.mark.celery
def test_new_site_in_search_index(site_data, search_engine, kclient):
    '''
    Checks if newly created page is accessible in search index.
    '''

    res = kclient.post('/accounts/login/', users[0])
    assert res.status_code == 302

    site_url = 'starcorporation.com'
    new_site = Site(url=site_url, owner_id=1)
    new_site.save()

    def is_in_search_index():
        from haystack.query import SearchQuerySet

        return SearchQuerySet().models(Site).filter(url=site_url).count()

    wait_for(is_in_search_index)


@pytest.mark.usefixtures('site_data', 'search_engine')
def test_error_deletecampaign_site():
    '''
        Assert that deleting page assigned to campaign rises error
    '''

    from django.db.models import ProtectedError

    campaign = Campaign.objects.get(name=campaigns[0]['name'])
    site = campaign.landing_site

    with pytest.raises(ProtectedError):
        site.delete()

    strategy_site = Site.objects.get(url=sites[2]['url'])
    with pytest.raises(ProtectedError):
        strategy_site.delete()
