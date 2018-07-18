from sendfile import sendfile

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from ui.utils import render_to_json, append_dollar


@login_required
@require_POST
def change_password(request):
    user = request.user
    password = request.POST['password']
    new_password = request.POST['new_password']

    if not user.check_password(password):
        return HttpResponse(
            'Please type correctly your old password!',
            status=400
        )

    user.set_password(new_password)
    user.save()

    return HttpResponse()


@login_required
@require_POST
def update_counter(request):
    '''
    Updates unread events counter for logged in user
    with data provided by frontend (stored in counter parameter
    in POST data).
    '''
    user = request.user

    user.unread_events_count = request.POST['counter']
    user.save()

    return HttpResponse()


@login_required
@render_to_json()
def billing_info(request):
    account = request.user.account

    return {
        'account_balance': append_dollar(account.account_balance()),
        'last_payment': append_dollar(account.last_payment),
        'transactions': account.transactions,
    }


@login_required
def download_invoice(request, id):
    '''
    Downloads invoice pdf for a given invoice within an account.
    '''
    invoice = get_object_or_404(request.user.account.invoice_set, id=id)
    return sendfile(request, invoice.pdf.path, attachment=True)
