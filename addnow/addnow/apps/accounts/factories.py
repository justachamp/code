import factory

from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler

from addnow.apps.accounts import constants, models


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.User
    FACTORY_DJANGO_GET_OR_CREATE = ('email',)
    email = factory.Sequence(lambda n: 'user{0}@test.com'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'password')


class ApiTokenFactory(factory.DictFactory):

    @classmethod
    def _build(cls, model_class, *args, **kwargs):
        return super(ApiTokenFactory, cls)._build(model_class, *args, **kwargs)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        payload = jwt_payload_handler(kwargs['user'])
        return {'token': jwt_encode_handler(payload), 'user': kwargs['user']}


class SiteFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Site
    FACTORY_DJANGO_GET_OR_CREATE = ('domain',)
    domain = factory.Sequence(lambda n: 'domain_{0}.com'.format(n))
    user = factory.SubFactory(UserFactory)


class WidgetConfigurationFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.WidgetConfiguration
    FACTORY_DJANGO_GET_OR_CREATE = ('name',)
    name = factory.Sequence(lambda n: 'config_{0}'.format(n))
    site = factory.SubFactory(SiteFactory)
    type = constants.WIDGET_CONFIGURATION_SHARING_BUTTONS
    orientation = constants.BUTTON_ORIENTATION_HORIZONTAL
    button_size = constants.BUTTON_SIZE_MEDIUM
    button_style = constants.BUTTON_STYLE_ICON
    counter_position = constants.COUNTER_POSITION_RIGHT


class WidgetButtonFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.WidgetButton
    configuration = factory.SubFactory(WidgetConfigurationFactory)


class FacebookWidgetButtonFactory(WidgetButtonFactory):
    service = constants.SOCIAL_SERVICE_FACEBOOK


class GoogleWidgetButtonFactory(WidgetButtonFactory):
    service = constants.SOCIAL_SERVICE_GOOGLE_PLUS


class EmailWidgetButtonFactory(WidgetButtonFactory):
    service = constants.SOURCE_EMAIL


class SiteFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Site
    FACTORY_DJANGO_GET_OR_CREATE = ('domain',)
    domain = factory.Sequence(lambda n: 'domain_{0}.com'.format(n))
    user = factory.SubFactory(UserFactory)


class SocialUrlFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.SocialUrl
    site = factory.SubFactory(SiteFactory)


class FacebookUrlFactory(SocialUrlFactory):
    service = constants.SOCIAL_SERVICE_FACEBOOK


class GoogleUrlFactory(SocialUrlFactory):
    service = constants.SOCIAL_SERVICE_GOOGLE_PLUS


class UniqueUserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.UniqueUser
