from django.conf import settings


TIMEZONE_CACHE_KEY_PLACEHOLDER = 'analytics-tizezone-%s'
FLOW_CACHE_KEY_PLACEHOLDER = 'analytics-flow-%d'
FLOW_SCOPE = ['https://www.googleapis.com/auth/analytics.readonly']

GA_TIME_ELAPSED = getattr(settings, 'ANALYTICS_GA_TIME_ELAPSED', 60 * 60 * 1)  # 1 hour
DISCOVERY_DOC_TIMEOUT = getattr(settings, 'ANALYTICS_DISCOVERY_DOC_TIMEOUT', 60 * 15)     # 15 minutes
