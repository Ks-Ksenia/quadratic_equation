from abc import ABC, abstractmethod


class UniversalObject(ABC):
    def __init__(self):
        self.properties = {}

    @abstractmethod
    def get_property(self, property_):
        return self.properties[property_]

    @abstractmethod
    def set_property(self, property_, new_value):
        self.properties[property_] = new_value
