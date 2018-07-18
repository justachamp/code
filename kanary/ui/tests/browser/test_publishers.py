from etc import dimensions
from ui.campaign.models import Strategy
from ui.targeting.models import PublisherTargetValue
from ui.publishers.models import PublisherSet
from haystack.query import SearchQuerySet


def go_to_publishers(client):
    '''
    Edit first strategy in first campaign
    '''

    # Go to campaigns (main menu)
    client.menu_jump_to('campaigns')

    # Click on first campaign
    client.click_on_class('campaign')

    # Click on first strategy
    client.click_on_class('strategy')

    # Click edit button
    client.click_on_class('edit-strategy')

    # Select publishers section
    client.click_on_class('sidebar-publishers')


def save_and_return_to_publishers(client):
    # Save strategy
    client.click_on_button('save-changes')

    # Click edit button
    client.click_on_class('edit-strategy')

    # Select publishers section
    client.click_on_class('sidebar-publishers')


def go_to_search_tab(client):
    client.click_on_class('search-results')


def go_to_selected_tab(client):
    client.click_on_class('selected-publishers')

get_name = lambda element: element[0]


def get_publishers_from_db(inventory, pubkey):
    '''
        Retrieves publisher list from database

        :param str inventory: Inventory type, 'app' or 'site'
        :param str pubkey: Inventory type, 'publisher_name' or 'network'

        :returns: List of tuples containing publishers (name, network), sorted by name
        :rtype list
    '''
    extract_values = lambda pub: (
        pub.value_dict[pubkey], pub.value_dict['network'])

    inventory_mapping = {
        'app': 'App',
        'site': 'Web'
    }
    by_key = lambda pub: pub.key == pubkey

    db_inventory = inventory_mapping[inventory]
    publishers = PublisherTargetValue.objects.representants() \
                 .filter(value__contains=db_inventory)
    publishers = map(extract_values, filter(by_key, publishers))
    return sorted(publishers, key=get_name)


def get_publisher_set_from_db(publisher_set, pubkey):
    '''
        Retrieves publisher set contents from database

        :param PublisherSet publisher_set: PublisherSet instance
        :param str pubkey: Inventory type, 'publisher_name' or 'network'

        :returns: List of tuples containing publishers (name, network), sorted by name
        :rtype list
    '''
    extract_values = lambda pub: (
        pub.value_dict[pubkey], pub.value_dict['network'])
    publishers = publisher_set.target_values.all()
    publishers = map(extract_values, publishers)
    return sorted(publishers, key=get_name)


def get_publishers_from_index(inventory, pubkey):
    '''
        Retrieves publisher list from search index

        :param str inventory: Inventory type, 'app' or 'site'
        :param str pubkey: Inventory type, 'publisher_name' or 'network'

        :returns: List of tuples containing publishers (name, network), sorted by name
        :rtype list
    '''
    publishers = SearchQuerySet().filter(inventory=inventory, pubkey=pubkey)
    publishers = [(p.name, p.network) for p in publishers]
    return sorted(publishers, key=get_name)


def get_publishers_from_ui(client, table_id, selected_only=False):
    '''
        Retrieves publisher list from database

        :param WebDriver client: Selenium driver
        :param str table_id: Table element ID

        :returns: List of tuples containing publishers (name, network), sorted by name
        :rtype list
    '''
    rows = get_rows(client, table_id)

    elements = []
    for row in rows:
        checkbox = client.get_checkbox(row)
        name = row.find_element_by_css_selector('td.name').text
        network = row.find_element_by_css_selector('td.network').text
        if (selected_only and client.is_checked(checkbox)) or not selected_only:
            elements.append((name, network))
    return sorted(elements, key=get_name)


def get_sets_from_tray(client):
    elements = client.find_elements_by_css_selector('.-publisher-set-list li')
    return sorted([e.text for e in elements])


def get_sets_from_db(**kwargs):
    sets = PublisherSet.objects.filter(**kwargs)
    return sorted([s.name for s in sets])


def get_rows(client, table_id):
    table = client.find_element_by_id(table_id)
    return table.find_elements_by_css_selector('tr.publisher-row')


def select_all(client, table_id):
    rows = get_rows(client, table_id)
    for row in rows:
        checkbox = client.get_checkbox(row)
        assert client.is_not_checked(checkbox)
        checkbox.click()
        assert client.is_checked(checkbox)


def unselect_all(client, table_id):
    rows = get_rows(client, table_id)
    for row in rows:
        checkbox = client.get_checkbox(row)
        assert client.is_checked(checkbox)
        checkbox.click()

    rows = get_rows(client, table_id)
    assert len(rows) == 0

SEARCH_TABLE_ID = 'publisher-search-table'
SELECTED_TABLE_ID = 'selected-publishers-table'


def test_select_publishers(client, publishers_db, search_engine):
    '''
        Tests if selecting and unselecting publishers works correctly
        1. Select all values, check if there weren't selected before.
        2. Check if all values appear in 'Selected' tab
        3. Unselect all values.
        4. Check if nothing is selected in both tabs.
    '''
    strategy = Strategy.objects.all()[0]
    inventory = strategy.type

    go_to_publishers(client)

    # Check if "Search" tab is active
    search_tab = client.find_element_by_css_selector('.-t-search-results')
    assert client.has_class(search_tab, 'active')

    # Publishers from index
    publishers_index = get_publishers_from_index(
        inventory, dimensions.publisher_name)

    # Publishers from db
    publishers_db = get_publishers_from_db(
        inventory, dimensions.publisher_name)

    # Publishers from UI search table
    publishers_search_ui = get_publishers_from_ui(client, SEARCH_TABLE_ID)

    # Check if publishers from all soures are the same
    assert publishers_index == publishers_db == publishers_search_ui

    select_all(client, SEARCH_TABLE_ID)

    # Go to "Selected" tab, check if it is active and contains all publishers
    go_to_selected_tab(client)

    search_tab = client.find_element_by_css_selector('.-t-selected-publishers')
    assert client.has_class(search_tab, 'active')

    publishers_selected_ui = get_publishers_from_ui(
        client, SELECTED_TABLE_ID)

    assert publishers_search_ui == publishers_selected_ui

    unselect_all(client, SELECTED_TABLE_ID)

    # Go to "Search" tab, check if no publisher is selected
    go_to_search_tab(client)

    selected_search_publishers = get_publishers_from_ui(
        client, SEARCH_TABLE_ID, selected_only=True)

    assert len(selected_search_publishers) == 0


def test_create_publisherset(client, publishers_db, search_engine):
    '''
        Tests creating publisher set
        1. Check if publisher set list is empty.
        2. Select all values in search tab.
        3. Save publisher set.
        4. Save strategy.
        5. Go back to publishers section and check if it was saved correctly.
    '''
    SET_NAME = "Cool publisher set"
    strategy = Strategy.objects.all()[0]
    assert strategy.publisherset is None
    go_to_publishers(client)

    # Open tray and check if it is empty
    client.click_on_button('publishers-open')
    client.wait_for_tray('trayPublishers')
    sets_ui = get_sets_from_tray(client)
    sets_db = get_sets_from_db()
    assert sets_ui == sets_db == []
    client.click_on_button('close')
    client.wait_for_tray('trayPublishers', hide=True)

    # Select all available publishers and store their names
    select_all(client, SEARCH_TABLE_ID)
    selected_publishers = get_publishers_from_ui(
        client, SEARCH_TABLE_ID, selected_only=True)

    # Save set
    client.click_on_button('save-set-as')
    client.wait_for_modal()
    name_input = client.find_element_by_css_selector(
        '.-t-input-publisher-set-name')
    name_input.send_keys(SET_NAME)
    client.click_on_button('modal-save')
    client.wait_for_modal(hide=True)

    # Save and go back to edition
    save_and_return_to_publishers(client)

    # Check if set was created and assigned to strategy
    assert PublisherSet.objects.all().count() == 1
    publisher_set = PublisherSet.objects.first()
    strategy = Strategy.objects.all()[0]
    assert strategy.publisherset == publisher_set

    # Check if selected publishers are the same
    saved_publishers_db = get_publisher_set_from_db(
        publisher_set, dimensions.publisher_name)
    saved_publishers_ui = get_publishers_from_ui(
        client, SEARCH_TABLE_ID, selected_only=True)
    assert selected_publishers == saved_publishers_ui == saved_publishers_db

    # Check if set is displayed in storage tray
    client.click_on_button('publishers-open')
    client.wait_for_tray('trayPublishers')
    sets_ui = get_sets_from_tray(client)
    sets_db = get_sets_from_db()
    assert sets_ui == sets_db == [SET_NAME]
    client.click_on_button('close')
    client.wait_for_tray('trayPublishers', hide=True)

    # Check if set name is the same
    client.click_on_button('save-set-as')
    client.wait_for_modal()
    name_input = client.find_element_by_css_selector(
        '.-t-input-publisher-set-name')
    saved_set_name = name_input.get_attribute('value')

    assert SET_NAME == saved_set_name


def test_open_publisherset(client, publisherset_db, search_engine):
    # Set default timeout for this test.
    client.implicitly_wait(1)

    # Go to publishers site
    go_to_publishers(client)

    # Check that strategy has no sets assigned
    strategy = Strategy.objects.all()[0]
    assert strategy.publisherset is None

    # Check if all sets from DB are displayed
    inventory = strategy.type
    client.click_on_button('publishers-open')
    client.wait_for_tray('trayPublishers')
    sets_ui = get_sets_from_tray(client)
    sets_db = get_sets_from_db(inventory=inventory)
    assert sets_ui == sets_db

    # Select first available set
    set_element = client.find_elements_by_css_selector('.-publisher-set-list li')[0]
    set_name = set_element.text
    set_element.click()
    client.wait_for_tray('trayPublishers', hide=True)

    # Check if all publishers included in this set are displayed
    publisher_set = PublisherSet.objects.get(name=set_name)
    selected_publishers_db = get_publisher_set_from_db(
        publisher_set, dimensions.publisher_name)
    selected_publishers_ui = get_publishers_from_ui(client, SEARCH_TABLE_ID,
        selected_only=True)

    assert selected_publishers_db == selected_publishers_ui

    # Save strategy
    client.click_on_button('save-changes')

    # Check if set has been saved with strategy
    strategy = Strategy.objects.all()[0]
    assert strategy.publisherset == publisher_set
