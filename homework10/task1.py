# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generator_names():
    while True:
        first_word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 16)))
        second_word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 16)))
        yield f'{first_word} {second_word}'

gen = generator_names()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Здесь пишем код