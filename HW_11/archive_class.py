''' Задание №2
Создайте класс Архив, который хранит пару свойств. Например, число и строку.
При создании нового экземпляра класса, старые данные из ранее созданных экземпляров 
сохраняются в пару списков-архивов list-архивы также являются свойствами экземпляра
'''


class Archive:
    """
    Класс Archive хранит пару свойств (число и строку).
    При создании нового экземпляра класса, сохраняются старые данные из ранее созданных экземпляров
    в пару списков-архивов. Списки-архивы также являются свойствами экземпляра.
    """
    numbers_archive = []
    strings_archive = []

    def __init__(self, number, string):
        """
        Инициализирует экземпляр класса Archive.

        Args:
            number (int): Числовое значение.
            string (str): Строковое значение.
        """
        self.number = number
        self.string = string

        # Добавляем текущие данные в списки-архивы экземпляра
        self.numbers_archive = Archive.numbers_archive.copy()
        self.strings_archive = Archive.strings_archive.copy()

        # Добавляем текущие данные в глобальные списки-архивы
        Archive.numbers_archive.append(number)
        Archive.strings_archive.append(string)

    def get_numbers_archive(self):
        """
        Возвращает список всех числовых значений из архива экземпляра.

        Returns:
            list: Список всех числовых значений из архива экземпляра.
        """
        return self.numbers_archive

    def get_strings_archive(self):
        """
        Возвращает список всех строковых значений из архива экземпляра.

        Returns:
            list: Список всех строковых значений из архива экземпляра.
        """
        return self.strings_archive

    def __repr__(self):
        """
        Метод представления экземпляра класса для программиста.
        Возвращает строку, содержащую информацию о числе и строке.

        Returns:
            str: Строка представления экземпляра класса для программиста.
        """
        return f"Archive(number={self.number}, string='{self.string}')"

    def __str__(self):
        """
        Метод представления экземпляра класса для пользователя.
        Возвращает строку, содержащую только значение строки.

        Returns:
            str: Строка представления экземпляра класса для пользователя.
        """
        return self.string


a1 = Archive(1, 'Один')
print(a1.get_numbers_archive())  # Выводит: []
print(a1.get_strings_archive())  # Выводит: []
print(repr(a1))  # Выводит: Archive(number=1, string='Один')
print(str(a1))  # Выводит: Один

a2 = Archive(2, 'Два')
print(a2.get_numbers_archive())  # Выводит: [1]
print(a2.get_strings_archive())  # Выводит: ['Один']
print(repr(a2))  # Выводит: Archive(number=2, string='Два')
print(str(a2))  # Выводит: Два
