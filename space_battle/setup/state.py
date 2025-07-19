from space_battle.exception_handler_store import ExceptionHandlerStore
from space_battle.ioc_container.ioc import IoC
from space_battle.event_loop import EventLoop


def ioc_setup_game_state():
    exception_handler_store = ExceptionHandlerStore()

    def _get_exception_handler_store():
        return exception_handler_store

    IoC.resolve(
        "IoC.Scope.Register",
        "ExceptionHandlerStore",
        _get_exception_handler_store,
    ).execute()

    event_loop = EventLoop(exception_handler_store)

    def _get_event_loop():
        return event_loop

    IoC.resolve(
        "IoC.Scope.Register",
        "EventLoop",
        _get_event_loop,
    ).execute()
