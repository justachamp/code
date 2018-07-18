import sys
import inspect


def subclasses_of(cls, module_name):
    ''' Returns all subclasses of a given class (cls) in a given module.
    :param class cls: base class
    :param str module_name: module with subclasses: e.g. 'some.module'
    :returns list subclasses
    :rtype list
    '''

    def is_subclass(subcls):
        if not inspect.isclass(subcls) \
                or not issubclass(subcls, cls) \
                or subcls.__name__ == cls.__name__:
            return False
        return True

    all_classes = inspect.getmembers(sys.modules[module_name], is_subclass)
    return [c for _, c in all_classes]
