from django.contrib.gis.geoip import GeoIP
from django.test import TestCase


class TestGeoIP(TestCase):
    def test_country(self):
        country = GeoIP().country('google.com')
        self.assertIsInstance(country, dict)

        for key in ['country_code', 'country_name']:
            self.assertIn(key, country)

    def test_city(self):
        city = GeoIP().city('google.com')
        self.assertIsInstance(city, dict)

        for key in ['city', 'continent_code', 'region', 'longitude', 'latitude', 'country_code', 'country_name']:
            self.assertIn(key, city)
