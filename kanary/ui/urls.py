from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from etc.config import settings as application_settings
from etc.constants import AUDIT_PATH
from ui.account import api as account_api
from ui.campaign import api as campaign_api
from ui.targeting import api as targeting_api
from ui.notification import api as notification_api
from ui.storage import api as storage_api
from ui.publishers import api as publisherset_api
from ui.mail import views as mail

admin.autodiscover()
admin_urls = mail.get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls

admin.site.index_template = 'admin_custom/index.html'

urlpatterns = patterns(
    '',
    url(r'^$', 'ui.backend.views.main.main', name='main'),
    url(r'^payments/deposit$', 'ui.backend.views.main.deposit_funds', name='deposit_funds'),
    url(r'^payments/confirmation$', 'ui.backend.views.main.payment_confirmation', name='payment_confirmation'),
    url(r'^%s$' % AUDIT_PATH, 'ui.backend.views.audit.audit_notify', name='appnexus_audit_notify_uri'),
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt')),
    url(r'^status$', 'ui.backend.views.main.status', name='status'),
    url(r'^static/$', 'django_js_reverse.views.urls_js', name='static_url'),
    url(r'^jsreverse/$', 'django_js_reverse.views.urls_js', name='js_reverse'),
    (r'^admin/', include(admin.site.urls)),
)

# AUTH

urlpatterns += patterns(
    '',
    url(r'^accounts/login/$', 'ui.backend.views.auth.login', name='auth-login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='auth-logout'),

    url(r'^accounts/reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'ui.backend.views.auth.reset_password_confirm', name='reset_password_confirm'),
    url(r'^accounts/reset_password/$', 'ui.backend.views.auth.reset_password', name='reset_password'),
    url(r'^accounts/reset_password/send/$', 'ui.backend.views.auth.reset_password_send', name='reset_password_send'),

    url(r'^accounts/create_profile/$', 'ui.backend.views.signup.create_profile', name='create_profile'),
    url(r'^accounts/charge_account/$', 'ui.backend.views.signup.charge_account', name='charge_account'),
    url(r'^accounts/processing_payment/$', 'ui.backend.views.signup.processing_payment', name='processing_payment'),
    url(r'^accounts/setup_complete/$', 'ui.backend.views.signup.setup_complete', name='setup_complete'),

    url(r'^accounts/fetch_states/$', 'ui.backend.views.signup.fetch_states', name='fetch_states'),
)

# SIGNUP

if application_settings.ui_enable_signup:
    urlpatterns += patterns(
        '',
        url(r'^accounts/signup/$', 'ui.backend.views.signup.signup', name='signup'),
    )

# LOG IN AS OTHER USER

urlpatterns += patterns(
    'loginas.views',
    url(r'^login/user/(?P<user_id>.+)/$', 'user_login', name='loginas-user-login'),
)

# USER

urlpatterns += patterns(
    '',
    url(r'^user/change_password/$', 'ui.account.views.change_password', name='change_password'),
    url(r'^user/update_counter/$', 'ui.account.views.update_counter', name='update_counter'),
    url(r'^user/billing_info/$', 'ui.account.views.billing_info', name='billing_info'),
    url(r'^user/download/invoice/(?P<id>\d+)/$', 'ui.account.views.download_invoice', name='download_invoice'),
)

# CAMPAIGN/STRATEGY
urlpatterns += patterns(
    'ui.campaign.views',
    url(r'^strategy/(?P<id>\d+)/toggle_active/$', 'strategy_toggle_active', name='strategy_toggle_active')
)

# REPORTS - OVERVIEW AND CHARTS
urlpatterns += patterns(
    'ui.report.views',
    url(r'^report_campaign_overview/(?P<campaign_slug>[-\w]+)/$', 'campaign_overview_report', name='report_campaign_overview'),
    url(r'^report_strategy_overview/(?P<strategy_slug>[-\w]+)/$', 'strategy_overview_report', name='report_strategy_overview'),
    url(r'^report_chart/(?P<model_name>[-\w]+)/(?P<slug>[-\w]+)/$', 'overview_chart', name='report_chart'),
    url(r'^report_blacklist/(?P<strategy_slug>[-\w]+)/$', 'whitelist_blacklist', {'action': 'blacklist'}, name='report_blacklist'),
    url(r'^report_whitelist/(?P<strategy_slug>[-\w]+)/$', 'whitelist_blacklist', {'action': 'whitelist'}, name='report_whitelist'),
)

# LIVE VIEW
urlpatterns += patterns(
    'ui.liveview.views',
    url(r'^liveview/(?P<model_name>[-\w]+)/$', 'liveview', name='liveview'),
)

# STORAGE

urlpatterns += patterns(
    'ui.storage.views',
    url(r'^storage/creatives/add-image/$', 'upload_creative_image', name='storage_creatives_add_image'),
)

# API
API_PREFIX = 'api/'

api_resources = {
    '': (
        campaign_api.CampaignResource(),
        campaign_api.StrategyResource(),
        campaign_api.PeriodResource(),
        campaign_api.AdvertResource(),
        campaign_api.SiteResource(),
    ),
    'targeting/': (
        targeting_api.DeviceOSResource(),
        targeting_api.DeviceModelResource(),
        targeting_api.LocationResource(),
        targeting_api.AgeGroupResource(),
        targeting_api.GenderResource(),
        targeting_api.ContentCategoryTreeResource(),
        targeting_api.CarrierResource(),
        targeting_api.PublishersResource(),
        targeting_api.PublisherAdPositionsResource(),
        targeting_api.PublishersInventoryTypeResource(),
        targeting_api.NetworkResource(),
        targeting_api.SegmentProximicMaturityRatingResource(),
        targeting_api.SegmentProximicSafetyLevelResource(),
        targeting_api.SegmentProximicLanguageResource(),
        targeting_api.SegmentProximicPageQualityResource(),
        targeting_api.SegmentProximicPageNoticeabilityResource(),
        targeting_api.SegmentProximicPagePlacementResource(),
        targeting_api.SegmentProximicContextualResource(),
        targeting_api.SegmentPeerContextualSegmentResource(),
        targeting_api.SegmentPeerPageQualityResource(),
        targeting_api.PeerLanguageResource(),
        targeting_api.PeerBrandProtection(),
        targeting_api.LotameDemographicResource(),
        targeting_api.LotameAdvancedDemographicResource(),
        targeting_api.LotameBehavioralInterestResource(),
        targeting_api.LotameInfluencersResource(),
        targeting_api.LotameOfflineResource(),
    ),
    'notification/': (
        notification_api.EventResource(),
        notification_api.EventCategoryResource(),
    ),
    'account/': (
        account_api.UserResource(),
    ),
    'storage/': (
        storage_api.CreativeResource(),
        storage_api.AudienceResource(),
        storage_api.BrandResource()
    ),
    'publishers/': (
        publisherset_api.PublisherSetResource(),
    )
}

# used for notifications (dashboard events))
api_objects = {
    campaign_api.StrategyResource: 'strategies',
    campaign_api.CampaignResource: 'campaigns',
}

for api_group, resources in api_resources.iteritems():
    api_path = '^%s%s' % (API_PREFIX, api_group)
    api_urls = [(api_path, include(r.urls)) for r in resources]
    urlpatterns += patterns('', *api_urls)

if settings.SERVE_STATIC:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
    urlpatterns += staticfiles_urlpatterns()

# Fake pattern for static files - used only in error pages as reverse pattern
# Lambda passed as view should be never executed
urlpatterns += patterns(
    '',
    url(r'^{0}assets/error/(?P<path>.*)$'.format(settings.STATIC_URL[1:]), lambda *args, **kwargs: None, name='error_page_static'),
)

JS_URLS_MATCH = (
    r'storage_.*', r'api*', r'^report_data.*$',
)
