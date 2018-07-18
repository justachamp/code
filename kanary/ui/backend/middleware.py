import simplejson

from django.conf import settings
from django.shortcuts import redirect

from django.core.urlresolvers import reverse


def user_is_authenticated(request):
    """
    :returns: True if user in given `django.http.HttpRequest` is authenticated
    :rtype bool
    """
    return hasattr(request, 'user') and request.user.is_authenticated()


class FrontendReloaderMiddleware(object):

    """
    If Kanary version updated, please inform user about it.
    """

    def process_response(self, request, response):
        """
        We only add this info to ajax requests.
        """
        if request.is_ajax():
            response[settings.AJAX_HEADER_X_VERSION] = settings.VERSION
        return response


class CompleteSignupFormMiddleware(object):

    """
    When user has is_signup_complete flag set to False
    she will be always redirected to the profile info form.
    """

    # When request is made to one of this path we do not redirect:
    EXCLUDE_URLS = (reverse('fetch_states'), reverse('create_profile'),
                    reverse('js_reverse'), )

    def process_response(self, request, response):

        # For urls without trailing slash, AuthenticationMiddleware would
        # not append user to the request object.

        if user_is_authenticated(request) and \
                request.path not in self.EXCLUDE_URLS and \
                not request.user.is_signup_complete:
            return redirect('create_profile')

        return response


class UpdatedInfoAboutUser(object):

    """
    Include message count and account balance in every request header instead
    of polling for fresh data.
    """

    def process_response(self, request, response):
        """
        We only add this info to ajax requests of logged in users.
        """
        if request.is_ajax() and user_is_authenticated(request):
            user = request.user

            response[settings.AJAX_HEADER_USER_INFO] = simplejson.dumps({
                "unread_events_count": user.unread_events_count,
                "account_balance": user.account.account_balance(),
            })

        return response
