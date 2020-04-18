from .auto_abs import AbsAuto


class NullCar(AbsAuto):
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print(f'{self._carname} does not exist')

    def stop(self):
        pass
