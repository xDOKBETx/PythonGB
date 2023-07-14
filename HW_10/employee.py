''' Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
шестизначный идентификационный номер
уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
'''


import random
from person_info import Person


class Employee(Person):
    def __init__(self, first_name, last_name, patronymic, age):
        """
        Конструктор класса Employee.

        Args:
            first_name (str): Имя сотрудника.
            last_name (str): Фамилия сотрудника.
            patronymic (str): Отчество сотрудника.
            age (int): Возраст сотрудника.
        """
        super().__init__(first_name, last_name, patronymic, age)
        self.employee_id = random.randint(100000, 999999)

    def calculate_access_level(self):
        MAGIC_KEY = 7

        """
        Метод для вычисления уровня доступа сотрудника.

        Returns:
            int: Уровень доступа.
        """
        access_level = self.employee_id % MAGIC_KEY
        return access_level


# Создание экземпляра класса Employee
employee = Employee("Джон", "Уик", "Иванович", 30)

# Использование свойства age
employee.birthday()
age = employee.age
access_level = employee.calculate_access_level()

# Вывод результатов
print("Имя:", employee.first_name)
print("Фамилия:", employee.last_name)
print("Отчество:", employee.patronymic)
print("Возраст:", age)
print("Идентификационный номер:", employee.employee_id)
print("Уровень доступа:", access_level)
