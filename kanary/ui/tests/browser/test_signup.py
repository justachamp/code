import pytest

from django.core import mail
from django.core.urlresolvers import reverse

from ui.tests.initial_datafixtures import inactive_user
from ui.tests.browser.page import SignupForm, LoginForm, CreateProfileForm

from ui.account.models import User


def login_user(client, user_data):
    '''
    Helper function for filling and submitting login form
    '''
    login_form = LoginForm(client)

    login_form.fill_inputs(
        username=inactive_user[0]['username'],
        password=inactive_user[0]['password']
    )

    login_form.submit()


@pytest.mark.skipif(True, reason='KANARY-1860')
def test_inactive_user_creation(base_client):
    '''
    Creates inactive user and checks if she has access only to profile form.
    Also checks if welcoming mail was sent.
    '''
    mail.outbox = []

    NEW_USER_DATA = {
        'email': 'inactive@user.com',
        'password': 'imsoinactive'
    }
    # Go to signup form
    base_client.find_element_by_class_name('-t-signup-link').click()

    signup_form = SignupForm(base_client)

    signup_form.fill_inputs(**NEW_USER_DATA)
    signup_form.submit()

    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == 'Welcome to Kanary'

    new_user = User.objects.get(username=NEW_USER_DATA['email'])

    assert new_user.is_signup_complete is False
    assert base_client.current_path == reverse('create_profile')

    # Try to redirect to next creator step or main app.
    # User always should be redirected to the 'create_profile' page
    for view_name in ['setup_complete', 'main']:
        base_client.get_nowait(reverse(view_name))
        assert base_client.current_path == reverse('create_profile')


@pytest.mark.skipif(True, reason='KANARY-1860')
def test_signup_flow(base_client, inactive_user_db):
    '''
    Logs in inactive user and goes through all signup steps.
    '''
    login_user(base_client, inactive_user)

    profile_form = CreateProfileForm(base_client)

    # try to save empty form
    profile_form.submit()
    profile_form.refresh()

    # check validation
    INVALID_INPUTS = ['company_name', 'first_name', 'last_name', 'address',
    'city', 'zip_code', 'phone']

    assert sorted(profile_form.get_invalid_inputs()) == sorted(INVALID_INPUTS)

    # fill proper data
    PROFILE_DATA = {
        'is_agency': True,
        'company_name': 'Test Company',
        'first_name': 'Name',
        'last_name': 'Last',
        'address': 'street 2/3',
        'city': 'London',
        'zip_code': '00-210',
        'phone': '234-123-566',
        'country': 'US',
        'province': 'US-CO'
    }
    profile_form.fill_form(**PROFILE_DATA)

    profile_form.submit()

    # Check if we land on setup comlete page and go to main app
    assert base_client.current_path == reverse('charge_account')
    base_client.find_element_by_class_name('-t-next').click()

    assert base_client.current_path == reverse('setup_complete')
    base_client.find_element_by_class_name('-t-go-to-main').click()

    assert base_client.current_path == reverse('main')

    # Check if data are saved and user is active now
    user = User.objects.get(username=inactive_user[0]['username'])

    assert user.is_signup_complete is True

    for field, value in PROFILE_DATA.items():
        assert getattr(user.account, field) == value


@pytest.mark.skipif(True, reason='KANARY-1860')
def test_signup_form_data_persistency(base_client, inactive_user_db):
    '''
    Checks if data in profile form are stored even
    when user logout before completing whole form.
    '''
    login_user(base_client, inactive_user)

    profile_form = CreateProfileForm(base_client)

    INCOMPLETE_DATA = {
        'is_agency': True,
        'company_name': 'Incomplete One',
        'country': 'US'
    }
    profile_form.fill_form(**INCOMPLETE_DATA)
    profile_form.submit()

    user = User.objects.get(username=inactive_user[0]['username'])

    assert user.is_signup_complete is False

    # Check if incomplete data are saved to db
    for field, value in INCOMPLETE_DATA.items():
        assert getattr(user.account, field) == value

    # Log user out and back in
    base_client.get_nowait(reverse('auth-logout'))
    login_user(base_client, inactive_user)

    profile_form.refresh()

    # Check if incomplete data are still persisted within profile form
    assert 'checked' in profile_form.is_agency_checkbox.get_attribute('class')
    assert profile_form.company_name_input.get_attribute('value') == INCOMPLETE_DATA['company_name']
    assert profile_form.country_select.all_selected_options[0] \
           .get_attribute('value') == INCOMPLETE_DATA['country']
