''' Задание №6
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара. 
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла. 
'''

import csv
import pickle

def pickle_to_csv(pickle_file, csv_file):
    """
    Преобразует pickle файл в CSV-файл.

    Args:
        pickle_file (str): Имя входного pickle-файла.
        csv_file (str): Имя выходного CSV-файла.
    """
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)

    if not data:
        print("Пустой список словарей в pickle-файле.")
        return

    # Извлекаем ключи словаря для заголовков столбца
    keys = data[0].keys()

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Данные из файла {pickle_file} успешно преобразованы и сохранены в {csv_file}")


pickle_filename = 'users_processed.pickle'
csv_filename = 'users_processed.csv'
pickle_to_csv(pickle_filename, csv_filename)
