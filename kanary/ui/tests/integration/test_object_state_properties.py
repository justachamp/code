from datetime import datetime, timedelta

import pytest
from ui.campaign.models import Advert, Campaign, Strategy

from ui.campaign.states import CampaignState, StrategyState, AdvertState
from ui.storage.models import Creative
from ui.storage.states import CreativeState
from ui.storage.tasks import send_for_audit


@pytest.mark.django_db
@pytest.mark.celery
@pytest.mark.parametrize('object_type, name, attr, cls', [
    ('campaign', 'I\'m a fruit', 'campaign', CampaignState),
    ('strategy', 'Hello this is Citrus', 'strategy', StrategyState),
    ('creative', 'creative_image_1', 'creative', CreativeState),
    ('advert', 'ad_lemon', 'advert', AdvertState),
])
def test_object_state_composition(state_app, object_type, name, attr, cls):
    obj = state_app.models[object_type][name]

    assert hasattr(obj, 'state') is True
    assert obj.state.__class__ == cls
    assert hasattr(obj.state, attr) is True
    assert getattr(obj.state, attr) == obj


@pytest.mark.django_db
def test_campaign_budget_status(state_app):
    campaign = state_app.models['campaign']['I\'m a fruit']
    strategy = state_app.models['strategy']['Hello this is Citrus']
    advert = state_app.models['advert']['ad_lemon']

    campaign.budget_spent = campaign.budget_total
    campaign.save()

    assert campaign.state.has_budget is False
    assert strategy.state.campaign_has_budget is False
    assert advert.state.campaign_has_budget is False

    campaign.budget_spent = 1000
    campaign.budget_total = 2 * campaign.budget_spent
    campaign.save()

    assert campaign.state.has_budget is True
    assert strategy.state.campaign_has_budget is True
    assert advert.state.campaign_has_budget is True


@pytest.mark.django_db
def test_campaign_scheduling_status(state_app):
    campaign = state_app.models['campaign']['I\'m a fruit']
    strategy = state_app.models['strategy']['Hello this is Citrus']

    campaign.start_UTC = datetime.utcnow() + timedelta(days=10)
    campaign.end_UTC = datetime.utcnow() + timedelta(days=30)
    campaign.save()

    assert campaign.state.scheduled is True
    assert campaign.state.in_progress is False
    assert campaign.state.finished is False

    assert strategy.state.campaign_scheduled is True

    campaign.start_UTC = datetime.utcnow()
    campaign.end_UTC = datetime.utcnow() + timedelta(days=5)
    campaign.save()

    assert campaign.state.in_progress is True
    assert campaign.state.finished is False
    assert campaign.state.scheduled is False

    assert strategy.state.campaign_in_progress is True

    campaign.start_UTC = datetime.utcnow() - timedelta(days=30)
    campaign.end_UTC = datetime.utcnow() - timedelta(days=15)
    campaign.save()

    assert campaign.state.finished is True
    assert campaign.state.in_progress is False
    assert campaign.state.scheduled is False

    assert strategy.state.campaign_finished is True


@pytest.mark.django_db
@pytest.mark.parametrize('status, correct, incorrect', [
    ('n', 'pending', ('rejected', 'audited')),
    ('p', 'pending', ('rejected', 'audited')),
    ('r', 'rejected', ('pending', 'audited')),
    ('u', 'rejected', ('pending', 'audited')),
    ('a', 'audited', ('rejected', 'pending')),
])
def test_conformity_between_creative_appnexus_status_and_creative_state(state_app,  appnexus_api_rejecting, status, correct, incorrect):

    creative = Creative.objects.get(name='creative_image_1')

    if correct == 'rejected' and status == 'r':
        send_for_audit()
    else:
        creative.appnexus_status = status
        creative.save()

    creative = Creative.objects.get(name='creative_image_1')
    advert_1 = Advert.objects.filter(creative__name='creative_image_1')[0]
    advert_2 = Advert.objects.filter(creative__name='creative_image_1')[1]
    assert getattr(creative.state, correct) is True
    assert getattr(creative.state, incorrect[0]) is False
    assert getattr(creative.state, incorrect[1]) is False

    assert getattr(advert_1.state, correct) is True
    assert getattr(advert_2.state, correct) is True


@pytest.mark.django_db
@pytest.mark.parametrize('status, valid, invalid', [
    ('n', 'creatives_pending', ('creatives_rejected', 'creatives_audited')),
    ('p', 'creatives_pending', ('creatives_rejected', 'creatives_audited')),
    ('r', 'creatives_rejected', ('creatives_pending', 'creatives_audited')),
    ('u', 'creatives_rejected', ('creatives_pending', 'creatives_audited')),
    ('a', 'creatives_audited', ('creatives_rejected', 'creatives_pending')),
])
def test_conformity_between_campaign_strategy_statuses_and_creative_appnexus_status(state_app, appnexus_api_rejecting, status, valid, invalid):

    creative = Creative.objects.get(name='creative_image_1')

    if valid == 'creatives_rejected' and status == 'r':
        send_for_audit()
    else:
        creative.appnexus_status = status
        creative.save()

    campaign =Campaign.objects.filter(name='I\'m a fruit')[0]
    strategy = Strategy.objects.filter(name='Hello this is Citrus')[0]

    assert creative in getattr(campaign.state, valid)
    assert creative not in getattr(campaign.state, invalid[0])
    assert creative not in getattr(campaign.state, invalid[1])

    assert creative in getattr(strategy.state, valid)
    assert creative not in getattr(strategy.state, invalid[0])
    assert creative not in getattr(strategy.state, invalid[1])

    # assure that distinct list of creatives is returned
    # no matter how much adverts with the same creative are bound to strategy
    assert len(getattr(campaign.state, valid)) == 1
    assert len(getattr(campaign.state, invalid[0])) == 0
    assert len(getattr(campaign.state, invalid[1])) == 0

    assert len(getattr(strategy.state, valid)) == 1
    assert len(getattr(strategy.state, invalid[0])) == 0
    assert len(getattr(strategy.state, invalid[1])) == 0


@pytest.mark.django_db
def test_campaign_strategy_filter_creatives(state_app):
    creative = state_app.models['creative']['creative_image_1']
    campaign = state_app.models['campaign']['I\'m a fruit']
    strategy = state_app.models['strategy']['Hello this is Citrus']

    def nofilter(ad):
        return ad

    assert len(strategy.state.filter_creatives(nofilter)) == 1, 'everything should be okay'
    assert len(campaign.state.filter_creatives(nofilter)) == 1, 'everything should be okay'

    creative.is_deleted = True
    creative.save()

    assert len(strategy.state.filter_creatives(nofilter)) == 0, 'creative deleted!'
    assert len(campaign.state.filter_creatives(nofilter)) == 0, 'creative deleted!'

    creative.is_deleted = False
    creative.save()

    # delete all strategies!
    campaign.strategy_set.update(is_deleted=True)

    assert len(strategy.state.filter_creatives(nofilter)) == 1, 'strategy deleted, but not creative'
    assert len(campaign.state.filter_creatives(nofilter)) == 0, 'strategy deleted, so no creative from strategy here!'


@pytest.mark.django_db
def test_strategies_budget_status(state_app):
    strategy_1 = state_app.models['strategy']['Hello this is Citrus']
    strategy_2 = state_app.models['strategy']['han i has a pumpkin?']
    campaign = state_app.models['campaign']['I\'m a fruit']
    advert_1 = state_app.models['advert']['ad_lemon']
    advert_2 = state_app.models['advert']['ad_carrot']

    strategy_2.budget_spent = strategy_1.budget_total
    strategy_2.save()

    assert strategy_1 in campaign.state.strategies_with_budget
    assert strategy_2 in campaign.state.strategies_without_budget
    assert len(campaign.state.strategies_with_budget) == 1
    assert len(campaign.state.strategies_without_budget) == 1

    assert advert_1.state.strategy_has_budget is True
    assert advert_2.state.strategy_has_budget is False

    strategy_2.budget_spent = 100
    strategy_2.save()

    assert strategy_1 in campaign.state.strategies_with_budget
    assert strategy_2 in campaign.state.strategies_with_budget
    assert len(campaign.state.strategies_with_budget) == 2
    assert len(campaign.state.strategies_without_budget) == 0

    assert advert_1.state.strategy_has_budget is True
    assert advert_2.state.strategy_has_budget is True
