from settings import log
from commands import ICommand
from queue_ import q


class RecordToLog(ICommand):
    def __init__(self, cmd, e):
        self.cmd = cmd
        self.e = e

    def execute(self):
        log.error(f"Ошибка {self.e} для команды {self.cmd}")


class WriteLogHandler:
    def __init__(self, cmd, e):
        self.cmd = cmd
        self.e = e

    def execute(self):
        q.append(RecordToLog(self.cmd, self.e))
