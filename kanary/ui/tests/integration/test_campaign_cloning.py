from copy import copy

import pytest


class CloneApp:
    def __init__(self, app):
        self.app = app
        self.setup = app.setup


@pytest.fixture()
def cloneapp(app, basic_fixture):
    app.setup.setup_creative_images()
    app.setup.setup_landing_pages()
    app.setup.setup_campaigns()
    app.setup.setup_strategies()
    return CloneApp(app)


@pytest.mark.celery
def test_campaign_copy(cloneapp):
    """Testing campaign.copy()"""

    campaign = cloneapp.setup.models['campaign']['I\'m a fruit']

    old_campaign = copy(campaign)
    old_strategies_counter = campaign.strategy_set.all().count()

    campaign.copy()

    assert campaign.name == old_campaign.name + ' (copy)'
    assert campaign.slug == old_campaign.slug + '-copy'

    # other fields
    ignore_fields = (
        'id',
        'id_random',
        'name',
        'slug',
        'modified',
        'strategy',
    )
    for field in campaign._meta.local_fields:
        if field.name in ignore_fields:
            continue
        new_value = getattr(campaign, field.name)
        old_value = getattr(old_campaign, field.name)
        assert new_value == old_value

    # number of strategies
    assert old_strategies_counter == campaign.strategy_set.all().count()


# currently disabled, waiting for cloning campaign/strategy feature enabling
@pytest.mark.celery
def _test_strategy_copy(cloneapp):
    """Testing strategy.copy()"""

    strategy = cloneapp.setup.models['strategy']['Hello this is Citrus']

    old_strategy = copy(strategy)

    counters = {}
    for field in strategy._meta.local_many_to_many:
        items_counter = getattr(strategy, field.name).all().count()
        counters[field.name] = items_counter

    old_bidding_periods = strategy.bidding_periods
    old_landing_sites_def = strategy.landing_sites_def
    old_creatives_def = strategy.creatives_def

    strategy.copy()

    assert strategy.name == old_strategy.name + ' (copy)'
    assert strategy.slug == old_strategy.slug + '-copy'

    # other fields
    ignore_fields = (
        'id',
        'id_random',
        'name',
        'slug',
        'modified',
        'created',
        'campaign',
        'advert',
        'landing_site_variable',
        'biddingperiod',
    )
    for field in strategy._meta.local_fields:
        if field.name in ignore_fields:
            continue
        new_value = getattr(strategy, field.name)
        old_value = getattr(old_strategy, field.name)
        assert new_value == old_value

    # count objects
    for field in strategy._meta.local_many_to_many:
        new_counter = getattr(strategy, field.name).all().count()
        assert counters[field.name] == new_counter

    # properties
    assert old_bidding_periods == strategy.bidding_periods
    assert old_landing_sites_def == strategy.landing_sites_def
    assert old_creatives_def == strategy.creatives_def
