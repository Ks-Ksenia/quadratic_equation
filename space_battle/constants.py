from repeat_cmd import RepeatHandler

from commands import MoveCommand, RotateCommand


handlers = {
    MoveCommand: {
        ZeroDivisionError: {"handler": RepeatHandler},
    },
    RotateCommand: {
        KeyError: {"handler": RepeatHandler},
    },
}