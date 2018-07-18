from celery import task
from celery.utils.log import get_task_logger

from django.conf import settings
from django.db import models

from ui.cache.base_models import CacheMapped

log = get_task_logger('django')


def is_cache_mapped(model):
    """
    Check if the model should be cache mapped.
    All cache mapped subclasses but those that define `abstract = True` should be used for mapping.
    :param django.db.models.base.Model model:
    :rtype: bool
    """
    return issubclass(model, CacheMapped) and not model.MapClass().__dict__.get('abstract', False)

# filter is ugly, but done only once at django initialization:
cache_mapped = filter(is_cache_mapped, models.get_models())


@task
def trigger_cache_mappings(
        time_limit=settings.TRIGGER_CACHE_MAPPINGS_TIMELIMIT,
        force=False
):
    ''' Triggers cache mappings for each CacheMapped class
    Arguments:
        force - if False triggers only dirty instances
    '''

    for cls in cache_mapped:
        changes_count = cls.cache_trigger_mappings(force)
        if changes_count == 0:
            continue  # No dirty objects for this class

        log.info('%s: %s objects mapped into cache.' % (cls, changes_count))
