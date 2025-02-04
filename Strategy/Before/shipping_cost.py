from shipper import Shipper
from order import Order


class ShippingCost(object):
    def shipping_cost(self, order: Order):
        if order.shipper == Shipper.fedex:
            return self._fedex_cost(order)

        if order.shipper == Shipper.ups:
            return self._ups_cost(order)

        if order.shipper == Shipper.postal:
            return self._postal_cost(order)
        else:
            raise ValueError('Invalid shipper %s', order.shipper)

    def _fedex_cost(self, order):
        return 3.00

    def _ups_cost(self, order):
        return 4.00

    def _postal_cost(self, order):
        return 5.00
