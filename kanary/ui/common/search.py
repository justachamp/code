
from haystack.inputs import Raw
from requests.utils import quote


class QuoteUrl(Raw):

    '''
    Escapes slashes for ElasticSearch
    '''

    input_type_name = 'slash_escape'

    def prepare(self, query_obj):
        query_string = super(QuoteUrl, self).prepare(query_obj)
        return quote(query_string).replace('/', '\/')
