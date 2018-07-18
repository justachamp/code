from urlparse import urlparse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from addnow.apps.accounts.models import Site
from addnow.apps.accounts import constants


@login_required
def demo(request):
    try:
        site = Site.objects.get(user=request.user, domain=request.GET.get('domain'))
    except (Site.DoesNotExist, ValueError):
        site = Site.objects.filter(user=request.user).first()

    base_url = urlparse(settings.BASE_URL)
    frontend_base_url = urlparse(settings.FRONTEND_BASE_URL)

    context = {
        'site': site,
        'widgets': site.widgets.exclude(type=constants.WIDGET_CONFIGURATION_COPY_PASTE),
        'styles': constants.styles,
        'backend': base_url.netloc,
        'frontend': frontend_base_url.netloc
    }
    return render(request, 'demo/demo.html', context)


class RealTimeMap(TemplateView):
    template_name = 'demo/analytics.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RealTimeMap, self).dispatch(*args, **kwargs)
