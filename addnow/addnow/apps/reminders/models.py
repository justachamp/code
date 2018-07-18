from django.conf import settings
from django.db import models

from post_office.models import EmailTemplate


class ReminderRule(models.Model):
    name = models.CharField(max_length=150)
    email_template = models.ForeignKey(EmailTemplate)
    dimension = models.PositiveSmallIntegerField(help_text='Please specify value in days')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class ReminderLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reminders')
    rule = models.ForeignKey(ReminderRule)

    created_at = models.DateTimeField(auto_now_add=True)
