

class BaseState(object):

    def _make_state_dict(self, state, fields_bool, fields_count):
        '''
        Returns a dict of states for Campaign/Strategy/Advert Resources

        :param state: instance of object state model
        (Campaign/Strategy/AdvertState)
        :param list fields_bool: list of strings with names of bool properties
        in coresponding State model
        :param list fields_count: list of strings with name of properties in
        State model which are list of objects.

        Example response: {'has_budget': True, 'creatives_audited': 5},
        where first item is from fields_bool list and second from fields_count

        '''
        state_dict = {}

        for field in fields_bool:
            state_dict.update({field: getattr(state, field)})

        for field in fields_count:
            state_dict.update({field: len(getattr(state, field))})

        return state_dict

    def to_dict(self):
        '''
            Method should return state object converted to dictionary
            through _make_state_dict
        '''
        raise NotImplementedError
