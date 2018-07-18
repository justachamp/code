import pytest

from etc import dimensions
from ui.targeting.models import TargetValue, TargetMap
from ui.targeting.appnexus_location_translation import translate_countries_and_states_from_csv


@pytest.mark.parametrize('location, tv_count, representant', (
        (['US'], 2, ['United States']),
        (['US', 'NY'], 2, ['United States', 'New York']),
        (['PL'], 2, ['Poland']),
        (['NZ', '1', 'Watapig'], 2, ['New Zealand', '1', 'Watapig']),
        (['CZ', '2', 'Praha'], 2, ['Czech Republic', '2', 'Praha']),
        (['US', 'XX', 'Washington'], 2, ['United States', 'XX', 'Washington']),
        (['XX'], 1, ['XX']),
))
@pytest.mark.django_db
def test_location_appnexus_translation(
        clean_targeting, location, tv_count, representant):
    original_location, _ = TargetValue.objects.get_or_create_representant(
        dimensions.g_location, location, 'appnexus')
    translate_countries_and_states_from_csv()

    assert TargetValue.objects.count() == tv_count

    translate_countries_and_states_from_csv()

    assert TargetValue.objects.count() == tv_count

    location_translated = TargetValue.objects.get(
        category=dimensions.g_location,
        value=TargetMap.pack(representant)
    )

    assert location_translated.is_representant is True
    # we expect to translated having a representant
    # only if we expect it to be translated
    original_location = TargetValue.objects.get(pk=original_location.pk)
    is_translated = location != representant
    assert original_location.has_representant == is_translated
    assert original_location.is_representant != is_translated
