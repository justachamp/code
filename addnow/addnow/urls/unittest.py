from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('addnow.urls.addnow')),
    url(r'^', include('addnow.urls.tracker')),
    url(r'^dashboard/', include('addnow.apps.dashboard.urls', namespace='dashboard')),
]
