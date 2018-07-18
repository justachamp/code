'''
This module was created in order to limit traffic size from AppNexus. We're using AppNexus API to update
Bidder Profile and reduce traffic to fit our strategies/ads targeting. Eg. if all of our strategies are
targeting only on USA, France and Spain so we don't want any traffic from Germany.

Usage example:

    from ui.campaign import appnexus_profile_updater

    appnexus_profile_updater.update()

'''

from etc.config import settings

from ui.campaign.models import Advert, Strategy
from adserving.bidder.appnexus_api import api


def get_ads_sizes():
    """Getting unique sizes from all active ads."""

    sizes = set()

    for advert in filter(lambda adv: adv.state.is_running, Advert.objects.all()):
        sizes.add((advert.width, advert.height))

    return [{'width': w, 'height': h} for w, h in sizes]


def get_locations(running_strategies):
    '''
    Getting unique countries and regions from all targeted strategies.

    :param list running_strategies: List of targeted Strategy instances

    :rtype: tuple
    :return: (
        [{'country': 'CA'}, {...}, ...],
        [{'region': 'CA:AB'}, {...}, ...],
    )
    '''

    countries = set()
    regions = set()

    for strategy in running_strategies:

        included_countries, included_regions = strategy.get_appnexus_locations()

        if not included_countries:
            # this strategy is targeting on all countries, so we can't limit the traffic by countries
            return [], []

        countries.update(included_countries)
        regions.update(included_regions)

    if not countries:
        return [], []

    if None in regions:
        # at least one strategy is not targeting on regions, so we can't limit the traffic by regions
        return (
            [{'country': c} for c in countries],
            [],
        )

    return (
        [{'country': c} for c in countries],
        [{'region': r} for r in regions],
    )


def get_segments(running_strategies):
    '''
    Getting unique included segments from all running strategies.

    ..warning:
        If all strategies have included segments, a sum of them is set in
        appnexus profile, otherwise no segments profile is set.

        We are not setting excludes in appnexus profile, because we could
        only exclude segments that are excluded in all strategies.
        It would complicate the implementation and not filter out much traffic.

    :param list running_strategies: List of running Strategy instances

    :rtype: list of dictionaries or empty list
    :return: [{'id': 43, 'action': 'include'}, {'id': 50, 'action': 'include'}, ...]
    '''

    segments = set()

    for strategy in running_strategies:

        strategy_segments = strategy.get_appnexus_segments()

        if not strategy_segments:
            # this strategy is targeting on all segments, so we can't limit the traffic
            return []

        segments.update(strategy_segments)

    if not segments:
        return []

    id_with_action = lambda appnexus_id: {'id': appnexus_id, 'action': 'include'}

    return map(id_with_action, segments)


WEB_TYPES = {'web'}
FACEBOOK_TYPES = {'facebook_sidebar'}
MOBILE_TYPES = {'mobile_web', 'mobile_app'}
SUPPLY_TYPES = {
    Strategy.SITE: WEB_TYPES,
    Strategy.MOBILE: MOBILE_TYPES,
    Strategy.FACEBOOK: FACEBOOK_TYPES
}


def get_supply_types(running_strategies):
    """
    Get supply types to target on.

    .. note::

        If we don't have any strategy set, we want all supply types we can work with.

    :param list running_strategies: List of running Strategy instances

    :returns: set of appnexus supply_types to include
    :rtype: list
    """

    supply_types = set()

    for strategy in running_strategies:
        supply_types = supply_types | SUPPLY_TYPES[strategy.type]

    return list(supply_types or WEB_TYPES | MOBILE_TYPES)


def build_profile():
    """
    Set all profile fields and call API update.

    :return: dictionary with profile values to be set
    :rtype: dict
    """

    running_strategies = Strategy.running()

    # Dictionary containing all AppNexus bidder profile fields which will be updated
    # https://wiki.appnexus.com/pages/viewpage.action?title=Bidder+Profile+Service&spaceKey=adnexusdocumentation
    # Use lowercase 'id' (even documentation says it's capital 'ID')!
    profile = {
        'id': settings.appnexus_profile_id,
        # set passthrough to 0 if we won't bid on anything
        'passthrough_percent': 0,
        'description': 'Automatic profile (off)',
        'country_action': 'exclude',
        'region_action': 'exclude',
        # supply_type
        'supply_type_action': 'include',
        'supply_type_targets': get_supply_types(running_strategies),
    }

    # ads sizes
    profile['size_targets'] = get_ads_sizes()

    # no size targets means no active advert, which means we won't bid on anything anyway.
    if profile['size_targets']:

        # passthrough from settings.
        profile['passthrough_percent'] = settings.appnexus_profile_passthrough
        profile['description'] = 'Automatic profile (on)'

    # locations
    profile['country_targets'], profile['region_targets'] = get_locations(running_strategies)
    if profile['country_targets']:
        profile['country_action'] = 'include'

    if profile['region_targets']:
        profile['region_action'] = 'include'

    # segments
    profile['segment_boolean_operator'] = 'or'
    profile['segment_targets'] = get_segments(running_strategies)

    return profile


def update():
    """Set new bidding profile for appnexus."""
    return api.profile_set(**build_profile())
