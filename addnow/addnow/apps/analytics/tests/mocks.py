from oauth2client.client import TokenRevokeError
from rest_framework.response import Response
from rest_framework import status

from addnow.apps.accounts.models import Site


def mocked_credential_revoke(http):
    pass


def mocked_expired_credential_revoke(http):
    raise TokenRevokeError


def mocked_validate_token(key, token, user_id, **kwargs):
    if token == '1':
        return True

    return False


def mocked_step2_exchange(*args, **kwargs):
    pass


def mocked_accounts_get(request):
    return Response([], status=status.HTTP_200_OK)


def mocked_site(pk, user):
    analytics_profile = True

    if pk == 1:
        analytics_profile = False

    return Site(pk=pk, user=user, analytics_profile=analytics_profile)


def get_analytics_ga_users_data(*args):
    return {
        'kind': 'analytics#gaData',
        'rows': [
            [
                '44.2167',
                '42.0500',
                'Russia',
                'Cherkessk',
                'yandex',
                '17',
                '56',
                '1'
            ],
            [
                '55.0084',
                '82.9357',
                'Russia',
                'Novosibirsk',
                'yandex',
                '17',
                '56',
                '1'
            ],
            [
                '52.2870',
                '104.3050',
                'Russia',
                'Irkutsk',
                'yandex',
                '17',
                '55',
                '1'
            ],
            [
                '55.7558',
                '37.6173',
                'Russia',
                'Moscow',
                'yandex',
                '17',
                '55',
                '2'
            ],
            [
                '59.9343',
                '30.3351',
                'Russia',
                'Saint Petersburg',
                'yandex',
                '17',
                '55',
                '1'
            ],
            [
                '47.9105',
                '33.3918',
                'Ukraine',
                'Kryvyi Rih',
                'yandex',
                '17',
                '54',
                '1'
            ],
            [
                '52.2870',
                '104.3050',
                'Russia',
                'Irkutsk',
                'yandex',
                '17',
                '54',
                '1'
            ],
            [
                '53.2000',
                '45.0167',
                'Russia',
                'Penza',
                'yandex',
                '17',
                '54',
                '1'
            ],
            [
                '56.9761',
                '60.5944',
                'Russia',
                'Verkhnyaya Pyshma',
                'yandex',
                '17',
                '54',
                '1'
            ],
            [
                '59.9343',
                '30.3351',
                'Russia',
                'Saint Petersburg',
                'yandex',
                '17',
                '54',
                '1'
            ],
            [
                '42.8803',
                '47.6383',
                'Russia',
                'Kaspiysk',
                'rambler',
                '17',
                '53',
                '1'
            ],
            [
                '53.2000',
                '45.0167',
                'Russia',
                'Penza',
                'yandex',
                '17',
                '53',
                '1'
            ],
            [
                '55.7558',
                '37.6173',
                'Russia',
                'Moscow',
                'yandex',
                '17',
                '53',
                '1'
            ],
            [
                '59.9343',
                '30.3351',
                'Russia',
                'Saint Petersburg',
                'yandex',
                '17',
                '53',
                '2'
            ],
            [
                '54.5519',
                '36.2851',
                'Russia',
                'Kaluga',
                'yandex',
                '17',
                '52',
                '1'
            ]
        ],
        'containsSampledData': False,
        'columnHeaders': [
            {
                'dataType': 'STRING',
                'columnType': 'DIMENSION',
                'name': 'ga:latitude'
            },
            {
                'dataType': 'STRING',
                'columnType': 'DIMENSION',
                'name': 'ga:longitude'
            },
            {
                'dataType': 'STRING',
                'columnType': 'DIMENSION',
                'name': 'ga:country'
            },
            {
                'dataType': 'STRING',
                'columnType': 'DIMENSION',
                'name': 'ga:city'
            },
            {
                'dataType': 'STRING',
                'columnType': 'DIMENSION',
                'name': 'ga:source'
            },
            {
                'dataType': 'STRING',
                'columnType': 'DIMENSION',
                'name': 'ga:hour'
            },
            {
                'dataType': 'STRING',
                'columnType': 'DIMENSION',
                'name': 'ga:minute'
            },
            {
                'dataType': 'INTEGER',
                'columnType': 'METRIC',
                'name': 'ga:users'
            }
        ],
        'profileInfo': {
            'webPropertyId': 'UA-35890489-3',
            'internalWebPropertyId': '74546951',
            'tableId': 'ga:76956947',
            'profileId': '76956947',
            'profileName': 'Ru',
            'accountId': '35890489'
        },
        'itemsPerPage': 15,
        'totalsForAllResults': {
            'ga:users': '2571'
        },
        'nextLink': 'https://www.googleapis.com/analytics/v3/data/ga?ids=ga:76956947&'
                    'dimensions=ga:latitude,ga:longitude,ga:country,ga:city,ga:source,ga:hour,ga:minute&'
                    'metrics=ga:users&sort=-ga:hour,-ga:minute&filters=ga:longitude!%3D0.0000&'
                    'start-date=2015-08-03&end-date=2015-08-04&start-index=16&max-results=15',
        'query': {
            'sort': [
                '-ga:hour',
                '-ga:minute'
            ],
            'max-results': 15,
            'dimensions': 'ga:latitude,ga:longitude,ga:country,ga:city,ga:source,ga:hour,ga:minute',
            'start-date': '2015-08-03',
            'start-index': 1,
            'ids': 'ga:76956947',
            'metrics': [
                'ga:users'
            ],
            'filters': 'ga:longitude!=0.0000',
            'end-date': '2015-08-04'
        },
        'totalResults': 2459,
        'id': 'https://www.googleapis.com/analytics/v3/data/ga?ids=ga:76956947&'
              'dimensions=ga:latitude,ga:longitude,ga:country,ga:city,ga:source,ga:hour,ga:minute&'
              'metrics=ga:users&sort=-ga:hour,-ga:minute&filters=ga:longitude!%3D0.0000&'
              'start-date=2015-08-03&end-date=2015-08-04&max-results=15',
        'selfLink': 'https://www.googleapis.com/analytics/v3/data/ga?ids=ga:76956947&'
                    'dimensions=ga:latitude,ga:longitude,ga:country,ga:city,ga:source,ga:hour,ga:minute&'
                    'metrics=ga:users&sort=-ga:hour,-ga:minute&filters=ga:longitude!%3D0.0000&'
                    'start-date=2015-08-03&end-date=2015-08-04&max-results=15'
    }


def get_analytics_realtime_users_data(*args):
    return {
        'kind': 'analytics#realtimeData',
        'rows': [
            [
                '44.216667',
                '42.049999',
                'Russia',
                'Cherkessk',
                'yandex',
                '1'
            ],
            [
                '44.952118',
                '34.102417',
                'Ukraine',
                'Simferopol',
                'yandex',
                '1'
            ],
            [
                '46.966667',
                '142.733337',
                'Russia',
                'Yuzhno-Sakhalinsk',
                '(not set)',
                '1'
            ],
            [
                '47.216667',
                '38.916664',
                'Russia',
                'Taganrog',
                'yandex',
                '1'
            ],
            [
                '47.233334',
                '39.700001',
                'Russia',
                'Rostov-on-Don',
                'yandex',
                '1'
            ],
            [
                '49.233082',
                '28.468218',
                'Ukraine',
                'Vinnytsia',
                'yandex',
                '1'
            ],
            [
                '52.612198',
                '39.598122',
                'Russia',
                'Lipetsk',
                '(not set)',
                '1'
            ],
            [
                '53.202778',
                '50.140831',
                'Russia',
                'Samara',
                '(not set)',
                '1'
            ],
            [
                '54.551861',
                '36.285099',
                'Russia',
                'Kaluga',
                '(not set)',
                '1'
            ],
            [
                '54.551861',
                '36.285099',
                'Russia',
                'Kaluga',
                'yandex',
                '1'
            ],
            [
                '54.790310',
                '32.050365',
                'Russia',
                'Smolensk',
                'yandex',
                '1'
            ],
            [
                '55.164440',
                '61.436844',
                'Russia',
                'Chelyabinsk',
                'yandex',
                '1'
            ],
            [
                '55.166668',
                '59.666668',
                'Russia',
                'Zlatoust',
                'yandex',
                '1'
            ],
            [
                '55.755829',
                '37.617298',
                'Russia',
                'Moscow',
                'yandex',
                '4'
            ],
            [
                '56.501038',
                '84.992447',
                'Russia',
                'Tomsk',
                'yandex',
                '1'
            ],
            [
                '58.000000',
                '56.316666',
                'Russia',
                'Perm',
                'yandex',
                '1'
            ],
            [
                '59.934277',
                '30.335098',
                'Russia',
                'Saint Petersburg',
                'yandex',
                '1'
            ]
        ],
        'totalResults': 17,
        'totalsForAllResults': {
            'rt:activeUsers': '20'
        },
        'columnHeaders': [
            {
                'dataType': 'STRING',
                'columnType': 'DIMENSION',
                'name': 'rt:latitude'
            },
            {
                'dataType': 'STRING',
                'columnType': 'DIMENSION',
                'name': 'rt:longitude'
            },
            {
                'dataType': 'STRING',
                'columnType': 'DIMENSION',
                'name': 'rt:country'
            },
            {
                'dataType': 'STRING',
                'columnType': 'DIMENSION',
                'name': 'rt:city'
            },
            {
                'dataType': 'STRING',
                'columnType': 'DIMENSION',
                'name': 'rt:source'
            },
            {
                'dataType': 'INTEGER',
                'columnType': 'METRIC',
                'name': 'rt:activeUsers'
            }
        ],
        'query': {
            'metrics': [
                'rt:activeUsers'
            ],
            'max-results': 1000,
            'ids': 'ga:76956947',
            'dimensions': 'rt:latitude,rt:longitude,rt:country,rt:city,rt:source'
        },
        'profileInfo': {
            'webPropertyId': 'UA-35890489-3',
            'internalWebPropertyId': '74546951',
            'tableId': 'realtime:76956947',
            'profileId': '76956947',
            'profileName': 'Ru',
            'accountId': '35890489'
        },
        'id': 'https://www.googleapis.com/analytics/v3/data/realtime?ids=ga:76956947&'
              'dimensions=rt:latitude,rt:longitude,rt:country,rt:city,rt:source&metrics=rt:activeUsers',
        'selfLink': 'https://www.googleapis.com/analytics/v3/data/realtime?ids=ga:76956947&'
                    'dimensions=rt:latitude,rt:longitude,rt:country,rt:city,rt:source&metrics=rt:activeUsers'
    }


def get_analytics_profile(*args):
    return {
        'kind': 'analytics#profile',
        'name': 'Ru',
        'created': '2013-09-23T17:47:25.510Z',
        'updated': '2014-03-08T18:51:37.663Z',
        'websiteUrl': 'http://razmerkoles.ru',
        'currency': 'USD',
        'internalWebPropertyId': '74546951',
        'childLink': {
            'href': 'https://www.googleapis.com/analytics/v3/management/accounts/35890489/webproperties/UA-35890489-3/'
                    'profiles/76956947/goals',
            'type': 'analytics#goals'
        },
        'eCommerceTracking': False,
        'webPropertyId': 'UA-35890489-3',
        'timezone': 'Asia/Omsk',
        'parentLink': {
            'href': 'https://www.googleapis.com/analytics/v3/management/accounts/35890489/webproperties/UA-35890489-3',
            'type': 'analytics#webproperty'
        },
        'permissions': {
            'effective': [
                'COLLABORATE',
                'EDIT',
                'MANAGE_USERS',
                'READ_AND_ANALYZE'
            ]
        },
        'type': 'WEB',
        'id': '76956947',
        'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/35890489/webproperties/UA-35890489-3/'
                    'profiles/76956947',
        'accountId': '35890489'
    }
