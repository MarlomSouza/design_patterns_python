from my_class import MyClass
from null_class import NullClass


class MyObjectFactory(object):

    @staticmethod
    def create_object(value):
        if value == 'myclass':
            return MyClass()
        return NullClass()
