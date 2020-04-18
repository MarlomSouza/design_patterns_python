class Computer(object):
    def __init__(self, case, mainboard, cpu, memory, hard_drive, video_card):
        self.case = case
        self.mainboard = mainboard
        self.cpu = cpu
        self.memory = memory
        self.hard_drive = hard_drive
        self.video_card = video_card

    def display(self):
        print("Computer: ")
        print(f"CASE: {self.case}")
        print(f"MAINBOARD: {self.mainboard}")
        print(f"CPU: {self.cpu}")
        print(f"MEMORY: {self.memory}")
        print(f"HARD DRIVE: {self.hard_drive}")
        print(f"VIDEO CARD: {self.video_card}")
