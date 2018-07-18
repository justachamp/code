from django.core.management.base import BaseCommand
from django.core.cache import cache


class Command(BaseCommand):
    help = 'Clears django caches'

    def handle(self, *args, **options):
        cache.clear()
        self.stdout.write('Cache cleared')
