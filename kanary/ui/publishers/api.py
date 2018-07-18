
from tastypie.resources import ALL
from tastypie.fields import ListField, ToManyField
from tastypie.validation import Validation
from haystack.query import SearchQuerySet

from ui.publishers.models import PublisherSet
from ui.targeting.models import TargetValue
from ui.targeting.api import PublishersResource
from ui.common.api import ProtectedModelResource

from ui.authorization import Auth
from etc import dimensions


class SetValidation(Validation):

    '''
        Validation that checks Creative
    '''
    error_messages = {
        'publishers': 'No publishers selected',
        'type': 'Type have to be chosen!',
        'wrong_type': 'Incorrect set type chosen',
        'target_values': 'Incorrect target values inside',
        'name': 'Please fill in name'
    }

    def _type_match_check(self, bundle):
        '''
        This check does not allow for mixed target values to be kept
        on same element.
        '''
        sqs = SearchQuerySet().filter_and(
            django_ct='targeting.publishertargetvalue',
            inventory=bundle.data['inventory'],
            django_id__in=bundle.data['targetvalues_ids']
        )

        if bundle.data['is_network']:
            sqs = sqs.filter_and(pubkey=dimensions.network)
        else:
            sqs = sqs.filter_and(pubkey=dimensions.publisher_name)

        return sqs.count() == len(bundle.data['targetvalues_ids'])

    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'No data has been given.'}

        errors = {}

        if not bundle.data.get('name'):
            errors['name'] = SetValidation.error_messages['name']

        if 'targetvalues_ids' not in bundle.data:
            errors['publishers'] = SetValidation.error_messages['publishers']

        if 'inventory' not in bundle.data:
            errors['inventory'] = SetValidation.error_messages['type']
        elif bundle.data['inventory'] not\
                in [t[0] for t in PublisherSet.TYPES]:
            errors['inventory'] = SetValidation.error_messages['wrong_type']
        if 'targetvalues_ids' in bundle.data and\
                not self._type_match_check(bundle):
            errors['target_values'] =\
                SetValidation.error_messages['target_values']

        return errors


class PublisherSetResource(ProtectedModelResource):

    targetvalues_ids = ListField(use_in='detail', default=[])
    targetvalues = ToManyField(PublishersResource, 'targetvalues',
        full=True, use_in='detail', readonly=True, default=[])

    class Meta:
        resource_name = 'sets'
        list_allowed_methods = ('get', 'post')
        details_allowed_methods = ('get', 'put')
        always_return_data = True

        queryset = PublisherSet.objects.all()
        authorization = Auth('owner')
        fields = ('id', 'name', 'inventory', 'is_network', 'blacklist')
        validation = SetValidation()
        filtering = {
            'inventory': ALL
        }

    def dehydrate_targetvalues_ids(self, bundle):
        ids = []
        for pub_id in bundle.obj.target_values.values('id'):
            ids.append(pub_id['id'])

        return ids

    def dehydrate_targetvalues(self, bundle):
        if bundle.obj.is_network:
            return self._dehydrate_networks(bundle)

        return self._dehydrate_publishers(bundle)

    def _dehydrate_publishers(self, bundle):

        publishers = []

        for publisher in bundle.obj.targetvalues:
            publishers.append({
                'id': publisher.pk,
                'inventory': publisher.inventory,
                'name': publisher.name,
                'network': publisher.network,
                'publisher_id': '{0}-{1}'.format(
                    publisher.network_id,
                    publisher.publisher_id
                ),
                'sizes': publisher.sizes,
                'positions': publisher.positions,
                'segments': publisher.segments
            })
        return publishers

    def _dehydrate_networks(self, bundle):

        networks = []

        for network in bundle.obj.targetvalues:
            network_dict = {
                'id': network.pk,
                'network': network.network,
                'network_id': network.network_id,
                'inventory': network.inventory
            }

            networks.append(network_dict)

        return networks

    def hydrate_m2m(self, bundle):
        if self.is_valid(bundle):
            target_values = TargetValue.objects.representants().filter(
                id__in=bundle.data.get('targetvalues_ids', [])
            )
            bundle.obj.target_values = target_values

    def hydrate(self, bundle):
        bundle.obj.owner = bundle.request.user.account
        return bundle
