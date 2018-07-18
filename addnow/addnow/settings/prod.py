from . import get_env_variable


# Get Addnow App
ADDNOW_APP = get_env_variable('ADDNOW_APP')

# Import app settings
if ADDNOW_APP == 'tracker':
    from .tracker import *
else:
    from .addnow import *


DEBUG = False
TEMPLATE_DEBUG = False

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [
            'redis://addnowprodredis2.emhym6.0001.use1.cache.amazonaws.com:6379/1'
        ],
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'addnow',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'addnow-prod.c89rwkwiidnr.us-east-1.rds.amazonaws.com',
    }
}


# pymongo
MONGODB_URI = 'mongodb://mongodb-0,mongodb-1,mongodb-2/?replicaSet=addnow-prod&readPreference=secondary'

TRIM_KEY = 'df3f818ec966040c485f6409f938970b'
TRIM_API = 'https://tr.im/'

GEOIP_LIBRARY_PATH = '/usr/lib64/libGeoIP.so'


# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'INFO',
        'handlers': ['logfile', 'sentry'],
    },
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/addnow/%s.log' % ADDNOW_APP,
            'formatter': 'standard',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['logfile'],
            'propagate': False,
        },
        'django': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': False,
        },
        'celery': {
            'handlers': ['logfile'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}

# Close demo page for production environment
SHOW_DEMO = False

# GOOGLE OAUTH
GOOGLE_OAUTH_CONFIG = {
    'web': {
        'client_id': '951076774379-hdmeoim87h5faecg8gqvgu3i81h1vt5i.apps.googleusercontent.com',
        'client_secret': 'W_khkikY0CutUeoZpymhN-Rh',
        'redirect_uris': ['http://addnow.com/analytics/auth/'],
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://accounts.google.com/o/oauth2/token',
        'approval_prompt': 'force'
    }
}

# LOCAL SETTINGS
try:
    if ADDNOW_APP == 'tracker':
        from .tracker_local import *
    else:
        from .addnow_local import *
except ImportError:
    pass
