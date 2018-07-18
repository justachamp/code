from . import get_env_variable


# Get Addnow App
ADDNOW_APP = get_env_variable('ADDNOW_APP')

# Import app settings
if ADDNOW_APP == 'tracker':
    from .tracker import *
else:
    from .addnow import *


STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('widget', '/data/addnow/addnow/widget/dist'),
)

DEBUG = True

BASE_URL = 'http://api.testing.addnow.com'
FRONTEND_BASE_URL = 'http://testing.addnow.com:80'

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
    'addnow.apps.trim',
    'addnow.apps.demo',
)

TRIM_KEY = 'a0135807f276796eb2d9f785353a8057'

RAVEN_CONFIG = {
    'dsn': 'https://4b9b8ce5055d450b8034b37e038abdd2:07ffe0ba352d49a684e696d364f228d1@app.getsentry.com/38999',
}


# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
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
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler'
        }
    },
    'loggers': {
        'django': {
            'level': 'ERROR',
            'handlers': ['logfile'],
            'propagate': False
        },
        'django.request': {
            'level': 'ERROR',
            'handlers': ['logfile'],
            'propagate': False
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['logfile'],
            'propagate': False
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['logfile'],
            'propagate': False
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['logfile'],
            'propagate': False
        },
        'addnow.apps.accounts': {
            'level': 'DEBUG',
            'handlers': ['logfile']
        },
        'addnow.apps.tracker': {
            'level': 'DEBUG',
            'handlers': ['logfile']
        },
        'addnow.apps.reports': {
            'level': 'DEBUG',
            'handlers': ['logfile']
        },
        'addnow.apps.dashboard': {
            'level': 'DEBUG',
            'handlers': ['logfile']
        },
        'addnow.apps.demo': {
            'level': 'DEBUG',
            'handlers': ['logfile']
        },
        'addnow.apps.trim': {
            'level': 'DEBUG',
            'handlers': ['logfile']
        }
    }
}

# GOOGLE OAUTH
GOOGLE_OAUTH_CONFIG = {
    'web': {
        'client_id': '951076774379-hdmeoim87h5faecg8gqvgu3i81h1vt5i.apps.googleusercontent.com',
        'client_secret': 'W_khkikY0CutUeoZpymhN-Rh',
        'redirect_uris': ['http://testing.addnow.com/analytics/auth/'],
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://accounts.google.com/o/oauth2/token',
        'approval_prompt': 'force'
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
