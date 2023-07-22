"""
Возьмите 1-3 задачи из тех, что были на прошлых 
семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом подробной информации. 
Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.
"""


import custom_exceptions_rectangle  # Импортируем наши пользовательские исключения


class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            if length <= 0 and width <= 0:
                raise custom_exceptions_rectangle.NegativeSideLengthError((length, width))
            elif length <= 0:
                raise custom_exceptions_rectangle.NegativeSideLengthError(length)
            else:
                raise custom_exceptions_rectangle.NegativeSideLengthError(width)

        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle: length={self.length}, width={self.width}"


def main():
    try:
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        rectangle = Rectangle(length, width)
        print(f"Площадь прямоугольника: {rectangle.area()}")

    except ValueError:
        print("Ошибка: Некорректный ввод. Введите числа.")
    except custom_exceptions_rectangle.BaseRectangleException as e:
        e.log_exception()  # Записываем исключение в файл
        print(e)


if __name__ == "__main__":
    main()
