from django.db import connection
from django.db import transaction

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = '''Development command!
        Drops all tables from project database (only postgresql)'''

    @transaction.atomic
    def handle(self, *args, **options):

        c = connection.cursor()

        droplist = """
            SELECT 'drop table if exists "' || tablename || '" cascade;'
            FROM pg_tables WHERE schemaname = 'public';
        """
        c.execute(droplist)
        drops = [drop[0] for drop in c.fetchall()]
        if not drops:
            print 'nothing to drop'
            return
        sql = ' '.join(drops)
        c.execute(sql)
