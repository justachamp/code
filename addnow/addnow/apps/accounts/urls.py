from django.conf.urls import url
from django.conf import settings

from addnow.apps.accounts import views


urlpatterns = [
    url(r'^%s/tokens$' % settings.API_PREFIX, views.ObtainJSONWebToken.as_view(), name='accounts_token'),

    url(r'^%s/users/reset_password$' % settings.API_PREFIX, views.PasswordResetAttemptView.as_view(),
        name='accounts_password_reset_attempt'),
    url(r'^%s/users/change_password$' % settings.API_PREFIX,
        views.PasswordResetConfirmView.as_view(), name='accounts_password_reset_confirm'),
    url(r'^%s/account' % settings.API_PREFIX, views.AccountView.as_view(),
        name='accounts_account'),

    url(r'^%s/users$' % settings.API_PREFIX,
        views.RegisterUserView.as_view(), name='accounts_create_user'),
    url(r'^%s/users/verify$' % settings.API_PREFIX,
        views.VerifyUserView.as_view(), name='accounts_verify_user'),
    url(r'^%s/users/verify/(?P<key>.+)$' % settings.API_PREFIX,
        views.EmailVerificationView.as_view(), name='accounts_email_verification'),

    url(r'^%s/sites$' % settings.API_PREFIX, views.SiteListCreateView.as_view(), name='accounts_sites'),
    url(r'^%s/sites/(?P<pk>\d+)$' % settings.API_PREFIX,
        views.SiteRetrieveUpdateView.as_view(), name='accounts_site_detail'),

    url(r'^%s/sites/(?P<site_pk>\d+)/widgets$' % settings.API_PREFIX, views.WidgetListCreateView.as_view(),
        name='accounts_widgets'),
    url(r'^%s/sites/(?P<site_pk>\d+)/widgets/(?P<widget_pk>\d+)$' % settings.API_PREFIX,
        views.WidgetRetrieveUpdateView.as_view(), name='accounts_widget_detail'),
]
