from order import Order


class ShippingCost(object):
    def __init__(self, shipping_stategy):
        self._shipping_stategy = shipping_stategy

    def shipping_cost(self, order):
        return self._shipping_stategy.calculate(order)
