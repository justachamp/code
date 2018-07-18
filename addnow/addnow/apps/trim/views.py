from json import dumps
from urllib import urlencode

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict


@csrf_exempt
def mock(request):
    post = request.POST
    if 'CONTENT_TYPE' not in request.META:
        post = QueryDict(request.body)

    return HttpResponse(
        dumps(
            {'short_url': post.get('url', 'null') + '?' +
                urlencode({'hook': post.get('hook', 'null')})}
        ))
