# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


class TestDivisionSuite:
    @pytest.mark.smoke
    def test_01_division_by_2(self):
        assert all_division(100, 2, 2) == 25

    def test_02_division_by_self(self):
        assert all_division(10, 10) == 1

    @pytest.mark.smoke
    def test_03_division_by_negative(self):
        assert all_division(100, -10, -10) == 1

    def test_04_division_million_3_times(self):
        assert all_division(1000000, 25, 80, 100) == 5

    def test_05_division_by_zero(self):
        with pytest.raises(ZeroDivisionError) as error:
            all_division(10, 0)
        assert str(error.value) == 'division by zero'
