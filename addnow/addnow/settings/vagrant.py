import logging

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
    ('widget', '/home/vagrant/addnow/widget/dist'),
)

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'addnow',
        'USER': 'addnow',
        'PASSWORD': 'addnow',
        'HOST': '127.0.0.1',
    }
}

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
    'addnow.apps.trim',
    'addnow.apps.demo',
)


# rest_framework & rest_framework_jwt
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'token': '100/sec',
        'password': '100/sec',
    }
}


# URLS
BASE_URL = 'http://api.addnow.dev:8081'
FRONTEND_BASE_URL = 'http://addnow.dev:8081'

# GOOGLE OAUTH
GOOGLE_OAUTH_CONFIG = {
    'web': {
        'client_id': '951076774379-hdmeoim87h5faecg8gqvgu3i81h1vt5i.apps.googleusercontent.com',
        'client_secret': 'W_khkikY0CutUeoZpymhN-Rh',
        'redirect_uris': ['http://addnow.dev:8081/analytics/auth/'],
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://accounts.google.com/o/oauth2/token',
        'approval_prompt': 'force'
    }
}


TRIM_API = 'https://stage.tr.im/'
TRIM_KEY = 'a0135807f276796eb2d9f785353a8057'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)s %(message)s'
        },
    },
    'root': {
        'handlers': ['default'],
        'level': 'DEBUG'
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/addnow/addnow.log',
            'maxBytes': 1024 * 1024 * 500,  # 500 MB
            'backupCount': 15,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'django': {
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


# LOCAL SETTINGS
try:
    if ADDNOW_APP == 'tracker':
        from .tracker_local import *
    else:
        from .addnow_local import *
except ImportError:
    pass
