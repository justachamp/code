from django.conf.urls import url
from django.conf import settings

from addnow.apps.reports import views

urlpatterns = [
    url(r'^%s/reports/sites/(?P<site_id>\d+)/visitors$' % settings.API_PREFIX,
        views.ActiveVisitorsView.as_view(), name='active_visitors'),

    url(r'^%s/reports$' % settings.API_PREFIX, views.GetReport.as_view(), name='reports'),
    url(r'^%s/digest$' % settings.API_PREFIX, views.GetDigest.as_view(), name='digest'),
]
