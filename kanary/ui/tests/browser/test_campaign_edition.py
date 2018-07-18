from random import choice
from datetime import datetime, timedelta

from adserving.types import Decimal

from selenium.webdriver.support.select import Select

from ui.campaign.models import Campaign


ERRORS = {
    'name_required': 'Campaign name: This field is required.',
    'start_date_required': 'Start date: This field is required.',
    'start_hour_required': 'Start hour: This field is required.',
    'start_date_invalid': 'Start date: This is not a valid date',
    'start_hour_invalid': 'Start hour: This is not a valid hour',
    'start_date_bad_format': 'Start date: Date must be in DD-MM-YYYY format',
    'start_hour_bad_format': 'Start hour: Hour must be in HH:mm format',
    'end_date_required': 'End date: This field is required.',
    'end_hour_required': 'End hour: This field is required.',
    'end_date_invalid': 'End date: This is not a valid date',
    'end_hour_invalid': 'End hour: This is not a valid hour',
    'end_date_bad_format': 'End date: Date must be in DD-MM-YYYY format',
    'end_hour_bad_format': 'End hour: Hour must be in HH:mm format',
    'invalid_period': 'End date: Start date cannot be later than end',
    'landing_site_required': 'Default landing page: This field is required.',
    'budget_required': 'Total budget: This field is required.',
    'conversion_name_required': 'Conversion name: This field is required.',
    'conversion_value_required': 'Conversion value: This field is required.',
}


def go_to_campaign_step(client, step_class):
    client.menu_jump_to('campaigns')
    client.click_on_class('campaign-edit')
    client.click_on_class(step_class)


def save_and_return(client, step_class):
    '''
    Saves campaign and returns to a given step
    '''
    client.click_on_class('save-campaign')
    client.click_on_class('edit-campaign')
    client.click_on_class(step_class)


def save_with_errors(client):
    '''
    Tries to save invalid campaign.
    Returns errors listed in modal.
    '''
    client.click_on_class('save-campaign')
    client.wait_for_modal()
    return client.get_modal_errors()


def test_campaign_left_time(client, fill_db):
    '''
    Checks that campaign left time is based on UTC, not local time
    '''

    # Set campaign left time to 4 hours
    client.menu_jump_to('campaigns')
    campaign_button = client.find_element_by_class_name('-t-campaign')

    campaign_name = campaign_button.text
    campaign = Campaign.objects.get(name=campaign_name)
    campaign.start_UTC = datetime.utcnow()
    campaign.end_UTC = datetime.utcnow() + timedelta(hours=4)
    campaign.save()

    # Go to campaign details and check left time
    campaign_button.click()

    time_left = client.find_element_by_class_name('-t-time-left').text
    assert '4 hours left' in time_left


def test_edit_campaign_overall(client, fill_db):

    edited_campaign = {
        'name': 'This campaign makes sense',
        'new_hour': '15:00',
        'landing_page': 'http://clearcode.cc'
    }

    # Go to first campaign in edit mode
    go_to_campaign_step(client, 'overall')

    # Try to save campaign with empty name
    name_input = client.get_input('campaign-name')
    name_input.clear()

    client.click_on_class('save-campaign')

    # Check if modal has a proper errors
    client.wait_for_modal()

    assert ERRORS['name_required'] in client.get_modal_errors()
    assert client.has_class(name_input, 'input-error')

    client.close_modal()

    # Set proper name
    name_input.send_keys(edited_campaign['name'])

    # for date fields:
    for date_section in ['start', 'end']:
        container = client.find_element_by_class_name(
            '-t-controls-%s-date' % date_section
        )
        date_inputs = container.find_elements_by_tag_name('input')
        time_input = date_inputs[1]

        # empty fields, check errors
        time_input.clear()

        modal_errors = save_with_errors(client)

        assert ERRORS['%s_hour_required' % date_section] in modal_errors
        assert client.has_class(time_input, 'input-error')

        client.close_modal()

        # write invalid date and hour
        client.send_keys(time_input, '32:08')

        modal_errors = save_with_errors(client)

        assert ERRORS['%s_hour_invalid' % date_section] in modal_errors
        assert client.has_class(time_input, 'input-error')

        client.close_modal()

        # write invalid format
        client.send_keys(time_input, '18.15', clear=True)

        modal_errors = save_with_errors(client)

        assert ERRORS['%s_hour_bad_format' % date_section] in modal_errors
        assert client.has_class(time_input, 'input-error')

        client.close_modal()

        # write proper ones
        client.send_keys(time_input, edited_campaign['new_hour'], clear=True)

    # clear landing page
    client.send_keys('default-landing-page', '', clear=True)
    modal_errors = save_with_errors(client)

    assert ERRORS['landing_site_required'] in modal_errors

    client.close_modal()

    # proper one
    client.send_keys(
        'default-landing-page',
        edited_campaign['landing_page'],
        clear=True
    )

    # save campaign and return to edit mode
    client.click_on_class('save-campaign')
    client.click_on_class('edit-campaign')

    # check UI and DB.
    assert client.get_input('campaign-name').get_attribute('value') == edited_campaign['name']
    assert client.get_input('start-hour').get_attribute('value') == edited_campaign['new_hour']
    assert client.get_input('end-hour').get_attribute('value') == edited_campaign['new_hour']
    assert client.get_input('default-landing-page').get_attribute('value') == edited_campaign['landing_page']

    campaign = Campaign.objects.get(name=edited_campaign['name'])

    assert campaign.landing_site.url == edited_campaign['landing_page']


def test_edit_campaign_budget(client, fill_db):
    edited_campaign = {
        'budget_total': '10000.34',
    }

    go_to_campaign_step(client, 'budget')

    # Clear total budget
    budget_input = client.get_input('budget-total')
    budget_input.clear()

    modal_errors = save_with_errors(client)

    assert ERRORS['budget_required'] in modal_errors
    assert client.has_class(budget_input, 'input-error') is True

    client.close_modal()

    # Writing invalid values
    budget_input.send_keys('good morning')
    client.loose_focus()

    assert budget_input.get_attribute('value') == ''

    # Write proper value
    client.send_keys('budget-total', edited_campaign['budget_total'], clear=True)
    assert budget_input.get_attribute('value') == edited_campaign['budget_total']

    save_and_return(client, 'budget')

    # Check UI and DB
    assert client.get_input('budget-total').get_attribute('value') == edited_campaign['budget_total']

    campaign = Campaign.objects.get(name='I\'m a fruit')

    assert campaign.budget_total == Decimal(edited_campaign['budget_total'])


def test_edit_campain_conversion(client, fill_db):
    conv_data = {
        'name': 'Here comes the conversion',
        'value': '5',
    }

    go_to_campaign_step(client, 'conversion')

    for item in ('name', 'value'):
        # Clear input
        input = client.get_input('conversion-%s' % item)
        input.clear()

        modal_errors = save_with_errors(client)

        assert ERRORS['conversion_%s_required' % item] in modal_errors
        assert client.has_class(input, 'input-error') is True

        client.close_modal()

        # Write proper value
        client.send_keys(input, conv_data['%s' % item])

    save_and_return(client, 'conversion')

    # Check UI and DB
    assert client.get_input('conversion-name').get_attribute('value') == conv_data['name']
    assert client.get_input('conversion-value').get_attribute('value') == conv_data['value']

    campaign = Campaign.objects.get(name='I\'m a fruit')

    assert campaign.conversion_def.name == conv_data['name']
    assert campaign.conversion_def.value == Decimal(conv_data['value'])


def test_edit_campaign_capping(client, fill_db):
    PERIODS = ['hour', 'day', 'month', 'year']
    CAPPING_STEPS = ['campaign', 'strategy', 'creative']

    cap_data = {
        'campaign': {
            'checked': choice([True, False]),
            'cap_value': '1000',
            'period': choice(PERIODS)
        },
        'strategy': {
            'checked': choice([True, False]),
            'cap_value': '100',
            'period': choice(PERIODS)
        },
        'creative': {
            'checked': choice([True, False]),
            'cap_value': '10',
            'period': choice(PERIODS)
        },
    }

    def get_inputs_for_step(step):
        group = client.find_element_by_class_name('-t-%s-capping' % step)
        checkbox_group = client.find_element_by_class_name('-t-%s-checkbox' % step)

        select = Select(group.find_element_by_class_name('-t-select'))
        checkbox = checkbox_group.find_element_by_class_name('checkbox')
        cap_input = group.find_element_by_class_name('-t-cap-value')
        label_selector = '.-t-%s-capping-label' % step

        return (checkbox, cap_input, select, label_selector)

    go_to_campaign_step(client, 'capping')

    for step in CAPPING_STEPS:
        checkbox, cap_input, select, label_selector = get_inputs_for_step(step)

        if cap_data[step]['checked']:
            checkbox.click()

        select.select_by_value(cap_data[step]['period'])

        client.send_keys(cap_input, cap_data[step]['cap_value'],
            focus_css_selector=label_selector)

    save_and_return(client, 'capping')

    # Check UI and DB
    campaign = Campaign.objects.get(name='I\'m a fruit')

    for step in CAPPING_STEPS:
        checkbox, cap_input, select, _ = get_inputs_for_step(step)

        if cap_data[step]['checked']:
            assert client.has_class(checkbox, 'checked') is True
        else:
            assert client.has_not_class(checkbox, 'checked') is True

        assert cap_input.get_attribute('value') == cap_data[step]['cap_value']

        assert getattr(campaign, 'cap_%s_selected' % step) == cap_data[step]['checked']

        # Hacking inconsistent naming in model - sometimes it's total sometimes campaign :c
        if step == 'campaign':
            step_model = 'total'
        else:
            step_model = step

        assert getattr(campaign, 'cap_%s_period_presented' % step_model) == cap_data[step]['period']
        assert getattr(campaign, 'cap_%s_presented' % step_model) == int(cap_data[step]['cap_value'])
