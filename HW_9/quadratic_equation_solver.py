'''
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл
'''

import csv
import json
import random
from functools import wraps
import math

# Функция нахождения корней квадратного уравнения


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
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2*a)
        return x, x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2

# Функция генерации CSV-файла с тремя случайными числами в каждой строке


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

# Декоратор для запуска функции нахождения корней квадратного уравнения с каждой тройкой чисел из CSV-файла


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
                numbers = [float(num) for num in row]
                func(*numbers)

    return wrapper

# Декоратор для сохранения параметров и результатов работы функции в JSON-файл


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

            # Сохранение параметров и результатов в JSON-файл
            data = {
                'args': args,
                'kwargs': kwargs,
                'result': result
            }
            with open(filename, 'w') as file:
                json.dump(data, file)

        return wrapper

    return decorator


if __name__ == '__main__':
    # Нахождение корней квадратного уравнения
    roots = solve_quadratic_equation(1, -3, 2)
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
        result = number**2
        print(f"Квадрат числа {number}:", result)

    # Вызов декорированной функции
    solve_from_csv('data.csv')

    # Вызов функции с сохранением результатов в JSON-файл
    calculate_square(112)
