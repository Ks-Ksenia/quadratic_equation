import pytest

from space_battle.ioc_container.ioc import IoC
from space_battle.commands import MoveCommand
from space_battle.movement import MovingObject
from space_battle.vector import Vector
from space_battle.setup.moveble import ioc_setup_movable
from space_battle.setup.adapters import ioc_setup_adapters
from space_battle.exceptions import CommandException
from tests.utils import make_movable_uobject


@pytest.fixture(autouse=True)
def _ioc_setup() -> None:
    ioc_setup_movable()
    ioc_setup_adapters()


def test_movement():
    uobj = make_movable_uobject(Vector(12, 5), Vector(-7, 3))

    movable = IoC.resolve("Adapter", MovingObject, uobj)
    move = MoveCommand(movable)
    move.execute()

    assert movable.get_location() == Vector(5, 8)

def test_get_move_location_error():
    uobj = make_movable_uobject(Vector(12, 5), Vector(-7, 3))

    def get_property_side_effect(prop):
        if prop == "move_location":
            raise CommandException
        return original_get_property(prop)

    original_get_property = uobj.get_property
    uobj.get_property = get_property_side_effect

    with pytest.raises(Exception):
        MoveCommand(IoC.resolve("Adapter", MovingObject, uobj)).execute()


def test_move_location_error() -> None:
    uobj = make_movable_uobject(Vector(12, 5), Vector(-7, 3))

    def set_property_side_effect(prop, value):
        if prop == "move_location":
            raise CommandException
        return original_set_property(prop, value)

    original_set_property = uobj.set_property
    uobj.set_property = set_property_side_effect

    with pytest.raises(Exception):
        MoveCommand(IoC.resolve("Adapter", MovingObject, uobj)).execute()


def test_get_move_velocity_error() -> None:
    uobj = make_movable_uobject(Vector(12, 5), Vector(-7, 3))

    def get_property_side_effect(prop):
        if prop == "move_velocity":
            raise CommandException
        return original_get_property(prop)

    original_get_property = uobj.get_property
    uobj.get_property = get_property_side_effect

    with pytest.raises(Exception):
        MoveCommand(IoC.resolve("Adapter", MovingObject, uobj)).execute()
