''' Задание №3
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1
'''

import math


class Factorial:
    """
    Класс для итерации и вычисления факториалов чисел в указанном диапазоне с заданным шагом.
    """

    def __init__(self, start, stop=None, step=1):
        """
        Конструктор класса Factorial.

        Параметры:
        - start (int): Начальное значение диапазона.
        - stop (int, optional): Конечное значение диапазона (включительно). По умолчанию None.
        - step (int, optional): Шаг итерации. По умолчанию 1.

        Исключения:
        - ValueError: Вызывается, если значения start, stop или step не являются положительными целыми числами.
        """
        if not isinstance(start, int) or start <= 0:
            raise ValueError("start должно быть положительным целым числом")
        if stop is not None and (not isinstance(stop, int) or stop <= 0):
            raise ValueError("stop должно быть положительным целым числом")
        if not isinstance(step, int) or step <= 0:
            raise ValueError("step должно быть положительным целым числом")
        self.start = start
        self.stop = stop
        self.step = step
        if self.stop is None:
            self.stop = self.start
            self.start = 1

    def __iter__(self):
        """
        Метод, возвращающий сам объект self для итерации.

        Возвращает:
        - self: Сам объект self.
        """
        self.iterated = False
        return self

    def __next__(self):
        """
        Метод, выполняющий итерацию и вычисление факториалов.

        Возвращает:
        - int: Значение факториала текущего числа.

        Исключения:
        - StopIteration: Вызывается, когда достигнут конец итерации.
        """
        if self.iterated or self.start > self.stop:
            raise StopIteration
        result = math.factorial(self.start)
        self.start += self.step
        if self.start > self.stop:
            self.iterated = True
        return result


if __name__ == "__main__":
    factorial_iterator = Factorial(1, 10, 2)
    for num in factorial_iterator:
        print(num)
