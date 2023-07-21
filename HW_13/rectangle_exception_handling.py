"""
Возьмите 1-3 задачи из тех, что были на прошлых 
семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом подробной информации. 
Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.
"""


import datetime


class BaseRectangleException(Exception):
    """Базовый класс пользовательского исключения для ошибок с прямоугольником."""

    def __init__(self, message, details=None):
        self.message = message
        self.details = details
        super().__init__(message)
        self.log_exception()  # Call log_exception() when the exception is raised

    def log_exception(self):
        """Метод для записи информации об исключении в журнал."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("error_log.txt", "a", encoding="utf-8") as log_file:  # Указываем кодировку "utf-8"
            log_file.write(f"[{timestamp}] {self.__class__.__name__}: {self.message}\n")
            if self.details:
                log_file.write(f"Details: {self.details}\n")
            log_file.write("\n")


class NegativeSideLengthError(BaseRectangleException):
    """Дочерний класс исключения для ошибок с отрицательными длинами сторон прямоугольника."""

    def __init__(self, side_length):
        message = "Ошибка: Сторона прямоугольника имеет отрицательную длину."
        details = f"Отрицательное значение стороны: {side_length}"
        super().__init__(message, details)


class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            if length <= 0 and width <= 0:
                raise NegativeSideLengthError((length, width))
            elif length <= 0:
                raise NegativeSideLengthError(length)
            else:
                raise NegativeSideLengthError(width)

        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


def main():
    try:
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        rectangle = Rectangle(length, width)
        print(f"Площадь прямоугольника: {rectangle.area()}")

    except ValueError:
        print("Ошибка: Некорректный ввод. Введите числа.")
    except BaseRectangleException as e:
        print(e.message)
        if e.details:
            print(f"Дополнительные детали: {e.details}")


if __name__ == "__main__":
    main()
