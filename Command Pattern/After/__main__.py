from create_order import CreateOrder
from ship_order import ShipOrder
from update_order import UpdateOrder
from no_command import NoCommand
import sys


def get_commands():
    commands = [CreateOrder, UpdateOrder, ShipOrder]
    return dict([cls.name, cls] for cls in commands)


def print_usage(commands):
    print("Commands: ")
    print(commands.values())
    for command in commands.values():
        print(-f" {command}")


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)


commands = get_commands()
if len(sys.argv) < 2:
    print_usage(commands)
    exit()

command = parse_command(commands, sys.argv[1:])
command.execute()
