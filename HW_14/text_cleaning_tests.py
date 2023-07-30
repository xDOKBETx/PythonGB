''' Задание №3
Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
'''

import unittest
from text_cleaner import clean_text

class TestCleanText(unittest.TestCase):
    def test_1(self):
        """
        Проверяет, что функция возвращает строку без изменений,
        если строка содержит только буквы латинского алфавита.

        Аргументы:
        Нет аргументов.

        Возвращает:
        Нет возвращаемого значения.
        """
        self.assertEqual(clean_text('python'), 'python', msg='Something is not OK')

    def test_2(self):
        """
        Проверяет, что функция приводит буквы в строке к нижнему регистру,
        сохраняя при этом все символы.

        Аргументы:
        Нет аргументов.

        Возвращает:
        Нет возвращаемого значения.
        """
        self.assertEqual(clean_text('Python'), 'python', msg='Something is not OK')

    def test_3(self):
        """
        Проверяет, что функция удаляет знаки пунктуации из строки,
        оставляя только буквы латинского алфавита и пробелы.

        Аргументы:
        Нет аргументов.

        Возвращает:
        Нет возвращаемого значения.
        """
        self.assertEqual(clean_text('python, but not java'), 'python but not java', msg='Something is not OK')

    def test_4(self):
        """
        Проверяет, что функция удаляет буквы, не являющиеся буквами латинского алфавита,
        из строки, оставляя только буквы латинского алфавита и пробелы.

        Аргументы:
        Нет аргументов.

        Возвращает:
        Нет возвращаемого значения.
        """
        self.assertEqual(clean_text('python - это не питон'), 'python    ', msg='Something is not OK')

    def test_5(self):
        """
        Проверяет, что функция комбинирует все предыдущие сценарии,
        удаляя знаки пунктуации и буквы не из латинского алфавита,
        и возвращает результат в нижнем регистре.

        Аргументы:
        Нет аргументов.

        Возвращает:
        Нет возвращаемого значения.
        """
        self.assertEqual(clean_text('"Python" - это не "Питон"'), 'python    ', msg='Something is not OK')

if __name__ == '__main__':
    unittest.main(verbosity=2)