from django.core.management.base import BaseCommand

from ui.targeting.appnexus_base import appnexus_targeting_update


class Command(BaseCommand):

    help = """Updates AppNexus targeting classes containing mapping of AppNexus
            IDs into verbose names"""

    def handle(self, *args, **options):
        appnexus_targeting_update()
