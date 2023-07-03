''' Задание №7
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
Распечатайте его как pickle строку.
'''
import csv
import pickle

def read_csv_to_pickle(csv_file):
    """
    Читает CSV-файл и возвращает его содержимое в виде строки формата pickle.

    Args:
        csv_file (str): Имя CSV-файла.

    Returns:
        str: Строка формата pickle.
    """
    data = []

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            data.append(row)

    pickle_string = pickle.dumps(data)
    return pickle_string


csv_filename = 'users_processed.csv'
pickle_string = read_csv_to_pickle(csv_filename)
print(pickle_string)
