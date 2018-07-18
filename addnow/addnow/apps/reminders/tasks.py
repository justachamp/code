import logging
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.db.models import Count

from addnow.apps.accounts.emails import encouraging_email
from addnow.apps.reminders.models import ReminderRule, ReminderLog
from addnow.celery import app


logger = logging.getLogger(__name__)


@app.task()
def send_reminder():
    user_class = get_user_model()
    rules = ReminderRule.objects.filter(is_active=True)
    for rule in rules:
        reminder_deadline = datetime.today() - timedelta(days=int(rule.dimension))

        queryset = user_class.objects\
            .annotate(widgets=Count('widgetconfiguration'))\
            .filter(
                is_active=True,
                is_reminders_muted=False,
                widgets=0,
                date_joined__year=reminder_deadline.year,
                date_joined__month=reminder_deadline.month,
                date_joined__day=reminder_deadline.day)\
            .prefetch_related('reminders')

        logger.debug(
            'sending encouraging email to users by rule date: %d.%d.%d',
            reminder_deadline.day,
            reminder_deadline.month,
            reminder_deadline.year
        )

        for user in queryset:

            if user.reminders.filter(rule=rule).exists():
                logger.debug('bypass %s', user)
                continue

            logger.debug('%s', user)

            encouraging_email(user, rule.email_template)

            log = ReminderLog(rule=rule, user=user)
            log.save()
