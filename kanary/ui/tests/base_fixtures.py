import pytest


@pytest.fixture
def kclient(basic_fixture):
    '''Helper fixture which does things:
     - creates our version of django client
     - logs him into default account
     It can be used as our default client in some part of integration tests.
    k(anary) client - name used for faster typing in tests.
    '''

    from ui.tests.client import KanaryClient
    client = KanaryClient()
    client.login(username='user_2', password='123')
    return client
