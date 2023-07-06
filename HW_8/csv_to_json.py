''' Задание №4
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
Дополните id до 10 цифр незначащими нулями. 
В именах первую букву сделайте прописной. 
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, 
где каждая строка csv файла представлена как отдельный json словарь. 
Имя исходного и конечного файлов передавайте как аргументы функции.
'''
import csv
import json
import hashlib

def process_csv(csv_file, json_file):
    """
    Читает CSV-файл, обрабатывает данные и сохраняет результат в JSON-файл.

    Args:
        csv_file (str): Имя входного CSV-файла.
        json_file (str): Имя выходного JSON-файла.
    """
    users = []

    # Чтение CSV-файла
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        # Обработка каждой строки CSV-файла
        for row in reader:
            name = row[0].capitalize()  # Приводим первую букву имени к прописной
            user_id = row[1].zfill(10)  # Добавляем ведущие нули к идентификатору
            access_level = row[2]

            # Создаем хеш на основе имени и идентификатора
            hash_value = hashlib.md5((name + user_id).encode()).hexdigest()

            # Создаем словарь с данными пользователя
            user = {
                'Имя': name,
                'Личный идентификатор': user_id,
                'Уровень доступа': access_level,
                'Хеш': hash_value
            }

            # Добавляем пользователя в список
            users.append(user)

    # Сохранение данных в JSON-файл
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

    print(f"Данные из файла {csv_file} успешно обработаны и сохранены в {json_file}")


csv_filename = 'users.csv'
json_filename = 'users_processed.json'
process_csv(csv_filename, json_filename)
