import csv
import json
import logging
import random
import math
import os
from functools import wraps

# Конфигурация логирования
logging.basicConfig(filename='function_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s', encoding='utf-8')


def solve_quadratic_equation(a, b, c):
    """
    Функция для нахождения корней квадратного уравнения.

    Args:
        a (float): Коэффициент a.
        b (float): Коэффициент b.
        c (float): Коэффициент c.

    Returns:
        tuple: Корни квадратного уравнения.
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2 * a)
        return x, x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2


def log_to_file(func):
    """
    Декоратор для логирования параметров и результатов работы функции в файл.

    Args:
        func (function): Декорируемая функция.

    Returns:
        function: Обернутая функция.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Логирование параметров функции
        logging.info(f"Вызов функции {func.__name__} с аргументами: args={args}, kwargs={kwargs}")

        # Выполнение декорируемой функции
        result = func(*args, **kwargs)

        # Логирование результата функции
        logging.info(f"Результат функции {func.__name__}: {result}")

        return result

    return wrapper


def solve_quadratic_equation_with_csv(func):
    """
    Декоратор для запуска функции нахождения корней квадратного уравнения с каждой тройкой чисел из CSV-файла.

    Args:
        func (function): Декорируемая функция.

    Returns:
        function: Обернутая функция.
    """

    @wraps(func)
    def wrapper(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                func(*(map(float, row)))

    return wrapper


def save_as_json(filename):
    """
    Декоратор для сохранения параметров и результатов работы функции в JSON-файл.

    Args:
        filename (str): Имя файла для сохранения.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Выполнение декорируемой функции
            result = func(*args, **kwargs)

            # Загрузка данных из файла, если файл существует
            data = []
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)

            # Сохранение параметров и результатов в список
            data.append({'args': args, 'kwargs': kwargs, 'result': result})

            # Сохранение данных в JSON файл
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)

        return wrapper

    return decorator


def generate_csv_file(filename):
    """
    Функция для генерации CSV-файла с тремя случайными числами в каждой строке.

    Args:
        filename (str): Имя файла для сохранения.
    """
    rows = random.randint(
        100, 1000)  # Случайное количество строк от 100 до 1000
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            row = [random.random() for _ in range(3)]
            writer.writerow(row)


if __name__ == '__main__':
    # Нахождение корней квадратного уравнения с логированием
    @log_to_file
    def solve_quadratic_equation_with_logging(a, b, c):
        return solve_quadratic_equation(a, b, c)


    roots = solve_quadratic_equation_with_logging(1, -3, 2)
    print("Корни:", roots)

    # Генерация CSV-файла
    generate_csv_file('data.csv')


    # Декорирование функции нахождения корней квадратного уравнения с CSV-файлом
    @solve_quadratic_equation_with_csv
    def solve_from_csv(a, b, c):
        roots = solve_quadratic_equation(a, b, c)
        print(f"Уравнение: {a}x^2 + {b}x + {c}")
        print("Корни:", roots)


    # Декорирование функции сохранения параметров и результатов в JSON-файл
    @save_as_json('results.json')
    def calculate_square(number):
        result = number ** 2
        print(f"Квадрат числа {number}:", result)


    # Вызов декорированной функции
    solve_from_csv('data.csv')

    # Вызов функции с сохранением результатов в JSON-файл
    calculate_square(11)
