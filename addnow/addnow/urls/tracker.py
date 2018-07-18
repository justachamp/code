from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('addnow.apps.tracker.urls')),
]
