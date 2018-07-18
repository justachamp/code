from datetime import datetime, timedelta

import pytest

# test cases for checking if object is ready to bid.
# just a few examples are given, feel free to extend this by new tests


def set_running_campaign(campaign, creative):
    creative.appnexus_status = 'a'
    creative.save()

    campaign.start_UTC = datetime.utcnow()
    campaign.end_UTC = datetime.utcnow() + timedelta(days=30)
    campaign.save()


@pytest.mark.django_db
def test_advert_is_running(state_app):
    campaign = state_app.models['campaign']['I\'m a fruit']
    creative = state_app.models['creative']['creative_image_1']
    advert = state_app.models['advert']['ad_lemon']

    set_running_campaign(campaign, creative)

    # what if total budget has been exceeded?
    campaign.budget_spent = campaign.budget_total
    campaign.save()
    assert advert.state.is_running is False

    campaign.budget_spent = 1
    campaign.save()
    assert advert.state.is_running is True

    creative.appnexus_status = 'p'
    creative.save()
    assert advert.state.is_running is False

    creative.appnexus_status = 'a'
    creative.save()
    assert advert.state.is_running is True

    # what if we deleted campaign?
    campaign.is_deleted = True
    campaign.save()
    assert advert.state.is_running is False

    # what if we deleted strategy and not campaign?
    campaign.is_deleted = False
    campaign.save()
    assert advert.state.is_running is True
    advert.strategy.is_deleted = True
    advert.strategy.save()
    assert advert.state.is_running is False


@pytest.mark.django_db
def test_campaign_deactivation(state_app):
    '''
    Tests if campaign deactivation has correct impact on
    is_running property of related objects.
    '''
    campaign = state_app.models['campaign']['I\'m a fruit']
    creative = state_app.models['creative']['creative_image_1']
    advert = state_app.models['advert']['ad_lemon']

    set_running_campaign(campaign, creative)
    assert advert.state.is_running is True

    campaign.is_paused = True
    campaign.save()
    assert advert.state.is_running is False


@pytest.mark.django_db
def test_strategy_deactivation(state_app):
    '''
    Tests if strategy deactivation has correct impact on
    is_running property of related objects.
    '''
    campaign = state_app.models['campaign']['I\'m a fruit']
    creative = state_app.models['creative']['creative_image_1']
    strategy = state_app.models['strategy']['Hello this is Citrus']
    advert = state_app.models['advert']['ad_lemon']

    set_running_campaign(campaign, creative)
    assert advert.state.is_running is True

    strategy.is_paused = True
    strategy.save()
    assert advert.state.is_running is False


@pytest.mark.django_db
def test_account_balance(state_app):
    """
    Test if changing account balance,
    has correct impact on is_running property
    on advert, strategy and campaign
    """
    campaign = state_app.models['campaign']['I\'m a fruit']
    creative = state_app.models['creative']['creative_image_1']
    strategy = state_app.models['strategy']['Hello this is Citrus']
    advert = state_app.models['advert']['ad_lemon']
    account = campaign.account
    set_running_campaign(campaign, creative)

    # what if account budget is off?
    assert advert.state.is_running is True
    assert strategy.state.is_running is True
    assert campaign.state.is_running is True
    # make sure we spend what we paid
    campaign.budget_spent = account.total_paid()
    # make budget twice that big, to be sure
    campaign.budget_total = 2 * account.total_paid()
    campaign.save()
    assert advert.state.is_running is False
    assert strategy.state.is_running is False
    assert campaign.state.is_running is False

    campaign.budget_spent = 1
    campaign.save()
    assert advert.state.is_running is True
    assert strategy.state.is_running is True
    assert campaign.state.is_running is True

    account.audit_fees = account.total_paid()
    account.save()
    assert advert.state.is_running is False
    assert strategy.state.is_running is False
    assert campaign.state.is_running is False
