import pytest
import csv
from random import randint

from functools import partial
from datetime import datetime, timedelta

from django.core.management import call_command
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from etc import dimensions
from adserving.types import Decimal
from bidrequest.constants import EXCHANGES

# imported but never used - needs stay for conftest.py mechanism:
from ui.tests.utils import default_user
from ui.tests.initial_datafixtures import auth_test_users, auth_test_accounts,\
    auth_test_lpages, auth_test_campaigns, publisherset_app, publisherset_site

from ui.tests.browser.selenium_extensions import Client
from ui.tests.browser.page import LoginForm

from ui.account.models import Account, Payment
from ui.targeting import models as TM
from ui.targeting.models import TargetValue, TargetMap
from ui.campaign.models import Campaign, Strategy, Advert
from ui.report import models as RM
from ui.report.models import ReportStrategy, ReportAdvert, ReportStrategyGender, ReportCampaignDomain
from ui.storage.models import Creative


BIDDING_IMAGES = [
    {'name': 'Creative Default', 'owner': 'acc',
     'width': 300, 'height': 250, 'image': 'test_creative.jpg'},
    {'name': 'Creative Custom', 'owner': 'acc',
     'width': 500, 'height': 200, 'image': 'test_creative.jpg'},
    {'name': 'Creative Parted', 'owner': 'acc',
     'width': 600, 'height': 200, 'image': 'test_creative.jpg'},
]

BIDDING_CAMPAIGN = [
    {'name': 'Bidding Campaign', 'account': 'acc',
     'budget_total': 500, 'start_UTC': '2014-01-01T00:00',
     'end_UTC': '2014-01-31T00:00',
     'landing_site': 'http://www.google.com/'}
]

BIDDING_STRATEGY = [
    {'name': 'Bidding Strategy', 'campaign': 'Bidding Campaign',
     'budget_total': 200, 'budget_daily': 200,
     'budget_bid_CPM': Decimal('0.1')}
]

BIDDING_ADVERTS = [
    {'name': 'ad_bidding_1', 'strategy': 'Bidding Strategy',
     'creative': 'Creative Default', 'url': 'http://www.google.com/'},
    {'name': 'ad_bidding_2', 'strategy': 'Bidding Strategy',
     'creative': 'Creative Custom', 'url': 'http://www.wp.pl/'},
    {'name': 'ad_bidding_3', 'strategy': 'Bidding Strategy',
     'creative': 'Creative Parted', 'url': 'http://www.google.com/'},
]

BILLING_INVOICE = [
    {'account': 'acc', 'number': '123456', 'datetime': '2014-03-21T00:00',
     'amount': Decimal('123.56'), 'pdf': 'test.pdf'}
]

BILLING_PAYMENT = [
    {'account': 'acc', 'datetime': '2014-03-23T00:00',
     'amount': Decimal('99.76')}
]


def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker(pytest.mark.selenium)
        item.add_marker(pytest.mark.django_db(True))
        item.add_marker(pytest.mark.nondestructive)


@pytest.fixture(autouse=True)
def autouse_fixture(appnexus_api, cdn_api):
    return


@pytest.fixture
def fill_db(user_db):
    ''' Initializes database with all data implemented in setup '''

    setup = user_db
    setup.setup_creative_images()
    setup.setup_landing_pages()
    setup.setup_campaigns()
    setup.setup_strategies()
    setup.setup_audiences()
    setup.setup_bidding_periods()
    setup.setup_adverts()
    call_command('rebuild_index', interactive=False)

    return setup


@pytest.fixture
def fill_db_mobile_strategies(fill_db):
    ''' Full campaign setup with mobile strategies '''

    setup = fill_db

    for strategy in Strategy.objects.all():
        strategy.type = Strategy.MOBILE
        strategy.save()

    return setup


@pytest.fixture
def user(user_db):
    return user_db.models['user'][default_user[0]['username']]


@pytest.fixture
def bidding_db(user_db):
    '''
    Initializes db with one strategy and 3 adverts with
    different creatives, for bidding testing purposes.
    '''
    setup = user_db

    setup.setup_creative_images(BIDDING_IMAGES)
    setup.setup_landing_pages()
    setup.setup_campaigns(BIDDING_CAMPAIGN)
    setup.setup_strategies(BIDDING_STRATEGY)
    setup.setup_adverts(BIDDING_ADVERTS)
    call_command('rebuild_index', interactive=False)

    return setup


@pytest.fixture
def billing_db(user_db):
    '''
    Initializes db based on data for Billing & Transactions
    '''
    setup = user_db

    setup.setup_creative_images()
    setup.setup_landing_pages()
    setup.setup_campaigns()
    setup.setup_invoices(BILLING_INVOICE)
    setup.setup_payments(BILLING_PAYMENT)

    return setup


@pytest.fixture
def publishers_db(fill_db):
    ''' Initializes databases with publisher sets '''

    fill_db.setup_publishers()

    return fill_db


@pytest.fixture
def publisherset_db(fill_db):
    ''' Initializes databases with publisher sets '''

    set_app = fill_db.setup_publisherset(publisherset_app)
    set_site = fill_db.setup_publisherset(publisherset_site)

    (publishers_app, publishers_site,
     publishers_network) = fill_db.setup_publishers()

    for publisher in publishers_app:
        set_app.target_values.add(publisher)
    set_app.save()

    for publisher in publishers_site:
        set_site.target_values.add(publisher)
    set_site.save()

    return fill_db


def insert_targetvalues(target_values, exchange):
    for category, values in target_values:
        value = TargetMap.pack(values)
        TargetValue.objects.get_or_create(exchange=exchange, category=category, value=value)


@pytest.fixture
def representants():
    '''Inserts representants which are not in targeting_initial'''
    target_values = [
        [dimensions.g_location, ['USA']],
        [dimensions.g_location, ['USA', 'Ohio']],
        [dimensions.g_location, ['USA', 'Ohio', 'Cleveland']],
        [dimensions.g_location, ['USA', 'Wisconsin']],
        [dimensions.g_location, ['USA', 'Wisconsin', 'Madison']],
        [dimensions.g_location, ['USA', 'New York']],
        [dimensions.g_location, ['USA', 'New York', 'Syracuse']],
        [dimensions.g_os, ['Android']],
        [dimensions.g_os, ['Nokia OS']],
        [dimensions.g_os, ['Symbian']],
        [dimensions.g_device, ['Samsung', 'Samsung Galaxy S']],
        [dimensions.g_device, ['Sony', 'Sony Xperia Z']],
        [dimensions.g_device, ['LG', 'Lg Swift L9']],
        [dimensions.carrier, ['Plus']],
        [dimensions.carrier, ['Vodafone']],
        [dimensions.carrier, ['Orange']],
        [dimensions.os_version, ['Samsung Galaxy S']],
        [dimensions.os_version, ['v11 beta']]
    ]
    insert_targetvalues(target_values, EXCHANGES.nexage)
    call_command('rebuild_index', interactive=False)


@pytest.fixture
def domains():
    domains = [
        u'greenfelder.biz', u'uptonschulist.com', u'haag.info',
        u'watsica.com', u'sipeshand.com', u'emard.com', u'larson.biz',
        u'stracke.org', u'lockman.com', u'jakubowski.com', u'littel.org',
        u'stark.com', u'schmitt.com', u'mitchell.net', u'goodwin.com',
        u'okeefe.net', u'treutel.org', u'friesenkiehn.net', u'lynch.org',
        u'kris.org', u'walsh.com', u'murazik.com', u'mclaughlin.com',
        u'ratkerohan.net', u'jacobikuvalis.com', u'funk.com', u'hills.org',
        u'ornharris.info', u'bartonoconnell.com', u'hintzrau.com',
        u'lubowitz.com', u'sawayn.info', u'moen.com', u'friesen.org',
        u'oharahayes.com', u'vandervort.com', u'douglas.net',
        u'dietrich.com', u'ernserpacocha.info', u'crist.com',
        u'collier.com', u'hicklerau.biz', u'feestspencer.info',
        u'trantow.com', u'prosacco.info', u'haleydamore.com', u'hayes.com',
        u'bergstrom.com', u'heller.com', u'gerlach.com', u'schaden.com',
        u'harris.info', u'turcotte.com', u'breitenberg.info',
        u'pfannerstill.com', u'hauck.net', u'hilll.com', u'osinski.com',
        u'lebsack.com', u'naderbernier.info', u'huel.com', u'abshire.com',
        u'feest.biz', u'hansenwest.com', u'welch.com', u'tromp.com',
        u'gerhold.com', u'oconner.com', u'pagac.info', u'wisoky.com',
        u'kuphal.com', u'hettinger.com', u'murazikstanton.com',
        u'luettgen.com', u'cristlesch.com', u'barrowskuhlman.com',
        u'okuneva.org', u'lesch.com', u'volkman.net', u'marvin.info',
        u'bashiriannienow.org', u'donnelly.info', u'daniel.com',
        u'morissette.info', u'mohr.com', u'ziemann.com', u'daugherty.net',
        u'kleinrohan.com', u'roobwalter.com', u'huelhudson.com',
        u'ryanschinner.org', u'trantowemard.info', u'reichel.net',
        u'rutherford.com', u'gutmannkuhic.com', u'koelpin.com',
        u'weber.com', u'bosco.biz', u'barrowsfadel.info', u'kerluke.com'
    ]

    for domain in domains:
        TargetValue.objects.get_or_create(
            exchange=EXCHANGES.nexage,
            category=dimensions.domain,
            value=domain
        )


@pytest.fixture
def base_client(mozwebqa, live_server):
    ''' :returns: client instance '''
    client = Client(mozwebqa, live_server)
    client.get_nowait('/')

    return client


@pytest.fixture
def client(base_client, user_db):
    ''' :returns: `Client` instance with logged in user '''
    login_form = LoginForm(base_client)

    login_form.fill_inputs(
        username=default_user[0]['username'],
        password=default_user[0]['password']
    )

    login_form.submit()

    # Wait for all requests and animations will end,
    base_client.wait_for_xhr()

    return base_client


@pytest.fixture
def maturity_rating_segment():
    '''
    Creates 3 proximic segments with maturity rating
    '''

    # Proximic segments with maturity rating
    MATURITY_RATING = (
        {
            'id': 94974,
            'name': 'G',
            'description': 'General Audiences'
        },
        {
            'id': 94975,
            'name': 'PG13',
            'description': 'Parents Strongly Cautioned'
        },
        {
            'id': 94976,
            'name': 'R',
            'description': 'Restricted'
        },
    )

    for segment in MATURITY_RATING:
        TM.SegmentProximicMaturityRating.objects.create(
            appnexus_id=segment['id'],
            name=segment['name'],
            description=segment['description'],
        )


@pytest.fixture
def safety_level_segment():
    '''
    Creates safety levels segments
    '''

    SEGMENTS = (
        (330728, 'Safe from Adult'),
        (330729, 'Safe from Offensive'),
        (330730, 'Safe from Accidents'),
        (330731, 'Safe from Gambling / Gaming'),
        (330732, 'Safe from UGC'),
        (330733, 'Safe from Online Illegal'),
        (330734, 'Safe from Health Issues'),
        (330735, 'Safe from Alcohol'),
        (330736, 'Safe from Illegal Drugs'),
        (330737, 'Safe from Tobacco'),
        (330738, 'Safe from Terrorism'),
        (330739, 'Safe from Weapons'),
        (330740, 'Safe from Manga'),
    )
    for appnexus_id, name in SEGMENTS:
        TM.SegmentProximicSafetyLevel.objects.create(
            name=name,
            appnexus_id=appnexus_id
        )


@pytest.fixture
def language_segment():
    '''
    Creates Proximic segment with languages
    '''

    LANGUAGES = (
        (237332, 'English'),
        (237504, 'French'),
        (237505, 'Spanish'),
        (237506, 'Italian'),
        (237507, 'Dutch'),
        (237508, 'Russian'),
        (237509, 'Portuguese'),
        (237510, 'Polish'),
        (237511, 'German'),
        (782938, 'Danish'),
        (782951, 'Finnish'),
        (782959, 'Swedish'),
        (782978, 'Norwegian'),
    )

    for appnexus_id, name in LANGUAGES:
        TM.SegmentProximicPageLanguage.objects.create(
            appnexus_id=appnexus_id,
            name=name,
        )


@pytest.fixture
def page_quality_segment():
    '''
    Creates Proximic segment with page quality options
    '''

    PAGE_QUALITY = (
        (502695, 'High'),
        (502696, 'Medium'),
        (502697, 'Low'),
    )

    for appnexus_id, name in PAGE_QUALITY:
        TM.SegmentProximicPageQuality.objects.create(
            appnexus_id=appnexus_id,
            name=name,
        )


@pytest.fixture
def page_placement_segment():
    '''
    Creates Proximic segment with page placement options
    '''

    PAGE_PLACEMENT = (
        (502713, 'High', '728x90'),
        (502714, 'Medium', '728x90'),
        (502715, 'Low', '728x90'),

        (502716, 'High', '160x600'),
        (502717, 'Medium', '160x600'),
        (502719, 'Low', '160x600'),

        (502720, 'High', '300x250'),
        (502721, 'Medium', '300x250'),
        (502723, 'Low', '300x250'),

        (502724, 'High', '468x60'),
        (502725, 'Medium', '468x60'),
        (502726, 'Low', '468x60'),
    )

    for appnexus_id, parent_name, name in PAGE_PLACEMENT:
        parent, _ = TM.SegmentProximicPagePlacement.objects.get_or_create(name=parent_name)  # noqa
        TM.SegmentProximicPagePlacement.objects.get_or_create(
            appnexus_id=appnexus_id,
            name=name,
            parent=parent
        )


@pytest.fixture
def page_noticeability_segment():
    '''
    Creates Proximic segment with page noticeability options
    '''

    PAGE_NOTICEABILITY = (
        (502698, 'High', '728x90'),
        (502699, 'Medium', '728x90'),
        (502700, 'Low', '728x90'),

        (502701, 'High', '160x600'),
        (502703, 'Medium', '160x600'),
        (502705, 'Low', '160x600'),

        (502706, 'High', '300x250'),
        (502707, 'Medium', '300x250'),
        (502708, 'Low', '300x250'),

        (502709, 'High', '468x60'),
        (502710, 'Medium', '468x60'),
        (502712, 'Low', '468x60'),
    )

    for appnexus_id, parent_name, name in PAGE_NOTICEABILITY:
        parent, _ = TM.SegmentProximicPageNoticeability.objects.get_or_create(name=parent_name)  # noqa
        TM.SegmentProximicPageNoticeability.objects.get_or_create(
            appnexus_id=appnexus_id,
            name=name,
            parent=parent
        )


@pytest.fixture
def proximic_contextual_segment():
    '''
    Creates Proximic segment with contextual content options
    '''

    CONTEXTUAL = (
        (94425, 'Arts & Entertainment'),
        (94426, 'Arts & Entertainment', 'Books & Literature'),
        (94427, 'Arts & Entertainment', 'Celebrity Fan/Gossip'),
        (94428, 'Arts & Entertainment', 'Fine Art'),
        (94429, 'Arts & Entertainment', 'Humor'),
        (94430, 'Arts & Entertainment', 'Movies'),
        (94431, 'Arts & Entertainment', 'Music'),
        (94432, 'Arts & Entertainment', 'Television'),
        (94433, 'Automotive'),
        (94434, 'Automotive', '4-Wheel Drive/SUVs'),
        (94435, 'Automotive', 'Auto Parts'),
        (94436, 'Automotive', 'Auto Repair'),
        (94437, 'Automotive', 'Buying/Selling Cars'),
        (94438, 'Automotive', 'Car Culture'),
        (94439, 'Automotive', 'Certified Pre-Owned'),
        (94440, 'Automotive', 'Convertible'),
        (94441, 'Automotive', 'Coupe'),
        (94442, 'Automotive', 'Crossover'),
        (94443, 'Automotive', 'Diesel'),
        (94444, 'Automotive', 'Electric Vehicles'),
        (94445, 'Automotive', 'Hatchback'),
        (94446, 'Automotive', 'Hybrid'),
        (94447, 'Automotive', 'Luxury'),
        (94448, 'Automotive', 'MiniVan'),
        (94449, 'Automotive', 'Motorcycles'),
        (94450, 'Automotive', 'Off-Road Vehicles'),
        (94451, 'Automotive', 'Performance Vehicles'),
        (94452, 'Automotive', 'Pickup'),
        (94453, 'Automotive', 'Road-Side Assistance'),
        (94454, 'Automotive', 'Sedan'),
        (94455, 'Automotive', 'Trucks & Accessories'),
        (94456, 'Automotive', 'Vintage Cars'),
        (94457, 'Automotive', 'Wagon'),
        (94458, 'Business'),
        (94459, 'Business', 'Advertising'),
        (94460, 'Business', 'Agriculture'),
        (94461, 'Business', 'Biotech/Biomedical'),
        (94462, 'Business', 'Business Software'),
        (94463, 'Business', 'Construction'),
        (94464, 'Business', 'E-Commerce'),
        (94465, 'Business', 'Entrepreneurs'),
        (94466, 'Business', 'Financial Services'),
        (94467, 'Business', 'Forestry'),
        (94468, 'Business', 'Government'),
        (94469, 'Business', 'Graphic Design'),
        (94470, 'Business', 'Green Solutions'),
        (94471, 'Business', 'Human Resources'),
        (94472, 'Business', 'Logistics'),
        (94473, 'Business', 'Management'),
        (94474, 'Business', 'Marketing'),
        (94475, 'Business', 'Metals'),
        (94476, 'Business', 'Non-Profit Organizations'),
        (94477, 'Business', 'Power Industry'),
        (94478, 'Business', 'Public Services'),
        (94479, 'Business', 'Purchasing'),
        (94480, 'Business', 'Retail Industry'),
        (94481, 'Business', 'SOHO'),
        (94482, 'Business', 'Telecom'),
        (94495, 'Education'),
        (94496, 'Education', '7-12 Educators'),
        (94497, 'Education', 'Adult Education'),
        (94498, 'Education', 'Art History'),
        (94499, 'Education', 'College Admissions'),
        (94500, 'Education', 'College Life'),
        (94501, 'Education', 'Distance Learning'),
        (94502, 'Education', 'English as a 2nd Language'),
        (94503, 'Education', 'Graduate School'),
        (94504, 'Education', 'Homeschooling'),
        (94505, 'Education', 'Homework/Study Tips'),
        (94506, 'Education', 'K-6 Educators'),
        (94507, 'Education', 'Language Learning'),
        (94508, 'Education', 'Private School'),
        (94509, 'Education', 'Special Education'),
        (94510, 'Education', 'Studying Business'),
        (94511, 'Family & Parenting'),
        (94512, 'Family & Parenting', 'Adoption'),
        (94513, 'Family & Parenting', 'Babies & Toddlers'),
        (94514, 'Family & Parenting', 'Daycare/Pre-School'),
        (94515, 'Family & Parenting', 'Eldercare'),
        (94516, 'Family & Parenting', 'Family Internet'),
        (94517, 'Family & Parenting', 'Parenting - K-6 Kids'),
        (94518, 'Family & Parenting', 'Parenting Teens'),
        (94519, 'Family & Parenting', 'Pregnancy'),
        (94520, 'Family & Parenting', 'Special Needs Kids'),
        (94521, 'Food & Drink'),
        (94522, 'Food & Drink', 'American Cusine'),
        (94523, 'Food & Drink', 'Barbecues & Grilling'),
        (94524, 'Food & Drink', 'Cajun/Creole'),
        (94525, 'Food & Drink', 'Chinese Cuisine'),
        (94526, 'Food & Drink', 'Cocktails/Beer'),
        (94527, 'Food & Drink', 'Coffee/Tea'),
        (94528, 'Food & Drink', 'Cuisine-specific'),
        (94529, 'Food & Drink', 'Desserts & Baking'),
        (94530, 'Food & Drink', 'Dining Out'),
        (94531, 'Food & Drink', 'Food Allergies'),
        (94532, 'Food & Drink', 'Food Issues'),
        (94533, 'Food & Drink', 'French Cuisine'),
        (94534, 'Food & Drink', 'Health/LowFat Cooking'),
        (94535, 'Food & Drink', 'Italian Cuisine'),
        (94536, 'Food & Drink', 'Japanese Cuisine'),
        (94537, 'Food & Drink', 'Mexican Cuisine'),
        (94538, 'Food & Drink', 'Vegan'),
        (94539, 'Food & Drink', 'Vegetarian'),
        (94540, 'Food & Drink', 'Wine'),
        (94541, 'Health & Fitness'),
        (94542, 'Health & Fitness', 'A.D.D.'),
        (94543, 'Health & Fitness', 'AIDS/HIV'),
        (94544, 'Health & Fitness', 'Allergies'),
        (94545, 'Health & Fitness', 'Alternative Medicine'),
        (94546, 'Health & Fitness', 'Arthritis'),
        (94547, 'Health & Fitness', 'Asthma'),
        (94548, 'Health & Fitness', 'Autism/PDD'),
        (94549, 'Health & Fitness', 'Bipolar Disorder'),
        (94550, 'Health & Fitness', 'Brain Tumor'),
        (94551, 'Health & Fitness', 'Cancer'),
        (94552, 'Health & Fitness', 'Cholesterol'),
        (94553, 'Health & Fitness', 'Chronic Fatigue Syndrome'),
        (94554, 'Health & Fitness', 'Chronic Pain'),
        (94555, 'Health & Fitness', 'Cold & Flu'),
        (94556, 'Health & Fitness', 'Deafness'),
        (94557, 'Health & Fitness', 'Dental Care'),
        (94558, 'Health & Fitness', 'Depression'),
        (94559, 'Health & Fitness', 'Dermatology'),
        (94560, 'Health & Fitness', 'Diabetes'),
        (94561, 'Health & Fitness', 'Epilepsy'),
        (94562, 'Health & Fitness', 'Exercise'),
        (94563, 'Health & Fitness', 'GERD/Acid Reflux'),
        (94564, 'Health & Fitness', 'Headaches/Migraines'),
        (94565, 'Health & Fitness', 'Heart Disease'),
        (94566, 'Health & Fitness', 'Herbs for Health'),
        (94567, 'Health & Fitness', 'Holistic Healing'),
        (94568, 'Health & Fitness', 'IBS/Crohn\'s Disease'),
        (94569, 'Health & Fitness', 'Incest/Abuse Support'),
        (94570, 'Health & Fitness', 'Incontinence'),
        (94571, 'Health & Fitness', 'Infertility'),
        (94572, 'Health & Fitness', 'Men\'s Health'),
        (94573, 'Health & Fitness', 'Nutrition'),
        (94574, 'Health & Fitness', 'Orthopedics'),
        (94575, 'Health & Fitness', 'Panic/Anxiety Disorders'),
        (94576, 'Health & Fitness', 'Pediatrics'),
        (94577, 'Health & Fitness', 'Physical Therapy'),
        (94578, 'Health & Fitness', 'Psychology/Psychiatry'),
        (94579, 'Health & Fitness', 'Senior Health'),
        (94580, 'Health & Fitness', 'Sexuality'),
        (94581, 'Health & Fitness', 'Sleep Disorders'),
        (94582, 'Health & Fitness', 'Smoking Cessation'),
        (94583, 'Health & Fitness', 'Substance Abuse'),
        (94584, 'Health & Fitness', 'Thyroid Disease'),
        (94585, 'Health & Fitness', 'Weight Loss'),
        (94586, 'Health & Fitness', 'Women\'s Health'),
        (94587, 'Hobbies & Interests'),
        (94588, 'Hobbies & Interests', 'Art/Technology'),
        (94589, 'Hobbies & Interests', 'Arts & Crafts'),
        (94590, 'Hobbies & Interests', 'Beadwork'),
        (94591, 'Hobbies & Interests', 'Birdwatching'),
        (94592, 'Hobbies & Interests', 'BoardGames/Puzzles'),
        (94593, 'Hobbies & Interests', 'Candle & Soap Making'),
        (94594, 'Hobbies & Interests', 'Card Games'),
        (94595, 'Hobbies & Interests', 'Chess'),
        (94596, 'Hobbies & Interests', 'Cigars'),
        (94597, 'Hobbies & Interests', 'Collecting'),
        (94598, 'Hobbies & Interests', 'Comic Books'),
        (94599, 'Hobbies & Interests', 'Drawing/Sketching'),
        (94600, 'Hobbies & Interests', 'Freelance Writing'),
        (94601, 'Hobbies & Interests', 'Genealogy'),
        (94602, 'Hobbies & Interests', 'Getting Published'),
        (94603, 'Hobbies & Interests', 'Guitar'),
        (94604, 'Hobbies & Interests', 'Home Recording'),
        (94605, 'Hobbies & Interests', 'Inventors & Patents'),
        (94606, 'Hobbies & Interests', 'Jewelry Making'),
        (94607, 'Hobbies & Interests', 'Magic & Illusion'),
        (94608, 'Hobbies & Interests', 'Needlework'),
        (94609, 'Hobbies & Interests', 'Painting'),
        (94610, 'Hobbies & Interests', 'Photography'),
        (94611, 'Hobbies & Interests', 'Radio'),
        (94612, 'Hobbies & Interests', 'Roleplaying Games'),
        (94613, 'Hobbies & Interests', 'Sci-Fi & Fantasy'),
        (94614, 'Hobbies & Interests', 'Scrapbooking'),
        (94615, 'Hobbies & Interests', 'Screenwriting'),
        (94616, 'Hobbies & Interests', 'Stamps & Coins'),
        (94617, 'Hobbies & Interests', 'Video & Computer Games'),
        (94618, 'Hobbies & Interests', 'Woodworking'),
        (94619, 'Home & Garden'),
        (94620, 'Home & Garden', 'Appliances'),
        (94621, 'Home & Garden', 'Entertaining'),
        (94622, 'Home & Garden', 'Environmental Safety'),
        (94623, 'Home & Garden', 'Gardening'),
        (94624, 'Home & Garden', 'Home Repair'),
        (94625, 'Home & Garden', 'Home Theater'),
        (94626, 'Home & Garden', 'Interior Decorating'),
        (94627, 'Home & Garden', 'Landscaping'),
        (94628, 'Home & Garden', 'Remodeling & Construction'),
        (94629, 'Law, Gov\'t & Politics'),
        (94630, 'Law, Gov\'t & Politics', 'Commentary'),
        (94631, 'Law, Gov\'t & Politics', 'Immigration'),
        (94632, 'Law, Gov\'t & Politics', 'Legal Issues'),
        (94633, 'Law, Gov\'t & Politics', 'Politics'),
        (94634, 'Law, Gov\'t & Politics', 'U.S. Government Resources'),
        (94635, 'News'),
        (94636, 'News', 'International News'),
        (94637, 'News', 'Local News'),
        (94638, 'News', 'National News'),
        (94639, 'Personal Finance'),
        (94640, 'Personal Finance', 'Beginning Investing'),
        (94641, 'Personal Finance', 'Credit/Debt & Loans'),
        (94642, 'Personal Finance', 'Financial News'),
        (94643, 'Personal Finance', 'Financial Planning'),
        (94644, 'Personal Finance', 'Frugal Living'),
        (94645, 'Personal Finance', 'Hedge Fund'),
        (94646, 'Personal Finance', 'Insurance'),
        (94647, 'Personal Finance', 'Investing'),
        (94648, 'Personal Finance', 'Mutual Funds'),
        (94649, 'Personal Finance', 'Options'),
        (94650, 'Personal Finance', 'Retirement Planning'),
        (94651, 'Personal Finance', 'Stocks'),
        (94652, 'Personal Finance', 'Tax Planning'),
        (94653, 'Pets'),
        (94654, 'Pets', 'Aquariums'),
        (94655, 'Pets', 'Birds'),
        (94656, 'Pets', 'Cats'),
        (94657, 'Pets', 'Dogs'),
        (94658, 'Pets', 'Large Animals'),
        (94659, 'Pets', 'Reptiles'),
        (94660, 'Pets', 'Veterinary Medicine'),
        (94661, 'Real Estate'),
        (94662, 'Real Estate', 'Apartments'),
        (94663, 'Real Estate', 'Architects'),
        (94664, 'Real Estate', 'Buying/Selling Homes'),
        (94665, 'Religion and Spirituality'),
        (94666, 'Religion and Spirituality', 'Alternative Religions'),
        (94667, 'Religion and Spirituality', 'Atheism/Agnosticism'),
        (94668, 'Religion and Spirituality', 'Buddhism'),
        (94669, 'Religion and Spirituality', 'Catholicism'),
        (94670, 'Religion and Spirituality', 'Christianity'),
        (94671, 'Religion and Spirituality', 'Hinduism'),
        (94672, 'Religion and Spirituality', 'Islam'),
        (94673, 'Religion and Spirituality', 'Judaism'),
        (94674, 'Religion and Spirituality', 'Latter-Day Saints'),
        (94675, 'Religion and Spirituality', 'Pagan/Wiccan'),
        (94676, 'Science'),
        (94677, 'Science', 'Astrology'),
        (94678, 'Science', 'Biology'),
        (94679, 'Science', 'Botany'),
        (94680, 'Science', 'Chemistry'),
        (94681, 'Science', 'Geography'),
        (94682, 'Science', 'Geology'),
        (94683, 'Science', 'Paranormal Phenomena'),
        (94684, 'Science', 'Physics'),
        (94685, 'Science', 'Space/Astronomy'),
        (94686, 'Science', 'Weather'),
        (94687, 'Shopping'),
        (94688, 'Shopping', 'Comparison Engines'),
        (94689, 'Shopping', 'Contests & Freebies'),
        (94690, 'Shopping', 'Couponing'),
        (94691, 'Society'),
        (94692, 'Society', 'Dating'),
        (94693, 'Society', 'Divorce Support'),
        (94694, 'Society', 'Ethnic-specific'),
        (94695, 'Society', 'Gay Life'),
        (94696, 'Society', 'Marriage'),
        (94697, 'Society', 'Senior Living'),
        (94698, 'Society', 'Teens'),
        (94699, 'Society', 'Weddings'),
        (94700, 'Sports'),
        (94701, 'Sports', 'Auto Racing'),
        (94702, 'Sports', 'Baseball'),
        (94703, 'Sports', 'Bicycling'),
        (94704, 'Sports', 'Bodybuilding'),
        (94705, 'Sports', 'Boxing'),
        (94706, 'Sports', 'Canoeing/Kayaking'),
        (94707, 'Sports', 'Cheerleading'),
        (94708, 'Sports', 'Climbing'),
        (94709, 'Sports', 'Cricket'),
        (94710, 'Sports', 'Figure Skating'),
        (94711, 'Sports', 'Fly Fishing'),
        (94712, 'Sports', 'Football'),
        (94713, 'Sports', 'Freshwater Fishing'),
        (94714, 'Sports', 'Game & Fish'),
        (94715, 'Sports', 'Golf'),
        (94716, 'Sports', 'Horse Racing'),
        (94717, 'Sports', 'Horses'),
        (94718, 'Sports', 'Hunting/Shooting'),
        (94719, 'Sports', 'Inline Skating'),
        (94720, 'Sports', 'Martial Arts'),
        (94721, 'Sports', 'Mountain Biking'),
        (94722, 'Sports', 'NASCAR Racing'),
        (94723, 'Sports', 'Olympics'),
        (94724, 'Sports', 'Paintball'),
        (94725, 'Sports', 'Power & Motoryachts'),
        (94726, 'Sports', 'Pro Basketball'),
        (94727, 'Sports', 'Pro Ice Hockey'),
        (94728, 'Sports', 'Rodeo'),
        (94729, 'Sports', 'Rugby'),
        (94730, 'Sports', 'Running/Jogging'),
        (94731, 'Sports', 'Sailing'),
        (94732, 'Sports', 'Saltwater Fishing'),
        (94733, 'Sports', 'Scuba Diving'),
        (94734, 'Sports', 'Skateboarding'),
        (94735, 'Sports', 'Skiing'),
        (94736, 'Sports', 'Snowboarding'),
        (94737, 'Sports', 'Surfing/Bodyboarding'),
        (94738, 'Sports', 'Swimming'),
        (94739, 'Sports', 'Table Tennis/Ping-Pong'),
        (94740, 'Sports', 'Tennis'),
        (94741, 'Sports', 'Volleyball'),
        (94742, 'Sports', 'Walking'),
        (94743, 'Sports', 'Waterski/Wakeboard'),
        (94744, 'Sports', 'World Soccer'),
        (94745, 'Style & Fashion'),
        (94746, 'Style & Fashion', 'Accessories'),
        (94747, 'Style & Fashion', 'Beauty'),
        (94748, 'Style & Fashion', 'Body Art'),
        (94749, 'Style & Fashion', 'Clothing'),
        (94750, 'Style & Fashion', 'Fashion'),
        (94751, 'Style & Fashion', 'Jewelry'),
        (94752, 'Technology & Computing'),
        (94753, 'Technology & Computing', '3-D Graphics'),
        (94754, 'Technology & Computing', 'Animation'),
        (94755, 'Technology & Computing', 'Antivirus Software'),
        (94756, 'Technology & Computing', 'C/C++'),
        (94757, 'Technology & Computing', 'Cameras & Camcorders'),
        (94758, 'Technology & Computing', 'Cell Phones'),
        (94759, 'Technology & Computing', 'Computer Certification'),
        (94760, 'Technology & Computing', 'Computer Networking'),
        (94761, 'Technology & Computing', 'Computer Peripherals'),
        (94762, 'Technology & Computing', 'Computer Reviews'),
        (94763, 'Technology & Computing', 'Data Centers'),
        (94764, 'Technology & Computing', 'Databases'),
        (94765, 'Technology & Computing', 'Desktop Publishing'),
        (94766, 'Technology & Computing', 'Desktop Video'),
        (94767, 'Technology & Computing', 'Email'),
        (94768, 'Technology & Computing', 'Graphics Software'),
        (94769, 'Technology & Computing', 'Home Video/DVD'),
        (94770, 'Technology & Computing', 'Internet Technology'),
        (94771, 'Technology & Computing', 'Java'),
        (94772, 'Technology & Computing', 'JavaScript'),
        (94773, 'Technology & Computing', 'Linux'),
        (94774, 'Technology & Computing', 'Mac OS'),
        (94775, 'Technology & Computing', 'Mac Support'),
        (94776, 'Technology & Computing', 'MP3/MIDI'),
        (94777, 'Technology & Computing', 'Net Conferencing'),
        (94778, 'Technology & Computing', 'Net for Beginners'),
        (94779, 'Technology & Computing', 'Network Security'),
        (94780, 'Technology & Computing', 'Palmtops/PDAs'),
        (94781, 'Technology & Computing', 'PC Support'),
        (94782, 'Technology & Computing', 'Portable Entertainment'),
        (94783, 'Technology & Computing', 'Shareware/Freeware'),
        (94784, 'Technology & Computing', 'Unix'),
        (94785, 'Technology & Computing', 'Visual Basic'),
        (94786, 'Technology & Computing', 'Web Clip Art'),
        (94787, 'Technology & Computing', 'Web Design/HTML'),
        (94788, 'Technology & Computing', 'Web Search'),
        (94789, 'Technology & Computing', 'Windows'),
        (94790, 'Travel'),
        (94791, 'Travel', 'Adventure Travel'),
        (94792, 'Travel', 'Africa'),
        (94793, 'Travel', 'Air Travel'),
        (94794, 'Travel', 'Asia'),
        (94795, 'Travel', 'Australia & New Zealand'),
        (94796, 'Travel', 'Bed & Breakfasts'),
        (94797, 'Travel', 'Budget Travel'),
        (94798, 'Travel', 'Business Travel'),
        (94799, 'Travel', 'By US Locale'),
        (94800, 'Travel', 'Camping'),
        (94801, 'Travel', 'Canada'),
        (94802, 'Travel', 'Caribbean'),
        (94803, 'Travel', 'Cruises'),
        (94804, 'Travel', 'Eastern Europe'),
        (94805, 'Travel', 'Europe'),
        (94806, 'Travel', 'France'),
        (94807, 'Travel', 'Greece'),
        (94808, 'Travel', 'Honeymoons/Getaways'),
        (94809, 'Travel', 'Hotels'),
        (94810, 'Travel', 'Italy'),
        (94811, 'Travel', 'Japan'),
        (94812, 'Travel', 'Mexico & Central America'),
        (94813, 'Travel', 'National Parks'),
        (94814, 'Travel', 'South America'),
        (94815, 'Travel', 'Spas'),
        (94816, 'Travel', 'Theme Parks'),
        (94817, 'Travel', 'Traveling with Kids'),
        (94818, 'Travel', 'United Kingdom'),
    )

    for item in CONTEXTUAL:
        appnexus_id, parent_name = item[0], item[1]
        try:
            name = item[2]
        except IndexError:
            name = None
        parent, _ = TM.SegmentProximicContextual.objects.get_or_create(name=parent_name)  # noqa
        if not name:
            continue
        TM.SegmentProximicContextual.objects.get_or_create(
            appnexus_id=appnexus_id,
            name=name,
            parent=parent
        )


@pytest.fixture
def peer39_segments():
    segment_definitions = [
        (TM.Peer39PageLanguage, 'languages.csv'),
        (TM.Peer39ContextualSegment, 'segments.csv'),
        (TM.Peer39BrandProtection, 'brand_protection.csv'),
        (TM.Peer39PageQuality, 'page_quality.csv')
    ]

    for Segment, file_name in segment_definitions:
        segment_get = partial(Segment.objects.get)
        segment_create = partial(Segment.objects.create)

        with open(settings.PROJECT_DIR / "targeting" /
                  "csv" / "peer39" / file_name, 'rb') as csvfile:
            rows = csv.reader(csvfile, delimiter=';')
            rows.next()

            for row in rows:
                ids = row[:2]
                appnexus_id, peer39_id = ids
                segment_names = row[2:]
                parent_id = segment_names[0]
                segment_name = segment_names[-1]
                parent = None
                if parent_id:
                    try:
                        parent = segment_get(peer39_id=parent_id)
                        # Ignore more than 1 level of nesting
                        if parent.parent:
                            continue
                    except ObjectDoesNotExist:
                        continue

                segment = segment_create(name=segment_name,
                                         peer39_id=peer39_id, appnexus_id=appnexus_id)
                if parent:
                    segment.parent = parent
                    segment.save()


@pytest.fixture
def running_strategies():
    ''' Make existing strategies running '''

    # extend campaigns end date
    for campaign in Campaign.objects.all():
        campaign.end_UTC = datetime.utcnow() + timedelta(days=3)
        campaign.save()

    # audit creatives
    for creative in Creative.objects.all():
        creative.appnexus_set_audited()
        creative.save()

    # Add funds to account
    for account in Account.objects.all():
        Payment.objects.create(
            account=account,
            datetime=datetime.utcnow(),
            amount=10000
        )


@pytest.fixture
def fake_reports_data():
    ''' Simple metrics values for reports '''

    NOW = datetime.utcnow()
    YESTERDAY = NOW - timedelta(days=1)

    return (
        {
            'time': YESTERDAY.replace(hour=16),
            'data_cost_value': 10,
            'imp': 47,
            'imp_value': 120,
            'clk': 15,
            'conv': 5,
            'conv_value': 60,
        },
        {
            'time': YESTERDAY.replace(hour=19),
            'data_cost_value': 35,
            'imp': 30,
            'imp_value': 160,
            'clk': 80,
            'conv': 90,
            'conv_value': 7,
        },
        {
            'time': NOW.replace(hour=11),
            'data_cost_value': 7,
            'imp': 29,
            'imp_value': 80,
            'clk': 10,
            'conv': 2,
            'conv_value': 22,
        },
    )


def insert_fake_data_into_strategy_report(fake_report, increment_by=0):
    '''
    :param tuple fake_report: provided by fake_reports_data fixture
    :param int increment_by: increment fake data with this value
                             in each interation
    '''

    i = 0

    for strategy in Strategy.objects.all():

        for report in fake_report:

            ReportStrategy.objects.create(
                related=strategy,
                time=report['time'],
                imp=report['imp'] + i,
                imp_value=report['imp_value'] + i,
                clk=report['clk'] + i,
                conv=report['conv'] + i,
                conv_value=report['conv_value'] + i,
                data_cost_value=report['data_cost_value'] + i,
            )

        i += increment_by


@pytest.fixture
def fake_strategy_reports_inserter(fill_db, fake_reports_data):
    '''
    Inserting fake data for ReportStrategy
    '''

    insert_fake_data_into_strategy_report(fake_reports_data)


@pytest.fixture
def fake_strategy_reports_inserter_incremented(fill_db, fake_reports_data):
    '''
    Inserting fake data for ReportStrategy with incmenting in each interation
    '''

    insert_fake_data_into_strategy_report(fake_reports_data, increment_by=1)


@pytest.fixture
def fake_advert_reports_inserter(fake_reports_data):
    '''
    Inserting fake data for ReportAdvert
    '''

    for report in fake_reports_data:

        for advert in Advert.objects.all():
            ReportAdvert.objects.create(related=advert, **report)


@pytest.fixture
def fake_strategy_gender_reports_inserter(fill_db, fake_reports_data):
    '''
    Inserting fake data for ReportStrategyGender
    '''

    for dimension in list(TargetValue.objects.filter(category=dimensions.gender, representant__isnull=True)) + [None]:

        for strategy in Strategy.objects.all():

            for report in fake_reports_data:
                ReportStrategyGender.objects.get_or_create(
                    related=strategy,
                    dimension=dimension,
                    **report)


@pytest.fixture
def fake_strategy_domains_reports_inserter(fill_db, domains, fake_reports_data):
    '''
    Inserting fake data for ReportStrategyGender
    '''
    for campaign in Campaign.objects.all():

        for dimension in list(TargetValue.objects.filter(category=dimensions.domain)) + [None]:

            for report in fake_reports_data:

                ReportCampaignDomain.objects.create(
                    related=campaign,
                    dimension=dimension,
                    **report)


def insert_reports(model, related_object, repeat=20, dimension=None):
    '''
    Generating fake data for reports (for last 30 days).

    :param model: ReportStrategy or ReportAdvert
    :param related_object: Strategy or Advert instance
    '''

    delta = timedelta(
        days=1,
        minutes=15,
    )
    report_time = datetime.utcnow()
    for _ in range(20):
        report_time = report_time - delta
        imp = randint(100, randint(100, 9000))
        imp_value = randint(100, 10000)
        clk = randint(100, imp)
        conv = randint(1, clk)
        conv_value = conv * randint(1, 100)
        data_cost_value = randint(10, 100)
        report = model(
            time=report_time,
            imp_value=imp_value,
            imp=imp,
            clk=clk,
            conv=conv,
            conv_value=conv_value,
            data_cost_value=data_cost_value
        )
        if dimension:
            report.dimension = dimension
        report.related = related_object
        report.save()


def insert_strategy_targeting_reports(strategy):
    '''
    Generate fake reports for TargetValue, Proximic, Peer39, Publishers and ContentCategory related models.

    :param obj strategy: strategy object
    '''

    for model in [
        RM.ReportStrategyCountry,
        RM.ReportStrategyRegion,
        RM.ReportStrategyCity,
        RM.ReportStrategyOs,
        RM.ReportStrategyMake,
        RM.ReportStrategyModel,
        RM.ReportStrategyCarrier,
        RM.ReportStrategyDomain,
        RM.ReportStrategyPosition,
        RM.ReportStrategyAge,
        RM.ReportStrategyGender,
    ]:
        for dimension in list(
                TargetValue.objects.filter(category=model.dimension_hierarchy, representant=None)) + [None]:
            insert_reports(
                model,
                strategy,
                repeat=1,
                dimension=dimension
            )

    for dimension in ['http://foo.com', 'http://bar.net', 'http://baz.org', None]:
        insert_reports(
            RM.ReportStrategySite,
            strategy,
            repeat=1,
            dimension=dimension
        )

    for dimension_model, report_model in [
        (TM.PublisherTargetValue, RM.ReportStrategyPublisher),
        (TM.SegmentProximicMaturityRating, RM.ReportStrategyProximicMaturity),
        (TM.SegmentProximicSafetyLevel, RM.ReportStrategyProximicSafety),
        (TM.SegmentProximicPageQuality, RM.ReportStrategyProximicQuality),
        (TM.SegmentProximicPageNoticeability, RM.ReportStrategyProximicNotice),
        (TM.SegmentProximicPagePlacement, RM.ReportStrategyProximicPlace),
        (TM.SegmentProximicPageLanguage, RM.ReportStrategyProximicLanguage),
        (TM.Peer39PageLanguage, RM.ReportStrategyPeer39Language),
        (TM.Peer39BrandProtection, RM.ReportStrategyPeer39Brand),
    ]:
        for dimension in list(dimension_model.objects.all()) + [None]:
            insert_reports(
                report_model,
                strategy,
                repeat=1,
                dimension=dimension
            )

    for dimension_model, report_model in [
        (TM.ContentCategoryValue, RM.ReportStrategyCategory),
        (TM.SegmentProximicContextual, RM.ReportStrategyProximicContext),
        (TM.Peer39ContextualSegment, RM.ReportStrategyPeer39Contextual),
        (TM.Peer39PageQuality, RM.ReportStrategyPeer39Quality),
        (TM.LotameDemographic, RM.ReportStrategyLotameDemographic),
        (TM.LotameAdvancedDemographic, RM.ReportStrategyLotameAdvancedDemographic),
        (TM.LotameBehavioralInterest, RM.ReportStrategyLotameBehavioralInterest),
        (TM.LotameInfluencers, RM.ReportStrategyLotameInfluencers),
        (TM.LotameOffline, RM.ReportStrategyLotameOffline)
    ]:
        for dimension in list(dimension_model.objects.all()[:10]) + [None]:
            insert_reports(
                report_model,
                strategy,
                repeat=1,
                dimension=dimension
            )


@pytest.fixture
def fake_strategy_multiple_reports_inserter(
        fill_db_mobile_strategies,
        maturity_rating_segment, language_segment, page_quality_segment,
        page_placement_segment, page_noticeability_segment,
        proximic_contextual_segment, safety_level_segment,
        peer39_segments, lotame_segments, fake_strategy_reports_inserter,
        fake_advert_reports_inserter):
    '''
    Inserting fake data for all related to strategy reports
    '''

    strategy = Strategy.objects.all()[0]

    for advert in strategy.advert_set.all():
        insert_reports(ReportAdvert, advert)
    # other reports
    insert_reports(ReportStrategy, strategy)
    insert_strategy_targeting_reports(strategy)
