from django.http import HttpResponseBadRequest

from oauth2client.client import AccessTokenRefreshError
from oauth2client.contrib.django_orm import Storage


from addnow.apps.analytics.models import CredentialsModel


class AnalyticsExceptionMiddleware(object):
    def process_exception(self, request, exception):
        if isinstance(exception, AccessTokenRefreshError):
            storage = Storage(CredentialsModel, 'user', request.user, 'credential')
            storage.delete()

            return HttpResponseBadRequest(
                content=b'{"message": "%s"}' % exception.message,
                content_type='application/json')

        return None
