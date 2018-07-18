from django.core.signing import Signer, BadSignature
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator


class UserSigner(Signer):
    def validate_token(self, value, token):
        try:
            _value = self.unsign(token)
        except BadSignature:
            pass
        else:
            return _value == force_str(value)


class PasswordResetSigner(object):
    @staticmethod
    def sign(user):
        return default_token_generator.make_token(user)

    @staticmethod
    def validate_token(user, token):
        return default_token_generator.check_token(user, token)


user_signer = UserSigner()
password_signer = PasswordResetSigner()
