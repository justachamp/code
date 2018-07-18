from .addnow import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'var/test',
    },
}


RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''

MONGODB_NAME = 'addnow_test'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

INSTALLED_APPS += ('snowpenguin.django.recaptcha2', 'django_nose', 'addnow.apps.tracker', 'addnow.apps.demo')

ROOT_URLCONF = 'addnow.urls.unittest'

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'


# REST
REST_FRAMEWORK['TEST_REQUEST_DEFAULT_FORMAT'] = 'json'


# SENTRY
SENTRY_SEND_CELERY_WARNINGS = False

# CELERY
CELERY_RESULT_BACKEND = None
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
BROKER_BACKEND = 'memory'

# CACHE

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'test'
    }
}

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django.db.backends.schema': {
            'level': 'DEBUG',
            'handlers': ['null'],
            'propagate': False
        },
        'factory': {
            'level': 'DEBUG',
            'handlers': ['null'],
            'propagate': False
        },
        '': {
            'level': 'INFO',
            'handlers': ['null'],
        },
    }
}


# GOOGLE OAUTH
GOOGLE_OAUTH_CONFIG = {
    'web': {
        'client_id': '',
        'client_secret': '',
        'redirect_uris': ['http://addnow.com/analytics/auth/'],
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://accounts.google.com/o/oauth2/token',
        'approval_prompt': 'force'
    }
}

DASHBOARD_DIGEST_CACHE_TIMEOUT = 5 * 60  # 5 minutes
COUNTERS_CACHE_TIMEOUT = 5 * 60  # 5 minutes

# LOCAL SETTINGS
try:
    from .addnow_local import *
except ImportError:
    pass
