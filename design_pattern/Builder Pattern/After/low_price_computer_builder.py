from builder_abs import AbsBuilder


class LowPriceComputerBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = "IN WIN BP655"

    def build_mainboard(self):
        self._computer.mainboard = 'Low Price MainBoard'
        self._computer.cpu = 'Intel Core i3'
        self._computer.memory = '4gb'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'Seagete 120 GB'

    def install_video_drive(self):
        self._computer.video_card = 'On board'
