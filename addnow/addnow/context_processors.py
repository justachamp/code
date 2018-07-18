"""
A set of request processors that return dictionaries to be merged into a
template context. Each function takes the request object as its only parameter
and returns a dictionary to add to the context.

These are referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and used by
RequestContext.
"""
from django.conf import settings


def base_url(request):
    """
    Adds BASE_URL variable to the template context.

    """
    return {'BASE_URL': settings.BASE_URL}
