from tests.mock_objs import MockUObject


def make_movable_uobject(loaction, velocity):
    uobj = MockUObject()
    uobj.set_property("move_location", loaction)
    uobj.set_property("move_velocity", velocity)
    return uobj
