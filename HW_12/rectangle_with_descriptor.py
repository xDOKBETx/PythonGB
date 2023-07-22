'''
Задание №4
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
Используйте декораторы свойств.

Задание №5
Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

Задание №6
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
'''

class SizeValidator:
    """
    Дескриптор SizeValidator предназначен для валидации размеров (длины и ширины) прямоугольника.
    Если значение атрибута (длины или ширины) задается меньше нуля, возбуждается исключение ValueError.

    Args:
        name (str): Название атрибута, который необходимо проверять.

    """

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name.capitalize()} не может быть отрицательным.")
        setattr(instance, self.name, value)


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

    __slots__ = ("_length", "_width", "perimeter", "area")

    def __init__(self, length, width=None):
        """
        Инициализирует объект Rectangle.

        Args:
            length (float): Длина прямоугольника.
            width (float, optional): Ширина прямоугольника. Если не указана, прямоугольник считается квадратом.
        """
        self._length = None
        self._width = None
        self.length = length
        if width is not None:
            self.width = width
        else:
            self.width = length

    length = SizeValidator("_length")
    width = SizeValidator("_width")

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
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        """
        Переопределяет оператор вычитания для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            Rectangle: Новый прямоугольник с периметром, равным разности периметров двух прямоугольников.
                      Если результат отрицательный, возвращается прямоугольник с периметром 0.
        """
        new_length = self.length - other.length
        new_width = self.width - other.width
        if new_length < 0:
            new_length = 0
        if new_width < 0:
            new_width = 0
        return Rectangle(new_length, new_width)

    def __eq__(self, other):
        """
        Переопределяет оператор равенства для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            bool: True, если площади прямоугольников равны, иначе False.
        """
        return self.calculate_area() == other.calculate_area()

    def __ne__(self, other):
        """
        Переопределяет оператор неравенства для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            bool: True, если площади прямоугольников не равны, иначе False.
        """
        return self.calculate_area() != other.calculate_area()

    def __gt__(self, other):
        """
        Переопределяет оператор "больше" для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            bool: True, если площадь текущего прямоугольника больше площади другого прямоугольника, иначе False.
        """
        return self.calculate_area() > other.calculate_area()

    def __lt__(self, other):
        """
        Переопределяет оператор "меньше" для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            bool: True, если площадь текущего прямоугольника меньше площади другого прямоугольника, иначе False.
        """
        return self.calculate_area() < other.calculate_area()

    def __ge__(self, other):
        """
        Переопределяет оператор "больше или равно" для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            bool: True, если площадь текущего прямоугольника больше или равна площади другого прямоугольника, иначе False.
        """
        return self.calculate_area() >= other.calculate_area()

    def __le__(self, other):
        """
        Переопределяет оператор "меньше или равно" для прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник.

        Returns:
            bool: True, если площадь текущего прямоугольника меньше или равна площади другого прямоугольника, иначе False.
        """
        return self.calculate_area() <= other.calculate_area()

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
        return f"Площадь прямоугольника: {self.calculate_area()}"


# Testing the Rectangle class
rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(4, 2)

# Trying to create a rectangle with negative dimensions (raises ValueError)
try:
    invalid_rectangle = Rectangle(-1, 2)
except ValueError as e:
    print("Ошибка:", e)

# Changing the length and width of a rectangle
rectangle1.length = 8
rectangle1.width = 6

# Displaying updated information about the rectangles
print(repr(rectangle1))
print(str(rectangle1))
print(repr(rectangle2))
print(str(rectangle2))

# Performing operations on rectangles
sum_rectangle = rectangle1 + rectangle2
sum_perimeter = sum_rectangle.calculate_perimeter()
print("Сумма периметров прямоугольников:", sum_perimeter)

diff_rectangle = rectangle1 - rectangle2
diff_perimeter = diff_rectangle.calculate_perimeter()
print("Разность периметров прямоугольников:", diff_perimeter)

print("Площадь прямоугольника 1 больше прямоугольника 2?", rectangle1 > rectangle2)
print("Площадь прямоугольника 1 меньше прямоугольника 2?", rectangle1 < rectangle2)
print(
    "Площадь прямоугольника 1 больше или равна площади прямоугольника 2?",
    rectangle1 >= rectangle2,
)
print(
    "Площадь прямоугольника 1 меньше или равна площади прямоугольника 2?",
    rectangle1 <= rectangle2,
)
print("Площади прямоугольников равны?", rectangle1 == rectangle2)
print("Площади прямоугольников не равны?", rectangle1 != rectangle2)
