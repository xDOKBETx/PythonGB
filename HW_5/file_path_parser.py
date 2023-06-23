'''
Напишите функцию, которая принимает на вход строку —абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''


def parse_file_path(file_path):
    path, file_with_extension = file_path.rsplit("\\", 1)
    filename, extension = file_with_extension.rsplit(".", 1)
    return path, filename, extension


file_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1\\bin\\pycharm64.exe"
path, filename, extension = parse_file_path(file_path)
print("Path:", path)
print("Filename:", filename)
print("Extension:", extension)
