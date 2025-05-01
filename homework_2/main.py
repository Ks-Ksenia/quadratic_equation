from handler import ExceptionHandler
from queue_ import q
from commands import MoveCommand, RotateCommand


def command_processing(queue):
    while queue:
        try:
            cmd = q.popleft()
            cmd.execute()
        except Exception as e:
            ExceptionHandler().handler(cmd, e.__class__).execute()


q.append(MoveCommand())
q.append(RotateCommand())

command_processing(q)
