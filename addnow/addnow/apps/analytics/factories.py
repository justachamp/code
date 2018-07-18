from django.contrib.auth import get_user_model

import factory

from addnow.apps.analytics.models import CredentialsModel


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Sequence(lambda n: 'user{0}@test.com'.format(n))
    password = 'password'
    has_analytics = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)


class CredentialsModelFactory(factory.DjangoModelFactory):
    class Meta:
        model = CredentialsModel

    user = factory.SubFactory(UserFactory)
