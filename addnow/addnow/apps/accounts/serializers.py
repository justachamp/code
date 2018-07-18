# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from calendar import timegm

from django.contrib.auth import authenticate
from django.conf import settings
from django.utils.translation import ugettext as _

from rest_framework import serializers
from rest_framework.fields import CharField, EmailField, BooleanField
from rest_framework.settings import api_settings
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings as jwt_api_settings

from addnow.apps.accounts import models
from addnow.apps.accounts.constants import SOCIAL_SERVICE_PINTEREST

jwt_payload_handler = jwt_api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = jwt_api_settings.JWT_ENCODE_HANDLER


class UniqueFieldForInstanceValidator(object):
    """
    Validator that checks that some field in serializer field with many=True is unique.
    """
    message = 'The field {unique_field} must be unique.'

    def __init__(self, serializer_field, unique_field, message=None):
        self.serializer_field = serializer_field
        self.unique_field = unique_field
        self.message = message or self.message

    def __call__(self, attrs):
        value = attrs.get(self.serializer_field, None)
        if value:
            field_list = [item[self.unique_field] for item in value]
            if len(field_list) != len(set(field_list)):
                message = self.message.format(unique_field=self.unique_field)
                raise serializers.ValidationError({self.serializer_field: message})


class JSONIsEmailVerifiedWebTokenSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)

                if not user.email_is_verified:
                    msg = _('You need to verify your account before logging in.')
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                # Include original issued at time for a brand new token,
                # to allow token refresh
                if jwt_api_settings.JWT_ALLOW_REFRESH:
                    payload['orig_iat'] = timegm(
                        datetime.utcnow().utctimetuple()
                    )

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = _('Unable to login with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)


class BaseUserSerializer(serializers.ModelSerializer):
    password = CharField(write_only=True, min_length=4)

    class Meta:
        model = models.User
        fields = ('id', 'email', 'password')

    def update(self, instance, validated_data):
        super(BaseUserSerializer, self).update(instance, validated_data)
        if validated_data.get('password', None):
            instance.set_password(validated_data.get('password'))
            instance.save()
        return instance

    def create(self, validated_data):
        return models.User.objects.create_user(email=validated_data['email'],
                                               password=validated_data['password'])


class UpdateUserSerializer(BaseUserSerializer):
    """
    old_password is required when password being changed
    """
    old_password = CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ('email', 'old_password', 'password', 'offset', 'has_analytics')

    def validate(self, attrs):
        if attrs.get('password') and not attrs.get('old_password'):
            raise serializers.ValidationError('Provide current password')

        return attrs

    def validate_offset(self, value):
        if not (-12 * 60 <= value <= 14 * 60):
            raise serializers.ValidationError('Invalid timezone offset')
        return value

    def validate_old_password(self, value):
        if not self.instance.check_password(value):
            raise serializers.ValidationError('Password is incorrect')

        return value


class PasswordResetSerializer(serializers.Serializer):
    email = EmailField()

    def validate_email(self, value):
        user = models.User.objects.filter(email=value).first()
        self.object = user

        if not user:
            raise serializers.ValidationError('Email not found')

        if not user.is_active:
            raise serializers.ValidationError('User is inactive')

        if not user.email_is_verified:
            raise serializers.ValidationError('Email is not verified')

        return value


class PasswordResetSuccessSerializer(serializers.Serializer):
    token = CharField(required=True)
    password = CharField(required=True, min_length=4, write_only=True)

    @staticmethod
    def _validate_user_token(user, token):
        return user.validate_password_reset_token(token)

    def validate_token(self, value):
        try:
            # see accounts/templates/emails/password_reset_attempt.html
            user_pk, token = value.split('|', 1)
        except (ValueError, AttributeError):
            user_pk, token = None, None

        user = models.User.objects.filter(pk=user_pk).first()

        if not user or not self._validate_user_token(user, token):
            raise serializers.ValidationError('Token is invalid')

        self.object = user

        return value


class PasswordResetSuccessSerializerTest(PasswordResetSuccessSerializer):
    @staticmethod
    def _validate_user_token(user, token):
        return token == 'valid'

if settings.API_TEST:
    PasswordResetSuccessSerializer = PasswordResetSuccessSerializerTest


class WidgetButtonSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()
    is_short_link = serializers.SerializerMethodField()
    has_counter = serializers.SerializerMethodField()

    class Meta:
        model = models.WidgetButton
        fields = ('service', 'is_extra_button', 'follow_url', 'text', 'is_short_link', 'has_counter')

    def get_text(self, instance):
        return instance.get_service_display()

    def get_is_short_link(self, instance):
        return instance.service not in ('pinterest', 'reddit')

    def get_has_counter(self, instance):
        return instance.service not in ('whatsapp', 'sms', 'email', 'gmail')


class WidgetConfigurationSerializer(serializers.ModelSerializer):
    site = serializers.PrimaryKeyRelatedField(queryset=models.Site.objects.all(), write_only=True)
    buttons = WidgetButtonSerializer(many=True, required=True)

    allow_many = True

    class Meta:
        model = models.WidgetConfiguration
        required_fields = ()
        fields = ('id', 'site', 'name', 'type', 'orientation', 'button_size',
                  'button_style', 'counter_position', 'buttons', 'is_active', 'vanity_domain',
                  'position', 'has_link_share_button', 'extra_button_animation')
        validators = [
            UniqueTogetherValidator(
                queryset=models.WidgetConfiguration.objects.all(),
                fields=('site', 'name'),
                message='The name field should be unique among the site widgets'
            ),
            UniqueFieldForInstanceValidator(
                'buttons', 'service',
                message='Service must be unique for the widget configuration.'
            )
        ]

    def get_fields(self):
        fields = super(WidgetConfigurationSerializer, self).get_fields()
        # The fields in WidgetConfiguration model are optional, because we store all
        # widget types in one table. Make certain fields required depend on a widget type.
        for field_name, field in fields.items():
            if field_name in self.Meta.required_fields:
                field.required = True
                field.allow_blank = False
        return fields

    def validate_buttons(self, value):
        if not value:
            raise serializers.ValidationError('Widget configuration has no buttons.')
        return value

    def create(self, validated_data):
        buttons = validated_data.pop('buttons')
        site = validated_data.get('site')

        if not self.allow_many:
            current_count = self.Meta.model.objects.filter(site=site).count()
            if current_count > 0:
                message = 'You can not create more than one widget of this type.'
                raise serializers.ValidationError({
                    api_settings.NON_FIELD_ERRORS_KEY: [message]
                })

        widget_configuration = models.WidgetConfiguration.objects.create(**validated_data)

        for i, button in enumerate(buttons):
            is_extra_button = button.get('is_extra_button', False)
            models.WidgetButton.objects.create(
                service=button['service'],
                order=i,
                configuration=widget_configuration,
                is_extra_button=is_extra_button,
                follow_url=button.get('follow_url')
            )
        return widget_configuration

    def update(self, instance, validated_data):
        buttons_data = validated_data.pop('buttons', None)

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        if buttons_data:
            for i, data in enumerate(buttons_data):
                data['order'] = i

            buttons_services = [data['service'] for data in buttons_data]
            deleted_buttons = instance.buttons.exclude(service__in=buttons_services)
            deleted_buttons.delete()
            buttons = instance.buttons.all()

            for button in buttons:
                button_data = next(data for data in buttons_data
                                   if data['service'] == button.service)
                is_extra_button = button_data.get('is_extra_button', False)
                button.order = button_data['order']
                button.is_extra_button = is_extra_button
                button.follow_url = button_data.get('follow_url')
                button.save()
                buttons_data.remove(button_data)

            for button_data in buttons_data:
                is_extra_button = button_data.get('is_extra_button', False)
                models.WidgetButton.objects.create(
                    service=button_data['service'],
                    order=button_data['order'],
                    follow_url=button_data.get('follow_url'),
                    is_extra_button=is_extra_button,
                    configuration=instance
                )
        return instance


class SharingButtonsWidgetSerializer(WidgetConfigurationSerializer):
    class Meta(WidgetConfigurationSerializer.Meta):
        model = models.SharingButtonsWidget


class CopyPasteWidgetSerializer(WidgetConfigurationSerializer):
    allow_many = False

    class Meta(WidgetConfigurationSerializer.Meta):
        model = models.CopyPasteWidget


class OriginButtonsWidgetSerializer(WidgetConfigurationSerializer):
    class Meta(WidgetConfigurationSerializer.Meta):
        model = models.OriginButtonsWidget


class NewsletterWidgetSerializer(WidgetConfigurationSerializer):
    allow_many = False

    class Meta(WidgetConfigurationSerializer.Meta):
        model = models.NewsletterWidget
        required_fields = ('page_title', 'page_url')
        optional_fields = ('media_url',)
        fields = WidgetConfigurationSerializer.Meta.fields + required_fields + optional_fields

    def validate(self, attrs):
        # Validate that media url is required only if pinterest button is chosen.
        buttons = attrs.get('buttons')
        if buttons is None:
            buttons = getattr(self.instance, 'buttons', None)
        media_url = attrs.get('media_url')
        if media_url is None:
            media_url = getattr(self.instance, 'media_url', None) or None
        # Find the service in the possible list
        pinterest_exist = any(filter(lambda button: button['service'] == SOCIAL_SERVICE_PINTEREST, buttons))
        if pinterest_exist:
            if media_url is None:
                raise serializers.ValidationError(
                    {'media_url': self.fields['media_url'].error_messages['required']}
                )
            if not media_url:
                raise serializers.ValidationError(
                    {'media_url': self.fields['media_url'].error_messages['blank']}
                )
        return attrs


class MobileWidgetSerializer(WidgetConfigurationSerializer):
    allow_many = False

    class Meta(WidgetConfigurationSerializer.Meta):
        model = models.MobileWidget
        required_fields = ('min_width',)
        fields = WidgetConfigurationSerializer.Meta.fields + required_fields


class FollowWidgetSerializer(WidgetConfigurationSerializer):
    class Meta(WidgetConfigurationSerializer.Meta):
        model = models.FollowWidget

    def update(self, instance, validated_data):

        buttons_data = validated_data.pop('buttons', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        instance.buttons.all().delete()

        for i, button in enumerate(buttons_data):
            btn = models.WidgetButton(configuration=instance, order=i, **button)
            btn.save()

        return instance


class VerticalFloatWidgetSerializer(WidgetConfigurationSerializer):
    allow_many = False

    class Meta(WidgetConfigurationSerializer.Meta):
        model = models.VerticalFloatWidget
        required_fields = ('position',)
        fields = WidgetConfigurationSerializer.Meta.fields + required_fields


class CircularMobileWidgetSerializer(WidgetConfigurationSerializer):
    MINIMUM_BUTTONS = 3
    MAXIMUM_BUTTONS = 5

    class Meta(WidgetConfigurationSerializer.Meta):
        model = models.CircularMobileWidget
        required_fields = ('min_width', 'position')
        fields = WidgetConfigurationSerializer.Meta.fields + required_fields

    def validate_buttons(self, value):
        """
        Check that the buttons meet minimum threshold.
        :param value list of selected networks
        """
        if not value:
            raise serializers.ValidationError('Widget configuration has no buttons.')

        visible = len(filter(lambda x: not x['is_extra_button'], value))

        if visible < self.MINIMUM_BUTTONS:
            raise serializers.ValidationError('At least %d buttons in the widget.' % self.MINIMUM_BUTTONS)
        if visible > self.MAXIMUM_BUTTONS:
            raise serializers.ValidationError('No more than %d buttons in the widget.' % self.MAXIMUM_BUTTONS)
        return value


widget_serializers_map = {
    'sharing-buttons': SharingButtonsWidgetSerializer,
    'copy-paste': CopyPasteWidgetSerializer,
    'newsletter': NewsletterWidgetSerializer,
    'mobile': MobileWidgetSerializer,
    'follow-buttons': FollowWidgetSerializer,
    'vertical-float': VerticalFloatWidgetSerializer,
    'origin-buttons': OriginButtonsWidgetSerializer,
    'circular-mobile': CircularMobileWidgetSerializer
}


class AllWidgetsSerializer(WidgetConfigurationSerializer):
    class Meta(WidgetConfigurationSerializer.Meta):
        required_fields = \
            SharingButtonsWidgetSerializer.Meta.required_fields + \
            CopyPasteWidgetSerializer.Meta.required_fields + \
            NewsletterWidgetSerializer.Meta.required_fields + \
            MobileWidgetSerializer.Meta.required_fields + \
            FollowWidgetSerializer.Meta.required_fields + \
            VerticalFloatWidgetSerializer.Meta.required_fields + \
            CircularMobileWidgetSerializer.Meta.required_fields
        fields = WidgetConfigurationSerializer.Meta.fields + required_fields

    def to_representation(self, instance):
        data = super(AllWidgetsSerializer, self).to_representation(instance)

        try:
            widget_type = data['type']
            fields = widget_serializers_map[widget_type].Meta.fields
        except KeyError:
            return data

        filtered_data = {k: v for (k, v) in data.items() if k in fields}
        return filtered_data


class SocialUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialUrl
        fields = ('id', 'service', 'url')


class SiteSerializer(serializers.ModelSerializer):
    domain = CharField(
        max_length=255,
        required=True,
        validators=[UniqueValidator(queryset=models.Site.objects.all())]
    )
    social_urls = SocialUrlSerializer(many=True, required=False)
    hash_id = serializers.ReadOnlyField()
    has_short_urls = BooleanField(read_only=True)

    class Meta:
        model = models.Site
        fields = ('id', 'hash_id', 'domain', 'social_urls', 'address_bar_sharing', 'vanity_domain',
                  'copy_paste_sharing', 'trim_api_key', 'has_short_urls',
                  'analytics_account', 'analytics_property', 'analytics_profile',
                  'thank_you_message', 'thank_you_advert_image_url', 'thank_you_advert_url', 'thank_you_advert_title')
        validators = [
            UniqueFieldForInstanceValidator(
                'social_urls', 'service',
                message='Service must be unique for the site.')
        ]

    def create(self, validated_data):
        social_urls = validated_data.pop('social_urls', [])

        site = models.Site.objects.create(**validated_data)
        for social_url in social_urls:
            models.SocialUrl.objects.create(
                service=social_url['service'],
                url=social_url['url'],
                site=site
            )
        return site

    def update(self, instance, validated_data):
        social_urls_data = validated_data.pop('social_urls', [])

        if not validated_data.get('trim_api_key') and instance.trim_api_key:
            models.WidgetConfiguration.objects.update(vanity_domain=None)

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        instance.social_urls.all().delete()

        for social_url_data in social_urls_data:
            models.SocialUrl.objects.create(
                service=social_url_data['service'],
                url=social_url_data['url'],
                site=instance
            )

        return instance
