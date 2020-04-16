import abc


class AbsObserver(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def udpate(self, value):
        pass
