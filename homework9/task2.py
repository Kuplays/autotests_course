# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
import random


def func_log(log_file='log.txt'):
    def _inner_decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            with open(log_file, 'a', encoding='utf-8') as initial_file:
                call_date = datetime.datetime.now()
                initial_file.write(f'{func.__name__} вызвана {call_date.strftime("%d.%m %H:%M:%S")}\n')
            return res
        return wrapper
    return _inner_decorator


@func_log()
def func1(text='default'):
    print('FUNC1 TEXT: ' + text)


@func_log(log_file='another_log.txt')
def func2():
    print(random.randint(0, 100) * random.randint(0, 10))


func1()
func2()
# Здесь пишем код