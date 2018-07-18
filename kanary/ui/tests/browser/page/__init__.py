from selenium.webdriver.support.ui import Select


class Controls(object):
    ''' Base class for all UI elements (widgets). '''

    def __init__(self, client, container_cls):
        self.client = client
        self.container = client.find_element_by_class_name(container_cls)
        self.container_cls = container_cls

    def refresh(self):
        '''
        Refreshses references to the wrapped object
        '''
        self.container = self.client.find_element_by_class_name(self.container_cls)


class BaseFormControls(Controls):
    '''
    Base class that encapsulates common behavior for forms in UI.
    It allows to define only desired inputs in its subclasses while
    this class handles all submitting and filling form behavior.

    Example of usage:

    MyForm(BaseFormControls):

        # Define in init type of fields (checkbox, input, select)
        def __init__(self, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)
            self._checkboxes = ['first']
            self._inputs = ['second']
            self._selects = ['third']

        # Define properties that returns input elements (remember of proper suffix)
        @property
        def first_checkbox(self)

        @property
        def second_input(self)

        @property
        def third_select(self)

    In the test you could do:

    my_form = MyForm(client, '-t-my-form')
    my_form.fill_form(first=True, second='foo', third='some_option)
    my_form.submit()

    '''

    def __init__(self, *args, **kwargs):
        super(BaseFormControls, self).__init__(*args, **kwargs)
        self._checkboxes = []
        self._inputs = []
        self._selects = []

    @property
    def submit_button(self):
        return self.container.find_element_by_class_name('-t-submit')

    def fill_checkboxes(self, **kwargs):
        for checkbox_name in self._checkboxes:
            if kwargs.get(checkbox_name):
                elem = getattr(self, '%s_checkbox' % checkbox_name)
                if kwargs[checkbox_name]:
                    elem.click()

    def fill_inputs(self, **kwargs):
        for input_name in self._inputs:
            if kwargs.get(input_name):
                elem = getattr(self, '%s_input' % input_name)
                elem.send_keys(kwargs[input_name])

    def fill_selects(self, **kwargs):
        for select_name in self._selects:
            if kwargs.get(select_name):
                elem = getattr(self, '%s_select' % select_name)
                elem.select_by_value(kwargs[select_name])

    def fill_form(self, **kwargs):
        self.fill_checkboxes(**kwargs)
        self.fill_inputs(**kwargs)
        self.fill_selects(**kwargs)

    def submit(self):
        self.submit_button.click()


class LoginForm(BaseFormControls):

    def __init__(self, client, container_cls='-t-login-form'):
        super(LoginForm, self).__init__(client, container_cls)
        self._inputs = ['username', 'password']

    @property
    def username_input(self):
        return self.container.find_element_by_class_name('-t-username')

    @property
    def password_input(self):
        return self.container.find_element_by_class_name('-t-password')


class SignupForm(BaseFormControls):

    def __init__(self, client, container_cls='-t-signup-form'):
        super(SignupForm, self).__init__(client, container_cls)

    @property
    def email_input(self):
        return self.container.find_element_by_class_name('-t-input-email')

    @property
    def password_input(self):
        return self.container.find_element_by_class_name('-t-input-password')

    @property
    def repeat_password_input(self):
        return self.container.find_element_by_class_name('-t-input-repeat-password')

    def fill_inputs(self, email, password):
        self.email_input.send_keys(email)
        self.password_input.send_keys(password)
        self.repeat_password_input.send_keys(password)


class CreateProfileForm(BaseFormControls):

    def __init__(self, client, container_cls='-t-create-profile-form'):
        super(CreateProfileForm, self).__init__(client, container_cls)
        self._checkboxes = ['is_agency']
        self._inputs = ['company_name', 'first_name', 'last_name', 'address',
        'city', 'zip_code', 'phone', 'vat']
        self._selects = ['country', 'province']

    @property
    def is_agency_checkbox(self):
        return self.container.find_element_by_class_name('-t-is-agency')

    @property
    def company_name_input(self):
        return self.container.find_element_by_class_name('-t-company-name')

    @property
    def first_name_input(self):
        return self.container.find_element_by_class_name('-t-first-name')

    @property
    def last_name_input(self):
        return self.container.find_element_by_class_name('-t-last-name')

    @property
    def address_input(self):
        return self.container.find_element_by_class_name('-t-address')

    @property
    def city_input(self):
        return self.container.find_element_by_class_name('-t-city')

    @property
    def zip_code_input(self):
        return self.container.find_element_by_class_name('-t-zip-code')

    @property
    def country_select(self):
        select_elem = self.container.find_element_by_class_name('-t-country')
        return Select(select_elem)

    @property
    def province_select(self):
        select_elem = self.container.find_element_by_class_name('-t-province')
        return Select(select_elem)

    @property
    def phone_input(self):
        return self.container.find_element_by_class_name('-t-phone')

    @property
    def vat_input(self):
        return self.container.find_element_by_class_name('-t-vat')

    @property
    def submit_button(self):
        return self.container.find_element_by_class_name('-t-submit')

    def get_invalid_inputs(self):
        '''
        :returns: list of input names that doesn't pass validation
        '''
        invalid_inputs = []

        for input_name in self._inputs:
            input_elem = getattr(self, '%s_input' % input_name)
            if 'input-error' in input_elem.get_attribute('class'):
                invalid_inputs.append(input_name)

        return invalid_inputs
