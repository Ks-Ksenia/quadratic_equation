from queue import Queue
from threading import Thread

from space_battle.commands import ICommand


class EventLoop:
    def __init__(self, exception_handler_store):
        self._command_queue = Queue()
        self._exception_handler_store = exception_handler_store

        self._before_hooks = []
        self._after_hooks = []

        self._stop_func = lambda: False

    def add_before_hook(self, hook):
        self._before_hooks.append(hook)

    def add_after_hook(self, hook):
        self._after_hooks.append(hook)

    def put_command(self, cmd):
        self._command_queue.put(cmd)

    def run_forever(self):
        self._run()

    def run_until_complete(self):
        self._stop_func = lambda: self._command_queue.empty()
        self._run()

    def set_hard_stop(self):
        self._stop_func = lambda: True

    def set_soft_stop(self):
        self._stop_func = lambda: self._command_queue.empty()

    def _run(self):
        for hook in self._before_hooks:
            hook()

        while not self._stop_func():
            cmd = self._command_queue.get()
            try:
                cmd.execute()
            except Exception as exc:
                self._exception_handler_store.create_handler_command(cmd, exc).execute()

        for hook in self._after_hooks:
            hook()


class RunEventLoopInThreadCommand(ICommand):
    def __init__(self, event_loop):
        self._event_loop = event_loop

    def execute(self):
        thread = Thread(target=self._event_loop.run_forever)
        thread.start()


class SoftStopEventLoopCommand(ICommand):
    def __init__(self, event_loop):
        self._event_loop = event_loop

    def execute(self):
        self._event_loop.set_soft_stop()


class HardStopEventLoopCommand(ICommand):
    def __init__(self, event_loop):
        self._event_loop = event_loop

    def execute(self):
        self._event_loop.set_hard_stop()
