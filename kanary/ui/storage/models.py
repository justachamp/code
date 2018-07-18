import os
import mimetypes
from datetime import date
from urlparse import urljoin

import magic
from PIL import Image
import hexagonit.swfheader

from jsonfield import JSONField
from django.conf import settings
from django.db import transaction
from django.db.models import (
    Model, F, Q, ForeignKey,
    BooleanField, IntegerField, CharField, TextField, DateTimeField, ImageField, FileField
)
from django_extensions.db.models import TimeStampedModel
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save, post_save
from django.db.models.loading import get_model
from polymorphic import PolymorphicModel

from etc.constants import AUDIT_FEE, CDN_RESOURCE_KEY_MASK
from etc.config import settings as project_settings
from adserving.adserver.utils import appnexus_vast_url

from ui.storage.states import CreativeState, LiverailStatus, LIVERAIL_STATUS_CHOICES
from ui.storage.managers import CreativeManager, NotRemovableCreativeManager
from ui.account.models import Account
from ui.storage import s3

from apis import liverail
from apis.liverail import LiveRailAPI

from ui.bidding_spendings.models import DailySpendings
from ui.common.models import RandomId, NotRemovable, KanaryDirtyFieldsMixin
from ui.cache.base_models import CacheMapped
from ui.notification.models import Event
from ui.mail import mailing
from ui.fields import CharField255, BudgetDecimalField, LongURLField
from adserving.bidder.appnexus_api import api as appnexus_api, AppCreativeTemplate


class Audience(KanaryDirtyFieldsMixin, RandomId, NotRemovable):

    name = CharField255()
    owner = ForeignKey(Account)
    is_ip = BooleanField(default=False)

    class Meta:
        ordering = ['name']

    @property
    def adverts(self):
        from ui.campaign.models import Advert
        return Advert.objects.filter(
            Q(strategy__audiences=self) | Q(strategy__audiences_exclude=self)
        )

    def __unicode__(self):
        return u'{self.name} (from {self.owner})'.format(self=self)


# mappings for brand access status
ACCESS_STATUS_CHOICES = (
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('rejected', 'rejected'),
)
ACCESS_STATUS = dict((v, k) for k, v in ACCESS_STATUS_CHOICES)
ACCESS_STATUS_DEFAULT = 'pending'


class Brand(NotRemovable):
    """
    Brand for Facebook newsfeed creatives.
    """
    brand_id = IntegerField()
    thirdparty_page_id = CharField(max_length=32)
    page_name = CharField(max_length=50)
    appnexus_access_status = CharField(max_length=20, default=ACCESS_STATUS_DEFAULT, choices=ACCESS_STATUS_CHOICES)
    check_access_status = BooleanField(default=False)

    owner = ForeignKey(Account)

    def __unicode__(self):
        return u'Page id: {self.thirdparty_page_id} (from {self.owner})'.format(self=self)

    def update_access_status(self):
        """
        Update appnexus_access_status from AppNexus.

        Send request to gain access to a Facebook brand page,
        if ``check_access_status`` is ``True``,
        after sent through API set ``check_access_status`` flag to ``False``.

        :returns: error dict if error happened
        :rtype: dict
        """
        if self.is_deleted or self.appnexus_access_status == ACCESS_STATUS['rejected']:
            return {'error': 'Not confirmable'}

        if self.check_access_status:
            result = appnexus_api.request_brand_page_access(self.brand_id, self.thirdparty_page_id)

            if 'error' in result:
                return result

            access_status = result['access_status']
            self.check_access_status = False
        else:
            access_status = appnexus_api.update_brand_page_access(self.thirdparty_page_id)

        # Can be None from update_brand_page_access(...)
        if access_status:
            self.appnexus_access_status = access_status

        self.save()

        return dict()


# mapping from appnexus status
# for facebook statuses look
# https://wiki.appnexus.com/pages/viewpage.action?title=Facebook+Right-Hand+Side+for+Bidders&spaceKey=adnexusdocumentation
AUDIT_STATUS = (
    ('n', 'no_audit'),
    ('p', 'pending'),
    ('r', 'rejected'),
    ('u', 'unauditable'),
    ('a', 'audited'),
    ('e', 'expired'),
    ('fp', 'pending_pre_audit'),
    ('fr', 'rejected_by_pre_audit'),
    ('fa', 'approved'),
)
STATUS = dict((v, k) for k, v in AUDIT_STATUS)
NON_AUDITABLE_STATUSES = (STATUS['pending'], STATUS['audited'], STATUS['unauditable'])
APPNEXUS_API_CHANGED_STATUSES = (STATUS['pending'], STATUS['audited'])
"""
These statuses are might change through appnexus.
"""
AUDIT_DEFAULT = 'n'

# mappings for creative destination. (AppNexus, Facebook)
DESTINATION_TUPLE = (
    ('d', 'default'),
    ('fs', 'facebook_sidebar'),
    ('fn', 'facebook_newsfeed'),
)
DESTINATION = dict((v, k) for k, v in DESTINATION_TUPLE)
DESTINATION_DEFAULT = 'd'


class AppNexusCreative(KanaryDirtyFieldsMixin, Model):

    # appnexus creative_id:
    appnexus_id = IntegerField(null=True, unique=True)
    # appnexus audit_feedback creative field - verbosive response from appnexus auditors or facebook
    appnexus_feedback = TextField(null=True)
    # appnexus estimated audit completion time
    appnexus_sla_eta = DateTimeField(null=True)
    appnexus_status = CharField(max_length=2, default=AUDIT_DEFAULT, choices=AUDIT_STATUS)
    landing_site_url = LongURLField(null=True)

    # No funds for audit notification sent
    appnexus_audit_blocked_no_funds = BooleanField(default=False)

    # Default or Facebook.
    destination = CharField(max_length=2, default=DESTINATION_DEFAULT, choices=DESTINATION_TUPLE)

    class Meta:
        abstract = True

    @property
    def size(self):
        ''' Should return tuple (width, height) '''
        raise NotImplementedError

    @property
    def appnexus_media_url(self):
        url = urljoin(project_settings.globals_media_cdn_url, CDN_RESOURCE_KEY_MASK)
        return url % {'cid': self.public_id}

    @property
    def appnexus_template_id(self):
        ''' Should return integer representing Appnexus creative template. '''
        raise NotImplementedError

    @property
    def is_auditable(self):
        """
        :returns: True if creative can be audited.
        :rtype: bool
        """
        if self.is_facebook_destination():
            return bool(self.landing_site_url)
        else:
            return self.appnexus_status not in NON_AUDITABLE_STATUSES and bool(self.landing_site_url)

    def has_money(self, audit_fee):
        ''' Should return True whether there are money for audit'''
        raise NotImplementedError

    def is_facebook_destination(self, verify_is_newsfeed=False):
        """ Check is creative have facebook destination or not.

        :param verify_is_newsfeed: if True - check is it facebook newsfeed creative or not.
        :rtype: bool
        """
        result = False
        facebook_destinations = (
            DESTINATION['facebook_sidebar'],
            DESTINATION['facebook_newsfeed']
        )
        result = self.destination in facebook_destinations

        if result and verify_is_newsfeed:
            result = self.destination == DESTINATION['facebook_newsfeed']

        return result

    @property
    def data_for_facebook_audit(self):
        """ Should return data for facebook audit. """
        return {}

    def send_for_audit(self, force=False):
        """
        Sends creative for AppNexus audit if it's not yet audited.
        After send through API set ``to_audit`` flag to ``False``.

        :param bool force: if set to True creative is sent for audit despite
            of its status or account balance
        :returns: True if creative was sent for audit to AppNexus server
        :rtype: bool
        """
        if not self.landing_site_url:
            raise ValueError('Creative cannot be sent for audit if it has not landing site specified.')

        if self.is_deleted:
            return False

        if self.has_money(AUDIT_FEE):
            self.notify_about_audit_blocked()
            return False

        if not force:
            self.appnexus_update_status()

        self.appnexus_id = appnexus_api.audit_creative(
            self.appnexus_id, self.public_id, self.width, self.height,
            self.appnexus_template_id, self.appnexus_media_url,
            # We don't support HTTPS in case of video creatives for appnexus.
            self.type != 'Video',
            self.data_for_facebook_audit
        )

        self.to_audit = False
        self.appnexus_audit_blocked_no_funds = False
        self.save(update_fields=['to_audit', 'appnexus_audit_blocked_no_funds', 'appnexus_id'])

        self.appnexus_update_status()
        return True

    def notify_about_audit_blocked(self):
        '''
        Send a notification about audit blocked by lack of funds, if it hasn't been sent earlier.
        '''
        if self.appnexus_audit_blocked_no_funds:
            return

        Event.objects.create_not_enough_budget_for_audit(self)
        self.appnexus_audit_blocked_no_funds = True
        self.save(update_fields=['appnexus_audit_blocked_no_funds'])

    def disable_audit(self):
        '''
        Disables AppNexus audit of this creative.
        '''
        if not self.appnexus_id:
            return

        appnexus_api.disable_creative_audit(self.appnexus_id)

    def appnexus_creative(self):
        '''
        Returns creative state by using AppNexus API
        Returns:
            creative(dict) - state of AppNexus creative
        '''
        if not self.appnexus_id:
            return

        return appnexus_api.creative(self.appnexus_id)

    def appnexus_creative_test_url(self):
        '''
        Returns creative test URL by using AppNexus API
        Returns:
            url(str) - Appnexus test page with sent creative
        '''
        if not self.appnexus_id:
            return

        return appnexus_api.creative_test_url(self.appnexus_id)

    def appnexus_update_status(self):
        """
        Receives via API current state of creative and updates fields in model
        Returns:
            creative(dict) - state of AppNexus creative
        """
        creative = self.appnexus_creative()
        if not creative:
            return None

        audit_prefix = ''
        if self.is_facebook_destination():
            audit_prefix = 'facebook_'

        if creative.get('is_expired'):
            # When a creative has not run and has not been modified for 45
            # consecutive days, then it will be automatically marked expired
            # ("is_expired": true) and will not serve on any inventory.
            #  -- https://wiki.appnexus.com/display/adnexusdocumentation/Creative+Service
            self.appnexus_status = STATUS['expired']
        else:
            self.appnexus_status = STATUS.get(creative[audit_prefix + 'audit_status'])

        # Appnexus put reject explanation in 'audit_feedback'
        if self.appnexus_status == STATUS['rejected_by_pre_audit']:
            audit_prefix = ''
        self.appnexus_feedback = creative[audit_prefix + 'audit_feedback']

        self.appnexus_sla_eta = creative.get('sla_eta')  # sla may be None

        self.update_status = True
        self.save(update_fields=['appnexus_status', 'appnexus_feedback',
                                 'appnexus_sla_eta'])
        return creative

    def appnexus_set_audited(self):
        '''
            Simply marks creative as audited by appnexus.

            .. warning::

                Use with caution!
        '''
        self.appnexus_status = 'a'

    @classmethod
    def appnexus_update_notify(cls, notify):
        '''
        Updates creative in database based on given appnexus notify request
        '''
        try:
            creative = cls.objects.get(appnexus_id=notify['creative_id'])
        except cls.DoesNotExist:
            return None

        creative.appnexus_update_status()
        return creative

    @classmethod
    def appnexus_update_status_all(cls):
        """
        Update statuses of all creatives that have 'appnexus_id' already set.

        .. note::

            Statuses, that might be changed: either pending or audited.

            Pending status might change to either audited or rejected,
            while audited status might change to expired.
        """
        for creative in cls.objects_visible.filter(
            appnexus_id__isnull=False, appnexus_status__in=APPNEXUS_API_CHANGED_STATUSES
        ):
            creative.appnexus_update_status()


class Creative(PolymorphicModel, TimeStampedModel, RandomId, AppNexusCreative, CacheMapped):

    """
    .. note::
        ``landing_site_url`` field is filled once Creative gets connected to
        Advert object for the first time. ``post_save`` signal checks if
        creative connected has this field filled, and if not, it simply
        copies url from ``Campaign.landing_site`` and stores here.

        See :func:`~ui.campaign.models.advert_post_save` to get the whole idea
    """
    owner = ForeignKey(Account)
    name = CharField(max_length=255, db_index=True)
    width = IntegerField(null=True)
    height = IntegerField(null=True)
    to_audit = BooleanField(default=False)
    audit_fees = BudgetDecimalField(default=0)
    """
    Will provide easier debug information on how many times we audited.

    .. note:

        Account model has it's own audit_fees field that should be updated along this one,
        And there's also a DailySpending model, that present same information per day,
        that also should be updated along.
    """

    objects = CreativeManager()
    objects_visible = NotRemovableCreativeManager()

    class Meta:
        ordering = ['name']

    def __init__(self, *args, **kwargs):
        super(Creative, self).__init__(*args, **kwargs)
        self.state = CreativeState(self)

    @property
    def landing_sites_ratios(self):
        '''
            Return one element list of landing_sites URLs.
            This property is used for getting audits from AppNexus.
        '''
        if not self.landing_site_url:
            return []
        return [(str(self.landing_site_url), 1)]

    @property
    def public_id(self):
        return str(self.id_random)

    @property
    def size(self):
        return self.width, self.height

    @property
    def api_data(self):
        '''
        Property to read and return creative type specific data
        '''
        return None

    @property
    def type(self):
        '''
        Reads creative type based on classname. By default it's extracted from
        Creative type name. Hence CreativeImage becomes Image, and so on.
        '''
        return self.__class__.__name__.split('Creative')[1]

    @property
    def mimetype(self):
        return mimetypes.guess_type(self.file_path_abs)[0]

    @property
    def contents(self):
        return self.file_path_abs.open().read()

    def has_money(self, audit_fee):
        return self.owner.account_balance() < audit_fee

    def is_attached_to_any_strategy(self):
        ''' Returns True if this creative is attached into any non-deleted strategy '''
        return self.advert_set.filter(is_deleted=False,
                                      strategy__is_deleted=False,
                                      strategy__campaign__is_deleted=False).exists()

    def strategies(self):
        '''
        :returns: strategies that this creative is attached to
        '''
        # circular dependency:
        from ui.campaign.models import Strategy
        return Strategy.objects_visible.filter(advert__creative=self,
                                               advert__is_deleted=False,
                                               campaign__is_deleted=False).distinct()

    def upload_to_cdn(self, contents):
        """
        Method is responsible for uploading creative to CDN service.
        Our default CDN is s3.

        :param bytes contents: contents of data stored in creative. We must pass it
        via params because file isn't available at celery worker machine.
        """

        s3.upload_file_to_cdn(contents, self.mimetype, self.public_id)
        self.force_audit = True
        self.save()

    def upload_to_cdn_async(self):
        """
        Open file and get content/content type. Then close the file
        and send these information to celery task.
        """

        from ui.storage.tasks import upload_file_to_cdn
        Creative.objects.filter(pk=self.pk).update(to_audit=False)
        return upload_file_to_cdn.delay(self.pk, self.contents)

    def disable_audit_async(self):
        from ui.storage.tasks import disable_creative_audit
        disable_creative_audit.delay(self.pk)

    def send_for_audit(self, force=False):
        """
        Sends creative for AppNexus audit if it's not yet audited.
        After send through API set ``to_audit`` flag to ``False``.

        :param bool force: if set to True creative is sent for audit despite
            of its status
        :returns: True if creative was sent for audit to AppNexus server
        :rtype: bool
        """
        is_sent = super(Creative, self).send_for_audit(force)
        if is_sent:
            self.update_audit_fees()
        return is_sent

    @transaction.atomic
    def update_audit_fees(self):
        """
        Update audit fees in creative and releted objects.
        """
        audit_fees = 'audit_fees'

        self.audit_fees = F(audit_fees) + AUDIT_FEE
        self.owner.audit_fees = F(audit_fees) + AUDIT_FEE
        daily_spendings, _ = DailySpendings.objects.get_or_create(
            date=date.today(), account_id=self.owner.id)
        daily_spendings.audit_fees = F(audit_fees) + AUDIT_FEE

        self.save(update_fields=[audit_fees])
        self.owner.save(update_fields=[audit_fees])
        daily_spendings.save(update_fields=[audit_fees])

    def __unicode__(self):
        return u'{self.name} [{self.width}x{self.height}]'.format(self=self)


def creative_factory(creative_type, *args, **kwargs):
    '''
        Creates specific Creative subclass object based on type argument
    '''
    if not creative_type:
        raise ValidationError('You cannot create creative without a type.')
    creative_class = get_model('storage', 'Creative' + creative_type)
    return creative_class(*args, **kwargs)


class CreativeImage(Creative):

    '''
        Creative image data model.
        Extends basic model with image field to store images
    '''
    image = ImageField(upload_to='creatives')

    # Fields for Facebook creatives
    title = CharField(null=True, default=None, max_length=255)
    body = CharField(null=True, default=None, max_length=255)
    message = CharField(null=True, default=None, max_length=500)
    domain = CharField(null=True, default=None, max_length=90)
    brand = ForeignKey(Brand, null=True, default=None)

    @property
    def appnexus_template_id(self):
        template_dict = {
            DESTINATION['default']:           AppCreativeTemplate.image,
            DESTINATION['facebook_sidebar']:  AppCreativeTemplate.fb_sidebar_image,
            DESTINATION['facebook_newsfeed']: AppCreativeTemplate.fb_newsfeed_image
        }
        return template_dict[self.destination]

    @property
    def file_path_abs(self):
        return settings.MEDIA_ROOT / self.image.name

    @property
    def api_data(self):
        if self.image:
            return self.image.url
        return ''

    @api_data.setter
    def api_data(self, imagename):

        image = ''
        if imagename:
            image = imagename.replace(settings.MEDIA_URL, '')

        if image == self.image:
            return

        file_path_abs = os.path.join(settings.MEDIA_ROOT, image)
        try:
            width, height = Image.open(file_path_abs).size
        except IOError:
            # this gets caught by tastypie
            # and returned as if it has been through validation
            raise ValidationError('Not an image file!')

        self.width = width
        self.height = height

        self.image = image

    @property
    def data_for_facebook_audit(self):
        data = {}

        if self.is_facebook_destination():
            data.update({
                'landing_page':       self.landing_site_url,
                'title':              self.title,
                'body':               self.body,
            })

        if self.is_facebook_destination(verify_is_newsfeed=True):
            data.update({
                'message':            self.message,
                'domain':             self.domain,
                'brand_id':           self.brand.brand_id,
                'thirdparty_page_id': self.brand.thirdparty_page_id,
            })

        return data


class CreativeFlash(Creative):

    '''
        Creative flash data model.
        Extends basic model with file field to store flash files
    '''
    file = FileField(upload_to='creatives')

    @property
    def appnexus_template_id(self):
        return AppCreativeTemplate.flash

    @property
    def file_path_abs(self):
        return settings.MEDIA_ROOT / self.file.name

    @property
    def api_data(self):
        if not self.file:
            return ''
        return self.file.url

    @api_data.setter
    def api_data(self, filename):

        flash_file = ''
        if filename:
            flash_file = filename.replace(settings.MEDIA_URL, '')

        if flash_file == self.file:
            return

        file_path_abs = os.path.join(settings.MEDIA_ROOT, flash_file)
        try:
            metadata = hexagonit.swfheader.parse(file_path_abs)
        except ValueError:
            # this gets caught by tastypie
            # and returned as if it has been through validation
            raise ValidationError('Not a Flash file!')

        self.width = metadata['width']
        self.height = metadata['height']

        self.file = flash_file


class CreativeVideo(Creative):

    '''
        Creative video data model.
        Extends basic model with field to store video files (uploaded to
        LiveRail).
    '''

    file = FileField(upload_to='creatives')

    allowed_extensions = ('api')

    # Fields connected to LiveRail integration.
    liverail_id = IntegerField(max_length=20, null=True, db_index=True)
    liverail_status = CharField(max_length=20, choices=LIVERAIL_STATUS_CHOICES,
                                default=LiverailStatus.pending, db_index=True)
    liverail_error = TextField(blank=True, default='')
    media_variants = JSONField(blank=True)

    # Duration of content, stored in seconds.
    duration = IntegerField(null=True, default=0)

    @property
    def media_variants_secure(self):
        """Provide a list of media_variants that can be served over https."""
        secure_variants = []
        for media in self.media_variants:
            secure_media = media.copy()
            secure_media['url'] = secure_media['url'].replace(
                LiveRailAPI.LIVERAIL_CDN, LiveRailAPI.LIVERAIL_CDN_SECURE
            )
            secure_variants.append(secure_media)
        return secure_variants

    @property
    def file_path_abs(self):
        return settings.MEDIA_ROOT / self.file.name

    @property
    def is_auditable(self):
        is_auditable = super(CreativeVideo, self).is_auditable
        return is_auditable and self.liverail_status == LiverailStatus.active

    @property
    def appnexus_media_url(self):
        return appnexus_vast_url(
            self.public_id,
            # is_secure set to False will create a vast url with http:// scheme, which is required by appnexus.
            is_secure=False
        )

    @property
    def vast_url(self):
        """
        Return vast url without any url schema.

        :returns: schema-less url to vast
        :rtype: str
        """
        return appnexus_vast_url(
            self.public_id,
            # is_secure None will render url without any scheme, leaving it out to browser.
            is_secure=None,
        )

    @property
    def appnexus_template_id(self):
        if self.duration == 15:
            return AppCreativeTemplate.video_vast_15s
        if self.duration == 30:
            return AppCreativeTemplate.video_vast_30s
        return AppCreativeTemplate.video_vast_other

    @property
    def api_data(self):
        if self.file:
            return self.file.url

    @api_data.setter
    def api_data(self, videoname):
        video = ''

        if videoname:
            video = videoname.replace(settings.MEDIA_URL, '')

        if video == self.file:
            return

        file_path_abs = settings.MEDIA_ROOT / video

        if not magic.from_file(file_path_abs, mime=True).startswith('video'):
            raise ValidationError("Uploaded video file isn't recognizable "
                                  "as a video filetype.")

        self.file = video

    def upload_to_cdn(self, contents):
        """
        Upload file to liverail cdn.

        :param str contents: read video file content.
        """
        with liverail.liverail_connection() as api:
            if not self.liverail_id:
                self.liverail_id = api.add_creative(self.pk, self.name)

            api.upload_video_asset(self.liverail_id, contents)
            self.liverail_status = LiverailStatus.uploaded
            self.save()

    def liverail_update_media(self, liverail_conn):
        """
        Update creative's LiveRail status.

        If the real updated status is 'active', save updated media types
        and set duration, width and height to their maximum of returned videos.

        :param apis.liverail.LiveRailAPI liverail_conn: LiveRail API wrapper in connected state
        """
        try:
            creative_status = liverail_conn.creative_status(self.liverail_id)
            if creative_status != liverail_conn.CreativeStatus.active:
                return
            video_assets = liverail_conn.list_video_assets(self.liverail_id)
        except liverail.LiveRailApiResponseError as e:
            self.liverail_error = str(e)
            self.liverail_status = LiverailStatus.error
            self.save(update_fields=['liverail_error', 'liverail_status'])
            return

        # Update the creative:
        self.liverail_status = LiverailStatus.active
        self.media_variants = video_assets
        self.width = max(v['width'] for v in video_assets)
        self.height = max(v['height'] for v in video_assets)
        # Duration should be constant but who knows (different encodings, different framerates, rounding...).
        self.duration = max(v['duration'] for v in video_assets)
        self.save(update_fields=['width', 'height', 'duration', 'liverail_status', 'media_variants'])

    @classmethod
    def liverail_update_media_all(cls):
        """
        Update media files list of all not active creatives with liverail_id.
        """
        with liverail.liverail_connection() as api:
            for creative in cls.objects_visible.filter(liverail_id__isnull=False).exclude(
                    liverail_status=LiverailStatus.active):
                creative.liverail_update_media(liverail_conn=api)

    def upload_to_cdn_async(self):
        """
        Overrides base method. Sets liverail_status to pending when creative
        is being uploaded to service.
        """
        # We can't execute save, because this method is called during
        # post_save signal, so we use update to avoid triggering signals at all.
        CreativeVideo.objects.filter(pk=self.pk).update(liverail_status=LiverailStatus.pending)

        return super(CreativeVideo, self).upload_to_cdn_async()


def update_facebook_sizes(creative):
    """ Hook to set standart sizes for facebook creatives. """
    if creative.destination == DESTINATION['facebook_sidebar']:
        creative.width = 254
        creative.height = 133

    elif creative.destination == DESTINATION['facebook_newsfeed']:
        if creative.width == creative.height:
            creative.width = 200
            creative.height = 200
        else:
            creative.width = 470
            creative.height = 246


def creative_pre_save(sender, instance, **kwargs):
    creative = instance
    if creative.is_facebook_destination():
        update_facebook_sizes(creative)

    creative.is_content_changed = True
    if not creative.pk:
        return

    previous_creative = Creative.objects.get(pk=creative.pk)
    previous_data = previous_creative.api_data
    if previous_data == creative.api_data:
        creative.is_content_changed = False

    # pre delete
    if creative.is_deleted and previous_creative.is_deleted is False:
        creative.disable_audit_async()


def is_creative_fields_changed(creative):
    """ Return true if some of specified fields of creative was changed. """
    fields_to_check = [
        'landing_site_url'
    ]

    if creative.is_facebook_destination():
        fields_to_check.extend([
            'title',
            'body'
        ])
        if creative.is_facebook_destination(verify_is_newsfeed=True):
            fields_to_check.extend([
                'message',
                'domain',
                'brand_id'
            ])

    result = False
    for field in fields_to_check:
        result = result or creative.has_changed(field, True)

    return result


def creative_post_save(sender, instance, **kwargs):
    """
    .. note::
        We add ``is_content_changed`` attribute in ``pre_save``.

        We could not change the object in ``post_save``, so we use
        ``update`` method to update ``to_audit`` field.
    """
    creative = instance

    # status change
    if creative.has_changed('appnexus_status', True):
        if creative.appnexus_status == STATUS['pending']:
            Event.objects.create_creative_pending(creative)
        elif creative.appnexus_status in (STATUS['rejected'], STATUS['unauditable']):
            Event.objects.create_creative_rejected(creative)
            mailing.creative_rejected(creative).send()
        elif creative.appnexus_status == STATUS['audited']:
            Event.objects.create_creative_audited(creative)
        elif creative.appnexus_status == STATUS['expired']:
            Event.objects.create_creative_expired(creative)

    # Hack: update_status is a fake-field added on the fly
    if creative.is_deleted or hasattr(creative, 'update_status'):
        return

    if creative.is_content_changed:
        creative.upload_to_cdn_async()
        return

    # Hack: force_audit is also a fake field added on the fly
    needs_audit = creative.is_content_changed or\
        ((is_creative_fields_changed(creative) and creative.is_auditable)) or\
        creative.has_changed('destination', True) or getattr(creative, 'force_audit', False)

    if creative.is_attached_to_any_strategy() and needs_audit:
        # Used update() instead of .save() in order to disable post_save signal
        Creative.objects.filter(pk=creative.pk).update(to_audit=True)
        Creative.objects.filter(pk=creative.pk).update(appnexus_status=AUDIT_DEFAULT)
        creative.to_audit = True
        creative.appnexus_status = AUDIT_DEFAULT


def video_creative_liverail_status(sender, instance, **kwargs):
    """
    Checks if video creative has changed status and is ready to audit.
    """
    creative = instance
    needs_audit = creative.has_changed('liverail_status', True) and creative.is_auditable
    if creative.is_attached_to_any_strategy() and needs_audit:
        Creative.objects.filter(pk=creative.pk).update(to_audit=True)
        creative.to_audit = True


def video_creative_emit_notifications(sender, instance, **kwargs):
    """Emit events specific to video creatives."""
    creative = instance
    if creative.has_changed('liverail_status', True):
        if creative.liverail_status == LiverailStatus.active:
            Event.objects.create_video_encoded(creative)
        elif creative.liverail_status == LiverailStatus.error:
            Event.objects.create_video_encoding_failed(creative)


pre_save.connect(creative_pre_save, sender=CreativeImage)
pre_save.connect(creative_pre_save, sender=CreativeFlash)
pre_save.connect(creative_pre_save, sender=CreativeVideo)
post_save.connect(creative_post_save, sender=CreativeImage)
post_save.connect(creative_post_save, sender=CreativeFlash)
post_save.connect(creative_post_save, sender=CreativeVideo)
post_save.connect(video_creative_liverail_status, sender=CreativeVideo)
post_save.connect(video_creative_emit_notifications, sender=CreativeVideo)
