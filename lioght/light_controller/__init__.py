import abc


class LightControllerRegister(type):

    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        """
            @param name: Name of the class
            @param bases: Base classes (tuple)
            @param attrs: Attributes defined for the class
        """
        new_cls = type.__new__(cls, name, bases, attrs)
        cls.REGISTRY[name] = new_cls
        return new_cls


class LightController(object):
    __metaclass__ = LightControllerRegister

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


def get_controller_class(product_name):
    return LightControllerRegister.REGISTRY.get(product_name.lower())
