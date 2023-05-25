# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII

conversion_table = {
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I'
}

# для составления значений из случаев IV, VI и тд
def recursive_helper(value, repeat):
    if value in (4, 9):
        return recursive_helper(1, repeat) + recursive_helper(value + 1, repeat)
    elif value in (6, 7, 8):
        return recursive_helper(value - 1, repeat) + recursive_helper(1, repeat)
    elif value in (2, 3):
        return recursive_helper(1, repeat) + recursive_helper(value - 1, repeat)
    elif value == 0:
        return ''
    return conversion_table[value * repeat]

def to_roman(val):
    roman_str = ''
    value_as_string = str(val)
    repeat_times = 1 * pow(10, len(value_as_string) - 1)
    for digit in value_as_string:
        roman_str += recursive_helper(int(digit), repeat_times)
        repeat_times //= 10
    return roman_str

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']


for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')