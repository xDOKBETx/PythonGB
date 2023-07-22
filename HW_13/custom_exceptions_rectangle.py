import datetime


class BaseRectangleException(Exception):
    """Базовый класс пользовательского исключения для ошибок с прямоугольником."""

    def __init__(self, message, details=None):
        self.message = message
        self.details = details

    def log_exception(self):
        """Метод для записи информации об исключении в журнал."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("error_log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"[{timestamp}] {self.__class__.__name__}: {self.message}\n")
            if self.details:
                log_file.write(f"Details: {self.details}\n")
            log_file.write("\n")

    def __str__(self):
        """Метод для форматированного вывода сообщения об ошибке."""
        if self.details:
            return f"{self.__class__.__name__}: {self.message}. Дополнительные детали: {self.details}"
        else:
            return f"{self.__class__.__name__}: {self.message}"


class NegativeSideLengthError(BaseRectangleException):
    """Дочерний класс исключения для ошибок с отрицательными длинами сторон прямоугольника."""

    def __init__(self, side_length):
        message = "Ошибка: Сторона прямоугольника имеет отрицательную длину."
        details = f"Отрицательное значение стороны: {side_length}"
        super().__init__(message, details)
