from django.core.management.base import BaseCommand

from addnow.apps.reminders.tasks import send_reminder


class Command(BaseCommand):
    help = 'Check email notification'

    def handle(self, *args, **options):
        send_reminder()
