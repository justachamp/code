import pytest
import shutil
from django.core.management import call_command

from ui.tests.utils import audit_creative
from ui.tests.initial_datafixtures import inactive_user


@pytest.fixture
def search_engine(request):
    call_command('rebuild_index', interactive=False)

    def clear():
        call_command('clear_index', interactive=False)
    request.addfinalizer(clear)


@pytest.fixture
def user_db(request, transactional_db):
    '''Initializes database with user data'''
    from ui.tests.utils import DatabaseDataFactory

    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()

    return setup


@pytest.fixture
def creative_images(user_db):
    setup = user_db
    setup.setup_creative_images()


@pytest.fixture
def video_creative_db(user_db, creative_images):
    ''' Fixture with active campaigns, strategies and adverts '''

    setup = user_db
    setup.setup_landing_pages()
    setup.setup_campaigns()
    setup.setup_strategies()
    setup.setup_creative_videos()
    adverts = [
        {
            'name': 'creative_image_1',
            'strategy': 'Hello this is Citrus',
            'creative': 'creative_image_1',
            'url': 'http://www.google.com/',
        },
        {
            'name': 'creative_video_1',
            'strategy': 'Hello this is Citrus',
            'creative': 'creative_video_1',
            'url': 'http://www.google.com/',
        },
    ]
    setup.setup_adverts(adverts)

    return setup


@pytest.fixture
def clean_strategy(user_db):
    """Strategy with no targeting set"""
    from datetime import datetime, timedelta

    from ui.account.models import Account
    from ui.campaign.models import Campaign, Strategy, Site, SiteRatio

    acc = Account.objects.first()
    site = Site.objects.create(
        url='http://www.python.org',
        owner=acc,
    )
    campaign = Campaign.objects.create(
        account=Account.objects.first(),
        name='Test Campaign',
        start_UTC=datetime.utcnow() - timedelta(days=7),
        end_UTC=datetime.utcnow() + timedelta(days=7),
        budget_total=1000,
        landing_site=site,
    )
    strategy = Strategy.objects.create(
        name='Test Strategy',
        campaign=campaign,
        budget_total=800,
        budget_bid_CPM=1
    )
    site_ratio = SiteRatio.objects.create(site=campaign.landing_site)
    strategy.landing_sites.add(site_ratio)
    return strategy


@pytest.fixture
def inactive_user_db(request, transactional_db):
    '''
    Initializes database with user data.
    :returns: saved user instance.
    '''
    from ui.tests.utils import DatabaseDataFactory

    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users(inactive_user)

    return setup


@pytest.fixture
def running_app(user_db, creative_images):
    ''' Fixture with active campaigns, strategies and adverts '''

    from ui.campaign.models import Advert

    setup = user_db
    setup.setup_landing_pages()
    setup.setup_campaigns_running()
    setup.setup_strategies()
    setup.setup_adverts()
    setup.setup_payments()

    # Fake creative audit
    for ad in Advert.objects.all():
        audit_creative(ad.creative)

    return setup


@pytest.fixture(autouse=True, scope="session")
def remove_media_root(request):
    """
    Remove media root directory after tests.
    """
    from django.conf import settings as django_settings

    request.addfinalizer(
        lambda: shutil.rmtree(django_settings.MEDIA_ROOT, ignore_errors=True)
    )


@pytest.fixture
def lotame_segments(user_db):
    """Create sample segments for all Lotame segment models"""
    from ui.targeting import models as TM

    id_seq = 1
    for SegmentModel in [TM.LotameDemographic, TM.LotameAdvancedDemographic,
            TM.LotameBehavioralInterest, TM.LotameInfluencers, TM.LotameOffline]:
        for _ in range(10):
            SegmentModel.objects.create(appnexus_id=id_seq, lotame_id=id_seq, name='Segment %s' % id_seq)
            id_seq += 1
