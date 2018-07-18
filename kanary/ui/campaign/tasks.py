from celery import task
from django.conf import settings

from ui.campaign import appnexus_profile_updater
from adserving.optimizer.tasks import update_probabilities
from ui.tasks import RedisTask


class BiddingPricesRedisTask(RedisTask):
    host = settings.REDIS['probabilities']['host']
    port = settings.REDIS['probabilities']['port']
    db = settings.REDIS['probabilities']['db']

    def __init__(self, *args, **kwargs):
        RedisTask.__init__(self, *args, **kwargs)


@task
def appnexus_update_profile():
    '''
    Update AppNexus bidder profile. See appnexus_profile_updater module for more documentation.

    :rtype: tuple
    :returns: AppNexus API response, dictionary with updated settings
    '''

    return appnexus_profile_updater.update()


@task(base=BiddingPricesRedisTask)
def update_probabilities_task():
    rd = update_probabilities_task.rd
    update_probabilities(rd)
