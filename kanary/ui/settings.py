import sys
from datetime import timedelta
from path import path

from celery import Celery
from celery.schedules import crontab

sys.path.append(str(path(__file__).dirname().abspath().parent))


from etc.config import settings
from etc.constants import __version__


DEBUG = settings.globals_debug
TEMPLATE_DEBUG = DEBUG

PROJECT_DIR = path(__file__).dirname().abspath()
PROJECT_NAME = 'Kanary'

ADMINS = (
    ('The A room', 'thearoom@clearcode.cc')
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': settings.ui_db_engine,
        'NAME': settings.ui_db_name,
        'USER': settings.ui_db_user,
        'PASSWORD': settings.ui_db_pass,
        'HOST': settings.ui_db_host,
        'PORT': settings.ui_db_port,
    },
}

FRONTEND_HOST = settings.ui_frontend_url

ALLOWED_HOSTS = settings.ui_allowed_hosts

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s %(asctime)s %(thread)d] '
                      '%(module)s:%(funcName)s - %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': settings.ui_loglevel,
        },
        'celery': {
            'handlers': ['console'],
            'propagate': True,
            'level': settings.ui_loglevel,
        },
    }
}

CELERYD_HIJACK_ROOT_LOGGER = False

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = settings.globals_timezone_name
USE_TZ = False

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_DIR / 'media'
# creatives directory location
CREATIVES_DIR = MEDIA_ROOT / 'creatives'
# invoices directory location
INVOICES_DIR = MEDIA_ROOT / 'invoices'

# create media subfolders if they not exist
path(MEDIA_ROOT).mkdir_p()
path(CREATIVES_DIR).mkdir_p()
path(INVOICES_DIR).mkdir_p()

# minimum age of creative file on filesystem, before we check if it's abandoned
# in hours
CREATIVE_CLEAN_MIN_AGE = 24

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# Directory for uploading things with Ajax Uploader
TMP_UPLOAD_DIR = 'tmp'
CREATIVES_UPLOAD_DIR = 'creatives'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'


STATIC_ROOT = PROJECT_DIR / 'static'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR / 'frontend',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# mailing static dir
MAILING_STATIC_DIR = PROJECT_DIR / 'frontend' / 'assets' / 'images' / 'mailing'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # ~ 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '7!58$*37z)3iq$1q&6$$_7^)@4iul2+43i^hjblnj6=*3ny!^h'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "ui.context_processors.settings_context",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'ui.backend.middleware.FrontendReloaderMiddleware',
    'ui.backend.middleware.CompleteSignupFormMiddleware',
    'ui.backend.middleware.UpdatedInfoAboutUser',
)

ROOT_URLCONF = 'ui.urls'

CSRF_FAILURE_VIEW = 'ui.backend.views.auth.csrf_failure'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

CACHE_REDIS = {
    'BACKEND': 'redis_cache.cache.RedisCache',
    'LOCATION': '{0}:{1}:{2}'.format(
        settings.targeting_cache_redis_host,
        settings.targeting_cache_redis_port,
        settings.targeting_cache_redis_db,
    ),
    'TIMEOUT': 99999999,  # Expire almost never (not possible to set it
                          # into infinite in Django 1.6.5)
    'OPTIONS': {
        'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        'PARSER_CLASS': 'redis.connection.HiredisParser',
    }
}

CACHES = {
    'default': CACHE_REDIS,
    'targetvalues': CACHE_REDIS,
    'spendings': CACHE_REDIS
}


# Used for correct redirects when django served behind other server:
USE_X_FORWARDED_HOST = True

AUTH_USER_MODEL = 'account.User'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
    'south',
    'kombu.transport.django',
    'djcelery_email',
    'mptt',
    'loginas',
    'ajaxuploader',
    'tastypie',
    'django_extensions',
    'django_js_reverse',
    'gunicorn',
    'haystack',
    'celery_haystack',
    'polymorphic',
    'ui.common',
    'ui.account',
    'ui.backend',
    'ui.storage',
    'ui.targeting',
    'ui.campaign',
    'ui.report',
    'ui.bidding_spendings',
    'ui.notification',
    'ui.cache',
    'ui.publishers',
    'ui.liveview'
)

BROKER_URL = settings.ui_celery_broker

SOUTH_MIGRATION_MODULES = {
    'django': 'ignore',
    'tastypie': 'ignore',
}

REDIS = {
    'adserver': {
        'host': settings.adserver_storage_redis_host,
        'port': settings.adserver_storage_redis_port,
        'db': settings.adserver_storage_redis_db,
    },
    'targeting': {
        'host': settings.targeting_redis_host,
        'port': settings.targeting_redis_port,
        'db': settings.targeting_redis_db,
    },
    'targeting_cache': {
        'host': settings.targeting_cache_redis_host,
        'port': settings.targeting_cache_redis_port,
        'db': settings.targeting_cache_redis_db,
    },
    'bidder_spendings': {
        'host': settings.spending_redis_host,
        'port': settings.spending_redis_port,
        'db': settings.spending_redis_db,
    },
    'profiles': {
        'host': settings.profiles_redis_host,
        'port': settings.profiles_redis_port,
        'db': settings.profiles_redis_db,
    },
    'probabilities': {
        'host': settings.probabilities_master_redis_host,
        'port': settings.probabilities_master_redis_port,
        'db': settings.probabilities_redis_db,
    },
    'optimizer': {
        'host': settings.optimizer_redis_host,
        'port': settings.optimizer_redis_port,
        'db': settings.optimizer_redis_db,
    }
}

# List of acceptable serializers
# http://celery.readthedocs.org/en/latest/userguide/security.html#serializers
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

# Keep number of celery workers greater than 3 because there are many tasks
# that are I/O bound (API calls) and these shouldn't block others e.g.
# spendings updates which must be called really often.
CELERYD_CONCURRENCY = settings.ui_celery_concurrency

CELERYD_MAX_TASKS_PER_CHILD = settings.ui_celeryd_max_tasks_per_child

# Most of tasks should be finished within max one/two minutes.
# Longer task should define own time limit if longer execution is expected.
CELERYD_TASK_TIME_LIMIT = 90

CELERY_TASK_RETRY_EXPONENTIAL_BASE = settings.ui_celery_retry_base

# results storing disabled, if you want to enable it, do it on per task-basis
# via ignore_result=False argument
CELERY_IGNORE_RESULT = True
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = False

# There's no need to use sql for celery results, we can benefit from RabbitMQ
# backend - SQL not required to run and results cleanup
# (celery.backend_cleanup) shouldn't torture SQL database.
CELERY_RESULT_BACKEND = 'amqp://'

AMAZON_BUCKET = settings.ui_amazon_bucket
AMAZON_ACCESS_KEY = settings.ui_amazon_access_key
AMAZON_SECRET_KEY = settings.ui_amazon_secret_key

# Length of period in seconds that is used in even distribution of budget
DISTRIBUTE_BUDGET_EVENLY_PERIOD = 60

targeting_sync_timeout = settings.bidders_targeting_sync_timeout / 2

# specific automatic queues.
# to make sure worker eats queue, add -Q parameter,
# define queues separated by comma:
#
# celery worker -A ui -Q spendings,targeting
#
# Use -X to tell worker to process all queues except these.
#
CELERY_ROUTES = {
    'ui.bidding_spendings.tasks.import_spendings': {
        'queue': 'spendings'},
    'ui.bidding_spendings.tasks.update_bidder_spendings': {
        'queue': 'spendings'},
    'ui.campaign.tasks.update_probabilities_task': {
        'queue': 'spendings'},
    'ui.cache.tasks.trigger_cache_mappings': {
        'queue': 'targeting'},
    'ui.targeting.tasks.bidder_targeting_ping': {
        'queue': 'targeting'},
    'ui.storage.tasks.appnexus_update_status_all': {
        'queue': 'appnexus_api'},
    'ui.storage.tasks.send_for_audit': {
        'queue': 'appnexus_api'},
    'ui.storage.tasks.update_brand_access_status': {
        'queue': 'appnexus_api'},
    'ui.targeting.tasks.appnexus_targeting_update': {
        'queue': 'appnexus_api'},
    'ui.targeting.tasks.appnexus_location_translation': {
        'queue': 'targeting'},
    'ui.publishers.tasks.appnexus_publishers_translation_update': {
        'queue': 'appnexus_api'},
    'ui.report.tasks.appnexus_publishers_translation_update': {
        'queue': 'spendings'},
}

# All tasks not defined here will be routed to default 'celery' queue!

CELERYBEAT_SCHEDULE = {
    'import-bidding-spendings': {
        'task': 'ui.bidding_spendings.tasks.import_spendings',
        'schedule': timedelta(seconds=60),
    },
    'update-bidder-spendings': {
        'task': 'ui.bidding_spendings.tasks.update_bidder_spendings',
        'schedule': timedelta(seconds=settings.spending_expire_interval),
    },
    'clear_daily_spendings': {
        'task': 'ui.bidding_spendings.tasks.clear_daily_spendings',
        'schedule': crontab(hour=23, minute=59),
    },
    'update-daily-spendings-hour': {
        'task': 'ui.bidding_spendings.tasks.'
                'put_today_spendings_to_daily_spendings',
        'schedule': timedelta(hours=1),
    },
    'update-daily-spendings-day': {
        'task': 'ui.bidding_spendings.tasks.put_spendings_to_daily_spendings',
        'schedule': timedelta(hours=24),
    },
    'update-prices-probabilities': {
        'task': 'ui.campaign.tasks.update_probabilities_task',
        'schedule': timedelta(seconds=settings.prices_sync_timeout / 3)
    },
    'trigger-cache-mappings': {
        'task': 'ui.cache.tasks.trigger_cache_mappings',
        'schedule': timedelta(seconds=60),
    },
    'ping-targeting': {
        'task': 'ui.targeting.tasks.bidder_targeting_ping',
        'schedule': timedelta(seconds=targeting_sync_timeout),
    },
    'appnexus_update_status_all': {
        'task': 'ui.storage.tasks.appnexus_update_status_all',
        'schedule': timedelta(minutes=15),
    },
    'appnexus_send_for_audit': {
        'task': 'ui.storage.tasks.send_for_audit',
        'schedule': timedelta(seconds=60),
    },
    'appnexus_update_brand_access_status': {
        'task': 'ui.storage.tasks.update_brand_access_status',
        'schedule': timedelta(seconds=60),
    },
    'targeting_appnexus_update': {
        'task': 'ui.targeting.tasks.appnexus_targeting_update',
        'schedule': timedelta(hours=12),
    },
    'targeting_appnexus_location_translation': {
        'task': 'ui.targeting.tasks.appnexus_location_translation',
        'schedule': crontab(hour=23, minute=59),
    },
    'appnexus_publishers_translate': {
        'task': 'ui.publishers.tasks.appnexus_publishers_translation_update',
        'schedule': timedelta(hours=2),
        'options': {'retry': False},
    },
    'update_video_creative_media': {
        'task': 'ui.storage.tasks.update_video_creative_media',
        'schedule': timedelta(minutes=15),
    },
    'translate_fixed_networks': {
        'task': 'ui.publishers.tasks.fixed_publishers_translation_update',
        'schedule': timedelta(minutes=30),
        'options': {'retry': False},
    },
    'clean_unsaved_files': {
        'task': 'ui.storage.tasks.clean_unsaved_files',
        'schedule': timedelta(hours=24),
        'args': (CREATIVE_CLEAN_MIN_AGE, )
    },
    'check_account_funds': {
        'task': 'ui.account.tasks.check_account_funds',
        'schedule': timedelta(minutes=5),
    },
    'populate_graphite': {
        'task': 'ui.tasks.send_appnexus_metrics_to_graphite',
        'schedule': timedelta(minutes=1),
        'options': {'retry': False},
    },
    'send_lotame_reports': {
        'task': 'ui.report.tasks.send_lotame_email_report',
        'schedule': crontab(minute=0, hour=0, day_of_month=15),
    }
}
CELERY_SEND_TASK_ERROR_EMAILS = settings.ui_celery_send_emails

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': settings.ui_haystack_search_engine,
        'URL': settings.ui_haystack_elastic_url,
        'INDEX_NAME': settings.ui_haystack_elastic_index
    }
}
HAYSTACK_SIGNAL_PROCESSOR = 'ui.signals.KanarySignalProcessor'


ELASTICSEARCH_INDEX_SETTINGS = {
    'settings': {
        "analysis": {
            "analyzer": {
                "ngram_analyzer": {
                    "type": "custom",
                    "tokenizer": "lowercase",
                    "filter": ["haystack_ngram"]
                },
                "edgengram_analyzer": {
                    "type": "custom",
                    "tokenizer": "lowercase",
                    "filter": ["haystack_edgengram"]
                },
                "autocomplete": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "kstem", "haystack_edgengram"]
                }
            },
            "tokenizer": {
                "haystack_ngram_tokenizer": {
                    "type": "nGram",
                    "min_gram": 3,
                    "max_gram": 15,
                },
                "haystack_edgengram_tokenizer": {
                    "type": "edgeNGram",
                    "min_gram": 2,
                    "max_gram": 15,
                    "side": "front"
                },
            },
            "filter": {
                "haystack_ngram": {
                    "type": "nGram",
                    "min_gram": 3,
                    "max_gram": 15
                },
                "haystack_edgengram": {
                    "type": "edgeNGram",
                    "min_gram": 2,
                    "max_gram": 15
                }
            }
        }
    }
}


SERVE_STATIC = settings.ui_serve_static
JS_BE_QUIET = settings.ui_js_be_quiet
REQUIRE_TIMEOUT = settings.ui_require_timeout


# Live view
LIVE_VIEW_POLLING_INTERVAL = settings.ui_live_view_polling_interval
LIVE_VIEW_IS_ENABLED = settings.liveview_turned

# sentry
RAVEN_CONFIG = {'dsn': settings.globals_sentry_dsn, }

# used for reloading frontend
VERSION = __version__

# tastypie
API_LIMIT_PER_PAGE = 10000  # Almost infinity.
TASTYPIE_FULL_DEBUG = True

# django-sendfiles
SENDFILE_BACKEND = settings.ui_sendfile_backend
# for serving files through Nginx
SENDFILE_ROOT = MEDIA_ROOT
SENDFILE_URL = MEDIA_URL

INTERCOM_APP_ID = settings.ui_intercom_app_id

EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
CELERY_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = settings.ui_smtp_host
EMAIL_PORT = settings.ui_smtp_port
EMAIL_HOST_USER = settings.ui_smtp_user
EMAIL_HOST_PASSWORD = settings.ui_smtp_password
EMAIL_USE_TLS = settings.ui_smtp_use_tls
DEFAULT_FROM_EMAIL = settings.ui_default_from_email


TARGETING_UPDATE_TIMELIMIT = settings.ui_targeting_update_timelimit
TRIGGER_CACHE_MAPPINGS_TIMELIMIT = settings.ui_trigger_cache_mappings_timelimit
APPNEXUS_PUBLISHERS_TRANSLATION_UPDATE_TIMELIMIT = settings.ui_appnexus_publishers_translation_update_timelimit

# don't use settings_local, use etc/config.ini

AJAX_HEADER_X_VERSION = 'X-Started'
AJAX_HEADER_USER_INFO = 'User-Info'


app = Celery('ui')
app.config_from_object('ui.settings')
app.autodiscover_tasks(lambda: INSTALLED_APPS)
