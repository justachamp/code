import pickle
import httplib2
import logging

from django.conf import settings
from django.core.cache import cache

from oauth2client import clientsecrets
from oauth2client.client import FlowExchangeError, OAuth2WebServerFlow, TokenRevokeError
from oauth2client.contrib import xsrfutil
from oauth2client.contrib.django_orm import Storage

from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from addnow.apps.accounts.models import Site
from addnow.apps.analytics import settings as analytics_settings, utils
from addnow.apps.analytics.exceptions import ProfileIDNotProvidedError
from addnow.apps.analytics.models import CredentialsModel
from addnow.apps.analytics.reports import get_active_visitors_report


# Get an instance of a logger
logger = logging.getLogger(__name__)


class OAuth2WebServerFlowMixin(object):
    @staticmethod
    def get_flow(scope, device_uri=None):
        client_type, client_info = clientsecrets._validate_clientsecrets(settings.GOOGLE_OAUTH_CONFIG)
        if client_type in (clientsecrets.TYPE_WEB, clientsecrets.TYPE_INSTALLED):
            constructor_kwargs = {
                'redirect_uri': client_info['redirect_uris'][0],
                'auth_uri': client_info['auth_uri'],
                'token_uri': client_info['token_uri'],
                'approval_prompt': client_info['approval_prompt']
            }

            revoke_uri = client_info.get('revoke_uri')
            if revoke_uri is not None:
                constructor_kwargs['revoke_uri'] = revoke_uri
            if device_uri is not None:
                constructor_kwargs['device_uri'] = device_uri
            return OAuth2WebServerFlow(
                client_info['client_id'],
                client_info['client_secret'],
                scope,
                **constructor_kwargs)


class LoginView(OAuth2WebServerFlowMixin, APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        flow = self.get_flow(scope=analytics_settings.FLOW_SCOPE)

        logger.debug('Generating state token...')

        flow.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY, request.user)
        key = analytics_settings.FLOW_CACHE_KEY_PLACEHOLDER % request.user.pk

        logger.debug('Setting OAuth2 Web server Flow to cache with key: %s', key)

        cache.set(key, pickle.dumps(flow))

        ctx = {'auth_url': flow.step1_get_authorize_url()}

        logger.debug('Response context: %s', ctx)

        return Response(ctx, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        storage = Storage(CredentialsModel, 'user', request.user, 'credential')
        credential = storage.get()

        key = analytics_settings.FLOW_CACHE_KEY_PLACEHOLDER % request.user.id

        logger.debug('Deleting OAuth2 Web server Flow to cache with key: %s', key)

        cache.delete(key)

        if credential:
            http = httplib2.Http()
            http = credential.authorize(http)
            try:
                credential.revoke(http)
            except TokenRevokeError:
                pass
            storage.delete()

        return Response({}, status=status.HTTP_200_OK)


class AuthCallbackView(OAuth2WebServerFlowMixin, APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        error = request.data.get('error')

        if error:
            logger.error(error)
            raise exceptions.ValidationError(error)

        try:
            state = request.data['state'].encode('ascii')
            code = request.data['code']
        except KeyError:
            logger.error('No mandatory fields supplied')
            raise exceptions.ValidationError('No mandatory fields supplied')

        if not xsrfutil.validate_token(settings.SECRET_KEY, state, request.user):
            logger.error('Invalid token')
            raise exceptions.PermissionDenied('Invalid token')

        key = analytics_settings.FLOW_CACHE_KEY_PLACEHOLDER % request.user.pk

        logger.debug('Getting OAuth2 Web server Flow from cache by key: %s', key)

        cached_flow = cache.get(key)

        if cached_flow:
            flow = pickle.loads(cached_flow)
        else:
            flow = self.get_flow(scope=analytics_settings.FLOW_SCOPE)

        try:
            credential = flow.step2_exchange(code)

            logger.debug('Saving OAuth2 credential to database')

            storage = Storage(CredentialsModel, 'user', request.user, 'credential')
            storage.put(credential)
        except FlowExchangeError as ex:
            logger.error(ex.message)
            raise exceptions.APIException(ex.message)

        return Response({}, status=status.HTTP_201_CREATED)


class AccountsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):

        data = []  # resulting dict

        service = utils.get_service(request.user)
        if not service:
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)

        accounts = utils.get_accounts(service)

        for account in accounts:
            properties_data = []

            logger.debug('Getting account `%s` web properties...', account.get('name'))
            webproperties = utils.get_webproperties(service, account['id'])

            for prop in webproperties:
                logger.debug('Web property name: %s (%s)', prop.get('name'), prop.get('id'))

                profiles = utils.get_profiles(service, account['id'], prop['id'])

                properties_data.append({'name': prop['name'], 'id': prop['id'], 'profiles': profiles})

            data.append({'id': account['id'], 'name': account['name'], 'properties': properties_data})

        return Response(data, status=status.HTTP_200_OK)


class PageviewsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, site_id):
        try:
            site = Site.objects.get(pk=site_id, user=request.user)
        except Site.DoesNotExist as ex:
            raise exceptions.APIException(ex.message)

        if not site.analytics_profile:
            raise exceptions.APIException('Analytics view (profile) ID does not provided for this site')

        begin_date = request.GET.get('begin_date')
        end_date = request.GET.get('end_date')
        aggregation = request.GET.get('aggregation', 'day')
        dimension = {
            'day': 'ga:date',
            'hour': 'ga:hour'
        }[aggregation]

        data = utils.get_report_data(
            request.user, site.analytics_profile, begin_date, end_date,
            ['ga:pageviews'], [dimension, 'ga:pagePath']
        )

        return Response(data)


class ReferringDomainsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, site_id):
        try:
            site = Site.objects.get(pk=site_id, user=request.user)
        except Site.DoesNotExist as ex:
            raise exceptions.APIException(ex.message)

        if not site.analytics_profile:
            raise exceptions.APIException('Analytics view (profile) ID does not provided for this site')

        begin_date = request.GET.get('begin_date')
        end_date = request.GET.get('end_date')

        data = utils.get_report_data(
            request.user, site.analytics_profile, begin_date, end_date,
            ['ga:entrances'], ['ga:source'], '-ga:entrances', 'ga:medium==referral'
        )

        return Response(data)


class SearchTermsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, site_id):
        try:
            site = Site.objects.get(pk=site_id, user=request.user)
        except Site.DoesNotExist as ex:
            raise exceptions.APIException(ex.message)

        if not site.analytics_profile:
            raise exceptions.APIException('Analytics view (profile) ID does not provided for this site')

        begin_date = request.GET.get('begin_date')
        end_date = request.GET.get('end_date')

        data = utils.get_report_data(
            request.user, site.analytics_profile, begin_date, end_date,
            ['ga:entrances'], ['ga:keyword'], '-ga:entrances',
            'ga:medium==organic;ga:keyword!=(not provided);ga:keyword!=(not set)'
        )

        return Response(data)


class SearchEnginesView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, site_id):
        try:
            site = Site.objects.get(pk=site_id, user=request.user)
        except Site.DoesNotExist as ex:
            raise exceptions.APIException(ex.message)

        if not site.analytics_profile:
            raise exceptions.APIException('Analytics view (profile) ID does not provided for this site')

        begin_date = request.GET.get('begin_date')
        end_date = request.GET.get('end_date')

        data = utils.get_report_data(
            request.user, site.analytics_profile, begin_date, end_date,
            ['ga:entrances'], ['ga:source'], '-ga:entrances', 'ga:medium==organic'
        )

        return Response(data)


class ActiveVisitorsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, site_id):
        try:
            site = Site.objects.get(pk=site_id, user=request.user)
        except Site.DoesNotExist as ex:
            raise exceptions.APIException(ex.message)

        history = request.query_params.get('history', None)

        try:
            data = get_active_visitors_report(request.user, site, history)
        except ProfileIDNotProvidedError as ex:
            raise exceptions.APIException(ex.message)

        return Response(data)
