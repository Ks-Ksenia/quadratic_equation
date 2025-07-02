from space_battle.commands import LambdaCommand
from space_battle.exceptions import IoCResolveError


def _default_ioc_resolve_strategy(dependency_name, *args, **kwargs):
    if dependency_name == "Обновить IoC Resolve стратегию":
        return LambdaCommand(_update_ioc_resolve_strategy).setup(*args, **kwargs)
    raise IoCResolveError(f"Зависимость '{dependency_name}' не найдена")


def _update_ioc_resolve_strategy(strategy_updater):
    new_strategy = strategy_updater(IoC.resolve_strategy)
    IoC.resolve_strategy = new_strategy


class IoC:
    resolve_strategy = _default_ioc_resolve_strategy

    @classmethod
    def resolve(cls, dependency_name, *args, **kwargs):
        try:
            return cls.resolve_strategy(dependency_name, *args, **kwargs)
        except Exception as e:
            raise IoCResolveError(
                f"Ошибка в зависимости {dependency_name}: {e}"
            )
