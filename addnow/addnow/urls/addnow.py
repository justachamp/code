from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('addnow.apps.accounts.urls')),
    url(r'^', include('addnow.apps.reports.urls', namespace='reports')),
    url(r'^', include('addnow.apps.analytics.urls', namespace='analytics')),
    url(r'^', include('addnow.apps.reminders.urls', namespace='reminders'))
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^dashboard/', include('addnow.apps.dashboard.urls', namespace='dashboard')),
        url(r'^trim/', include('addnow.apps.trim.urls'))
    ]

if settings.SHOW_DEMO:
    urlpatterns += [
        url(r'^demo/', include('addnow.apps.demo.urls'))
    ]
