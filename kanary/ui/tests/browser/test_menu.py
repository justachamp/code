import pytest


menu = {
    'Dashboard': 'dashboard',
    'Campaigns': 'campaigns',
    'Storage': 'storage',
}


@pytest.mark.usefixtures('fill_db')
def test_items_select(client):
    ''' Tests if sidebar loads correctly after clicking on button in menu
    '''

    for title, link in menu.items():
        client.get('/')
        client.menu_jump_to(link)
        client.check_sidebar_title(title)
