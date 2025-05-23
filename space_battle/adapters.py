from abc import abstractmethod
from math import cos, sin

from movement import MovingObject, RotationObject, FuelObject, ChangeVelocityObject
from vector import Vector


class MovingObjectAdapter(MovingObject):
    def __init__(self, universal_obj):
        self.universal_obj = universal_obj

    @abstractmethod
    def get_location(self):
        return self.universal_obj.get_property("location")

    @abstractmethod
    def set_location(self, new_location):
        self.universal_obj.set_property("location", new_location)

    @abstractmethod
    def get_velocity(self):
        velocity = self.universal_obj.get_property("velocity")
        location = self.universal_obj.get_property("location")
        return Vector(velocity.x + location.x, velocity.y + location.y)


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
