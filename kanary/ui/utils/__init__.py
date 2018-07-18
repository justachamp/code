import urllib
from adserving.types import Decimal
from datetime import datetime, timedelta, time
from functools import wraps

import pytz
import simplejson
from django.utils import timezone
from django.http import HttpResponse
from django.conf.urls import url

from slugify import slugify

from etc.constants import (
    BACKEND_DATE_FORMAT, BACKEND_TIME_FORMAT, BACKEND_DATE_TIME_FORMAT
)


def render_to_json(preserve_http_response=False, **jsonargs):
    """
    http://djangosnippets.org/snippets/2102/
    Renders a JSON response with a given returned instance. Assumes
    json.dumps() can handle the result. The default output uses an indent of 4.

    @render_to_json()
    def a_view(request, arg1, argN):
        ...
        return {'x': range(4)}

    @render_to_json(indent=2)
    def a_view2(request):
        ...
        return [1, 2, 3]

    """
    def outer(f):
        @wraps(f)
        def inner_json(request, *args, **kwargs):
            result = f(request, *args, **kwargs)
            if preserve_http_response and isinstance(result, HttpResponse):
                return result

            r = HttpResponse(mimetype='application/json')
            if result:
                indent = jsonargs.pop('indent', 4)
                r.write(simplejson.dumps(result, indent=indent, **jsonargs))
            else:
                r.write("{}")
            return r
        return inner_json
    return outer


def now_UTC():
    '''
    Returns:
        datetime without timezone - current UTC time
    '''

    now = timezone.make_aware(timezone.now(), timezone.get_current_timezone())
    utc_now = now.astimezone(pytz.timezone('UTC'))
    return utc_now.replace(tzinfo=None)


def into_UTC(date_time, timezone):
    '''
    Moves datetime.datetime to UTC time using account timezone

    Args:
        date_time(datetime.datetime) - date to be moved
        timezone(string) - timezone from pytz.all_timezones
    Returns:
        datetime.datetime without tzinfo - time moved into UTC
    '''

    if date_time.tzinfo:
        raise Exception('Can\'t UTC datetime with tzinfo')

    tz = pytz.timezone(timezone)
    date_time = tz.localize(date_time, is_dst=True)
    utc = pytz.timezone('UTC')
    return date_time.astimezone(utc).replace(tzinfo=None)


def get_default_timezone():
    '''Returns default timezone for app'''
    return 'UTC'


def from_UTC(date_time, timezone):
    '''
    Moves datetime.datetime from UTC time into account timezone

    Args:
        date_time(datetime.datetime) - date to be moved
        timezone(string) - timezone from pytz.all_timezones
    Returns:
        datetime.datetime without tzinfo - time moved into account tz
    '''

    if date_time.tzinfo:
        raise Exception('Can\'t move datetime with tzinfo')

    tz = pytz.timezone(timezone)
    date_time = date_time.replace(tzinfo=pytz.timezone('UTC'))
    date_time = date_time.astimezone(tz)
    return date_time.replace(tzinfo=None)


def prepend_slug(self):
    '''
    Tastypie related function.
    Returns urls list that allows to use slug in path of resource
    '''

    view = self.wrap_view('dispatch_detail')
    name = self._meta.resource_name

    path_slug = r'^(?P<resource_name>%s)/s/(?P<slug>\S+)/$' % name
    path_id = r'^(?P<resource_name>%s)/(?P<id>\d+)/$' % name

    return [
        url(path_slug, view, name='api_dispatch_detail'),
        url(path_id, view, name='api_dispatch_detail_id'),
    ]


def unique_slugify(instance, account_filter=None, field=None):
    '''
    Returns unique slug based on specified field of given object.
    If slug exists - new one with appended suffix ('-2', '-3', etc.)
    is created ad returned.
    '''
    account_filter = account_filter or {}
    if not field:
        field = lambda instance: instance.name

    another_exists = lambda s: \
        instance.__class__.objects.filter(slug=s, **account_filter) \
        .exclude(id=instance.id).exists()

    base = slug = slugify(unicode(field(instance)))
    suffix = 2
    while another_exists(slug):
        slug = '%s-%s' % (base, suffix)
        suffix += 1

    return slug


def format_number(number_string):
    '''
    Formats given number string to the UI representation.
    '''
    number = Decimal(number_string)
    return "{:,}".format(number)


def append_dollar(decimal_val):
    '''
    Appends dollar sign to the Decimal value (rounded to two places)
    and returns it as a string.
    :rtype: string (i.e '$12.45' or '-$12.45') or None (if value is None)
    '''
    if decimal_val is None:
        return None

    rounded_val = decimal_val.quantize(Decimal('0.01'))

    if rounded_val >= 0:
        return '$%s' % rounded_val

    return '-$%s' % abs(rounded_val)


def chop(thestring, ending):
    '''
    Removes given ending from the string.
    :param str thestring: base string that we want to chop off.
    :param str ending: string that will be cut off from the base string.
    '''
    if thestring.endswith(ending):
        return thestring[:-len(ending)].rstrip()
    return thestring


def get_period_quarters(start=None, until=None, tz='UTC'):
    '''Returns quarters values (strings) between two times
    Also translates it to proper timezones
    Args:
        start (time) - start of period
        until (time) - end of period
        tz - optional timezone name
    Returns:
        A list of strings describing next quarters in format:
        get_period_quarters(time(15, 30), time(16, 0))
        ['1530', '1545', '1600']
    '''
    start = start or time(0)
    until = until or time(23, 59)

    # TODO: implement user time-zones
    our_timezone = pytz.timezone(get_default_timezone())
    user_timezone = pytz.timezone(tz)

    curr_time = datetime(2000, 1, 1, start.hour, start.minute, 0, 0,
                         our_timezone).astimezone(user_timezone)
    end_time = datetime(2000, 1, 1, until.hour, until.minute, 0, 0,
                        our_timezone).astimezone(user_timezone)
    minutes = []
    while curr_time < end_time:
        minutes.append(curr_time.strftime("%H%M"))
        curr_time += timedelta(minutes=15)
    return minutes


def time_hydrate(data, prefix, date_pattern='{0}', time_pattern='{0}_hour'):
    """Time form conversion: dict -> datetime"""
    return datetime.strptime('{0}T{1}'.format(
        data[date_pattern.format(prefix)],
        data[time_pattern.format(prefix)]
    ), BACKEND_DATE_TIME_FORMAT)


def time_dehydrate(dt, prefix, date_pattern='{0}', time_pattern='{0}_hour'):
    """Time form conversion: datetime -> dict"""
    return {
        date_pattern.format(prefix): dt.strftime(BACKEND_DATE_FORMAT),
        time_pattern.format(prefix): dt.strftime(BACKEND_TIME_FORMAT),
    }


def is_timezoned(datet):
    '''
    Arguments:
        datet(datetime.datetime)
    Returns:
        is_timezoned(bool) - true if datetime has timezone setted
    '''
    if datet and hasattr(datet, 'tzinfo') and datet.tzinfo is not None:
        return True
    return False


def traverse_object(obj, path=None):
    '''
    Returns object's attribute according to passed path
    or None if such attribute doesn't exist.
    Example usage:
        foobar = traverse_object(Class, ['foo', 'bar'])
        foobar == Class.foo.bar -> True
    '''
    if not path:
        return obj

    for i in path:
        obj = getattr(obj, i)
        if obj is None:
            return
    return obj


def url_with_querystring(path, **kwargs):
    return path + '?' + urllib.urlencode(kwargs)
