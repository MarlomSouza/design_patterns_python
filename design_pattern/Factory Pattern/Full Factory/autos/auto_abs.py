import abc


class AbsAuto(metaclass=abc.ABCMeta):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abc.abstractmethod
    def start(self):
        print(f'{self.name} starting')

    @abc.abstractmethod
    def stop(self):
        print(f'{self.name} stopping')
