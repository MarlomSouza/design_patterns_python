from command_abs import AbsCommand
from order_command_abs import AbsOrderCommand


class CreateOrder(AbsCommand, AbsOrderCommand):
    name = "CreateOrder"
    description = "Creating a order"

    def __init__(self, args):
        self.value = args[1]

    def execute(self):
        print(f"Creating an order {self.value}")
