'''
Custom fields for models - required by South migrations
'''

from functools import partial

from south.modelsinspector import introspector
from django.db.models import (
    ForeignKey,
    CharField,
    DecimalField,
    DateTimeField,
    SET_NULL,
    URLField
)

from adserving.types import Decimal
from etc.constants import cpm_offset_length, f_offset_length
from etc.utils import round_time_quarter


ForeignKeySetNull = partial(ForeignKey, null=True, on_delete=SET_NULL)
CharField255 = partial(CharField, max_length=255)
LongURLField = partial(URLField, max_length=2000)

DECIMAL_BIG = (19, 2)
DECIMAL_SMALL = (7, 2)

CPM = (7, 3)
BUDGET = (19, 2)
BUDGET_SPENT = (30, cpm_offset_length + f_offset_length + CPM[1])


class BaseDecimal(DecimalField):

    max_digits = None
    decimal_places = None

    @classmethod
    def to_precision(cls, dec):
        '''
        Return rounded decimal for easy comparisions.
        :param Decimal dec: decimal to quantize
        :return Decimal: copy of dec, quantized to class precision
        '''
        precision = Decimal('0.1') ** cls.decimal_places
        return dec.quantize(precision)

    def __init__(self, max_digits=None, decimal_places=None, **kwargs):
        DecimalField.__init__(self,
                              max_digits=max_digits or self.max_digits,
                              decimal_places=decimal_places or self.decimal_places,
                              **kwargs)


class BigDecimalField(BaseDecimal):

    max_digits, decimal_places = DECIMAL_BIG


class SmallDecimalField(BaseDecimal):

    max_digits, decimal_places = DECIMAL_SMALL


class BudgetDecimalField(BaseDecimal):

    max_digits, decimal_places = BUDGET


class BudgetSpentDecimalField(BaseDecimal):

    max_digits, decimal_places = BUDGET_SPENT


class CPMDecimalField(BaseDecimal):

    max_digits, decimal_places = CPM


class QuarterDateTimeField(DateTimeField):

    '''
    Rounds the datetime values stored in field to minute quarters.

    Eg. date with hour 13:33 will be converted to 13:30 and anything below
    minutes will be cut off

    more examples:

    * 13:44:59 -> 13:30
    * 12:12:00 -> 12:00
    * 09:00:01 -> 09:00

    .. warning::

        Due to DjangoORM nature, this won't be visible on model instance,
        unless you save and read object again.
    '''

    def to_python(self, value):
        value = super(QuarterDateTimeField, self).to_python(value)
        if not value:
            return value

        return round_time_quarter(value)

    def south_field_triple(self):
        args, kwargs = introspector(self)
        return 'django.db.models.fields.DateTimeField', args, kwargs


# South rules declaration for custom fields
rules = [
    [
        (BigDecimalField, ),
        [],
        {
            'max_digits': ['max_digits', {'default': DECIMAL_BIG[0]}],
            'decimal_places': ['decimal_places', {'default': DECIMAL_BIG[1]}],
        },
    ],
    [
        (SmallDecimalField, ),
        [],
        {
            'max_digits': ['max_digits', {'default': DECIMAL_SMALL[0]}],
            'decimal_places': [
                'decimal_places', {'default': DECIMAL_SMALL[1]}
            ],
        },
    ],
    [
        (BudgetDecimalField, ),
        [],
        {
            'max_digits': ['max_digits', {'default': BUDGET[0]}],
            'decimal_places': [
                'decimal_places', {'default': BUDGET[1]}
            ],
        },
    ],
    [
        (BudgetSpentDecimalField, ),
        [],
        {
            'max_digits': ['max_digits', {'default': BUDGET_SPENT[0]}],
            'decimal_places': [
                'decimal_places', {'default': BUDGET_SPENT[1]}
            ],
        },
    ],
    [
        (CPMDecimalField, ),
        [],
        {
            'max_digits': ['max_digits', {'default': CPM[0]}],
            'decimal_places': [
                'decimal_places', {'default': CPM[1]}
            ],
        },
    ],
]
