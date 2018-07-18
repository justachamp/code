from random import choice, sample, randrange

import pytest

from etc import dimensions, constants
from ui.targeting.models import (
    TargetValue, ContentCategory, SegmentProximicMaturityRating,
    SegmentProximicPageNoticeability, SegmentProximicPagePlacement,
    SegmentProximicContextual, Peer39ContextualSegment, Peer39PageQuality,
    LotameDemographic, LotameAdvancedDemographic, LotameBehavioralInterest,
    LotameInfluencers, LotameOffline
)
from ui.campaign.models import Strategy
from ui.storage.models import Audience

from ui.tests.browser import utils_strategy as utils
from ui.tests.browser.page.strategy import TargetingPage, TARGETING_WIDGET_NAMES as WIDGET_NAMES


# TARGETING HELPERS
def get_dropdowns(client):
    '''
    Returns dropdown elements in targeting steps
    '''
    include_dropdown = client.find_element_by_class_name('-t-include-dropdown')
    exclude_dropdown = client.find_element_by_class_name('-t-exclude-dropdown')

    return include_dropdown, exclude_dropdown


def get_group(widget, group_name):
    '''
    Gets checkbox group element from given widget
    '''
    groups = widget.find_elements_by_class_name('-t-group')
    with_header = lambda gr: gr.find_element_by_css_selector('h5').text == group_name
    matched_groups = filter(with_header, groups)
    if len(matched_groups) > 1:
        raise Exception('There is more than one group matching this name.')
    if not matched_groups:
        raise Exception('There is no such group within this widget')
    return matched_groups[0]


def get_tags(widget, from_box=False):
    '''
    Returns a list of all tags from given widget.
    '''
    class_name = '-t-tag'
    if from_box:
        class_name = '-t-box'

    tag_elements = widget.find_elements_by_class_name(class_name)
    tags = []
    for element in tag_elements:
        element.location_once_scrolled_into_view
        tag_text = element.text.replace(' (state)', '')
        if tag_text:
            # Unselected tags are invisible, thus the text returned is ''
            # We should ignore them
            tags.append(tag_text)
    return tags


def display_widget(client, name, section='include'):
    dropdown_toggle = '%s-target' % section
    add_widget = '%s-%s' % (section, name)
    widget = '-t-widget-%s-%s' % (section, name)

    client.click_on_class(dropdown_toggle)
    client.click_on_class(add_widget)

    client.wait_until_displayed(widget)

    return client.find_element_by_class_name(widget)


def click_checkbox(group, label_text):
    '''
    Clicks checkbox input within given group base on its label.
    '''
    checkboxes = group.find_elements_by_class_name('-t-checkbox')

    for checkbox in checkboxes:
        label = checkbox.find_element_by_css_selector('span')
        label.location_once_scrolled_into_view
        if label.text == label_text:
            label.click()
            return

    raise Exception("There is no checkbox with given label within this group")


# TEST CASES
@pytest.mark.usefixtures(
    'maturity_rating_segment', 'language_segment', 'page_quality_segment',
    'page_placement_segment', 'page_noticeability_segment', 'proximic_contextual_segment',
    'peer39_segments', 'lotame_segments', 'fake_strategy_reports_inserter'
)
def test_targeting_widgets_behavior(client):
    '''
    Tests if all targeting widgets are selectable from include/exclude dropdown
    Checks if they are visible and if can be removed.
    '''
    utils.go_to_step(client, 'overall')
    type_selector = client.find_element_by_class_name('-t-type')
    for option in type_selector.find_elements_by_tag_name('option'):
        if option.text == 'Mobile':
            option.click()

    targeting_step_class = 'sidebar-targeting'
    client.click_on_class(targeting_step_class)

    # Set default timeout for this test.
    client.implicitly_wait(1)

    include_dropdown, exclude_dropdown = get_dropdowns(client)
    include_target_btn = client.find_element_by_class_name('-t-include-target')
    exclude_target_btn = client.find_element_by_class_name('-t-exclude-target')

    # Test both for include and exclude dropdown
    for dropdown in [include_dropdown, exclude_dropdown]:
        if dropdown is include_dropdown:
            button = include_target_btn
            section = 'include'
        else:
            button = exclude_target_btn
            section = 'exclude'

        # Display all available widgets
        for widget_name in WIDGET_NAMES:
            widget_class = '-t-widget-%s-%s' % (section, widget_name)
            widget_dropdown_class = '-t-%s-%s' % (section, widget_name)
            widget_collapse_class = '-t-widget-%s-%s-collapse' % (section, widget_name)
            widget_expand_class = '-t-widget-%s-%s-expand' % (section, widget_name)
            widget_content_id = 'targeting-%s-%s' % (section, widget_name)

            # Dropdown should be closed
            assert client.has_not_class(dropdown, 'open') is True

            # Open the dropdown
            client.click(button)
            assert client.has_class(dropdown, 'open') is True

            # Check if dropdown contains a picked widget
            assert client.is_present_in_DOM(widget_dropdown_class) is True

            # Select widget and check if it appears.
            client.click_on_class(widget_dropdown_class, bare=True)
            client.wait_until_displayed(widget_class)

            # Check if dropdown does not contain a picked widget
            assert client.is_present_in_DOM(widget_dropdown_class) is False

            # Collapse widget
            widget_content = client.find_element_by_id(widget_content_id)
            collapse_btn = client.find_element_by_class_name(widget_collapse_class)
            expand_btn = client.find_element_by_class_name(widget_expand_class)
            assert widget_content.is_displayed() is True

            client.click_on_class(widget_collapse_class, bare=True)

            client.wait_for_widget_action(widget_content, expanded=False)

            assert client.has_not_class(widget_content, 'in') is True
            assert collapse_btn.is_displayed() is False
            assert expand_btn.is_displayed() is True

            # Expand widget
            client.click_on_class(widget_expand_class, bare=True)

            client.wait_for_widget_action(widget_content, expanded=True)

            assert client.has_class(widget_content, 'in') is True
            assert collapse_btn.is_displayed() is True
            assert expand_btn.is_displayed() is False

        # Remove all displayed widgets
        for widget_name in WIDGET_NAMES:
            widget_class = '-t-widget-%s-%s' % (section, widget_name)
            widget_dropdown_class = '-t-%s-%s' % (section, widget_name)
            widget_remove_class = '-t-widget-%s-%s-remove' % (section, widget_name)

            client.click_on_class(widget_remove_class, bare=True, scroll=True)

            # Check if widget is not displayed
            assert client.is_present_in_DOM(widget_class) is False

            # Check if dropdown does contains a picked widget
            assert client.is_present_in_DOM(widget_dropdown_class) is True


@pytest.mark.usefixtures(
    'fake_strategy_reports_inserter', 'fake_advert_reports_inserter'
)
def test_userprofile_widget(client, fill_db):
    '''
    Tries to save data using checkboxes in User Profile widget.
    Checks if checkbox and tags are correctly saved in UI and
    if data are stored in DB.
    Then tries if when we remove widget data is also removed from DB.
    '''
    # Representant values
    AGE_GROUPS = [t.value for t in TargetValue.objects.representants().filter(category=dimensions.age_group)]
    GENDERS = [t.value for t in TargetValue.objects.representants().filter(category=dimensions.gender)]

    utils.go_to_step(client, 'targeting', existing=True)

    widget = display_widget(client, 'UserProfile')

    # Checked values are stored here
    checked_age_groups = []
    checked_genders = []

    # Test both groups in widget
    for group_name, representants, checked in [
            ('Age Group', AGE_GROUPS, checked_age_groups),
            ('Gender', GENDERS, checked_genders)]:

        group = get_group(widget, group_name)
        checkboxes = group.find_elements_by_class_name('-t-checkbox')

        # Check if labels text comes from representants
        for checkbox in checkboxes:
            checkbox.location_once_scrolled_into_view
            label = checkbox.find_element_by_css_selector('span')
            assert label.text in representants

        # Click random checkboxes
        labels_to_check = sample(representants, randrange(1, len(representants) + 1))
        checked.extend(labels_to_check)

        for label in labels_to_check:
            click_checkbox(group, label)

    # Check if tags are correct
    all_checked = checked_age_groups + checked_genders
    tags = get_tags(widget)
    assert sorted(tags) == sorted(all_checked)

    utils.save_and_return_to_step(client)

    # Check if widget is displayed
    client.wait_until_displayed('-t-widget-include-UserProfile')
    widget = client.find_element_by_class_name('-t-widget-include-UserProfile')
    assert widget.is_displayed() is True

    strategy = Strategy.objects.all()[0]

    # Check displayed data and tags
    for group_name, category, checked in [
            ('Age Group', dimensions.age_group, checked_age_groups),
            ('Gender', dimensions.gender, checked_genders)]:
        group = get_group(widget, group_name)

        for checkbox in group.find_elements_by_class_name('-t-checkbox'):
            checkbox.location_once_scrolled_into_view
            label = checkbox.find_element_by_css_selector('span')
            if label.text in checked:
                client.has_class(checkbox, 'checked') is True
            else:
                client.has_not_class(checkbox, 'checked') is True

        # Check database
        saved_tvalues = [tv.value for tv in strategy.targeting_values.filter(category=category)]
        assert sorted(checked) == sorted(saved_tvalues)

    tags = get_tags(widget)
    assert sorted(tags) == sorted(all_checked)

    client.click_on_class('widget-include-UserProfile-remove')

    utils.save_and_return_to_step(client)

    # Check if widget is not displayed and data is not in DB
    assert client.is_present_in_DOM('-t-widget-include-UserProfile') is False

    strategy = Strategy.objects.all()[0]
    assert strategy.targeting_values.representants().count() == 0


@pytest.mark.usefixtures(
    'page_placement_segment', 'page_noticeability_segment', 'proximic_contextual_segment',
    'peer39_segments', 'fake_strategy_reports_inserter', 'fake_advert_reports_inserter'
)
@pytest.mark.parametrize('widget_name, get_category_tree, get_strategy_categories', (
    (
        'Content',
        lambda: ContentCategory.objects.into_tree(),
        lambda strategy: strategy.content_category_values.all(),
    ),
    (
        'ProximicPageNoticeability',
        lambda: SegmentProximicPageNoticeability.objects.into_tree(),
        lambda strategy: strategy.segment_proximic_page_noticeability.all(),
    ),
    (
        'ProximicPagePlacement',
        lambda: SegmentProximicPagePlacement.objects.into_tree(),
        lambda strategy: strategy.segment_proximic_page_placement.all(),
    ),
    (
        'ProximicContextual',
        lambda: SegmentProximicContextual.objects.into_tree(),
        lambda strategy: strategy.segment_proximic_contextual.all(),
    ),
    (
        'PeerContextual',
        lambda: Peer39ContextualSegment.objects.into_tree(),
        lambda strategy: strategy.segment_peer_contextual.all(),
    ),
    (
        'PeerPageQuality',
        lambda: Peer39PageQuality.objects.into_tree(),
        lambda strategy: strategy.segment_peer_page_quality.all()
    ),
))
def test_tree_widget(client, fill_db, widget_name, get_category_tree, get_strategy_categories,
                     section='include'):
    '''
    Test editing content categories

    :param string widget_name: Name of widget, defined in strategy.js
    :param function get_category_tree: Function retrieving list of categories with subcategories
    :param function get_strategy_categories: A function retrieving saved
        categories from strategy
    :param string section: Name of targeting section widget will be added to.
        Can equal 'include' or 'exclude'
    '''
    def scroll_to_bottom():
        '''
        Make sure that entire category list is visible
        by scrolling to a button under the widget
        '''
        btn_class = '-t-%s-dropdown' % section
        include_btn = client.find_element_by_class_name(btn_class)
        include_btn.location_once_scrolled_into_view

    def find_by_text(elements, text):
        '''
        Find first WebElement with a matching text

        :param list elements: List of WebElements
        :param string text: Text to match
        '''
        def by_text(element):
            element.location_once_scrolled_into_view
            return element.text == text
        matches = filter(by_text, elements)
        return matches[0]

    def expand(node):
        '''
        Expand tree node, return list of child nodes

        :param WebElement node: Element containing collapse handle and node name
        :returns Element containing list of child nodes
        :rtype WebElement
        '''
        expand_btn = node.find_element_by_class_name('collapsed')
        subelements_selector = expand_btn.get_attribute('data-target')
        client.click(expand_btn)
        scroll_to_bottom()
        client.wait_until_displayed(subelements_selector, by="css_selector")
        return client.find_element_by_css_selector(subelements_selector)

    def collapse(node):
        '''
        Collapse tree node

        :param WebElement node: Element containing collapse handle and node name
        '''
        collapse_btn = node.find_element_by_class_name('collapse-handle')
        subelements_selector = collapse_btn.get_attribute('data-target')
        client.click(collapse_btn)
        client.wait_until_displayed(subelements_selector, by="css_selector", until=False)

    # Select 1 random main category, and 1 random subcategory that is
    # not included in the first category.
    category_tree = get_category_tree()
    category_tree_with_children = filter(lambda c: c.get('children'), category_tree)

    strategy = Strategy.objects.all().first()
    WIDGET_CLASS = '-t-widget-%s-%s' % (section, widget_name)
    random_main_categories = sample(category_tree_with_children, 2)
    first_category = random_main_categories[0]
    second_category = random_main_categories[1]
    SELECTED_CATEGORIES = []
    SELECTED_MAIN_CATEGORY = first_category['name']
    SELECTED_MAIN_CATEGORY_CHILDREN = [c['name'] for c in first_category['children']]
    SELECTED_SUBCATEGORY_PARENT = second_category['name']
    SELECTED_SUBCATEGORY = choice(second_category['children'])['name']

    # Store categories that should be saved to DB
    SELECTED_CATEGORIES.append(SELECTED_MAIN_CATEGORY)
    SELECTED_CATEGORIES.extend(SELECTED_MAIN_CATEGORY_CHILDREN)
    SELECTED_CATEGORIES.append(SELECTED_SUBCATEGORY)
    IS_ONLY_SUBCATEGORY = (len(second_category['children']) == 1)
    if IS_ONLY_SUBCATEGORY:
        SELECTED_CATEGORIES.append(SELECTED_SUBCATEGORY_PARENT)

    # Go to targeting, display widget and make sure it is fully visible
    utils.go_to_step(client, 'targeting', existing=True)

    widget = display_widget(client, widget_name, section=section)

    scroll_to_bottom()

    # Check if all main categories are displayed.

    main_tree_elements = [e for e in widget.find_elements_by_class_name('-t-tree-main') if e.text]

    ui_main_categories = [e.text for e in main_tree_elements if e.text]

    main_categories = [c['name'] for c in category_tree]

    assert ui_main_categories == main_categories

    # Check if all subcategories are displayed after expanding main category.
    # Check if they are hidden when category is collapsed.
    for index, category in enumerate(category_tree):
        subcategories = [c['name'] for c in category.get('children', [])]
        ui_main_category = main_tree_elements[index]
        collapse_handle = ui_main_category.find_element_by_class_name('tree-handle')

        ui_subcategories = []

        if 'collapsed' in collapse_handle.get_attribute('class'):
            ui_main_category.location_once_scrolled_into_view
            subcategory_ul = expand(ui_main_category)
            subcategory_ul.location_once_scrolled_into_view

            for e in subcategory_ul.find_elements_by_class_name('-t-checkbox'):
                if not e.is_displayed():
                    e.location_once_scrolled_into_view

                # Filter undisplayed subelements
                if e.is_displayed() and e.text:
                    ui_subcategories.append(e.text)

            collapse(ui_main_category)

        assert sorted(ui_subcategories) == sorted(subcategories)

    # Select a random main category. Check if main and subcategory
    # checkboxes state change.

    ui_main_category = find_by_text(main_tree_elements, SELECTED_MAIN_CATEGORY)
    subcategory_ul = expand(ui_main_category)
    main_checkbox = client.get_checkbox(ui_main_category)
    assert client.is_not_checked(main_checkbox)

    sub_checkboxes = subcategory_ul.find_elements_by_class_name('-t-checkbox')
    for checkbox in sub_checkboxes:
        assert client.is_not_checked(checkbox)

    main_checkbox.click()

    assert client.is_checked(main_checkbox)
    sub_checkboxes = subcategory_ul.find_elements_by_class_name('-t-checkbox')
    for checkbox in sub_checkboxes:
        assert client.is_checked(checkbox)

    collapse(ui_main_category)

    # Select a random subcategory. Check if checkbox state chenges.

    ui_subcategory_parent = find_by_text(main_tree_elements, SELECTED_SUBCATEGORY_PARENT)
    main_checkbox = client.get_checkbox(ui_subcategory_parent)
    subcategory_ul = expand(ui_subcategory_parent)
    sub_checkboxes = subcategory_ul.find_elements_by_class_name('-t-checkbox')
    sub_checkbox = find_by_text(sub_checkboxes, SELECTED_SUBCATEGORY)

    # If there is only one child category, parent should be automatically checked
    if IS_ONLY_SUBCATEGORY:
        assert client.is_not_checked(main_checkbox)

    assert client.is_not_checked(sub_checkbox)

    client.click(sub_checkbox)

    if IS_ONLY_SUBCATEGORY:
        assert client.is_checked(main_checkbox)

    assert client.is_checked(sub_checkbox)

    collapse(ui_subcategory_parent)

    # Save strategy

    assert len(get_strategy_categories(strategy)) == 0
    utils.save_and_return_to_step(client)

    # Check if all categories were saved to DB

    db_categories = [c.name for c in get_strategy_categories(strategy)]
    assert sorted(SELECTED_CATEGORIES) == sorted(db_categories)

    # 5. Check if they are displayed correctly, uncheck them and save

    widget = client.find_element_by_class_name(WIDGET_CLASS)
    scroll_to_bottom()
    main_tree_elements = widget.find_elements_by_class_name('-t-tree-main')

    ui_main_category = find_by_text(main_tree_elements, SELECTED_MAIN_CATEGORY)
    subcategory_ul = expand(ui_main_category)
    main_checkbox = client.get_checkbox(ui_main_category)
    assert client.is_checked(main_checkbox)

    sub_checkboxes = subcategory_ul.find_elements_by_class_name('-t-checkbox')
    for checkbox in sub_checkboxes:
        assert client.is_checked(checkbox)

    main_checkbox.click()

    assert client.is_not_checked(main_checkbox)
    sub_checkboxes = subcategory_ul.find_elements_by_class_name('-t-checkbox')
    for checkbox in sub_checkboxes:
        assert client.is_not_checked(checkbox)

    collapse(ui_main_category)

    # Uncheck the subcategory

    ui_subcategory_parent = find_by_text(main_tree_elements, SELECTED_SUBCATEGORY_PARENT)
    subcategory_ul = expand(ui_subcategory_parent)
    sub_checkboxes = subcategory_ul.find_elements_by_class_name('-t-checkbox')
    sub_parent_checkbox = client.get_checkbox(ui_subcategory_parent)
    sub_checkbox = find_by_text(sub_checkboxes, SELECTED_SUBCATEGORY)

    if IS_ONLY_SUBCATEGORY:
        assert client.is_checked(sub_parent_checkbox)

    assert client.is_checked(sub_checkbox)

    client.click(sub_checkbox)

    if IS_ONLY_SUBCATEGORY:
        assert client.is_not_checked(sub_parent_checkbox)

    assert client.is_not_checked(sub_checkbox)

    collapse(ui_subcategory_parent)

    utils.save_and_return_to_step(client)

    # Check if categories were removed from UI and DB

    assert len(get_strategy_categories(strategy)) == 0
    assert client.is_present_in_DOM(WIDGET_CLASS) is False


@pytest.mark.usefixtures(
    'fake_strategy_reports_inserter', 'fake_advert_reports_inserter'
)
def test_text_search_widgets(client, fill_db_mobile_strategies, representants):
    '''
    Tries to select all available text search widgets, make manipulation
    with them (choosing/removing options) and saving strategy.
    Then it removes widgets and tests if they are not present in UI and
    if values are not stored in db.
    '''
    def check_tags_boxes(widget, widget_data):
        tags = get_tags(widget)
        boxes = get_tags(widget, from_box=True)

        assert sorted(tags) == sorted(widget_data['checked'])
        assert sorted(boxes) == sorted(widget_data['checked'])

    SEARCH_WIDGETS = {
        # KANARY-2206
        # 'Device': {
        #     'category': dimensions.g_device,
        #     'checked': [],
        # },
        'Location': {
            'category': dimensions.g_location,
            'checked': [],
        },
        'Os': {
            'category': dimensions.g_os,
            'checked': [],
        },
        'Carrier': {
            'category': dimensions.carrier,
            'checked': [],
        },
    }

    utils.go_to_step(client, 'targeting', existing=True)

    # Set default timeout for this test.
    client.implicitly_wait(1)

    include_target_btn = client.find_element_by_class_name('-t-include-target')

    for widget_name, widget_data in SEARCH_WIDGETS.iteritems():
        include_target_btn.click()
        client.click_on_class('-t-include-%s' % widget_name, bare=True)
        client.wait_until_displayed('-t-widget-include-%s' % widget_name)

        # Scroll down to the button to make sure suggestions are visible
        include_target_btn.location_once_scrolled_into_view

        widget = client.find_element_by_class_name(
            '-t-widget-include-%s' % widget_name
        )

        target_values = TargetValue.objects.representants()\
            .filter(category=widget_data['category'])\
            .order_by('value')\
            .distinct('value')

        values_count = target_values.count()

        # pick some random values from representants (we will type them in widget)
        random_values = sample(target_values, randrange(2, values_count))

        input_field = client.find_element_by_class_name(
            '-t-input-include-%s' % widget_name
        )

        for tv in random_values:
            # Scroll down to the button to make sure suggestions are visible
            include_target_btn.location_once_scrolled_into_view

            # type in input
            lowest_hierarchy = tv.value_list[-1]
            value_to_type = lowest_hierarchy[:3].lower()
            input_field.send_keys(value_to_type)

            # wait for dropdown appearance
            client.wait_until_displayed('tt-dataset-%s' % widget_name)

            # click in dropdown first suggestion
            client.click_on_class('value-%s' % widget_name)

            widget_data['checked'].append(lowest_hierarchy)

        check_tags_boxes(widget, widget_data)

    utils.save_and_return_to_step(client)

    # Check all widgets data and remove each widget
    for widget_name, widget_data in SEARCH_WIDGETS.iteritems():
        client.wait_until_displayed('-t-widget-include-%s' % widget_name)

        widget = client.find_element_by_class_name(
            '-t-widget-include-%s' % widget_name
        )

        assert widget.is_displayed()

        check_tags_boxes(widget, widget_data)

        # check database
        strategy = Strategy.objects.all()[0]
        saved_repr = [tv.value_list[-1] for tv in strategy.targeting_values.representants().filter(
                      category=widget_data['category'])]

        assert sorted(saved_repr) == sorted(widget_data['checked'])

        # remove widget
        client.click_on_class('widget-include-%s-remove' % widget_name)

    utils.save_and_return_to_step(client)

    # for each widget check if db is empty and if it is not displayed
    for widget_name, widget_data in SEARCH_WIDGETS.iteritems():

        assert client.is_present_in_DOM('-t-widget-include-%s' % widget_name) is False

        strategy = Strategy.objects.all()[0]

        assert strategy.targeting_values.representants().filter(category=widget_data['category']).count() == 0


@pytest.mark.usefixtures(
    'fake_strategy_reports_inserter', 'fake_advert_reports_inserter'
)
def test_audiences_widget(client, fill_db):
    '''
        Tests adding and removing audiences from targeting, both in UI and DB
    '''

    def get_audiences_from_widget(client):
        return client.find_elements_by_css_selector('.-t-audience-list li')

    def get_audiences_from_tray(client):
        return client.find_elements_by_css_selector('.-t-audience-tray-list li')

    utils.go_to_step(client, 'targeting', existing=True)

    # Set default timeout for this test.
    client.implicitly_wait(1)

    # Check if widget is created empty
    display_widget(client, 'Audiences')
    widget_class = '-t-widget-%s-%s' % ('include', 'Audiences')

    audiences_included = get_audiences_from_widget(client)

    assert len(audiences_included) == 0

    # Check if audiences in tray are displayed
    client.click_on_class('add-audience')
    client.wait_for_tray('trayAudiences')
    audiences_in_tray = get_audiences_from_tray(client)
    audiences_tray_names = [a.text for a in audiences_in_tray]
    audiences_from_db = Audience.objects.values_list('name', flat=True)

    assert sorted(audiences_tray_names) == sorted(audiences_from_db)

    # Check selecting an audience
    selected_audience = audiences_in_tray[0]
    selected_name = selected_audience.text
    client.click(selected_audience)

    audiences_included = get_audiences_from_widget(client)
    assert len(audiences_included) == 1
    assert audiences_included[0].text == selected_name

    # Check saving audience
    utils.save_and_return_to_step(client)

    audiences_included = get_audiences_from_widget(client)
    assert len(audiences_included) == 1
    assert audiences_included[0].text == selected_name

    # Check removing audience
    audiences_included = get_audiences_from_widget(client)
    remove_button = audiences_included[0].find_element_by_class_name('remove')
    client.click(remove_button)

    audiences_included = get_audiences_from_widget(client)
    assert len(audiences_included) == 0

    utils.save_and_return_to_step(client)

    assert client.is_present_in_DOM(widget_class) is False


@pytest.mark.usefixtures(
    'fake_strategy_reports_inserter', 'fake_advert_reports_inserter'
)
def test_audience_validation(client, fill_db):
    '''
        Tests if Django validation rejects the same audience
        in includes and exludes section
    '''
    def add_audience_to_widget(client, widget):
        add_button = widget.find_element_by_class_name('-t-add-audience')
        client.click(add_button)
        client.wait_for_tray('trayAudiences')
        audiences = client.find_elements_by_css_selector('.-t-audience-tray-list li')
        selected_audience = audiences[0]
        client.click(selected_audience)
        client.wait_for_tray('trayAudiences', hide=True)

    utils.go_to_step(client, 'targeting', existing=True)
    include_widget = display_widget(client, 'Audiences')
    exclude_widget = display_widget(client, 'Audiences', section="exclude")

    add_audience_to_widget(client, include_widget)
    add_audience_to_widget(client, exclude_widget)
    client.click_on_class('button-save-changes')

    modal = client.find_element_by_id('modal')
    assert client.has_class(modal, 'in') is True


@pytest.mark.usefixtures(
    'maturity_rating_segment', 'safety_level_segment',
)
def test_brand_protection_widget(client, fill_db):
    '''
        Tests adding and removing brand protection widget
    '''

    strategy = fill_db.models['strategy']['Hello this is Citrus']

    utils.go_to_step(client, 'targeting', existing=True)

    # checking additional data costs counter
    costs = client.find_element_by_class_name('-t-additional-data-costs')
    assert costs.text == '-'

    # adding BRAND PROTECTION widget to INCLUDE section
    widget_type = 'ProximicBrandProtection'
    widget = display_widget(client, widget_type)

    # additional data costs shouldn't be added
    client.wait_until(lambda: costs.text == '-')

    # checking if all segments are available and not selected
    segments = SegmentProximicMaturityRating.objects.all()\
        .values_list('name', flat=True)

    for segment in segments:
        el = client.find_element_by_class_name('-t-protection-%s' % segment)
        assert el
        assert 'active' not in el.get_attribute('class').split()

    # checking segments in database
    assert strategy.segment_proximic_maturity_rating.all().count() == 0

    # selecting PG-13 segment
    client.click_on_class('protection-PG13')

    # checking additional data costs counter
    client.wait_until(lambda: costs.text == '$%s' %
                      constants.TARGETING_ADDITIONAL_DATA_COSTS['brand_protection'])

    # checking label in widget's header
    assert 'PG13' in get_tags(widget)

    # saving campaign
    utils.save_and_return_to_step(client)

    # check segment in database
    segments_in_db = strategy.segment_proximic_maturity_rating.all()
    client.wait_until(lambda: segments_in_db.count() == 1)

    # checking if PG-13 segment is already selected
    segment = client.find_element_by_class_name('-t-protection-PG13')
    assert client.has_class(segment, 'active')

    # checking label in widget's header
    widget_class = '-t-widget-include-%s' % widget_type
    widget = client.find_element_by_class_name(widget_class)
    assert 'PG13' in get_tags(widget)

    # removing widget
    client.click_on_class('widget-include-%s-remove' % widget_type)

    # checking if widget has been removed
    assert client.is_present_in_DOM(widget_class) is False

    # checking additional data costs counter
    costs = client.find_element_by_class_name('-t-additional-data-costs')
    client.wait_until(lambda: costs.text == '-')

    # saving campaign
    utils.save_and_return_to_step(client)

    # check if widget is removed after save
    assert client.is_present_in_DOM(widget_class) is False

    # checking segments in database
    client.wait_until(lambda: segments_in_db.count() == 0)


@pytest.mark.parametrize('widget_name, get_segment_list, get_strategy_included, get_strategy_excluded', (
    (
        'LotameDemographic',
        lambda: LotameDemographic.objects.all(),
        lambda strategy: strategy.segment_lotame_demographic.all(),
        lambda strategy: strategy.segment_lotame_demographic_exclude.all()
    ),
    (
        'LotameAdvancedDemographic',
        lambda: LotameAdvancedDemographic.objects.all(),
        lambda strategy: strategy.segment_lotame_advanced_demographic.all(),
        lambda strategy: strategy.segment_lotame_advanced_demographic_exclude.all()
    ),
    (
        'LotameBehavioralInterest',
        lambda: LotameBehavioralInterest.objects.all(),
        lambda strategy: strategy.segment_lotame_behavioral_interest.all(),
        lambda strategy: strategy.segment_lotame_behavioral_interest_exclude.all()
    ),
    (
        'LotameInfluencer',
        lambda: LotameInfluencers.objects.all(),
        lambda strategy: strategy.segment_lotame_influencers.all(),
        lambda strategy: strategy.segment_lotame_influencers_exclude.all()
    ),
    (
        'LotameOffline',
        lambda: LotameOffline.objects.all(),
        lambda strategy: strategy.segment_lotame_offline.all(),
        lambda strategy: strategy.segment_lotame_offline_exclude.all()
    ),
))
def test_list_widget(client, fill_db, lotame_segments, widget_name, get_segment_list, get_strategy_included,
                     get_strategy_excluded):
    """Test including and excluding segments through list widget"""

    utils.go_to_step(client, 'targeting', existing=True)
    strategy_name = client.find_element_by_class_name('-t-name').text
    strategy = Strategy.objects.get(name=strategy_name)

    # No segments should be selected
    assert get_strategy_included(strategy).count() == 0
    assert get_strategy_excluded(strategy).count() == 0

    # Choose more than 1 segment
    SAMPLE_SIZE = 6
    segments = sample(get_segment_list(), SAMPLE_SIZE)
    # Include half of the sample, and exclude the other half
    included_segments = segments[:SAMPLE_SIZE/2]
    excluded_segments = segments[SAMPLE_SIZE/2:]

    targeting_page = TargetingPage(client)
    include_widget = targeting_page.include.add(widget_name)
    exclude_widget = targeting_page.exclude.add(widget_name)

    # Include and exclude some random segments
    for widget, segments in [
        (include_widget, included_segments),
        (exclude_widget, excluded_segments)
    ]:
        checkboxes = widget.checkboxes
        for segment in segments:
            checkbox = client.find_by_text(checkboxes, segment.name)
            client.click(checkbox)
            assert client.is_checked(checkbox)
        assert sorted(widget.tags) == sorted(s.name for s in segments)

    # Save strategy and check if segments were saved
    utils.save_and_return_to_step(client)

    assert include_widget.is_displayed
    assert exclude_widget.is_displayed

    for widget, segments in [
        (include_widget, included_segments),
        (exclude_widget, excluded_segments)
    ]:
        checkboxes = widget.checkboxes
        selected_names = [s.name for s in segments]
        assert sorted(widget.tags) == sorted(selected_names)
        for checkbox in checkboxes:
            checkbox.location_once_scrolled_into_view
            if checkbox.text in selected_names:
                assert client.is_checked(checkbox)
            else:
                assert client.is_not_checked(checkbox)

    # Check included and excluded segments in database
    included_segments_db = get_strategy_included(strategy).values_list('id', 'name')
    excluded_segments_db = get_strategy_excluded(strategy).values_list('id', 'name')

    def id_and_name(segment):
        return (segment.id, segment.name)

    assert sorted(map(id_and_name, included_segments)) == sorted(included_segments_db)
    assert sorted(map(id_and_name, excluded_segments)) == sorted(excluded_segments_db)


@pytest.mark.usefixtures(
    'maturity_rating_segment', 'language_segment', 'page_quality_segment', 'safety_level_segment',
    'page_placement_segment', 'page_noticeability_segment', 'proximic_contextual_segment',
    'peer39_segments', 'lotame_segments', 'fill_db_mobile_strategies', 'representants',
    'fake_strategy_reports_inserter', 'fake_advert_reports_inserter'
)
def test_include_exclude_validation(client):
    """Test if the same values cannot be included and excluded at the same time"""
    utils.go_to_step(client, 'targeting', existing=True)

    targeting_page = TargetingPage(client)

    def check_errors(*args):
        targeting_page.save()
        client.wait_for_modal()

        errors = client.get_modal_errors()
        for field_name in args:
            message = '{field_name}: Cannot include and exlude the same values'.format(field_name=field_name)
            assert message in errors

        client.close_modal()

    # Checkbox widgets
    single_column_widgets = [
        ('PeerContextual', 'Peer contextual'),
        ('PeerPageQuality', 'Peer page quality'),
        ('PeerBrandProtection', 'Peer brand protection'),
        ('PeerLanguage', 'Peer page language'),
        ('LotameDemographic', 'Lotame demographic'),
        ('LotameAdvancedDemographic', 'Lotame advanced demographic'),
        ('LotameBehavioralInterest', 'Lotame behavioral interest'),
        ('LotameInfluencer', 'Lotame influencers'),
        ('LotameOffline', 'Lotame offline'),
        ('ProximicLanguage', 'Proximic language'),
        ('ProximicPageQuality', 'Proximic page quality'),
        ('ProximicPageNoticeability', 'Proximic page noticeability'),
        ('ProximicPagePlacement', 'Proximic page placement'),
        ('ProximicContextual', 'Proximic contextual')
    ]
    for widget_name, field_name in single_column_widgets:
        for section in (targeting_page.include, targeting_page.exclude):
            widget = section.add(widget_name)
            widget.checkboxes[0].click()

        check_errors(field_name)

    multiple_column_widgets = [
        ('UserProfile', ['Age group', 'Gender']),
    ]
    for widget_name, fields in multiple_column_widgets:
        for section in (targeting_page.include, targeting_page.exclude):
            widget = section.add(widget_name)
            for group in widget.checkbox_groups:
                group[0].click()

        check_errors(*fields)

    # Custom widgets
    for section in (targeting_page.include, targeting_page.exclude):
        widget = section.add('ProximicBrandProtection')
        maturity = widget.container.find_element_by_class_name('btn-radio')
        client.click(maturity)
        safety_level = widget.checkboxes[0]
        client.click(safety_level)

    check_errors('Proximic maturity rating', 'Proximic safety level')

    # Search widgets
    search_widgets = [
        ('Device', 'sony', 'Device'),
        ('Location', 'ohio', 'Location'),
        ('Os', 'android', 'Operating system'),
        ('Carrier', 'plus', 'Carrier')
    ]
    for widget_name, text_to_type, field_name in search_widgets:
        for section in (targeting_page.include, targeting_page.exclude):

            widget = section.add(widget_name)

            # Scroll down to the button to make sure suggestions are visible
            section._dropdown.location_once_scrolled_into_view

            # type in input
            widget.search_input.send_keys(text_to_type)

            # wait for dropdown appearance
            client.wait_until_displayed(widget.search_dropdown)

            # click in dropdown first suggestion
            client.click(widget.search_suggestions[0])

        check_errors(field_name)
