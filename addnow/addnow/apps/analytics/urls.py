from django.conf.urls import url
from django.conf import settings

from addnow.apps.analytics import views


urlpatterns = [
    url(r'^%s/analytics/login$' % settings.API_PREFIX, views.LoginView.as_view(), name='analytics_login'),
    url(r'^%s/analytics/logout$' % settings.API_PREFIX, views.LogoutView.as_view(), name='analytics_logout'),
    url(r'^%s/analytics/auth$' % settings.API_PREFIX, views.AuthCallbackView.as_view(), name='analytics_auth'),
    url(r'^%s/analytics/accounts$' % settings.API_PREFIX, views.AccountsView.as_view(), name='accounts'),
    url(r'^%s/analytics/sites/(?P<site_id>\d+)/pageviews$' % settings.API_PREFIX,
        views.PageviewsView.as_view(), name='pageviews'),
    url(r'^%s/analytics/sites/(?P<site_id>\d+)/referring-domains$' % settings.API_PREFIX,
        views.ReferringDomainsView.as_view(), name='referring_domains'),
    url(r'^%s/analytics/sites/(?P<site_id>\d+)/search-terms$' % settings.API_PREFIX,
        views.SearchTermsView.as_view(), name='search_terms'),
    url(r'^%s/analytics/sites/(?P<site_id>\d+)/search-engines$' % settings.API_PREFIX,
        views.SearchEnginesView.as_view(), name='search_engines'),
    url(r'^%s/analytics/sites/(?P<site_id>\d+)/visitors$' % settings.API_PREFIX,
        views.ActiveVisitorsView.as_view(), name='active_visitors'),
]
