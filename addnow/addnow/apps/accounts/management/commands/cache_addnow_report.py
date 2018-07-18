# -*- coding: utf-8 -*-
import datetime
from optparse import make_option

from dateutil.relativedelta import relativedelta
from django.core.management.base import BaseCommand

from addnow.apps.accounts.models import Site
from addnow.apps.reports.views.archive import get_digest_data


def get_dates():
    out = []
    end_date = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    s_date = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    out.append((s_date.strftime('%s'), end_date.strftime('%s'), 'hour'))
    start_date = s_date - relativedelta(months=1)
    out.append((start_date.strftime('%s'), end_date.strftime('%s'), 'day'))
    start_date = s_date - relativedelta(years=1)
    out.append((start_date.strftime('%s'), end_date.strftime('%s'), 'day'))
    start_date = s_date - relativedelta(weeks=1)
    out.append((start_date.strftime('%s'), end_date.strftime('%s'), 'day'))
    return out


class Command(BaseCommand):
    help = 'Caching reports'
    option_list = BaseCommand.option_list + (
        make_option('--seconds', action='store', dest='seconds', default=86400, help='Specify seconds'),
    )

    def handle(self, *args, **options):
        cache_timeout = options.get('seconds')
        for begin_date, end_date, aggregation in get_dates():
            for site in Site.objects.all().order_by('pk'):
                line = 'site: %s, %s %s, cache: %s' % (site.pk, begin_date, end_date, cache_timeout)
                self.stdout.write(line)
                begin_date = datetime.datetime.fromtimestamp(int(begin_date))
                end_date = datetime.datetime.fromtimestamp(int(end_date))
                get_digest_data(
                    site, begin_date, end_date, aggregation,
                    cache_timeout=cache_timeout, clear_cache=True
                )
