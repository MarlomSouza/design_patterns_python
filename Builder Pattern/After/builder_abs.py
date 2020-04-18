from abc import ABCMeta, abstractmethod
from computer import Computer


class AbsBuilder(object):
    __metaclass__ = ABCMeta

    def get_computer(self):
        return self._computer

    def new_computer(self):
        self._computer = Computer()

    @abstractmethod
    def build_mainboard(self):
        pass

    @abstractmethod
    def get_case(self):
        pass

    @abstractmethod
    def install_mainboard(self):
        pass

    @abstractmethod
    def install_hard_drive(self):
        pass

    @abstractmethod
    def install_video_drive(self):
        pass
