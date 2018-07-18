import os
import time

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Removing temporary files (older than 1 day) from: %s' % (
        os.path.join(settings.MEDIA_ROOT, settings.TMP_UPLOAD_DIR)
    )

    def handle(self, *args, **options):

        path = os.path.join(settings.MEDIA_ROOT, settings.TMP_UPLOAD_DIR)
        now = time.time()

        for f in os.listdir(path):
            file_path = os.path.join(path, f)
            if os.stat(file_path).st_mtime < now - 1 * 86400:
                os.remove(file_path)
