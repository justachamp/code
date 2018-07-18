import datetime

from .default import *


INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',

    # 3d party apps
    'corsheaders',
    'djcelery_email',
    'post_office',
    'rest_framework',

    # addnow apps
    'addnow.apps.accounts',
    'addnow.apps.analytics',
    'addnow.apps.dashboard',
    'addnow.apps.reminders',
    'addnow.apps.reports'
)

# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)s %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/addnow/addnow.log',
            'maxBytes': 1024 * 1024 * 500,  # 500 MB
            'backupCount': 15,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['default'],
            'propagate': False,
        },
        '': {
            'level': 'INFO',
            'handlers': ['default'],
        },
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'addnow.apps.analytics.middleware.AnalyticsExceptionMiddleware'
)

ROOT_URLCONF = 'addnow.urls.addnow'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',

                'addnow.context_processors.base_url',
            ),
        }
    },
]

WSGI_APPLICATION = 'addnow_wsgi.application'


###################################
# Installed App Specific SETTINGS #
###################################


# corsheaders
CORS_URLS_REGEX = r'^/api/.*$'

# rest_framework & rest_framework_jwt
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'token': '20/day',
        'password': '10/hour',
    }
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7)
}

# Open demo page
SHOW_DEMO = True

DASHBOARD_DIGEST_CACHE_TIMEOUT = 86400

SUIT_CONFIG = {
    'ADMIN_NAME': 'G4 Addnow',
    'SEARCH_URL': '/admin/accounts/site/',
    'MENU_EXCLUDE': ('auth',),
    'LIST_PER_PAGE': 50
}
