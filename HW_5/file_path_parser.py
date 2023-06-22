'''
Напишите функцию, которая принимает на вход строку —абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

import os


def parse_file_path(file_path):
    # Разделяем путь и имя файла
    path, filename = os.path.split(file_path)
    # Разделяем имя файла и расширение
    filename, extension = os.path.splitext(filename)
    # Возвращаем кортеж из трех элементов
    return path, filename, extension


file_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1\\bin\\pycharm64.exe"
path, filename, extension = parse_file_path(file_path)
print("Path:", path)
print("Filename:", filename)
print("Extension:", extension)
