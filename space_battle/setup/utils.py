from space_battle.adapters import MovingObjectAdapter
from space_battle.adapters import MovingObject


def _get_move_location(universal_obj):
    return universal_obj.get_property("move_location")

def _set_move_location(universal_obj, vector) -> None:
    universal_obj.set_property("move_location", vector)

def _get_move_velocity(universal_obj):
    return universal_obj.get_property("move_velocity")

def _get_move_adapter(interface, universal_obj):
    adapter_dict = {
        MovingObject: MovingObjectAdapter
    }
    return adapter_dict[interface](universal_obj)
