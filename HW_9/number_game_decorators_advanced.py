#  Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.

import os
import json
import random
from functools import wraps


def create_guessing_game(number_range, attempts):
    """
    Функция-замыкание, которая создает игру "Угадай число".

    Args:
        number_range (tuple): Диапазон чисел для загадывания (min, max).
        attempts (int): Количество попыток для угадывания.

    Returns:
        function: Функция для игры "Угадай число".
    """
    def guessing_game():
        """
        Функция для игры "Угадай число".

        Просит пользователя угадать загаданное число в указанном диапазоне
        за указанное количество попыток.

        """
        number = random.randint(*number_range)
        print(f"Загадано число от {number_range[0]} до {number_range[1]}")
        for _ in range(attempts):
            guess = int(input("Введите число: "))
            if guess == number:
                print("Вы угадали!")
                return
            elif guess < number:
                print("Загаданное число больше")
            else:
                print("Загаданное число меньше")
        print("Попытки исчерпаны, вы проиграли!")

    return guessing_game


def validate_range(func):
    """
    Декоратор, который проверяет и заменяет переданные значения диапазона чисел и количества попыток,
    если они не соответствуют условиям задачи.

    Args:
        func (function): Декорируемая функция.

    Returns:
        function: Обернутая функция.
    """
    @wraps(func)
    def wrapper(*args):
        number_range, attempts = args
        min_num, max_num = number_range
        if not (1 <= min_num <= max_num <= 100):
            print("Некорректный диапазон чисел. Используются значения по умолчанию.")
            number_range = (1, 100)
        return func(number_range, attempts)

    return wrapper


def param(count):
    """
    Декоратор с параметром, определяющим количество запусков декорируемой функции.

    Args:
        count (int): Количество запусков.

    Returns:
        function: Декоратор.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            nonlocal count
            while count > 0:
                func(*args)
                count -= 1

        return wrapper

    return decorator


def save_as_json(filename):
    """
    Декоратор, сохраняющий параметры и результат декорируемой функции в JSON файл.

    Args:
        filename (str): Имя файла для сохранения.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Загрузка данных из файла, если файл существует
            data = []
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)

            # Вызов декорируемой функции
            result = func(*args, **kwargs)

            # Сохранение параметров и результата в список
            data.append({'args': args, 'kwargs': kwargs, 'result': result})

            # Сохранение данных в JSON файл
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)

        return wrapper

    return decorator


@validate_range
@param(count=5)
@save_as_json('result.json')
def my(number_range, attempts):
    """
    Функция, принимающая переменное количество аргументов.

    Args:
        number_range (tuple): Диапазон чисел для загадывания (min, max).
        attempts (int): Количество попыток для угадывания.

    Returns:
        tuple: Кортеж с переданными аргументами.
    """
    print(
        f"Вызвана функция my с параметрами: number_range={number_range}, attempts={attempts}")
    return number_range, attempts


if __name__ == '__main__':
    my((1, 100), 3)
