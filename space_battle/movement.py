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
    @abstractmethod
    def get_angle(self):
        ...

    @abstractmethod
    def set_angle(self, value):
        ...

    @abstractmethod
    def get_angle_velocity(self):
        ...


class FuelObject(ABC):
    @abstractmethod
    def get_fuel_quantity(self):
        ...

    @abstractmethod
    def set_fuel_quantity(self, value):
        ...

    @abstractmethod
    def get_fuel_consumption(self):
        ...

    @abstractmethod
    def set_fuel_consumption(self, value):
        ...


class ChangeVelocityObject(MovingObject, RotationObject):
    @abstractmethod
    def get_velocity(self):
        ...

    @abstractmethod
    def set_velocity(self, value):
        ...