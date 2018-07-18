from datetime import datetime, timedelta

from celery import task

from ui.mail import mailing


@task
def check_account_funds():
    """
    Checks if accounts are charged. If account is not charged and has campaigns in progress
    it sends notification emails about campains on hold.
    """
    from ui.account.models import Account

    for account in Account.objects.filter(insufficient_funds_sent_emails_count__lte=1).all():
        if account.account_balance() > 0:
            continue

        stopped_campaigns = [campaign.state.waits_for_account_charging
                             for campaign in account.campaign_set.all()]
        sent_emails_count = account.insufficient_funds_sent_emails_count
        last_sent_email_at = account.insufficient_funds_last_sent_email_at

        if (stopped_campaigns and (sent_emails_count == 0 or
                last_sent_email_at <= datetime.utcnow() - timedelta(days=1))):
            mailing.insufficient_funds(account, reminder=sent_emails_count > 0).send()

            account.insufficient_funds_sent_emails_count += 1
            account.insufficient_funds_last_sent_email_at = datetime.utcnow()
            account.save(update_fields=['insufficient_funds_sent_emails_count',
                                        'insufficient_funds_last_sent_email_at'])
