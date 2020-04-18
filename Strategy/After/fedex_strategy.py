from shipping_stategy import ShippingStategy


class FedexStategy(ShippingStategy):
    def calculate(self, order):
        return 3.00
