import simplejson as json

import pytest


@pytest.mark.django_db
@pytest.mark.parametrize('object_type, name, resource_uri', [
    ('campaign', 'I\'m a fruit', '/api/campaign/%s/'),
    ('strategy', 'Hello this is Citrus', '/api/strategy/%s/'),
    ('advert', 'ad_lemon', '/api/advert/%s/'),
])
def test_resource_state_api(client, state_app, object_type,
                            name, resource_uri):
    '''
    Check if response is valid and has 'state' attribute, which is of dict type
    '''

    client.login(username='user_2', password='123')

    obj = state_app.models[object_type][name]
    request = client.get(resource_uri % obj.id)

    resource_dict = json.loads(request.content)

    assert request.status_code == 200
    assert 'state' in resource_dict.keys()
    assert type(resource_dict['state']) is dict

    client.logout()
