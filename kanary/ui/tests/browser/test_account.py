
from ui.account.models import User

from ui.tests.initial_datafixtures import default_user


DEFAULT_USERNAME = default_user[0]['username']
DEFAULT_PASSWORD = default_user[0]['password']


def test_account_information(client, fill_db):
    '''
    Checks if correct data are displayed for logged in user
    in Account Information section.
    '''
    client.menu_jump_to('account')

    user = fill_db.models['user'][DEFAULT_USERNAME]

    assert int(client.get_content_elem('-t-account-number').text) == user.account.account_number
    assert client.get_input_val('email') == user.email


def test_change_password(client, fill_db):
    '''
    Checks if user password can be changed in Account Information.
    '''
    NEW_PASSWORD = 'niktniezgadnie'
    ERRORS = {
        'wrong_password': 'Please type correctly your old password!',
        'wrong_matching': "New passwords didn't match each other."
    }

    def check_errors(error_name):
        client.wait_for_modal()

        assert ERRORS[error_name] in client.get_modal_errors()

        client.close_modal()

    client.menu_jump_to('account')

    client.click_on_class('change-password')

    # Write wrong password
    client.send_keys('password', NEW_PASSWORD, focus_css_selector=False)
    client.click_on_class('btn-save-changes')

    # Check if error modal appear
    check_errors('wrong_password')

    # Write correct password
    client.send_keys('password', DEFAULT_PASSWORD, clear=True, focus_css_selector=False)

    # Write new password but do not repeat it properly
    client.send_keys('new-password', NEW_PASSWORD, focus_css_selector=False)
    client.click_on_class('btn-save-changes')

    # Check for errors
    check_errors('wrong_matching')

    # Write correct password again
    client.send_keys('repeat-password', NEW_PASSWORD, focus_css_selector=False)
    client.click_on_class('btn-save-changes')

    # Check if new password is saved
    user = fill_db.models['user'][DEFAULT_USERNAME]
    updated_user = User.objects.get(id=user.id)

    assert updated_user.check_password(NEW_PASSWORD) is True
