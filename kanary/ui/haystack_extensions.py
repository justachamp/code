"""
Kanary hasytack extensions.

based on
# http://www.wellfireinteractive.com/blog/custom-haystack-elasticsearch-backend/ # noqa

"""
from django.conf import settings
from haystack.backends.elasticsearch_backend import ElasticsearchSearchBackend
from haystack.backends.elasticsearch_backend import ElasticsearchSearchEngine
from haystack.fields import CharField as BaseCharField
from haystack.fields import NgramField as BaseNgramField
from haystack.fields import EdgeNgramField as BaseEdgeNgramField


class ConfigurableElasticBackend(ElasticsearchSearchBackend):

    """
    Haystack elasticsearch backend providing per-field configuration.

    To overwrite default hastack settings for elasticsearch, configure a
    ELASTICSEARCH_INDEX_SETTINGS in your project settings.py

    """

    DEFAULT_ANALYZER = "snowball"

    def __init__(self, connection_alias, **connection_options):
        super(ConfigurableElasticBackend, self).__init__(connection_alias, **connection_options)
        user_settings = getattr(settings, 'ELASTICSEARCH_INDEX_SETTINGS', {})
        if user_settings:
            setattr(self, 'DEFAULT_SETTINGS', user_settings)

    def build_schema(self, fields):
        """
        Build elasticsearch schema.

        Overrides :meth:`ElasticsearchSearchBackend.build_schema`

        :param dict fields: fields used in indexing
        :returns: typle consisting of content_field_name and generated mapping
        :rtype: tuple

        """
        content_field_name, mapping = super(ConfigurableElasticBackend, self).build_schema(fields)

        for field_name, field_class in fields.items():
            field_mapping = mapping[field_class.index_fieldname]

            if field_mapping['type'] == 'string' and field_class.indexed:
                if not hasattr(field_class, 'facet_for'):
                    index_analyzer = getattr(field_class, 'index_analyzer', None)
                    search_analyzer = getattr(field_class, 'search_analyzer', None)
                    if not (index_analyzer and search_analyzer):
                        field_mapping['analyzer'] = getattr(field_class, 'analyzer', self.DEFAULT_ANALYZER)
                    else:
                        # remove to actually make use of index_analyzer
                        # and search_analyzer. otherwise we elastic sets just
                        # search_query_analyzer and discards both index and
                        # search analzyer
                        del field_mapping['analyzer']
                        field_mapping['index_analyzer'] = index_analyzer if index_analyzer else self.DEFAULT_ANALYZER
                        field_mapping['search_analyzer'] =\
                            search_analyzer if search_analyzer else self.DEFAULT_ANALYZER

            mapping.update({field_class.index_fieldname: field_mapping})
        return (content_field_name, mapping)


class ConfigurableElasticSearchEngine(ElasticsearchSearchEngine):

    """ElasticSearch engine using ConfigurableElasticBackend."""

    backend = ConfigurableElasticBackend


class ConfigurableFieldMixin(object):

    """Haystack field mixin adding option to configure specific analyzers."""

    def __init__(self, **kwargs):
        self.analyzer = kwargs.pop('analyzer', None)
        self.search_analyzer = kwargs.pop('search_analyzer', None)
        self.index_analyzer = kwargs.pop('index_analyzer', None)
        super(ConfigurableFieldMixin, self).__init__(**kwargs)


class CharField(ConfigurableFieldMixin, BaseCharField):

    """CharField that allows analyzers configuration for elasticsearch."""

    pass


class NgramField(ConfigurableFieldMixin, BaseNgramField):

    """NgramField that allows analyzers configuration for elasticsearch."""

    def __init__(self, **kwargs):
        kwargs['analyzer'] = kwargs.get('analyzer', 'ngram_analyzer')
        super(NgramField, self).__init__(**kwargs)


class EdgeNgramField(ConfigurableFieldMixin, BaseEdgeNgramField):

    """EdgeNgramField that allows analyzers configuration for elasticsearch."""

    def __init__(self, **kwargs):
        kwargs['analyzer'] = kwargs.get('analyzer', 'edgengram_analyzer')
        super(EdgeNgramField, self).__init__(**kwargs)


class AutocompleteField(ConfigurableFieldMixin, BaseCharField):

    """Field preconfigured for autocomplete."""

    def __init__(self, **kwargs):
        kwargs.pop('analyzer', None)  # no general analyzer here please
        kwargs['search_analyzer'] = kwargs.get('search_analyzer', 'standard')
        kwargs['index_analyzer'] = kwargs.get('index_analyzer', 'autocomplete')
        super(AutocompleteField, self).__init__(**kwargs)
