import logging

from django.core import signing
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.views import JSONWebTokenAPIView

from addnow.apps.accounts import emails, serializers
from addnow.apps.accounts.models import Site, User, WidgetConfiguration
from addnow.apps.accounts.serializers import JSONIsEmailVerifiedWebTokenSerializer, AllWidgetsSerializer, \
    widget_serializers_map
from addnow.apps.accounts.throttling import TokenRateThrottle, UpdateAccountRateThrottle
from addnow.cache import SiteSettingsCache, SiteTrimSettingsCache

logger = logging.getLogger(__name__)


class ObtainJSONWebToken(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = JSONIsEmailVerifiedWebTokenSerializer


class RegisterUserView(APIView):
    """
    Creates new account
    """
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = serializers.BaseUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save(force_insert=True)
            emails.verification(user)
            data = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUserView(APIView):
    """
    Creates new account
    """
    authentication_classes = ()
    permission_classes = ()

    def put(self, request):
        email = request.data.get('email')
        user = get_object_or_404(User, email=email)
        emails.verification(user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccountView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UpdateAccountRateThrottle,)
    serializer_class = serializers.UpdateUserSerializer

    def get_object(self, queryset=None):
        self.user_email = self.request.user.email
        return self.request.user

    def perform_update(self, serializer):
        # email changed - invalidate `is_verified` flag and send email with new verification token
        serializer.save()
        if self.user_email != serializer.instance.email:
            serializer.instance.email_is_verified = False
            serializer.instance.save(update_fields=['email_is_verified'])
            emails.verification(serializer.instance)


class EmailVerificationView(APIView):
    """
    Verifies email address if token is valid and redirects to SPA
    """
    throttle_classes = (TokenRateThrottle,)
    permission_classes = ()

    def get(self, request, key):
        try:
            data = signing.loads(key)
        except (signing.BadSignature, signing.SignatureExpired):
            return Response('Tampering detected!', status=status.HTTP_400_BAD_REQUEST)

        user_class = get_user_model()
        user = get_object_or_404(user_class, pk=data['uid'])

        if user.validate_email_token(data['token']):
            if not user.email_is_verified:
                user.email_is_verified = True
                user.save(update_fields=['email_is_verified'])
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response('Invalid token!', status=status.HTTP_400_BAD_REQUEST)


class PasswordResetAttemptView(APIView):
    """
    Sends email with token if email exists in database
    """
    throttle_classes = (TokenRateThrottle,)
    permission_classes = ()

    def post(self, request):
        serializer = serializers.PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object
            emails.password_reset_attempt(user)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    """
    Changes password if token is valid
    """
    throttle_classes = (TokenRateThrottle,)
    permission_classes = ()

    def post(self, request):
        serializer = serializers.PasswordResetSuccessSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object
            user.set_password(serializer.validated_data['password'])
            user.save(update_fields=['password'])
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseSiteView(generics.GenericAPIView):
    serializer_class = serializers.SiteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Site.objects.filter(user=self.request.user)


class SiteListCreateView(BaseSiteView, generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SiteRetrieveUpdateView(BaseSiteView, generics.RetrieveUpdateAPIView):

    def perform_update(self, serializer):
        current_site = Site.objects.get(id=serializer.instance.pk)
        if current_site.trim_api_key and not serializer.instance.trim_api_key:
            for widget in serializer.instance.widget_configurations.all():
                widget.vanity_domain = ""
                widget.save()

        serializer.save()
        delete_dict = dict(site_id=serializer.instance.pk)
        SiteSettingsCache.delete(delete_dict)
        SiteTrimSettingsCache.delete(delete_dict)


class BaseWidgetView(generics.GenericAPIView):
    lookup_url_kwarg = 'widget_pk'
    permission_classes = (IsAuthenticated,)


class WidgetListCreateView(BaseWidgetView, generics.ListCreateAPIView):
    def get_queryset(self):
        serializer_class = self.get_serializer_class()
        site_pk = self.kwargs['site_pk']
        return serializer_class.Meta.model.objects.filter(site=site_pk)

    def create(self, request, *args, **kwargs):
        self.request.data['site'] = self.kwargs['site_pk']
        return super(WidgetListCreateView, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        site_pk = self.kwargs['site_pk']
        serializer.save(site=Site.objects.get(pk=site_pk))
        SiteSettingsCache.delete(dict(site_id=site_pk))

    def get_serializer_class(self):
        request_data = self.request.data.copy()
        request_data.update(self.request.query_params)
        widget_type = request_data.get('type')
        return widget_serializers_map.get(widget_type, AllWidgetsSerializer)


class WidgetRetrieveUpdateView(BaseWidgetView, generics.RetrieveUpdateAPIView):
    def get_queryset(self):
        site_pk = self.kwargs['site_pk']
        return WidgetConfiguration.objects.filter(site=site_pk)

    def perform_update(self, serializer):
        serializer.save()
        SiteSettingsCache.delete(dict(site_id=serializer.instance.site.pk))

    def get_object(self):
        self.instance = super(WidgetRetrieveUpdateView, self).get_object()
        if self.request.method != 'GET':
            self.request.data['user'] = self.instance.site.user.pk
        return self.instance

    def get_serializer_class(self):
        return widget_serializers_map.get(self.instance.type, AllWidgetsSerializer)
