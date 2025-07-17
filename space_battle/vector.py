import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_angle_and_length(cls, angle, length):
        return cls(
            round(length * math.cos(angle.to_rads())),
            round(length * math.sin(angle.to_rads())),
        )

    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError
        print(other)
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"

