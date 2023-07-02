'''
Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры: 
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
'''
'''
Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
'''
'''
Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''

import os
import random
import string


def generate_random_files(directory, extensions, min_name_length=6, max_name_length=30, min_file_size=256,
                          max_file_size=4096, num_files=1):
    '''
    Генерирует случайные файлы с указанными расширениями в заданной директории.
    directory (str): Путь к директории.
    extensions (list): Список расширений файлов.
    min_name_length (int): Минимальная длина имени файла.
    max_name_length (int): Максимальная длина имени файла.
    min_file_size (int): Минимальный размер файла в байтах.
    max_file_size (int): Максимальный размер файла в байтах.
    num_files (int): Количество файлов для каждого расширения.
    '''
    check_directory(directory)

    for extension in extensions:
        for _ in range(num_files):
            name_length = random.randint(min_name_length, max_name_length)
            file_name = generate_random_file_name(directory, extension, name_length)

            while os.path.exists(file_name):
                file_name = generate_random_file_name(directory, extension, name_length)

            file_size = random.randint(min_file_size, max_file_size)
            random_bytes = generate_random_bytes(file_size)

            with open(file_name, 'wb') as file:
                file.write(random_bytes)


def check_directory(directory):
    '''
    Проверяет наличие указанной директории и создает ее, если она не существует.
    directory (str): Путь к директории.
    '''
    if not os.path.exists(directory):
        os.makedirs(directory)


def generate_random_file_name(directory, extension, name_length):
    '''
    Генерирует случайное имя файла с указанным расширением.
    directory (str): Путь к директории.
    extension (str): Расширение файла.
    name_length (int): Длина имени файла.
    Returns:
        str: Сгенерированное имя файла.
    '''
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length))
    return os.path.join(directory, random_name + '.' + extension)


def generate_random_bytes(file_size):
    '''
    Генерирует случайные байты указанного размера.
    file_size (int): Размер файла в байтах.
    Returns:
        bytes: Сгенерированные случайные байты.
    '''
    return os.urandom(file_size)


if __name__ == '__main__':
    directory_path = 'D:\\ONE DRIVE\\OneDrive\\Документы\\PythonGB\\HW_7'
    extensions_list = ['txt', 'bin', 'png', 'mp4']
    generate_random_files(directory_path, extensions_list, min_name_length=8, max_name_length=15,
                          min_file_size=512, max_file_size=2048, num_files=10)

