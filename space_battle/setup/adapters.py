from space_battle.ioc_container.ioc import IoC
from space_battle.setup.utils import _get_move_adapter
from space_battle.movement import MovingObject
from space_battle.adapters import MovingObjectAdapter

def ioc_setup_adapters():

    IoC.resolve("IoC.Scope.Register", "Adapter", _get_move_adapter).execute()

