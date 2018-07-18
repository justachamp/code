"""Page objects for strategy forms"""

from random import choice
from ui.tests.browser.page import Controls


class StrategyPage(Controls):
    """
    Wrapper for Creatives tab in strategy edition.
    Functions operate on the first creative.
    """
    def __init__(self, client, container_cls='-t-creatives-container'):
        super(StrategyPage, self).__init__(client, container_cls)

    @property
    def file_name(self):
        return self.container.find_element_by_class_name('-t-input-creative-name')

    @property
    def upload(self):
        return self.client.find_element_by_css_selector('.-t-creative-upload input')

    @property
    def js_code(self):
        return self.container.find_element_by_class_name('-t-input-js-code')

    @property
    def custom_pixel(self):
        return self.container.find_element_by_class_name('-t-input-custom-pixel')

    @property
    def js_code_label(self):
        return self.container.find_element_by_class_name('-t-show-js-code-input')

    @property
    def custom_pixel_label(self):
        return self.container.find_element_by_class_name('-t-show-custom-pixel-input')

    @property
    def storage_button(self):
        return self.container.find_element_by_class_name('-t-button-creative-storage')

    @property
    def remove_button(self):
        return self.client.find_element_by_class_name('-t-remove-ad')

    def _show_textarea(self, textarea, textarea_label, should_fail):
        """Ensure textarea is hidden and show it. Ensure it appeared. Validate the label."""

        if textarea.get_attribute('value').strip() == '':
            assert textarea_label.text == 'Add tracking'
        else:
            assert textarea_label.text == 'Show tracking'

        assert not textarea.is_displayed()
        textarea_label.click()
        if should_fail:
            assert not textarea.is_displayed()
        else:
            assert textarea_label.text == 'Hide tracking'
            assert textarea.is_displayed()

    def show_js_code(self, should_fail=False):
        self._show_textarea(self.js_code, self.js_code_label, should_fail)

    def show_custom_pixel(self, should_fail=False):
        self._show_textarea(self.custom_pixel, self.custom_pixel_label, should_fail)

    def hide_js_code(self):
        """Ensure JS Code is visible and hide it. Ensure it disappeared."""
        self.assert_only_js_code_textarea_is_displayed()
        self.js_code_label.click()
        assert not self.js_code.is_displayed()

    def hide_custom_pixel(self):
        """Ensure Custom Pixel is visible and hide it. Ensure it disappeared."""
        self.assert_only_custom_pixel_textarea_is_displayed()
        self.custom_pixel_label.click()
        assert not self.custom_pixel.is_displayed()

    def assert_both_textareas_hidden(self):
        assert not self.js_code.is_displayed()
        assert not self.custom_pixel.is_displayed()

    def assert_only_js_code_textarea_is_displayed(self):
        assert self.js_code.is_displayed()
        assert not self.custom_pixel.is_displayed()

    def assert_only_custom_pixel_textarea_is_displayed(self):
        assert self.custom_pixel.is_displayed()
        assert not self.js_code.is_displayed()

    def close_both_textareas(self):
        if self.custom_pixel.is_displayed():
            self.hide_custom_pixel()
        if self.js_code.is_displayed():
            self.hide_js_code()

    def check_toggling(self):
        """Check if textareas can be toggled freely."""
        self.close_both_textareas()

        # Activate Pixel Tracking textarea:
        self.show_js_code()
        self.assert_only_js_code_textarea_is_displayed()

        # If Pixel Tracking is empty, showing Custom Tracking should hide Pixel Tracking:
        self.show_custom_pixel()
        self.assert_only_custom_pixel_textarea_is_displayed()

        # Toggling the same way, back:
        self.show_js_code()
        self.assert_only_js_code_textarea_is_displayed()

        self.close_both_textareas()

    def check_name(self, name):
        """Check if provided name is equal to name in form"""
        assert self.file_name.get_attribute('value') == name

    def show_creatives_tray(self):
        self.storage_button.click()
        self.client.wait_for_tray('trayCreatives')

    def select_creative_from_tray(self, name=None):
        """
        Selects a creative with given name or random creative

        :returns: name of selected creative
        :rtype str
        :raises Exception: if no creatives are available
        or many creatives were matched
        """
        self.show_creatives_tray()

        creatives = self.client.find_elements_by_css_selector('.-creatives-list li')

        if not creatives:
            raise Exception('No creatives available')

        creative = None

        if name:
            matching_creatives = filter(lambda c: c.text == name, creatives)
            if len(matching_creatives) != 1:
                raise Exception('%s matching creatives found instead of 1' % len(matching_creatives))
            creative = matching_creatives[0]
        else:
            creative = choice(creatives)

        selected_name = creative.text
        creative.click()
        self.client.wait_for_tray('trayCreatives', hide=True)

        return selected_name

    def upload_file(self, file_path):
        """
        :param str file_path: absolute path to file to upload
        """
        self.client.show_file_input('file')
        self.upload.send_keys(file_path)
        self.client.wait_for_xhr()


# Names must reflect targeting widgets types in strategy.js
TARGETING_WIDGET_NAMES = [
    'Location', 'Os', 'Carrier', 'Device', 'UserProfile', 'Audiences', 'Content',
    'ProximicBrandProtection', 'ProximicLanguage', 'ProximicPageQuality',
    'ProximicPageNoticeability', 'ProximicPagePlacement', 'ProximicContextual',
    'PeerContextual', 'PeerPageQuality', 'PeerLanguage', 'PeerBrandProtection',
    'LotameDemographic', 'LotameAdvancedDemographic', 'LotameBehavioralInterest',
    'LotameInfluencer', 'LotameOffline'
]


class TargetingPage(Controls):
    """Targeting tab in strategy edit"""

    def __init__(self, client, container_cls='-t-targeting-container'):
        super(TargetingPage, self).__init__(client, container_cls)
        self.include = TargetingSection(client, 'include')
        self.exclude = TargetingSection(client, 'exclude')

    def save(self):
        """Save strategy"""
        button = self.client.find_element_by_class_name('-t-button-save-changes')
        self.client.click(button)


class TargetingSection(Controls):
    """ Include or exclude section in targeting page"""

    def __init__(self, client, section):
        container_cls = '-t-%s-widgets' % section
        super(TargetingSection, self).__init__(client, container_cls)
        self.section = section
        self.widgets = {}
        for widget_name in TARGETING_WIDGET_NAMES:
            widget_cls = '-t-widget-{section}-{widget_name}'.format(
                section=section, widget_name=widget_name)
            self.widgets[widget_name] = Widget(client, widget_cls)

    @property
    def _dropdown(self):
        return self.client.find_element_by_class_name('-t-%s-dropdown' % self.section)

    @property
    def visible_widgets(self):
        """
        Get names of displayed widgets

        :rtype: list
        :returns: list of widget names
        """
        widget_xpath = '//div[starts-with(@class, "-t-widget-%s-")]' % self.section
        widgets = self.client.find_elements_by_xpath(widget_xpath)
        return [w.get_attribute('data-widget') for w in widgets]

    def add(self, widget_name):
        """
        Add targeting widget by its name

        :rtype: Widget
        :returns: added widget
        """
        if widget_name not in TARGETING_WIDGET_NAMES:
            raise ValueError('Widget name %s not in %' % (widget_name, TARGETING_WIDGET_NAMES))

        # Open dropdown
        menu_toggle = self._dropdown.find_element_by_class_name('dropdown-toggle')
        self.client.click(menu_toggle)

        # Select targeting widget
        link_cls = '-t-{section}-{widget_name}'.format(section=self.section, widget_name=widget_name)
        menu_element = self._dropdown.find_element_by_class_name(link_cls)
        self.client.click(menu_element)

        # Wait until it is displayed
        widget_cls = '-t-widget-{section}-{widget_name}'.format(section=self.section, widget_name=widget_name)
        self.client.wait_until_displayed(widget_cls)

        return self.widgets[widget_name]


class Widget(Controls):
    """Targeting widget"""

    def __init__(self, client, container_cls):
        self.client = client
        self.container_cls = container_cls

    @property
    def container(self):
        """
        Widgets are removed from DOM after they are removed, so we make sure
        we always have fresh container element
        """
        return self.client.find_element_by_class_name(self.container_cls)

    @property
    def search_input(self):
        """Input in search widget"""
        return self.container.find_element_by_class_name('-t-search-input')

    @property
    def search_dropdown(self):
        """Suggestions dropdown in search widget"""
        return self.container.find_element_by_class_name('tt-dropdown-menu')

    @property
    def search_suggestions(self):
        """Suggestions list in search widget"""
        return self.search_dropdown.find_elements_by_class_name('tt-value')

    def refresh(self):
        """
        Container is looked up on paged each time it is used,
        no need for refreshing element references
        """
        raise NotImplementedError()

    @property
    def checkboxes(self):
        """Get all checkbox elements in widget"""
        return self.container.find_elements_by_class_name('-t-checkbox')

    @property
    def checkbox_groups(self):
        """Get list of checkbox groups available in widget"""
        groups = []
        group_elements = self.container.find_elements_by_class_name('-t-group')
        for group in group_elements:
            groups.append(group.find_elements_by_class_name('-t-checkbox'))
        return groups

    @property
    def tags(self):
        '''
        Returns list of tags in widget.

        :rtype: list
        :returns: list of tag names (strings)
        '''
        def get_text(el):
            el.location_once_scrolled_into_view
            return el.text

        tags = map(get_text, self.container.find_elements_by_class_name('-t-tag'))
        return filter(lambda t: t != '', tags)

    @property
    def is_displayed(self):
        """Checks if container exists in DOM."""
        return self.client.is_present_in_DOM(self.container_cls)
