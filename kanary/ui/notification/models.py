''' Mind that Events are strongy denormalized for performance purposes.
'''

from collections import OrderedDict

import simplejson
from django.db import models as m
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db.models import F
from django.db.models.signals import pre_save, post_save
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from ui.utils import is_timezoned
from ui.fields import CharField255
from ui.account.models import User


class EventCategory(m.Model):

    '''Every Event needs to be categoriezed'''

    name = CharField255(unique=True, db_index=True)

    def __unicode__(self):
        return self.name


class EventObjectManager(m.Manager):

    def __getattr__(self, attr):
        '''Allows to call Event.objects.create_event_name(*params)
        which sets 'message_type' and 'category' in background.
        '''

        try:
            _, name = attr.split('create_')
        except ValueError:
            raise AttributeError

        if name not in Event.Messages.types.keys():
            raise AttributeError('No event named %s' % name)

        return self.create_(name)

    def create_(self, event_name):
        '''Allows to call Event.objects.create_event_name(*params)
        Method defined as 'create_' for easier tab-completion in shell.
        '''
        message_type = Event.Messages.types.keys().index(event_name)
        cat_name = Event.Messages.types[event_name]
        category, _ = EventCategory.objects.get_or_create(name=cat_name)

        def create(*args, **kwargs):
            args, kwargs = getattr(Event, event_name)(*args, **kwargs)
            return self.create(message_type=message_type, category=category, *args, **kwargs)
        return create

    def filter_message(self, message):
        """
        Filter agaist textual representation of message that is hardcoded
        in the model.
        :param str message: one of Event.types keys
        :rtype: QuerySet
        :return: QuerySet with filter applied
        """
        message_type = Event.Messages.get_message_code(message)
        return self.filter(message_type=message_type)


class Event(m.Model):

    '''Event (notifications/timeline) class.
    Responsible for rendering different kinds of messages.
    obj_1, obj_2 can be used for rendering of message e.g.:
        "<%= obj_1 %>, <%= obj_2 %>, and more was removed because
         <%= user_1 % => removed <%= campagin_1 %>."
    '''

    message_type = m.IntegerField()

    account = m.ForeignKey('account.Account', db_index=True)
    user = m.ForeignKey('account.User', null=True)

    category = m.ForeignKey(EventCategory)
    datetime_UTC = m.DateTimeField(auto_now_add=True, db_index=True)

    object_id_1 = m.PositiveIntegerField(null=True, blank=True)
    content_type_1 = m.ForeignKey(ContentType, null=True, blank=True,
                                  related_name='ct1')
    obj_1 = generic.GenericForeignKey('content_type_1', 'object_id_1')

    object_id_2 = m.PositiveIntegerField(null=True, blank=True)
    content_type_2 = m.ForeignKey(ContentType, null=True, blank=True,
                                  related_name='ct2')
    obj_2 = generic.GenericForeignKey('content_type_2', 'object_id_2')

    class Messages:
        basic_information = 'Basic information'
        audit = 'Audit'
        types = OrderedDict([
            ('campaign_created', basic_information),
            ('strategy_created', basic_information),
            ('report_created', basic_information),
            ('creative_pending', audit),
            ('creative_audited', audit),
            ('creative_rejected', audit),
            ('not_enough_budget_for_audit', audit),
            ('creative_expired', basic_information),
            ('video_encoded', basic_information),
            ('video_encoding_failed', basic_information),
            # add new types only in the end of OrderedDict
        ])

        @classmethod
        def get_message_code(cls, message_name):
            """
            Return code of given message.
            :param str message: one of Event.types keys
            :rtype: int
            :return: message index
            """
            return cls.types.keys().index(message_name)

    class Meta:
        ordering = ['-datetime_UTC']

    objects = EventObjectManager()

    def __unicode__(self):
        return u'{0}'.format(self.message_name)

    # properties

    @property
    def message_name(self):
        return self.Messages.types.keys()[self.message_type]

    @property
    def message(self):
        msg = getattr(self, '%s_message' % self.message_name)()
        return simplejson.dumps({'message': msg[0], 'objects': msg[1]})

    @property
    def header(self):
        object_name, obj = getattr(self, '%s_header' % self.message_name)()
        is_deleted = getattr(obj, 'is_deleted', False)
        id = getattr(obj, 'pk', None) if not is_deleted else None
        return simplejson.dumps({
            'object': object_name,
            'id': id,
            'name': getattr(obj, 'name', ''),
        })

    @property
    def is_system_event(self):
        return self.user is None

    def obj_dict(self, obj, object_name):
        pk = obj.pk if not obj.is_deleted else None
        return {'object': object_name, 'id': pk, 'name': obj.name}

    @property
    def creative_1_dict(self):
        return self.obj_dict(self.obj_1, 'creative')

    @property
    def strategy_1_dict(self):
        return self.obj_dict(self.obj_1, 'strategy')

    @property
    def campaign_1_dict(self):
        return self.obj_dict(self.obj_1, 'campaign')

    @property
    def report_1_dict(self):
        return {'object': 'report', 'id': self.report_1_id,
                'name': self.report_1_name}

    # Events rendering declarations

    # event 'campaign_created'

    @classmethod
    def campaign_created(cls, campaign, *args, **kwargs):
        kwargs.update(
            account=campaign.account,
            obj_1=campaign,
        )
        return args, kwargs

    def campaign_created_header(self):
        return 'campaign', self.obj_1

    def campaign_created_message(self):
        return 'The campaign <%= campaign %> was just created', \
            {'campaign': self.campaign_1_dict}

    # event 'strategy_created'

    @classmethod
    def strategy_created(cls, strategy, *args, **kwargs):
        kwargs.update(
            account=strategy.campaign.account,
            obj_2=strategy.campaign,
            obj_1=strategy,
        )
        return args, kwargs

    def strategy_created_header(self):
        return 'campaign', self.obj_2

    def strategy_created_message(self):
        return 'The strategy <%= strategy %> was just created', \
            {'strategy': self.strategy_1_dict}

    # event 'creative_pending'

    @classmethod
    def creative_pending(cls, creative, *args, **kwargs):
        kwargs.update(account=creative.owner, obj_1=creative)
        return args, kwargs

    def creative_pending_header(self):
        return 'creative', self.obj_1

    def creative_pending_message(self):
        return 'The creative <%= creative %> was just submitted for audit', \
            {'creative': self.creative_1_dict}

    # event 'creative_audited'

    @classmethod
    def creative_audited(cls, creative, *args, **kwargs):
        return cls.creative_pending(creative, *args, **kwargs)

    def creative_audited_header(self):
        return 'creative', self.obj_1

    def creative_audited_message(self):
        return 'The creative <%= creative %> just passed audit', \
            {'creative': self.creative_1_dict}

    # event 'creative_rejected'

    @classmethod
    def creative_rejected(cls, creative, *args, **kwargs):
        return cls.creative_pending(creative, *args, **kwargs)

    def creative_rejected_header(self):
        return 'creative', self.obj_1

    def creative_rejected_message(self):
        return 'The creative <%= creative %> is rejected', \
            {'creative': self.creative_1_dict}

    # event 'creative_expired'

    @classmethod
    def creative_expired(cls, creative, *args, **kwargs):
        return cls.creative_pending(creative, *args, **kwargs)

    def creative_expired_header(self):
        return 'creative', self.obj_1

    def creative_expired_message(self):
        return 'The creative <%= creative %> has expired', {'creative': self.creative_1_dict}

    # event 'video_encoded'

    @classmethod
    def video_encoded(cls, creative, *args, **kwargs):
        return cls.creative_pending(creative, *args, **kwargs)

    def video_encoded_header(self):
        return 'creative', self.obj_1

    def video_encoded_message(self):
        return 'The video <%= creative %> has finished encoding', {'creative': self.creative_1_dict}

    # event 'video_encoding_failed'

    @classmethod
    def video_encoding_failed(cls, creative, *args, **kwargs):
        return cls.creative_pending(creative, *args, **kwargs)

    def video_encoding_failed_header(self):
        return 'creative', self.obj_1

    def video_encoding_failed_message(self):
        return 'The video <%= creative %> failed to encode', {'creative': self.creative_1_dict}

    # event 'not_enough_budget_for_audit'

    @classmethod
    def not_enough_budget_for_audit(cls, creative, *args, **kwargs):
        return cls.creative_pending(creative, *args, **kwargs)

    def not_enough_budget_for_audit_header(self):
        return 'creative', self.obj_1

    def not_enough_budget_for_audit_message(self):
        return 'Not enough money to send creative <%= creative %> for audit', \
            {'creative': self.creative_1_dict}


# Event signals

@receiver(pre_save, sender=Event)
def event_pre_save(sender, instance, **kwargs):
    event = instance

    if is_timezoned(event.datetime_UTC):
        raise ValidationError("datetime_UTC can't have timezone")


@receiver(post_save, sender=Event)
def event_post_save(sender, instance, **kwargs):
    event = instance
    User.objects.filter(account=event.account)\
        .update(unread_events_count=F('unread_events_count') + 1)
