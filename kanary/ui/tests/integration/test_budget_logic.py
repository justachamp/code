import pytest

from ui.campaign.models import Strategy


@pytest.mark.parametrize('object_type, name', [
    ('campaign', 'I\'m a fruit'),
    ('strategy', 'Hello this is Citrus'),
])
def test_budget_total(budget_app, object_type, name):
    '''
    Assures that campaign/strategy budget cannot be
    saved as lower than spent budget
    '''
    model = budget_app.setup.models[object_type][name]

    # this is change
    model.budget_spent *= 2
    model.save()

    model.budget_total = model.budget_spent / 2
    model.save()

    assert model.budget_total == model.budget_spent

# test settings as tuples (budget total, budget spent)
campaign = (10, 5)
strategy_1 = (3, 2)
strategy_2 = (6, 3)


@pytest.mark.parametrize('camp, str1, str2, results', [
    (campaign, strategy_1, strategy_2, (0, 5, 3, 5)),
])
def test_budget_trimming(budget_app, camp, str1, str2, results):
    campaign = budget_app.setup.models['campaign']['I\'m a fruit']
    strategy_1 = budget_app.setup.models['strategy']['Hello this is Citrus']
    strategy_2 = budget_app.setup.models['strategy']['han i has a pumpkin?']

    campaign.budget_total = camp[0]
    campaign.budget_spent = camp[1]
    campaign.save()

    strategy_1.budget_total = str1[0]
    strategy_1.budget_spent = str1[1]
    strategy_1.save()

    strategy_2.budget_total = str2[0]
    strategy_2.budget_spent = str2[1]
    strategy_2.save()

    campaign.budget_total = results[0]
    campaign.save()

    assert campaign.budget_total == results[1]
    assert Strategy.objects.get(pk=strategy_1.pk).budget_total == results[2]
    assert Strategy.objects.get(pk=strategy_2.pk).budget_total == results[3]


def test_budget_total_is_constant_on_budget_spent_update(budget_app):
    strategy = budget_app.setup.models['strategy']['han i has a pumpkin?']

    strategy_budget_total = strategy.budget_total
    strategy.budget_spent = strategy.budget_total * 10
    strategy.save()

    # assert if budget_total stays the same after save_spendings()
    assert strategy_budget_total == strategy.budget_total


def test_strategy_budget_total_cut_to_campaign_budget_total(budget_app):
    '''
    Checking if strategy total budget greater than campaign total budget
    will be cut to campaign total budget level after save.
    '''

    strategy = budget_app.setup.models['strategy']['han i has a pumpkin?']
    strategy.budget_total = strategy.campaign.budget_total * 2
    strategy.save()

    assert strategy.budget_total == strategy.campaign.budget_total
