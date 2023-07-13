''' Задание №1
Создайте класс Моя Строка, где: будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)
'''

import time


class MyString(str):
    """
    Класс MyString наследуется от встроенного класса str
    и добавляет дополнительные свойства автора и времени создания.
    """

    def __new__(cls, value, author):
        """
        Создает новый экземпляр класса MyString.

        Args:
            value (str): Значение строки.
            author (str): Имя автора строки.

        Returns:
            MyString: Экземпляр класса MyString.
        """
        instance = super().__new__(cls, value)
        instance.author = author
        instance.created_time = time.time()
        return instance

    def __str__(self):
        """
        Возвращает строковое представление экземпляра класса MyString.

        Returns:
            str: Строковое представление экземпляра класса MyString.
        """
        return super().__str__()

    def print_author(self):
        """
        Выводит имя автора на печать.
        """
        print(self.author)

    def print_created_time(self):
        """
        Выводит время создания на печать.
        """
        print(self.created_time)


s = MyString("Hello, world!", "Алексей")

# Задача 1: Вывод строки
print(s)  # Выводит: Hello, world!

# Задача 2: Вывод имени автора
s.print_author()  # Выводит: Алексей

# Задача 3: Вывод времени создания
s.print_created_time()  # Выводит: текущее время
