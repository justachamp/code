import pytest
from ui.storage.models import Audience
from ui.tests.initial_datafixtures import default_audiences
TEST_AUDIENCE = default_audiences[0]


@pytest.fixture
def audiences_db(user_db):
    '''Initializes database with data needed by audiences'''

    setup = user_db
    setup.setup_audiences()
    return setup


def go_to_audiences(client):
    client.menu_jump_to('storage')
    client.click_on_class('audiences-tab')


@pytest.mark.usefixtures('audiences_db')
def test_check_list_audiences(client):
    go_to_audiences(client)

    audiences_from_db = [a.name for a in Audience.objects.all()]
    audiences_ul = client.get_sidebar_elem('-t-audiences-list')
    audiences_li = audiences_ul.find_elements_by_tag_name('li')
    audience_sidebar_names = [a.text for a in audiences_li]

    assert sorted(audience_sidebar_names) == sorted(audiences_from_db)


def test_create_audience(client):
    saved_audiences_count = len(Audience.objects.all())
    assert saved_audiences_count == 0

    go_to_audiences(client)
    client.click_on_class('new-audience')
    client.send_keys('audience-name', TEST_AUDIENCE['name'], clear=True, focus_css_selector=False)
    client.click_on_button('save')
    name_input = client.get_input('audience-name')
    client.check_input_value(name_input, TEST_AUDIENCE['name'])

    saved_audiences_count = len(Audience.objects.all())
    assert saved_audiences_count == 1
    assert Audience.objects.filter(name=TEST_AUDIENCE['name']).exists()


@pytest.mark.usefixtures('audiences_db')
def test_edit_audience(client):
    '''
    Changes name of an audience and checks if it is saved correctly
    '''
    def find_matching_element(elements, text):
        match = lambda el: el.find_element_by_css_selector('span').text == text
        return filter(match, elements)

    audiences_li_selector = '.-t-audiences-list li'
    go_to_audiences(client)
    audiences_li = client.find_elements_by_css_selector(audiences_li_selector)

    # Select first audience and store old name
    selected_audience = audiences_li[0]
    old_name = selected_audience.text
    new_name = 'Updated audience'

    # Check if an audience with new name doesn't exist
    # and if there is only one audience with old name
    audiences_li = client.find_elements_by_css_selector(audiences_li_selector)
    old_name_audiences = find_matching_element(audiences_li, old_name)
    new_name_audiences = find_matching_element(audiences_li, new_name)

    assert len(old_name_audiences) == 1
    assert len(new_name_audiences) == 0

    client.click(selected_audience)

    # Change name
    client.send_keys('audience-name', new_name, clear=True, focus_css_selector='div.-t-input-audience label')
    client.click_on_button('save')

    # Check if name has changed in details view
    name_input = client.get_input('audience-name')
    client.check_input_value(name_input, new_name)

    # Check if name has changed in list view
    audiences_li = client.find_elements_by_css_selector(audiences_li_selector)
    old_name_audiences = find_matching_element(audiences_li, old_name)
    new_name_audiences = find_matching_element(audiences_li, new_name)

    assert len(old_name_audiences) == 0
    assert len(new_name_audiences) == 1

    assert len(Audience.objects.filter(name=new_name)) == 1
    assert Audience.objects.filter(name=old_name).exists() is False


@pytest.mark.usefixtures('audiences_db')
def test_delete_audience(client):
    go_to_audiences(client)

    audiences_from_db = [a.name for a in Audience.objects.all()]
    audiences_ul = client.get_sidebar_elem('-t-audiences-list')
    first_audience = audiences_ul.find_elements_by_tag_name('li')[0]
    client.click(first_audience)
    audience_url = client.current_url
    client.click_on_button('delete')

    assert not audience_url == client.current_url

    audiences_li = audiences_ul.find_elements_by_tag_name('li')

    assert len(audiences_li) == len(audiences_from_db) - 1
