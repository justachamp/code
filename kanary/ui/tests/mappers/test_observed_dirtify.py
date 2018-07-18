from datetime import datetime

import pytest

from ui.campaign.models import Campaign, Advert, Strategy
from ui.account.models import Account, Payment
from ui.targeting.models import TargetValue, PublisherTargetValue
from ui.common.models import LatestUpdate
from ui.publishers.models import PublisherSet
from ui.storage.models import Audience


def test_dirtifying_dates(strategies):
    ''' Checks if when time passes objects are marked as dirty
    (when it has observes_date_fields defined).
    '''
    now = datetime.utcnow()

    last = LatestUpdate.by_name(Advert.__name__)
    last.latest_update = now
    last.save()

    ad = Advert.objects.all()[0]
    campaign = Campaign.objects.get(pk=ad.strategy.campaign_id)
    campaign.end_UTC = datetime.utcnow()
    campaign.save()

    # mark all as not dirty
    Advert.objects.all().update(cache_is_dirty=False)

    assert len(Advert._cache_dirty_dates(now)) > 0

    Advert.cache_dirtify_dates()

    assert Advert.objects.filter(cache_is_dirty=True).exists()

    # after dirtify no more dirty dates should occur
    assert len(Advert._cache_dirty_dates(datetime.utcnow())) == 0


def test_advert_modify_add_targeting(app_noaudit):
    '''
    check if adding new target value to strategy will dirtify strategy Adverts
    '''
    # mark all as not dirty
    Advert.objects.all().update(cache_is_dirty=False)

    for strategy in Strategy.objects.all():
        tv = TargetValue.objects.first()
        strategy.targeting_values.add(tv)

        # get advert
        ad = strategy.advert_set.get()
        assert ad.cache_is_dirty is True


def test_advert_modify_remove_targeting(app_noaudit):
    '''
    check if removing target value from strategy will dirtyfy strategy Adverts
    '''
    # mark all as not dirty
    Advert.objects.all().update(cache_is_dirty=False)

    for strategy in Strategy.objects.all():
        tv = strategy.targeting_values.first()
        strategy.targeting_values.remove(tv)

        # get advert
        ad = strategy.advert_set.get()
        assert ad.cache_is_dirty is True


def test_advert_modify_remove_strategy_from_targeting(app_noaudit):
    '''
    check if removing strategy from target_value will dirtyfy strategy Adverts
    '''
    # mark all as not dirty
    Advert.objects.all().update(cache_is_dirty=False)

    for strategy in Strategy.objects.all():
        tv = strategy.targeting_values.first()
        tv.strategy_set.remove(strategy)

        # get advert
        ad = strategy.advert_set.get()
        assert ad.cache_is_dirty is True


def test_advert_modify_add_publisher(app_noaudit_publisherset):
    '''
    check if adding new publisher to publisherset will dirtify strategy Adverts
    '''
    # mark all as not dirty
    Advert.objects.all().update(cache_is_dirty=False)

    publisherset = PublisherSet.objects.get()
    unused_publisher = PublisherTargetValue.objects.exclude(
        pk__in=publisherset.target_values.values('pk')).first()

    publisherset.target_values.add(unused_publisher)

    assert Advert.objects.filter(cache_is_dirty=True).exists()


def test_advert_modify_remove_publisher(app_noaudit_publisherset):
    '''
    check if removing publisher from publisherset will dirtify strategy Adverts
    '''
    # mark all as not dirty
    Advert.objects.all().update(cache_is_dirty=False)

    publisherset = PublisherSet.objects.get()
    publisher = publisherset.target_values.first()

    publisherset.target_values.remove(publisher)

    assert Advert.objects.filter(cache_is_dirty=True).exists()


def test_advert_modify_remove_publisherset_from_publisher(
        app_noaudit_publisherset):
    '''
    check if removing publisherset from publisher will dirtify strategy Adverts
    '''
    # mark all as not dirty
    Advert.objects.all().update(cache_is_dirty=False)

    publisherset = PublisherSet.objects.get()
    publisher = publisherset.target_values.first()
    publisher.publishertargetvalue.publisherset_set.remove(publisherset)

    assert Advert.objects.filter(cache_is_dirty=True).exists()


def test_advert_modify_remove_publisherset_from_strategy(
        app_noaudit_publisherset):
    '''
    check if removing publisherset from publisher will dirtify strategy Adverts
    '''
    # mark all as not dirty
    Advert.objects.all().update(cache_is_dirty=False)

    publisherset = PublisherSet.objects.get()
    strategy = publisherset.strategy_set.first()
    strategy.publisherset = None
    strategy.save()

    assert Advert.objects.filter(cache_is_dirty=True).exists()


@pytest.mark.parametrize('include', (True, False))
def test_advert_strategy_add_audience(app_audited_audiences, include):
    '''
    Check if adding audience to strategy dirtifies advert
    '''
    Advert.objects.all().update(cache_is_dirty=False)
    strategy = Strategy.objects.first()
    audiences = Audience.objects.all()
    if include:
        strategy.audiences = audiences
    else:
        strategy.audiences_exclude = audiences

    strategy.save()

    assert Advert.objects.filter(cache_is_dirty=True).exists()


@pytest.mark.parametrize('include', (True, False))
def test_advert_strategy_remove_audience(app_audited_audiences, include):
    '''
    Check if adding audience to strategy dirtifies advert
    '''
    Advert.objects.all().update(cache_is_dirty=False)
    strategy = Strategy.objects.first()
    audiences = Audience.objects.all()
    if include:
        strategy.audiences = audiences
    else:
        strategy.audiences_exclude = audiences

    strategy.save()
    Advert.objects.all().update(cache_is_dirty=False)
    strategy = Strategy.objects.get(pk=strategy.pk)
    if include:
        strategy.audiences.remove(audiences[0])
    else:
        strategy.audiences_exclude.remove(audiences[0])

    assert Advert.objects.filter(cache_is_dirty=True).exists()


def test_advert_account_add_payment(app_audited_audiences):
    Advert.objects.all().update(cache_is_dirty=False)
    account = Account.objects.first()
    payment = Payment()
    payment.account = account
    payment.datetime = datetime.utcnow()
    payment.amount = 20
    payment.save()

    assert Advert.objects.filter(cache_is_dirty=True).exists()


def test_advert_account_audit_fee(app_audited_audiences):
    Advert.objects.all().update(cache_is_dirty=False)
    account = Account.objects.first()
    account.audit_fees = 20
    account.save()

    assert Advert.objects.filter(cache_is_dirty=True).exists()
