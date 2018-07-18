from ui.account.models import User
from ui.tests.initial_datafixtures import auth_test_users

PATHS = [
    'account/account/', 'account/invoice/', 'account/payment/', 'account/user/', 'bidding_spendings/dailyspendings/',
    'welcome/', 'creative_sent_for_audit/', 'creative_audit_rejected/', 'new_invoice/', 'no_sufficient_funds/',
    'no_sufficient_funds_reminder/',
]


def test_admin_urls(client, auth_app):
    """Check if all admin urls are configured properly, and accessible."""
    user = auth_test_users[0]
    User.objects.filter(username=user['username']).update(is_staff=True, is_superuser=True)

    client.login(username=user['username'], password=user['password'])

    for path in PATHS:
        assert client.get('/admin/' + path).status_code == 200
