from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from addnow.apps.accounts.models import Site
from addnow.apps.reports.providers import get_provider, DataProviderError


class ActiveVisitorsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, site_id):
        try:
            site = Site.objects.get(pk=site_id, user=request.user)
        except Site.DoesNotExist as ex:
            raise exceptions.APIException(ex.message)

        source = 'mongo'  # = request.query_params.get('source', 'mongo')

        if site.analytics_profile:
            source = 'ga'

        provider = get_provider(source)

        history = request.query_params.get('history', None)

        try:
            data = provider.get_data(request.user, site, history)
        except DataProviderError as ex:
            raise exceptions.APIException(ex.message)

        return Response(data)
