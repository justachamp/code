from django.contrib.auth import get_user_model
from django.core import signing
from django.shortcuts import get_object_or_404

from requests import codes
from rest_framework.response import Response
from rest_framework.views import APIView

from addnow.apps.accounts.throttling import TokenRateThrottle


class ReminderMuteView(APIView):
    """
    Unsubscribe from reminders if token is valid
    """
    throttle_classes = (TokenRateThrottle,)
    permission_classes = ()

    def get(self, request, key):

        try:
            data = signing.loads(key)
        except (signing.BadSignature, signing.SignatureExpired):
            return Response(data={'status': 'bad signature'}, status=codes.bad)

        user_class = get_user_model()
        user = get_object_or_404(user_class, pk=data['uid'])
        user.is_reminders_muted = True
        user.save()

        return Response(data={'status': 'done'}, status=codes.ok)
