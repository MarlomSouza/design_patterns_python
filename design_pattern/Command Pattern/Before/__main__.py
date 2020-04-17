import sys
from command_executer import CommandExecuter

# CreateOrder
# UpdateQuantity value
# ShipOrder

executer = CommandExecuter()
executer.execute_command(sys.argv[1:])
