# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
purchases_sums = []
with open('test_file/task_3.txt', 'r', encoding='utf-8') as initial_file:
    text_data = initial_file.readlines()
    current_sum = 0
    for item in text_data:
        if item == '\n':
            purchases_sums.append(current_sum)
            current_sum = 0
            continue
        current_sum += int(item[:-1])
purchases_sums.sort(reverse=True)
three_most_expensive_purchases = purchases_sums[0] + purchases_sums[1] + purchases_sums[2]

assert three_most_expensive_purchases == 202346
