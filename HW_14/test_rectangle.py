''' Задание №5
На семинарах по ООП был создан класс прямоугольник, хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
'''

import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_1(self):
        """
        Проверяет, что экземпляр класса Rectangle создается успешно.

        Аргументы:
        Нет аргументов.

        Возвращает:
        Нет возвращаемого значения.
        """
        self.assertIsInstance(Rectangle(5), Rectangle)

    def test_2(self):
        """
        Пока не содержит функциональности. Здесь можно добавить тесты для других методов или свойств класса Rectangle.

        Аргументы:
        Нет аргументов.

        Возвращает:
        Нет возвращаемого значения.
        """
        pass

    def test_3(self):
        """
        Пока не содержит функциональности. Здесь можно добавить тесты для других методов или свойств класса Rectangle.

        Аргументы:
        Нет аргументов.

        Возвращает:
        Нет возвращаемого значения.
        """
        pass

    def test_4(self):
        """
        Пока не содержит функциональности. Здесь можно добавить тесты для других методов или свойств класса Rectangle.

        Аргументы:
        Нет аргументов.

        Возвращает:
        Нет возвращаемого значения.
        """
        pass

    def test_5(self):
        """
        Пока не содержит функциональности. Здесь можно добавить тесты для других методов или свойств класса Rectangle.

        Аргументы:
        Нет аргументов.

        Возвращает:
        Нет возвращаемого значения.
        """
        pass

    def test_6(self):
        """
        Пока не содержит функциональности. Здесь можно добавить тесты для других методов или свойств класса Rectangle.

        Аргументы:
        Нет аргументов.

        Возвращает:
        Нет возвращаемого значения.
        """
        pass

    def test_7(self):
        """
        Пока не содержит функциональности. Здесь можно добавить тесты для других методов или свойств класса Rectangle.

        Аргументы:
        Нет аргументов.

        Возвращает:
        Нет возвращаемого значения.
        """
        pass

if __name__ == '__main__':
    # Запускаем все тесты из данного файла с подробным выводом результатов
    unittest.main(verbosity=2)
