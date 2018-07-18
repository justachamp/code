from django.db import models as m
from south.modelsinspector import add_introspection_rules

from ui.fields import rules

# adding South custom fields definition
add_introspection_rules(rules, ['^ui\.fields'])


class AppNexus(m.Model):

    # cached AppNexus tokens
    bidder_token = m.CharField(max_length=40, null=True)
    member_token = m.CharField(max_length=40, null=True)

    @classmethod
    def tokens(cls, bidder_token=None, member_token=None):
        """
        Getter/Setter.

        If bidder_token or member_token is not None:
            save values to the database.

        :returns: (bidder_token, member_token)
        :rtype: str tuple

        """
        row, _ = cls.objects.get_or_create(pk=1)
        if bidder_token is not None:
            row.bidder_token = bidder_token
            row.save()
        if member_token is not None:
            row.member_token = member_token
            row.save()

        return row.bidder_token, row.member_token
