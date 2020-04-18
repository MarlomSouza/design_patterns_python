from command_abs import AbsCommand
from order_command_abs import AbsOrderCommand


class UpdateOrder(AbsCommand, AbsOrderCommand):
    name = "UpdateOrder"
    description = "UpdateOrder number"

    def __init__(self, args):
        self.newqty = args[1]

    def execute(self):
        oldqty = 5
        print("Database updated")
        print(f"Log: Previues value: {oldqty}, new value: {self.newqty} ")
