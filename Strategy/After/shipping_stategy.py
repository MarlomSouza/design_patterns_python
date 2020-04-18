from abc import ABCMeta, abstractmethod


class ShippingStategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, order):
        """ Calculate shipping cost """
