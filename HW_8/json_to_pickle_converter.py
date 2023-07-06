''' Задание №5
Напишите функцию, которая ищет json файлы в указанной директории и 
сохраняет их содержимое в виде одноимённых pickle файлов.
'''
import os
import json
import pickle


def convert_json_to_pickle(directory):
    """
    Ищет JSON-файлы в указанной директории и сохраняет их содержимое в виде одноименных pickle-файлов.

    Args:
        directory (str): Путь к директории.
    """
    for file_name in os.listdir(directory):
        if file_name.endswith(".json"):
            json_file = os.path.join(directory, file_name)
            pickle_file = os.path.join(directory, os.path.splitext(file_name)[0] + ".pickle")

            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            with open(pickle_file, "wb") as f:
                pickle.dump(data, f)

            print(f"Файл {json_file} успешно преобразован и сохранен в {pickle_file}")



directory = "HW_8"
convert_json_to_pickle(directory)
