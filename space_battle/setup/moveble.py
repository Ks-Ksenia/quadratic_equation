from space_battle.ioc_container.ioc import IoC
from space_battle.commands import LambdaCommand
from space_battle.setup.utils import _get_move_location, _get_move_velocity, _set_move_location


def ioc_setup_movable():
    IoC.resolve(
        "IoC.Scope.Register",
        "MovingObject.location.get",
        _get_move_location,
    ).execute()

    IoC.resolve(
        "IoC.Scope.Register",
        "MovingObject.location.set",
        LambdaCommand(_set_move_location).setup,
    ).execute()

    IoC.resolve(
        "IoC.Scope.Register",
        "MovingObject.velocity.get",
        _get_move_velocity,
    ).execute()
