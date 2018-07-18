import pytest

from ui.campaign.models import Site


@pytest.mark.usefixtures('fill_db')
def test_site_autocomplete_campaign(client, user):

    client.open_create_new_campaign()

    client.send_keys('default-landing-page', 'htt', focus_css_selector=False)
    suggestions = client.find_elements_by_class_name('tt-value')

    assert len(suggestions) == Site.objects.filter(owner_id=user.account.id).count()


@pytest.mark.usefixtures('fill_db')
def test_site_autocomplete_strategy(client, user):

    client.menu_jump_to('campaigns')

    client.click(client.get_sidebar_elem('-t-campaign'))
    client.click(client.get_sidebar_elem('-t-button-new'))

    client.click(client.get_sidebar_elem('-t-sidebar-landing'))
    client.click_on_button('add')

    client.send_keys('landing-page', 'htt', focus_css_selector=False)
    client.wait_until(lambda: client.find_elements_by_class_name('tt-value'))

    suggestions = client.find_elements_by_class_name('tt-value')
    assert len(suggestions) == Site.objects.filter(owner_id=user.account.id).count()

    client.click(client.get_sidebar_elem('-t-sidebar-creatives'))
    client.click_on_button('add')

    client.send_keys('landing-site', 'htt', focus_css_selector=False)
    client.wait_until(lambda: client.find_elements_by_class_name('tt-value'))

    suggestions = client.find_elements_by_class_name('tt-value')
    assert len(suggestions) == Site.objects.filter(owner_id=user.account.id).count()
