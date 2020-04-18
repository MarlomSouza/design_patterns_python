from autos.abs_auto import AbsAuto


class Linconln(AbsAuto):
    def __init__(self):
        super().__init__("Linconln")

    def start(self):
        return super().start()

    def stop(self):
        print(f'{self.name} shutting down.')
