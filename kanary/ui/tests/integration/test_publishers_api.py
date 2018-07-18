import json

import pytest

from ui.tests.utils import get_resource
from ui.tests.initial_datafixtures import auth_test_accounts, auth_test_users
from ui.targeting.models import PublisherTargetValue
from ui.publishers.models import PublisherSet
from ui.publishers.api import SetValidation
from etc import dimensions


PUBLISHERS_LIST_URL = '/api/targeting/publisher/'
PUBLISHERS_SET_URL = '/api/publishers/sets/'

user = auth_test_users[0]

pytestmark = pytest.mark.usefixtures('publishertargetvalues_db',
                                     'search_engine')


def check_data(publisher_dict):
    '''
    Checks publisher database data with dictionary returned from API,
    1. Reads PublisherTargetValue from database
    2. Checks whether network, inventory and publisher name are the same on
        object, as they are in api
    3. Formats publisher_id out of publisher generated data and also checks
        it with value returned from API
    '''
    publisher = PublisherTargetValue.objects.get(pk=publisher_dict['id'])
    assert publisher.value_dict['network'] == publisher_dict['network']
    assert publisher.inventory_key == publisher_dict['inventory']
    assert publisher.value_dict['publisher_name'] == publisher_dict['name']

    # check restrictions
    assert publisher.sizes == publisher_dict['sizes']
    assert publisher_dict['positions'] == ['Above the fold']
    segment_0 = publisher.segments.all()[0]
    assert publisher_dict['segments'] == [segment_0.display_name]

    publisher_id = '{0}-{1}'.format(publisher.network_id, publisher.id)
    assert publisher_id == publisher_dict['publisher_id']


def test_publishers_list(client):
    publishers = PublisherTargetValue.objects.representants()

    response, data = get_resource(client, PUBLISHERS_LIST_URL)

    # publishers contains networks itself
    assert data['meta']['total_count'] < len(publishers)

    count_publishers = 0
    for publisher in publishers:
        if publisher.key == dimensions.publisher_name:
            count_publishers += 1

    assert data['meta']['total_count'] == count_publishers

    # now lets check if required data is served by API
    for publisher in data['objects']:
        check_data(publisher)


@pytest.mark.parametrize('inventory_type', ('app', 'site'))
def test_publishers_list_by_type(client, inventory_type):
    publishers = PublisherTargetValue.objects.representants()
    filtered_publishers = []
    # lets filter those with given type only:
    for publisher in publishers:
        if publisher.inventory_key == inventory_type and \
                        publisher.key == dimensions.publisher_name:
            filtered_publishers.append(publisher)

    inventory_filtered_url = '{0}?inventory={1}'.format(
        PUBLISHERS_LIST_URL, inventory_type
    )

    response, data = get_resource(client, inventory_filtered_url)

    assert data['meta']['total_count'] == len(filtered_publishers)

    for publisher in data['objects']:
        check_data(publisher)


def test_publishers_filter_by_network(client):
    publishers_targetvalue = PublisherTargetValue.objects.representants()

    networks = []
    publishers = []
    for publisher in publishers_targetvalue:
        if publisher.key == dimensions.network:
            networks.append(publisher)
        else:
            publishers.append(publisher)

    assert networks

    for network in networks:
        filtered_publishers = []
        # lets filter those with given inventory and network id only:
        for publisher in publishers:
            if publisher.network_id == network.network_id and \
                            publisher.inventory_key == network.inventory_key:
                filtered_publishers.append(publisher)

        network_filter_url = '{0}?network_id={1}&inventory={2}'.format(
            PUBLISHERS_LIST_URL,
            network.network_id,
            network.inventory_key
        )

        _, network_data = get_resource(client, network_filter_url)
        assert network_data['meta']['total_count'] == len(filtered_publishers)

        for publisher in network_data['objects']:
            check_data(publisher)

        for filtered_publisher in filtered_publishers:
            publisher_filter_url = '{0}?publisher_id={1}-{2}&inventory={3}' \
                .format(
                PUBLISHERS_LIST_URL,
                filtered_publisher.network_id,
                filtered_publisher.id,
                filtered_publisher.inventory_key
            )

            _, data = get_resource(client, publisher_filter_url)
            # exact match
            assert data['meta']['total_count'] == 1

            assert data['objects'][0] in network_data['objects']

            check_data(data['objects'][0])


@pytest.mark.parametrize('name,count,contains', (
        ('Fruit', 2, 1),
        ('Nothing', 0, 0),
        ('rafalmichal.com', 2, 1),
        ('Ninja Fruit', 1, 1),
        ('Ninja', 1, 1),
        ('Fru', 2, 1),
        ('rafa', 2, 1),
))
def test_publishers_filter_by_name(client, name, count, contains):
    filter_url = '{0}?name={1}'.format(PUBLISHERS_LIST_URL, name)

    _, data = get_resource(client, filter_url)

    assert data['meta']['total_count'] == count
    # exact match should be higher
    if contains:
        assert name in data['objects'][contains - 1]['name']


@pytest.mark.parametrize('network,count', (
        ('appnexus', 0),
        ('Nexage', 2),
        ('Rubicon', 2),
        ('rubicon', 2)
))
def test_publishers_filter_by_networkname(client, network, count):
    filter_url = '{0}?network={1}'.format(PUBLISHERS_LIST_URL, network)

    _, data = get_resource(client, filter_url)

    assert data['meta']['total_count'] == count


def test_publisherset(client, auth_app, publisherset_db):
    client.login(username=user['username'],
                 password=user['password'])

    sets = PublisherSet.objects.filter(
        owner=auth_app.setup.models['account'][auth_test_accounts[0]['name']]
    ).all()

    _, data = get_resource(client, PUBLISHERS_SET_URL)

    assert data['meta']['total_count'] == sets.count()

    for i, pub_set in enumerate(data['objects']):

        _, pub_data = get_resource(client, pub_set['resource_uri'])

        targetvalues_count = sets[i].targetvalues.count()
        assert len(pub_data['targetvalues']) == targetvalues_count
        assert len(pub_data['targetvalues_ids']) == targetvalues_count
        for publisher in pub_data['targetvalues']:
            assert publisher['inventory'] == pub_set['inventory']
            check_data(publisher)


def test_create_publisherset_errors(client, auth_app):
    client.login(username=user['username'],
                 password=user['password'])

    set_no_publishers = {
        'name': 'Awsome set',
        'inventory': 'site'
    }

    res = client.post(PUBLISHERS_SET_URL, data=json.dumps(set_no_publishers),
                      content_type='application/json')

    errors = json.loads(res.content)

    assert res.status_code == 400
    assert errors['sets']['publishers'] == \
           SetValidation.error_messages['publishers']

    set_no_name = {
        'name': '',
        'inventory': 'site'
    }

    res = client.post(PUBLISHERS_SET_URL, data=json.dumps(set_no_name),
                      content_type='application/json')

    errors = json.loads(res.content)

    assert res.status_code == 400
    assert errors['sets']['name'] == SetValidation.error_messages['name']

    set_no_type = {
        'name': 'Awsome set'
    }

    res = client.post(PUBLISHERS_SET_URL, data=json.dumps(set_no_type),
                      content_type='application/json')

    errors = json.loads(res.content)

    assert res.status_code == 400
    assert errors['sets']['inventory'] == SetValidation.error_messages['type']

    set_wrong_type = {
        'name': 'Awsome set',
        'inventory': 'website'
    }

    res = client.post(PUBLISHERS_SET_URL, data=json.dumps(set_wrong_type),
                      content_type='application/json')

    errors = json.loads(res.content)

    assert res.status_code == 400
    assert errors['sets']['inventory'] == \
           SetValidation.error_messages['wrong_type']


@pytest.mark.parametrize('inventory', ('app', 'site'))
def test_create_publisherset(client, auth_app, inventory):
    client.login(username=user['username'],
                 password=user['password'])

    publishers = PublisherTargetValue.objects.representants()

    publishers_ids = []
    # lets filter those with given type only:
    for publisher in publishers:
        if publisher.inventory_key == inventory and \
                        publisher.key == dimensions.publisher_name:
            publishers_ids.append(publisher.id)

    app_set = {
        'name': 'Awsome set',
        'inventory': inventory,
        'targetvalues_ids': publishers_ids,
        'is_network': False
    }

    res = client.post(PUBLISHERS_SET_URL, data=json.dumps(app_set),
                      content_type='application/json')

    response = json.loads(res.content)

    assert app_set['targetvalues_ids'] == response['targetvalues_ids']


@pytest.mark.parametrize('inventory', ('app', 'site'))
def test_create_publisherset_wrong_inventory(client, auth_app, inventory):
    '''
    Check if API prevents saving different types of publishers in one set.
    '''
    client.login(username=user['username'],
                 password=user['password'])

    publishers = PublisherTargetValue.objects.representants()

    publishers_ids = []
    # lets filter those with given type only:
    for publisher in publishers:
        publishers_ids.append(publisher.id)

    app_set = {
        'name': 'Awsome set',
        'inventory': inventory,
        'targetvalues_ids': publishers_ids,
        'is_network': False
    }

    res = client.post(PUBLISHERS_SET_URL, data=json.dumps(app_set),
                      content_type='application/json')

    errors = json.loads(res.content)
    assert res.status_code == 400
    assert errors['sets']['target_values'] == \
           SetValidation.error_messages['target_values']


@pytest.mark.parametrize('inventory', ('app', 'site'))
def test_create_publisherset_wrong_targetvalues(client, auth_app, inventory):
    '''
    Check if API prevents saving different publishers
    when set should store networks.
    '''
    client.login(username=user['username'],
                 password=user['password'])

    publishers = PublisherTargetValue.objects.representants()

    publishers_ids = []
    # lets filter those with given type only:
    for publisher in publishers:
        if publisher.inventory_key == inventory and \
                        publisher.key == dimensions.publisher_name:
            publishers_ids.append(publisher.id)

    assert publishers_ids

    app_set = {
        'name': 'Awsome set',
        'inventory': inventory,
        'targetvalues_ids': publishers_ids,
        'is_network': True
    }

    res = client.post(PUBLISHERS_SET_URL, data=json.dumps(app_set),
                      content_type='application/json')

    errors = json.loads(res.content)
    assert res.status_code == 400
    assert errors['sets']['target_values'] == \
           SetValidation.error_messages['target_values']


def test_edit_publishersets(client, auth_app, publisherset_db):
    '''
    Edits existing publisher by removing one of the TargetValue
    '''

    client.login(username=user['username'],
                 password=user['password'])

    _, sets = get_resource(client, PUBLISHERS_SET_URL)

    current_count = PublisherSet.objects.count()

    for set_element in sets['objects']:
        _, full_set = get_resource(client, set_element['resource_uri'])

        all_ids = full_set['targetvalues_ids']

        full_set['targetvalues_ids'] = full_set['targetvalues_ids'][:1]

        res = client.put(set_element['resource_uri'],
                         data=json.dumps(full_set),
                         content_type='application/json')

        # this should not change! as put requests should only edit resource.
        assert current_count == PublisherSet.objects.count()
        # this assert is placed here to make sure our api is secured against
        # this strange bug in tastypie

        edited_set = json.loads(res.content)

        assert not edited_set['targetvalues_ids'] == all_ids


@pytest.mark.parametrize('inventory', ('app', 'site'))
def test_create_network_publisherset(client, auth_app, inventory):
    client.login(username=user['username'],
                 password=user['password'])

    publishers = PublisherTargetValue.objects.representants()

    networks_ids = []
    # lets filter those with given type only:
    for publisher in publishers:
        if publisher.inventory_key == inventory and \
                        publisher.key == dimensions.network:
            networks_ids.append(publisher.id)

    assert networks_ids

    network_set = {
        'name': 'Awsome, networked set',
        'inventory': inventory,
        'targetvalues_ids': networks_ids,
        'is_network': True
    }

    res = client.post(PUBLISHERS_SET_URL, data=json.dumps(network_set),
                      content_type='application/json')

    set_data = json.loads(res.content)

    assert res.status_code == 201
    assert len(set_data['targetvalues']) == len(networks_ids)


def test_not_translated_positions(kclient, publishertargetvalue_positions,
                                  search_engine):
    '''
    Attempt to run haystack search indexing with unknown positions in
    PublisherTargetValues.
    '''
    code, publishers_json = get_resource(kclient, '/api/targeting/publisher/')
    assert code == 200
    metadata = publishers_json['meta']
    assert min(metadata['total_count'], metadata['limit']) == \
           len(publishers_json['objects'])

    positions_list = [obj['positions'] for obj in publishers_json['objects']]
    empty_positions = map(lambda positions: positions == [], positions_list)
    assert all(empty_positions)


def test_huge_number_of_publishers(client, auth_app, huge_publisherlist_db):
    '''
    Test querying several pages with publishers, with big total number of pages.
    '''

    client.login(username=user['username'],
                 password=user['password'])

    total_count = len(huge_publisherlist_db['publishers_app'] + huge_publisherlist_db['publishers_site'])
    previous_data = {}
    limit = 20
    number_of_pages = (total_count + limit - 1) / limit  # make sure to take ceil

    # query over few pages (not all)
    for page in range(1, number_of_pages, 3):
        url = '{0}?limit={2}&page={1}'.format(PUBLISHERS_LIST_URL, str(page), limit)
        response, data = get_resource(client, url)

        assert response == 200
        assert len(data['objects']) == limit
        assert previous_data != data
        previous_data = data
