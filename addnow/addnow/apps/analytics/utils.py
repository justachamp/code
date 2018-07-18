import logging
import random
import time

from httplib2 import Http

from googleapiclient import discovery, errors
from oauth2client.contrib.django_orm import Storage

from addnow.apps.analytics.cache import cache
from addnow.apps.analytics.http import AddnowHttpRequest
from addnow.apps.analytics.models import CredentialsModel

MAX_RESULTS = '500'

# Get an instance of a logger
logger = logging.getLogger(__name__)


def make_request_with_exponential_backoff(analytics):
    """Wrapper to request Google Analytics data with exponential backoff.

    The makeRequest method accepts the analytics service object, makes API
    requests and returns the response. If any error occurs, the makeRequest
    method is retried using exponential backoff.

    :param analytics: The analytics service object

    Returns:
    The API response from the makeRequest method.

    """
    for n in range(0, 5):
        try:
            return analytics.execute()
        except errors.HttpError, ex:
            logger.exception(ex)
            if ex.resp.reason in ['userRateLimitExceeded', 'quotaExceeded']:
                time.sleep((2 ** n) + random.random())

    logger.debug('There has been an error, the request never succeeded.')
    return []


def get_service(user):
    service = None
    storage = Storage(CredentialsModel, 'user', user, 'credential')
    credentials = storage.get()
    if credentials:
        authorized_http = credentials.authorize(Http())
        credentials.refresh(authorized_http)
        service = discovery \
            .build(
                'analytics', 'v3',
                http=authorized_http,
                requestBuilder=AddnowHttpRequest,
                credentials=credentials,
                cache=cache
            )

    return service


def get_report_data(user, profile_id, start_date, end_date, metrics, dimensions, sort=None, filters=None):
    service = get_service(user)

    if sort and isinstance(sort, (list, type)):
        sort = ','.join(sort)

    analytics = service \
        .data() \
        .ga() \
        .get(
            ids='ga:' + profile_id,
            start_date=start_date.strftime('%Y-%m-%d'),
            end_date=end_date.strftime('%Y-%m-%d'),
            metrics=','.join(metrics),
            dimensions=','.join(dimensions),
            sort=sort,
            filters=filters,
            max_results=MAX_RESULTS
        )

    return make_request_with_exponential_backoff(analytics)


def get_realtime_data(user, profile_id, metrics, dimensions, filters=None):
    service = get_service(user)

    analytics = service \
        .data() \
        .realtime() \
        .get(
            ids='ga:' + profile_id,
            metrics=','.join(metrics),
            dimensions=','.join(dimensions),
            filters=filters
        )

    return make_request_with_exponential_backoff(analytics)


def get_accounts(service):
    analytics = service \
        .management() \
        .accounts() \
        .list()

    accounts = make_request_with_exponential_backoff(analytics)
    logger.debug('Accounts found: %s', accounts.get('totalResults'))

    return accounts.get('items', [])


def get_webproperties(service, account_id):
    analytics = service \
        .management() \
        .webproperties() \
        .list(
            accountId=account_id
        )

    webproperties = make_request_with_exponential_backoff(analytics)
    logger.debug('Web properties found: %s', webproperties.get('totalResults'))

    return webproperties.get('items', [])


def get_profiles(service, account_id, web_property_id):
    analytics = service \
        .management() \
        .profiles() \
        .list(
            accountId=account_id,
            webPropertyId=web_property_id
        )

    profiles = make_request_with_exponential_backoff(analytics)
    logger.debug('Profiles found: %s', profiles.get('totalResults'))

    return profiles.get('items', [])


def get_profile(user, account_id, web_property_id, profile_id):
    service = get_service(user)

    analytics = service \
        .management() \
        .profiles() \
        .get(
            accountId=account_id,
            webPropertyId=web_property_id,
            profileId=profile_id
        )

    return make_request_with_exponential_backoff(analytics)
