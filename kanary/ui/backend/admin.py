from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

from tastypie.models import ApiKey


# Unregister unused django apps from admin
try:
    admin.site.unregister(ApiKey)
    admin.site.unregister(Group)
    admin.site.unregister(Site)
except admin.sites.NotRegistered:
    # to avoid error during import tests
    pass
