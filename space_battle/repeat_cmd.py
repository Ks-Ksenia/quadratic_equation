from commands import ICommand
from repeat_twice_cmd import RepeatTwiceHandler
from queue_ import q


class RepeatCommand(ICommand):
    def __init__(self, cmd, e):
        self.cmd = cmd
        self.e = e

    def execute(self, *args, **kwargs):
        try:
            self.cmd().execute()
        except Exception:
            RepeatTwiceHandler(self.cmd, self.e).execute()


class RepeatHandler:
    def __init__(self, cmd, e):
        self.cmd = cmd
        self.e = e

    def execute(self):
        q.append(RepeatCommand(self.cmd, self.e))
