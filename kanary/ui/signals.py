from celery_haystack.signals import CelerySignalProcessor
from django.db import models

from ui.campaign.models import Site


class KanarySignalProcessor(CelerySignalProcessor):

    def setup(self):
        super(KanarySignalProcessor, self).setup()
        models.signals.post_save.connect(self.handle_save, sender=Site)
        models.signals.post_delete.connect(self.handle_delete, sender=Site)

    def teardown(self):
        super(KanarySignalProcessor, self).teardown()
        models.signals.post_save.disconnect(self.handle_save, sender=Site)
        models.signals.post_delete.disconnect(self.handle_delete, sender=Site)
