from space_battle.ioc_container.ioc import IoC
from space_battle.setup.utils import _get_type_of_move_adapter

def ioc_setup_adapters():
    IoC.resolve("IoC.Scope.Register", "Adapter", _get_type_of_move_adapter).execute()
