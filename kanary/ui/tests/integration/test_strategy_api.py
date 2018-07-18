from decimal import Decimal
import json
import random

import pytest

from ui.tests.utils import get_resource, put_resource
from ui.tests.initial_datafixtures import default_user
from ui.account.models import User
from ui.campaign.models import Campaign, Strategy, SiteRatio
from ui.campaign.api import Targeting
from ui.publishers.models import PublisherSet
from ui.targeting.models import (
    LotameDemographic,
    LotameAdvancedDemographic,
    LotameBehavioralInterest,
    LotameInfluencers,
    LotameOffline
)


@pytest.mark.django_db
def test_strategy_add_publisherset_api(client, strategies_publisherset,
                                       search_engine):
    '''
    Check if adding a valid publisherset through API returns an error.
    '''

    client.login(
        username=default_user[0]['username'],
        password=default_user[0]['password']
    )

    strategy = Strategy.objects.first()

    strategy_url = '/api/strategy/{0}/'.format(strategy.id)
    status, strategy_data = get_resource(client, strategy_url)

    assert status == 200
    assert 'publisherset' in strategy_data
    assert not strategy_data['publisherset']

    publisherset = PublisherSet.objects.get(owner=strategy.campaign.account)

    # add publisherset to strategy
    strategy_data['publisherset'] = publisherset.id

    res = client.put(strategy_url,
                     data=json.dumps(strategy_data),
                     content_type='application/json')

    strategy_edited_data = json.loads(res.content)

    assert res.status_code == 201
    assert strategy_edited_data['publisherset'] == publisherset.id

    strategy = Strategy.objects.get(pk=strategy_edited_data['id'])

    assert strategy.publisherset == publisherset


def test_advert_tracking_validation(client, video_creative_db):
    '''
    Check if accessing strategy detail view by slug filters content by owner.
    '''

    client.login(
        username=default_user[0]['username'],
        password=default_user[0]['password']
    )

    strategy = Strategy.objects.get(name='Hello this is Citrus')

    # GET strategy
    strategy_url = '/api/strategy/{0}/'.format(strategy.id)
    status, strategy_data = get_resource(client, strategy_url)
    assert status == 200

    # PUT with data from get
    status, saved_data = put_resource(client, strategy_url, strategy_data)
    assert status == 201
    assert saved_data == strategy_data

    image_ad, video_ad = strategy_data['adverts']

    # One ad can't have both tracking methods
    image_ad['custom_pixel'] = 'http://www.google.com/'
    image_ad['js_code'] = 'console.log("sth");'

    # Video ads can't have JS tracked
    video_ad['js_code'] = 'console.log("sth");'

    # Try to save incorrect strategy
    status, put_response = put_resource(client, strategy_url, strategy_data)
    assert status == 400
    VALIDATION_ERRORS = {
        'adverts_video': 'Cannot add JS tracker to video creative.',
        'adverts': 'Cannot add both pixel and JS code tracker.'
    }
    assert put_response['strategy'] == VALIDATION_ERRORS


@pytest.fixture()
def duplicate_campaign_strategy_names_db(user_db):
    """
    Database setup with two campaigns with same slug and two strategies with
    the same slug, owned by different users.
    """

    setup = user_db
    setup.setup_creative_images()
    setup.setup_landing_pages()

    campaigns = [
        {
            'name': 'Campaign One', 'account': 'acc',
            'budget_total': 8000, 'start_UTC': '2013-01-01T00:00',
            'end_UTC': '2013-01-31T00:00',
            'landing_site': 'http://www.google.com/'
        },
        {
            'name': 'Campaign One', 'account': 'acc_2',
            'budget_total': 6000, 'start_UTC': '2014-01-01T00:00',
            'end_UTC': '2014-01-31T00:00',
            'landing_site': 'http://www.python.org/'
        }
    ]

    setup.setup_campaigns(campaigns)

    strategies = [
        {'name': 'Strategy One', 'campaign': 'Campaign One', 'account': 'acc',
         'budget_total': 8000, 'budget_bid_CPM': Decimal('0.1')},
        {'name': 'Strategy One', 'campaign': 'Campaign One', 'account': 'acc_2',
         'budget_total': 4321, 'budget_bid_CPM': Decimal('0.1')}
    ]

    for strategy_dict in strategies:
        strategy_dict['campaign'] = Campaign.objects.get(
            name=strategy_dict['campaign'],
            account=setup.models['account'].get(strategy_dict['account'])
        )

        del strategy_dict['account']
        strategy = Strategy.objects.create(**strategy_dict)

        # add landing site
        landing_site = SiteRatio.objects.create(
            site=strategy.campaign.landing_site,
        )
        strategy.landing_sites.add(landing_site)

        setup.models['strategy'][strategy.name] = strategy

    return setup


def test_account_filtering_strategy(client, duplicate_campaign_strategy_names_db):
    '''
    Check if accessing strategy detail view by slug filters content by owner.
    '''

    user = User.objects.get(username=default_user[0]['username'])
    account = user.account

    client.login(
        username=default_user[0]['username'],
        password=default_user[0]['password']
    )

    strategy = Strategy.objects.get(campaign__account=account)

    strategy_url = '/api/strategy/s/{0}/'.format(strategy.slug)
    status, strategy_data = get_resource(client, strategy_url)

    assert status == 200
    assert strategy_data['id'] == strategy.id

    # Check chart resource
    chart_url = '/report_chart/Strategy/{0}/'.format(strategy.slug)
    chart_url += '?start_date=22-07-2014&end_date=22-07-2014&chart_metric=imp&dim=advert'
    status, chart_data = get_resource(client, chart_url)

    assert status == 200


def test_account_filtering_campaign(client, duplicate_campaign_strategy_names_db):
    '''
    Check if accessing campaign detail view by slug filters content by owner.
    '''

    user = User.objects.get(username=default_user[0]['username'])
    account = user.account

    client.login(
        username=default_user[0]['username'],
        password=default_user[0]['password']
    )

    campaign = Campaign.objects.get(account=account)

    campaign_url = '/api/campaign/s/{0}/'.format(campaign.slug)
    status, campaign_data = get_resource(client, campaign_url)

    assert status == 200
    assert campaign_data['id'] == campaign.id

    # Check chart resource
    chart_url = '/report_chart/Campaign/{0}/'.format(campaign.slug)
    chart_url += '?start_date=22-07-2014&end_date=22-07-2014&chart_metric=imp&dim=strategy'
    status, chart_data = get_resource(client, chart_url)

    assert status == 200


@pytest.fixture
def segments_db(user_db, lotame_segments):
    """Fixture with example lotame segments"""

    setup = user_db
    setup.setup_landing_pages()
    setup.setup_campaigns()
    setup.setup_strategies()

    return setup


@pytest.mark.parametrize(('SegmentModel, mapping, strategy_include_field, strategy_exclude_field'),
                         (
                                 (LotameDemographic, Targeting.LOTAME_DEMOGRAPHIC_FIELDS_MAPPING,
                                  'segment_lotame_demographic', 'segment_lotame_demographic_exclude'),
                                 (LotameAdvancedDemographic, Targeting.LOTAME_ADVANCED_DEMOGRAPHIC_FIELDS_MAPPING,
                                  'segment_lotame_advanced_demographic', 'segment_lotame_advanced_demographic_exclude'),
                                 (LotameBehavioralInterest, Targeting.LOTAME_BEHAVIORAL_FIELDS_MAPPING,
                                  'segment_lotame_behavioral_interest', 'segment_lotame_behavioral_interest_exclude'),
                                 (LotameInfluencers, Targeting.LOTAME_INFLUENCERS_MAPPING,
                                  'segment_lotame_influencers', 'segment_lotame_influencers_exclude'),
                                 (LotameOffline, Targeting.LOTAME_OFFLINE_MAPPING,
                                  'segment_lotame_offline', 'segment_lotame_offline_exclude')
                         )
)
def test_lotame_segment_saving(client, segments_db, SegmentModel, mapping,
                               strategy_include_field, strategy_exclude_field):
    """Check if lotame segments are correctly saved with strategy"""

    (api_include_field, _), (api_exclude_field, _) = mapping

    client.login(
        username=default_user[0]['username'],
        password=default_user[0]['password']
    )

    strategy = Strategy.objects.first()

    # GET strategy
    strategy_url = '/api/strategy/{0}/'.format(strategy.id)
    status, strategy_data = get_resource(client, strategy_url)
    assert status == 200

    # Do something with data
    random_segments = random.sample(SegmentModel.objects.all(), 6)
    included_segments = random_segments[:3]
    excluded_segments = random_segments[3:]

    def get_id_and_name(segment):
        return {'id': segment.id, 'name': segment.name}

    strategy_data[api_include_field] = map(get_id_and_name, included_segments)
    strategy_data[api_exclude_field] = map(get_id_and_name, excluded_segments)

    status, saved_data = put_resource(client, strategy_url, strategy_data)
    assert status == 201
    assert sorted(saved_data[api_include_field]) == sorted(strategy_data[api_include_field])
    assert sorted(saved_data[api_exclude_field]) == sorted(strategy_data[api_exclude_field])

    db_included_segments = getattr(strategy, strategy_include_field).all().values_list('id', flat=True)
    db_excluded_segments = getattr(strategy, strategy_exclude_field).all().values_list('id', flat=True)

    assert sorted(db_included_segments) == sorted(s.id for s in included_segments)
    assert sorted(db_excluded_segments) == sorted(s.id for s in excluded_segments)
