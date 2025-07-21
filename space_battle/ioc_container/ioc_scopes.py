import threading
from contextvars import ContextVar

from space_battle.commands import LambdaCommand
from space_battle.ioc_container.ioc import IoC
from space_battle.exceptions import IoCScopedError


class Scope:
    def __init__(self, name, store):
        self.name = name
        self.store = store


class ScopedIoC:
    _current_scope = ContextVar("_current_scope", default=None)

    def __init__(self):
        self._current_scope.set(None)
        self._root_scope = Scope("Root", {})

        self._setup_lock = threading.Lock()
        self._is_setup: bool = False

    def setup(self):
        with self._setup_lock:
            if self._is_setup:
                return

            default_store = {
                "IoC.Scope.Current.Set": LambdaCommand(self._set_scope).setup,
                "IoC.Scope.Current.Clear": LambdaCommand(self._clear_scope).setup,
                "IoC.Scope.Current": self._get_current_scope,
                "IoC.Scope.Parent": self._get_parent_scope,
                "IoC.Scope.Create": self._create_scope,
                "IoC.Scope.Register": LambdaCommand(self._register_dependency).setup,
                "Adapter": LambdaCommand(self._register_dependency).setup,
            }

            self._root_scope.store.update(default_store)

            def update_ioc_strategy(_old_strategy):
                return self._resolve_strategy

            IoC.resolve("Обновить IoC Resolve стратегию", update_ioc_strategy).execute()

            self._is_setup = True

    def _set_scope(self, scope):
        self._current_scope.set(scope)

    def _clear_scope(self):
        self._current_scope.set(None)

    def _get_current_scope(self):
        return self._current_scope.get() or self._root_scope

    def _get_parent_scope(self):
        raise IoCScopedError("Корневая область не имеет родительского области")

    def _create_scope(self, name, parent=None):
        new_scope = Scope(name, {})
        if not parent:
            parent = self._get_current_scope()
        new_scope.store["IoC.Scope.Parent"] = lambda: parent
        return new_scope

    def _register_dependency(self, dependency_name, dependency_func):
        self._get_current_scope().store[dependency_name] = dependency_func

    def _resolve_strategy(self, dependency_name, *args, **kwargs):
        scope = self._get_current_scope()
        while True:
            if strategy := scope.store.get(dependency_name):
                return strategy(*args, **kwargs)
            if scope is self._root_scope:
                raise IoCScopedError(f"Не удалось разрешить зависимость в '{dependency_name}'")
            scope = scope.store["IoC.Scope.Parent"]()

_scoped_ioc = ScopedIoC()
setup = _scoped_ioc.setup
