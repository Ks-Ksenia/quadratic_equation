from queue_ import q


class ICommand:
    def execute(self, *args, **kwargs):
        pass


class MoveCommand(ICommand):
    def execute(self, *args, **kwargs):
        l = 1/0


class RotateCommand(ICommand):
    def execute(self, *args, **kwargs):
        dict_ = {}
        dict_['key']
