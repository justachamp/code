from django.conf.urls import url
from django.conf import settings as s

from addnow.apps.reminders import views


urlpatterns = [
    url(r'^%s/reminders/mute/(?P<key>[^/]+)$' % s.API_PREFIX, views.ReminderMuteView.as_view(), name='reminder-mute'),
]
