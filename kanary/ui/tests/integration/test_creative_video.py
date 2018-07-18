from itertools import cycle

import pytest
from mock import patch, Mock, call

from ui.storage.tasks import upload_file_to_cdn, update_video_creative_media
from ui.tests.utils import DatabaseDataFactory, copy_creative_to_media_root
from ui.storage.states import LiverailStatus


def refresh(model_instance):
    """
    Refreshes model instance by reloading data from database.
    """
    return model_instance.__class__.objects.get(pk=model_instance.pk)


@pytest.fixture
def video_app(basic_fixture):
    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()
    setup.setup_landing_pages()
    setup.setup_campaigns()
    setup.setup_strategies()
    setup.setup_creative_videos()
    setup.setup_adverts([
        {
            'name': 'ad_blueberry',
            'strategy': 'han i has a pumpkin?',
            'creative': 'creative_video_1',
            'url': 'http://www.wp.pl/',
        },
    ])
    return setup


@pytest.yield_fixture
def liverail_api():
    """
    Mocks behaviours of liverail api, tries to return various ids (1..100)
    and then assumes that all creatives are already transcoded and active.
    """
    api_mock = Mock()
    liverail_id_serial = cycle(reversed(xrange(1, 100, 1)))
    medias = [{'duration': 15, 'width': 400, 'height': 300, 'type': 'video/flv', 'url': 'http://example.com'}]
    with patch('apis.liverail.LiveRailAPI') as api_mock:
        api_mock.return_value.add_creative.side_effect = lambda *args, **kwargs: liverail_id_serial.next()
        api_mock.return_value.creative_status.return_value = 'active'
        api_mock.return_value.CreativeStatus.active = 'active'
        api_mock.return_value.list_video_assets.return_value = medias
        yield api_mock


@pytest.fixture
def video(video_app):
    """ Shortcut for access for video creative. """
    video_model = video_app.models['creative']['creative_video_1']
    video_model.liverail_id = None
    video_model.liverail_status = LiverailStatus.pending
    video_model.save()
    return video_model


@pytest.mark.django_db
def test_creative_video_upload(liverail_api, video):
    """
    Tests following scenario:
    * uploads new creative.
    * tries to reupload creative again and checks if liverail_id didn't change.
    """
    upload_file_to_cdn(video.pk, video.contents)

    register_call = call().add_creative(video.pk, video.name)

    video = refresh(video)
    upload_call = call().upload_video_asset(video.liverail_id, video.contents)

    assert register_call in liverail_api.mock_calls
    assert upload_call in liverail_api.mock_calls
    assert video.liverail_id == 99

    liverail_api.mock_calls = []

    # Uploading new version of video, liverail_id shouldn't change.
    copy_creative_to_media_root("creative2.mpg", "creatives/creative2.mpg")
    video.file = 'creatives/creative2.mpg'
    video.save()

    upload_call = call().upload_video_asset(video.liverail_id, video.contents)

    upload_file_to_cdn(video.pk, video.contents)
    assert register_call not in liverail_api.mock_calls
    assert upload_call in liverail_api.mock_calls
    assert video.liverail_id == 99


@pytest.mark.django_db
def test_creative_video_liverail_statuses(liverail_api, video):
    """
    Tests if statuses are set properly during upload of data to cdn.
    Additionally, there's re-upload scenario.
    """
    assert video.liverail_status == LiverailStatus.pending
    upload_file_to_cdn(video.pk, video.contents)

    video = refresh(video)
    assert video.liverail_status == LiverailStatus.uploaded

    # Video after save and proper get of liverail status data should
    # be audited via appnexus.
    update_video_creative_media()
    video = refresh(video)

    assert video.is_auditable
    video.save()

    video = refresh(video)
    assert video.to_audit  # video has been sent to audit.

    # Uploading new version of video, liverail_id shouldn't change.
    copy_creative_to_media_root("creative2.mpg", "creatives/creative2.mpg")
    video.file = 'creatives/creative2.mpg'
    video.save()

    video = refresh(video)
    # after second upload, status should be reset to pending for a little moment
    # and then creative should be reuploaded again what causes 'uploaded' status.
    assert video.liverail_status == LiverailStatus.uploaded
    assert not video.to_audit
