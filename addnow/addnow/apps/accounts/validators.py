# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, URLValidator


class DomainNameValidator(RegexValidator):
    message = 'Enter a valid domain name.'
    regex = re.compile(
        r'(?:' + URLValidator.ipv4_re + '|' + URLValidator.ipv6_re + '|' + URLValidator.host_re + ')\Z',
        re.IGNORECASE
    )

    def __init__(self, accept_idna=True, **kwargs):
        self.accept_idna = accept_idna
        super(DomainNameValidator, self).__init__(**kwargs)

    def __call__(self, value):
        try:
            super(DomainNameValidator, self).__call__(value)
        except ValidationError as exc:
            if not self.accept_idna:
                raise
            if not value:
                raise
            try:
                idna_value = value.encode('idna')
            except UnicodeError:
                raise exc
            super(DomainNameValidator, self).__call__(idna_value)
