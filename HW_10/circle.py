''' Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь.
'''

import math


class Circle:
    def __init__(self, radius):
        """
        Инициализация объекта Circle.

        Args:
            radius (float): Радиус окружности.
        """
        self.radius = radius

    def calculate_circumference(self):
        """
        Вычисление длины окружности.

        Returns:
            float: Длина окружности.
        """
        circumference = 2 * math.pi * self.radius
        return circumference

    def calculate_area(self):
        """
        Вычисление площади окружности.

        Returns:
            float: Площадь окружности.
        """
        area = math.pi * (self.radius ** 2)
        return area


# Создание экземпляра класса Circle с радиусом 5
circle = Circle(10)

# Вычисление и вывод длины окружности
circumference = circle.calculate_circumference()
print("Длина окружности:", circumference)

# Вычисление и вывод площади окружности
area = circle.calculate_area()
print("Площадь окружности:", area)
