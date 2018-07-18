from optparse import make_option
from django.core.management.base import BaseCommand

from adserving.bidder import appnexus_api


class Command(BaseCommand):

    help = "Set up bidder instances according to the config."

    option_list = BaseCommand.option_list + (
        make_option(
            "-c", "--config",
            dest='config', help='Instances config path',
            default='~/config/bidder_instances.ini'
        ),
    )

    def handle(self, *args, **options):
        api = appnexus_api.AppNexusAPI()
        api.bidder_update(config_path=options['config'])
