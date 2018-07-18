import pytest
from django.core.management import call_command

from haystack.query import SearchQuerySet
from etc import dimensions
from ui.targeting.models import (
    TargetValue,
    LotameDemographic,
    LotameAdvancedDemographic,
    LotameBehavioralInterest,
    LotameInfluencers,
    LotameOffline
)
from ui.tests.utils import get_resource


SEARCH_URL = '/api/targeting/location/search/'


@pytest.mark.django_db
def test_location_autoheal(search_engine, targetvalues_all_states, client):
    raw_name = 'WC'

    raw_weird_country, _ = TargetValue.objects.get_or_create_representant(
        category=dimensions.g_location,
        value=[raw_name],
        exchange='appnexus'
    )

    call_command('rebuild_index', interactive=False)

    assert raw_weird_country.pk in [
        int(res.pk) for res in SearchQuerySet().filter(
            django_ct='targeting.targetvalue', category=dimensions.g_location
        )
    ]

    response, data = get_resource(client, SEARCH_URL + '?q=' + raw_name)

    assert len(data['objects']) == 1, 'We should have found {0}!'.format(raw_name)

    representant, _ = TargetValue.objects.get_or_create_representant(
        category=dimensions.g_location,
        value=['Weird Country'],
        exchange='appnexus'
    )
    raw_weird_country.representant = representant
    raw_weird_country.save()

    # WC country should be removed here
    response, data = get_resource(client, SEARCH_URL + '?q=' + raw_name)

    # out of results
    assert len(data['objects']) == 0, '{0} should get removed from index'.format(raw_name)

    # out of index
    assert raw_weird_country.pk not in [
        int(res.pk) for res in SearchQuerySet().filter(
            django_ct='targeting.targetvalue', category=dimensions.g_location
        )
    ]


def test_lotame_segments_api(client, lotame_segments):
    """Test if api resources for lotame return all segments for given segment category"""

    for LotameSegmentModel, resource_url in [
        (LotameDemographic, 'lotame_demographic'),
        (LotameAdvancedDemographic, 'lotame_advanced_demographic'),
        (LotameBehavioralInterest, 'lotame_behavioral_interest'),
        (LotameInfluencers, 'lotame_influencers'),
        (LotameOffline, 'lotame_offline'),
    ]:
        url = '/api/targeting/%s/' % resource_url
        status, segment_data = get_resource(client, url)

        database_segments = LotameSegmentModel.objects.values_list('id', 'name')
        api_segments = map(lambda seg: (seg['id'], seg['name']), segment_data['objects'])

        assert any(api_segments)
        assert sorted(api_segments) == sorted(database_segments)
