from etc.config import settings as kanary_settings
from django.conf import settings


def settings_context(request):
    return {
        'SIGNUP_ENABLED': kanary_settings.ui_enable_signup,
        'VERSION': settings.VERSION
    }
