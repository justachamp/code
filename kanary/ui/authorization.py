from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized

from ui.utils import traverse_object


class Auth(Authorization):

    '''
    Class used for limit access to resources exposed via tastypie REST API.
    Authorization goal here is to present to logged in user only this data
    that match her account.
    '''
    def __init__(self, field, get_account=None, *args, **kwargs):
        '''
        init accepts two arguments that determine which data are
        permitted to be accessed by user.
            field - field name to be filtered
            get_account - Optional function that takes bundle as
                          argument and returns object that is a filter target.
                          If no function is passed 'bundle.request.user.account'
                          object is used.
        '''
        super(Authorization, self).__init__(*args, **kwargs)

        self.field = field
        self.get_request_account = get_account or (lambda b: b.request.user.account)

    def get_object_account(self, bundle):
        '''
        Getting account which attempt to modify the resource.
        '''
        path = self.field.split('__')
        object_account = traverse_object(bundle.obj, path)

        if isinstance(object_account, unicode):
            return int(object_account)

        return object_account

    def auth_list(self, objects, bundle):

        if not bundle.request.user.is_authenticated():
            raise Unauthorized(
                "You have no permissions to access this resource.")

        return objects.filter(**{self.field: self.get_request_account(bundle)})

    def auth_detail(self, objects, bundle):
        if not bundle.request.user.is_authenticated() or \
                not self.get_object_account(bundle) == \
                self.get_request_account(bundle):
            raise Unauthorized(
                "You have no permissions to access this resource.")

        return True

    # Methods required by tastypie (derived from Authorization)
    def read_list(self, object_list, bundle):
        return self.auth_list(object_list, bundle)

    def read_detail(self, object_list, bundle):
        return self.auth_detail(object_list, bundle)

    def update_list(self, object_list, bundle):
        return self.auth_list(object_list, bundle)

    def update_detail(self, object_list, bundle):
        return self.auth_detail(object_list, bundle)

    def delete_list(self, object_list, bundle):
        return self.auth_list(object_list, bundle)

    def delete_detail(self, object_list, bundle):
        return self.auth_detail(object_list, bundle)

    # create_detail - we are not implementing this, account is not attached
    #                 to models before they are saved
