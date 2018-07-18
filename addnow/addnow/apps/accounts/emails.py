from django.conf import settings
from django.core import signing

from post_office import mail

CONFIRMATION_PATH = '/confirm/'
PASSWORD_RESET_PART = '/resetpass/'
REMINDERS_UNSUBSCRIBE_PATH = '/reminders/unsubscribe/'


def send_post_office_email(recipient_list, template_name, context):
    if context and isinstance(context, dict):
        context.setdefault('base_url', settings.BASE_URL)

    mail.send(
        recipients=recipient_list,
        sender=settings.DEFAULT_FROM_EMAIL,
        template=template_name,
        context=context
    )


def verification(user):
    context = {
        'path': CONFIRMATION_PATH,
        'token': user.generate_email_token(),
        'base_url': settings.FRONTEND_BASE_URL
    }
    send_post_office_email([user.email], 'confirmation_email', context)


def password_reset_attempt(user):
    context = {
        'user': user,
        'path': PASSWORD_RESET_PART,
        'token': user.generate_password_reset_token(),
        'base_url': settings.FRONTEND_BASE_URL
    }
    send_post_office_email([user.email], 'password_reset', context)


def encouraging_email(user, template):
    context = {
        'user': user,
        'path': REMINDERS_UNSUBSCRIBE_PATH,
        'token': signing.dumps({'uid': user.pk}),
        'base_url': settings.FRONTEND_BASE_URL
    }
    send_post_office_email([user.email], template, context)


def trim_fail_email(site, error):
    context = {
        'user': site.user.email,
        'site': site.domain,
        'error': error
    }
    send_post_office_email([site.user.email], 'trim_fail', context)
