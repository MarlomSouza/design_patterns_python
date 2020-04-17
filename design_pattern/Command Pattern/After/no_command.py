from command_abs import AbsCommand


class NoCommand(AbsCommand):
    def __init__(self, args):
        self._command = args[0]

    def execute(self):
        print(f"There no command with name {self._command}")
