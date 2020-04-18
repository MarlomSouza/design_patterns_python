from factories.ford_factory import FordFactory
from factories.gm_factory import GmFactory


for factory in GmFactory, FordFactory:
    for car in factory.create_economy(), factory.create_luxury(), factory.create_sport():
        car.start()
        car.stop()

