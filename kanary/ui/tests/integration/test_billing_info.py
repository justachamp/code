import pytest
import simplejson
from django.core.urlresolvers import reverse

from adserving.types import Decimal


@pytest.mark.parametrize('user_data, results', [
    (('user_1', '123'), ('$30.00', '$30.00', 2)),
    (('user_2', '123'), ('$0.00', None, 0)),
])
def test_billing_info_auth(client, billing_app, user_data, results):
    '''
    Checks if user has access to proper data of billing
    and checks if proper values are returned
    '''
    username, password = user_data
    client.login(username=username, password=password)

    request = client.get(reverse('billing_info'))
    content = simplejson.loads(request.content)

    assert content['account_balance'] == results[0]
    assert content['last_payment'] == results[1]
    assert len(content['transactions']) == results[2]


@pytest.mark.parametrize('budget_spent, balance', [
    (Decimal('30'), '$0.00'),
    (Decimal('40.25'), '-$10.25'),
    (Decimal('20.75'), '$9.25')
])
def test_account_balance(client, billing_app, budget_spent, balance):
    '''
    Checks if account balance is properly counted for positive,
    zero and negative values.
    '''
    # Save money spent in campaign
    campaign = billing_app.setup.models['campaign']['campaign_1']
    campaign.budget_spent = budget_spent
    campaign.save()

    # Get billing info data
    client.login(username='user_1', password='123')

    request = client.get(reverse('billing_info'))
    content = simplejson.loads(request.content)

    # Check if account has a proper value returned
    assert content['account_balance'] == balance
