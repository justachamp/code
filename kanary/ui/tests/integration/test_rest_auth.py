import pytest
import simplejson as json


@pytest.mark.django_db
@pytest.mark.parametrize('user_data, campaign_name', [
    (('user_1', '123'), ('campaign_1')),
    (('user_2', '123'), ('campaign_2')),
])
def test_campaign_list(client, auth_app, user_data, campaign_name):
    '''
    Tests if user gets from server only those campaigns which has
    same account as user's one.
    '''
    username, password = user_data
    client.login(username=username, password=password)

    request = client.get('/api/campaign/')
    campaigns = json.loads(request.content)['objects']

    assert len(campaigns) == 1
    assert campaigns[0]['name'] == campaign_name
