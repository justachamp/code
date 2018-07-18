import os
from adserving.types import Decimal

import pytest

from ui.campaign.models import Strategy


TEST_STRATEGY = {
    'name': 'I\'ve become a drill',
    'budget': '2000',
    'bid': '1.00',
}


def check_highlight(client, class_name, highlight_class='current'):
    '''
    Checks if element that matches class_name has class responsible
    for highlighting this element.
    '''
    element = client.find_element_by_class_name(class_name)
    assert client.has_class(element, highlight_class) is True


def click_next(client):
    '''
    Performs a click of button 'Next'
    '''
    client.click_on_button('next')


def go_to_strategy_creator(client):
    client.get('/#campaigns')
    client.wait_for_xhr()

    campaign = client.find_element_by_class_name('-t-campaign')
    client.click(campaign)

    client.wait_until_displayed('-t-strategies')
    client.click(client.find_element_by_class_name('-t-button-new'))


def test_create_valid_strategy(client, fill_db):
    '''
    Log in.
    Go to campaigns list.
    Click first campaign.
    Click new strategy button.
    Each step: fill required fields and click 'next step'
    On final step: click 'save changes'
    Check if newly created strategy data are correct on redirect page
    (strategy details).
    Go to campaign detail page and check if strategy is on strategies list
    '''

    def find_by_text(elements, text):
        match = lambda el: el.text == text
        return filter(match, elements)[0]

    STORAGE_CREATIVE_NAME = fill_db.models['creative']['creative_image_1'].name
    UPLOADED_CREATIVE_NAME = 'creative.jpg'
    UPLOADED_CREATIVE_PATH = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'uploads', UPLOADED_CREATIVE_NAME
    ))
    creative_button = '.-t-button-creative-storage'

    go_to_strategy_creator(client)

    # Overall information
    client.wait_until_displayed('-t-form-overall')
    check_highlight(client, '-t-sidebar-overall')

    client.send_keys('name', TEST_STRATEGY['name'], clear=True)
    client.send_keys('budget', TEST_STRATEGY['budget'], clear=True)

    click_next(client)

    # Targeting
    client.wait_until_displayed('-t-targeting-container')
    check_highlight(client, '-t-sidebar-targeting')

    click_next(client)
    # Click next one more time to jump over publishers step
    click_next(client)

    # Landing pages
    client.wait_until_displayed('-t-lpages-container')
    check_highlight(client, '-t-sidebar-landing')

    client.click_on_button('add')

    client.send_keys('landing-page', 'http://www.onet.pl/')

    click_next(client)

    # Creatives
    client.wait_until_displayed('-t-creatives-container')
    check_highlight(client, '-t-sidebar-creatives')

    # From upload
    client.click_on_button('add')
    client.wait_until_displayed('-t-creatives-widget')
    client.show_file_input('file')
    client.find_element_by_css_selector(
        '.-t-creative-upload input').send_keys(UPLOADED_CREATIVE_PATH)
    client.wait_for_xhr()

    name_input = client.get_input('creative-name')

    client.check_input_value(name_input, UPLOADED_CREATIVE_NAME)

    # From storage
    client.click_on_button('add')

    client.wait_until_displayed('-t-creatives-widget')
    storage_button = client.find_elements_by_css_selector(creative_button)[1]
    storage_button.click()
    client.wait_for_tray('trayCreatives')

    creatives_li = client.find_elements_by_css_selector('.-creatives-list li')
    storage_creative = find_by_text(creatives_li, STORAGE_CREATIVE_NAME)
    assert creatives_li
    storage_creative.click()

    click_next(client)

    # Bidding
    client.wait_until_displayed('-t-bidding-container')
    check_highlight(client, '-t-sidebar-bidding')
    client.send_keys('bid', TEST_STRATEGY['bid'], clear=True)

    # Save new strategy
    client.click_on_button('save')

    # redirect on strategy detail page
    client.wait_until_displayed('-t-strategy-sidebar')

    # Check if strategy is saved with valid data
    name = client.find_element_by_class_name('-t-name').text
    budget = client.find_element_by_class_name('-t-budget').text
    bid = client.find_element_by_class_name('-t-bid').text
    creatives_li = client.find_elements_by_class_name('-t-creative-name')
    ui_creative_names = [cr.text for cr in creatives_li]

    db_creative_names = [
        STORAGE_CREATIVE_NAME,
        UPLOADED_CREATIVE_NAME,
    ]

    assert name == TEST_STRATEGY['name']
    assert float(budget) == float(TEST_STRATEGY['budget'])
    assert bid == TEST_STRATEGY['bid']
    assert sorted(ui_creative_names) == sorted(db_creative_names)

    # Database checking
    strategy = Strategy.objects.get(name=TEST_STRATEGY['name'])

    assert strategy.name == TEST_STRATEGY['name']
    assert strategy.budget_total == Decimal(TEST_STRATEGY['budget'])
    assert strategy.budget_bid_CPM == Decimal(TEST_STRATEGY['bid'])


@pytest.mark.usefixtures('fill_db')
def test_create_invalid_strategy(client):
    '''
    Tries to save empty strategy, and checks if modal is displayed and can
    be clicked.
    '''

    go_to_strategy_creator(client)

    client.click_on_button('save-changes')
    client.wait_for_tray('modal')

    # Check if modal is opened
    modal = client.find_element_by_id('modal')
    assert client.has_class(modal, 'in') is True

    # Close modal
    client.click_on_class('close-modal')

    # Check if modal was closed
    assert client.has_not_class(modal, 'in') is True
