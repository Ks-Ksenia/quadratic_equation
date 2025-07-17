from space_battle.univeral_obj import UniversalObject


class MockUObject(UniversalObject):
    def __init__(self) -> None:
        self._props = {}

    def get_property(self, prop):
        return self._props[prop]

    def set_property(self, prop, value):
        self._props[prop] = value

    def __repr__(self) -> str:
        return f"MockUObject({self._props})"
