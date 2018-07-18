from urllib import quote_plus

from django.conf import settings as ui_settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from etc.config import settings


@login_required
def main(request):
    from ui.utils.js import js_config
    context = {
        'js_config': js_config,
        'user': request.user,
        'INTERCOM_APP_ID': ui_settings.INTERCOM_APP_ID,
    }
    return render(request, 'backend/index.html', context)


@login_required
def deposit_funds(request):
    """
        Redirects to PayPal service. If on localhost, it just redirects
        to mockup page of PayPal service.
    """
    url = settings.ui_paypal_button_url

    if request.REQUEST.get('signup'):
        view_name = 'processing_payment'
    else:
        view_name = 'payment_confirmation'

    return_url = request.build_absolute_uri(reverse(view_name))

    if url:
        url = url % {
            'return_url': quote_plus(return_url),
            'account_id': request.user.account.id
        }
        return redirect(url)
    else:
        return render(request, 'backend/paypal_mock.html', dict(return_url=return_url))


@login_required
def payment_confirmation(request):
    """
        It is return page from PayPal service. It just redirects to correct page of one-page app, because PayPal
        can't redirect back to urls with hash (#).
    """
    return redirect('{0}#/account/payment'.format(request.build_absolute_uri(reverse('main'))))


def status(request):
    return HttpResponse('ok')
