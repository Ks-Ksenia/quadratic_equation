from abc import ABC, abstractmethod


class MovingObject(ABC):
    @abstractmethod
    def get_location(self):
        ...

    @abstractmethod
    def set_location(self, value):
        ...

    @abstractmethod
    def get_velocity(self):
        ...


class RotationObject(ABC):
    def get_angle(self):
        ...
    def set_angle(self, value):
        ...
    def get_angle_velocity(self):
        ...
