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

ALLOWED_HOSTS = [
    '.stage.addnow.com',
    '.staging.addnow.com'
]

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [
            'redis://addnow-stage-redis.emhym6.0001.use1.cache.amazonaws.com:6379/1'
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
        'USER': 'addnow',
        'PASSWORD': 'pothDoopdolyodHecAylfiv4',
        'HOST': 'addnow-stage.c89rwkwiidnr.us-east-1.rds.amazonaws.com',
    }
}

# INSTALLED APPS
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
    'addnow.apps.trim',
    'addnow.apps.demo',
)

# pymongo
MONGODB_URI = 'mongodb://mongodb-0:27017,mongodb-1:27017,mongodb-2:27017/?replicaSet=addnow-stage'


TRIM_KEY = 'a0135807f276796eb2d9f785353a8057'
TRIM_API = 'https://stage.tr.im/'

GEOIP_LIBRARY_PATH = '/usr/lib64/libGeoIP.so'


# URLS
BASE_URL = 'http://api.staging.addnow.com'
FRONTEND_BASE_URL = 'http://staging.addnow.com'


# GOOGLE OAUTH
GOOGLE_OAUTH_CONFIG = {
    'web': {
        'client_id': '951076774379-hdmeoim87h5faecg8gqvgu3i81h1vt5i.apps.googleusercontent.com',
        'client_secret': 'W_khkikY0CutUeoZpymhN-Rh',
        'redirect_uris': ['http://staging.addnow.com/analytics/auth/'],
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://accounts.google.com/o/oauth2/token',
        'approval_prompt': 'force'
    }
}

RAVEN_CONFIG = {
    'dsn': 'https://4b9b8ce5055d450b8034b37e038abdd2:07ffe0ba352d49a684e696d364f228d1@app.getsentry.com/38999',
}

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
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
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['logfile'],
            'level': 'INFO',
        },
        'addnow.apps.accounts': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        },
        'addnow.apps.tracker': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        },
        'addnow.apps.reports': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        },
        'addnow.apps.dashboard': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        },
        'addnow.apps.demo': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        },
        'addnow.apps.trim': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        },
    },
}

CELERYBEAT_SCHEDULE = {
    'create-site-stats-report': {
        'task': 'addnow.apps.reports.tasks.site_stats',
        'schedule': crontab(hour=0, minute=30),
        'args': (['sergio@gravity4.com'],),
    }
}


DASHBOARD_DIGEST_CACHE_TIMEOUT = 5 * 60  # 5 minutes
COUNTERS_CACHE_TIMEOUT = 5 * 60  # 5 minutes

# LOCAL SETTINGS
try:
    if ADDNOW_APP == 'tracker':
        from .tracker_local import *
    else:
        from .addnow_local import *
except ImportError:
    pass
