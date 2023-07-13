''' Задание №5
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений

     Задание №6
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
'''


class Rectangle:
    """
    Класс Rectangle представляет прямоугольник с возможностью вычисления периметра, площади,
    а также выполнения операций сложения, вычитания и сравнения по площади.

    Attributes:
        length (float): Длина прямоугольника.
        width (float): Ширина прямоугольника.
        perimeter (float): Периметр прямоугольника.
        area (float): Площадь прямоугольника.
    """

    def __init__(self, length, width=None):
        """
        Инициализирует объект Rectangle.

        Args:
            length (float): Длина прямоугольника.
            width (float, optional): Ширина прямоугольника. Если не указана, прямоугольник считается квадратом.
        """
        self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

        # вычисляем периметр и сохраняем в переменную
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()  # вычисляем площадь и сохраняем в переменную

    def calculate_perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Returns:
            float: Значение периметра прямоугольника.
        """
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def calculate_area(self):
        """
        Вычисляет площадь прямоугольника.

        Returns:
            float: Значение площади прямоугольника.
        """
        area = self.length * self.width
        return area

    def __add__(self, other):
        """
        Переопределяет оператор сложения для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            Rectangle: Новый прямоугольник с периметром, равным сумме периметров двух прямоугольников.
        """
        perimeter = self.perimeter + other.perimeter
        return Rectangle(perimeter / 4)

    def __sub__(self, other):
        """
        Переопределяет оператор вычитания для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            Rectangle: Новый прямоугольник с периметром, равным разности периметров двух прямоугольников.
                      Если результат отрицательный, возвращается прямоугольник с периметром 0.
        """
        perimeter = self.perimeter - other.perimeter
        if perimeter < 0:
            perimeter = 0
        return Rectangle(perimeter / 4)

    def __eq__(self, other):
        """
        Переопределяет оператор равенства для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            bool: True, если площади прямоугольников равны, иначе False.
        """
        return self.area == other.area

    def __ne__(self, other):
        """
        Переопределяет оператор неравенства для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            bool: True, если площади прямоугольников не равны, иначе False.
        """
        return self.area != other.area

    def __gt__(self, other):
        """
        Переопределяет оператор "больше" для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            bool: True, если площадь текущего прямоугольника больше площади другого прямоугольника, иначе False.
        """
        return self.area > other.area

    def __lt__(self, other):
        """
        Переопределяет оператор "меньше" для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            bool: True, если площадь текущего прямоугольника меньше площади другого прямоугольника, иначе False.
        """
        return self.area < other.area

    def __ge__(self, other):
        """
        Переопределяет оператор "больше или равно" для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            bool: True, если площадь текущего прямоугольника больше или равна площади другого прямоугольника, иначе False.
        """
        return self.area >= other.area

    def __le__(self, other):
        """
        Переопределяет оператор "меньше или равно" для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            bool: True, если площадь текущего прямоугольника меньше или равна площади другого прямоугольника, иначе False.
        """
        return self.area <= other.area

    def __repr__(self):
        """
        Метод представления экземпляра класса для программиста.
        Возвращает строку, содержащую информацию о длине и ширине прямоугольника.

        Returns:
            str: Строка представления экземпляра класса для программиста.
        """
        return f"Rectangle(length={self.length}, width={self.width})"

    def __str__(self):
        """
        Метод представления экземпляра класса для пользователя.
        Возвращает строку, содержащую информацию о площади прямоугольника.

        Returns:
            str: Строка представления экземпляра класса для пользователя.
        """
        return f"Площадь прямоугольника: {self.area}"


rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(4, 2)

# Вычисление и вывод периметра прямоугольника
print("Периметр прямоугольника 1:", rectangle1.perimeter)
print("Периметр прямоугольника 2:", rectangle2.perimeter)

# Вычисление и вывод площади прямоугольника
print("Площадь прямоугольника 1:", rectangle1.area)
print("Площадь прямоугольника 2:", rectangle2.area)

# Сложение прямоугольников
sum_rectangle = rectangle1 + rectangle2
sum_perimeter = sum_rectangle.perimeter
print("Сумма периметров прямоугольников:", sum_perimeter)

# Вычитание прямоугольников
diff_rectangle = rectangle1 - rectangle2
diff_perimeter = diff_rectangle.perimeter
print("Разность периметров прямоугольников:", diff_perimeter)

# Сравнение прямоугольников по площади
print("Площадь прямоугольника 1 больше прямоугольника 2?", rectangle1 > rectangle2)
print("Площадь прямоугольника 1 меньше прямоугольника 2?", rectangle1 < rectangle2)
print("Площадь прямоугольника 1 больше или равна площади прямоугольника 2?",
      rectangle1 >= rectangle2)
print("Площадь прямоугольника 1 меньше или равна площади прямоугольника 2?",
      rectangle1 <= rectangle2)
print("Площади прямоугольников равны?", rectangle1 == rectangle2)
print("Площади прямоугольников не равны?", rectangle1 != rectangle2)

# Вывод информации о прямоугольниках
print(repr(rectangle1))
print(str(rectangle1))
print(repr(rectangle2))
print(str(rectangle2))
