from adserving.types import Decimal
from etc import dimensions, constants
from bidrequest.constants import EXCHANGES

date_format = '%Y-%m-%dT%H:%M'

default_account = [
    {'name': 'acc', 'timezone': 'Europe/Warsaw'},
    {'name': 'acc_2', 'timezone': 'Africa/Bamako'}
]

default_user = [{'username': 'user_2', 'email': 'test@clearcode.cc',
                 'password': '123', 'account': 'acc', 'is_signup_complete': True}]

inactive_user = [default_user[0].copy()]
inactive_user[0]['is_signup_complete'] = False

default_payments = [
    {'account': 'acc', 'datetime': '2014-02-10T00:00', 'amount': 30},
    {'account': 'acc_2', 'datetime': '2014-01-11T00:00', 'amount': 2}
]

default_invoices = [
    {'account': 'acc', 'number': '123456', 'datetime': '2014-02-08T00:00',
     'amount': 50, 'pdf': 'test.pdf'}
]

default_landing_page = [
    {'owner': 'acc', 'url': 'http://www.google.com/'},
    {'owner': 'acc', 'url': 'http://www.wp.pl/'},
    {'owner': 'acc_2', 'url': 'http://www.python.org/'}
]
default_campaign = [
    {
        'name': 'I\'m a fruit', 'account': 'acc',
        'budget_total': 8000, 'start_UTC': '2013-01-01T00:00',
        'end_UTC': '2013-01-31T00:00',
        'landing_site': 'http://www.google.com/'
    },
    {
        'name': 'Campaign for multi-user testing', 'account': 'acc_2',
        'budget_total': 6000, 'start_UTC': '2014-01-01T00:00',
        'end_UTC': '2014-01-31T00:00',
        'landing_site': 'http://www.python.org/'
    }
]

default_strategies = [
    {'name': 'Hello this is Citrus', 'campaign': 'I\'m a fruit',
     'budget_total': 8000, 'budget_bid_CPM': Decimal('0.1')},
    {'name': 'han i has a pumpkin?', 'campaign': 'I\'m a fruit',
     'budget_total': 4321, 'budget_bid_CPM': Decimal('0.1')},
    {'name': 'FBX', 'campaign': 'I\'m a fruit',
     'budget_total': 100055, 'budget_bid_CPM': Decimal('0.1'), 'type': u'fb'}
]
default_creative = [{'name': 'creative_image_1', 'owner': 'acc', 'width': 300,
                     'height': 250, 'image': 'creatives/test_creative.jpg'}]

default_fbx_creative = [{'name': 'creative_fbx_1', 'owner': 'acc', 'width': 254,
                     'height': 133, 'destination':u'fs', 'title':'fb_default_creative_title', 'body': 'fb_default_creative_body', 'image': 'creatives/test_creative.jpg'},
                        {'name': 'creative_fbx_2', 'owner': 'acc', 'width': 600,
                     'height': 315, 'destination':u'fs', 'title':'fb_default_creative_title', 'body': 'fb_default_creative_body', 'image': 'creatives/test_creative.jpg'}]

default_news_feed_creative = [{'name': 'creative_fbx_news_feed_1', 'owner': 'acc', 'width': 200,
                     'height': 200, 'destination':u'fn', 'title':'fb_default_creative_title', 'body': 'fb_default_creative_body', 'image': 'creatives/test_creative.jpg',
                     'message': 'fbx news feed default message', 'domain': 'gravity4_0.com', 'brand_id': 1},
                              {'name': 'creative_fbx_news_feed_2', 'owner': 'acc', 'width': 470,
                     'height': 246, 'destination':u'fn', 'title':'fb_default_creative_title', 'body': 'fb_default_creative_body', 'image': 'creatives/test_creative.jpg',
                     'message': 'fbx news feed default message', 'domain': 'gravity4_0.com', 'brand_id': 1},
                              {'name': 'creative_fbx_news_feed_3', 'owner': 'acc', 'width': 90,
                     'height': 90, 'destination':u'fn', 'title':'fb_default_creative_title', 'body': 'fb_default_creative_body', 'image': 'creatives/test_creative.jpg',
                     'message': 'fbx news feed default message', 'domain': 'gravity4_0.com', 'brand_id': 1},
                              {'name': 'creative_fbx_news_feed_4', 'owner': 'acc', 'width': 600,
                     'height': 315, 'destination':u'fn', 'title':'fb_default_creative_title', 'body': 'fb_default_creative_body', 'image': 'creatives/test_creative.jpg',
                     'message': 'fbx news feed default message', 'domain': 'gravity4_0.com', 'brand_id': 1},]

default_creative_flash = [{'name': 'creative_flash_1', 'owner': 'acc',
                           'width': 300, 'height': 250, 'file': 'creatives/game.swf'}]

default_creative_video = [{'name': 'creative_video_1',
                           'owner': 'acc',
                           'width': 736,
                           'height': 1472,
                           'file': 'creatives/creative.mpg',
                           'liverail_id': 2233,
                           'liverail_status': 'active',
                           'duration': 15, 'media_variants': [
                               {
                                   u'bitrate': 736,
                                   u'duration': 15,
                                   u'height': 360,
                                   u'type': u'video/mp4',
                                   u'url': u'http://example.com/lo.mp4',
                                   u'width': 480
                               }, {
                                   u'bitrate': 1472,
                                   u'duration': 15,
                                   u'height': 480,
                                   u'type': u'video/mp4',
                                   u'url': u'http://example.com/me.mp4',
                                   u'width': 640
                               }
                           ]},
                            {'name': 'creative_video_2',
                           'owner': 'acc',
                           'width': 736,
                           'height': 666,
                           'file': 'creatives/creative.mpg',
                           'liverail_id': 2234,
                           'liverail_status': 'pending'}]

default_adverts = [
    {
        'name': 'ad_lemon',
        'strategy': 'Hello this is Citrus',
        'creative': 'creative_image_1',
        'url': 'http://www.google.com/',
    },
    {
        'name': 'ad_orange',
        'strategy': 'Hello this is Citrus',
        'creative': 'creative_image_1',
        'url': 'http://www.wp.pl/',
    },
    {
        'name': 'ad_carrot',
        'strategy': 'han i has a pumpkin?',
        'creative': 'creative_image_1',
        'url': 'http://www.google.com/',
    },
    {
        'name': 'ad_celery',
        'strategy': 'han i has a pumpkin?',
        'creative': 'creative_image_1',
        'url': 'http://www.wp.pl/',
    },
]

default_audiences = [{'name': 'Vegetarian Audience', 'owner': 'acc'},
                     {'name': 'Meat-eater Audience', 'owner': 'acc'}]

default_segments = [
    {'appnexus_id': 95002, 'name': 'Brand Protection Data::Non-standard Content::Alcohol (proximic)'},
    {'appnexus_id': 94999, 'name': 'Brand Protection Data::Non-standard Content::Adult (proximic)'},
    {'appnexus_id': 94435, 'name': 'Automotive::Auto Parts (proximic)'},
]

default_app_publishers = [
    {
        'category': dimensions.g_publisher,
        'exchange': EXCHANGES.appnexus,
        'values': ('Application', 'Rubicon', 'Ninja Fruit'),
        'represented_values': ('app', '23', 'Ninja Fruit')
    },
    {
        'category': dimensions.g_publisher,
        'exchange': EXCHANGES.appnexus,
        'values': ('Application', 'Rubicon', 'Angry Birds'),
        'represented_values': ('app', '23', 'Angry Birds')
    }
]

default_fb_pages = [
    {'brand_id': 1, 'thirdparty_page_id': '15530789316308597', 'page_name': 'test_fbx_page_1', 'owner': 'acc'},
    {'brand_id': 2, 'thirdparty_page_id': '15530789316308597', 'page_name': 'test_fbx_page_2', 'owner': 'acc'}
]

default_site_publishers = [
    {
        'category': dimensions.g_publisher,
        'exchange': EXCHANGES.appnexus,
        'values': ('Web', 'Rubicon', 'piwik.pro'),
        'represented_values': ('site', '23', 'piwik.pro')
    },
    {
        'category': dimensions.g_publisher,
        'exchange': EXCHANGES.nexage,
        'values': ('Web', 'Nexage', 'rafalmichal.com'),
        'represented_values': ('site',
                               constants.NEXAGE_NETWORK_ID,
                               'rafalmichal.com')
    }
]

default_network_publishers = [
    {
        'category': dimensions.g_publisher,
        'exchange': EXCHANGES.appnexus,
        'values': ('Application', 'Rubicon'),
        'represented_values': ('app', '23')
    },
    {
        'category': dimensions.g_publisher,
        'exchange': EXCHANGES.appnexus,
        'values': ('Web', 'Rubicon'),
        'represented_values': ('site', '23')
    },
    {
        'category': dimensions.g_publisher,
        'exchange': EXCHANGES.nexage,
        'values': ('Application', 'Nexage'),
        'represented_values': ('app', constants.NEXAGE_NETWORK_ID)
    },
    {
        'category': dimensions.g_publisher,
        'exchange': EXCHANGES.nexage,
        'values': ('Web', 'Nexage'),
        'represented_values': ('site', constants.NEXAGE_NETWORK_ID)
    }
]

publisherset_app = {
    'owner': 'acc',
    'name': 'Awsome app publishers',
    'inventory': 'app'
}

publisherset_site = {
    'owner': 'acc',
    'name': 'Awsome web publishers',
    'inventory': 'site'
}

auth_test_users = [
    {'username': 'user_1', 'email': 'user1@clearcode.cc', 'password': '123',
     'account': 'account_1', 'is_signup_complete': True},
    {'username': 'user_2', 'email': 'user2@clearcode.cc', 'password': '123',
     'account': 'account_2', 'is_signup_complete': True}
]

auth_test_accounts = [
    {'name': 'account_1', 'timezone': 'Europe/Warsaw'},
    {'name': 'account_2', 'timezone': 'Europe/Warsaw'}
]

auth_test_lpages = [
    {'owner': 'account_1', 'url': 'http://site1.com'},
    {'owner': 'account_2', 'url': 'http://site2.com'}
]

auth_test_campaigns = [
    {'name': 'campaign_1', 'account': 'account_1', 'budget_total': 100,
     'start_UTC': '2013-05-01T00:00', 'end_UTC': '2013-05-10T00:00',
     'landing_site': 'http://site1.com'},
    {'name': 'campaign_2', 'account': 'account_2', 'budget_total': 200,
     'start_UTC': '2013-05-01T00:00', 'end_UTC': '2013-05-10T00:00',
     'landing_site': 'http://site2.com'},
]

auth_default_invoices = [
    {'account': 'account_1', 'number': '123456', 'datetime': '2014-02-08T00:00',
     'amount': 50, 'pdf': 'test.pdf'}
]

auth_default_payments = [
    {'account': 'account_1', 'datetime': '2014-02-10T00:00', 'amount': 30}
]
