from director import Director
from my_computer_builder import MyComputerBuilder
from low_price_computer_builder import LowPriceComputerBuilder

computer_builder = Director(MyComputerBuilder)
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

computer_builder = Director(LowPriceComputerBuilder)
computer_builder.build_computer()
low_price_computer = computer_builder.get_computer()
low_price_computer.display()

