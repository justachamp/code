import re
from datetime import datetime
from decimal import Decimal

import pytest

from tastypie.resources import ModelResource
from ui.utils import prepend_slug
from ui.backend.management.commands.fill_reports import distribute_sum_randomly


@pytest.mark.django_db
def test_prepend_slug():
    class TestResource(ModelResource):
        prepend_urls = prepend_slug

    test_resource = TestResource()

    url = test_resource.urls[0]
    regex = r'^(?P<resource_name>test)/s/(?P<slug>\S+)/$'
    assert url.regex.pattern == re.compile(regex, re.UNICODE).pattern
    assert url.name == 'api_dispatch_detail'

    url = test_resource.urls[1]
    regex = r'^(?P<resource_name>test)/(?P<id>\d+)/$'
    assert url.regex.pattern == re.compile(regex, re.UNICODE).pattern
    assert url.name == 'api_dispatch_detail_id'


def test_now_UTC():
    from ui.utils import now_UTC

    now = now_UTC()

    assert now is not None
    assert isinstance(now, datetime)
    assert now.tzinfo is None


def test_into_UTC():
    from pytz.exceptions import UnknownTimeZoneError
    from ui.utils import into_UTC

    now = datetime.utcnow()

    utc_now = into_UTC(now, 'CET')
    assert isinstance(utc_now, datetime)
    assert now.tzinfo is None
    with pytest.raises(UnknownTimeZoneError):
        into_UTC(now, '')


@pytest.mark.parametrize('dividers_number, total_sum', (
        (5, 100),
        (5, Decimal('100.00')),
        (8, Decimal('58.96')),
        (3, 1),
        (2, 0),
        (4, Decimal('1.00')),
        (6, Decimal('0.00')),
))
def test_distribute_sum_randomly(dividers_number, total_sum):
    distribution = distribute_sum_randomly(dividers_number, total_sum)

    assert len(distribution) == dividers_number
    assert sum(distribution) == total_sum
