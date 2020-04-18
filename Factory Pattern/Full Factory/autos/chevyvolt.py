from .auto_abs import AbsAuto


class ChevyVolt(AbsAuto):

    def start(self):
        print(f'{self.name} starting')

    def stop(self):
        print(f'{self.name} stopping')
