from django.core.management.base import BaseCommand
from ui.targeting.appnexus_location_translation import translate_countries_and_states_from_csv


class Command(BaseCommand):

    help = """Updates AppNexus location translation with proper translations
    Read from embedded csv files."""

    def handle(self, *args, **options):
        translate_countries_and_states_from_csv()
