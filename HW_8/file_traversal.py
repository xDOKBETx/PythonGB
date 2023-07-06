'''
Напишите функцию, которая получает на вход директорию
и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle. 
Для дочерних объектов указывайте родительскую директорию. 
Для каждого объекта укажите файл это или директория. 
Для файлов сохраните его размер в байтах, 
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
'''

import os
import json
import csv
import pickle


def traverse_directory(directory):
    """
    Рекурсивно обходит указанную директорию и все вложенные директории.
    Сохраняет результаты обхода в файлы JSON, CSV и pickle.

    Args:
        directory (str): Путь к директории.

    Returns:
        dict: Структура данных с результатами обхода.
    """
    result = {'path': directory, 'type': 'directory', 'size': 0, 'contents': []}

    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isdir(path):
            subdir = traverse_directory(path)
            result['size'] += subdir['size']
            result['contents'].append(subdir)
        elif os.path.isfile(path):
            file_size = os.path.getsize(path)
            result['size'] += file_size
            result['contents'].append({'path': path, 'type': 'file', 'size': file_size})

    return result


def save_as_json(data, filename):
    """
    Сохраняет данные в формате JSON.

    Args:
        data (any): Данные для сохранения.
        filename (str): Имя файла для сохранения.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def save_as_csv(data, filename):
    """
    Сохраняет данные в формате CSV.

    Args:
        data (dict): Структура данных для сохранения.
        filename (str): Имя файла для сохранения.
    """
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path', 'Type', 'Size'])

        def write_row(item):
            writer.writerow([item['path'], item['type'], item['size']])
            if 'contents' in item:
                for subitem in item['contents']:
                    write_row(subitem)

        write_row(data)


def save_as_pickle(data, filename):
    """
    Сохраняет данные в формате pickle.

    Args:
        data (any): Данные для сохранения.
        filename (str): Имя файла для сохранения.
    """
    with open(filename, 'wb') as f:
        pickle.dump(data, f)



directory_path = 'HW_8'
output_directory = 'HW_8'

result = traverse_directory(directory_path)

json_filename = os.path.join(output_directory, 'result.json')
save_as_json(result, json_filename)

csv_filename = os.path.join(output_directory, 'result.csv')
save_as_csv(result, csv_filename)

pickle_filename = os.path.join(output_directory, 'result.pickle')
save_as_pickle(result, pickle_filename)
