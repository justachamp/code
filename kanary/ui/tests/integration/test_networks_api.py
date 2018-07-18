import pytest

from ui.tests.utils import get_resource
from ui.targeting.models import PublisherTargetValue
from etc import dimensions


LIST_URL = '/api/targeting/network/'

pytestmark = pytest.mark.usefixtures('publishertargetvalues_db',
                                     'search_engine')


def check_data(network_dict):
    '''
    Checks network database data with dictionary returned from API,
    1. Reads PublisherTargetValue from database
    2. Checks whether network, inventory and publisher name are the same on
        object, as they are in api
    3. Formats publisher_id out of publisher generated data and also checks
        it with value returned from API
    '''

    network = PublisherTargetValue.objects.get(pk=network_dict['id'])
    assert network.value_dict['network'] == network_dict['network']
    assert network.inventory_key == network_dict['inventory']


def test_networks_list(client):
    publishers = PublisherTargetValue.objects.representants()

    response, data = get_resource(client, LIST_URL)

    # publishers contains networks itself
    assert data['meta']['total_count'] < len(publishers)

    count_publishers = 0
    for publisher in publishers:
        if publisher.key == dimensions.network:
            count_publishers += 1

    assert data['meta']['total_count'] == count_publishers

    # now lets check if required data is served by API
    for publisher in data['objects']:
        check_data(publisher)


@pytest.mark.parametrize('inventory_type', ('app', 'web'))
def test_networks_list_by_type(client, inventory_type):
    publishers = PublisherTargetValue.objects.representants()
    filtered_networks = []
    # lets filter those with given type only:
    for network in publishers:
        if network.inventory_key == inventory_type and \
                        network.key == dimensions.network:
            filtered_networks.append(network)

    inventory_filtered_url = '{0}?inventory={1}'.format(
        LIST_URL, inventory_type
    )

    response, data = get_resource(client, inventory_filtered_url)

    assert data['meta']['total_count'] == len(filtered_networks)

    for network in data['objects']:
        check_data(network)


def test_networks_filter_by_id(client):
    publishers_targetvalue = PublisherTargetValue.objects.representants()

    networks = []
    for network in publishers_targetvalue:
        if network.key == dimensions.network:
            networks.append(network)

    assert networks

    for network in networks:

        network_filter_url = '{0}?network_id={1}&inventory={2}'.format(
            LIST_URL,
            network.network_id,
            network.inventory_key
        )

        _, network_data = get_resource(client, network_filter_url)
        assert network_data['meta']['total_count'] == 1

        for network in network_data['objects']:
            check_data(network)


@pytest.mark.parametrize('name,count', (
        ('Rubicon', 2),
        ('Nothing', 0),
        ('Nexage', 2),
))
def test_networks_filter_by_name(client, name, count):
    filter_url = '{0}?network={1}'.format(LIST_URL, name)

    _, data = get_resource(client, filter_url)

    assert data['meta']['total_count'] == count
