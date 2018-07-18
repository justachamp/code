from celery import task

from ui import settings


@task(time_limit=settings.APPNEXUS_PUBLISHERS_TRANSLATION_UPDATE_TIMELIMIT)
def appnexus_publishers_translation_update():
    from ui.publishers.network_translations import (
        appnexus_publishers_translate
    )
    appnexus_publishers_translate()


@task
def fixed_publishers_translation_update():
    from ui.publishers.network_translations import translate_fixed_networks
    translate_fixed_networks()
