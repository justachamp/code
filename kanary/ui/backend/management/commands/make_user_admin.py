from django.core.management.base import BaseCommand

from ui.account.models import User


class Command(BaseCommand):
    args = "username"
    help = "Grants admin privileges to given user"

    def handle(self, *args, **options):
        if args:
            username = args[0]

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                print "Hey, user does not exist!"
            else:
                user.is_staff = True
                user.is_active = True
                user.is_superuser = True
                user.save()
        else:
            print "Please, provide the username."
