''' Задание №1
Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
'''
from random import randint, uniform

MIN = -1000
MAX = 1000
NUM_ROW = 5


def fill_file_with_random_pairs(count_row, filename):
    """
    Заполнение файла случайными парами чисел
    :param count_row: количество строк для заполнения
    :param filename: имя файла
    """
    with open(filename, 'a', encoding='utf-8') as file:
        for _ in range(count_row):
            num1 = randint(MIN, MAX)
            num2 = round(uniform(MIN, MAX), 2)
            pair = f'{num1} | {num2}\n'
            file.write(pair)


if __name__ == '__main__':
    fill_file_with_random_pairs(NUM_ROW, 'HW_7/numbers.txt')
