from django.conf.urls import url

from addnow.apps.trim import views

urlpatterns = [
    url(r'^$', views.mock),
]
