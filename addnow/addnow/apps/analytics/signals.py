import django.dispatch

analytics_revoke_access = django.dispatch.Signal(providing_args=['user'])
