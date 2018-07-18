'''Common code for various celery purposes'''
import logging

import redis
import requests
from celery import Task, task
from raven.contrib.django.raven_compat.models import client


class RedisTask(Task):

    '''
    Initializes connection with redis which is later accessible
    via self.rd in task.
    It solves some performance problems and creates smarter connection creation
    policy (by default - one connection/pool of connection per task-thread).

    To use this class you must create subclass with given parameters:
    class ProfsetRedisTask(RedisTask):
        host = 'localhost'
        port = '1234'
        db = 0

    @task
    def hello_world(base=ProfsetRedisTask):
        assert(hasattr(self.rd))
    '''
    abstract = True

    def __init__(self, *args, **kwargs):
        self.rd = redis.Redis(host=self.host, port=self.port, db=self.db)

    @property
    def host(self):
        raise AttributeError('Must be defined in sub-class')

    @property
    def port(self):
        raise AttributeError('Must be defined in sub-class')

    @property
    def db(self):
        raise AttributeError('Must be defined in sub-class')


@task(ignore_result=True)
def send_appnexus_metrics_to_graphite():
    from stats.appnexus.tasks import populate_graphite
    try:
        populate_graphite()
    except requests.Timeout as e:
        client.captureMessage('Appnexus reports timeouted: {0}'.format(e), level=logging.INFO)
