import urllib2
import os
import base64
import datetime
from uuid import uuid4
from adserving.types import Decimal
from shutil import copyfile

from django.db import transaction
from django.core.management.base import BaseCommand
from django.core import management
from django.conf import settings

from etc import dimensions, constants
from bidrequest.constants import EXCHANGES
from ui.account.models import Account, User, Payment
from ui.storage.models import CreativeImage, CreativeVideo, Audience
from ui.storage.states import LiverailStatus
from ui.campaign.models import (
    Campaign, Conversion, Strategy, SiteRatio, BiddingPeriod, Advert,
    AdvertPeriod, Site
)
from ui.targeting.models import PublisherTargetValue, TargetValue, TargetMap

from ui.targeting.appnexus import AppNexusSegment

from ui.notification.models import EventCategory
from ui.publishers.models import PublisherSet


@transaction.atomic
class Command(BaseCommand):
    help = """QA and dev command to insert example campaigns into database."""

    def download_placeholder(self, width, height, path):
        u = urllib2.urlopen('http://placehold.it/%sx%s' % (width, height))
        name = base64.urlsafe_b64encode(uuid4().bytes).replace('=', '')
        localFile = open(path + name + '.jpg', 'w')
        localFile.write(u.read())
        localFile.close()
        return name + '.jpg'

    def upload_video(self, creative_name, media_path):
        """Copy video creative to media root"""
        path_to_file_name = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), 'uploads', creative_name
            )
        )

        copyfile(
            path_to_file_name,
            os.path.join(media_path, creative_name)
        )

    # Targeting
    def setup_targetvalues(self, exchange):
        target_values = [
            [dimensions.g_location, 'USA'],
            [dimensions.g_location, 'USA', 'Ohio'],
            [dimensions.g_location, 'USA', 'Ohio', 'New Pittsburgh'],
            [dimensions.g_location, 'USA', 'Wisconsin'],
            [dimensions.g_location, 'USA', 'Wisconsin', 'New Richmond'],
            [dimensions.g_location, 'USA', 'New York'],
            [dimensions.g_location, 'USA', 'New York', 'New York'],
            [dimensions.g_os, 'Android'],
            [dimensions.g_os, 'Nokia OS'],
            [dimensions.g_os, 'Symbian'],
            [dimensions.g_device, 'Samsung'],
            [dimensions.g_device, 'Sony'],
            [dimensions.g_device, 'LG'],
            [dimensions.g_device, 'Samsung', 'Samsung Galaxy S'],
            [dimensions.g_device, 'Sony', 'Sony Xperia Z'],
            [dimensions.g_device, 'LG', 'Lg Swift L9'],
            [dimensions.carrier, 'WiFi'],
            [dimensions.carrier, '3G'],
            [dimensions.carrier, 'EDGE'],
            [dimensions.carrier, 'GPRS'],
            [dimensions.os_version, 'Samsung Galaxy S'],
            [dimensions.os_version, 'v11 beta']
        ]

        for row in target_values:
            category, values = row[0], row[1:]
            value = TargetMap.pack(values)
            TargetValue.objects.get_or_create(exchange=exchange, category=category, value=value)

    def handle(self, *args, **options):

        self.stdout.write('Filling campaigns with fake data')

        # Account
        a, _ = Account.objects.get_or_create(
            name='Test account',
            timezone='UTC',
        )

        u, _ = User.objects.get_or_create(
            username='kanary',
            email='test@clearcode.cc',
            account=a,
            is_signup_complete=True
        )
        u.set_password('kanary')
        u.save()

        account2, _ = Account.objects.get_or_create(
            name='Gravity4 DSP',
            timezone='UTC',
        )

        gravity_u, _ = User.objects.get_or_create(
            username='gravity',
            email='gravity@clearcode.cc',
            account=a,
            is_signup_complete=True
        )
        gravity_u.set_password('gravity')
        gravity_u.save()

        admin, _ = User.objects.get_or_create(
            username='admin',
            email='thearoom@clearcode.cc',
            account=a,
            is_signup_complete=True,
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        admin.set_password('admin')
        admin.save()

        # Events

        EventCategory.objects.get_or_create(name='Basic information')
        EventCategory.objects.get_or_create(name='Warnings')

        # Creatives
        path = os.path.join(settings.MEDIA_ROOT, 'creatives', '')

        if not os.path.exists(path):
            os.makedirs(path)

        image_name = self.download_placeholder(125, 125, path)
        co1, _ = CreativeImage.objects.get_or_create(
            name='Image One',
            owner=a,
            width=125,
            height=125,
            defaults={'image': "creatives/%s" % image_name},
            appnexus_status='a',
        )

        image_name = self.download_placeholder(125, 125, path)
        co2, _ = CreativeImage.objects.get_or_create(
            name='Image 2',
            owner=a,
            width=125,
            height=125,
            defaults={'image': "creatives/%s" % image_name},
            appnexus_status='a'
        )

        image_name = self.download_placeholder(125, 125, path)
        co3, _ = CreativeImage.objects.get_or_create(
            name='Image Three',
            owner=a,
            width=125,
            height=125,
            defaults={'image': "creatives/%s" % image_name},
            appnexus_status='p',
            appnexus_audit_blocked_no_funds=True
        )

        image_name = self.download_placeholder(125, 125, path)
        co4, _ = CreativeImage.objects.get_or_create(
            name='Image rejected',
            owner=a,
            width=125,
            height=125,
            appnexus_status='r',
            defaults={'image': "creatives/%s" % image_name},
        )
        image_name = self.download_placeholder(125, 125, path)
        co5, _ = CreativeImage.objects.get_or_create(
            name='Image expired',
            owner=a,
            width=125,
            height=125,
            appnexus_status='e',
            defaults={'image': "creatives/%s" % image_name},
        )

        co6, _ = CreativeImage.objects.get_or_create(
            name='Image audited',
            owner=a,
            width=125,
            height=125,
            appnexus_status='a',
            defaults={'image': "creatives/%s" % image_name},
        )

        # Video
        video_name = 'video_creative.mpg'
        self.upload_video(video_name, path)

        video1, _ = CreativeVideo.objects.get_or_create(
            name='video_active',
            owner=a,
            width=480,
            height=720,
            file='creatives/%s' % video_name,
            liverail_id=214900,  # Real uploaded video on LiveRail. Features a lovely shell session.
            duration=10,
            media_variants=[  # Real liverail-converted media.
                {
                    u'bitrate': 736,
                    u'duration': 10,
                    u'height': 360,
                    u'type': u'video/mp4',
                    u'url': u'http://cdn.liverail.com/adasset4/62531/64866/214900/lo.mp4',
                    u'width': 480
                }, {
                    u'bitrate': 1472,
                    u'duration': 10,
                    u'height': 480,
                    u'type': u'video/mp4',
                    u'url': u'http://cdn.liverail.com/adasset4/62531/64866/214900/me.mp4',
                    u'width': 640
                }, {
                    u'bitrate': 3072,
                    u'duration': 10,
                    u'height': 720,
                    u'type': u'video/mp4',
                    u'url': u'http://cdn.liverail.com/adasset4/62531/64866/214900/hi.mp4',
                    u'width': 960
                }, {
                    u'bitrate': 736,
                    u'duration': 10,
                    u'height': 360,
                    u'type': u'video/webm',
                    u'url': u'http://cdn.liverail.com/adasset4/62531/64866/214900/lo.webm',
                    u'width': 480
                }, {
                    u'bitrate': 1472,
                    u'duration': 10,
                    u'height': 480,
                    u'type': u'video/webm',
                    u'url': u'http://cdn.liverail.com/adasset4/62531/64866/214900/me.webm',
                    u'width': 640
                }, {
                    u'bitrate': 3072,
                    u'duration': 10,
                    u'height': 720,
                    u'type': u'video/webm',
                    u'url': u'http://cdn.liverail.com/adasset4/62531/64866/214900/hi.webm',
                    u'width': 960
                }, {
                    u'bitrate': 736,
                    u'duration': 10,
                    u'height': 360,
                    u'type': u'video/x-flv',
                    u'url': u'http://cdn.liverail.com/adasset4/62531/64866/214900/lo.flv',
                    u'width': 480
                }, {
                    u'bitrate': 1472,
                    u'duration': 10,
                    u'height': 480,
                    u'type': u'video/x-flv',
                    u'url': u'http://cdn.liverail.com/adasset4/62531/64866/214900/me.flv',
                    u'width': 640
                }, {
                    u'bitrate': 3072,
                    u'duration': 10,
                    u'height': 720,
                    u'type': u'video/x-flv',
                    u'url': u'http://cdn.liverail.com/adasset4/62531/64866/214900/hi.flv',
                    u'width': 960
                }, {
                    u'bitrate': 736,
                    u'duration': 10,
                    u'height': 360,
                    u'type': u'video/x-ms-wmv',
                    u'url': u'http://cdn.liverail.com/adasset4/62531/64866/214900/lo.wmv',
                    u'width': 480
                }, {
                    u'bitrate': 1472,
                    u'duration': 10,
                    u'height': 480,
                    u'type': u'video/x-ms-wmv',
                    u'url': u'http://cdn.liverail.com/adasset4/62531/64866/214900/me.wmv',
                    u'width': 640
                }, {
                    u'bitrate': 3072,
                    u'duration': 10,
                    u'height': 720,
                    u'type': u'video/x-ms-wmv',
                    u'url': u'http://cdn.liverail.com/adasset4/62531/64866/214900/hi.wmv',
                    u'width': 960
                }
            ]
        )
        # set required liverail status, which gets set to pending by post_save signal
        video1.liverail_status = LiverailStatus.active
        video1.save()

        video2, _ = CreativeVideo.objects.get_or_create(
            name='video_pending',
            owner=a,
            file='creatives/%s' % video_name,
            liverail_status=LiverailStatus.pending
        )

        # Audiences
        audience1, _ = Audience.objects.get_or_create(
            name="First audience",
            owner=a
        )
        audience2, _ = Audience.objects.get_or_create(
            name="Second audience",
            owner=a
        )

        # Sites
        site, _ = Site.objects.get_or_create(
            owner=a,
            url='http://www.onet.pl'
        )
        Site.objects.get_or_create(
            owner=a,
            url='http://www.wp.pl'
        )
        Site.objects.get_or_create(
            owner=a,
            url='http://www.google.com'
        )

        # Campaigns

        now = datetime.datetime.utcnow()
        campaign_1, _ = Campaign.objects.get_or_create(
            account=a,
            name='Test Campaign One',
            budget_total=Decimal('8000.'),
            landing_site=site,
            id_random='0',
            defaults={
                'start_UTC': now - datetime.timedelta(days=10),
                'end_UTC': now + datetime.timedelta(days=5)
            }
        )

        campaign_2, _ = Campaign.objects.get_or_create(
            account=a,
            name='Test Campaign Two',
            budget_total=Decimal('8000.'),
            landing_site=site,
            id_random='1',
            defaults={
                'start_UTC': now - datetime.timedelta(days=2),
                'end_UTC': now + datetime.timedelta(days=30)
            }
        )

        campaign_3, _ = Campaign.objects.get_or_create(
            account=a,
            name='Test Campaign Three',
            budget_total=Decimal('8000.'),
            landing_site=site,
            id_random='2',
            defaults={
                'start_UTC': now + datetime.timedelta(days=2),
                'end_UTC': now + datetime.timedelta(days=300)
            }
        )

        conversion_1, _ = Conversion.objects.get_or_create(
            campaign=campaign_1)

        conversion_2, _ = Conversion.objects.get_or_create(
            campaign=campaign_2)

        conversion_3, _ = Conversion.objects.get_or_create(
            campaign=campaign_3)

        nexage = EXCHANGES.nexage
        smaato = EXCHANGES.smaato
        appnexus = EXCHANGES.appnexus

        strategy_1, _ = Strategy.objects.get_or_create(
            campaign=campaign_1,
            name='Test Strategy One',
            id_random='0',

            defaults={
                'budget_total': Decimal('1000.'),
                'budget_bid_CPM': Decimal('2'),
                'is_day_parted': True
            }
        )

        site_ratio, _ = SiteRatio.objects.get_or_create(
            site=Site.objects.all()[1],
            ratio=1,
            custom_variable='?test=2',
        )

        site_ratio_2, _ = SiteRatio.objects.get_or_create(
            site=Site.objects.all()[1],
            ratio=1,
            custom_variable='?test=3',
        )

        strategy_1.landing_sites.add(site_ratio, site_ratio_2)

        strategy_2, _ = Strategy.objects.get_or_create(
            campaign=campaign_2,
            name='Test Strategy Two',
            type=Strategy.MOBILE,
            defaults={
                'budget_total': Decimal('1200.'),
                'budget_daily': Decimal('120.'),
                'budget_bid_CPM': Decimal('5'),
                'id_random': '1',
            }
        )

        strategy_2_2, _ = Strategy.objects.get_or_create(
            campaign=campaign_2,
            name='Test Strategy Two II',
            defaults={
                'budget_total': Decimal('1500.'),
                'budget_daily': Decimal('150.'),
                'budget_bid_CPM': Decimal('5'),
                'id_random': '1_1',
            }
        )

        strategy_2.landing_sites.add(site_ratio, site_ratio_2)

        strategy_2_2.landing_sites.add(site_ratio, site_ratio_2)

        strategy_3, _ = Strategy.objects.get_or_create(
            campaign=campaign_3,
            name='Test Strategy Three',
            type=Strategy.MOBILE,
            defaults={
                'budget_total': Decimal('2500.'),
                'budget_daily': Decimal('300.'),
                'budget_bid_CPM': Decimal('3'),
                'id_random': '2',
            }
        )

        strategy_3.landing_sites.add(site_ratio, site_ratio_2)

        Payment.objects.create(
            account=a,
            datetime=datetime.datetime.utcnow(),
            amount=5000
        )

        Payment.objects.create(
            account=a,
            datetime=datetime.datetime.utcnow(),
            amount=700
        )

        # Bidding periods

        time1 = datetime.time(14, 30)
        time2 = datetime.time(16, 0)

        biddingperiod_1, _ = BiddingPeriod.objects.get_or_create(
            strategy=strategy_1,
            start=time1,
            end=time2
        )

        adverts_str_1 = [
            Advert.objects.create(
                strategy=strategy_1,
                creative=co1,
                landing_site=site,
                custom_variable='?test=%s' % n,
                id_random=str(n)
            ) for n in range(11)
        ]

        adverts_str_2 = [
            Advert.objects.create(
                strategy=strategy_2,
                creative=co2,
                landing_site=site,
                custom_variable='?test=%s' % n,
                id_random=str(n)
            ) for n in range(11, 13)
        ]

        adverts_str_2_2 = [
            Advert.objects.create(
                strategy=strategy_2_2,
                creative=co2,
                landing_site=site,
                custom_variable='?test=%s' % n,
                id_random=str(n)
            ) for n in range(13, 15)
        ]

        adverts_str_3 = [
            Advert.objects.create(
                strategy=strategy_3,
                creative=co3,
                landing_site=site,
                custom_variable='?test=%s' % n,
                id_random=str(n)
            ) for n in range(16, 20)
        ]

        adverts = adverts_str_1 + adverts_str_2 + adverts_str_2_2 + adverts_str_3

        creative_period_1, _ = AdvertPeriod.objects.get_or_create(
            advert=adverts[0],
            period=biddingperiod_1,
            custom_bid_CPM=2,
        )

        # Targeting
        self.setup_targetvalues(nexage)

        # publishers
        segments = [
            (95002, 'Brand Protection Data::Non-standard Content::Alcohol (proximic)'),
            (94999, 'Brand Protection Data::Non-standard Content::Adult (proximic)'),
            (94435, 'Automotive::Auto Parts (proximic)'),
        ]

        for segment in segments:
            AppNexusSegment.objects.create(
                appnexus_id=segment[0],
                name=segment[1]
            )

        publisherset_app, _ = PublisherSet.objects.get_or_create(
            owner=a, name='Awsome app publishers', inventory='app'
        )
        publisherset_web, _ = PublisherSet.objects.get_or_create(
            owner=a, name='Awsome web publishers', inventory='site'
        )

        publishers = [
            [dimensions.g_publisher, appnexus,
                ('Application', 'Rubicon'),
                ('app', '23'),
                ['720x90', '50x50'],
                ['below', 'above']],
            [dimensions.g_publisher, appnexus,
                ('Web', 'Rubicon'),
                ('site', '23'),
                ['720x100', '640x80'],
                ['above']],
            [dimensions.g_publisher, smaato,
                ('Web', 'Smaato'),
                ('site', constants.SMAATO_NETWORK_ID),
                ['720x100', '640x80'], [1]],
            [dimensions.g_publisher, smaato,
                ('Application', 'Smaato'),
                ('app', constants.SMAATO_NETWORK_ID),
                ['340x50'], [2]],
            [dimensions.g_publisher, nexage,
                ('Application', 'Nexage'),
                ('app', constants.NEXAGE_NETWORK_ID),
                ['340x50'], [1]],
            [dimensions.g_publisher, nexage,
                ('Web', 'Nexage'),
                ('site', constants.NEXAGE_NETWORK_ID),
                ['560x50'], [2]],
            [dimensions.g_publisher, appnexus,
                ('Application', 'Rubicon', 'Ninja Fruit'),
                ('app', '23', 'Ninja Fruit'),
                ['800x100', '640x80'],
                ['above']],
            [dimensions.g_publisher, appnexus,
                ('Web', 'Rubicon', 'rafalmichal.com'),
                ('site', '23', 'rafalmichal.com'),
                ['80x30'],
                ['below']],
            [dimensions.g_publisher, nexage,
                ('Application', 'Nexage', 'Ninja Fruit'),
                ('app', constants.NEXAGE_NETWORK_ID, 'Ninja Fruit'),
                ['640x80'], [2]],
            [dimensions.g_publisher, nexage,
                ('Web', 'Nexage', 'rafalmichal.com'),
                ('site', constants.NEXAGE_NETWORK_ID, 'rafalmichal.com'),
                ['450x80'], [3]],
            [dimensions.g_publisher, smaato,
                ('Application', 'Smaato', 'Ninja Fruit'),
                ('app', constants.SMAATO_NETWORK_ID, 'Ninja Fruit'),
                ['640x80'], [2]],
            [dimensions.g_publisher, smaato,
                ('Web', 'Smaato', 'rafalmichal.com'),
                ('site', constants.SMAATO_NETWORK_ID, 'rafalmichal.com'),
                ['450x80'], [3]],
        ]

        for row in publishers:
            category, exchange, values, representant_values, sizes, positions = row
            value = TargetMap.pack(values)
            target, _ = PublisherTargetValue.objects.get_or_create(
                exchange=exchange,
                category=category,
                value=value
            )

            if representant_values:
                # add restrictions
                segment = AppNexusSegment.objects.brand_protection().order_by('?')[0]
                target.sizes = sizes
                target.positions = positions
                target.save()
                target.segments.add(segment)

                PublisherTargetValue.objects.create_value_with_representant(
                    representant_values, target)

            if target.key == dimensions.network:
                continue

            if target.inventory_key == 'app':
                publisherset_app.target_values.add(target)
            else:
                publisherset_web.target_values.add(target)

        # domains
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
                exchange=appnexus,
                category=dimensions.domain,
                value=domain
            )

        management.call_command('rebuild_index', interactive=False)
