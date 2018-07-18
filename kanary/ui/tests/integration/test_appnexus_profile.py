import pytest

from ui.tests.utils import DatabaseDataFactory, audit_creative
from ui.targeting.models import SegmentProximicSafetyLevel
from ui.campaign.models import Strategy
from ui.campaign.appnexus_profile_updater import get_segments as get_appnexus_segments, get_ads_sizes, build_profile


@pytest.fixture()
def profile_app(db):
    """Database setup with active strategies"""
    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()
    setup.setup_creative_images()
    setup.setup_landing_pages()
    setup.setup_campaigns_running()
    setup.setup_strategies()
    setup.setup_bidding_periods()
    setup.setup_adverts()
    setup.setup_payments()

    for creative in setup.models['creative'].values():
        audit_creative(creative)

    return setup


def add_segments(strategy, segments):
    for action, appnexus_id in segments:
        field = 'segment_proximic_safety_level' if action == 'include' else 'segment_proximic_safety_level_exclude'
        segment, _ = SegmentProximicSafetyLevel.objects.get_or_create(
            appnexus_id=appnexus_id,
            name=str(appnexus_id)
        )
        getattr(strategy, field).add(segment)


@pytest.mark.parametrize('strategy_a_segments, strategy_b_segments, expected_segments', [
    (
            # No segments included in one of strategies - appnexus segments list should be empty.
            [],
            [('include', 2), ('exclude', 3)],
            [],
    ),
    (
            # Separate sets
            [('include', 1)],
            [('include', 2), ('include', 3), ('exclude', 4)],
            [('include', 1), ('include', 2), ('include', 3)],
    ),
    (
            # Crossing sets - common part of included and excluded set should be included
            [('include', 1), ('include', 3)],
            [('include', 2), ('include', 3), ('exclude', 4)],
            [('include', 1), ('include', 2), ('include', 3)],
    ),
])
def test_segment_targets(profile_app, strategy_a_segments, strategy_b_segments, expected_segments):
    """Test case for calculating segments to include/exclude in appnexus profile"""
    strategy_a = profile_app.models['strategy']['han i has a pumpkin?']
    add_segments(strategy_a, strategy_a_segments)

    strategy_b = profile_app.models['strategy']['Hello this is Citrus']
    add_segments(strategy_b, strategy_b_segments)

    targeted_strategies = Strategy.running()
    appnexus_segments = map(lambda seg: (seg['action'], seg['id']), get_appnexus_segments(targeted_strategies))

    assert sorted(expected_segments) == sorted(appnexus_segments)


def test_ads_sizes_with_video_creative(profile_app):
    """
    Test if 1x1px appnexus size hack is included in all ads sizes if there is one video creative.
    Test if it is not if there are no video creatives.
    """

    # profile_app shouldn't include 1px x 1px hack as there are no video creatives.
    vast_size = {'height': 1, 'width': 1}
    assert vast_size not in get_ads_sizes()

    profile_app.setup_creative_videos()
    video_creative = profile_app.models['creative']['creative_video_1']
    video_creative.appnexus_set_audited()
    video_creative.save()

    profile_app.setup_adverts([{
                                   'name': 'ad_video',
                                   'strategy': 'han i has a pumpkin?',
                                   'creative': 'creative_video_1',
                                   'url': 'http://www.wp.pl/',
                               }])

    # Now there are video creatives in set up adverts so profile_app should include the hack.
    assert vast_size in get_ads_sizes()


def test_passthrough_percent(profile_app):
    """
    Check if passthrough_percent sets specified percent
    """
    profile = build_profile()

    assert profile['passthrough_percent'] > 0

    for strategy in Strategy.objects.all():
        strategy.is_paused = True
        strategy.save()

    profile = build_profile()

    # nothing to bid on
    assert profile['passthrough_percent'] == 0
