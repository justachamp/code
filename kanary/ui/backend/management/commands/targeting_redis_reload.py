from django.core.management.base import BaseCommand

from ui.cache.tasks import trigger_cache_mappings


class Command(BaseCommand):
    help = "Forces targeting cache refreshing"

    def handle(self, *args, **options):
        trigger_cache_mappings(force=True)
