from .abs_factory import AbsFactory
from autos.gm.cadillac import CadillacCTS
from autos.gm.camaro import ChevyCamaro
from autos.gm.spark import ChevySpark


class GmFactory(AbsFactory):

    @staticmethod
    def create_economy():
        return ChevySpark('ChevySpark')

    @staticmethod
    def create_sport():
        return ChevyCamaro('ChevyCamaro')

    @staticmethod
    def create_luxury():
        return CadillacCTS('CadillacCTS')
