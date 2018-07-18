import logging
from models import LiveViewCounter
from django.db import transaction


class DataStorer(object):

    """Class responsible for storing data in database"""

    logger = logging.getLogger('storm')

    @transaction.atomic
    def retrive_entry(self, entry_id, entry_time):
        entry = LiveViewCounter.objects.select_for_update().filter(
            public_id=entry_id, time=entry_time)

        if entry:
            return entry[0]

        return LiveViewCounter(
            public_id=entry_id, time=entry_time, bid=0, imp=0)

    def store(self, entry_id, entry_time, entry_event_type, amount):
        self.logger.info("Storing: [%s]" % str([entry_id, entry_time]))
        entry = self.retrive_entry(entry_id, entry_time)

        if entry_event_type == 'bid':
            entry.bid += amount
        else:
            entry.imp += amount

        entry.save()
        self.logger.info("Stored: [%s]" % str([entry_id, entry_time]))
