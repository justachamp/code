from django.conf import settings

from rest_framework.permissions import SAFE_METHODS
from rest_framework.throttling import UserRateThrottle


if settings.API_TEST:
    class BaseUserRateThrottle(UserRateThrottle):
        def allow_request(self, request, view):
            return request.META.get('HTTP_X_BOT') != '1'

        def wait(self):
            return 1

else:
    class BaseUserRateThrottle(UserRateThrottle):
        def allow_request(self, request, view):
            if request.method in SAFE_METHODS:
                return True
            return super(UserRateThrottle, self).allow_request(request, view)


class TokenRateThrottle(BaseUserRateThrottle):
    scope = 'token'


class UpdateAccountRateThrottle(BaseUserRateThrottle):
    scope = 'password'
