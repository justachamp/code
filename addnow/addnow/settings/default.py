"""
Django settings for addnow project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import socket

from celery.schedules import crontab


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


###################################
#    Django Specific SETTINGS     #
###################################

# Core Settings

ALLOWED_HOSTS = [
    '.addnow.com',
    '.addnow.com.',
]

APPEND_SLASH = False

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SERIALIZER": "django_redis.serializers.msgpack.MSGPackSerializer",
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'addnow',
        'USER': 'addnow',
        'PASSWORD': 'addnow',
        'HOST': '127.0.0.1',
        'CONN_MAX_AGE': 300
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DEFAULT_FROM_EMAIL = 'support@addnow.com'

# EMAIL SETTINGS
EMAIL_BACKEND = 'post_office.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'postmaster@mailer.addnow.com'
EMAIL_HOST_PASSWORD = 'fb92e6c02771ad875ce9d41e768bb2b3'
EMAIL_USE_SSL = False
EMAIL_USE_TLS = False

EMAIL_SUBJECT_PREFIX = '[Addnow] '

FORCE_SCRIPT_NAME = None

INSTALLED_APPS = ()

LANGUAGE_CODE = 'en-us'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/addnow/debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

MIDDLEWARE_CLASSES = ()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'js)_w$uhgc=bf((m&rpax!ob5oa9_t)-^pu5-+s6bfb01xino-'

SERVER_EMAIL = 'no-reply@addnow.com'

SIGNING_BACKEND = 'django.core.signing.TimestampSigner'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',

                'addnow.context_processors.base_url',
            ),
        }
    },
]

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True

WSGI_APPLICATION = None

###################################
# Installed App Specific SETTINGS #
###################################

# Auth

AUTH_USER_MODEL = 'accounts.User'

LOGIN_REDIRECT_URL = '/accounts/profile/'

LOGIN_URL = '/admin/login/'

LOGOUT_URL = '/admin/logout/'

PASSWORD_RESET_TIMEOUT_DAYS = 2


# Static Files

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('widget', '/home/addnow/addnow/widget/dist'),
)

# corsheaders
CORS_ORIGIN_ALLOW_ALL = True

# GeoIP settings
GEOIP_PATH = '/usr/share/GeoIP'
GEOIP_LIBRARY_PATH = '/usr/lib64/libGeoIP.so'
GEOIP_CITY = 'GeoIPCity.dat'

# django-redis

# if you do not want exceptions when Redis is down
# http://niwibe.github.io/django-redis/#_memcached_exceptions_behavior
DJANGO_REDIS_IGNORE_EXCEPTIONS = True

# nltk
NLTK_DATA_PATH = os.path.join(BASE_DIR, 'var', 'nltk_data')

# post_office
POST_OFFICE = {
    'BACKENDS': {
        'default': 'djcelery_email.backends.CeleryEmailBackend',
    },
    'BATCH_SIZE': 5000,         # Limit the number of emails sent in a batch
    'DEFAULT_PRIORITY': 'now',  # Override default priority for integration with asynchronous email backend
    'LOG_LEVEL': 1              # Log only failed deliveries
}


# raven
RAVEN_CONFIG = {}


###################################
#    Project Specific SETTINGS    #
###################################

API_PREFIX = 'api/v1'

API_TEST = False

# set a global socket timeout:
DEFAULT_GLOBAL_SOCKET_TIMEOUT = 5 * 60  # 5 minutes
socket.setdefaulttimeout(DEFAULT_GLOBAL_SOCKET_TIMEOUT)


# NOTE: Following sensitive settings should be overwritten in local.py file


# pymongo
MONGODB_NAME = 'addnow'
MONGODB_URI = 'mongodb://localhost:27017'

# django-ipware
IPWARE_PRIVATE_IP_PREFIX = (
    '0.',   # externally non-routable
    '10.',  # class A private block
    '169.254.',  # link-local block
    '172.16.', '172.17.', '172.18.', '172.19.',
    '172.20.', '172.21.', '172.22.', '172.23.',
    '172.24.', '172.25.', '172.26.', '172.27.',
    '172.28.', '172.29.', '172.30.', '172.31.',  # class B private blocks
    '192.0.2.',  # reserved for documentation and example code
    '192.168.',  # class C private block
    '255.255.255.',  # IPv4 broadcast address
) + (  # the following addresses MUST be in lowercase)
    '2001:db8:',  # reserved for documentation and example code
    'fc00:',  # IPv6 private block
    'fe80:',  # link-local unicast
    'ff00:',  # IPv6 multicast
)

IPWARE_NON_PUBLIC_IP_PREFIX = IPWARE_PRIVATE_IP_PREFIX + (
    '127.',  # IPv4 loopback device
    '::1',  # IPv6 loopback device
)

# URLS
BASE_URL = 'http://api.addnow.com'
FRONTEND_BASE_URL = 'http://addnow.com'

# TRIM
TRIM_API = 'https://stage.tr.im/'
TRIM_KEY = ''


# CELERY
CELERY_ALWAYS_EAGER = False
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = None
CELERY_IGNORE_RESULT = True


# Only add pickle to this list if your broker is secured
CELERY_ACCEPT_CONTENT = ['pickle']
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = False
# The 'CELERYD_LOG_FILE' setting is scheduled for deprecation in  version 2.4 and removal in version v4.0.
CELERYD_LOG_FILE = '/var/log/addnow/celery.log'

# http://docs.celeryproject.org/en/master/configuration.html#celeryd-task-time-limit
CELERYD_TASK_SOFT_TIME_LIMIT = 5 * 60  # 5 minutes
CELERYD_TASK_TIME_LIMIT = CELERYD_TASK_SOFT_TIME_LIMIT + 10
CELERYD_HIJACK_ROOT_LOGGER = False

CELERY_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
CELERY_EMAIL_TASK_CONFIG = {
    'ignore_result': True,
    'rate_limit': '50/m',  # 50 emails per minute
    'queue': 'emails',
}

# Route celery tasks according to documentation:
# https://confluence.gravity4.com/display/AN/Tasks
CELERY_CREATE_MISSING_QUEUES = True
CELERY_ROUTES = {
    'addnow.apps.tracker.tasks.add_hook': {
        'queue': 'trim_api',
    },
    'addnow.apps.tracker.tasks.update_counters': {
        'queue': 'mongo_write',
    },
    'addnow.apps.tracker.tasks.save_external_shares': {
        'queue': 'mongo_write',
    },
    'addnow.apps.tracker.tasks.save_geoip_data': {
        'queue': 'mongo_write',
    }
}

CELERYBEAT_SCHEDULE = {
    # Executes every midnight at 0:00 A.M
    'daily-reminders': {
        'task': 'addnow.apps.reminders.tasks.send_reminder',
        'schedule': crontab(minute=0, hour=0),
    },
}
