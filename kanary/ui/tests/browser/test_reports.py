import pytest

from ui.tests.initial_datafixtures import default_strategies
from etc.constants import FRONTEND_REPORTS_ITEMS_LIMIT
from etc import dimensions

from ui.campaign.models import Strategy
from ui.tests.browser.page.strategy import TargetingPage


class ReportPage(object):

    def __init__(self, client):
        self.client = client
        self.dimensions_menu = dimensions.named_dimensions_report.values()
        self.refresh_bindings()

    def refresh_bindings(self):
        ''' Refresh HTML bindings after DOM update '''
        self.table = self.client.find_element_by_class_name('-t-reports-table')
        self.tablerows = self.table.find_elements_by_class_name('-t-row')

    def change_report(self, dimension):
        '''
        Change report by using dimensions dropdown menu.

        :param str dimension: dimension label eg. Domain
        '''
        menu_toggle = self.client.find_element_by_css_selector('.-t-dimensions .dropdown-toggle')
        self.client.click(menu_toggle)
        dimension_index = self.dimensions_menu.index(dimension)
        menu_element = self.client.find_elements_by_css_selector('.-t-dimensions .dropdown-menu a')[dimension_index]
        menu_element.location_once_scrolled_into_view
        menu_element.click()
        self.client.wait_for_xhr()
        self.refresh_bindings()

    def click_on_first_button(self):
        '''
        Click on whitelist/blacklist button in first row.

        :rtype: tuple
        :returns: (label of clicked element, button label before click)
        '''
        button = self.tablerows[0].find_element_by_tag_name('a')
        element_label = self.tablerows[0].find_element_by_class_name('-t-col-name').text
        button.click()
        self.client.wait_for_xhr()
        return element_label, button.text

    def check_whitelist_blacklist_button_existence(self):
        '''
        Checking if whitelist/blacklist button exists in first row.

        :rtype: boolean
        '''
        for tablerow in self.tablerows:
            if tablerow.text == 'Unknown':
                continue
            if 'BLACKLIST' in tablerow.text:
                return True

        return False

    def click_first_in_report(self, dimension):
        '''
        Blacklist or whitelist first posision in report for given dimension.

        :param str dimension: eg. age_group.
        :rtype: tuple
        :returns: (label of clicked element, button label before click)
        '''
        self.change_report(dimensions.named_dimensions_report[dimension])
        return self.click_on_first_button()

    def edit_strategy(self):
        self.client.click_on_class('edit-strategy')


class CampaignReportPage(ReportPage):

    def __init__(self, client):
        super(CampaignReportPage, self).__init__(client)
        self.dimensions_menu.insert(0, 'Strategy')


class StrategyReportPage(ReportPage):

    def __init__(self, client):
        super(StrategyReportPage, self).__init__(client)
        self.dimensions_menu.insert(0, 'Advert')


def change_date_range(client, range_label):
    '''
    Changing date range with datepicker.

    :param str range_label: name of range in datepicker (Today, Yesterday, etc)
    '''
    RANGES_MAP = {
        'Today': 0,
        'Yesterday': 1,
    }
    datepicker = client.find_element_by_class_name('-t-datepicker')
    client.click(datepicker)
    ranges = client.find_elements_by_css_selector('.-t-ranges li')
    custom_range = ranges[RANGES_MAP[range_label]]
    client.click(custom_range)


def check_column(client, row_numer, metric_slug):
    '''
    Checking value of single metric in table row.

    :param int row_numer: numer of row in table tbody
    :param str metric_slug: metric slug used as cell class name
    '''
    row = client.find_element_by_css_selector('.row{0}'.format(row_numer))
    field = row.find_element_by_class_name('-t-col-{0}'.format(metric_slug))
    field.location_once_scrolled_into_view
    return int(field.text)


@pytest.mark.usefixtures('fake_strategy_reports_inserter')
def test_report_campaign_overview(client, fake_reports_data):
    ''' Testing table with metrics for campaign '''

    # 1. Go to campaign
    client.menu_jump_to('campaigns')
    client.click_on_class('campaign')

    # 2. Check numer of strategies in rows
    table = client.find_element_by_class_name('-t-reports-table')
    number_of_rows = len(table.find_elements_by_class_name('-t-row'))
    assert number_of_rows == len(default_strategies)

    # 3. Check numer of impressions for first strategy
    imp = check_column(client, 0, 'imp')
    imp_sum = sum(v['imp'] for v in fake_reports_data)
    assert imp == imp_sum

    # 4. Check number of clicks for first strategy
    clk = check_column(client, 0, 'clk')
    clk_sum = sum(v['clk'] for v in fake_reports_data)
    assert clk == clk_sum

    # 5. Change datepicker date range to Today
    change_date_range(client, 'Today')

    # 6. Check numer of impressions for first strategy
    imp = check_column(client, 0, 'imp')
    imp_sum = fake_reports_data[2]['imp']
    assert imp == imp_sum

    # 7. Change datepicker date range to Yesterday and check impressions
    change_date_range(client, 'Yesterday')
    imp = check_column(client, 0, 'imp')
    imp_sum = sum(v['imp'] for v in fake_reports_data[:2])
    assert imp == imp_sum


@pytest.mark.usefixtures('fake_strategy_reports_inserter_incremented')
def test_report_sorting(client):
    ''' Testing table sorting '''

    def get_values_from_column(table, metric_slug):
        '''
        Getting text value for each cell in column
        :param WebElement table: selenium table object
        :param string metric_slug: metric slug used as class name
        :returns: list of strings
        :rtype: list
        '''
        column_values = table.find_elements_by_class_name('-t-col-{0}'.format(metric_slug))
        values = []
        for label in column_values:
            label.location_once_scrolled_into_view
            values.append(label.text)
        return values

    # 1. Go to campaign
    client.menu_jump_to('campaigns')
    client.click_on_class('campaign')

    table = client.find_element_by_class_name('-t-reports-table')

    # 2. Sorting by impressions
    imp_header = table.find_element_by_class_name('column0')
    # asc
    client.click(imp_header)
    assert ['106', '109'] == get_values_from_column(table, 'imp')
    # desc
    client.click(imp_header)
    assert ['109', '106'] == get_values_from_column(table, 'imp')

    # 3. Sorting by CTR %
    ctr_header = table.find_element_by_class_name('column3')

    # asc
    client.click(ctr_header)
    assert ['99.06', '99.08'] == get_values_from_column(table, 'ctr')
    # desc
    client.click(ctr_header)
    assert ['99.08', '99.06'] == get_values_from_column(table, 'ctr')


@pytest.mark.usefixtures('fake_strategy_gender_reports_inserter')
def test_report_campaign_overview_gender_reports(client, fake_reports_data):
    ''' Testing table with metrics with gender dimension  '''

    # 1. Go to campaign
    client.menu_jump_to('campaigns')
    client.click_on_class('campaign')

    report_page = CampaignReportPage(client)

    # 2. Click on dimensions dropdown and select gender option
    report_page.change_report('Gender')

    table = client.find_element_by_class_name('-t-reports-table')
    rows = table.find_elements_by_class_name('-t-row')

    # 3. Iterate rows and check values
    for row in rows:
        name = row.find_element_by_class_name('-t-col-name').text
        assert name in ['Male', 'Female', 'Other', 'Unspecified']

        imp = row.find_element_by_class_name('-t-col-imp').text
        imp_from_fake_data = sum(row['imp'] for row in fake_reports_data)
        assert imp == str(imp_from_fake_data)


@pytest.mark.usefixtures('fake_strategy_domains_reports_inserter')
def test_report_load_more(client):
    ''' Testing 'Load more' of domain reports table '''

    # 1. Go to campaign
    client.menu_jump_to('campaigns')
    client.click_on_class('campaign')

    report_page = CampaignReportPage(client)

    # 2. Click on dimensions dropdown and select domain option
    report_page.change_report('Domain')

    table = client.find_element_by_class_name('-t-reports-table')
    number_of_rows = len(table.find_elements_by_class_name('-t-row'))
    assert number_of_rows == FRONTEND_REPORTS_ITEMS_LIMIT

    for i in range(2, 5):
        button = client.find_element_by_class_name('-t-load-more')
        button.location_once_scrolled_into_view
        button.click()

        client.wait_for_xhr()

        number_of_rows = len(table.find_elements_by_class_name('-t-row'))
        assert number_of_rows == i * FRONTEND_REPORTS_ITEMS_LIMIT


@pytest.mark.usefixtures('fake_strategy_reports_inserter', 'running_strategies')
def test_report_graying_out_not_running_items(client):
    ''' Testing table with metrics for campaign '''

    # 1. Go to campaign
    client.menu_jump_to('campaigns')
    client.click_on_class('campaign')

    # 2. Check if we have active rows
    table = client.find_element_by_class_name('-t-reports-table')
    table.location_once_scrolled_into_view
    number_of_rows = len(table.find_elements_by_css_selector('.-t-row:not(.muted)'))
    assert number_of_rows == len(default_strategies)

    # 3. Disable campaign
    client.find_element_by_class_name('-t-campaign-switcher').click()
    client.refresh()

    # 4. Check if rows are muted
    table = client.find_element_by_class_name('-t-reports-table')
    number_of_rows = len(table.find_elements_by_css_selector('.-t-row.muted'))
    assert number_of_rows == len(default_strategies)


@pytest.mark.xfail(reason='KANARY-2394')
@pytest.mark.usefixtures('fake_strategy_multiple_reports_inserter')
def test_report_strategy_whitelist_blacklist(client):
    '''
    Testing:
        - whitelist/blacklist buttons appearance in strategy reports
        - whitelist/blacklist side effects in strategy targeting
    '''

    # go to strategy reports
    client.menu_jump_to('campaigns')
    client.click_on_class('campaign')
    client.click_on_class('strategy')

    # page object for reports
    report_page = StrategyReportPage(client)

    def search_dimension_by_label(dimension_label):
        '''
        Changing dimension labels for dimension names

        :param str dimension_label: eg. Age group
        :rtype: string
        :returns: dimension name eg. age_group
        '''
        for dimension, label in dimensions.named_dimensions_report.items():
            if dimension_label == label:
                return dimension
        return dimension_label.lower()

    # check whitelist/blacklist buttons appearance in each report
    for dimension_label in report_page.dimensions_menu:
        report_page.change_report(dimension_label)
        dimension = search_dimension_by_label(dimension_label)
        button_should_appear = dimension in Strategy.DIMENSIONS_TO_FIELDS_MAP.keys()
        assert button_should_appear == report_page.check_whitelist_blacklist_button_existence()

    def get_nested_tag_name(tagname):
        '''
        Getting nested tag name from tag in tree-related widgets:

        :param str tag name: full tagname with nested tags (Eg. Technology & Computing > 3-D Graphics)
        :rtype: string
        :returns: tag name of last nested tag (Eg. 3-D Graphics)
        '''
        return tagname.split(' > ')[-1]

    # blacklist OS
    os_name, button_text = report_page.click_first_in_report(dimensions.os)
    assert button_text == 'WHITELIST'

    # whitelist OS
    os_name, button_text = report_page.click_on_first_button()
    assert button_text == 'BLACKLIST'

    # blacklist Content Category
    content_category_name, button_text = report_page.click_first_in_report(dimensions.content_category)
    assert button_text == 'WHITELIST'

    # blacklist Proximic Contextual
    proximic_contextual, button_text = report_page.click_first_in_report(dimensions.proximic_contextual)
    assert button_text == 'WHITELIST'

    # blacklist Lotame Demographic
    lotame_demographic, button_text = report_page.click_first_in_report(dimensions.lotame_demographic)
    assert button_text == 'WHITELIST'

    # go to targeting
    report_page.edit_strategy()
    client.click_on_class('sidebar-targeting')

    # page object for targeting
    targeting_page = TargetingPage(client)

    # checking included and excluded widgets
    assert targeting_page.include.visible_widgets == ['Os']

    assert sorted(targeting_page.exclude.visible_widgets) == \
        sorted(['Content', 'ProximicContextual', 'LotameDemographic'])

    # checking included OS
    assert os_name in targeting_page.include.widgets['Os'].tags

    # checking excluded Content Category
    assert get_nested_tag_name(content_category_name) in targeting_page.exclude.widgets['Content'].tags

    # checking excluded Proximic Contextual
    assert get_nested_tag_name(proximic_contextual) in targeting_page.exclude.widgets['ProximicContextual'].tags

    # checking excluded Lotame Demographic
    assert get_nested_tag_name(lotame_demographic) in targeting_page.exclude.widgets['LotameDemographic'].tags
