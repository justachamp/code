from django.contrib import admin
from django.contrib.admin import register

from addnow.apps.analytics.models import CredentialsModel


@register(CredentialsModel)
class CredentialsAdmin(admin.ModelAdmin):
    list_display = ['user', 'has_analytics']
