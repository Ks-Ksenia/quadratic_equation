from abc import ABC, abstractmethod
from space_battle.exceptions import CommandException


class ICommand(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        ...


class MoveCommand(ICommand):
    @abstractmethod
    def execute(self, *args, **kwargs):
        ...


class RotateCommand(ICommand):
    @abstractmethod
    def execute(self, *args, **kwargs):
        ...

class CheckFuelCommand(ICommand):
    def __init__(self, obj):
        self.obj = obj

    @abstractmethod
    def execute(self, *args, **kwargs):
        current_fuel = self.obj.get_fuel_quantity()
        consumption_fuel =self.obj.get_fuel_consumption()
        if current_fuel < consumption_fuel:
            raise CommandException(f"Недостаточно топлива для объекта {self.obj}: "
                             f"текущее значение - {current_fuel} , необходимо списать - {consumption_fuel}")


class BurnFuelCommand(ICommand):
    def __init__(self, obj):
        self.obj = obj

    @abstractmethod
    def execute(self, *args, **kwargs):
        current_fuel = self.obj.get_fuel_quantity()
        consumption_fuel =self.obj.get_fuel_consumption()
        self.obj.set_fuel_quantity(current_fuel - consumption_fuel)


class MacroCommand(ICommand):
    def __init__(self, commands):
        self.commands = commands

    @abstractmethod
    def execute(self, *args, **kwargs):
        try:
            for cmd in self.commands:
                cmd.execute()
        except Exception as e:
            raise CommandException(msg=e)


class MoveWithBurnFuelCommand(ICommand):
    def __init__(self, obj):
        self.obj = obj

    @abstractmethod
    def execute(self, *args, **kwargs):
        cmds = [CheckFuelCommand(self.obj), MoveCommand(), BurnFuelCommand(self.obj)]
        MacroCommand(cmds).execute()


class ChangeVelocityCommand(ICommand):
    def __init__(self, obj):
        self.obj = obj

    @abstractmethod
    def execute(self, *args, **kwargs):
        velocity = self.obj.get_velocity()
        if not velocity:
            raise CommandException("Невозможно изменить скорость.")


class LambdaCommand(ICommand):
    def __init__(self, func):
        self._func = func
        self._args = []
        self._kwargs = {}

    def setup(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        return self

    def execute(self):
        self._func(*self._args, **self._kwargs)
