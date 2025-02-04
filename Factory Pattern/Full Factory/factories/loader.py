from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .abs_factory import AbsFactory


def load_factory(factory_name):
    try:
        factory_module = import_module('.' + factory_name, 'factories')
    except ImportError:
        factory_module = import_module('.null_factory', 'factories')

    classes = getmembers(
        factory_module, lambda b: isclass(b) and not isabstract(b))

    for name, _class in classes:
        if issubclass(_class, AbsFactory):
            return _class()

# TODO:Create function to send Unknown auto to null car