from shipping_stategy import ShippingStategy

class UPSStrategy(ShippingStategy):
    def calculate(self, order):
        return 4.00