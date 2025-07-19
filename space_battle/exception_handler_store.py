class NoSuitableExceptionHandlerError(Exception):
    def __init__(self, cmd, exc):
        super().__init__(
            f"No suitable exception handler found for Command: {cmd} and Exception: {exc}"
        )


class ExceptionHandlerStore:
    def __init__(self) -> None:
        self._handlers = {}
        self._default_command_handlers= {}
        self._default_exception_handlers= {}
        self._default_handler = None

    def create_handler_command(self, cmd, exc):
        handler = (
            self._handlers.get(type(cmd), {}).get(type(exc), None)
            or self._default_exception_handlers.get(type(exc), None)
            or self._default_command_handlers.get(type(cmd), None)
            or self._default_handler
        )
        if not handler:
            raise NoSuitableExceptionHandlerError(cmd, exc)

        return handler(cmd, exc)

    def register_handler(self, ct, et, handler):
        self._handlers.setdefault(ct, {})[et] = handler

    def register_default_command_handler(self, ct, handler):
        self._default_command_handlers[ct] = handler

    def register_default_exception_handler(self, et, handler):
        self._default_exception_handlers[et] = handler

    def register_default_handler(self, handler) -> None:
        self._default_handler = handler
