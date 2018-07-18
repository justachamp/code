# -*- encoding: utf-8 -*-
import csv
import json

import pytest
from django.core.management import call_command
from django.conf import settings as django_settings

from haystack.query import SearchQuerySet
from etc import dimensions
from etc.config import settings
from bidrequest.constants import EXCHANGES
from ui.targeting.models import TargetValue, TargetMap, ContentCategory
from ui.targeting.targetcache import TargetCache


TARGET_VALUES = (
    dict(category=dimensions.g_location,
         value=TargetMap.pack(['BARUSA', 'FOO', 'new foo'])),
    dict(category=dimensions.g_device,
         value=TargetMap.pack(['kanary', 'mobile']))
)

QUERY_MOCK_DATA = (
    ('/api/targeting/%(group)s/search/', TARGET_VALUES),
)


def get_search_results(client, url, query, context):
    url = url + '?q=' + query
    url = url % context
    return json.loads(client.get(url).content)


@pytest.mark.parametrize('searchurl, values', QUERY_MOCK_DATA)
def test_searchengine_found_results(app, kclient, searchurl, values):
    '''Tests if search engine works for given values/query strings'''
    TargetValue.objects.all().delete()
    for data in values:
        TargetValue.objects.create(**data)

    call_command('rebuild_index', interactive=False)

    assert SearchQuerySet().all().count() == 2

    for query in values:
        category = query['category']
        ctx = dict(group=category)
        for query_str in TargetMap.unpack(query['value']):
            results = get_search_results(kclient, searchurl, query_str, ctx)
            assert SearchQuerySet().all().count() > 0
            assert len(results['objects']) > 0
            for result in results['objects']:
                assert query_str in result['value']


def test_searchengine_location_with_hierarchy(transactional_db):
    '''
    Test if search results for location are limited to given dimension
    if query contains it
    '''

    def filter_locations(value=None):
        filters = {
            'django_ct': 'targeting.targetvalue',
            'category': dimensions.g_location
        }
        if value:
            filters['value'] = value
        return SearchQuerySet().filter(**filters)

    states = (
        ['USA', 'California'],
    )
    cities = (
        ['USA', 'California', 'Los Angeles'],
        ['USA', 'Pensylvania', 'California'],
        ['USA', 'Missouri', 'California'],
        ['USA', 'Arkansas', 'California']
    )

    for location in states + cities:
        TargetValue.objects.create(
            category=dimensions.g_location,
            value=TargetMap.pack(location)
        )

    call_command('rebuild_index', interactive=False)

    search_all = \
        [l.object.value_list for l in filter_locations('california')]
    assert sorted(search_all) == sorted(states + cities)

    search_state = \
        [l.object.value_list for l in filter_locations('california state')]
    assert sorted(search_state) == sorted(states)

    search_city = \
        [l.object.value_list for l in filter_locations('california city')]
    assert sorted(search_city) == sorted(cities)


def test_searchengine_location_order_by_rank(transactional_db):
    '''
    Test if search results for location are ordered by hierarchy
    - countries should be first, then states and cities
    '''

    countries = [['California']]
    # Should there be a country with the same name as city, or state
    # it should be higher in search results

    states = [['USA', 'California']]

    cities = [
        ['USA', 'Pensylvania', 'California'],
        ['USA', 'Missouri', 'California'],
        ['USA', 'Washington', 'California'],
        ['USA', 'California', 'Los Angeles'],
        ['USA', 'California', 'Miami'],
        ['USA', 'California', 'San Diego']
    ]

    locations = cities + countries + states

    for location in locations:
        TargetValue.objects.create(
            category=dimensions.g_location,
            value=TargetMap.pack(location)
        )

    call_command('rebuild_index', interactive=False)

    query = SearchQuerySet().filter(
        django_ct='targeting.targetvalue',
        category=dimensions.g_location,
        value="California"
    ).order_by('rank')

    values_all = [l.object.value_list for l in query]

    assert values_all[0] == countries[0]
    assert values_all[1] == states[0]


def test_targetvalue_states(targetvalues_all_states):
    '''
    For single TargetValue of each type, test manager queries and model
    properties.
    '''
    tvs = targetvalues_all_states

    # Testing properties/states:
    assert tvs['representant'].is_representant is True
    assert tvs['represented'].has_representant is True
    assert tvs['unrepresented'].is_representant is False
    assert tvs['unrepresented'].has_representant is False

    # Testing manager queries by states:
    representants = TargetValue.objects.representants()
    represented = TargetValue.objects.represented()
    unrepresented = TargetValue.objects.unrepresented()
    assert representants.count() == 1
    assert representants[0] == tvs['representant']
    assert represented.count() == 1
    assert represented[0] == tvs['represented']
    assert unrepresented.count() == 1
    assert unrepresented[0] == tvs['unrepresented']

    # Those sets must be distinct:
    assert (representants | represented | unrepresented).count() == 3


@pytest.mark.search
@pytest.mark.parametrize('searchurl, values', QUERY_MOCK_DATA)
def test_searchengine_notfound_results(app, kclient, searchurl, values):
    ''' Tests if some another random world does not return any results '''

    TargetValue.objects.all().delete()
    for data in values:
        TargetValue.objects.create(**data)

    call_command('rebuild_index', interactive=False)

    for query in values:
        category = query['category']
        ctx = dict(group=category)
        reverse_query = ''.join(TargetMap.unpack(query['value'])[::-1])
        results = get_search_results(kclient, searchurl, reverse_query, ctx)
        assert len(results['objects']) == 0


def test_genders_representants_exist(app):
    '''
    Tests if in initial state of application
    proper gender representants are loaded into the database.
    '''
    gender_repr = TargetValue.objects.representants_category_gender()

    assert gender_repr.count() == 4
    assert gender_repr.filter(value='Male').exists() is True
    assert gender_repr.filter(value='Female').exists() is True
    assert gender_repr.filter(value='Other').exists() is True
    assert gender_repr.filter(value='Unspecified').exists() is True


@pytest.mark.parametrize('exchange, target_values', [
    (EXCHANGES.appnexus, ('male', 'female')),
    (EXCHANGES.nexage, ('M', 'F')),
])
def test_genders_target_values(app, exchange, target_values):
    '''
    Test if adequate gender target values are inserted into the database
    both for appnexus and nexage exchange.
    '''
    values = TargetValue.objects.filter(
        category='gender',
        exchange=exchange
    )

    assert values.filter(value=target_values[0]).exists() is True
    assert values.filter(value=target_values[1]).exists() is True


@pytest.mark.parametrize('category, value', [
    (dimensions.g_location, ['USA', 'New York', 'Brooklyn']),
    (dimensions.g_location, ['USA', 'New York', None]),
    (dimensions.g_location, ['USA', None, None]),
    (dimensions.g_location, ['USA', None, 'Iowa']),
    (dimensions.g_device, ['Apple', 'Imac']),
    (dimensions.g_device, ['Apple', None]),
    (dimensions.g_os, ['Android', '1.2']),
    (dimensions.g_os, ['Android', None]),
    (dimensions.carrier, ['UltraSupa']),
])
def test_creation_of_representants(app, category, value):
    '''Tries to create representants for all available categories'''
    rep = TargetValue.objects.create_representant(
        'nexage', category, value)
    assert rep.value_list == value


@pytest.mark.parametrize('category, untranslated, representant', [
    (
            dimensions.g_location,
            [['USA', 'New York', 'Brooklyn']],
            ['USA', 'New York', 'NY']
    ),
])
def test_assigning_of_representants(app, category, untranslated, representant):
    dbrepresentant = TargetValue.objects.create_representant(
        'nexage', category, representant)

    # creating untranslated
    for item in untranslated:
        TargetValue.objects.create_unrepresented('nexage', category, item)

    untrans = TargetValue.objects.get_unrepresented_values('nexage', category)
    assert len(untrans) > 0

    for item in TargetValue.objects \
            .get_unrepresented_values('nexage', category):
        TargetValue.objects.create_value_with_representant(item,
                                                           dbrepresentant)
    assert dbrepresentant.untranslate_to('nexage').count() == \
           len(untranslated) + 1


def test_content_category_exist(app):
    """
    Tests if in initial state of application proper content category
    representants are loaded into the database.

    #. Get the number of them.
    #. Checks if these categories exists in database.
    """
    content_category_repr = ContentCategory.objects.all()

    assert content_category_repr.count() == 171

    categories = set()

    with open(django_settings.PROJECT_DIR / "targeting" /
                      "csv" / "content_categories" /
                      "category_mapping_complete.csv", 'rb') as csvfile:
        rows = csv.reader(csvfile, delimiter=';')
        rows.next()

        for row in rows:
            (
                iab_category,
                iab_category_name,
                appnexus_category_name,
                appnexus_category
            ) = row

            if appnexus_category == "#N/A":
                continue

            appnexus_category_name = appnexus_category_name \
                .split("(")[0].strip()
            categories.add(appnexus_category_name)

    for category in categories:
        assert content_category_repr.filter(name=category).exists()


@pytest.mark.parametrize('params, value', (
        (['nexage', 'category', ('łódź', 'gżęgżółka')], 666),
        (['appnexus', 'location', ('繁體', )], 777),
))
def test_target_cache_for_unicode_values(redisdb_targeting_cache, params, value):
    TargetCache.set_target_pk(*params + [value])

    assert TargetCache.get_target_pk(*params) == value


@pytest.mark.parametrize('dimension_values, pks', (
        (
                [
                    ('USA', 'NY', 'NY'),
                    ('USA', 'NY')
                ],
                [4, 3]
        ), (
                [
                    ('CAN', 'NY', 'NY'),
                    ('CAN', 'NY')
                ],
                [4, None]
        ),
))
def test_target_cache_multiget(redisdb_targeting_cache, dimension_values, pks):
    """
    Check if multi_get is able to retrieve multiple pks from cache.
    """

    exchange = EXCHANGES.appnexus
    category = 'region'
    for param, value in zip(dimension_values, pks):
        if value:
            # if None, we won't set it, but we should get None back from cache.
            TargetCache.set('prefix', exchange, category, param, value)

    results = TargetCache.multi_get('prefix', [exchange, category], dimension_values)
    for param, value in zip(dimension_values, pks):
        assert results[param] == value


def test_target_cache_disabled(redisdb_targeting_cache):
    assert settings.targeting_cache_enabled is True
    TargetCache.tv_cache.client.clear()
    assert TargetCache.set('AA', 'BB', 'b') is True
    assert TargetCache.set('AA', 'CC', 'c') is True

    assert TargetCache.get('AA', 'CC') == 'c'
    assert TargetCache.multi_get('AA', '', ['BB', 'CC']) == {'BB': 'b', 'CC': 'c'}

    settings.targeting_cache_enabled = False
    assert TargetCache.get('AA', 'CC') is None
    assert TargetCache.multi_get('AA', '', ['BB', 'CC']) == {'BB': None, 'CC': None}

    assert TargetCache.set('AA', 'DD', 'd') is None  # Should be ignored.

    settings.targeting_cache_enabled = True
    assert TargetCache.get('AA', 'DD') is None  # Saving keys to disabled cache should have no effect.
    # Values saved before switching the cache off should remain intact:
    assert TargetCache.multi_get('AA', '', ['BB', 'CC']) == {'BB': 'b', 'CC': 'c'}

    # After re-enabling, the cache should function:
    assert TargetCache.set('AA', 'EE', 'e') is True
    assert TargetCache.get('AA', 'EE') == 'e'
