from autos.abs_auto import AbsAuto


class Fiesta(AbsAuto):
    def __init__(self):
        super().__init__("Fiesta")

    def start(self):
        return super().start()

    def stop(self):
        print(f'{self.name} shutting down.')
