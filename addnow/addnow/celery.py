from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('ADDNOW_APP', 'addnow')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'addnow.settings.vagrant')

app = Celery('addnow')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS + ('addnow.apps.tracker',))
