from abc import ABCMeta, abstractmethod


class AbsCommand(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass
