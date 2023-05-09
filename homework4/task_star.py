# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974
import time

def form_number(lst):
	str_res = [str(integer) for integer in lst]
	a_string = "".join(str_res)

	return int(a_string)


def max_division_by_3(num):
	found_numbers = []
	new_num = [int(x) for x in str(num)]
	for i in range(len(new_num)):
		remember_digit = new_num[i]
		digit = remember_digit
		while digit <= 9:
			new_num[i] = digit
			current_contestant_number = form_number(new_num)
			if current_contestant_number % 3 == 0:
				found_numbers.append(current_contestant_number)
			digit += 1
		new_num[i] = remember_digit
	new_num = max(found_numbers)
	return new_num

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')