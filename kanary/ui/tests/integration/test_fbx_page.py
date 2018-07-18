from mock import call
import pytest
import simplejson

from ui.storage.models import Brand
from ui.storage.tasks import update_brand_access_status
from ui.tests.utils import DatabaseDataFactory


__author__ = 'amatsal'


@pytest.fixture
def audit_app(basic_fixture):
    setup = DatabaseDataFactory()
    setup.setup_accounts()
    setup.setup_users()
    setup.setup_fbx_pages()
    setup.models['brand']['test_fbx_page_2'].delete()
    return setup


@pytest.mark.django_db
@pytest.mark.fbx
def test_fbx_page_update_to_confirm_status_from_pending(audit_app, appnexus_api_auditing):
    update_brand_access_status()
    assert Brand.objects.filter(page_name='test_fbx_page_1')[0].appnexus_access_status == 'confirmed'
    update_brand_page_access_call = call.update_brand_page_access(Brand.objects.all()[0].thirdparty_page_id)
    assert appnexus_api_auditing.mock_calls == [update_brand_page_access_call]


@pytest.mark.django_db
@pytest.mark.fbx
def test_fbx_page_update_to_reject_status_from_pending(audit_app, appnexus_api_rejecting):
    update_brand_access_status()
    assert Brand.objects.filter(page_name='test_fbx_page_1')[0].appnexus_access_status == 'rejected'
    update_brand_page_access_call = call.update_brand_page_access(Brand.objects.all()[0].thirdparty_page_id)
    assert appnexus_api_rejecting.mock_calls == [update_brand_page_access_call]


@pytest.mark.django_db
@pytest.mark.fbx
def test_fbx_page_update_to_reject_status_from_confirmed(audit_app, appnexus_api_rejecting):
    update_brand_status(Brand.objects.filter(page_name='test_fbx_page_1')[0], 'confirmed')
    update_brand_access_status()
    assert Brand.objects.filter(page_name='test_fbx_page_1')[0].appnexus_access_status == 'rejected'
    update_brand_page_access_call = call.update_brand_page_access(Brand.objects.all()[0].thirdparty_page_id)
    assert appnexus_api_rejecting.mock_calls == [update_brand_page_access_call]


@pytest.mark.django_db
@pytest.mark.fbx
def test_fbx_page_update_to_pending_status_from_confirmed(audit_app, appnexus_api):
    update_brand_status(Brand.objects.filter(page_name='test_fbx_page_1')[0], 'confirmed')
    update_brand_access_status()
    assert Brand.objects.filter(page_name='test_fbx_page_1')[0].appnexus_access_status == 'pending'
    update_brand_page_access_call = call.update_brand_page_access(Brand.objects.all()[0].thirdparty_page_id)
    assert appnexus_api.mock_calls == [update_brand_page_access_call]


@pytest.mark.django_db
@pytest.mark.fbx
def test_no_calls_to_api_for_rejected_fbx_page(audit_app, appnexus_api):
    appnexus_api = appnexus_api
    update_brand_status(Brand.objects.filter(page_name='test_fbx_page_1')[0], 'rejected')
    update_brand_access_status()
    assert appnexus_api.mock_calls == []


@pytest.mark.django_db
@pytest.mark.fbx
def test_no_calls_to_api_for_deleted_fbx_page(audit_app, appnexus_api):
    appnexus_api = appnexus_api
    Brand.objects.filter(page_name='test_fbx_page_1')[0].delete()
    update_brand_access_status()
    assert appnexus_api.mock_calls == []


@pytest.mark.django_db
@pytest.mark.fbx
def test_send_request_access_button_click(audit_app, kclient):
    brand = Brand.objects.filter(page_name='test_fbx_page_1')[0]
    update_brand_status(brand, 'rejected')
    update_brand_data = {
        "appnexus_access_status": brand.appnexus_access_status,
        "brand_id": brand.brand_id,
        "check_access_status": True,
        "facebook_page_id": brand.thirdparty_page_id,
        "id": brand.id,
        "page_name": brand.page_name
    }
    response = kclient.put('/api/storage/brand/{0}/'.format(brand.id), data=simplejson.dumps(update_brand_data),
                           content_type='application/json')
    assert response.status_code == 200
    assert Brand.objects.filter(page_name='test_fbx_page_1')[0].appnexus_access_status == 'pending'
    assert Brand.objects.filter(page_name='test_fbx_page_1')[0].check_access_status == True


@pytest.mark.django_db
@pytest.mark.fbx
def test_system_makes_post_to_appnexus_api_when_check_access_status_is_true(audit_app, appnexus_api):
    brand = Brand.objects.filter(page_name='test_fbx_page_1')[0]
    brand.check_access_status = True
    brand.save()
    update_brand_access_status()
    request_brand_page_access_call = call.request_brand_page_access(brand.brand_id, brand.thirdparty_page_id)
    assert appnexus_api.mock_calls == [request_brand_page_access_call]
    assert Brand.objects.filter(page_name='test_fbx_page_1')[0].check_access_status == False


def update_brand_status(brand, new_status):
    brand.appnexus_access_status = new_status
    brand.save()