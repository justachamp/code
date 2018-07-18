import random
from urlparse import urljoin

from etc.constants import DJANGO_MAX_INT

from django.core.urlresolvers import reverse
from django.forms import (
    Form, ModelForm, CharField, EmailField, ValidationError
)
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.safestring import mark_safe

from ui.account.models import User, Account
from ui.mail import mailing

from ui.settings import FRONTEND_HOST


class SignupForm(Form):

    email = EmailField()
    password = CharField()
    repeat_password = CharField()

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(SignupForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']

        if Account.objects.filter(name=email).exists():
            login_url = self.request.build_absolute_uri(reverse('auth-login'))
            raise ValidationError(
                mark_safe('This email is already registered. Please '
                          '<a href="%s">login</a>.' % login_url)
            )
        return email

    def clean_repeat_password(self):
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')

        if password and repeat_password and password != repeat_password:
            raise ValidationError('Please repeat password correctly.')

        return repeat_password

    def save_new_user(self):
        """ Creates empty account and new inactive user. """

        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        while True:
            account_number = random.randint(1000, DJANGO_MAX_INT)
            if not Account.objects.filter(account_number=account_number).exists():
                break

        account = Account.objects.create(account_number=account_number,
                                         name=email)
        user = User(account=account, username=email, email=email,
                    is_signup_complete=False)
        user.set_password(password)

        user.save()

        return user


class ProfileForm(ModelForm):

    class Meta:
        model = Account
        fields = [
            'is_agency', 'company_name', 'first_name', 'last_name', 'address',
            'city', 'zip_code', 'country', 'province', 'phone', 'vat'
        ]

    def save_validated_fields(self):
        """
        Saves only those fields that passed validation.
        """
        for field in self.cleaned_data.iterkeys():
            setattr(self.instance, field, self.cleaned_data[field])

        self.instance.save()


class KanaryPasswordResetForm(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email__iexact=email, is_active=True)
        except User.DoesNotExist:
            raise ValidationError('Account with specified email does not exist')
        return email

    def save(self, *args, **kwargs):
        """
        Overrides default django behavior to enable sending mail about
        password reset by our mailing implementation.
        """
        email = self.cleaned_data["email"]
        try:
            user = User.objects.get(email__iexact=email, is_active=True)
        except User.DoesNotExist:
            return

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = kwargs['token_generator'].make_token(user)

        reset_link = urljoin(
            FRONTEND_HOST,
            reverse('reset_password_confirm', args=[uid, token])
        )

        mailing.reset_password(user, reset_link).send()
