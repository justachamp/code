# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import StringIO
import csv
from datetime import datetime, timedelta

from django.core.mail import EmailMessage
from celery.utils.log import get_task_logger

from addnow.apps.accounts.models import Site
from addnow.apps.reports.archive import get_site_stats
from addnow.celery import app

logger = get_task_logger(__name__)


SUMMARY_EVENTS = ['shares', 'clicks', 'views', 'follows', 'copies']


@app.task(max_retries=10)
def site_stats(recipients):
    """
    Creates csv report for widgets usage and sends it attached in email to a list of people.
    """

    now = datetime.now()
    base_date_for_report = now - timedelta(days=1)
    csv_file = StringIO.StringIO()
    csv_writer = csv.writer(csv_file)
    first_row = ['Date', 'Login email', 'Last login', 'Site id', 'Site name']

    for event in SUMMARY_EVENTS:
        first_row.append(event.capitalize())
        first_row.append('Avg 7 days %s' % event)
        first_row.append('Avg 30 days %s' % event)
    csv_writer.writerow(first_row)

    date = base_date_for_report.date().isoformat()
    for site in Site.objects.all():
        stats = get_site_stats(site.pk, base_date_for_report, events=SUMMARY_EVENTS)
        last_login = site.user.last_login.date().isoformat() if site.user.last_login else '-'
        row = [date, site.user.email, last_login, site.pk, site.domain]
        for event in SUMMARY_EVENTS:
            row.append(stats[event])
            row.append(stats['%s_7_average' % event])
            row.append(stats['%s_30_average' % event])
        csv_writer.writerow(row)
    subject = 'Addnow sites usage report created on (%s)' % now.isoformat()
    body = 'Report is attached to this message'
    message = EmailMessage(subject, body, to=recipients)
    message.attach('addnow_report.csv', csv_file.getvalue(), 'text/csv')
    message.send()
    logger.info('Created site stats report')
