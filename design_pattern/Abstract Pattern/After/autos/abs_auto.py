import abc


class AbsAuto(metaclass=abc.ABCMeta):
    
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abc.abstractmethod
    def start(self):
        print(f'{self.__name} starting')

    @abc.abstractmethod
    def stop(self):
        pass
