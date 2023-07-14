''' Задание №3
Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения возраста на год, 
full_name для вывода полного ФИО и т.п. на ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст
'''


class Person:
    def __init__(self, first_name, last_name, patronymic, age):
        """
        Конструктор класса Person.

        Args:
            first_name (str): Имя человека.
            last_name (str): Фамилия человека.
            patronymic (str): Отчество человека.
            age (int): Возраст человека.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self._age = age

    @property
    def age(self):
        """
        Свойство для доступа к возрасту человека.

        Returns:
            int: Возраст человека.
        """
        return self._age

    def birthday(self):
        """
        Метод для увеличения возраста на год.
        """
        self._age += 1

    def full_name(self):
        """
        Метод для получения полного имени человека.

        Returns:
            str: Полное имя человека.
        """
        return f"{self.last_name} {self.first_name} {self.patronymic}"


if __name__ == "__main__":
    
    # Создание экземпляра класса Person
    person = Person("Джон", "Уик", "Иванович", 30)

    # Вывод текущего возраста
    print("Текущий возраст:", person.age)

    # Увеличение возраста на год
    person.birthday()

    # Вывод нового возраста
    print("Новый возраст:", person.age)

    # Вывод полного имени
    print("Полное имя:", person.full_name())
