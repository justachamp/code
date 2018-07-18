import os
import simplejson

from path import path

from ui.settings import *


HAYSTACK_CONNECTIONS['default']['TIMEOUT'] = 60


MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES) + [
    'ui.tests.middleware.ArtificialDelay',
]


TEST_DB = os.environ.get('DJANGO_TEST_DB')
if TEST_DB:
    DATABASES = simplejson.loads(TEST_DB)


# force test database not to be in memory
for db in DATABASES.values():
    if db['ENGINE'] == 'django.db.backends.sqlite3':
        db['TEST_NAME'] = os.path.abspath(db['NAME'] + 'test')


# Absolute path to the directory that holds media.
MEDIA_ROOT = path('/tmp/kanary_media')
path(MEDIA_ROOT).mkdir_p()

# creatives directory location
CREATIVES_DIR = MEDIA_ROOT / 'creatives'
# invoices directory location
INVOICES_DIR = MEDIA_ROOT / 'invoices'

# create media subfolders if they not exist
path(CREATIVES_DIR).mkdir_p()
path(INVOICES_DIR).mkdir_p()

INTERCOM_APP_ID = ''

CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_ALWAYS_EAGER = True
BROKER_BACKEND = 'memory'

CELERY_EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'


app = Celery('ui')
app.config_from_object('ui.settings_test')
app.autodiscover_tasks(lambda: INSTALLED_APPS)
