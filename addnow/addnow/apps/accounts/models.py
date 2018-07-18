from django.core import signing, urlresolvers
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from django.utils import timezone

from addnow.apps.accounts import constants
from addnow.apps.accounts.fields import BlankAsNullDomainNameField, BlankAsNullCharField, BlankAsNullURLField
from addnow.apps.accounts.signers import user_signer, password_signer
from addnow.apps.analytics.models import CredentialsModel
from addnow.apps.analytics.signals import analytics_revoke_access


class UserManager(BaseUserManager):
    def create(self, email, password, is_admin, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, is_admin=is_admin, is_active=True, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **kwargs):
        return self.create(email, password, False, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        return self.create(email, password, True, **kwargs)


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    email_is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, editable=False)
    is_reminders_muted = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    dsp_pixel_url = models.URLField('DSP pixel', max_length=1000, blank=True)
    offset = models.SmallIntegerField('timezone offset in minutes', default=0)
    has_analytics = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def has_sites(self):
        return self.site_set.count() > 0

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def generate_email_token(self):
        return signing.dumps({'uid': self.pk, 'token': user_signer.sign(self.email)})

    def validate_email_token(self, token):
        return user_signer.validate_token(self.email, token)

    def generate_password_reset_token(self):
        return password_signer.sign(self)

    def validate_password_reset_token(self, token):
        return password_signer.validate_token(self, token)


class Site(models.Model):
    user = models.ForeignKey(User)
    widget_configurations = models.ManyToManyField(
        'WidgetConfiguration', blank=True, related_name='sites', help_text='deprecated by ADDNOW-807')

    domain = BlankAsNullDomainNameField(max_length=255, unique=True)
    trim_api_key = BlankAsNullCharField(max_length=255, null=True, blank=True)

    # thank you popup fields
    thank_you_message = models.CharField(max_length=500, blank=True)
    thank_you_advert_image_url = models.CharField(max_length=255, blank=True)
    thank_you_advert_url = models.CharField(max_length=255, blank=True)
    thank_you_advert_title = models.CharField(max_length=150, blank=True)

    address_bar_sharing = models.BooleanField(default=False)
    copy_paste_sharing = models.BooleanField(default=False)
    has_short_urls = models.BooleanField(default=True)

    analytics_account = models.CharField(max_length=255, blank=True)
    analytics_property = models.CharField(max_length=255, blank=True)
    analytics_profile = models.CharField(max_length=255, blank=True)

    dmp_execute_code = models.BooleanField(default=False)
    vanity_domain = BlankAsNullDomainNameField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return '%s: %s' % (self.user, self.domain)

    @property
    def hash_id(self):
        """ The hash_id is the site_id's signature
            needed in tracker methods to accessing them from widgets.
            It increases the security level rather than using the raw id.
        """
        signer = signing.Signer()
        return signer.sign(self.pk)

    def get_config(self):
        from addnow.apps.accounts.serializers import AllWidgetsSerializer

        thank_you = {
            'services': {v['service']: v['url'] for v in self.social_urls.values('service', 'url')},
            'message': self.thank_you_message,
            'advertImageUrl': self.thank_you_advert_image_url,
            'advertUrl': self.thank_you_advert_url,
            'advertTitle': self.thank_you_advert_title
        }

        sharing = {
            'byHash': self.address_bar_sharing,
            'copyPaste': self.copy_paste_sharing,
            'hasShortUrls': self.has_short_urls
        }
        serializer = AllWidgetsSerializer(self.widgets.exclude(is_active=False), many=True)

        config = dict(
            offset=self.user.offset,  # TODO: Move to another method when tasks
                                      # will use it's own cache
            sharing=sharing,
            thank_you=thank_you,
            hash_id=self.hash_id,
            widget_configurations=serializer.data,
            dmp_execute_code=self.dmp_execute_code,
            vanity_domain=self.vanity_domain
        )
        return config

    @classmethod
    def get_id_by_hash(cls, site_id):
        """ This method is the reverse method of hash_id. the conversion to int()
        SHOULD BE REMOVED IN THE FUTURE which is for legacy purpose.
        """
        # TODO: The int() conversion should be in removed after the migration from old site-id usage is finished
        try:
            return str(int(site_id))
        except (ValueError, TypeError):
            signer = signing.Signer()
            return signer.unsign(site_id)


class WidgetConfiguration(models.Model):
    site = models.ForeignKey(Site, related_name='widgets')

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=constants.WIDGET_CONFIGURATION_TYPE_CHOICES)
    orientation = models.CharField(max_length=20, choices=constants.BUTTON_ORIENTATION_CHOICES, blank=True)
    button_size = models.CharField(max_length=20, choices=constants.BUTTON_SIZE_CHOICES, blank=True)
    button_style = models.CharField(max_length=20, choices=constants.BUTTON_STYLE_CHOICES, blank=True)
    counter_position = models.CharField(max_length=20, choices=constants.COUNTER_POSITION_CHOICES, blank=True)
    position = models.CharField(max_length=20, choices=constants.WIDGET_POSITIONS, blank=True)
    page_title = models.CharField(max_length=255, blank=True)
    page_url = models.URLField(max_length=255, blank=True)
    media_url = models.URLField(max_length=255, blank=True)
    min_width = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    vanity_domain = BlankAsNullDomainNameField(max_length=255, blank=True, null=True)
    has_link_share_button = models.BooleanField(default=False)
    extra_button_animation = models.BooleanField(default=False)

    class Meta:
        unique_together = ('site', 'name')

    def __unicode__(self):
        return self.name

    def changeform_link(self):
        if self.id:
            changeform_url = urlresolvers.reverse(
                'admin:accounts_widgetconfiguration_change', args=(self.id,)
            )
            return u'<a href="%s" target="_blank">Edit</a>' % changeform_url
        return u''
    changeform_link.allow_tags = True
    changeform_link.short_description = ''   # omit column header


class SharingButtonsWidgetManager(models.Manager):
    def get_queryset(self):
        return super(SharingButtonsWidgetManager, self).get_queryset().filter(
            type=constants.WIDGET_CONFIGURATION_SHARING_BUTTONS)


class SharingButtonsWidget(WidgetConfiguration):
    class Meta:
        proxy = True

    objects = SharingButtonsWidgetManager()


class OriginButtonsWidgetManager(models.Manager):
    def get_queryset(self):
        return super(OriginButtonsWidgetManager, self).get_queryset().filter(
            type=constants.WIDGET_CONFIGURATION_ORIGIN_BUTTONS)


class OriginButtonsWidget(WidgetConfiguration):
    class Meta:
        proxy = True

    objects = OriginButtonsWidgetManager()


class CopyPasteWidgetManager(models.Manager):
    def get_queryset(self):
        return super(CopyPasteWidgetManager, self).get_queryset().filter(
            type=constants.WIDGET_CONFIGURATION_COPY_PASTE)


class CopyPasteWidget(WidgetConfiguration):
    class Meta:
        proxy = True

    objects = CopyPasteWidgetManager()


class NewsletterWidgetManager(models.Manager):
    def get_queryset(self):
        return super(NewsletterWidgetManager, self).get_queryset().filter(
            type=constants.WIDGET_CONFIGURATION_NEWSLETTER)


class NewsletterWidget(WidgetConfiguration):
    class Meta:
        proxy = True

    objects = NewsletterWidgetManager()


class MobileWidgetManager(models.Manager):
    def get_queryset(self):
        return super(MobileWidgetManager, self).get_queryset().filter(
            type=constants.WIDGET_CONFIGURATION_MOBILE)


class MobileWidget(WidgetConfiguration):
    class Meta:
        proxy = True

    objects = MobileWidgetManager()


class CircularMobileWidgetManager(models.Manager):
    def get_query_set(self):
        return super(CircularMobileWidgetManager, self).get_queryset().filter(
            type=constants.WIDGET_CONFIGURATION_MOBILE)


class CircularMobileWidget(WidgetConfiguration):
    class Meta:
        proxy = True

    objects = CircularMobileWidgetManager()


class FollowWidgetManager(models.Manager):
    def get_queryset(self):
        return super(FollowWidgetManager, self).get_queryset().filter(
            type=constants.WIDGET_CONFIGURATION_FOLLOW)


class FollowWidget(WidgetConfiguration):
    class Meta:
        proxy = True

    objects = FollowWidgetManager()


class VerticalFloatWidgetManager(models.Manager):
    def get_queryset(self):
        return super(VerticalFloatWidgetManager, self).get_queryset().filter(
            type=constants.WIDGET_CONFIGURATION_VERTICAL_FLOAT)


class VerticalFloatWidget(WidgetConfiguration):
    class Meta:
        proxy = True

    objects = VerticalFloatWidgetManager()


class WidgetButton(models.Model):
    configuration = models.ForeignKey(WidgetConfiguration, related_name='buttons')
    service = models.CharField(max_length=20, choices=constants.BUTTONS_SOURCE_SET)
    order = models.PositiveSmallIntegerField()
    is_extra_button = models.BooleanField(default=False)
    follow_url = BlankAsNullURLField(max_length=255, null=True, blank=True)  # For usage only in FollowWidget

    class Meta:
        unique_together = ('configuration', 'service',)
        ordering = ('is_extra_button', 'order',)

    def __unicode__(self):
        if self.follow_url:
            return '%s : %s (%s)' % (self.configuration, self.service, self.follow_url)

        return '%s : %s' % (self.configuration, self.service)


class SocialUrl(models.Model):
    """
    Class to hold the site's urls in social services.
    """
    site = models.ForeignKey(Site, related_name='social_urls')
    service = models.CharField(max_length=20, choices=constants.SOCIAL_SERVICE_CHOICES)
    url = models.CharField(max_length=255)

    class Meta:
        unique_together = ('site', 'service',)
        ordering = ['pk']

    def __unicode__(self):
        return '%s - %s: %s' % (self.site, self.service, self.url)


class UniqueUser(models.Model):
    """
    Model containing uuid used by user.
    It's used to identify dark shares.
    """
    uuid = models.CharField(max_length=16, primary_key=True)
    # Time of creation. Theoretically entries in this table should never be
    # removed, but if it will be necessary - this field will help to set cutoff
    # point.
    created_at = models.DateTimeField()


@receiver(analytics_revoke_access, sender=CredentialsModel)
def analytics_revoke_handler(sender, **kwargs):
    user = kwargs.get('user')

    if user:
        Site.objects.filter(user=user).update(analytics_account='', analytics_property='', analytics_profile='')
        user.has_analytics = False
        user.save()


@receiver(post_save, sender=Site, dispatch_uid="reset_site_cache")
@receiver(post_delete, sender=Site, dispatch_uid="reset_site_cache")
def reset_cache(sender, instance, **kwargs):
    from addnow.cache import SiteSettingsCache, SiteTrimSettingsCache
    SiteSettingsCache.delete(dict(site_id=instance.pk))
    SiteTrimSettingsCache.delete(dict(site_id=instance.pk))
