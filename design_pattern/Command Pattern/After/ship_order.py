from command_abs import AbsCommand
from order_command_abs import AbsOrderCommand


class ShipOrder(AbsCommand, AbsOrderCommand):
    name = "ShipOrder"
    description = "Shipping a order"

    def __init__(self, args):
        self.value = args[1]

    def execute(self):
        print(f"Shippinh an order {self.value}")
