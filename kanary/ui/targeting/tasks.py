import cPickle
from celery import task
from celery.utils.log import get_task_logger
from django.conf import settings

from etc.constants import TARGETING_PING_CHANNEL
from ui.tasks import RedisTask


log = get_task_logger(__name__)


class TargetingRedisTask(RedisTask):
    host = settings.REDIS['targeting']['host']
    port = settings.REDIS['targeting']['port']
    db = settings.REDIS['targeting']['db']


# Appnexus API returns tousands of entries and that takes a lot of time
# so we use custom time_limit for this task.
@task(time_limit=settings.TARGETING_UPDATE_TIMELIMIT)
def appnexus_targeting_update():
    from ui.targeting.appnexus_base import appnexus_targeting_update
    appnexus_targeting_update()


@task
def appnexus_location_translation():
    from ui.targeting.appnexus_location_translation import translate_countries_and_states_from_csv
    log.info('[TRANSLATE_LOCATIONS] Translation started')
    translate_countries_and_states_from_csv()


def targeting_ping(rd):
    rd.publish(TARGETING_PING_CHANNEL, cPickle.dumps(''))


@task(base=TargetingRedisTask)
def bidder_targeting_ping():
    rd = bidder_targeting_ping.rd
    targeting_ping(rd)
