from math import inf
import pytest

from main import get_roots_quadratic_equation


class TestQuadraticEquation:
    def test_equation_without_root(self):
        roots = get_roots_quadratic_equation(1.0, 0.0, 1.0)
        assert roots == []


    def test_equation_with_two_root(self):
        roots = get_roots_quadratic_equation(1.0, 0.0, -1.0)
        assert roots == [1.0, -1.0]


    def test_equation_with_one_root(self):
        roots = get_roots_quadratic_equation(1.0, 2.0, 1.0)
        assert roots == [-1.0]


    def test_param_a_close_zero(self):
        roots = get_roots_quadratic_equation(0.000000001, 2.0, 1.0)
        assert roots == [-0.5000000413701855, -1999999999.4999998]


    def test_param_d_close_zero_and_less_epsilon(self):
        roots = get_roots_quadratic_equation(-0.0000000056, -0.0004, 1.0)
        assert roots == [-35714.28571428572]


    def test_param_a_less_than_zero(self):
        with pytest.raises(ValueError) as e:
            get_roots_quadratic_equation(0, 2.0, 1.0)
        assert 'Значение a должно быть больше нуля.' == e.value.args[0]

    @pytest.mark.parametrize(
        'a, b, c',
        [
            (inf, 1.0, 1.0),
            (1.0, inf, 1.0),
            (1.0, 1.0, inf),
            (inf, inf, inf),
        ]
    )
    def test_equation_with_inf_root(self, a, b, c):
        with pytest.raises(ValueError) as e:
            get_roots_quadratic_equation(a, b, c)
        assert 'Значение переменных не должно быть inf.' == e.value.args[0]
