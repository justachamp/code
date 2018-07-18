from decimal import Decimal
from datetime import date, datetime

import pytest
from django.core import mail
from mock import call, patch

from etc.constants import AUDIT_FEE
from adserving.bidder.appnexus_api import AppCreativeTemplate
from tests.api_mocks import appnexus_id_seq
from ui.account.models import Payment
from ui.campaign.models import Advert, Site
from ui.storage.models import Creative, CreativeImage, Brand
from ui.storage.tasks import send_for_audit
from ui.bidding_spendings.models import DailySpendings
from ui.notification.models import Event
from ui.storage.tasks import (appnexus_update_status_all,
                              update_video_creative_media)
from ui.storage.states import CreativeState
from ui.tests.utils import DatabaseDataFactory, copy_creative_to_media_root
from ui.tests.integration.test_mailing import is_email_sent


default_payments = [
    {'account': 'acc', 'datetime': '2014-02-10T00:00', 'amount': 2}
]


@pytest.fixture
def audit_app(request, basic_fixture):
    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()
    setup.setup_fbx_pages()
    setup.setup_landing_pages()
    setup.setup_campaigns()
    setup.setup_strategies()
    setup.setup_creative_images()
    setup.setup_creative_fbx()
    setup.setup_creative_fbx_news_feed()
    setup.setup_creative_flash()
    setup.setup_creative_videos()
    setup.setup_payments(default_payments)
    return setup


liverail_login = patch('apis.liverail.LiveRailAPI.login')
liverail_logout = patch('apis.liverail.LiveRailAPI.logout')
liverail_creative_status = patch('apis.liverail.LiveRailAPI.creative_status', return_value='active')


@pytest.mark.django_db
@pytest.mark.fbx
@pytest.mark.parametrize('creative_name, creative_template', [
    ('creative_fbx_1', AppCreativeTemplate.fb_sidebar_image),
    ('creative_fbx_2', AppCreativeTemplate.fb_sidebar_image),
    ('creative_fbx_news_feed_1', AppCreativeTemplate.fb_newsfeed_image),
    ('creative_fbx_news_feed_2', AppCreativeTemplate.fb_newsfeed_image),
    ('creative_fbx_news_feed_3', AppCreativeTemplate.fb_newsfeed_image),
    ('creative_fbx_news_feed_4', AppCreativeTemplate.fb_newsfeed_image)
])
def test_creative_size_for_fbx_creatives(audit_app, appnexus_api_auditing, cdn_api, creative_name, creative_template):
    creative = audit_app.models['creative'][creative_name]
    if creative.destination == u'fs':
        assert creative.width == 254
        assert creative.height == 133
    else:
        if creative.height == creative.width:
            assert creative.width == 200
        else:
            assert creative.width == 470
            assert creative.height == 246


@pytest.mark.django_db
@pytest.mark.fbx
@pytest.mark.parametrize('creative_name', [
    # ('creative_image_1'),
    # ('creative_flash_1'),
    # ('creative_video_2'),
    # ('creative_video_2'),
    # ('creative_video_2'),
    ('creative_fbx_1'),
    ('creative_fbx_news_feed_1')
])
def test_data_for_facebook_audit(audit_app, appnexus_api_auditing, cdn_api, creative_name):
    creative = audit_app.models['creative'][creative_name]
    if creative.destination == u'd':
        assert creative.data_for_facebook_audit == {}
    elif creative.destination == u'fs':
        assert creative.data_for_facebook_audit == {
            'title': creative.title,
            'body': creative.body,
            'landing_page': creative.landing_site_url
        }
    else:
        assert creative.data_for_facebook_audit == {
            'title': creative.title,
            'body': creative.body,
            'landing_page': creative.landing_site_url,
            'domain': creative.domain,
            'message': creative.message,
            'brand_id': creative.brand.brand_id,
            'thirdparty_page_id': creative.brand.thirdparty_page_id
        }


@pytest.mark.django_db
@pytest.mark.fbx
@pytest.mark.parametrize('creative_name, creative_template, duration', [
    ('creative_image_1', AppCreativeTemplate.image, 0),
    ('creative_flash_1', AppCreativeTemplate.flash, 0),
    ('creative_video_2', AppCreativeTemplate.video_vast_15s, 15),
    ('creative_video_2', AppCreativeTemplate.video_vast_30s, 30),
    ('creative_video_2', AppCreativeTemplate.video_vast_other, 100),
    ('creative_fbx_1', AppCreativeTemplate.fb_sidebar_image, 0),
    ('creative_fbx_news_feed_1', AppCreativeTemplate.fb_newsfeed_image, 0)
])
def test_audit_tasks_execution(audit_app, appnexus_api_auditing,
                               cdn_api, creative_name,
                               creative_template,
                               duration):
    '''
    Checks if creation of Advert has a side effect in calling cdn
    and AppNexus API.
    '''
    medias = [{'duration': duration, 'width': 400, 'height': 300, 'type': 'video/flv', 'url': 'http://example.com'}]
    liverail_list_video_assets = patch('apis.liverail.LiveRailAPI.list_video_assets', return_value=medias)

    appnexus_api = appnexus_api_auditing
    creative = audit_app.models['creative'][creative_name]
    if creative.destination == u'd':
        strategy = audit_app.models['strategy']['Hello this is Citrus']
    else:
        strategy = audit_app.models['strategy']['FBX']
    with liverail_login, liverail_creative_status, liverail_list_video_assets, liverail_logout:
        update_video_creative_media()

    creative = Creative.objects.get(pk=creative.pk)
    advert = Advert.objects.create(
        strategy=strategy,
        creative=creative,
        landing_site=Site.objects.get(url='http://www.google.com/',
                                      owner=strategy.campaign.account)
    )

    send_for_audit()

    creative = Creative.objects.get(pk=creative.pk)

    upload_call = call(creative.pk, creative.contents)

    creative_call = call.creative(creative.appnexus_id)
    audit_creative_call = call.audit_creative(None, creative.id_random,
                                              creative.width, creative.height, creative_template,
                                              creative.appnexus_media_url, creative.type != 'Video',
                                              creative.data_for_facebook_audit)

    assert upload_call in cdn_api.mock_calls
    assert appnexus_api.mock_calls == [audit_creative_call, creative_call]

    appnexus_api.mock_calls = []
    cdn_api.mock_calls = []

    advert.is_default = True
    advert.save()

    # changing advert shouldn't send creative for audit
    assert appnexus_api.mock_calls == []

    creative.name += '[updated]'
    creative.save()

    # changing creative name shoudn't send it for audit
    assert appnexus_api.mock_calls == []
    assert cdn_api.mock_calls == []


def set_creative_as_audited(creative):
    creative.appnexus_set_audited()
    creative.appnexus_id = appnexus_id_seq.next()
    creative.update_status = True
    creative.to_audit = False
    creative.save()


@pytest.mark.django_db
@pytest.mark.fbx
@pytest.mark.parametrize('creative_name, strategy_name, creative_template', [
    ('creative_image_1', 'Hello this is Citrus', AppCreativeTemplate.image),
    ('creative_fbx_1', 'FBX', AppCreativeTemplate.fb_sidebar_image),
    ('creative_fbx_news_feed_1', 'FBX', AppCreativeTemplate.fb_newsfeed_image),
    ('creative_fbx_news_feed_2', 'FBX', AppCreativeTemplate.fb_newsfeed_image)
])
def test_creatives_is_send_to_audit_when_image_is_changed(cdn_api, audit_app, appnexus_api_auditing, creative_name,
                                                          strategy_name, creative_template):
    appnexus_api = appnexus_api_auditing

    creative = audit_app.models['creative'][creative_name]
    strategy = audit_app.models['strategy'][strategy_name]
    landing = Site.objects.get(url='http://www.google.com/',
                               owner=strategy.campaign.account)

    Advert.objects.create(strategy=strategy, creative=creative,
                          landing_site=landing)

    # reset mock calls set by saving advert
    appnexus_api.mock_calls = []
    cdn_api.mock_calls = []

    set_creative_as_audited(creative)

    creative_image = 'creatives/test_creative_2.jpg'
    copy_creative_to_media_root(creative_name=creative_image)

    creative = Creative.objects.get(pk=creative.pk)
    creative.image = creative_image

    creative.save()

    upload_call = call.delay(
        creative.pk,
        creative.contents
    )

    assert upload_call in cdn_api.mock_calls

    send_for_audit()

    creative_call = call.creative(Creative.objects.filter(name=creative_name)[0].appnexus_id)
    audit_creative_call = \
        call.audit_creative(creative.appnexus_id, creative.id_random, creative.width, creative.height,
                            creative_template, creative.appnexus_media_url,
                            creative.type != 'Video', creative.data_for_facebook_audit)

    assert creative_call in appnexus_api.mock_calls
    assert audit_creative_call in appnexus_api.mock_calls


@pytest.mark.django_db
@pytest.mark.fbx
@pytest.mark.parametrize('creative_name, strategy_name, creative_template, duration', [
    ('creative_image_1', 'Hello this is Citrus', AppCreativeTemplate.image, 0),
    ('creative_flash_1', 'Hello this is Citrus', AppCreativeTemplate.flash, 0),
    ('creative_video_2', 'Hello this is Citrus', AppCreativeTemplate.video_vast_15s, 15),
    ('creative_fbx_1', 'FBX', AppCreativeTemplate.fb_sidebar_image, 0),
    ('creative_fbx_news_feed_1', 'FBX', AppCreativeTemplate.fb_newsfeed_image, 0),
    ('creative_fbx_news_feed_2', 'FBX', AppCreativeTemplate.fb_newsfeed_image, 0)
])
def test_creatives_is_not_sent_to_audit_when_name_is_changed(cdn_api, audit_app, appnexus_api_auditing, creative_name,
                                                             strategy_name, creative_template, duration):
    medias = [{'duration': duration, 'width': 400, 'height': 300, 'type': 'video/flv', 'url': 'http://example.com'}]
    liverail_list_video_assets = patch('apis.liverail.LiveRailAPI.list_video_assets', return_value=medias)

    appnexus_api = appnexus_api_auditing
    creative = audit_app.models['creative'][creative_name]
    if creative.destination == u'd':
        strategy = audit_app.models['strategy']['Hello this is Citrus']
    else:
        strategy = audit_app.models['strategy']['FBX']
    with liverail_login, liverail_creative_status, liverail_list_video_assets, liverail_logout:
        update_video_creative_media()

    strategy = audit_app.models['strategy'][strategy_name]
    landing = Site.objects.get(url='http://www.google.com/',
                               owner=strategy.campaign.account)

    Advert.objects.create(strategy=strategy, creative=creative,
                          landing_site=landing)

    # reset mock calls set by saving advert
    appnexus_api.mock_calls = []
    cdn_api.mock_calls = []

    set_creative_as_audited(creative)

    creative = Creative.objects.get(pk=creative.pk)
    creative.name = 'New name'
    creative.save()

    send_for_audit()

    assert appnexus_api.mock_calls == []
    assert appnexus_api.mock_calls == []


@pytest.mark.django_db
@pytest.mark.fbx
@pytest.mark.parametrize('creative_name, strategy_name, creative_template', [
    ('creative_image_1', 'Hello this is Citrus', AppCreativeTemplate.image),
    ('creative_fbx_1', 'FBX', AppCreativeTemplate.fb_sidebar_image),
    ('creative_fbx_news_feed_1', 'FBX', AppCreativeTemplate.fb_newsfeed_image),
    ('creative_fbx_news_feed_2', 'FBX', AppCreativeTemplate.fb_newsfeed_image)
])
def test_creatives_is_send_to_audit_when_landing_page_is_changed(cdn_api, audit_app, appnexus_api_auditing,
                                                                 creative_name, strategy_name, creative_template):
    appnexus_api = appnexus_api_auditing

    creative = audit_app.models['creative'][creative_name]
    strategy = audit_app.models['strategy'][strategy_name]
    landing = Site.objects.get(url='http://www.google.com/',
                               owner=strategy.campaign.account)

    Advert.objects.create(strategy=strategy, creative=creative,
                          landing_site=landing)

    set_creative_as_audited(creative)

    appnexus_api.mock_calls = []
    cdn_api.mock_calls = []

    creative = Creative.objects.get(pk=creative.pk)
    creative.landing_site_url = 'http://go.com/'
    creative.save()

    send_for_audit()

    creative_call = call.creative(creative.appnexus_id)
    audit_creative_call = \
        call.audit_creative(creative.appnexus_id, creative.id_random, creative.width, creative.height,
                            creative_template, creative.appnexus_media_url,
                            creative.type != 'Video', creative.data_for_facebook_audit)

    # don't upload to cdn if content is not changed
    assert cdn_api.mock_calls == []
    # don't send for audit on landing_site_url change if already audited
    if not creative.destination == u'd':
        assert creative_call in appnexus_api.mock_calls
        assert audit_creative_call in appnexus_api.mock_calls
    else:
        assert appnexus_api.mock_calls == []

    creative = Creative.objects.get(pk=creative.pk)
    creative.appnexus_status = 'r'
    creative.landing_site_url = 'http://gohome.com/'

    creative.save()

    creative_call = call.creative(creative.appnexus_id)
    audit_creative_call = \
        call.audit_creative(creative.appnexus_id, creative.id_random, creative.width, creative.height,
                            creative_template, creative.appnexus_media_url,
                            creative.type != 'Video', creative.data_for_facebook_audit)

    appnexus_api.mock_calls = []

    send_for_audit()

    # send for audit on landing_site_url change of rejected creative
    assert creative_call in appnexus_api.mock_calls
    assert audit_creative_call in appnexus_api.mock_calls
    # don't upload to cdn
    assert cdn_api.mock_calls == []


@pytest.mark.django_db
@pytest.mark.fbx
@pytest.mark.parametrize('creative_name, strategy_name, creative_template', [
    ('creative_fbx_1', 'FBX', AppCreativeTemplate.fb_sidebar_image),
    ('creative_fbx_news_feed_1', 'FBX', AppCreativeTemplate.fb_newsfeed_image),
    ('creative_fbx_news_feed_2', 'FBX', AppCreativeTemplate.fb_newsfeed_image)
])
def test_fbx_creatives_is_send_to_audit_when_title_is_changed(cdn_api, audit_app, appnexus_api_auditing, creative_name,
                                                              strategy_name, creative_template):
    appnexus_api = appnexus_api_auditing

    creative = audit_app.models['creative'][creative_name]
    strategy = audit_app.models['strategy'][strategy_name]
    landing = Site.objects.get(url='http://www.google.com/',
                               owner=strategy.campaign.account)

    Advert.objects.create(strategy=strategy, creative=creative,
                          landing_site=landing)


    # reset mock calls
    appnexus_api.mock_calls = []
    cdn_api.mock_calls = []

    set_creative_as_audited(creative)

    creative = Creative.objects.get(pk=creative.pk)
    creative.title = 'new title'

    creative.save()

    send_for_audit()

    creative_call = call.creative(creative.appnexus_id)
    audit_creative_call = \
        call.audit_creative(creative.appnexus_id, creative.id_random, creative.width, creative.height,
                            creative_template, creative.appnexus_media_url,
                            creative.type != 'Video', creative.data_for_facebook_audit)

    # send for audit on landing_site_url change of rejected creative
    assert creative_call in appnexus_api.mock_calls
    assert audit_creative_call in appnexus_api.mock_calls
    # don't upload to cdn
    assert cdn_api.mock_calls == []


@pytest.mark.django_db
@pytest.mark.fbx
@pytest.mark.parametrize('creative_name, strategy_name, creative_template', [
    ('creative_fbx_1', 'FBX', AppCreativeTemplate.fb_sidebar_image),
    ('creative_fbx_news_feed_1', 'FBX', AppCreativeTemplate.fb_newsfeed_image),
    ('creative_fbx_news_feed_2', 'FBX', AppCreativeTemplate.fb_newsfeed_image)
])
def test_fbx_creatives_is_send_to_audit_when_body_is_changed(cdn_api, audit_app, appnexus_api_auditing, creative_name,
                                                             strategy_name, creative_template):
    appnexus_api = appnexus_api_auditing

    creative = audit_app.models['creative'][creative_name]
    strategy = audit_app.models['strategy'][strategy_name]
    landing = Site.objects.get(url='http://www.google.com/',
                               owner=strategy.campaign.account)

    Advert.objects.create(strategy=strategy, creative=creative,
                          landing_site=landing)

    set_creative_as_audited(creative)
    appnexus_api.mock_calls = []
    cdn_api.mock_calls = []

    creative = Creative.objects.get(pk=creative.pk)
    creative.body = 'new body'

    creative.save()
    send_for_audit()

    creative_call = call.creative(creative.appnexus_id)
    audit_creative_call = \
        call.audit_creative(creative.appnexus_id, creative.id_random, creative.width, creative.height,
                            creative_template, creative.appnexus_media_url,
                            creative.type != 'Video', creative.data_for_facebook_audit)

    # send for audit on landing_site_url change of rejected creative
    assert creative_call in appnexus_api.mock_calls
    assert audit_creative_call in appnexus_api.mock_calls
    # don't upload to cdn
    assert cdn_api.mock_calls == []


@pytest.mark.django_db
@pytest.mark.fbx
@pytest.mark.parametrize('creative_name', [
    ('creative_fbx_news_feed_1'),
    ('creative_fbx_news_feed_2')
])
def test_fbx_news_feed_creatives_is_send_to_audit_when_message_is_changed(cdn_api, audit_app, appnexus_api_auditing,
                                                                          creative_name):
    appnexus_api = appnexus_api_auditing

    creative = audit_app.models['creative'][creative_name]
    strategy = audit_app.models['strategy']['FBX']
    landing = Site.objects.get(url='http://www.google.com/',
                               owner=strategy.campaign.account)

    Advert.objects.create(strategy=strategy, creative=creative,
                          landing_site=landing)
    set_creative_as_audited(creative)
    # reset mock calls set by saving advert
    appnexus_api.mock_calls = []
    cdn_api.mock_calls = []

    creative = Creative.objects.get(pk=creative.pk)
    creative.message = 'new message'

    creative.save()
    send_for_audit()

    creative_call = call.creative(creative.appnexus_id)
    audit_creative_call = \
        call.audit_creative(creative.appnexus_id, creative.id_random, creative.width, creative.height,
                            AppCreativeTemplate.fb_newsfeed_image, creative.appnexus_media_url,
                            creative.type != 'Video', creative.data_for_facebook_audit)

    # send for audit on landing_site_url change of rejected creative
    assert creative_call in appnexus_api.mock_calls
    assert audit_creative_call in appnexus_api.mock_calls
    # don't upload to cdn
    assert cdn_api.mock_calls == []


@pytest.mark.django_db
@pytest.mark.fbx
@pytest.mark.parametrize('creative_name', [
    ('creative_fbx_news_feed_1'),
    ('creative_fbx_news_feed_2')
])
def test_fbx_creatives_is_send_to_audit_when_domain_is_changed(cdn_api, audit_app, appnexus_api_auditing,
                                                               creative_name):
    appnexus_api = appnexus_api_auditing

    creative = audit_app.models['creative'][creative_name]
    strategy = audit_app.models['strategy']['FBX']
    landing = Site.objects.get(url='http://www.google.com/',
                               owner=strategy.campaign.account)

    Advert.objects.create(strategy=strategy, creative=creative,
                          landing_site=landing)
    set_creative_as_audited(creative)
    # reset mock calls set by saving advert
    appnexus_api.mock_calls = []
    cdn_api.mock_calls = []

    creative = Creative.objects.get(pk=creative.pk)
    creative.domain = 'gravity4_1.com'

    creative.save()
    send_for_audit()

    creative_call = call.creative(creative.appnexus_id)
    audit_creative_call = \
        call.audit_creative(creative.appnexus_id, creative.id_random, creative.width, creative.height,
                            AppCreativeTemplate.fb_newsfeed_image, creative.appnexus_media_url,
                            creative.type != 'Video', creative.data_for_facebook_audit)

    # send for audit on landing_site_url change of rejected creative
    assert creative_call in appnexus_api.mock_calls
    assert audit_creative_call in appnexus_api.mock_calls
    # don't upload to cdn
    assert cdn_api.mock_calls == []


@pytest.mark.django_db
@pytest.mark.fbx
@pytest.mark.parametrize('creative_name', [
    ('creative_fbx_news_feed_1'),
    ('creative_fbx_news_feed_2')
])
def test_fbx_creatives_is_send_to_audit_when_brand_is_changed(cdn_api, audit_app, appnexus_api_auditing, creative_name):
    appnexus_api = appnexus_api_auditing

    creative = audit_app.models['creative'][creative_name]
    strategy = audit_app.models['strategy']['FBX']
    landing = Site.objects.get(url='http://www.google.com/',
                               owner=strategy.campaign.account)

    Advert.objects.create(strategy=strategy, creative=creative,
                          landing_site=landing)

    # reset mock calls set by saving advert
    appnexus_api.mock_calls = []
    cdn_api.mock_calls = []

    set_creative_as_audited(creative)

    creative = Creative.objects.get(pk=creative.pk)
    creative.brand = Brand.objects.all()[1]
    creative.save()

    send_for_audit()

    creative_call = call.creative(creative.appnexus_id)
    audit_creative_call = \
        call.audit_creative(creative.appnexus_id, creative.id_random, creative.width, creative.height,
                            AppCreativeTemplate.fb_newsfeed_image, creative.appnexus_media_url,
                            creative.type != 'Video', creative.data_for_facebook_audit)

    # send for audit on landing_site_url change of rejected creative
    assert creative_call in appnexus_api.mock_calls
    assert audit_creative_call in appnexus_api.mock_calls
    # don't upload to cdn
    assert cdn_api.mock_calls == []


@pytest.mark.django_db
def test_creative_is_auditable(audit_app, appnexus_api_auditing):
    '''
    Checks if only those creatives which are attached to some strategy
    can be auditable (which means that they could be sent for audit manually from UI).
    '''
    creative = audit_app.models['creative']['creative_image_1']
    strategy = audit_app.models['strategy']['Hello this is Citrus']
    landing_site = Site.objects.get(url='http://www.google.com/',
                                    owner=strategy.campaign.account)

    audit_creative_call = \
        call.audit_creative(creative.appnexus_id, creative.id_random,
                            creative.width, creative.height, AppCreativeTemplate.image,
                            creative.appnexus_media_url, True)

    # Creative is not attached to any strategy
    assert creative.is_auditable is False

    # Sending for audit manually will result in exception
    with pytest.raises(ValueError):
        creative.send_for_audit()

    # Let's attach creative to some strategy by creating an advert
    Advert.objects.create(strategy=strategy, creative=creative,
                          landing_site=landing_site)
    creative = Creative.objects.get(id=creative.id)

    assert creative.is_auditable is True

    creative.send_for_audit()
    assert audit_creative_call in appnexus_api_auditing.mock_calls


@pytest.mark.django_db
def test_audit_disabling(audit_app, appnexus_api_auditing):
    """checks if audit is disabled when creative is deleted."""
    appnexus_api = appnexus_api_auditing

    creative = audit_app.models['creative']['creative_image_1']
    strategy = audit_app.models['strategy']['Hello this is Citrus']
    landing = Site.objects.get(url='http://www.google.com/',
                               owner=strategy.campaign.account)

    advert = Advert.objects.create(strategy=strategy, creative=creative,
                                   landing_site=landing)

    creative.appnexus_id = 1234
    # creative.save()

    send_for_audit()

    advert.delete()
    creative.delete()

    disable_creative_audit_call = call.disable_creative_audit(creative.appnexus_id)

    assert disable_creative_audit_call in appnexus_api.mock_calls


@pytest.mark.django_db
def test_audit_fees(audit_app, appnexus_api_auditing):
    appnexus_api = appnexus_api_auditing

    creative = audit_app.models['creative']['creative_image_1']
    strategy = audit_app.models['strategy']['Hello this is Citrus']
    landing = Site.objects.get(url='http://www.google.com/',
                               owner=strategy.campaign.account)
    Advert.objects.create(strategy=strategy, creative=creative,
                          landing_site=landing)

    audit_creative_call = \
        call.audit_creative(creative.appnexus_id, creative.id_random,
                            creative.width, creative.height, AppCreativeTemplate.image,
                            creative.appnexus_media_url, True)

    audit_fees = 0
    account_balance = creative.owner.account_balance()
    assert account_balance > AUDIT_FEE

    # 1. There is enough money to audit. Send creative multiple times for
    # audit and check if fees are calculated correctly.

    while account_balance > 0:
        creative.send_for_audit(force=True)
        creative = Creative.objects.get(pk=creative.pk)

        audit_fees += AUDIT_FEE
        account_balance -= AUDIT_FEE

        assert creative.audit_fees == audit_fees
        assert creative.owner.account_balance() == account_balance
        assert DailySpendings.objects.get(date=date.today(), account=creative.owner) \
                   .audit_fees == audit_fees

        assert audit_creative_call in appnexus_api.mock_calls
        appnexus_api.mock_calls = []

    # 2. Account balance is empty. Check if creative is not sent for audit. No fees should
    # be changed and notification event about low budget should be created.

    creative.send_for_audit(force=True)
    creative = Creative.objects.get(pk=creative.pk)

    assert creative.audit_fees == audit_fees
    assert creative.owner.account_balance() == account_balance
    assert audit_creative_call not in appnexus_api.mock_calls
    assert Event.objects.filter(
        message_type=Event.Messages.types.keys().index('not_enough_budget_for_audit')
    ).count() == 1

    # 3. Charge account and try to send creative again.

    audit_app.setup_payments(default_payments)
    account_balance = creative.owner.account_balance()

    creative.send_for_audit(force=True)
    creative = Creative.objects.get(pk=creative.pk)

    audit_fees += AUDIT_FEE
    account_balance -= AUDIT_FEE

    assert creative.audit_fees == audit_fees
    assert creative.owner.account_balance() == account_balance
    assert audit_creative_call in appnexus_api.mock_calls
    assert DailySpendings.objects.get(date=date.today(), account=creative.owner) \
               .audit_fees == audit_fees


@pytest.mark.django_db
def test_audit_email_sending(audit_app, appnexus_api_auditing):
    creative = audit_app.models['creative']['creative_image_1']
    strategy = audit_app.models['strategy']['Hello this is Citrus']
    landing = Site.objects.get(url='http://www.google.com/',
                               owner=strategy.campaign.account)
    Advert.objects.create(strategy=strategy, creative=creative,
                          landing_site=landing)

    # clear outbox
    mail.outbox = []

    send_for_audit()
    assert is_email_sent('Your ad has been sent for audit')

    # charge account to have enough money for next audits
    audit_app.setup_payments(default_payments)

    # create 3 new creatives and make sure that only 1 email is sent
    for index in ['A', 'B', 'C']:
        creative = CreativeImage.objects.create(name='creative_{0}'.format(index),
                                                owner=strategy.campaign.account,
                                                width=300, height=250,
                                                image='creatives/test_creative.jpg')
        Advert.objects.create(strategy=strategy, creative=creative,
                              landing_site=landing)

    # clear outbox
    mail.outbox = []

    send_for_audit()
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == 'Your ads have been sent for audit'


@pytest.fixture
def audit_low_budget(db, basic_fixture):
    amount = AUDIT_FEE * Decimal(0.8)
    payments = [
        {'account': 'acc', 'datetime': '2014-02-10T00:00', 'amount': amount},
        {'account': 'acc_2', 'datetime': '2014-01-11T00:00', 'amount': amount}
    ]
    creative = [{'name': 'creative_image_1', 'owner': 'acc', 'width': 300,
                 'height': 250, 'image': 'creatives/test_creative.jpg'}]
    adverts = [
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
    ]
    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()
    setup.setup_payments(payments)
    setup.setup_landing_pages()
    setup.setup_creative_images(creative)
    setup.setup_campaigns_running()
    setup.setup_strategies()
    setup.setup_bidding_periods()
    setup.setup_adverts(adverts)

    return setup


def test_audit_not_enough_budget(audit_low_budget, appnexus_api_auditing):
    '''
    Test creative 'audit blocked because of not enough budget'
    '''
    creative = Creative.objects.first()
    assert creative.state.pending
    assert not creative.state.blocked

    # Try to audit creative with too low account balance
    send_for_audit()

    # Check if event was created and creative status was set to blocked
    latest_event = Event.objects.all()[0]
    assert latest_event.message_name == 'not_enough_budget_for_audit'

    creative = Creative.objects.first()
    assert creative.state.pending
    assert creative.state.blocked

    # Add funds to account
    Payment.objects.create(
        account=creative.owner,
        datetime=datetime.utcnow(),
        amount=AUDIT_FEE
    )

    # Try to audit, status should not be not blocked
    send_for_audit()

    creative = Creative.objects.first()
    assert not creative.state.pending
    assert not creative.state.blocked


@pytest.mark.django_db
def test_creative_rejected_email_sending(audit_app, appnexus_api_rejecting):
    creative = audit_app.models['creative']['creative_image_1']
    strategy = audit_app.models['strategy']['Hello this is Citrus']
    landing = Site.objects.get(url='http://www.google.com/',
                               owner=strategy.campaign.account)
    Advert.objects.create(strategy=strategy, creative=creative,
                          landing_site=landing)
    send_for_audit()
    import ipdb;ipdb.set_trace()
    assert is_email_sent('Your ad has been rejected')


@pytest.mark.django_db
@patch(
    'ui.storage.models.appnexus_api.creative',
    return_value={'is_expired': True, 'audit_feedback': 'In your face!'}
)
def test_creative_expiration(creative_resource, audit_app):
    '''
    Checks if creation of Advert has a side effect in calling cdn
    and AppNexus API.
    '''
    creative = Creative.objects.first()
    creative.appnexus_id = 111
    creative.appnexus_status = 'a'
    creative.save()

    assert creative_resource.call_count == 0
    appnexus_update_status_all()
    assert creative_resource.call_count == 1
    reloaded_creative = Creative.objects.get(pk=creative.pk)
    assert reloaded_creative.appnexus_status == 'e'

    state = CreativeState(reloaded_creative)
    assert filter(lambda state: state[1] is True, state.to_dict().items()) == [('expired', True)]
