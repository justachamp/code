import os
import json
from uuid import uuid4
import base64

import pytest
from django.conf import settings

from ui.tests.utils import DatabaseDataFactory, get_resource
from ui.tests.initial_datafixtures import default_account
from ui.account.models import Account
from ui.storage.models import Creative


accounts = [{'name': 'acc', 'timezone': 'Europe/Warsaw'},
            {'name': 'acc_2', 'timezone': 'Europe/Warsaw'}]

users = [{'username': 'user_2', 'email': 'test@clearcode.cc',
          'password': '123', 'account': 'acc', 'is_signup_complete': True},
         {'username': 'no_creatives', 'email': 'test2@clearcode.cc',
          'password': 'sad', 'account': 'acc_2', 'is_signup_complete': True}]

creatives = [{'name': 'creative_image_1', 'owner': 'acc',
              'width': 300, 'height': 250, 'image': 'test_creative.jpg'},
             {'name': 'creative_image_2', 'owner': 'acc',
              'width': 300, 'height': 250, 'image': 'test_creative2.jpg'}]


@pytest.fixture
def setup_db(db):
    suite = DatabaseDataFactory()
    suite.setup_accounts(accounts)
    suite.setup_users(users)
    suite.setup_creative_images(creatives)

    return suite


pytestmark = pytest.mark.usefixtures('setup_db')


@pytest.yield_fixture
def imagefile(request):
    u = open('../uploads/creative.jpg')
    name = base64.urlsafe_b64encode(uuid4().bytes).replace('=', '')

    filename = name + '.jpg'
    filepath = os.path.join(settings.CREATIVES_DIR, filename)
    localFile = open(filepath, 'w')
    localFile.write(u.read())
    localFile.close()

    yield os.path.join('creatives', filename)
    os.remove(filepath)


@pytest.yield_fixture
def flashfile(request):
    u = open('../uploads/creative.swf')
    name = base64.urlsafe_b64encode(uuid4().bytes).replace('=', '')

    filename = name + '.jpg'
    filepath = os.path.join(settings.CREATIVES_DIR, filename)
    localFile = open(filepath, 'w')
    localFile.write(u.read())
    localFile.close()

    yield os.path.join('creatives', filename)
    os.remove(filepath)


@pytest.mark.parametrize('user, creatives_count', [
    (users[0], 2),
    (users[1], 0),
])
def test_creatives_list(client, user, creatives_count):
    '''
    Check list creatives, if we get creatives assigned for given user
    '''

    list_url = '/api/storage/creative/'

    status_code, _ = get_resource(client, list_url)
    assert status_code == 401

    client.login(username=user['username'], password=user['password'])

    status_code, content = get_resource(client, list_url)
    assert status_code == 200

    assert content['meta']['total_count'] == creatives_count
    assert len(content['objects']) == creatives_count


def test_creatives_view(client):
    '''test for one creative view'''

    url = '/api/storage/creative/'

    client.login(username=users[0]['username'],
                 password=users[0]['password'])

    account = Account.objects.get(name=default_account[0]['name'])

    creatives = Creative.objects_visible.filter(owner=account)

    _, response = get_resource(client, url)

    for creative in creatives:
        elements = [rc for rc in response['objects']
                    if rc['id'] == creative.id]
        assert elements

        # checking if type is equal substracted Creative class name
        assert elements[0]['type'] == creative.__class__.__name__[8:]

        status, creative_resource = get_resource(
            client, elements[0]['resource_uri'])

        assert status == 200
        assert creative_resource == elements[0]


def test_delete_creative(client):
    '''delete creative'''

    url = '/api/storage/creative/'

    client.login(username=users[0]['username'],
                 password=users[0]['password'])

    account = Account.objects.get(name=default_account[0]['name'])

    creatives = Creative.objects_visible.filter(owner=account)

    _, response = get_resource(client, url)

    assert len(creatives) == 2
    assert len(response['objects']) == 2

    object_to_delete = response['objects'][0]

    res = client.delete(object_to_delete['resource_uri'])

    assert res.status_code == 204
    assert not res.content

    status, _ = get_resource(client, object_to_delete['resource_uri'])
    assert status == 404

    creatives = Creative.objects_visible.filter(owner=account)

    _, response = get_resource(client, url)

    assert len(creatives) == 1
    assert len(response['objects']) == 1


@pytest.mark.parametrize('creative_type, is_valid', [
    ('Image', True),
    ('', False)
])
def test_add_creative(client, imagefile, creative_type, is_valid):
    '''adding new creative'''

    url = '/api/storage/creative/'

    client.login(username=users[0]['username'],
                 password=users[0]['password'])

    _, response = get_resource(client, url)

    assert len(response['objects']) == 2

    new_creative = {'type': creative_type,
                    'name': 'Awsome image',
                    'api_data': imagefile}

    res = client.post(url, data=json.dumps(new_creative),
                      content_type='application/json')

    response = json.loads(res.content)

    if is_valid:
        assert response['width'] == 200
        assert response['height'] == 200
        assert response['type'] == 'Image'

        _, response = get_resource(client, url)
        assert len(response['objects']) == 3
    else:
        assert res.status_code == 400
        assert response['error'] == "[u'You cannot create creative without a type.']"


def test_add_flash_creative(client, flashfile):
    '''adding new creative'''

    url = '/api/storage/creative/'

    client.login(username=users[0]['username'],
                 password=users[0]['password'])

    _, response = get_resource(client, url)

    assert len(response['objects']) == 2

    new_creative = {'type': 'Flash',
                    'name': 'Awsome flash file',
                    'api_data': flashfile}

    res = client.post(url, data=json.dumps(new_creative),
                      content_type='application/json')
    response = json.loads(res.content)

    assert response['width'] == 300
    assert response['height'] == 250
    assert response['type'] == 'Flash'

    _, response = get_resource(client, url)
    assert len(response['objects']) == 3


def test_edit_creative(client, imagefile):
    '''updating existing creative'''

    url = '/api/storage/creative/'

    client.login(username=users[0]['username'],
                 password=users[0]['password'])

    _, response = get_resource(client, url)

    # we have two creatives
    assert len(response['objects']) == 2

    # we take one to edit
    original_creative = response['objects'][0]
    db_object = Creative.objects_visible.filter(id=original_creative['id'])[0]

    # we change everything except id
    edited_creative = {'id': original_creative['id'],
                       'type': 'Image',
                       'name': 'Awsome image',
                       'api_data': imagefile}

    client.put(original_creative['resource_uri'],
               data=json.dumps(edited_creative),
               content_type='application/json')

    # make sure we still have two creatives
    _, response = get_resource(client, url)
    assert len(response['objects']) == 2

    # get changed creative data
    _, response = get_resource(client, original_creative['resource_uri'])

    assert response['id'] == db_object.id
    # should be different than original one
    assert not response['name'] == db_object.name
    assert not response['api_data'] == db_object.image
    # this is what it should match to
    assert response['name'] == edited_creative['name']
    assert response['api_data'].replace(settings.MEDIA_URL, '') == \
           edited_creative['api_data']
