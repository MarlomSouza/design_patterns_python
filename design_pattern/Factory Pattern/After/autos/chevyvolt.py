from .auto_abs import AbsAuto


class ChevyVolt(AbsAuto):
    def start(self):
        print('Chevy volt starting')

    def stop(self):
        print('Chevy volt stopping')
