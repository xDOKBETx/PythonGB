''' Задание №2
Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
Полученные имена сохраните в файл.
'''

import random
import string

COUNT_NAMES = 5
VOVELS = 'eyuioa'
CONSONANT = 'qwrtpsdfghjklzxcvbnm'
MIN_LENGTH = 4
MAX_LENGTH = 7


def generate_pseudonyms(count_names):
    '''
    Генерация псевдонимов (имен)

    Args:
        count_names (int): Количество генерируемых псевдонимов

    Returns:
        list: Список сгенерированных псевдонимов
    '''
    pseudonyms = []
    for _ in range(count_names):
        lenn = random.randint(MIN_LENGTH, MAX_LENGTH)
        name = [random.choice(VOVELS)]
        name += [random.choice(CONSONANT) for _ in range(lenn-1)]
        pseudonyms.append(''.join(name).capitalize())
    return pseudonyms


def save_pseudonyms_to_file(pseudonyms, filename):
    '''
    Сохранение псевдонимов в файл

    Args:
        pseudonyms (list): Список псевдонимов
        filename (str): Имя файла для сохранения псевдонимов
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(pseudonyms))


if __name__ == '__main__':
    filename = 'HW_7/names.txt'
    pseudonyms = generate_pseudonyms(COUNT_NAMES)
    save_pseudonyms_to_file(pseudonyms, filename)
