from urlparse import urljoin, urlparse

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    NoSuchElementException, StaleElementReferenceException, TimeoutException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of, element_to_be_clickable
from selenium.webdriver.remote.webelement import WebElement

from etc.config import settings


TIMEOUT = settings.test_selenium_timeout


class Client(object):

    ''' Wraps mozwebqa and selenium with a useful helpers '''

    def __init__(self, mozwebqa, live_server):
        self.mozwebqa = mozwebqa
        self.selenium = mozwebqa.selenium
        self.live_server = live_server

    def __getattr__(self, attr):
        return getattr(self.selenium, attr)

    def get_nowait(self, url):
        self.selenium.get(urljoin(unicode(self.live_server), url))

    def get(self, url):
        self.get_nowait(url)
        self.wait_for_xhr()

    @property
    def current_path(self):
        return urlparse(self.current_url).path

    def wait_until(self, condition, timeout=TIMEOUT, error=None):
        cond = lambda selenium, *args, **kwargs: condition(*args, **kwargs)
        return WebDriverWait(self.selenium, timeout).until(cond, error)

    def wait_until_ec(self, condition, timeout=TIMEOUT, error=None):
        return WebDriverWait(self.selenium, timeout).until(condition, error)

    def wait_until_not(self, condition, timeout=TIMEOUT, error=None):
        cond = lambda selenium, *args, **kwargs: condition(*args, **kwargs)
        return WebDriverWait(self.selenium, timeout).until_not(cond, error)

    def wait_until_not_ec(self, condition, timeout=TIMEOUT, error=None):
        return WebDriverWait(self.selenium, timeout) \
            .until_not(condition, error)

    def wait_for_xhr(self):
        ''' Waits for animations and XHR requests to finish '''
        self.wait_for_sidebar()
        self.wait_for_content()

        def ajax_done():
            return self.execute_script('return jQuery.active') == 0

        self.wait_until(ajax_done)

    def wait_for_sidebar(self):
        self.wait_until_not(self.sidebar_is_loading)

    def wait_for_content(self):
        self.wait_until_not(self.content_is_loading)

    def wait_for_uploader(self):
        self.wait_until_not(self.uploader_is_sending)

    def wait_for_css(self, element, attribute, value):
        '''
        Wait until element's css attribute has given value
        '''
        def attribute_equals():
            return element.value_of_css_property(attribute) == value
        self.wait_until(attribute_equals)
        self.wait_for_xhr()

    def wait_for_tray(self, id, hide=False):
        '''
        Wait until tray has slided into the view
        :param str id: id of tray element (trayLandingPages or trayCreatives)
        :param bool hide: if set to True then function waits until tray is not
         visible.
        '''
        tray = self.find_element_by_id(id)

        if hide:
            self.wait_for_css(tray, 'right', '-417px')
            return

        self.wait_for_css(tray, 'right', '0px')

    def wait_for_modal(self, hide=False):
        modal = self.find_element_by_id('modal')

        if hide:
            def hide_modal():
                return self.is_modal_hidden(modal)
            self.wait_until(hide_modal)
            return

        self.wait_for_css(modal, 'right', '0px')

    def wait_for_widget_action(self, widget_content, expanded):
        '''
        Checks if given widget is in collapsed or expanded state.
        '''
        def widget_collapsed():
            return widget_content.value_of_css_property('height') == '0px'

        if not expanded:
            self.wait_until(widget_collapsed)
            return

        self.wait_until_not(widget_collapsed)

    def wait_until_displayed(self, selector, by='class_name', until=True):
        '''
            Waits until element is displayed

            :param str selector: element selector string or WebElement
            :param str by: type of selector as for find_element_by_* mehtods
            :param bool until: whether to wait until, or until_not
        '''
        if isinstance(selector, basestring):
            find_element = getattr(self.selenium, 'find_element_by_' + by)
            element = find_element(selector)
        else:
            element = selector

        # make sure it is in view
        element.location_once_scrolled_into_view

        visible = visibility_of(element)

        if until:
            self.wait_until_ec(visible)
        else:
            self.wait_until_not_ec(visible)

        self.wait_for_xhr()

    def wait_until_disappeared(self, element):
        '''Wait until the element has disappeared.'''

        def stale():
            try:
                element.location
            except StaleElementReferenceException:
                return True

            return False

        self.wait_until(stale)

    def sidebar_is_loading(self):
        return self.execute_script("""
            return (window['sidebar_is_loading'] != void 0 ?
                    sidebar_is_loading : true)""")

    def content_is_loading(self):
        return self.execute_script("""
            return (window['content_is_loading'] != void 0 ?
                    content_is_loading : true)""")

    def uploader_is_sending(self):
        return self.execute_script("return window['file_is_uploaded']")

    def click(self, element):
        self.wait_for_xhr()
        element.location_once_scrolled_into_view
        self.wait_for_xhr()
        element.click()
        self.wait_for_xhr()

    def click_on_class(self, class_name, bare=False, scroll=False):
        # if bare=True the -t- prefix will not be added
        if not bare:
            class_name = '-t-%s' % class_name
        el = self.find_element_by_class_name(class_name)
        if scroll:
            el.location_once_scrolled_into_view
        self.click(el)

    def click_on_button(self, class_name):
        class_name = 'button-%s' % class_name
        self.click_on_class(class_name)

    def find_by_text(self, elements_list, text):
        """
        Find element on list by text

        ..warning:: Scrolls to each element on list
        :param list elements_list: list of Element
        :param str text: text to find

        :returns Matched element
        :rtype: Element

        :raises Exception if 0 or more than 1 element is matched
        """
        def by_text(el):
            el.location_once_scrolled_into_view
            return el.text == text

        matched = filter(by_text, elements_list)
        if len(matched) != 1:
            raise Exception('Found %s elements with text %s' % (len(matched), text))
        return matched[0]

    def get_menu_link(self, item):
        '''Tries to gets link with given item/hash'''
        return self.find_element_by_class_name('-t-menu-%s' % item)

    def menu_jump_to(self, section_name):
        '''Click only on links on only inside in menu'''
        self.click(self.get_menu_link(section_name))

    def open_create_new_campaign(self):
        '''
            Goes to create new campaign
        '''
        self.menu_jump_to('campaigns')
        self.click(self.find_element_by_class_name('-t-new-campaign'))

    def get_content_elem(self, classname):
        '''Tries to get elements which are within content section'''
        selector = "div.content-active .%s" % classname
        return self.selenium.find_element_by_css_selector(selector)

    def get_input(self, name):
        return self.get_content_elem('-t-input-%s' % name)

    def get_input_val(self, name):
        input_elem = self.get_input(name)
        return input_elem.get_attribute('value')

    def get_submit(self):
        return self.get_content_elem('-t-button-submit')

    def get_checkbox(self, element):
        return element.find_element_by_css_selector('.checkbox')

    def is_checked(self, checkbox):
        return 'checked' in checkbox.get_attribute('class')

    def is_not_checked(self, checkbox):
        return 'checked' not in checkbox.get_attribute('class')

    def is_present_in_DOM(self, element_class):
        """
        Checks if element with given class exists in DOM.
        """
        elements = self.find_elements_by_class_name(element_class)
        return len(elements) >= 1

    def send_keys(self, input_cls_or_elem, val, clear=False, focus_css_selector='header.body span'):
        """
        Send keys to input

        :param (str, WebElement) input_cls_or_elem: either element or input class
        :param str val: value to insert into input field
        :param bool clear: whether to clear input first
        :param (bool, str) focus_css_selector: loose focus by clicking somewhere in page. Pass false to disable.

        """

        if not isinstance(input_cls_or_elem, WebElement):
            input_element = self.get_input(input_cls_or_elem)
        else:
            input_element = input_cls_or_elem

        input_element.location_once_scrolled_into_view

        if clear:
            input_element.clear()

        input_element.send_keys(val)
        self.wait_for_xhr()

        if focus_css_selector:
            self.loose_focus(focus_css_selector)

    def close_modal(self):
        self.click_on_class('close-modal')
        self.wait_for_modal(hide=True)

    def loose_focus(self, focus_css_selector='header.body span'):
        """
        Loose focus by clicking on other specified element.

        :param str focus_css_selector: css selector to loose focus on.

            Default is span contains username only, should be unclickable,
            that's why it's good place to rest click for loosing focus
            and it should be visible, and clickable anywhere, where user logs in
        """

        # this span contains username only, should be unclickable,
        # that's why it's good place to rest click for loosing focus
        # and it should be visible, and clickable anywhere, where user logs in
        self.wait_until_ec(element_to_be_clickable([By.CSS_SELECTOR, focus_css_selector]))
        self.find_element_by_css_selector(focus_css_selector).click()

    def get_sidebar_elem(self, classname):
        '''Tries to get elements which are within sidebar'''
        sidebar_select = 'section.sidebar-active'
        element_select = '%s .%s' % (sidebar_select, classname)
        self.wait_for_xhr()
        return self.find_element_by_css_selector(element_select)

    def get_title(self):
        '''Gets title of currently selected sidebar'''
        try:
            return self.get_sidebar_elem('-t-title').text
        except (NoSuchElementException, AttributeError):
            title = ''
        return title

    def get_modal_errors(self):
        '''
        Returns list of errors listed in modal
        '''
        modal = self.find_element_by_id('modal')
        return [
            error.text for error in modal.find_elements_by_class_name(
                '-t-error-message'
            )
        ]

    def check_sidebar_title(self, title):
        def has_title():
            try:
                element_title = self.get_title()
            except (NoSuchElementException, StaleElementReferenceException):
                element_title = ''
            return element_title == title
        error = u'Cannot load %s' % title
        self.wait_until(has_title, error=error)

    def is_header_shown(self, header_text):
        '''Checks if header with given text is shown in sidebar section'''
        return self.get_title() == header_text

    def is_step_shown(self, header_text):
        '''Checks if header with given text is shown in content section'''
        try:
            title = self.get_content_elem('-t-title')
            return title.text == header_text
        except (NoSuchElementException, StaleElementReferenceException):
            return False

    def is_modal_hidden(self, element):
        '''Checks if element isn' totally hidden on side of browser what
        makes it invisible for normal user but totally visible for js
        :property element: modal element'''

        size, _ = self.get_float_property(element, 'width')
        side, side_type = self.get_float_property(element, 'right')
        # When layer is fully hidden then margin should be negative
        # and should have value >= of element's width/height
        if side < 0:
            if abs(side) >= size:
                return True

        # Special case for different selenium drivers which returns
        # right as percent value
        if side_type == '%' and side == -100.0:
            return True

        return False

    def get_by_class(self, element, classname):
        selector = "//*[contains(@class, '%s')]" % classname
        return element.find_element_by_xpath(selector)

    def get_by_tagname(self, element, tag):
        return element.find_element_by_tag_name(tag)

    def show_file_input(self, input_name):
        template_vars = dict(name=input_name)
        show_input_js = "return $('input[name=\"%(name)s\"]')"\
            ".css('width', '10px').css('height', '10px')"\
            ".css('top', '0').css('left', '0');" % template_vars
        self.execute_script(show_input_js)

    def get_float_property(self, element, property_):
        '''Returns given property from given element, casted to float.
           :return tuple: return tuple with numerical value and type of value.
           Currently supports only px and %'''
        value = element.value_of_css_property(property_)
        value_type = 'px'
        if '%' in value:
            value_type = '%'
        return float(value.replace('px', '').replace('%', '')), value_type

    def check_input_value(self, input_, value):
        self.wait_until(lambda: input_.get_attribute('value') == value)

    def class_exists(self, element, class_name, appeared=True):

        def check_if_appeared():
            if appeared:
                return class_name in element.get_attribute('class')
            return class_name not in element.get_attribute('class')

        try:
            self.wait_until(check_if_appeared)
        except TimeoutException:
            return False

        return True

    def has_class(self, element, class_name):
        '''Returns True if WebElement has given class_name'''

        return self.class_exists(element, class_name)

    def has_not_class(self, element, class_name):
        '''Returns True if WebElement doesn't has given class_name'''

        return self.class_exists(element, class_name, appeared=False)
