import logging

from queue_ import q
from repeat_cmd import RepeatHandler, RepeatCommand
from repeat_twice_cmd import RepeatTwiceHandler, RepeatTwiceCommand
from write_log_cmd import WriteLogHandler, RecordToLog
from commands import MoveCommand
from settings import log

log_filepath = f"./homework_2/{__name__}.log"
log_handler = logging.FileHandler(log_filepath, mode='w')
log_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

log_handler.setFormatter(log_formatter)
log.addHandler(log_handler)


class TestHandler:
    def test_repeat_handler(self):
        assert not q
        try:
            cmd = MoveCommand()
            cmd.execute()
        except Exception as e:
            RepeatHandler(cmd, e.__class__).execute()

        assert q.pop().__class__ == RepeatCommand
        assert not q

    def test_repeat_cmd(self):
        assert not q
        try:
            cmd = MoveCommand()
            cmd.execute()
        except Exception as e:
            RepeatCommand(cmd, e).execute()

        assert q.pop().__class__ == RepeatTwiceCommand
        assert not q

    def test_twice_repeat_handler(self):
        assert not q
        try:
            cmd = MoveCommand()
            cmd.execute()
        except Exception as e:
            RepeatTwiceHandler(cmd, e.__class__).execute()

        assert q.pop().__class__ == RepeatTwiceCommand
        assert not q

    def test_twice_repeat_cmd(self):
        assert not q
        try:
            cmd = MoveCommand()
            cmd.execute()
        except Exception as e:
            RepeatTwiceCommand(cmd, e).execute()

        assert q.pop().__class__ == RecordToLog
        assert not q

    def test_write_log_handler(self):
        assert not q
        try:
            cmd = MoveCommand()
            cmd.execute()
        except Exception as e:
            WriteLogHandler(cmd, e.__class__).execute()

        assert q.pop().__class__ == RecordToLog
        assert not q

    def test_record_to_log(self):
        try:
            cmd = MoveCommand()
            cmd.execute()
        except Exception as e:
            RecordToLog(cmd, e.__class__).execute()

        with open(log_filepath, 'r') as log_file:
            line = log_file.readline()
            assert "Ошибка <class 'ZeroDivisionError'> для команды <commands.MoveCommand" in line

