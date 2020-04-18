from .abs_factory import AbsFactory
from autos.ford.fiesta import Fiesta
from autos.ford.linconln import Linconln
from autos.ford.mustang import Mustang


class FordFactory(AbsFactory):

    @staticmethod
    def create_economy():
        return Fiesta()

    @staticmethod
    def create_sport():
        return Mustang()

    @staticmethod
    def create_luxury():
        return Linconln()
