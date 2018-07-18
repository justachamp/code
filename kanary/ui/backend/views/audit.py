"""
Receiving Audit Notify Request
https://wiki.appnexus.com/display/adnexusdocumentation/Audit+Notify+Request
"""

import simplejson

from django.http import HttpResponse
from django.views.decorators.http import require_POST

from ui.storage.tasks import audit_notify_request


@require_POST
def audit_notify(request):
    notify = simplejson.loads(request.body)
    audit_notify_request.delay(notify)
    return HttpResponse()
