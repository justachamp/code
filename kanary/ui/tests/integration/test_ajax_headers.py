from django.conf import settings


def test_ajax_headers(client, auth_app):
    client.login(username='user_1', password='123')

    # Ajax request.
    response = client.get('/api/campaign/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

    # Check headers, we should have them.
    assert response.has_header(settings.AJAX_HEADER_USER_INFO)
    assert response.has_header(settings.AJAX_HEADER_X_VERSION)

    # Are we add info to header?
    assert 'unread_events_count' in response.serialize_headers()
    assert 'account_balance' in response.serialize_headers()
