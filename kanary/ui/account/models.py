from adserving.types import Decimal
from itertools import chain
from operator import attrgetter
from random import randint

from etc import constants

from django.db import models as m
from django.db.models import Sum
from django.db.models.signals import post_save
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.dispatch import receiver
from django.core.urlresolvers import reverse

from ui.fields import (
    CharField255,
    BudgetDecimalField,
)
from ui.mail import mailing
from ui.utils import into_UTC, from_UTC, get_default_timezone, append_dollar
from ui.common.models import KanaryDirtyFieldsMixin, RandomId


class Invoice(m.Model):

    class Meta:
        ordering = ('-datetime', )

    account = m.ForeignKey('Account')
    number = m.CharField(max_length=20)
    datetime = m.DateTimeField(db_index=True)
    pdf = m.FileField(upload_to='invoices')
    amount = BudgetDecimalField()
    status = CharField255(null=True, blank=True)

    def __unicode__(self):
        return '{0}: {1}, {2}'.format(
            self.number, self.account.name, self.amount
        )

    def to_json(self):
        return {
            'date': self.datetime.strftime('%b. %d %Y'),
            'amount': append_dollar(self.amount),
            'event': 'Kanary Commision',
            'number': self.number,
            'status': self.status,
            'download_url': reverse('download_invoice', args=[self.id])
        }


class Payment(m.Model):

    class Meta:
        ordering = ('-datetime', )

    account = m.ForeignKey('Account')
    datetime = m.DateTimeField(db_index=True)
    amount = BudgetDecimalField()

    def __unicode__(self):
        return '{0}: {1}'.format(self.account.name, self.amount)

    def to_json(self):
        return {
            'date': self.datetime.strftime('%b. %d %Y'),
            'amount': append_dollar(self.amount),
            'event': 'Deposit'
        }


class Account(KanaryDirtyFieldsMixin, RandomId):

    account_number = m.IntegerField(null=False, unique=True)
    name = m.CharField(max_length=255)
    timezone = m.CharField(max_length=40, default=get_default_timezone())
    commission = m.SmallIntegerField(default=constants.COMMISSION)
    audit_fees = BudgetDecimalField(default=0)
    """
    Sum of what account had spent on audits.

    .. note:

        Creative model has it's own audit_fees field that should be updated along this one
        (we know what creative we're auditing, don't we?).
        And there's also a DailySpending model, that present same information per day,
        that also should be updated along.
    """

    # Fields used in profile form (second step of signup)
    # They could be empty because sometimes wee need to create empty account.
    # But blank=True because in signup forms they are required.
    is_agency = m.BooleanField(default=False, null=False)
    company_name = m.CharField(max_length=255, null=True, blank=False)
    first_name = m.CharField(max_length=50, null=True, blank=False)
    last_name = m.CharField(max_length=50, null=True, blank=False)
    address = m.CharField(max_length=255, null=True, blank=False)
    city = m.CharField(max_length=60, null=True, blank=False)
    zip_code = m.CharField(max_length=10, null=True, blank=False)
    country = m.CharField(max_length=5, null=True, blank=False)
    province = m.CharField(max_length=8, null=True, blank=True)
    phone = m.CharField(max_length=20, null=True, blank=False)
    vat = m.CharField(max_length=20, null=True, blank=True)

    insufficient_funds_sent_emails_count = m.IntegerField(null=False, default=0)
    insufficient_funds_last_sent_email_at = m.DateTimeField(null=True)

    def into_UTC(self, date_time):
        return into_UTC(date_time, self.timezone)

    def from_UTC(self, date_time):
        return from_UTC(date_time, self.timezone)

    def __unicode__(self):
        return self.name

    @property
    def adverts(self):
        from ui.campaign.models import Advert
        return Advert.objects.filter(creative__owner=self)

    def account_balance(self):
        """
        Calculate account balance.

        :returns: money balance for a given account
        :rtype: Decimal
        """

        return self.total_paid() - self.total_spent()

    def total_paid(self):
        """
        Sum of payments account made.

        :returns: money balance for a given account
        :rtype: Decimal

        """
        return self.payment_set.aggregate(
            sum=Sum('amount')
        )['sum'] or Decimal(0)

    def total_spent(self):
        """
        Sum of all account spendings (commission included).
        """
        aggregation = self.campaign_set.aggregate(
            sum=Sum('budget_spent'),
            commission=Sum('budget_spent_commission')
        )

        return (aggregation['sum'] or Decimal(0)) + \
               (aggregation['commission'] or Decimal(0)) + \
            self.audit_fees

    @property
    def last_payment(self):
        '''
        :returns: last payment value for a given account
        :rtype: Decimal or None
        '''
        last_one = self.payment_set.first()

        if last_one:
            return last_one.amount

    @property
    def transactions(self):
        '''
        Returns a list of all Invoices and Payments attributes
        sorted by date, displayed in user interface.
        '''
        transactions = sorted(
            chain(self.invoice_set.all(), self.payment_set.all()),
            reverse=True,
            key=attrgetter('datetime')
        )

        return [tr.to_json() for tr in transactions]

    def emails(self):
        """ Returns list of user emails from this account. """
        return self.users.values_list('email', flat=True)

    def reset_insufficient_funds_emails(self):
        """
        Reenables sending emails about insufficient funds.
        """
        if self.account_balance() > 0 and self.insufficient_funds_sent_emails_count > 0:
            self.insufficient_funds_sent_emails_count = 0
            self.insufficient_funds_last_sent_email_at = None
            self.save(update_fields=['insufficient_funds_sent_emails_count',
                                     'insufficient_funds_last_sent_email_at'])

    def save(self, *args, **kwargs):
        def random_accountnumber():
            return randint(1000, 100000)
        self._set_unique_field(10, 'account_number', random_accountnumber)
        super(Account, self).save(*args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):

    USERNAME_FIELD = 'username'

    account = m.ForeignKey('Account', related_name="users", null=False)
    username = CharField255(unique=True, db_index=True)
    email = m.EmailField(max_length=255, unique=True, db_index=True)
    unread_events_count = m.IntegerField(null=False, default=0)

    # indicates if user has complete signup process
    # and can be logged into the app.
    is_signup_complete = m.BooleanField(null=False, default=False)

    # admin related fields
    is_staff = m.BooleanField(default=False)
    is_active = m.BooleanField(default=True)

    objects = BaseUserManager()

    def get_full_name(self):
        return self.username

    # for admin site purposes
    def get_short_name(self):
        return self.username


@receiver(post_save, sender=Payment, weak=False)
def payment_post_save(sender, instance, created, **kwargs):
    payment = instance

    if created:
        mailing.payment_successful(payment).send()

        account = Account.objects.get(pk=payment.account.pk)
        account.reset_insufficient_funds_emails()


@receiver(post_save, sender=Invoice, weak=False)
def invoice_post_save(sender, instance, created, **kwargs):
    invoice = instance

    if created:
        mailing.new_invoice(invoice).send()


@receiver(post_save, sender=User, weak=False)
def user_post_save(sender, instance, created, **kwargs):

    if created:
        mailing.welcome(instance).send()
