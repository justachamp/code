from haystack.indexes import (
    Indexable, CharField, IntegerField
)
from celery_haystack.indexes import CelerySearchIndex
from requests.utils import quote

from ui.campaign.models import Site
from ui.haystack_extensions import NgramField


class SiteIndex(CelerySearchIndex, Indexable):

    '''Base search index which will be shared between various search indexes
    in targeting. It's strongly related to django-haystack'''

    #: defines text field on contents of which search will be performed.
    text = CharField(document=True, use_template=True)
    url = NgramField()
    owner_id = IntegerField(model_attr='owner_id')

    def get_model(self):
        return Site

    def prepare_url(self, site):
        return quote(site.url)

    def index_queryset(self, **kwargs):
        '''Returns query on which haystack will perform indexing'''
        return self.get_model().objects.all()
