from datetime import time, datetime, timedelta
from ui.storage.models import DESTINATION, Brand
from ui.tests.initial_datafixtures import default_fb_pages

from ui.tests.utils import appnexus_id_seq

from ui.tests.utils import copy_creative_to_media_root


def create_campaign(name, budget_total, landing_site):
    '''Creates campaign for given name
    Args:
        name - name of campaign
    Returns:
        campaign object'''
    from ui.campaign.models import Campaign
    from ui.account.models import Account

    account = Account.objects.all()[0]
    campaign = Campaign.objects.create(
        name=name,
        budget_total=budget_total,
        start_UTC=datetime.utcnow() - timedelta(days=1),
        end_UTC=datetime.utcnow() + timedelta(days=3),
        landing_site=landing_site,
        account=account)
    return campaign


def create_strategy(campaign, name, budget_total, landing_page, exchange,
                    budget_daily=None, bid_cpm=None, targeting=None):
    '''Creates strategy object
    Args:
        campaign - parent campaign
        name - name of strategy
        budget - total budget of strategy
        targeting - list of targeting values for which we generate random data/
            assigments.
        bid_cpm - (optional) value of custom bid CPM
    Returns:
        Strategy objects
    '''
    from ui.campaign.models import Strategy, SiteRatio


    bid_cpm = bid_cpm or budget_total / 1000
    targeting = targeting or ()
    if not exchange == 'facebook':

        strategy = Strategy.objects.create(campaign=campaign, name=name,
                                           budget_daily=budget_daily,
                                           budget_total=budget_total,
                                           budget_bid_CPM=bid_cpm)
    else:
        strategy = Strategy.objects.create(campaign=campaign, name=name,
                                           budget_daily=budget_daily,
                                           budget_total=budget_total,
                                           budget_bid_CPM=bid_cpm,
                                           type=u'fb')

    for relation_name, model, data_sets in targeting:
        for data_set, include in data_sets:
            if not include:
                manager_name = relation_name + '_exclude'
            else:
                manager_name = relation_name
            manager = getattr(strategy, manager_name)
            instance, _ = model.objects.get_or_create(**data_set)
            manager.add(instance)
    site_ratio = SiteRatio.objects.create(site=landing_page)
    strategy.landing_sites.add(site_ratio)
    return strategy


def create_landing_site(url=None):
    from ui.campaign.models import Site
    from ui.account.models import Account

    account = Account.objects.all()[0]
    site = Site.objects.create(url=url, owner=account)
    return site

def create_fbx_page(page_name, page_id, brand_id):
    from ui.account.models import Account
    owner = Account.objects.all()[0]
    fbx_page = Brand.objects.create(page_name=page_name, thirdparty_page_id=page_id, brand_id=brand_id, owner=owner)
    return fbx_page


def create_advert(strategy, landing_site, bid, creative_type, custom_variable=None):
    '''Creates advert for given strategy
    Args:
        strategy - parent strategy of advert
        custom_variable - optional custom variable of advert
        bid - optional custom bid CPM
    Returs:
        advert object'''
    from ui.campaign.models import Advert
    from ui.storage.models import CreativeImage

    image_name = 'creatives/kitteh.jpg'

    copy_creative_to_media_root(creative_name=image_name)

    advert = None
    if creative_type == 'default':
        creative = CreativeImage.objects.create(owner=landing_site.owner,
                                                image=image_name,
                                                width=728,
                                                height=90,
                                                name='Appnexus creative')

        advert = Advert.objects.create(strategy=strategy,
                                       creative=creative,
                                       landing_site=landing_site,
                                       custom_variable=custom_variable,
                                       custom_bid_CPM=bid)

    elif creative_type == 'facebook_sidebar':
        creative = CreativeImage.objects.create(owner=landing_site.owner,
                                                image=image_name,
                                                width=254,
                                                height=133,
                                                destination=u'fs',
                                                title='fb_creative',
                                                body='fb_creative_body',
                                                name='Facebook_sidebar')
    elif creative_type == 'facebook_newsfeed':
        creative = CreativeImage.objects.create(owner=landing_site.owner,
                                                image=image_name,
                                                width=200,
                                                height=200,
                                                destination=u'fn',
                                                title='fnf_creative',
                                                body='fnf_creative_body',
                                                message='fnf_message',
                                                name='Facebook_newsfeed',
                                                brand=Brand.objects.all()[0])
    else:
        raise NotImplementedError

    if creative_type == 'facebook_sidebar' or creative_type == 'facebook_newsfeed':
        advert = Advert.objects.create(strategy=strategy,
                               creative=creative,
                               custom_variable=custom_variable,
                               custom_bid_CPM=bid)
    if advert is None:
        raise IncorrectCreativeTypeException('Creative type is {0}'.format(creative_type))
    return advert


class IncorrectCreativeTypeException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
       return repr(self.value)

def create_advertperiod(advert, start, end, bid):
    '''Creates advert period from given parameters and assigns to advert
    Args:
        advert - parent advert
        start - start time in format 12:30
        end - end time in format 13:00
        bid - optional value of custom bids for period
    Returns:
        Created advert period object'''
    from ui.campaign.models import BiddingPeriod, AdvertPeriod

    tstart = time(*map(int, start.split(':')))
    tend = time(*map(int, end.split(':')))
    biddingperiod = BiddingPeriod.objects.create(start=tstart, end=tend,
                                                 strategy=advert.strategy)
    advertperiod = AdvertPeriod.objects.create(period=biddingperiod,
                                               advert=advert,
                                               custom_bid_CPM=bid)
    return advertperiod


def advertperiod_generator(test_data):
    '''Creates strategies with advert periods from test_data'''
    landing_site = create_landing_site('http://google.pl')
    for i, (exchange, start, end, targeting_keys) in enumerate(test_data):
        campaign = create_campaign('Campaign day parting %s' % i, 1234,
                                   landing_site)
        strategy = create_strategy(campaign, 'Strategy day parting %s' % i,
                                   1234, landing_site,
                                   targeting=targeting_keys)
        advert = create_advert(strategy, landing_site, 1234)
        advertperiod = create_advertperiod(advert, start, end, 12)
        yield advertperiod, strategy


def advert_generator(test_data, noaudit=False):
    '''Creates strategies without advert periods from test_data'''
    landing_site = create_landing_site('http://google.pl')
    for i, (exchange, start, end, targeting_keys, creative_type) in enumerate(test_data):
        campaign = create_campaign('Campaing day parting %s' % i, 1234,
                           landing_site)
        strategy = create_strategy(campaign, 'Strategy day parting %s' % i,
                                   1234, landing_site, exchange,
                                   targeting=targeting_keys)
        advert = create_advert(strategy, landing_site, None, creative_type)
        #we need add capping for facebook campaign, without it no user id matching while bid request will happened
        if not noaudit:
            advert.creative.appnexus_id = appnexus_id_seq.next()
            advert.creative.save()
            advert.creative.appnexus_set_audited()
            advert.creative.update_status = True
            advert.creative.save(update_fields=['appnexus_status'])
        yield advert, strategy

def fbx_page_generator(fbx_page_dictionary=default_fb_pages):
    for fbx_page in fbx_page_dictionary:
        fbx_page = create_fbx_page(fbx_page['page_name'], fbx_page['thirdparty_page_id'], fbx_page['brand_id'])
        yield fbx_page

