import logging


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#     }
# }
import sys

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'addnow-dev',
        'USER': 'addnow',
        'PASSWORD': 'addnow',
        'HOST': '127.0.0.1',
        'CONN_MAX_AGE': 300
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATICFILES_DIRS = (
    ('widget', '/opt/thumbtack/addnow/widget/dist'),
)

GEOIP_LIBRARY_PATH = '/usr/lib64/libGeoIP.so'


# URLS
BASE_URL = 'http://api.addnow.dev'
FRONTEND_BASE_URL = 'http://addnow.dev'

# GOOGLE OAUTH
GOOGLE_OAUTH_CONFIG = {
    'web': {
        'client_id': '951076774379-hdmeoim87h5faecg8gqvgu3i81h1vt5i.apps.googleusercontent.com',
        'client_secret': 'W_khkikY0CutUeoZpymhN-Rh',
        'redirect_uris': ['http://addnow.dev/analytics/auth/'],
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://accounts.google.com/o/oauth2/token',
        'approval_prompt': 'force'
    }
}

RAVEN_CONFIG = {
    'dsn': 'http://d01626fc524e416883d0a9ddbcf828eb:dc49d3d4f37e47fdace3fa5c21fc4b16@sentry.wheel-size.com/6',
    'CELERY_LOGLEVEL': logging.INFO
}

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)s %(message)s'
        },
    },
    'root': {
        'handlers': ['console', 'sentry'],
        'level': 'DEBUG'
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django': {
            'level': 'ERROR'
        },
        'googleapiclient': {
            'level': 'ERROR'
        },
        'addnow.apps.analytics': {
            'level': 'ERROR'
        }
    }
}

# Get all the existing loggers
root = logging.root
existing = root.manager.loggerDict.keys()

# Set them explicitly to a blank value so that they are overidden
# and propagate to the root logger
for logger in existing:
    LOGGING['loggers'][logger] = {}


DASHBOARD_DIGEST_CACHE_TIMEOUT = 2 * 60  # 2 minutes
