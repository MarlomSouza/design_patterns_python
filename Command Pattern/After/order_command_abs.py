from abc import ABCMeta, abstractmethod


class AbsOrderCommand(object):
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass
