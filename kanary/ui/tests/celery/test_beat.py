import re
from importlib import import_module

from celery import Task
from django.conf import settings


def test_cron_tasks_existence():
    ''' checks if all celery beat defined tasks are importable '''

    for name, sched in settings.CELERYBEAT_SCHEDULE.iteritems():
        module, task_name = re.match(r'^(.*)\.(.+)$', sched['task']).groups()
        module = import_module(module)

        task = getattr(module, task_name)
        assert isinstance(task, Task)
