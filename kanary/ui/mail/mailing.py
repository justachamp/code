from urlparse import urljoin

from etc.config import settings
from etc.constants import LOTAME_SUBJECT_FORMAT, LOTAME_SUBJECT_PERIOD_FORMAT
from ui.mail import HTMLEmailMessage


def insufficient_funds(account, reminder=False):
    """
    :param Account account: account with balance equal 0
    """
    context = dict(
        subject='No sufficient funds' if not reminder else 'Payment Needed',
        billing_url=urljoin(settings.ui_frontend_url, '#/account/billing')
    )
    template = 'emails/no_sufficient_funds.html' if not reminder else \
               'emails/no_sufficient_funds_reminder.html'
    return HTMLEmailMessage(context['subject'], to=account.emails(),
                            template=template, template_context=context)


def creatives_sent_for_audit(creatives):
    """
    :param list creatives: list of creatives sent for audit. All creatives should belong
        to one account
    """
    strategies = set()
    account = creatives[0].owner
    estimated_audit_time = None

    for creative in creatives:
        for strategy in creative.strategies():
            strategies.add(strategy)

        if creative.appnexus_sla_eta:
            sla_eta = creative.appnexus_sla_eta
            if sla_eta is None:
                continue
            if estimated_audit_time is None:
                estimated_audit_time = sla_eta
            else:
                estimated_audit_time = min(estimated_audit_time, sla_eta)

    context = dict(
        creatives=creatives,
        strategies=[s.name for s in strategies],
        subject='Your ad has been sent for audit' if len(creatives) == 1
                else 'Your ads have been sent for audit',
        estimated_audit_time=estimated_audit_time
    )
    return HTMLEmailMessage(context['subject'], to=account.emails(),
                            template='emails/creative_sent_for_audit.html', template_context=context)


def creative_rejected(creative):
    """
    :param Creative creative: creative that was rejected
    """
    context = dict(
        creative=creative,
        strategies=creative.strategies().values_list('name', flat=True),
        subject='Your ad has been rejected'
    )
    return HTMLEmailMessage(context['subject'], to=creative.owner.emails(),
                            template='emails/creative_rejected.html', template_context=context)


def payment_successful(payment):
    context = dict(
        payment_amount=payment.amount,
        account_balance=payment.account.account_balance(),
        subject='Account credited'
    )
    return HTMLEmailMessage(context['subject'], to=payment.account.emails(),
                            template='emails/payment_successful.html', template_context=context)


def new_invoice(invoice):
    context = dict(
        invoice=invoice,
        billing_url=urljoin(settings.ui_frontend_url, '#/account/billing'),
        subject="This Month's Invoice"
    )
    msg = HTMLEmailMessage(context['subject'], to=invoice.account.emails(),
                            template='emails/new_invoice.html', template_context=context)
    msg.attach_file(invoice.pdf.path)
    return msg


def reset_password(user, reset_link):
    context = dict(
        reset_link=reset_link,
        subject='Reset your password',
    )
    return HTMLEmailMessage(context['subject'], to=[user.email],
                            template='emails/reset_password.html', template_context=context)


def welcome(user):
    return HTMLEmailMessage('Welcome to Gravity4', to=[user.email],
                            template='emails/welcome.html', template_context={})


def lotame_report(period, csv_data=None, csv_file_name=None):
    """`
    :param str csv_file: path to file with report generated to csv.
    """
    report_msg = HTMLEmailMessage(LOTAME_SUBJECT_FORMAT.format(period=period.strftime(LOTAME_SUBJECT_PERIOD_FORMAT)),
                                  to=settings.lotame_email_report_to,
                                  cc=settings.lotame_email_report_cc,
                                  bcc=settings.lotame_email_report_bcc,
                                  template='emails/lotame_report.html',
                                  template_context={
                                  'period': period,
                                  'has_csv': bool(csv_file_name)
                                  })
    if csv_file_name:
        report_msg.attach(csv_file_name, csv_data, 'text/csv')

    return report_msg
