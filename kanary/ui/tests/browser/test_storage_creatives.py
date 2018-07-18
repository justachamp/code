import os
import pytest

from django.core.management import call_command

from ui.storage.models import Creative, STATUS


ENCODED_CREATIVE_NAME = 'encoded'
NOTENCODED_CREATIVE_NAME = 'not_encoded'


@pytest.fixture
def creatives_db(user_db):
    '''Initializes database with data needed by storage'''

    creatives = [
        {'name': 'creative_image_rejected', 'owner': 'acc', 'width': 300,
         'height': 250, 'image': 'test_creative.jpg'},
        {'name': 'creative_image_audited', 'owner': 'acc', 'width': 300,
         'height': 250, 'image': 'test_creative.jpg'},
        {'name': 'creative_image_expired', 'owner': 'acc', 'width': 300,
         'height': 250, 'image': 'test_creative.jpg'},
        {'name': 'creative_image_4', 'owner': 'acc', 'width': 300,
         'height': 250, 'image': 'test_creative.jpg'}
    ]

    setup = user_db
    setup.setup_creative_images(creatives)

    creative1 = Creative.objects_visible.get(name=creatives[0]['name'])
    creative1.appnexus_status = STATUS['rejected']
    creative1.appnexus_id = 1
    creative1.save()
    creative2 = Creative.objects_visible.get(name=creatives[1]['name'])
    creative2.appnexus_status = STATUS['audited']
    creative2.appnexus_id = 2
    creative2.save()
    creative3 = Creative.objects_visible.get(name=creatives[2]['name'])
    creative3.appnexus_status = STATUS['expired']
    creative3.appnexus_id = 3
    creative3.save()
    return creatives


@pytest.fixture
def creatives_reaudit_db(user_db, creatives_db):

    adverts = [
        {
            'name': 'ad_lemon',
            'strategy': 'Hello this is Citrus',
            'creative': 'creative_image_rejected',
            'url': 'http://www.google.com/',
        },
        {
            'name': 'ad_orange',
            'strategy': 'Hello this is Citrus',
            'creative': 'creative_image_audited',
            'url': 'http://www.wp.pl/',
        },
        {
            'name': 'ad_carrot',
            'strategy': 'han i has a pumpkin?',
            'creative': 'creative_image_expired',
            'url': 'http://www.google.com/',
        },
        {
            'name': 'ad_celery',
            'strategy': 'han i has a pumpkin?',
            'creative': 'creative_image_4',
            'url': 'http://www.wp.pl/',
        },
    ]

    setup = user_db
    setup.setup_landing_pages()
    setup.setup_campaigns()
    setup.setup_strategies()
    setup.setup_audiences()
    setup.setup_bidding_periods()
    setup.setup_adverts(adverts)
    call_command('rebuild_index', interactive=False)
    return setup


@pytest.fixture
def video_creatives_db(user_db):
    '''
    Both encoded and not encoded video creatives
    (not attached to any strategy).
    '''
    creatives = [
        {'name': NOTENCODED_CREATIVE_NAME, 'owner': 'acc',
         'file': 'creatives/creative.mpg'},
        {'name': ENCODED_CREATIVE_NAME, 'owner': 'acc',
         'file': 'creatives/creative.mpg', 'liverail_status': 'active'}
    ]

    setup = user_db
    setup.setup_creative_videos(creatives)

    return creatives


# Test helpers

def is_form_shown(client, header_text):
    title = client.get_content_elem('-t-title')
    return title.text == header_text


def split_attr(obj, attr='class'):
    return obj.get_attribute(attr).split()


# Tests
def test_check_list_creatives(client, creatives_db):
    '''
        Go to storage
        See three creatives in sidebar,
        Check their statuses: pending, audited and rejected
        visit each creatives page:
        see if their statuses match there
        go to new creative
    '''
    status_prefix = 'status-creative-'
    status_maps = {
        'creative_image_rejected': status_prefix + 'rejected',
        'creative_image_audited': status_prefix + 'audited',
        'creative_image_expired': status_prefix + 'expired',
        'creative_image_4': status_prefix + 'pending',
    }

    client.menu_jump_to('storage')

    creatives_ul = client.get_sidebar_elem('-t-creatives-list')
    creatives = creatives_ul.find_elements_by_tag_name('li')

    assert len(creatives) == len(creatives_db)

    for i, creative in enumerate(creatives):
        creative = client.get_sidebar_elem('-t-creatives-list') \
            .find_elements_by_tag_name('li')[i]
        creative_text = creative.text

        status = creative.find_element_by_class_name('-t-status')
        assert status_maps[creative.text] in split_attr(status)

        creative.click()

        client.wait_for_xhr()

        form_status = client.get_content_elem('-t-creative-status')
        assert status_maps[creative_text] in split_attr(form_status)


@pytest.mark.parametrize('filename, type', [
    ('creative.jpg', 'image'),
    ('creative.swf', 'flash'),
    ('creative.mpg', 'video')
])
def test_create_creative(client, creatives_db, filename, type):
    '''
        Go to storage
        click new creative
        upload file, check that the name is changed to image name
        save and see refreshed list of creatives
    '''
    creative_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'uploads', filename
    ))

    client.menu_jump_to('storage')

    client.click(client.find_element_by_class_name('-t-new-creative'))

    client.show_file_input('file')
    client.find_element_by_css_selector(
        '.-t-creative-upload input').send_keys(creative_path)
    client.wait_for_xhr()

    name_input = client.get_input('creative-name')

    client.check_input_value(name_input, filename)

    client.click_on_button('save')

    # and we're landing on a creative page
    creatives_ul = client.get_sidebar_elem('-t-creatives-list')
    creatives = creatives_ul.find_elements_by_tag_name('li')

    assert len(creatives) == len(creatives_db) + 1

    [new_creative] = filter(lambda c: c.text == filename, creatives)
    assert 'creative-' + type in split_attr(new_creative)

    status = client.get_content_elem('-t-creative-status')
    assert 'status-creative-pending' in split_attr(status)
    assert client.get_content_elem('-t-title').text == filename

    creative_db = Creative.objects.get(name=filename)
    assert creative_db.to_audit is False

    # Check if audit status is not changed to False after saving creative
    creative_db.to_audit = True
    creative_db.save()

    client.click_on_button('save')
    creative_db = Creative.objects.get(name=filename)
    assert creative_db.to_audit is True


def test_manual_audit(client, creatives_reaudit_db):
    """
    Sends creative to manual advert.
    Goes to creative that can be sent to re-audit.
    Sends, and check if creative has status changed to pending.
    """

    client.menu_jump_to('storage')

    audited = Creative.objects.get(name='creative_image_audited')
    expired = Creative.objects.get(name='creative_image_expired')
    rejected = Creative.objects.get(name='creative_image_rejected')

    for creative in [audited, expired, rejected]:
        client.get_sidebar_elem('-creative-' + str(creative.id)).click()
        client.wait_for_content()
        audit_button = client.get_content_elem('-t-force-audit')
        audit_button.click()
        client.wait_for_xhr()
        creative = Creative.objects.get(pk=creative.pk)
        assert creative.to_audit is True


def test_delete_creative(client, creatives_db):
    '''
    Go to storage
    Choose creative with rejected status
    delete and check if removed
    '''
    client.menu_jump_to('storage')

    client.click(client.get_sidebar_elem('status-creative-rejected'))

    creative_url = client.current_url

    client.click_on_button('delete')

    # assert we've been redirected
    assert not creative_url == client.current_url

    creatives_ul = client.get_sidebar_elem('-t-creatives-list')
    creatives = creatives_ul.find_elements_by_tag_name('li')
    assert len(creatives) == len(creatives_db) - 1


def test_video_creative_preview(client, video_creatives_db):
    """
    Go to storage.
    Choose encoded creative and check if preview is enabled.
    Choose not encoded one and check if preview is disabled.
    """

    encoded = Creative.objects.get(name=ENCODED_CREATIVE_NAME)
    encoded.liverail_status = 'active'
    encoded.save()
    not_encoded = Creative.objects.get(name=NOTENCODED_CREATIVE_NAME)
    client.menu_jump_to('storage')

    for creative, preview_enabled in [(encoded, True), (not_encoded, False)]:
        client.get_sidebar_elem('-creative-' + str(creative.id)).click()
        client.wait_for_content()
        preview_elements = client.find_elements_by_class_name('-vast-preview')

        if preview_enabled:
            assert len(preview_elements) == 1
        else:
            assert len(preview_elements) == 0
