from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def static_bust(url):
    """Construct static url with asset versioning."""
    return settings.STATIC_URL + url + '?v=' + settings.VERSION
