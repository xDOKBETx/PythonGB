''' Задание №3
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
'''

import csv
import json


def convert_to_csv(json_file, csv_file):
    """
    Преобразует данные из JSON-файла в формат CSV и сохраняет их в файл.

    Args:
        json_file (str): Имя JSON-файла.
        csv_file (str): Имя CSV-файла.
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        
        # Записываем заголовки столбцов в CSV-файл
        writer.writerow(['Имя', 'Личный идентификатор', 'Уровень доступа'])

        # Записываем данные пользователей в CSV-файл
        for level in data:
            for user_id, user_info in data[level].items():
                name = user_info['Имя']
                access_level = user_info['Уровень доступа']
                writer.writerow([name, user_id, access_level])

    print(f"Данные из файла {json_file} успешно преобразованы и сохранены в {csv_file}")


json_filename = 'users.json'
csv_filename = 'users.csv'
convert_to_csv(json_filename, csv_filename)
