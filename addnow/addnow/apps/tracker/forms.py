import logging

import html2text

from django import forms
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

logger = logging.getLogger(__name__)

SUBJECT = 'Check this out!'


class SendEmailForm(forms.Form):
    from_email = forms.EmailField(label='Your email address')
    to_email = forms.EmailField(label='Your Friends email address')
    message = forms.CharField(widget=forms.Textarea, label='Write a message', max_length=2000, min_length=6)
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    def send_email(self):
        cd = self.cleaned_data
        html_body = render_to_string('tracker/email_body.html', cd)
        body = html2text.html2text(html_body)
        headers = {
            'Reply-To': cd['from_email'],
            'From': cd['from_email'],
            'Sender': settings.DEFAULT_FROM_EMAIL
        }

        email = EmailMultiAlternatives(
            SUBJECT, body, settings.DEFAULT_FROM_EMAIL,
            [cd['to_email']], headers=headers
        )
        email.attach_alternative(html_body, 'text/html')
        email.send()
