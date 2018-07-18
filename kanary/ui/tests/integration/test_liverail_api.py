import pytest
from mock import patch

from apis.liverail import liverail_connection, LiveRailApiResponseError
from ui.storage.tasks import update_video_creative_media
from ui.storage.models import CreativeVideo
from ui.storage.states import LiverailStatus
from ui.notification.models import Event
from ui.tests.utils import copy_creative_to_media_root


MEDIA_TYPES = [
    {'duration': 30, 'width': 400, 'height': 300, 'type': 'video/flv', 'url': 'http://example.com/vid/1'},
    {'duration': 31, 'width': 200, 'height': 100, 'type': 'video/flv', 'url': 'http://example.com/vid/2'},
]

liverail_login = patch('apis.liverail.LiveRailAPI.login')
liverail_logout = patch('apis.liverail.LiveRailAPI.logout')
liverail_list_video_assets = patch('apis.liverail.LiveRailAPI.list_video_assets', return_value=MEDIA_TYPES)
liverail_list_video_no_assets = patch('apis.liverail.LiveRailAPI.list_video_assets', return_value=[])


def liverail_creative_status(status):
    """
    Create a patch object that patches LiveRail creative status call with given status.
    :param str status:
    :rtype mock._patch:
    """
    return patch('apis.liverail.LiveRailAPI.creative_status', return_value=status)


creative_status_error_msg = '<error><code>1</code><message>OMG</message>'
error_msg_list_video_assets_error = '<error><code>2</code><message>WTF</message>'

liverail_creative_status_error = patch('apis.liverail.LiveRailAPI.creative_status',
                                       side_effect=LiveRailApiResponseError(creative_status_error_msg))
liverail_list_video_assets_error = patch('apis.liverail.LiveRailAPI.list_video_assets',
                                         side_effect=LiveRailApiResponseError(error_msg_list_video_assets_error))


@pytest.yield_fixture(autouse=True)
def module_fixtues():
    with patch('apis.liverail.LiveRailAPI.post', side_effect=RuntimeError('API function not mocked.')):
        yield


@pytest.yield_fixture
def liverail_auth():
    with liverail_login as login, liverail_logout as logout:
        yield {'login': login, 'logout': logout}


@pytest.fixture
def video_creatives_nomedia(budget_app):
    creativename = 'creatives/creative_nomedia.mpg'
    copy_creative_to_media_root('creative.mpg', creativename)
    setup = budget_app.setup
    setup.setup_strategies()
    video_creatives = []
    for strategy in setup.models['strategy'].itervalues():
        video_creative = CreativeVideo(
            name='Kreativ von Strategie %s' % strategy.name,
            owner=strategy.campaign.account,
            liverail_id=strategy.pk * 10000 - 1337,
            liverail_status=LiverailStatus.pending,
            file=creativename
        )
        video_creative.save()
        video_creatives.append(video_creative)
    return video_creatives


@pytest.mark.django_db
@liverail_creative_status('active')
@liverail_list_video_assets
def test_liverail_update_media(
        liverail_assets, liverail_creative_status, liverail_auth, video_creatives_nomedia):
    """
    Send all video creatives to audit. Check if all got sent. Check if media responses got saved.
    Check LiveRail calls. Test if login and logout are done once per task.
    """
    update_video_creative_media()
    creatives = CreativeVideo.objects_visible.all()
    for creative in creatives:
        assert creative.media_variants == MEDIA_TYPES
        assert creative.liverail_status == LiverailStatus.active
        assert creative.width == 400
        assert creative.height == 300
        assert creative.duration == 31

    assert liverail_auth['login'].call_count == 1
    assert liverail_auth['logout'].call_count == 1
    assert liverail_creative_status.call_count == len(creatives)
    assert liverail_assets.call_count == len(creatives)

    updated_ids = {c[0][0] for c in liverail_assets.call_args_list}
    creatives_ids = {c.liverail_id for c in creatives}
    assert updated_ids == creatives_ids

    events = Event.objects.filter_message('video_encoded').all()
    assert len(events) == len(creatives)


@pytest.mark.django_db
@patch('ui.storage.models.CreativeVideo.liverail_update_media')
def test_liverail_skip_active_creatives(liverail_update_media, liverail_auth, video_creatives_nomedia):
    """
    Test if creatives with 'active' liverail status are skipped during update_video_creative_media.
    """
    CreativeVideo.objects.all().update(liverail_status=LiverailStatus.active)
    update_video_creative_media()
    assert not liverail_update_media.called


@pytest.mark.django_db
@liverail_creative_status('encoding')
@liverail_list_video_assets
def test_liverail_media_encoding(media, status_encoding, liverail_auth, video_creatives_nomedia):
    """
    `creative_status` should be called once. It should return 'encoding',
    so `list_video_assets` (that actually returns some videos) should not be called.
    """
    creative = video_creatives_nomedia[0]

    with liverail_connection() as api:
        creative.liverail_update_media(api)
        assert status_encoding.call_count == 1
        assert media.call_count == 0
        assert not creative.media_variants

    assert not Event.objects.filter_message('video_encoded').exists()


@pytest.mark.django_db
def test_liverail_media_error(liverail_auth, video_creatives_nomedia):
    """
    Test if errors in API queries result in 'error' state and error message saved in creative.
    """
    creative_1 = video_creatives_nomedia[0]
    creative_2 = video_creatives_nomedia[1]

    with liverail_connection() as api:
        with liverail_creative_status_error:
            creative_1.liverail_update_media(api)
            assert creative_1.liverail_status == LiverailStatus.error
            assert creative_1.liverail_error == creative_status_error_msg
        with liverail_creative_status('active'), liverail_list_video_assets_error:
            creative_2.liverail_update_media(api)
            assert creative_2.liverail_status == LiverailStatus.error
            assert creative_2.liverail_error == error_msg_list_video_assets_error

    assert not Event.objects.filter_message('video_encoded').exists()
    events = Event.objects.filter_message('video_encoding_failed').all()
    assert len(events) == 2
