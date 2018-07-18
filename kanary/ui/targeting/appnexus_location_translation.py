import csv
import logging as log

from django.conf import settings

from etc import dimensions
from bidrequest.constants import EXCHANGES
from ui.targeting.models import TargetValue, TargetMap


csv_dir = settings.PROJECT_DIR / 'targeting' / 'csv' / 'location'


def translate_countries_and_states_from_csv():
    """
    Translates yet untranslated Appnexus target values reading mappings from CSV files.

    # Replaces country short code like 'CA' with full name like 'Canada'
    # Replaces USA state short code like 'ME' with 'Maine'
    """
    # Read mappings from file
    countries = {}
    regions_usa = {}

    with open(csv_dir / 'iso3166.csv') as countries_file,\
            open(csv_dir / 'states.csv') as us_states_file:
        for country in csv.DictReader(countries_file, ['code', 'name']):
            countries[country['code']] = country['name']

        for state in csv.DictReader(us_states_file, ['name', 'code']):
            regions_usa[state['code']] = state['name']

    locations = TargetValue.objects.filter(
        category=dimensions.g_location,  # location
        exchange=EXCHANGES.appnexus,  # appnexus
        representant__isnull=True,  # it is representant
        represented__isnull=True  # but does not represent anything
    )

    log.info('[TRANSLATE_LOCATIONS] Found %s locations that need to be translated' % len(locations))
    translated_count = 0
    for location in locations:
        country_code = location.value_dict.get(dimensions.country)
        country_name = countries.get(country_code)
        region_code = location.value_dict.get(dimensions.region)
        region_name = regions_usa.get(region_code)

        location_values = location.value_list
        print len(location_values)

        # Set full name for country
        if country_name:
            location_values[0] = country_name
        else:
            log.info('[TRANSLATE_LOCATIONS] Can\'t translate location %s' % location)
            # No values can be translated, skip translation
            continue

        # Set full name for US region
        if country_code == 'US' and region_code:
            if not region_name:
                log.info('[TRANSLATE_LOCATIONS] Can\'t translate US region %s' % region_code)
            else:
                location_values[1] = region_name

        # Create exchange agnostic value
        representant, create = TargetValue.objects.get_or_create(
            exchange=None,
            category=dimensions.g_location,
            value=TargetMap.pack(location_values)
        )
        if representant.is_representant:
            location.make_represented(representant)
            location.save()
            translated_count += 1
        else:
            log.info('[TRANSLATE_LOCATIONS] Can\'t translate {0}, because {1} is not representant'.format(
                location, representant))

    log.info('[TRANSLATE_LOCATIONS] Succesfully translated %s out of %s locations' % (translated_count, len(locations)))
