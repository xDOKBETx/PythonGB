'''
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. 
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
имя файла без расширения или название каталога,
расширение, если это файл,
флаг каталога,
название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
'''

import os
import logging
import collections
import argparse

# Настройка логгирования для сохранения информации в файл 'directory_info.log'
logging.basicConfig(filename='directory_info.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Определение структуры данных для хранения информации о файле или каталоге
FileInfo = collections.namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent'])


def gather_directory_info(my_directory_path):
    """
    Собирает информацию о содержимом указанного каталога и возвращает список объектов FileInfo.

    Параметры:
        my_directory_path (str): Путь до каталога на ПК.

    Возвращает:
        list: Список объектов FileInfo, каждый из которых содержит информацию о файле или каталоге.

    Генерирует:
        FileNotFoundError: Если указанный путь не существует.

    """
    try:
        dir_info = []
        abs_path = os.path.abspath(my_directory_path)
        parent_dir = os.path.basename(abs_path)
        for item_in_dir in os.listdir(my_directory_path):
            item_path = os.path.join(abs_path, item_in_dir)
            name, extension = os.path.splitext(item_in_dir)
            is_directory = os.path.isdir(item_path)
            dir_info.append(FileInfo(name, extension[1:] if not is_directory else '', is_directory, parent_dir))

        # Логгирование информации о содержимом каталога
        logging.info(f"Directory Info: {dir_info}")

        return dir_info

    except FileNotFoundError:
        logging.exception("Ошибка при сборе информации о содержимом каталога:")
        raise


def save_to_text_file(file_info_list, filename):
    """
    Сохраняет информацию о файлах и каталогах в текстовый файл.

    Параметры:
        file_info_list (list): Список объектов FileInfo.
        filename (str): Имя файла для сохранения информации.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        for item in file_info_list:
            file.write(f"{item.name}, {item.extension}, {item.is_directory}, {item.parent}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gather information about files and directories in a given path.')
    parser.add_argument('directory_path', type=str, help='Path to the directory on the computer')
    args = parser.parse_args()

    try:
        directory_info = gather_directory_info(args.directory_path)
        for item in directory_info:
            print(item)

        # Сохранение данных в текстовый файл
        save_to_text_file(directory_info, 'directory_info.txt')

    except FileNotFoundError:
        print("Указанный путь не существует.")
