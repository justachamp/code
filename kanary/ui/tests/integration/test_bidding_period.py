from datetime import time, timedelta, tzinfo

import pytest
from django.core.exceptions import ValidationError

from ui.tests.utils import DatabaseDataFactory
from ui.campaign.models import BiddingPeriod, biddingperiod_presave


def make_bidding_period(start_tpl, end_tpl, strategy_key, tzinfo, db):
    """
    A shortcut for creating BiddingPeriod instance w/o saving into DB

    TODO: once database factory class will get rid of models attribute,
    the db param will be obsolete as well

    """
    return BiddingPeriod(
        start=time(*start_tpl, tzinfo=tzinfo),
        end=time(*end_tpl, tzinfo=tzinfo),
        strategy=db.models['strategy'][strategy_key]
    )


@pytest.fixture()
def bidding_app(db):
    """Extension of default setup by storing additional bidding periods"""
    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()
    setup.setup_creative_images()
    setup.setup_landing_pages()
    setup.setup_campaigns()
    setup.setup_strategies()
    setup.setup_bidding_periods()
    setup.setup_adverts()

    bp1 = make_bidding_period((19, 0), (20, 0),
                              'han i has a pumpkin?', None, setup)
    bp1.save()
    setup.models['bidding_period']['additional_bp1'] = bp1

    bp2 = make_bidding_period((22, 0), (23, 0),
                              'han i has a pumpkin?', None, setup)
    bp2.save()
    setup.models['bidding_period']['additional_bp2'] = bp2
    return setup


class TestBiddingPeriod(object):
    """Test case class for BiddingPeriod - pre_save signal"""

    class DummyTimeZone(tzinfo):
        """Fake timezone"""
        utcoffset = lambda self, dt: timedelta(hours=7, minutes=32)
        tzname = lambda self, dt: "Kanary Time Zone"

    @pytest.mark.parametrize('start_tpl, end_tpl, strategy_key', [
        ((0, 0), (4, 10), 'han i has a pumpkin?'),
        ((13, 30), (13, 40), 'Hello this is Citrus'),
        ((21, 0), (22, 30), 'Hello this is Citrus'),
        ((2, 15), (5, 55), 'han i has a pumpkin?'),
    ])
    def test_valid(self, bidding_app, start_tpl, end_tpl, strategy_key):
        """Test case for valid bidding periods, without time overlapping"""
        bp = make_bidding_period(start_tpl, end_tpl,
                                 strategy_key, None, bidding_app)
        # for all cases biddingperiod_presave should be executed w/o exception
        # then None is returned
        assert biddingperiod_presave(BiddingPeriod, bp) is None

    @pytest.mark.parametrize('start_tpl, end_tpl, strategy_key, tzinfo', [
        # timezone
        ((1, 0), (9, 5), 'han i has a pumpkin?', DummyTimeZone()),
        ((11, 10), (7, 35), 'Hello this is Citrus', None),  # start > end
        ((13, 45), (14, 10), 'Hello this is Citrus', None),  # overlapping
        ((10, 30), (13, 0), 'han i has a pumpkin?', None),  # overlapping
        ((8, 25), (18, 20), 'han i has a pumpkin?', None),  # overlapping
        ((17, 0), (19, 30), 'han i has a pumpkin?', None),  # overlapping
        ((20, 0), (23, 0), 'han i has a pumpkin?', None),  # overlapping
    ])
    def test_invalid(self, bidding_app,
                     start_tpl, end_tpl, strategy_key, tzinfo):
        """Test case for invalid bidding periods, with time overlapping etc."""
        bp = make_bidding_period(start_tpl, end_tpl,
                                 strategy_key, tzinfo, bidding_app)
        # for all cases validation exception should be raised
        with pytest.raises(ValidationError):
            biddingperiod_presave(BiddingPeriod, bp)
