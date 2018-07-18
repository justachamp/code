import pytest

from ui.notification.models import Event


@pytest.mark.parametrize('creative_id, status, msg', [
    ('creative_image_1', 'r', 'creative_rejected'),
    ('creative_image_1', 'a', 'creative_audited'),
    ('creative_image_1', 'p', 'creative_pending'),
    ('creative_image_1', 'u', 'creative_rejected'),
    ('creative_image_1', 'e', 'creative_expired'),
])
def test_audit_events(state_app, creative_id, status, msg):
    '''
    Check if changing appnexus_status generates correct timeline events.
    '''

    creative = state_app.models['creative'][creative_id]
    creative.appnexus_status = status
    creative.save()

    latest_event = Event.objects.all()[0]
    assert latest_event.message_name == msg
