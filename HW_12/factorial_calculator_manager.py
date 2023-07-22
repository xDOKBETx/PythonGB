""" Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
"""

import json
import math


class Factorial:
    """
    Класс для вычисления факториала числа и сохранения результатов в списке словарей.
    """

    def __init__(self, k):
        """
        Конструктор класса Factorial.

        Параметры:
        - k (int): Размер истории (количество последних вычислений факториалов, которые будут сохранены).

        Исключения:
        - ValueError: Вызывается, если значение k не является положительным целым числом.
        """
        if not isinstance(k, int) or k <= 0:
            raise ValueError("k должно быть положительным целым числом")
        self.k = k
        self.list_dict = []

    def calculate_factorial(self, num):
        """
        Вычисляет факториал числа num.

        Параметры:
        - num (int): Число, для которого необходимо вычислить факториал.

        Возвращает:
        - int: Результат вычисления факториала числа num.

        Исключения:
        - ValueError: Вызывается, если значение num не является положительным целым числом.
        """
        if not isinstance(num, int) or num <= 0:
            raise ValueError("num должно быть положительным целым числом")
        fac = math.factorial(num)
        self.list_dict.append({num: fac})
        if len(self.list_dict) >= self.k:
            self.list_dict = self.list_dict[-self.k :]
        return fac

    def show(self):
        """
        Возвращает список словарей, содержащих вычисленные факториалы.
        """
        return self.list_dict

    def save_to_json(self, filename):
        """
        Сохраняет список словарей в JSON-файл.

        Параметры:
        - filename (str): Имя файла, в который нужно сохранить данные.
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.list_dict, f)
        except Exception as e:
            print(f"Ошибка при сохранении в JSON-файл: {e}")

    def __enter__(self):
        """
        Метод контекстного менеджера, выполняемый при входе в контекстный блок `with`.
        В данном случае, он возвращает сам объект self.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Метод контекстного менеджера, выполняемый при выходе из контекстного блока `with`.
        В данном случае, он вызывает метод save_to_json для сохранения в JSON-файл.

        Параметры:
        - exc_type (type): Тип исключения, если произошло.
        - exc_val (Exception): Исключение, если произошло.
        - exc_tb (traceback): Traceback исключения, если произошло.
        """
        filename = "factorials.json"
        self.save_to_json(filename)


if __name__ == "__main__":
    with Factorial(5) as factorial:
        for i in range(1, 8):
            factorial.calculate_factorial(i)
    print(factorial.show())
