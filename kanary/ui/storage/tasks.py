import os
import logging
import time
from collections import defaultdict

from celery import task
from djcelery_transactions import task as transaction_task

from django.conf import settings
from django.db.models import Q

from raven.contrib.django.raven_compat.models import client

from apis.liverail import LiveRailDBError
from ui.storage.models import Creative

from ui.mail import mailing

log = logging.getLogger('django')


def exponential_retry_time(retries):
    '''
    Returns next interval to retry task in exponential manner
    '''
    t = settings.CELERY_TASK_RETRY_EXPONENTIAL_BASE ** retries
    return int(t + 60)


@transaction_task(max_retries=None)
def upload_file_to_cdn(pk, content):
    """
    Tries to upload from given path and create key in amazon's bucket.

    :param int pk: id of creative instance

    :param string content: content to upload
    :rtype: int or None
    :returns: id of creative instance

    .. note::
        Retries if any :exc:`IOError` occured.
    """

    creative = Creative.objects.get(pk=pk)
    try:
        creative.upload_to_cdn(content)
    except IOError as e:
        log.error(u'UPLOAD_FILE_TO_CDN:cid:%s:FAIL:%s', creative.public_id, str(e))
        retry_time = exponential_retry_time(upload_file_to_cdn.request.retries)
        upload_file_to_cdn.retry(countdown=retry_time)


@task
def send_for_audit():
    """
    Get creatives objects and send them for audit.
    """
    from ui.storage.models import Creative

    sent_creatives = defaultdict(list)
    for creative in Creative.objects.filter(to_audit=True).all():
        if creative.send_for_audit():
            sent_creatives[creative.owner].append(creative)

    for creatives in sent_creatives.values():
        mailing.creatives_sent_for_audit(creatives).send()


@task
def update_brand_access_status():
    """
    Update appnexus_access_status from AppNexus for all brands.
    Send request to gain access to a Facebook brand page (for marked brands)
    """
    from ui.storage.models import Brand

    for brand in Brand.objects.all():
        brand.update_access_status()


@task(max_retries=None)
def disable_creative_audit(cid, *args, **kwargs):
    from ui.storage.models import Creative
    Creative.objects.get(pk=cid).disable_audit()


@task(max_retries=None)
def audit_notify_request(audit_notify):
    '''
    Arguments:
        audit_notify(dict) - received from AppNexus
    Returns:
        creative_pk(int) - creative.pk
    '''
    from ui.storage.models import Creative
    creative = Creative.appnexus_update_notify(audit_notify)

    if not creative:
        log.error('audit_notify %s no such creative in db', audit_notify)


@task
def appnexus_update_status_all():
    from ui.storage.models import Creative
    Creative.appnexus_update_status_all()


@task
def update_video_creative_media():
    from ui.storage.models import CreativeVideo

    try:
        CreativeVideo.liverail_update_media_all()
    except LiveRailDBError as e:
        client.captureMessage(e.message, level=logging.INFO)


@task
def clean_unsaved_files(min_age, max_age=None):
    '''
        Cleans unsaved creative files from filesystem

        :param int min_age: minimum age file has to be on filesystem,
            before task will consider checking this file (in seconds)
        :param int max_age: maximum age file has to be on filesystem,
            after which task will not check it (in seconds)
    '''
    from ui.storage.models import Creative

    present = time.time()
    min_age *= 3600  # let us make it hours
    max_age = max_age * 3600 if max_age else present

    count = 0

    for root, dirs, files in os.walk(settings.CREATIVES_DIR):
        dirname = root.replace(settings.MEDIA_ROOT + '/', '')
        for name in files:
            mtime = os.path.getmtime(os.path.join(root, name))
            if (present - max_age) < mtime < (present - min_age):
                filename = os.path.join(dirname, name)
                if not Creative.objects.filter(
                    Q(creativeimage__image=filename) |
                        Q(creativeflash__file=filename)).exists():
                    os.remove(os.path.join(root, name))
                    count += 1
                    log.info('clean_unsaved_files: removing %s' % filename)

    if count:
        log.info('clean_unsaved_files: removed %d abandoned creative files'
                 % count)
