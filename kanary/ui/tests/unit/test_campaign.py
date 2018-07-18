import pytest
from mock import patch, PropertyMock

from ui.campaign.states import StrategyState, AdvertState
from ui.storage.states import CreativeState


class TestAdvertState(object):

    @pytest.mark.unit
    @patch.object(StrategyState, 'is_running', PropertyMock(return_value=True))
    @patch.object(AdvertState, 'audited', PropertyMock(return_value=True))
    def test_is_running_is_true_when_all_params_are_correct(self, advert_running):
        assert advert_running.state.is_running is True

    @pytest.mark.unit
    @patch.object(StrategyState, 'is_running', PropertyMock(return_value=True))
    @patch.object(AdvertState, 'audited', PropertyMock(return_value=True))
    def test_is_running_is_false_when_advert_is_deleted(self, advert_running):
        assert advert_running.state.is_running is True
        advert_running.is_deleted = True
        assert advert_running.state.is_running is False

    @pytest.mark.unit
    @patch.object(StrategyState, 'is_running', PropertyMock(return_value=True))
    @patch.object(AdvertState, 'audited', PropertyMock(return_value=True))
    def test_is_running_is_false_when_creative_is_deleted(self, advert_running):
        assert advert_running.state.is_running is True
        advert_running.creative.is_deleted = True
        assert advert_running.state.is_running is False

    @pytest.mark.unit
    @patch.object(StrategyState, 'is_running', PropertyMock(return_value=False))
    @patch.object(AdvertState, 'audited', PropertyMock(return_value=True))
    def test_is_running_is_false_when_strategy_is_not_running(self, advert_running):
        assert advert_running.state.is_running is False

    @pytest.mark.unit
    @patch.object(StrategyState, 'is_running', PropertyMock(return_value=True))
    @patch.object(AdvertState, 'audited', PropertyMock(return_value=False))
    def test_is_running_is_false_when_advert_not_audited(self, advert_running):
        assert advert_running.state.is_running is False

    @pytest.mark.unit
    @patch.object(CreativeState, 'audited', PropertyMock(return_value=True))
    @patch.object(CreativeState, 'brand_page_confirmed', PropertyMock(return_value=True))
    def test_audited_is_true_when_all_params_are_correct(self, advert_running):
        assert advert_running.state.audited is True

    @pytest.mark.unit
    @patch.object(CreativeState, 'audited', PropertyMock(return_value=False))
    @patch.object(CreativeState, 'brand_page_confirmed', PropertyMock(return_value=True))
    def test_audited_is_false_when_creative_not_audited(self, advert_running):
        assert advert_running.state.audited is False

    @pytest.mark.unit
    @patch.object(CreativeState, 'audited', PropertyMock(return_value=True))
    @patch.object(CreativeState, 'brand_page_confirmed', PropertyMock(return_value=False))
    def test_audited_is_false_when_brand_page_not_confirmed(self, advert_running):
        assert advert_running.state.audited is False

    @pytest.mark.unit
    @patch.object(CreativeState, 'audited', PropertyMock(return_value=False))
    @patch.object(CreativeState, 'brand_page_confirmed', PropertyMock(return_value=False))
    def test_audited_is_false_when_all_not_correct_params(self, advert_running):
        assert advert_running.state.audited is False
