from ui.tests.browser.page import LoginForm
from ui.tests.utils import default_user


def test_login(base_client, user):
    """ Log user in and log out """

    login_form = LoginForm(base_client)

    login_form.fill_inputs(
        username=default_user[0]['username'],
        password=default_user[0]['password']
    )

    login_form.submit()

    # Redirecting to campaigns in order to avoid liveview loading.
    base_client.menu_jump_to('campaigns')

    assert base_client.get_title() == 'Campaigns'

    base_client.find_element_by_class_name('-t-logout').click()

    LoginForm(base_client)
