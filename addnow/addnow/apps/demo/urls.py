from django.conf.urls import url

from addnow.apps.demo import views

urlpatterns = [
    url(r'^$', views.demo, name='demo_demo'),

    url(r'^analytics/$', views.RealTimeMap.as_view())
]
