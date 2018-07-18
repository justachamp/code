from addnow.apps.analytics.exceptions import ProfileIDNotProvidedError
from addnow.apps.analytics.reports import get_active_visitors_report as ga_active_visitors
from addnow.apps.reports.realtime import get_active_visitors_report as mongo_active_visitors


class DataProviderError(Exception):
    def __init__(self, message):
        self.message = message


class DataProvider(object):
    def get_data(self, user, site, history):
        raise NotImplementedError()


class GoogleAnalyticsDataProvider(DataProvider):
    """Get real time data from Google Analytics"""

    def get_data(self, user, site, history):
        try:
            return ga_active_visitors(user, site, history)
        except ProfileIDNotProvidedError as ex:
            raise DataProviderError(ex.message)


class MongoDataProvider(DataProvider):
    """Get real time data from MongoDB real time collection"""

    def get_data(self, user, site, history):
        try:
            return mongo_active_visitors(user, site, history)
        except Exception as ex:
            raise DataProviderError(ex.message)


def get_provider(source='ga'):
    """The factory method"""

    data_providers = {
        'ga': GoogleAnalyticsDataProvider,
        'mongo': MongoDataProvider
    }

    # fallback to ga data provider
    if source not in data_providers:
        source = 'ga'

    return data_providers[source]()
