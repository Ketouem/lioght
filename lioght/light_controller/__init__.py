import abc


class LightControllerRegistry(type):

    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        """
            @param name: Name of the class
            @param bases: Base classes (tuple)
            @param attrs: Attributes defined for the class
        """
        new_cls = type.__new__(cls, name, bases, attrs)
        if name != 'LightController':
            vendor = attrs.get('VENDOR')
            cls.REGISTRY[(name, vendor)] = new_cls
        return new_cls

    @classmethod
    def get_controller_class(cls, vendor):
        for kls_name, v in cls.REGISTRY:
            if v and v.lower() == vendor.lower():
                return cls.REGISTRY[(kls_name, v)]


class LightController(object):

    VENDOR = None

    __metaclass__ = LightControllerRegistry

    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def switch_on(self, light_id, *args, **kwargs):
        pass

    @abc.abstractmethod
    def switch_off(self, light_id, *args, **kwargs):
        pass

    @abc.abstractmethod
    def change_color(self, light_id, color, *args, **kwargs):
        pass
