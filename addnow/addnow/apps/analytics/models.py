from django.conf import settings
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from oauth2client.contrib.django_orm import CredentialsField

from addnow.apps.analytics.signals import analytics_revoke_access


class CredentialsModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='analytics_credential', primary_key=True)
    credential = CredentialsField()

    def has_analytics(self):
        return self.user.has_analytics


@receiver(pre_delete, sender=CredentialsModel)
def delete_handler(sender, instance, **kwargs):
    analytics_revoke_access.send(sender=sender, user=instance.user)
