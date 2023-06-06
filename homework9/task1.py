# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
with open('test_file/task1_data.txt', 'r', encoding='utf-8') as initial_file:
    text_data = initial_file.readlines()
    for i in range(len(text_data)):
        text_data[i] = ''.join([char for char in text_data[i] if not char.isdigit()])
    with open('test_file/task1_answer.txt', 'w', encoding='utf-8') as result_file:
        result_file.write(''.join(text_data))

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
