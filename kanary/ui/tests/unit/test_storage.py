import pytest


class TestCreative(object):

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "destination, verify_is_newsfeed, expected", [
            ('default', False, False),
            ('facebook_sidebar', False, True),
            ('facebook_newsfeed', False, True),
            ('default', True, False),
            ('facebook_sidebar', True, False),
            ('facebook_newsfeed', True, True)
        ])
    def test_is_facebook_destination_for_destination(self, destination, verify_is_newsfeed,
                                                     expected, destination_creatives):
        creative = destination_creatives[destination]
        is_facebook_destination = creative.is_facebook_destination(verify_is_newsfeed=verify_is_newsfeed)

        assert is_facebook_destination == expected


class TestCreativeState(object):

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "destination, expected", [
            ('default', True),
            ('facebook_sidebar', True),
        ])
    def test_brand_page_confirmed_not_facebook_newsfeed_destination(self, destination, expected,
                                                                          destination_creatives):
        creative = destination_creatives[destination]
        assert creative.state.brand_page_confirmed

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "brand_access_status, expected", [
            ('pending', False),
            ('confirmed', True),
            ('rejected', False),
        ])
    def test_brand_page_confirmed(self, brand_access_status, expected,
                                        destination_creatives, default_brand):
        creative = destination_creatives['facebook_newsfeed']
        default_brand.appnexus_access_status = brand_access_status
        creative.brand = default_brand

        assert creative.state.brand_page_confirmed == expected

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "brand_access_status, expected", [
            ('pending', False),
            ('confirmed', False),
            ('rejected', True),
        ])
    def test_brand_page_rejected(self, brand_access_status, expected,
                                        destination_creatives, default_brand):
        creative = destination_creatives['facebook_newsfeed']
        default_brand.appnexus_access_status = brand_access_status
        creative.brand = default_brand

        assert creative.state.brand_page_rejected == expected
