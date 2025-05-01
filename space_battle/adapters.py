from abc import abstractmethod
from math import cos, sin

from movement import MovingObject, RotationObject
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
