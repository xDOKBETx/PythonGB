''' Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
'''

class Rectangle:
    def __init__(self, length, width=None):
        """
        Инициализация объекта Rectangle.

        Args:
            length (float): Длина прямоугольника.
            width (float): Ширина прямоугольника (по умолчанию None).
        """
        self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

    def calculate_perimeter(self):
        """
        Вычисление периметра прямоугольника.

        Returns:
            float: Периметр прямоугольника.
        """
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def calculate_area(self):
        """
        Вычисление площади прямоугольника.

        Returns:
            float: Площадь прямоугольника.
        """
        area = self.length * self.width
        return area


# Создание экземпляра класса Rectangle с длиной и шириной
rectangle = Rectangle(5, 3)

# Вычисление и вывод периметра прямоугольника
perimeter = rectangle.calculate_perimeter()
print("Периметр прямоугольника:", perimeter)

# Вычисление и вывод площади прямоугольника
area = rectangle.calculate_area()
print("Площадь прямоугольника:", area)
