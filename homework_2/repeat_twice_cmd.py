from write_log_cmd import WriteLogHandler
from queue_ import q


class RepeatTwiceCommand:
    def __init__(self, cmd, e):
        self.cmd = cmd
        self.e = e

    def execute(self, *args, **kwargs):
        try:
            self.cmd().execute()
        except Exception:
            WriteLogHandler(self.cmd, self.e).execute()


class RepeatTwiceHandler:
    def __init__(self, cmd, e):
        self.cmd = cmd
        self.e = e

    def execute(self):
        q.append(RepeatTwiceCommand(self.cmd, self.e))
