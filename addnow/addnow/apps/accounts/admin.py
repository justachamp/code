from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User, Site, WidgetConfiguration, WidgetButton, SocialUrl


def reset_social_counters_cache(modeladmin, request, queryset):
    from addnow.cache import SocialCountersCache
    for site in queryset:
        SocialCountersCache.delete_pattern(dict(site_id=site.pk))
reset_social_counters_cache.short_description = "Reset Social counters cache"


def reset_settings_cache(modeladmin, request, queryset):
    from addnow.cache import SiteSettingsCache, SiteTrimSettingsCache
    for site in queryset:
        SiteSettingsCache.delete(dict(site_id=site.pk))
        SiteTrimSettingsCache.delete(dict(site_id=site.pk))
reset_settings_cache.short_description = "Reset Settings cache"


def reset_trim_fail_cache(modeladmin, request, queryset):
    from addnow.cache import TrimFailCache
    for site in queryset:
        TrimFailCache.delete(dict(site=site.pk))
reset_trim_fail_cache.short_description = "Reset Trim Fail cache"


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'email_is_verified', 'is_admin', 'date_joined', 'last_login')
    list_filter = ('is_admin', 'is_active')
    ordering = ['date_joined']
    search_fields = ('email',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_reminders_muted', 'email_is_verified')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Custom data'), {'fields': ('dsp_pixel_url', 'offset', 'has_analytics')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


class WidgetButtonInline(admin.TabularInline):
    model = WidgetButton
    suit_classes = 'suit-tab suit-tab-widget-buttons'
    extra = 0


@admin.register(WidgetConfiguration)
class WidgetConfigurationAdmin(admin.ModelAdmin):
    inlines = [WidgetButtonInline]

    list_filter = ['is_active', 'has_link_share_button', 'extra_button_animation', 'type']
    list_display = ['site', 'name', 'type', 'is_active']
    search_fields = ['site__domain', 'site__trim_api_key']

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'is_active', 'site', 'name', 'type', 'vanity_domain', 'has_link_share_button', 'extra_button_animation']
        }),
        ('Specific data', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'orientation', 'button_size', 'button_style', 'counter_position', 'position', 'page_title',
                'page_url', 'media_url', 'min_width']
        }),
        ('Buttons', {
            'classes': ('suit-tab', 'suit-tab-widget-buttons',),
            'fields': []
        })
    ]

    suit_form_tabs = (
        ('general', 'General'),
        ('widget-buttons', 'Buttons')
    )


class WidgetsInline(admin.TabularInline):
    model = WidgetConfiguration
    suit_classes = 'suit-tab suit-tab-widgets'
    extra = 0

    fields = (
        'name', 'type', 'has_link_share_button', 'extra_button_animation', 'vanity_domain', 'is_active',
        'changeform_link'
    )
    readonly_fields = (
        'name', 'type', 'has_link_share_button', 'extra_button_animation', 'vanity_domain', 'is_active',
        'changeform_link'
    )


class SocialUrlInline(admin.TabularInline):
    model = SocialUrl
    suit_classes = 'suit-tab suit-tab-follow'
    extra = 0

    verbose_name = 'Social network url'
    verbose_name_plural = 'Social network urls'


class SiteAdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            'thank_you_message': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'thank_you_advert_image_url': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'thank_you_advert_url': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'thank_you_advert_title': forms.TextInput(attrs={'class': 'input-xxlarge'}),
        }
        labels = {
            "thank_you_message": _("Message"),
            "thank_you_advert_image_url": _("Advert Image URL"),
            "thank_you_advert_url": _("Advert URL"),
            "thank_you_advert_title": _("Advert Title"),
        }


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):

    actions = [reset_social_counters_cache, reset_settings_cache, reset_trim_fail_cache]
    inlines = (WidgetsInline, SocialUrlInline)
    form = SiteAdminForm

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['user', 'domain', 'trim_api_key', 'address_bar_sharing', 'copy_paste_sharing', 'has_short_urls',
                       'vanity_domain', 'dmp_execute_code']
        }),
        ('Thank you popup', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['thank_you_message', 'thank_you_advert_image_url', 'thank_you_advert_url',
                       'thank_you_advert_title']
        }),
        ('Google analytics', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['analytics_account', 'analytics_property', 'analytics_profile']
        }),
        ('Widgets', {
            'classes': ('suit-tab', 'suit-tab-widgets',),
            'fields': []
        }),
        ('Follow details', {
            'classes': ('suit-tab', 'suit-tab-follow',),
            'fields': []
        })
    ]

    suit_form_tabs = (
        ('general', 'General'),
        ('widgets', 'Widgets'),
        ('follow', 'Follow details')
    )

    list_display = ('user', 'domain', 'get_widget_configurations')
    list_filter = ('widgets',)
    list_select_related = True

    search_fields = ['domain', 'user__email']

    def get_widget_configurations(self, obj):
        return ', '.join([config.name for config in obj.widgets.all()])
    get_widget_configurations.short_description = 'Widget configurations'
