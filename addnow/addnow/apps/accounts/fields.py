from django.db import models

from addnow.apps.accounts.validators import DomainNameValidator


class BlankAsNullMixin(models.Field):
    """
    Allows to store empty strings as nulls.
    """
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(BlankAsNullMixin, self).__init__(*args, **kwargs)

    def to_python(self, value):
        value = super(BlankAsNullMixin, self).to_python(value)
        return value or ''

    def get_prep_value(self, value):
        value = super(BlankAsNullMixin, self).get_prep_value(value)
        return value or None


class BlankAsNullCharField(BlankAsNullMixin, models.CharField):
    pass


class BlankAsNullURLField(BlankAsNullMixin, models.URLField):
    pass


class BlankAsNullDomainNameField(BlankAsNullCharField):
    default_validators = [DomainNameValidator()]
    description = 'Domain name'
