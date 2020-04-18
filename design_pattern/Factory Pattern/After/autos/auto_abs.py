from abc import ABCMeta, abstractmethod


class AbsAuto(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start():
        pass

    @abstractmethod
    def stop():
        pass
