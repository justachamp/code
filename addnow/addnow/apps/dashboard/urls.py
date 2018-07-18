from django.conf.urls import url

from addnow.apps.dashboard import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^logout$', views.logout_start, name='logout_start')
]
