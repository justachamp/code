import pytest

from etc import dimensions
from ui.targeting import models as TM
from ui.storage.models import Audience


@pytest.mark.unit
def test_is_interest_based_audiences(clean_strategy):
    """Test if adding audiences to strategy changes is_interest_based flag to True"""
    strategy = clean_strategy
    audience = Audience.objects.create(
        name='Test Audience',
        owner=strategy.campaign.account
    )

    for field in (strategy.audiences, strategy.audiences_exclude):
        assert strategy.is_interest_based() is False
        field.add(audience)
        assert strategy.is_interest_based() is True
        field.remove(audience)


@pytest.mark.parametrize('category', [
    dimensions.gender,
    dimensions.age_group,
])
@pytest.mark.unit
def test_is_interest_based_target_values(clean_strategy, category):
    """Test if adding interest based target values to strategy changes is_interest_based flag to True"""
    strategy = clean_strategy
    target_value = TM.TargetValue.objects.filter(category=category).first()

    for field in (strategy.targeting_values, strategy.targeting_values_exclude):
        assert strategy.is_interest_based() is False
        field.add(target_value)
        assert strategy.is_interest_based() is True
        field.remove(target_value)


@pytest.mark.parametrize('include_field, Segment', [
    ('segment_lotame_demographic', TM.LotameDemographic),
    ('segment_lotame_advanced_demographic', TM.LotameAdvancedDemographic), #noqa
    ('segment_lotame_behavioral_interest', TM.LotameBehavioralInterest),
    ('segment_lotame_influencers', TM.LotameInfluencers),
    ('segment_lotame_offline', TM.LotameOffline),
])
@pytest.mark.unit
def test_is_interest_based_lotame_segments(clean_strategy, include_field, Segment):
    """Test if adding lotame segments to targeting changes is_interest_based flag to True"""
    strategy = clean_strategy
    target_value = Segment.objects.create(name='Test Segment', appnexus_id=782, lotame_id=451)

    exclude_field = '%s_exclude' % include_field
    for field in (getattr(strategy, include_field), getattr(strategy, exclude_field)):
        assert strategy.is_interest_based() is False
        field.add(target_value)
        assert strategy.is_interest_based() is True
        field.remove(target_value)
