import re
import shutil
from operator import contains
from datetime import datetime, timedelta
from itertools import chain

from mock import Mock
import pytest
from django.core import mail
from django.conf import settings

from ui.account.tasks import check_account_funds
from ui.account.models import Account, Invoice, Payment
from ui.storage.models import Creative
from ui.campaign.models import Strategy
from ui.mail.mailing import creatives_sent_for_audit, creative_rejected


sla_eta = datetime(year=2014, month=1, day=12, hour=11, minute=30)
sla_eta_formated = 'Jan. 12, 2014, 11:30 a.m.'

html_tag = re.compile(r'<[^>]+>')


def clean_html(html_str):
    """Remove newlines and tags from markup."""
    return ' '.join(html_tag.sub('', html_str).replace('\n', '').split())


def is_email_sent(subject):
    """ Returns ``True`` if email with given subject exists in outbox. """
    return any([msg.subject == subject for msg in mail.outbox])


def check_mail_contents(subject, substrings, check_cb=None):
    """
    Parse contents of the last sent mail, validate subject and check if it contains given substrings.
    :param callable check_cb: function which should evaluate to bool.
    """
    check_cb = check_cb or contains
    audit_mail = mail.outbox[-1]
    assert audit_mail.subject == subject
    body_decoded = unicode(audit_mail.body, 'utf-8')
    clean_body = clean_html(body_decoded)
    for substring in substrings:
        assert check_cb(clean_body, substring)


def set_running_campaign(campaign, creative):
    creative.appnexus_status = 'a'
    creative.save()

    campaign.start_UTC = datetime.utcnow()
    campaign.end_UTC = datetime.utcnow() + timedelta(days=30)
    campaign.budget_spent = 0
    campaign.save()


@pytest.fixture
def single_creative_audit(state_app):
    creative = Creative.objects.first()
    creative.appnexus_sla_eta = sla_eta
    return {
        'creatives': [creative],
        'strategies': creative.strategies()
    }


@pytest.fixture
def bulk_creatives_audit(state_app):
    account = state_app.models['account']['acc']
    strategy_1 = Strategy(name='Some strat 1', pk=1221)
    strategy_2 = Strategy(name='Some strat 2', pk=1222)
    bulk_creatives = [
        Creative(name='Some creative 1', appnexus_sla_eta=sla_eta, owner=account),
        Creative(name='Some creative 2', appnexus_sla_eta=sla_eta + timedelta(days=1), owner=account),
        Creative(name='Some creative 3', appnexus_sla_eta=None, owner=account)  # Date should be ignored.
    ]
    for c in bulk_creatives:
        c.strategies = Mock(return_value=[strategy_1, strategy_2])
    return {
        'creatives': bulk_creatives,
        'strategies': [strategy_1, strategy_2]
    }


@pytest.mark.django_db
def test_insufficient_funds_email_sending(state_app):
    campaign = state_app.models['campaign']['I\'m a fruit']
    creative = state_app.models['creative']['creative_image_1']

    set_running_campaign(campaign, creative)
    mail.outbox = []

    assert campaign.state.is_running is True

    # spend all account money
    campaign.budget_spent = campaign.account.account_balance()
    campaign.save()

    check_account_funds()
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == 'No sufficient funds'

    # assure we won't send this email again if already sent
    mail.outbox = []
    check_account_funds()
    assert len(mail.outbox) == 0

    # charge account
    Payment.objects.create(account=campaign.account, amount=100, datetime=datetime.utcnow())
    mail.outbox = []

    # spend all money again
    campaign.budget_spent += 100
    campaign.save()

    check_account_funds()
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == 'No sufficient funds'
    mail.outbox = []

    # after 24 hours we should send reminder
    account = Account.objects.get(pk=campaign.account.pk)
    account.insufficient_funds_last_sent_email_at = datetime.utcnow() - timedelta(days=1, minutes=1)
    account.save()

    check_account_funds()
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == 'Payment Needed'


@pytest.mark.django_db
def test_payment_successful_email_sending(state_app):
    account = state_app.models['account']['acc']

    # clear outbox
    mail.outbox = []

    Payment.objects.create(account=account, amount=100, datetime=datetime.utcnow())
    assert is_email_sent('Account credited')


@pytest.mark.django_db
def test_new_invoice_email_sending(state_app):
    account = state_app.models['account']['acc']

    # clear outbox
    mail.outbox = []
    # copy invoice file
    invoice_path = settings.INVOICES_DIR / 'test.pdf'
    shutil.copyfile(settings.PROJECT_DIR / 'tests' / 'uploads' / 'test.pdf', invoice_path)

    Invoice.objects.create(account=account, amount=100, datetime=datetime.utcnow(),
                           pdf=invoice_path,
                           number='FV/1234')
    assert is_email_sent("This Month's Invoice")


@pytest.mark.django_db
@pytest.mark.parametrize('case, message', [
    ('single_creative_audit', 'Your ad has been sent for audit'),
    ('bulk_creatives_audit', 'Your ads have been sent for audit')
])
def test_creatives_sent_for_audit(state_app, single_creative_audit, bulk_creatives_audit, case, message):
    """
    Test validity of audit date and if strategies names are shown.
    """
    audit = locals()[case]
    creatives_sent_for_audit(audit['creatives']).send()

    strategies_names = (s.name for s in audit['strategies'])
    audit_time_message = 'Estimated audit time is %s UTC.' % sla_eta_formated
    check_mail_contents(message, chain(strategies_names, audit_time_message))


def test_creative_rejected_content(state_app):
    """
    Test rejection message - strategies must be embedded in the message
    and pluralization must be applied. Feedback should be given.
    """
    account = state_app.models['account']['acc']
    feedback = 'Your creative is bad and you should feel bad.'
    creative = Creative(name='Some creative', owner=account,
                        appnexus_feedback=feedback)

    def mock_strategies_values_list(names_list):
        return lambda: Mock(values_list=Mock(return_value=names_list))

    # 1 strategy.
    creative.strategies = mock_strategies_values_list(['Some strat 1'])
    creative_rejected(creative).send()
    check_mail_contents('Your ad has been rejected', [
        'Your Ad from Some strat 1 strategy has been rejected. Rejection reason is: "%s"' % feedback]
    )

    # 2 strategies.
    creative.strategies = mock_strategies_values_list(['Some strat 1', 'Some strat 2'])
    creative_rejected(creative).send()
    check_mail_contents('Your ad has been rejected', [
        'Your Ad from Some strat 1, Some strat 2 strategies has been rejected. Rejection reason is: "%s"' %
        feedback]
    )
