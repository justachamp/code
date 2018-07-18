from datetime import date

from django.core import mail
import pytest

from ui.report.tasks import (get_previous_period,
                             get_lotame_report_key,
                             send_lotame_email_report,
                             generate_lotame_report_csv)
from ui.targeting.models import LotameBase
from ui.tests.integration.test_mailing import is_email_sent, check_mail_contents


@pytest.fixture
def lotame_app(basic_fixture):
    """
    Initializes database with basic lotame segments.
    """
    for segment_cls in LotameBase.__subclasses__():
        for segment_id in xrange(100):
            # Adding offset for differentiate values.
            lotame_id = segment_id + 7200
            segment_cls.objects.create(name="Segment %s" % lotame_id,
                                       appnexus_id=segment_id,
                                       lotame_id=lotame_id)


@pytest.fixture
def period():
    """
    Returns a period for which we want test sending reports.
    """
    return get_previous_period()


@pytest.fixture
def lotame_report_data(redisdb_spendings):
    """
    Populates redis with data for basic reports.
    """

    # Generates data for previous month which will be used as a reference
    # in tests.
    lotame_report_key = get_lotame_report_key(get_previous_period())
    for segment_id in xrange(25, 50):
        redisdb_spendings.hset(lotame_report_key, segment_id, 25)

    # Generates a set of data for current month to check if
    # code doesn't read data for invalid period.
    lotame_report_key = get_lotame_report_key(date.today())
    for segment_id in xrange(125, 150):
        redisdb_spendings.hset(lotame_report_key, segment_id, 29)


def check_mail_attachments(attachment_name, mimetype='text/csv'):
    """
    Checks if email contains given attachment_name and if attachment isn't empty.
    """
    mail_msg = mail.outbox[-1]
    attachments = mail_msg.attachments
    assert len(attachments) == 3  # Images + our file

    attachment = attachments[-1]
    # checking attachment name
    assert attachment_name == attachment[0]

    # checking if any contents has been sent
    assert len(attachment[1])

    # Checking attachment mimetype
    assert mimetype == attachment[2]


@pytest.mark.django_db
def test_lotame_csv_results(lotame_app, redisdb_spendings, lotame_report_data, period):
    """
    Test if generated results in csv are correct.
    """
    report_csv = generate_lotame_report_csv(redisdb_spendings, period).split('\n')

    # First row should contain columns names
    assert report_csv[0] == '"bids_won","segment_id","lotame_id","appnxs_segment_name","CPM","Vendor Cost"'

    # Checking last row if it's valid. -2 because csv.writer seems to generate newline at end
    # of file and it results with empty record at the end of list.
    assert report_csv[-2] == '"25","49","7249","Segment 7249","1","25"'


@pytest.mark.django_db
def test_lotame_email_report_full(lotame_app, lotame_report_data, period):
    """
    Tries to send lotame report with csv data.
    """
    email_subject = 'Gravity4 segments usage report for {period}'.format(period=period.strftime("%Y, %m"))
    email_csv_file = "{period}_LTME_DataUsage.csv".format(period=period.strftime("%y%m"))

    send_lotame_email_report()
    assert is_email_sent(email_subject)

    check_mail_contents(email_subject, ['In this month we had not used any of Lotame segments.'],
                        lambda content, substring: substring not in content)

    check_mail_attachments(email_csv_file)


@pytest.mark.django_db
def test_lotame_email_report_empty(lotame_app, period):
    """
    Tries to send lotame report withot csv data.
    """
    email_subject = 'Gravity4 segments usage report for {period}'.format(period=period.strftime("%Y, %m"))
    send_lotame_email_report()

    check_mail_contents(email_subject, ['In this month we had not used any of Lotame segments.'])
