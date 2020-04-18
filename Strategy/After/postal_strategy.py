from shipping_stategy import ShippingStategy


class PostalStrategy(ShippingStategy):
    def calculate(self, order):
        return 5.00
