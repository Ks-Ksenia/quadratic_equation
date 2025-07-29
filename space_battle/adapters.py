from abc import abstractmethod
from math import cos, sin
from space_battle.vector import Vector

from space_battle.movement import MovingObject, RotationObject, FuelObject, ChangeVelocityObject
from space_battle.ioc_container.ioc import IoC


class MovingObjectAdapter(MovingObject):
    def __init__(self, universal_obj):
        self.universal_obj = universal_obj

    def get_location(self):
        return IoC.resolve(
            "MovingObject.location.get",
            self.universal_obj)

    def set_location(self, new_location):
        return IoC.resolve("MovingObject.location.set",
                           self.universal_obj,
                           new_location).execute()

    def get_velocity(self):
        return IoC.resolve("MovingObject.velocity.get", self.universal_obj)


class RotationObjectAdapter(RotationObject):
    def __init__(self, universal_obj):
        self.universal_obj = universal_obj

    @abstractmethod
    def get_angle(self):
        return self.universal_obj.get_property("angle")

    @abstractmethod
    def set_angle(self, new_angle):
        self.universal_obj.set_property("angle", new_angle)

    @abstractmethod
    def get_angle_velocity(self):
        velocity = self.universal_obj.get_property("velocity")
        angle = self.universal_obj.get_property("angle")
        return Vector(velocity * cos(angle), sin(angle))


class FuelObjectAdapter(FuelObject):
    def __init__(self, universal_obj):
        self.universal_obj = universal_obj

    @abstractmethod
    def get_fuel_quantity(self):
        return self.universal_obj.get_property("fuel_quantity")

    @abstractmethod
    def set_fuel_quantity(self, new_angle):
        self.universal_obj.set_property("fuel_quantity", new_angle)

    @abstractmethod
    def get_fuel_consumption(self):
        return self.universal_obj.get_property("fuel_consumption")

    @abstractmethod
    def set_fuel_consumption(self, new_angle):
        self.universal_obj.set_property("fuel_consumption", new_angle)


class ChangeVelocityAdapter(ChangeVelocityObject):
    def __init__(self, universal_obj):
        self.universal_obj = universal_obj

    @abstractmethod
    def get_velocity(self):
        ...

    @abstractmethod
    def set_velocity(self, value):
        ...


class AutoGenerateAdapter(MovingObject):
    def __init__(self, universal_obj):
        self.universal_obj = universal_obj

    def get_velocity(self):
        return IoC.resolve("MovingObject.velocity.get", self.universal_obj)

    def get_location(self):
        return IoC.resolve("MovingObject.location.get", self.universal_obj)

    def set_location(self, value):
        return IoC.resolve("MovingObject.location.set", self.universal_obj, value).execute()
