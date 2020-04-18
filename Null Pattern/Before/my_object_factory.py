from my_class import MyClass


class MyObjectFactory(object):

    @staticmethod
    def create_object(value):
        if value == 'myclass':
            return MyClass()
        return None
