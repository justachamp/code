from django.conf.urls import url

from addnow.apps.tracker import views

urlpatterns = [
    url(r'^e$', views.track_event, name='track_event'),
    url(r'^s$', views.site_settings, name='site_settings'),
    url(r'^click$', views.click, name='tracker_click'),
    url(r'^click/(?P<site_id>\d+)/(?P<tool>[\w-]+)$', views.click, name='tracker_click_hook'),
    url(r'^click/(?P<site_id>[^/]+)/(?P<tool>[\w-]+)$', views.click, name='tracker_click_hook'),
    url(r'^create_shortlink$', views.create_shortlink, name='tracker_create_shortlink'),
    url(r'^send_email$', views.send_email, name='tracker_send_email'),
    url(r'^counters/(?P<site_id>\d+)$', views.counters, name='counters'),
    url(r'^counters/(?P<site_id>[^/]+)$', views.counters, name='counters'),
    url(r'^vanity_domains$', views.vanity_domains, name='tracker_vanity_domains'),
    url(r'^share/(?P<channel>\w+)$', views.share, name='tracker_share'),
]
