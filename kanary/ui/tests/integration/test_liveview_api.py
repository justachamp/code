from datetime import datetime, timedelta

import pytest

from ui.tests.utils import get_resource
from ui.tests.initial_datafixtures import default_user
from etc.constants import FRONTEND_LIVE_VIEW_PERIOD_SECONDS as LIVE_VIEW_PERIOD
from ui.account.models import Account
from ui.liveview.views import LiveViewDataSource
from ui.liveview.models import LiveViewCounter


@pytest.mark.parametrize('model_name', [
    'Campaign',
    'Strategy',
    'Advert'
])
def test_liveview_api(client, running_app, model_name):
    '''
    Check liveview api filtering and updating
    '''

    LIVEVIEW_URL = '/liveview/%s/' % model_name
    METRICS = [
        {'bid': 10, 'imp': 1},
        {'bid': 100, 'imp': 10},
        {'bid': 1000, 'imp': 100}
    ]
    METRICS_SUM = {'bid': 1110, 'imp': 111, 'winbid_ratio': '10.0%'}

    client.login(
        username=default_user[0]['username'],
        password=default_user[0]['password']
    )

    account = Account.objects.get(name=default_user[0]['account'])

    active_objects = LiveViewDataSource(model_name, account).active_objects

    # Active objects list should not be empty otherwise test will check nothing
    assert active_objects

    # Insert old metric for first object
    test_object_id = active_objects[0].public_id
    LiveViewCounter.objects.create(
        public_id=test_object_id,
        imp=1234,
        bid=4567,
        time=datetime.utcnow() - timedelta(seconds=LIVE_VIEW_PERIOD * 2)
    )

    # Get live view data
    status, live_data = get_resource(client, LIVEVIEW_URL)
    assert status == 200

    assert [(o.public_id, o.full_name) for o in active_objects] == \
           [(metric['public_id'], metric['name']) for metric in live_data]

    # Check if all metrics are empty. Metrics older than live view period
    # should not be displayed
    for metric in live_data:
        assert metric['imp'] == 0
        assert metric['bid'] == 0
        assert metric['winbid_ratio'] == '0.0%'

    # Insert fresh metrics for first object
    for index, metric in enumerate(METRICS, start=2):
        metric['time'] = datetime.utcnow() - timedelta(seconds=LIVE_VIEW_PERIOD / index)
        metric['public_id'] = test_object_id
        LiveViewCounter.objects.create(**metric)

    # Get live view data
    status, live_data = get_resource(client, LIVEVIEW_URL)
    assert status == 200

    # Check if metric sums were calculated correctly
    test_metric = filter(lambda m: test_object_id == m['public_id'], live_data)[0]
    assert test_metric['bid'] == METRICS_SUM['bid']
    assert test_metric['imp'] == METRICS_SUM['imp']
    assert test_metric['winbid_ratio'] == METRICS_SUM['winbid_ratio']
