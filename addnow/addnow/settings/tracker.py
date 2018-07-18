from .default import *


FORCE_SCRIPT_NAME = '/tracker'  # should be synchronized with nginx location

INSTALLED_APPS = (
    # 3d party apps
    'snowpenguin.django.recaptcha2',
    'corsheaders',

    # apps
    'addnow.apps.accounts',
    'addnow.apps.tracker',

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
            'filename': '/var/log/addnow/tracker.log',
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
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'addnow.urls.tracker'

WSGI_APPLICATION = 'tracker_wsgi.application'


###################################
# Installed App Specific SETTINGS #
###################################


# corsheaders
CORS_URLS_REGEX = r'^/.*$'


RECAPTCHA_PUBLIC_KEY = '6LdFMgQTAAAAAIM7V7Sp0ossA5_RAvneGQLMAQQO'
RECAPTCHA_PRIVATE_KEY = '6LdFMgQTAAAAAFNYC6c3t4X-DCOEPYhttnoDckmX'


COUNTERS_CACHE_TIMEOUT = 30 * 24 * 60 * 60  # 30 days
