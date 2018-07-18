import csv
from datetime import date, timedelta
from decimal import Decimal
import tempfile
import logging

from celery import task
from celery.utils.log import get_task_logger
from raven.contrib.django.raven_compat.models import client

from etc.constants import (LOTAME_IMP_REPORT_KEY,
                           LOTAME_REPORT_FILENAME,
                           LOTAME_PERIOD_FORMAT,
                           LOTAME_CSV_PERIOD_FORMAT)

from ui.bidding_spendings.tasks import BiddingSpendingsRedisTask
from ui.targeting.models import LotameBase
from ui.mail import mailing

log = get_task_logger(__name__)


def get_lotame_report_key(period):
    """
    Generates key in which should be stored impresssions for segments from given period.
    """
    return LOTAME_IMP_REPORT_KEY.format(period=period.strftime(LOTAME_PERIOD_FORMAT))


def get_previous_period():
    """
    Gets previous period against current datetime.now()
    """
    return date.today().replace(day=1) - timedelta(days=1)


def get_csv_file_name(period):
    """
    Generates csv file which should be sent for given period.
    :param date period: period for which we want csv name
    """
    return LOTAME_REPORT_FILENAME.format(period=period.strftime(LOTAME_CSV_PERIOD_FORMAT))


def generate_lotame_report_csv(redis_instance, period):
    """
    Generates csv file which is later sent to lotame/gravity4.
    :param RedisClient redis_instance: instance of redis client.
    :param date period: period for which we want data (one full month)
    :rtype: bytes
    :return: contents of generated csv file.
    """
    # Stores appnexus_id -> lotame_id map
    appnexus_to_lotame = {}

    # Stores appnexus_id -> segment_name map
    appnexus_names = {}

    # Stores appnexus_id -> segment_cpm map
    appnexus_cpm = {}

    lotame_spendings = redis_instance.hgetall(get_lotame_report_key(period))

    if not lotame_spendings:
        return

    appnexus_ids = lotame_spendings.keys()

    # We retrieve data from Segment classes and putting it to maps
    # for faster lookups during generation of final csv rows.
    for lotame_segment_cls in LotameBase.__subclasses__():
        segments_ids = lotame_segment_cls.objects.filter(appnexus_id__in=appnexus_ids)
        appnexus_to_lotame_map = dict(segments_ids.values_list('appnexus_id', 'lotame_id'))
        appnexus_names_map = dict(segments_ids.values_list('appnexus_id', 'name'))

        for appnexus_id in appnexus_to_lotame.keys():
            appnexus_cpm[appnexus_id] = lotame_segment_cls.PRICE_CPM

        appnexus_to_lotame.update(appnexus_to_lotame_map)
        appnexus_names.update(appnexus_names_map)

    _, csv_path = tempfile.mkstemp()

    with open(csv_path, "wb") as csv_fd:
        csv_writer = csv.writer(csv_fd, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["bids_won", "segment_id", "lotame_id", "appnxs_segment_name", "CPM", "Vendor Cost"])

        for appnexus_segment_id, impressions in sorted(lotame_spendings.items(), key=lambda x: int(x[0])):
            appnexus_segment_id = int(appnexus_segment_id)
            bids_won = Decimal(impressions)
            segment_id = appnexus_to_lotame[appnexus_segment_id]
            appnxs_segment_name = appnexus_names[appnexus_segment_id]
            cpm = appnexus_cpm[appnexus_segment_id]
            vendor_cost = appnexus_cpm[appnexus_segment_id] * bids_won

            row = [bids_won,
                   appnexus_segment_id,
                   segment_id,
                   appnxs_segment_name,
                   cpm,
                   vendor_cost]
            csv_writer.writerow(row)

    log.info("Temporary csv report: %s" % csv_path)
    return open(csv_path, "rU").read()


@task(base=BiddingSpendingsRedisTask)
def send_lotame_email_report(period=None):
    """
    Sends a e-mail report for Lotame.

    :param date period: a period (Year, month) for which we want to send report.
    If given period is None we use previous month.
    """
    period = period or get_previous_period()

    csv_data = generate_lotame_report_csv(send_lotame_email_report.rd, period)

    if not csv_data:
        log.info("There's no data for %s" % period)
        mailing.lotame_report(period).send()
        return

    csv_file_name = get_csv_file_name(period)
    client.captureMessage('Generated report for {0} {1}'.format(period, csv_file_name), level=logging.INFO)
    mailing.lotame_report(period, csv_data, csv_file_name).send()
