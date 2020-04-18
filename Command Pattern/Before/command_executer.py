class CommandExecuter(object):

    def execute_command(self, args):
        if args[0] == "CreateOrder":
            self.create_order()
        elif args[0] == "UpdateQuantity":
            self.update_quantity(args[1])
        elif args[0] == "ShipOrder":
            self.ship_order()
        else:
            print(f"Unregonized command {args[0]}")

    def create_order(self):
        print("Order Created")

    def update_quantity(self, value):
        print(value)
        old_value = 5
        print(f"Value updated from {old_value} to {value}")

    def ship_order(self):
        print("Order shipped")
