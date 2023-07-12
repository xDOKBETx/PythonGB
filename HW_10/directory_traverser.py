'''
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра
'''

import os
import json
import csv
import pickle


class DirectoryTraverser:
    def __init__(self, directory):
        """
        Инициализация класса DirectoryTraverser.

        Args:
            directory (str): Путь к директории.
        """
        self.directory = directory
        self.result = {'path': directory,
                       'type': 'directory', 'size': 0, 'contents': []}

    def traverse_directory(self):
        """
        Рекурсивно обходит указанную директорию и все вложенные директории.
        Сохраняет результаты обхода в свойстве result.

        Returns:
            dict: Структура данных с результатами обхода.
        """
        self._traverse_directory_recursive(self.directory)
        return self.result

    def _traverse_directory_recursive(self, directory):
        """
        Вспомогательный метод для рекурсивного обхода директории.

        Args:
            directory (str): Путь к директории.
        """
        for name in os.listdir(directory):
            path = os.path.join(directory, name)
            if os.path.isdir(path):
                subdir = DirectoryTraverser(path)
                subdir_result = subdir.traverse_directory()
                self.result['size'] += subdir_result['size']
                self.result['contents'].append(subdir_result)
            elif os.path.isfile(path):
                file_size = os.path.getsize(path)
                self.result['size'] += file_size
                self.result['contents'].append(
                    {'path': path, 'type': 'file', 'size': file_size})

    def save_as_json(self, filename):
        """
        Сохраняет данные в формате JSON.

        Args:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.result, f, ensure_ascii=False, indent=4)

    def save_as_csv(self, filename):
        """
        Сохраняет данные в формате CSV.

        Args:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Path', 'Type', 'Size'])
            self._write_row(self.result, writer)

    def _write_row(self, item, writer):
        """
        Вспомогательный метод для записи строки в CSV.

        Args:
            item (dict): Структура данных для записи.
            writer (csv.writer): Объект writer для записи в CSV.
        """
        writer.writerow([item['path'], item['type'], item['size']])
        if 'contents' in item:
            for subitem in item['contents']:
                self._write_row(subitem, writer)

    def save_as_pickle(self, filename):
        """
        Сохраняет данные в формате pickle.

        Args:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self.result, f)


directory_path = 'HW_10'
output_directory = 'HW_10'

traverser = DirectoryTraverser(directory_path)
result = traverser.traverse_directory()

json_filename = os.path.join(output_directory, 'result.json')
traverser.save_as_json(json_filename)

csv_filename = os.path.join(output_directory, 'result.csv')
traverser.save_as_csv(csv_filename)

pickle_filename = os.path.join(output_directory, 'result.pickle')
traverser.save_as_pickle(pickle_filename)
