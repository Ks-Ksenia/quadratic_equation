from math import sqrt, isinf, isclose
from typing import Optional


EPSILON = 0.000001

def get_roots_quadratic_equation(a: float, b: float, c: float) -> Optional[list]:
    if any((isinf(a), isinf(b), isinf(c))):
        raise ValueError('Значение переменных не должно быть inf.')

    if isclose(a, 0):
        raise ValueError('Значение a должно быть больше нуля.')

    d = b ** 2 - 4 * a * c

    if isclose(d, 0) or (0 < d < EPSILON):
        x = -b / (2 * a)
        return [x]
    elif d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return [x1, x2]
    else:
        return []
