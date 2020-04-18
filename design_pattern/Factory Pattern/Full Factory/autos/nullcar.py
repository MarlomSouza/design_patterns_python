from .auto_abs import AbsAuto

class NullCar(AbsAuto):

    def start(self):
        print(f'{self.name} does not exist')

    def stop(self):
        pass
