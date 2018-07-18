'''Various functions connected with testing ui modules and django'''
import os
import json
import shutil
from datetime import time, timedelta, datetime
from collections import defaultdict
from functools import partial

from shutil import copyfile

from tests.api_mocks import appnexus_id_seq
from ui.storage.models import Brand, Creative
from ui.tests.initial_datafixtures import (
    date_format,
    default_account, default_audiences, default_campaign, default_creative,
    default_creative_flash, default_creative_video, default_strategies, default_user,
    default_landing_page, default_segments, default_adverts, default_invoices,
    default_payments, default_app_publishers, default_site_publishers,
    default_network_publishers,
    default_fbx_creative, default_fb_pages, default_news_feed_creative)
from django.conf import settings


DEFAULT_CID = None


def assert_dict_values(dict_, **kwargs):
    '''
    Checks if values in dict_ are valid with given values in kwargs.
    Args:
        dict_ - dict with values to validate
        **kwargs - keys are mapped to dict_ keys, values are asserted with
        values from dict_
    Returns:
        Rases AssertionException if given value not match with value in dict_
    '''
    for name, value in kwargs.iteritems():
        assert(dict_[name] == value)


def ajax_request(client, url, data, method):
    '''
        Returns resource code, with resource data

        :param client: app client
        :param str url: url to call for data
        :param str method: HTTP metod name lowercase
        :param object data: data to send in request

        :returns: tuple (status_code, laoded_data)
    '''
    client_method = getattr(client, method)
    extra_kwargs = {}
    if data:
        extra_kwargs = {
            'data': json.dumps(data),
            'content_type': 'application/json'
        }
    res = client_method(url, **extra_kwargs)

    content = None
    if res.content:
        content = json.loads(res.content)

    return res.status_code, content


get_resource = partial(ajax_request, data=None, method='get')


put_resource = partial(ajax_request, method='put')


def audit_creative(creative):
    creative.appnexus_set_audited()
    creative.appnexus_id = appnexus_id_seq.next()
    creative.save()


dtformat = '%Y-%m-%dT%H:%M'


def copy_creative_to_media_root(file_name="creative.jpg",
                                creative_name="creatives/test_creative.jpg"):
    """
    Copy image from uploads to our media tmp files (creatives).

    :param str file_name:
    :param str creative_name:
    :rtype: None
    :returns: None
    """
    path_to_file_name = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), 'uploads', file_name
        )
    )

    copyfile(
        path_to_file_name,
        settings.MEDIA_ROOT / creative_name
    )


class DatabaseDataFactory(object):

    '''
        Creates database for tests, filling it with required values
    '''

    def __init__(self):
        from django.test import Client
        self.models = defaultdict(dict)
        self.client = Client()

    def setup_accounts(self, accounts=default_account):
        '''
        Adds accounts according to passed list of dicts:
        [{name:, timezone:}, ]
        '''
        from ui.account.models import Account

        for account_dict in accounts:
            # if we will not copy, certain keys will get overridden for
            # duration of the test suite, not only test function
            account_dict = account_dict.copy()
            account = Account.objects.create(**account_dict)

            self.models['account'][account.name] = account
        return self.models['account']

    def setup_users(self, users=default_user):
        '''
        Adds users according to list of dicts:
        [{username:, email:, password:, account:}, ]
        '''
        from ui.account.models import User

        for user_dict in users:
            # if we will not copy, certain keys will get overridden for
            # duration of the test suite, not only test function
            user_dict = user_dict.copy()

            user = User.objects.create(
                account=self.models['account'][user_dict['account']],
                username=user_dict['username'],
                email=user_dict['email'],
                is_signup_complete=user_dict['is_signup_complete'],
            )
            user.set_password(user_dict['password'])

            user.save()

            self.models['user'][user.username] = user


    def setup_creatives(self, model, call_on_creative, creatives):
        """
        Generic method which setups creatives.
        :param django.db.Model model: Creative model e.g. CreativeImage, CreativeFlash
        :param callable call_on_creative: callable which can be used for specific operation
        to given creative type like copying files etc.
        :param list creative: list of dictionaries with data which are passed to the
        constructor of model.
        """
        for creative_dict in creatives:
            creative_dict = creative_dict.copy()
            owner = self.models['account'][creative_dict['owner']]
            call_on_creative(creative_dict)
            creative_dict['owner'] = owner
            creative = model.objects.create(**creative_dict)

            self.models['creative'][creative.name] = creative

    def setup_creative_images(self, creatives=default_creative):
        '''
        Sets creative images media based on passed list of dicts
        [{'name': , 'owner': , 'width': , 'height': , 'image': }]

        owner key is account object's name attribute value to be assigned
        '''
        from ui.storage.models import CreativeImage

        def copy_creative(creative_dict):
            copy_creative_to_media_root(creative_name=creative_dict['image'])
        self.setup_creatives(CreativeImage, copy_creative, creatives)

    def setup_creative_fbx(self, creatives=default_fbx_creative):
        self.setup_creative_images(creatives)

    def setup_creative_fbx_news_feed(self, creatives=default_news_feed_creative):
        self.setup_creative_images(creatives)
        for creative in self.models['creative'].values():
            if creative.destination == u'fn':
                creative.brand = Brand.objects.all()[0]
                creative.save()

    def setup_creative_flash(self, creatives=default_creative_flash):
        '''
        Sets creative flash media based on passed list of dicts
        [{'name': , 'owner': , 'width': , 'height': , 'image': }]

        owner key is account object's name attribute value to be assigned
        '''

        from ui.storage.models import CreativeFlash

        def copy_creative(creative_dict):
            copy_creative_to_media_root(
                file_name="creative.swf",
                creative_name=creative_dict["file"],
            )
        self.setup_creatives(CreativeFlash, copy_creative, creatives)

    def setup_creative_videos(self, creatives=default_creative_video):
        '''
        Sets creative video based on passed list of dicts
        [{'name': , 'owner': , 'width': , 'height': , 'file': }]

        owner key is account object's name attribute value to be assigned
        '''
        from ui.storage.models import CreativeVideo

        def copy_creative(creative_dict):
            copy_creative_to_media_root(
                file_name="creative.mpg",
                creative_name=creative_dict["file"],
            )
        self.setup_creatives(CreativeVideo, copy_creative, creatives)

    def setup_fbx_pages(self, fbx_pages=default_fb_pages):
        for fbx_page_dict in fbx_pages:
            fbx_page_dict = fbx_page_dict.copy()
            owner = self.models['account'][fbx_page_dict['owner']]
            fbx_page_dict['owner'] = owner
            fbx_page = Brand.objects.create(**fbx_page_dict)

            self.models['brand'][fbx_page.page_name] = fbx_page
    def setup_landing_pages(self, sites=default_landing_page):
        '''
        Adds landing pages according to passed params in a given format:
        [{'name': , 'owner': , 'url': },]
        owner is a name of account that is set up in self.models dict
        '''
        from ui.campaign.models import Site

        for site_dict in sites:
            site_dict = site_dict.copy()
            owner = self.models['account'][site_dict['owner']]
            site_dict['owner'] = owner
            Site.objects.create(**site_dict)

    def setup_campaigns(self, campaigns=default_campaign):
        '''
        Adds campaign according to passed params in a given format:
        [{'name': ,'account': , 'budget_total': , 'start_UTC': , 'end_UTC': ,
                                        'landing_site': }]
        account is a name of account that is set up in self.models dict
        landing_site is a name of landing site defined in self.models
        start/end_UTC is a datestring in YYYY-MM-DDTHH:mm format
        '''
        from ui.campaign.models import Campaign, Site

        for campaign_dict in campaigns:
            campaign_dict = campaign_dict.copy()

            campaign_dict['account'] =\
                self.models['account'][campaign_dict['account']]
            campaign_dict['landing_site'] = Site.objects.get(
                url=campaign_dict['landing_site'],
                owner=campaign_dict['account'])
            campaign_dict['start_UTC'] =\
                datetime.strptime(campaign_dict['start_UTC'], date_format)
            campaign_dict['end_UTC'] =\
                datetime.strptime(campaign_dict['end_UTC'], date_format)

            campaign = Campaign.objects.create(**campaign_dict)

            self.models['campaign'][campaign.name] = campaign

    def setup_campaigns_running(self, campaigns=default_campaign):
        ''' Adds campaigns that are are running (scheduled for now) '''
        yesterday = datetime.utcnow() - timedelta(days=1)
        next_week = datetime.utcnow() + timedelta(days=7)
        for campaign in campaigns:
            campaign['start_UTC'] = yesterday.strftime(dtformat)
            campaign['end_UTC'] = next_week.strftime(dtformat)

        return self.setup_campaigns(campaigns)

    def setup_strategies(self, strategies=default_strategies):
        '''
        adds strategies based on params:
        [{'name': , 'campaign': ,'budget_total': , 'budget_bid_CPM': },]
        '''
        from ui.campaign.models import Strategy, SiteRatio

        for strategy_dict in strategies:
            strategy_dict = strategy_dict.copy()
            strategy_dict['campaign'] =\
                self.models['campaign'][strategy_dict['campaign']]
            strategy = Strategy.objects.create(**strategy_dict)

            # add landing site
            landing_site = SiteRatio.objects.create(
                site=strategy.campaign.landing_site,
            )
            strategy.landing_sites.add(landing_site)

            self.models['strategy'][strategy.name] = strategy

    def setup_bidding_periods(self):
        ''' adding 2 bidding periods '''
        from ui.campaign.models import BiddingPeriod

        bidding_period_citrus = BiddingPeriod.objects.create(
            start=time(13, 45),
            end=time(16, 30),
            strategy=self.models['strategy']['Hello this is Citrus']
        )
        self.models['bidding_period']['citrus'] = bidding_period_citrus

        bidding_period_veg = BiddingPeriod.objects.create(
            start=time(10, 0),
            end=time(13, 15),
            strategy=self.models['strategy']['han i has a pumpkin?']
        )
        self.models['bidding_period']['veg'] = bidding_period_veg

    def setup_adverts(self, adverts=default_adverts):
        from ui.campaign.models import Advert, Site

        advert_objects = []
        for advert in adverts:
            strategy = self.models['strategy'][advert['strategy']]
            ad = Advert.objects.create(
                strategy=strategy,
                creative=self.models['creative'][advert['creative']],
                landing_site=Site.objects.get(
                    url=advert['url'],
                    owner=strategy.campaign.account
                ),
                is_default=advert.get('is_default', True)
            )
            self.models['advert'][advert['name']] = ad
            advert_objects.append(ad)
        return advert_objects

    def setup_targetvalues(self, targetvalues, targetvalue_class=None):
        '''
        Setup targetingValues for given base class

        :param list targetvalues: list of dictionaries
            [{
                'category': some_category_name,
                'exchange': exchange_instance,
                'values': ('aaa', 'bb'),
                'represented_values': ('foo', 'bar')
            },]
            represented_values can be optional.

            .. note::

                 represented_values will equal values this should create
                 unmoderated targetvalues

                 dictionaries without represented_values will result in self
                 representant
                 other case will create standard representant/represented
                 element

        :param class targetvalue_class: class type that will be used to create
            TargetValue. Default will result in TargetValue being used

        '''

        from ui.targeting.models import TargetValue, TargetMap
        if not targetvalue_class:
            targetvalue_class = TargetValue

        created = []
        for row in targetvalues:
            value = TargetMap.pack(row['values'])
            target, _ = targetvalue_class.objects.get_or_create(
                exchange=row['exchange'],
                category=row['category'],
                value=value
            )

            if row.get('represented_values'):
                targetvalue_class.objects.create_value_with_representant(
                    row['represented_values'], target)
            created.append(target)

        return created

    def setup_audiences(self, audiences=default_audiences):
        from ui.storage.models import Audience

        for audience_dict in audiences:
            audience_dict = audience_dict.copy()
            owner = self.models['account'][audience_dict['owner']]

            audience_dict['owner'] = owner
            Audience.objects.create(**audience_dict)

    def setup_publisherset(self, publisherset):
        from ui.publishers.models import PublisherSet

        new_publisherset, _ = PublisherSet.objects.get_or_create(
            owner=self.models['account'][publisherset['owner']],
            inventory=publisherset['inventory'],
            name=publisherset['name']
        )

        return new_publisherset

    def setup_publishers(self, site_publishers=default_site_publishers,
                         app_publishers=default_app_publishers,
                         network_publishers=default_network_publishers):
        from ui.targeting.models import PublisherTargetValue

        publishers_site = self.setup_targetvalues(site_publishers,
                                                  PublisherTargetValue)

        publishers_app = self.setup_targetvalues(app_publishers,
                                                 PublisherTargetValue)

        publishers_network = self.setup_targetvalues(
            network_publishers,
            PublisherTargetValue)

        return (publishers_app, publishers_site, publishers_network)

    def setup_segments(self, segments=default_segments):
        '''
        Creates 2 proximic segments, by default: one with brand protection
        and one only with the category
        '''
        from ui.targeting.appnexus import AppNexusSegment

        for segment in segments:
            AppNexusSegment.objects.create(
                appnexus_id=segment['appnexus_id'],
                name=segment['name']
            )

    def setup_payments(self, payments=default_payments):
        from ui.account.models import Payment

        for payment_dict in payments:
            Payment.objects.create(
                account=self.models['account'][payment_dict['account']],
                datetime=datetime.strptime(payment_dict['datetime'],
                                           date_format),
                amount=payment_dict['amount']
            )

    def setup_invoices(self, invoices=default_invoices):
        from ui.account.models import Invoice

        for invoice_dict in invoices:
            invoice_path = settings.INVOICES_DIR / invoice_dict['pdf']
            shutil.copyfile(settings.PROJECT_DIR / 'tests' / 'uploads' / invoice_dict['pdf'], invoice_path)

            Invoice.objects.create(
                account=self.models['account'][invoice_dict['account']],
                datetime=datetime.strptime(invoice_dict['datetime'],
                                           date_format),
                number=invoice_dict['number'],
                amount=invoice_dict['amount'],
                pdf=invoice_path
            )
