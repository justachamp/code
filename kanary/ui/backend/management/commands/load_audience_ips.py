import csv
import os
import sys
from redis.connection import Connection

from netaddr import IPAddress
from django.core.management.base import BaseCommand

from etc.config import settings
from ui.account.models import User
from ui.storage.models import Audience
from adserving.adserver.profiles import Profiles


class Command(BaseCommand):
    args = 'owner_username audience_name csv_file'
    help = '''Creates Audience for account of given user and
    emites IP addresses from file to redis. Use it like this:
    ./ui/manage.py load_audience_ips owner "name" ips.csv | redis-cli --pipe'''

    def handle(self, *args, **options):
        owner_username = args[0]
        audience_name = args[1]
        filename = os.path.abspath(args[2])
        redis_key = Profiles.ip_audiences_key
        # the connection is not necessary, but the object is used to
        # format redis commands to redis protocol using pack_command
        redis_connection = Connection(host=settings.profiles_redis_host,
                                      port=settings.profiles_redis_port)
        user = User.objects.get(username=owner_username)
        audience, _ = Audience.objects.get_or_create(
            name=audience_name,
            owner=user.account,
            is_ip=True
        )
        audience_id = audience.public_id

        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                ip = IPAddress(row[0]).packed
                sys.stdout.write(
                    redis_connection.pack_command(
                        "SADD",
                        redis_key.format(ip),
                        audience_id
                    )
                )
