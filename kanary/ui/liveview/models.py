from django.db import models
from etc.constants import ID_RANDOM_LENGTH


class LiveViewCounter(models.Model):
    class Meta:
        index_together = [["time", "public_id"], ]

    time = models.DateTimeField()
    public_id = models.CharField(max_length=ID_RANDOM_LENGTH * 4 + 3) #3 underscores + 4*id_length (#id=2 12_12_12)
    bid = models.BigIntegerField()
    imp = models.BigIntegerField()

    def __str__(self):
        return ('{0} {1} {2} {3}'.format(
            self.time, self.public_id, self.bid, self.imp))
