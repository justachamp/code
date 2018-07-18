from adserving.bidder.appnexus_api import AppNexApiError, api
from ui.targeting.models import (
    PublisherTargetValue, TargetValue, TargetValueQueryError
)
from etc.constants import (
    SELF_TRANSLATING_PUBLISHERS_EXCHANGES, BASIC_TARGETVALUE_EXCHANGE,
    NETWORK_IDS
)
from etc import dimensions


def translate_fixed_networks():
    '''
    Translates all networks/publishers from exchanges
    that have their network name fixed
    '''

    # let us iterate all exchanges that provide us with network name
    # in BidRequest ()
    for exchange in SELF_TRANSLATING_PUBLISHERS_EXCHANGES:
        # get all untranslated publishers from that exchange
        publishers = PublisherTargetValue.objects.get_unrepresented_values(
            exchange, dimensions.g_publisher
        )
        for untranslated_publisher in publishers:

            # separate network type
            network_value = untranslated_publisher[:2]

            # get representant
            network = PublisherTargetValue.objects.get_representant_value_list(
                exchange, dimensions.g_publisher, network_value
            )

            # if does not exists, lets create it quickly
            if not network:

                inventory = get_inventory(network_value[0])

                # substitute representant with relevant values
                network = [inventory, NETWORK_IDS[int(network_value[-1])]]
                PublisherTargetValue.objects\
                    .create_value_with_custom_representant(
                        exchange, dimensions.g_publisher, network_value,
                        network
                    )

            # substitute publisher with relevant values
            representant_publisher = list(network)
            representant_publisher.append(untranslated_publisher[-1])

            PublisherTargetValue.objects.create_value_with_custom_representant(
                exchange, dimensions.g_publisher, untranslated_publisher,
                representant_publisher
            )


def get_inventory(value):
    # get inventory representant
    inventory = TargetValue.objects.get_representant_value_list(
        BASIC_TARGETVALUE_EXCHANGE,
        dimensions.inventory,
        [value]
    )
    return inventory[0]


NETWORK_CACHE = {}


def translate_appnexus_network(network_value):
    '''
    Tries to translate values for network:
        - first within kept TargetValue (PublisherTargetValue),
        - if that surch gives nothing, tries AppNexus API

    :param list network_value: list of values as per
        dimensions.hierarchy.g_publisher, but limited to first two elements

    :returns: translated network values
    '''
    network = PublisherTargetValue.objects.get_representant_value_list(
        'appnexus', dimensions.g_publisher, network_value
    )
    if network:
        return network

    # see dimensions.hierarchy.g_publisher:
    #   [inventory, network, publisher_name]
    # selling_member_id to be consistent with
    #   AppNexus bidRequest field name
    selling_member_id = int(network_value[1])

    member = NETWORK_CACHE.get(selling_member_id)
    if member is None:
        try:
            response = api.member(selling_member_id)
            NETWORK_CACHE[selling_member_id] = response
        except AppNexApiError as e:
            print 'Error: {0} for selling_member_id {1}'.format(e, selling_member_id)
            return

        if response['status'] != 'OK':
            print 'API responded not OK for selling_member_id {0} Bidrequest: {1}'.format(
                selling_member_id, response)
            return

        # Docs says 'platform_members', with list
        # but in reality it is 'platform_member' with dict only
        member = response['platform_member']

    if member['primary_type'] == dimensions.network:

        inventory = get_inventory(network_value[0])

        network = [inventory, member['name']]

        PublisherTargetValue.objects.create_value_with_custom_representant(
            'appnexus', dimensions.g_publisher, network_value, network
        )

        return network


def appnexus_publishers_translate():
    '''
    Updates TargetingValue.category == dimensions.network with proper
    representants.

    Using prints all the time because celery breaks our logging.
    '''
    NETWORK_CACHE.clear()

    # Prepopulate network cache with everything we care about:
    NETWORK_CACHE.update({m['id']: m for m in api.members()})
    cache_size = len(NETWORK_CACHE)

    print 'Prepopulated network cache with %s entries.' % cache_size

    # read all untranslated publishers
    publishers = PublisherTargetValue.objects.get_unrepresented_values(
        'appnexus',
        dimensions.g_publisher)
    print 'updating {0} publishers translations...'.format(len(publishers))

    for untranslated_publisher in publishers:

        network = translate_appnexus_network(untranslated_publisher[:2])

        if network and len(untranslated_publisher) > len(network):

            representant_publisher = list(network)
            representant_publisher.append(untranslated_publisher[-1])

            try:

                PublisherTargetValue.objects\
                    .create_value_with_custom_representant(
                        'appnexus', dimensions.g_publisher,
                        untranslated_publisher, representant_publisher
                    )

            except TargetValueQueryError:
                print '''[NETWORK_TRANSLATION] Appnexus publisher {0}
                    wants representation that is raw exchange value {1}
                    '''.format(untranslated_publisher, representant_publisher)

    print ('Finished appnexus publishers translation. Had to query for extra %s members.' %
           (len(NETWORK_CACHE) - cache_size))
    NETWORK_CACHE.clear()
