import pytest

from ui.campaign.models import Strategy, Advert
from ui.storage.models import Creative, Brand, CreativeImage, DESTINATION


def get_instance(model, model_dict=None):
    model_dict = model_dict or {}
    instance = model(**model_dict)
    return instance


def get_creative_image(creative_image_dict):
    creative = get_instance(CreativeImage, creative_image_dict)
    destination = creative.destination
    # if destination name is full
    # e.g. 'facebook_sidebar' instead of 'fb'
    if destination not in DESTINATION.values():
        creative.destination = DESTINATION[destination]

    return creative


@pytest.fixture()
def default_brand():
    return get_instance(Brand, {
        'brand_id': 2,
        'thirdparty_page_id': 333,
        'page_name': 'Test brand page name',
    })


@pytest.fixture()
def advert_running():
    creative = get_instance(Creative, {'is_deleted': False})
    strategy = get_instance(Strategy)

    advert = get_instance(Advert, {
        'is_deleted': False,
        'creative': creative,
        'strategy': strategy
    })

    return advert


@pytest.fixture(scope="module")
def destination_creatives():
    """
    Return dict of creatives with such struct:
        {
            'facebook_sidebar': Creative with facebook_sidebar destination,
            ...
        }
    """
    creatives_dict = [{'destination': d} for d in DESTINATION.keys()]
    creatives = {c['destination']: get_creative_image(c) for c in creatives_dict}
    return creatives
