# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
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

GEOIP_LIBRARY_PATH = '/usr/lib64/libGeoIP.so'
