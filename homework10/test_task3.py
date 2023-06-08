# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('args1, expected', [
    pytest.param(
        [10, 10], 1, marks=pytest.mark.smoke
    ),
    pytest.param(
        [100, 10, 0], 'division by zero', marks=pytest.mark.skip('Не смотрим деление на ноль, оно ведь не стрельнет...')
    ),
    ([1000000, 25, 80, 100], 5)
])
def test_using_parametrize(args1, expected):
    assert all_division(*args1) == expected
