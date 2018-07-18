import pytest
import simplejson

from etc.constants import AUDIT_PATH
from ui.tests.utils import DatabaseDataFactory, default_user as user
from ui.notification.models import Event


@pytest.fixture
def db_setup(request, db, client):
    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()
    setup.setup_landing_pages()
    setup.setup_campaigns()
    setup.setup_strategies()
    setup.setup_bidding_periods()
    client.login(username=user[0]['username'], password=user[0]['password'])

    def teardown():
        client.logout()

    request.addfinalizer(teardown)
    return setup


@pytest.mark.django_db
def test_audit(client, redisdb_adserver):
    audit_url = '/' + AUDIT_PATH
    response = client.get(audit_url)
    assert response.status_code == 405

    notify = """
        {
           "creative_id":"123",
           "new_audit_status":"audited",
           "old_audit_status":"pending",
           "audit_feedback":"",
           "description":"sample_creative_160x600",
           "google_audit_status":"approved",
           "google_audit_feedback":"",
           "old_google_audit_status":"pending",
           "msft_audit_status":"approved",
           "msft_audit_feedback":"",
           "old_msft_audit_status":"pending",
           "new_brand_id":42
        }
    """
    response = client.post(audit_url, notify, content_type='application/json')
    assert response.content == ''
    assert response.status_code == 200


@pytest.mark.django_db
def test_api_notifications(client, db_setup):
    ''' test if django api returns notifications in correct format '''
    response = client.get('/api/notification/event/?limit=0')

    response = simplejson.loads(response.content)
    assert 'meta' in response
    assert 'objects' in response

    # test first object structure
    obj_0 = response['objects'][0]
    event_0 = simplejson.loads(Event.objects.all()[0].message)

    assert 'datetime' in obj_0
    assert 'header' in obj_0
    message = simplejson.loads(obj_0['message'])
    assert message['objects'].keys() == ['strategy']
    assert message['message'] == event_0['message']
