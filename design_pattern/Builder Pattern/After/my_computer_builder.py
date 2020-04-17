from builder_abs import AbsBuilder


class MyComputerBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = "Coolermaster n3000"

    def build_mainboard(self):
        self._computer.mainboard = 'MSI 970'
        self._computer.cpu = 'Intel Core i7'
        self._computer.memory = '16gb'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'Seagete 2TB'

    def install_video_drive(self):
        self._computer.video_card = 'Geforce GTX 1070'
