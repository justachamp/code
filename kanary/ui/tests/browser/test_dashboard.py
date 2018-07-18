import pytest


pytestmark = [
    pytest.mark.nondestructive,
    pytest.mark.django_db,
    pytest.mark.selenium,
]


@pytest.mark.usefixtures('fill_db')
def test_timeline_creative_link(client, user):
    ''' Check if creative audited event is correctly clickable on timeline '''

    # mark some creative as audited
    creative_0 = user.account.creative_set.all()[0]
    creative_0.appnexus_set_audited()
    creative_0.save()

    # refresh dashboard state
    client.refresh()
    client.wait_for_xhr()

    # click event's header on time-line
    event_box = client.find_elements_by_link_text(creative_0.name)[0]
    client.click(event_box)

    # check if we are redirected into storage item
    client.check_sidebar_title('Storage')

    titles = client.find_elements_by_class_name('-t-title')
    assert creative_0.name in map(lambda t: t.text, titles)


class LiveView():
    def __init__(self, client):
        self.client = client
        self.container = self.client.find_element_by_class_name('-t-liveview')
        self.drill_selector = self.container.find_element_by_css_selector('.dropdown.-t-liveview-drill')

    @property
    def table(self):
        return self.container.find_element_by_css_selector('tbody').text

    def wait_for_refresh(self):
        row = self.container.find_element_by_css_selector('tbody tr')
        self.client.wait_until_disappeared(row)

    def select_drill(self, drill):
        ''' Select a given drill and wait for refreshing '''
        self.drill_selector.click()
        self.container.find_element_by_link_text(drill).click()
        self.wait_for_refresh()


@pytest.mark.usefixtures('running_app')
def test_liveview(client):
    '''
    Test changing and refreshing liveview.
    API details are checked in separate test
    '''
    liveview = LiveView(client)
    liveview.wait_for_refresh()
    for drill in ['Advert', 'Strategy', 'Campaign']:
        liveview.select_drill(drill)
        # Check if table is displayed
        assert liveview.table
        # Check if it is refreshed automatically
        liveview.wait_for_refresh()
