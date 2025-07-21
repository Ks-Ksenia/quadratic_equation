from tests.mock_objs import MockUObject


def make_movable_uobject(position, velocity):
    uobj = MockUObject()
    uobj.set_property("move_location", position)
    uobj.set_property("move_velocity", velocity)
    return uobj
