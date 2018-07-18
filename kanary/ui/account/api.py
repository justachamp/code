from tastypie import fields
from ui.authorization import Auth
from ui.utils import prepend_slug
from ui.account.models import User
from ui.common.api import ProtectedModelResource


class UserResource(ProtectedModelResource):

    prepend_urls = prepend_slug

    class Meta:
        resource_name = 'user'
        queryset = User.objects.all()
        allowed_methods = ('get', )
        authorization = Auth('id', lambda b: b.request.user.id)
        always_return_data = True
        fields = ['unread_events_count', 'email', 'account__account_number']

    id = fields.IntegerField('id', readonly=True)
    username = fields.CharField('username', readonly=True)
    timezone = fields.CharField('account__timezone', readonly=True)
    account_number = fields.IntegerField(
        'account__account_number',
        readonly=True
    )
    account_balance = fields.DecimalField(
        'account__account_balance',
        readonly=True
    )
