
from polymorphic import PolymorphicManager


class CreativeManager(PolymorphicManager):

    '''
        .. warning::
            Creative Manager, works on Polymorphic Queries,
            meaning, that whenever possible, it'll return inheriting
            model instance, instead of base one!
    '''

    def campaign_related(self, campaign):
        '''
        Returns set of creatives that are used in a given campaign.
        The same creatives could be used in more than once within campaign's
        strategies but this method always returns just a distinct set.

        :param Campaign campaign: instance of Campaign model
        :rtype queryset of Creative objects
        '''
        return self.get_query_set().filter(
            is_deleted=False,
            advert__is_deleted=False,
            advert__strategy__in=campaign.strategy_visible_set,
            advert__strategy__campaign=campaign
        ).distinct()

    def strategy_related(self, strategy):
        '''
        Returns set of creatives that are used in a given strategy.
        The same creatives could be used in more than once within strategy,
        but this method always returns just a distinct set.

        :param Strategy strategy: instance of Strategy model
        :rtype queryset of Creative objects
        '''
        return self.get_query_set().filter(
            is_deleted=False,
            advert__is_deleted=False,
            advert__strategy=strategy
        ).distinct()


class NotRemovableCreativeManager(PolymorphicManager):

    def get_query_set(self):
        return super(self.__class__, self).get_query_set().filter(is_deleted=False)
