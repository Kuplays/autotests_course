# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest

def add_func(a, b):
    return a + b


@pytest.mark.usefixtures('start_time')
class TestSample:

    @pytest.mark.parametrize('a, b, result', [
        (5, 5, 10),
        (1, 1, 2),
        (-5, 5, 0),
        (100, 10, 110),
        (11, 9, 20)
    ])
    @pytest.mark.usefixtures('run_time')
    def test_01_add_small_values(self, a, b, result):
        assert add_func(a, b) == result

    @pytest.mark.parametrize('a, b, result', [
        (10000, 10000, 20000),
        (999999, 1, 1000000)
    ])
    def test_01_add_big_values(self, a, b, result):
        assert add_func(a, b) == result
