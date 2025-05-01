from constants import handlers


class ExceptionHandler:
    def handler(self, cmd, e):
        error_class = handlers[cmd.__class__][e]
        return error_class['handler'](cmd, e)
