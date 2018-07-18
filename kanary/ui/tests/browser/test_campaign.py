import pytest

from ui.campaign.models import Campaign
from ui.account.models import User


def open_datepicker(client, datepicker):
    selector = '.-t-controls-%s .icon-calendar' % (datepicker)
    client.click(client.find_element_by_css_selector(selector))


def select_next_day(client, datepicker):
    '''
        :param WebElement datepicker: selected datepicker element
    '''
    client.wait_until_displayed(datepicker)

    today = datepicker.find_element_by_css_selector('.day.active')

    days = datepicker.find_elements_by_xpath(
        './/td[not(contains(@class, "old")) and contains(@class, "day")]')

    for day in days:
        if days.index(day) > days.index(today):
            client.click(day)
            break


@pytest.mark.usefixtures('fill_db')
def test_create_campaign(client, user):
    '''
        After sign in click campaign button.
        Click  CREATE NEW CAMPAIGN.
        Change the name of campaign.
        Select some date from calendar. (use picker, don't type)
        Select some time from time picker (use picker, don't type)
        Input any site.
        Click Next Step.
        Setup total budget to 0.
        Goto capping.
        Save changes -  activate campaings.
        click campaigns button in menu.
        assert text existience:
            'You have currently 1 active campaign out of 1 in total.'
        Assert campaign in database reflects inputed data.
    '''
    campaign_title = 'Awsome campaign'
    wait_step2_budget = lambda: client.is_step_shown('Budget')
    wait_step3_conversion = lambda: client.is_step_shown('Conversion tracker')
    wait_step4_capping = lambda: client.is_step_shown('Capping')
    campaigns_when_started = user.account.campaign_set.count()

    client.open_create_new_campaign()
    client.send_keys(
        'campaign-name', campaign_title, clear=True, focus_css_selector='div.-t-campaign-name label')

    client.check_sidebar_title(campaign_title)

    open_datepicker(client, 'start-date')
    # should be two pickers on the website
    pickers = client.find_elements_by_class_name('datepicker')
    assert len(pickers) == 2

    # first datepicker would be the one for startdate
    select_next_day(client, pickers[0])
    client.loose_focus(focus_css_selector='div.-t-start-date label')
    assert not pickers[0].is_displayed()

    open_datepicker(client, 'end-date')

    # should be two pickers on the website
    pickers = client.find_elements_by_class_name('datepicker')
    assert len(pickers) == 2

    # first datepicker would be the one for startdate
    select_next_day(client, pickers[1])
    client.loose_focus(focus_css_selector='div.-t-end-date label')
    assert not pickers[1].is_displayed()

    client.send_keys('default-landing-page', 'http://www.onet.pl',
        focus_css_selector='div.-t-landing-page label')

    # step 2 - budget
    client.click_on_button('next')
    client.wait_until(wait_step2_budget)

    client.send_keys('budget-total', '0', focus_css_selector=False)

    # step 3 - conversion tracker
    client.click_on_button('next')
    client.wait_until(wait_step3_conversion)

    client.send_keys('conversion-name', 'New conversion', clear=True)
    client.send_keys('conversion-value', '1', clear=True)

    # step 4 - capping
    client.click_on_button('next')
    client.wait_until(wait_step4_capping)

    client.click_on_button('save')

    client.wait_until(lambda: client.is_header_shown(campaign_title))

    client.wait_until_displayed('-t-menu-campaigns')
    client.menu_jump_to('campaigns')
    client.check_sidebar_title('Campaigns')

    client.wait_until_displayed('-t-campaigns-counter')
    counter = client.find_element_by_class_name('-t-campaigns-counter')

    assert counter.text ==\
        'You have currently 1 active campaign out of %d in total.'\
        % (campaigns_when_started + 1)

    assert Campaign.objects_visible.filter(account__users=user).count() == \
        (campaigns_when_started + 1)

    campaign = Campaign.objects.get(name=campaign_title)
    assert campaign.budget_total == 0

    # check unread events count
    # should be one
    dashboard_href = client.find_element_by_class_name('-t-menu-dashboard')
    user = User.objects.get(pk=user.pk)
    assert int(dashboard_href.text) == user.unread_events_count
    dashboard_href.click()

    # should be zero
    client.wait_for_xhr()
    dashboard_href = client.find_element_by_class_name('-t-menu-dashboard')
    user = User.objects.get(pk=user.pk)
    assert int(dashboard_href.text) == user.unread_events_count


@pytest.mark.usefixtures('fill_db')
def test_create_activate_campaign(client):
    '''
        After sign in click campaign button.
        Click  CREATE NEW CAMPAIGN.
        Click Activate campaign
        Click OK in Modal.
    '''

    client.open_create_new_campaign()

    client.click(client.get_sidebar_elem('-t-button-activate'))

    client.wait_until_displayed('modal', by='id')
    client.click(client.find_element_by_css_selector('#modal a'))

    # impossible to get in firefox 22 with selenium 2.33
    # and with chrome with chromedriver smaller than < 2.1
    # self.wait_until_displayed(client, 'modal', by='id', until=False)

    def modal_is_scrolled():
        return client.is_modal_hidden(client.find_element_by_id('modal'))

    client.wait_until(modal_is_scrolled)


def goto_some_campaign_view(client, user):
    '''
    Jumps to campaigns list, and then clicks on some campaign based on
    campaign name taken from db.
    '''
    client.menu_jump_to('campaigns')

    campaign = user.account.campaign_set.order_by('?')[0]
    campaign_list = client.get_sidebar_elem('-t-campaigns-list')
    selector = './/span[text()="%s"]' % campaign.name

    client.click(campaign_list.find_element_by_xpath(selector))
    return campaign


@pytest.mark.usefixtures('fill_db')
def test_campaign_summary_display(client, user):
    '''
        given we've got some campaigns in db,
        go to list of campaigns,
        click on the campaign with name,
        assert campaign `name` is displayed and correct
    '''
    campaign = goto_some_campaign_view(client, user)

    assert client.get_title() == campaign.name
    assert client.get_content_elem('-t-title').text == campaign.name


@pytest.mark.usefixtures('fill_db')
def test_campaign_deactivation_campaign_view(client, user):
    '''
        given we've got some campaign in db
        goto campaign view
        deactivate this campaign
        check on campaigns list if it's deactivated
    '''
    campaign = goto_some_campaign_view(client, user)

    client.find_element_by_class_name('-t-campaign-switcher').click()

    client.menu_jump_to('campaigns')
    deactivated_class = '-t-campaign-deactivated-%d' % campaign.pk
    client.find_element_by_class_name(deactivated_class)
