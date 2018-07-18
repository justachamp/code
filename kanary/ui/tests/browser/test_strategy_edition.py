import os
from random import choice

import pytest

from selenium.webdriver.support.select import Select

from adserving.types import Decimal
from adserving.optimizer.metrics import OPTIMIZATION_METRICS, CPC

from ui.campaign.models import Strategy, Advert
from ui.tests.browser import utils_strategy as utils
from ui.tests.browser.page.strategy import StrategyPage


SITE_ERROR = 'Creatives: some urls have incorrect format'


def go_to_strategy_edition(client):
    '''
    Edit first strategy in first campaign
    '''

    # go to campaigns (main menu)
    client.menu_jump_to('campaigns')

    # click on first campaign
    client.click_on_class('campaign')

    # click on first strategy
    client.click_on_class('strategy')

    # click edit button
    client.click_on_class('edit-strategy')


def get_adverts_data(client):
    '''
    Returns list of ads info currently saved in strategy
    '''
    adverts_data = []

    adverts = client.find_elements_by_class_name('-t-creatives-widget')

    for advert in adverts:
        info = {}
        info['name'] = advert.find_element_by_class_name(
            '-t-input-creative-name'
        ).get_attribute('value')

        info['landing_site'] = advert.find_element_by_class_name(
            '-t-input-landing-site'
        ).get_attribute('value')

        info['js-code'] = advert.find_element_by_class_name(
            '-t-input-js-code'
        ).get_attribute('value')

        adverts_data.append(info)

    return adverts_data


def add_bid_periods(client, periods):
    '''
    Add bid period to the strategy based on periods data
    :param periods tuple: periods data with following structure:
                          ('valuefrom', 'value_to')
    '''
    for start, end in periods:
        client.send_keys('from', start, clear=True)
        client.send_keys('to', end, clear=True)
        client.click_on_class('add-period')


def remove_bid_period(client, period_val):
    '''
    Removes given bid period from strategy
    :param period_val string: period value in format 'hh:mm - hh:mm'
    '''
    periods = client.find_elements_by_class_name('-t-bidding-period')
    for period in periods:
        value = period.find_element_by_class_name('-t-period-value').get_attribute('value')
        if value == period_val:
            remove_btn = period.find_element_by_class_name('-t-remove-period')
            remove_btn.location_once_scrolled_into_view
            remove_btn.click()


def test_strategy_overall(client, fill_db):
    '''
    Tries to save strategy without required fields,
    Check errors and fill inputs with proper data.
    Saves strategy and checks UI and DB.
    '''
    EDITED_STRATEGY = {
        'name': 'Strategy Edited',
        'budget': '50',
        'budget-daily': '20',
    }

    ERRORS = {
        'name_required': 'Strategy name: This field is required.',
        'budget_required': 'Total strategy budget: This field is required.',
    }

    INPUTS = ['name', 'budget', 'budget-daily']

    utils.go_to_step(client, 'overall', existing=True)

    # Clear all inputs
    for input_name in INPUTS:
        client.get_input(input_name).clear()

    # Try to save and check if correct errors are displayed
    client.click_on_class('button-save-changes')
    client.wait_for_modal()
    modal_errors = client.get_modal_errors()

    assert len(modal_errors) == len(ERRORS)
    for key in ERRORS.keys():
        assert ERRORS[key] in modal_errors

    client.close_modal()

    # Fill inputs with proper data
    for input_name in INPUTS:
        client.send_keys(input_name, EDITED_STRATEGY[input_name])

    # Save again and check UI and DB
    utils.save_and_return_to_step(client)

    for input_name in INPUTS:
        assert client.get_input_val(input_name) == EDITED_STRATEGY[input_name]

    strategy = Strategy.objects.all()[0]

    assert strategy.name == EDITED_STRATEGY['name']
    assert strategy.budget_total == Decimal(EDITED_STRATEGY['budget'])
    assert strategy.budget_daily == Decimal(EDITED_STRATEGY['budget-daily'])


def test_landing_pages_incorrect(client, fill_db):
    '''
        Inserts invalid or none landing pages,
        checks if validation errors are raised
    '''
    def get_row_count():
        return len(client.find_elements_by_class_name('-t-landing-page-row'))

    ERRORS = {
        'landing_page_invalid_format': 'Landing pages: some landing pages are in incorrect format.'
    }

    empty_page_count = 2

    utils.go_to_step(client, 'landing', existing=True)

    client.implicitly_wait(1)

    # Remove all lading pages
    input_row_class = '-t-landing-page-row'
    input_rows = client.find_elements_by_class_name(input_row_class)
    for row in input_rows:
        row_count_before = get_row_count()
        client.click(client.find_element_by_class_name('remove'))
        row_count_after = get_row_count()

    # Add empty landing pages and check if they are saved correctly
    for index in range(0, empty_page_count):
        row_count_before = get_row_count()
        client.click_on_button('add')
        row_count_after = get_row_count()
        assert row_count_after == row_count_before + 1

    # Check if validation rejects empty urls
    modal_errors = utils.save_with_errors(client)
    assert ERRORS['landing_page_invalid_format'] in modal_errors


def test_landing_pages_correct(client, fill_db):
    '''
        Inserts valid landing pages data,
        checks if they are saved and displayed correctly
    '''

    correct_landing_pages = [
        {'url': 'http://www.wykop.pl', 'weight': 10},
        {'url': 'http://www.gazeta.pl', 'weight': 30},
    ]
    utils.go_to_step(client, 'landing', existing=True)

    client.implicitly_wait(1)

    # Remove all lading pages and test if validation error is raised on save
    input_row_class = '-t-landing-page-row'
    input_rows = client.find_elements_by_class_name(input_row_class)
    for row in input_rows:
        client.click(client.find_element_by_class_name('remove'))

    for index in range(0, len(correct_landing_pages)):
        client.click_on_button('add')

    input_rows = client.find_elements_by_class_name(input_row_class)
    page_class = '-t-input-landing-page'
    weight_class = '-t-input-weight'
    for i, page in enumerate(correct_landing_pages):
        row = input_rows[i]
        url_input = row.find_element_by_class_name(page_class)
        weight_input = row.find_element_by_class_name(weight_class)
        url_input.clear()
        weight_input.clear()
        url_input.send_keys(page['url'])
        weight_input.send_keys(page['weight'])

    utils.save_and_return_to_step(client)

    strategy = Strategy.objects.all()[0]
    landing_pages = strategy.landing_sites.all()

    assert len(landing_pages) == len(correct_landing_pages)

    # Check sites in DB
    for page in correct_landing_pages:
        match_url_and_ratio = lambda el: (el.site.url == page['url']) and (el.ratio == page['weight'])
        matched_sites = filter(match_url_and_ratio, landing_pages)
        assert len(matched_sites) == 1

    # Check sites in UI
    input_rows = client.find_elements_by_class_name(input_row_class)
    for row in input_rows:
        displayed_url = row.find_element_by_class_name(page_class).get_attribute('value')
        displayed_weight = row.find_element_by_class_name(weight_class).get_attribute('value')
        match_url_and_ratio = lambda el: (el['url'] == displayed_url) and (str(el['weight']) == displayed_weight)
        matched_sites = filter(match_url_and_ratio, correct_landing_pages)
        assert len(matched_sites) == 1


def test_creative_edit(client, fill_db):
    CREATIVE = {
        'landing_site': 'http://test.site.com',
        'JSCode': 'console.log("no code tehre")',
    }

    utils.go_to_step(client, 'creatives', existing=True)

    # Edit first of creatives (choose one from storage)
    client.click_on_button('creative-storage')
    client.wait_for_tray('trayCreatives')
    creatives = client.find_elements_by_css_selector('.-creatives-list li')

    # check random creative from tray
    creative = choice(creatives)
    creative.click()

    CREATIVE['name'] = creative.text

    # Try to type invalid site
    client.send_keys('landing-site', 'not a site in fact', clear=True)
    client.click_on_class('button-save-changes')

    client.wait_for_modal()

    assert SITE_ERROR in client.get_modal_errors()

    client.close_modal()

    # Change landing site and jscode for proper ones
    client.send_keys('landing-site', CREATIVE['landing_site'], clear=True)
    # Show custom tracker
    client.click_on_class('show-js-code-input')
    client.send_keys('js-code', CREATIVE['JSCode'], clear=True, focus_css_selector=False)

    # save strategy and return to the creatives
    utils.save_and_return_to_step(client)

    # check UI and DB
    assert CREATIVE['name'] == client.get_input('creative-name').get_attribute('value')
    assert CREATIVE['landing_site'] == client.get_input('landing-site').get_attribute('value')
    assert CREATIVE['JSCode'] == client.get_input('js-code').get_attribute('value')

    strategy = Strategy.objects.all()[0]

    adverts = strategy.advert_set.filter(
        is_deleted=False,
        creative__name=CREATIVE['name'],
        landing_site__url=CREATIVE['landing_site'],
        js_code=CREATIVE['JSCode']
    )

    assert adverts.count() == 1


def test_add_creative_custom_tracker_tracking_pixel(client, fill_db):
    '''
    Test Custom Pixel and JS Code textareas' states interaction and validation of
    Custom Pixel URL.
    Both textareas are hidden by default.
    '''
    JS_CODE = '   (function(){     }());   '
    PIXEL_URL = ' http://pixel.example.com   '

    utils.go_to_step(client, 'creatives', existing=True)
    creative_edit = StrategyPage(client)

    # The labels should have default values for empty textareas.
    assert creative_edit.js_code_label.text == 'Add tracking'
    assert creative_edit.custom_pixel_label.text == 'Add tracking'
    creative_edit.assert_both_textareas_hidden()

    creative_edit.check_toggling()  # No input - should toggle freely.

    # 1. Add whitespace to both inputs. It should be ignored. Test label text (Add/Hide).
    creative_edit.show_js_code()
    creative_edit.js_code.send_keys(' \n\n ')
    creative_edit.show_custom_pixel()  # Close JS code textarea and open custom pixel.
    creative_edit.custom_pixel.send_keys(' \n\n ')
    creative_edit.hide_custom_pixel()

    creative_edit.check_toggling()  # Whitespace-only input should be ignored and toggling should be possible.

    # 2. Add some non-whitespace chars to the custom pixel input. It should not be possible to
    # switch the textarea now. It should be possible to hide it.
    creative_edit.show_js_code()
    creative_edit.js_code.send_keys(JS_CODE)  # Will also contain prevoiusly inserted whitespace - that's OK.
    # Now it should not be possible to open the other textarea.
    creative_edit.show_custom_pixel(should_fail=True)
    creative_edit.hide_js_code()
    # With JS code hidden try to open custom pixel textarea again:
    creative_edit.show_custom_pixel(should_fail=True)

    # 3. Save the campaign. JS code should be stripped and saved.
    utils.save_and_return_to_step(client)
    creative_edit.refresh()
    creative_edit.assert_both_textareas_hidden()
    creative_edit.show_js_code()
    assert creative_edit.js_code.get_attribute('value') == JS_CODE.strip()

    # 4. Entering custom pixel should fail because we have JS code inserted.
    creative_edit.show_custom_pixel(should_fail=True)
    creative_edit.js_code.clear()  # Clear JS code textarea.
    assert creative_edit.js_code.get_attribute('value') == ''

    # 5. Now with JS code empty it should be possible to insert custom tracker.
    creative_edit.show_custom_pixel()
    creative_edit.custom_pixel.send_keys('My home page')  # Invalid URL.
    creative_edit.show_js_code(should_fail=True)
    creative_edit.hide_custom_pixel()

    client.click_on_class('button-save-changes')
    # Error modal should appear. Handle the error.
    client.wait_for_modal()
    assert SITE_ERROR in client.get_modal_errors()
    client.close_modal()
    assert 'input-error' in creative_edit.custom_pixel.get_attribute('class')

    creative_edit.show_custom_pixel()
    creative_edit.custom_pixel.clear()
    creative_edit.custom_pixel.send_keys(PIXEL_URL)  # Insert a valid URL.

    utils.save_and_return_to_step(client)
    creative_edit.refresh()
    creative_edit.assert_both_textareas_hidden()

    creative_edit.show_custom_pixel()
    assert creative_edit.custom_pixel.get_attribute('value') == PIXEL_URL.strip()


@pytest.fixture
def video_db(fill_db):
    setup = fill_db
    setup.setup_creative_videos()
    return setup


def test_add_video_creative(client, video_db):
    """Checks saving strategy with video creative"""
    VIDEO_CREATIVE_NAME = 'creative_video_1'
    utils.go_to_step(client, 'creatives', existing=True)

    creative_edit = StrategyPage(client)

    # Check if both trackers are hidden
    creative_edit.assert_both_textareas_hidden()

    # Add a custom JS tracker
    creative_edit.show_js_code()
    creative_edit.js_code.send_keys('console.log("some tracker")')

    # Choose video creative from storage, check if its name is displayed in input
    creative_edit.remove_button.click()
    creative_edit.select_creative_from_tray(VIDEO_CREATIVE_NAME)
    creative_edit.check_name(VIDEO_CREATIVE_NAME)

    # Custom JS tracker should be cleared and disabled
    creative_edit.show_js_code(should_fail=True)
    assert creative_edit.js_code.get_attribute('value') == ''

    # Save and check if changes have been saved
    utils.save_and_return_to_step(client)

    creative_edit.refresh()
    creative_edit.check_name(VIDEO_CREATIVE_NAME)

    strategy_name = client.find_element_by_class_name('-t-name').text
    strategy = Strategy.objects.get(name=strategy_name)

    adverts = strategy.advert_set.filter(
        is_deleted=False,
        creative__name=VIDEO_CREATIVE_NAME
    )

    assert adverts.count() == 1


def test_add_creative_without_site(client, fill_db):
    '''
    Checks if when we save advert without custom landing page,
    no Site object related to advert is saved to db.
    '''
    utils.go_to_step(client, 'creatives', existing=True)

    client.click_on_button('add')

    container = client.find_elements_by_class_name('-t-creatives-widget')[-1]
    add_creative_btn = container.find_element_by_class_name('-t-button-creative-storage')
    client.click(add_creative_btn)

    client.wait_for_tray('trayCreatives')
    creatives = client.find_elements_by_css_selector('.-creatives-list li')

    # check random creative from tray
    creative = choice(creatives)
    creative.click()

    creative_name = creative.text

    # save strategy and return to the creatives
    utils.save_and_return_to_step(client)

    # check db if advert without Site object is created
    strategy = Strategy.objects.all()[0]

    adverts = strategy.advert_set.filter(
        is_deleted=False,
        creative__name=creative_name,
        landing_site__isnull=True
    )

    assert adverts.count() == 1


def test_creative_delete(client, fill_db):
    REMOVED_CREATIVE = {}

    utils.go_to_step(client, 'creatives', existing=True)
    client.wait_until_displayed('-t-creatives-container')

    # Store info about first add in strategy
    REMOVED_CREATIVE['name'] = client.get_input('creative-name').get_attribute('value')
    REMOVED_CREATIVE['landing_site'] = client.get_input('landing-site').get_attribute('value')
    REMOVED_CREATIVE['js-code'] = client.get_input('js-code').get_attribute('value')

    # Remove first ad
    client.click_on_class('remove-ad')

    # Save strategy
    utils.save_and_return_to_step(client)

    # Check UI and db
    adverts_data = get_adverts_data(client)

    assert REMOVED_CREATIVE not in adverts_data

    strategy = Strategy.objects.all()[0]

    removed_adverts = strategy.advert_set.filter(
        is_deleted=True,
        creative__name=REMOVED_CREATIVE['name'],
        landing_site__url=REMOVED_CREATIVE['landing_site'],
        js_code=REMOVED_CREATIVE['js-code']
    )

    assert removed_adverts.count() == 1


@pytest.mark.parametrize('creative_name, creative_type', [
    ('creative.jpg', 'Image'),
    ('creative.swf', 'Flash'),
    ('creative.mpg', 'Video')
])
def test_upload_creative(client, fill_db, creative_name, creative_type):
    """Upload creative from strategy edit"""
    CREATIVE_PATH = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'uploads', creative_name
    ))
    utils.go_to_step(client, 'creatives', existing=True)

    strategy_name = client.find_element_by_class_name('-t-name').text
    strategy = Strategy.objects.get(name=strategy_name)

    # Creative with this name should not exist
    with pytest.raises(Advert.DoesNotExist):
        strategy.advert_set.get(
            is_deleted=False,
            creative__name=creative_name
        )

    creative_edit = StrategyPage(client)
    creative_edit.remove_button.click()

    # Upload file and check if its name is displayed in form
    creative_edit.upload_file(CREATIVE_PATH)

    def file_name_updated():
        return creative_edit.file_name.get_attribute('value') == creative_name
    client.wait_until(file_name_updated)

    # Save and check if creative has been created
    utils.save_and_return_to_step(client)

    creative_edit.refresh()
    creative_edit.check_name(creative_name)

    advert = strategy.advert_set.get(
        is_deleted=False,
        creative__name=creative_name
    )
    assert advert.creative.type == creative_type


def set_creative_bid_values(client, BID_MAPPING):
    """
    :param ui.tests.browser.utils.Client client: selenium client
    :param dict BID_MAPPING: look at :func:`test_bidding_step`
    """
    # for each creative choose another bid type
    for box in client.find_elements_by_class_name('-t-advert-box'):
        creative_name_element = box.find_element_by_class_name('-t-name')
        creative_name_element.location_once_scrolled_into_view
        name = creative_name_element.text
        select = Select(box.find_element_by_class_name('-t-select'))

        select.select_by_value(BID_MAPPING[name]['type'])

        # set custom bid value
        if BID_MAPPING[name]['type'] == 'custom':
            client.send_keys('custom-val', BID_MAPPING[name]['value'], clear=True)

        # set value for day parting
        if BID_MAPPING[name]['type'] == 'day_parting':
            for input_elem in client.find_elements_by_class_name('-t-day-parted-val'):
                input_elem.location_once_scrolled_into_view
                input_elem.clear()
                input_elem.send_keys(BID_MAPPING[name]['value'])


def check_creative_bid_values(client, BID_MAPPING):
    """
    :param ui.tests.browser.utils.Client client: selenium client
    :param dict BID_MAPPING: look at :func:`test_bidding_step`
    """
    # check if UI is populated correctly
    for box in client.find_elements_by_class_name('-t-advert-box'):
        name_el = box.find_element_by_class_name('-t-name')
        name_el.location_once_scrolled_into_view
        name = name_el.text
        select = Select(box.find_element_by_class_name('-t-select'))

        if BID_MAPPING[name]['type'] == 'default':
            assert name == 'Creative Default'
            assert select.first_selected_option.get_attribute('value') == 'default'

        if BID_MAPPING[name]['type'] == 'custom':
            assert name == 'Creative Custom'
            assert select.first_selected_option.get_attribute('value') == 'custom'
            assert client.get_input_val('custom-val') == BID_MAPPING[name]['value']

        if BID_MAPPING[name]['type'] == 'day_parting':
            assert name == 'Creative Parted'
            assert select.first_selected_option.get_attribute('value') == 'day_parting'
            for input_elem in client.find_elements_by_class_name('-t-day-parted-val'):
                assert input_elem.get_attribute('value') == BID_MAPPING[name]['value']


def check_strategy_adverts_in_database(strategy, adverts, BID_MAPPING, BID_PERIODS):
    """
    :param ui.campaign.models.Strategy strategy: strategy model
    :param list adverts: list of adverts
    :param dict BID_MAPPING: look at :func:`test_bidding_step`
    """
    for period in strategy.biddingperiod_set.all():
        # checking unicode to avoid checking dicts equality or datetimes
        # it is nice representation of how period is saved.
        assert unicode(period) in BID_PERIODS

    for advert in adverts:
        if BID_MAPPING[advert.creative.name] in ['Creative Default', 'Creative Custom']:
            assert advert.status == BID_MAPPING[advert.creative.name]['type']
            assert advert.custom_bid_CPM == BID_MAPPING[advert.creative.name]['value']

        if BID_MAPPING[advert.creative.name] == 'Creative Parted':
            assert advert.status == 'day_parting'
            for period in advert.advertperiod_set.all():
                assert period.custom_bid_CPM == BID_MAPPING[advert.creative.name]['value']
                assert unicode(period) in BID_PERIODS


def test_bidding_step(client, bidding_db):
    OVERLAP_ERROR = "Bidding: bidding periods can't overlap each other."
    END_BEFORE_START_ERROR = "Bidding: period start can't be later than end."
    QUARTERS_ERROR = 'Bidding: Minutes must be multiples of quarter of an hour.'
    BID_REQUIRED_ERROR = 'Default CPM bid: This field is required.'

    BID_PRICE = '0.50'
    BID_PERIODS = ['08:00:00 - 12:00:00', '12:45:00 - 13:15:00', '13:15:00 - 13:30:00']

    BID_MAPPING = {
        'Creative Default': {
            'type': 'default'
        },
        'Creative Custom': {
            'type': 'custom',
            'value': '2'
        },
        'Creative Parted': {
            'type': 'day_parting',
            'value': '1.50'
        }
    }

    utils.go_to_step(client, 'bidding', existing=True)

    client.wait_until_displayed('-t-bidding-container')
    client.get_input('bid').clear()
    client.click_on_class('enable-dayparting')

    add_bid_periods(client, [
        ('08:00', '12:00'),
        ('12:45', '13:15'),
        ('13:00', '13:15'),  # Overlapping periods
        ('13:15', '13:30'),
        ('14:00', '14:59'),  # Minutes not multiple of 15
        ('17:00', '00:00')  # End before start
    ])

    client.click_on_class('button-save')

    client.wait_for_modal()
    # Check if notification about default bid is shown
    assert BID_REQUIRED_ERROR in client.get_modal_errors()
    # Check if overlapping is detected
    assert OVERLAP_ERROR in client.get_modal_errors()
    # Check if end before start is detected
    assert END_BEFORE_START_ERROR in client.get_modal_errors()
    # Check if not quarter multiple minutes are detected
    assert QUARTERS_ERROR in client.get_modal_errors()
    client.close_modal()

    # Set default bid
    client.send_keys('bid', BID_PRICE)

    # Remove invalid periods
    remove_bid_period(client, '13:00 - 13:15')
    remove_bid_period(client, '14:00 - 14:59')
    remove_bid_period(client, '17:00 - 00:00')

    set_creative_bid_values(client, BID_MAPPING)

    # save strategy
    utils.save_and_return_to_step(client)

    check_creative_bid_values(client, BID_MAPPING)

    # check database
    strategy = Strategy.objects.all()[0]
    adverts = strategy.advert_set.all()
    check_strategy_adverts_in_database(
        strategy, adverts, BID_MAPPING, BID_PERIODS
    )

    # check if creative prated value is zero
    # is should be zero.
    BID_MAPPING["Creative Parted"]["value"] = '0'

    set_creative_bid_values(client, BID_MAPPING)

    # save strategy
    utils.save_and_return_to_step(client)

    check_creative_bid_values(client, BID_MAPPING)

    # check database
    strategy = Strategy.objects.all()[0]
    adverts = strategy.advert_set.all()
    assert strategy.budget_bid_CPM == Decimal(BID_PRICE)
    assert strategy.is_automatically_bidded is False
    assert strategy.optimized_metric is None
    check_strategy_adverts_in_database(
        strategy, adverts, BID_MAPPING, BID_PERIODS
    )


def test_automatic_bidding(client, bidding_db):
    """Check automatic bidding behaviour."""

    utils.go_to_step(client, 'bidding', existing=True)

    # Check automatic bid price
    client.click_on_class('automatic-bid-price')

    utils.save_and_return_to_step(client)

    strategy = Strategy.objects.all()[0]
    strategy_pk = strategy.pk
    assert strategy.is_automatically_bidded is True
    assert strategy.optimized_metric == CPC.__name__

    # move default metric to the end.
    metrics = list(OPTIMIZATION_METRICS)
    if metrics[0][0] == strategy.optimized_metric:
        cpc_metric = metrics.pop(0)
        metrics.append(cpc_metric)

    for metric, description in metrics:
        # let us check description first if correct
        element_description = client.get_content_elem('-metric-description-' + metric.lower())
        assert client.get_by_tagname(element_description, 'span').text == description
        assert client.get_by_tagname(element_description, 'strong').text == metric

        # first metric will be set up, we'll go to others first to check,
        # and first should be checked last one
        control_element = client.get_content_elem('-controls-' + metric.lower())
        client.click(client.get_by_tagname(control_element, 'span'))
        utils.save_and_return_to_step(client)

        strategy = Strategy.objects.get(pk=strategy_pk)
        assert strategy.is_automatically_bidded is True
        assert strategy.optimized_metric == metric
