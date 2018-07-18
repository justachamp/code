from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Populate targeting cache redis db used by BidDimensionExtractor.'

    def handle(self, *args, **options):
        from ui.targeting.targetcache_sync import TargetCacheSync
        TargetCacheSync.populate()
