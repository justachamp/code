from django.db import models


from ui.account.models import Account
from ui.targeting.models import TargetValue, PublisherTargetValue
from etc import dimensions


class PublisherSet(models.Model):

    TYPE_SITE = 'site'
    TYPE_APP = 'app'

    TYPES = (
        (TYPE_SITE, 'site'),
        (TYPE_APP, 'app'),
    )

    name = models.CharField(max_length=30)
    owner = models.ForeignKey(Account, related_name='publisher_sets')
    target_values = models.ManyToManyField(TargetValue, blank=False)
    # sets type
    inventory = models.CharField(max_length=10, choices=TYPES)
    # defines whether this set keeps networks or publishers
    is_network = models.BooleanField(default=False)
    blacklist = models.BooleanField(default=False)

    @property
    def targetvalues(self):
        '''
        Returns either networks or publishers depend on is_network flag
        '''
        from haystack.query import SearchQuerySet

        ids = []
        for pub_id in self.target_values.values('id'):
            ids.append(pub_id['id'])

        django_ct = '{0}.{1}'.format(
            PublisherTargetValue._meta.app_label,
            PublisherTargetValue._meta.object_name.lower()
        )

        sqs = SearchQuerySet().filter_and(
            django_ct=django_ct,
            django_id__in=ids,
            inventory=self.inventory
        )
        if self.is_network:
            return sqs.filter_and(pubkey=dimensions.network)

        return sqs.filter_and(pubkey=dimensions.publisher_name)

    @property
    def adverts(self):
        from ui.campaign.models import Advert
        return Advert.objects.filter(strategy__publisherset=self.pk)
