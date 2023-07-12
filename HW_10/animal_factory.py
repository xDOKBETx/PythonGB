'''
Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики
'''


class Animal:
    def __init__(self, name):
        self.name = name


class Fish(Animal):
    prop = {1: 'Пресноводная', 2: 'Морская'}

    def __init__(self, name, specific):
        super().__init__(name)
        self.spec_op = self.get_specific(specific)

    def get_specific(self, specific):
        """
        Получает значение специфичной характеристики рыбы на основе переданного значения specific.
        :param specific: Значение специфичной характеристики (1 для 'Пресноводная', 2 для 'Морская').
        :return: Значение специфичной характеристики рыбы.
        :raises: ValueError, если передано недопустимое значение specific.
        """
        if specific in self.prop:
            return self.prop[specific]
        else:
            raise ValueError("Недопустимое значение specific")


class Bird(Animal):
    prop = {1: 'Летает', 2: 'Не летает'}

    def __init__(self, name, specific):
        super().__init__(name)
        self.spec_op = self.get_specific(specific)

    def get_specific(self, specific):
        """
        Получает значение специфичной характеристики птицы на основе переданного значения specific.
        :param specific: Значение специфичной характеристики (1 для 'Летает', 2 для 'Не летает').
        :return: Значение специфичной характеристики птицы.
        :raises: ValueError, если передано недопустимое значение specific.
        """
        if specific in self.prop:
            return self.prop[specific]
        else:
            raise ValueError("Недопустимое значение specific")


class Human(Animal):
    prop = {1: 'Курит', 2: 'Не курит'}

    def __init__(self, name, specific):
        super().__init__(name)
        self.spec_op = self.get_specific(specific)

    def get_specific(self, specific):
        """
        Получает значение специфичной характеристики человека на основе переданного значения specific.
        :param specific: Значение специфичной характеристики (1 для 'Курит', 2 для 'Не курит').
        :return: Значение специфичной характеристики человека.
        :raises: ValueError, если передано недопустимое значение specific.
        """
        if specific in self.prop:
            return self.prop[specific]
        else:
            raise ValueError("Недопустимое значение specific")


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, specific):
        """
        Создает экземпляр животного на основе переданного типа и возвращает его.
        :param animal_type: Тип животного ("Fish", "Bird" или "Human").
        :param name: Имя животного.
        :param specific: Значение специфичной характеристики для животного.
        :return: Экземпляр животного.
        :raises: ValueError, если передан недопустимый тип животного.
        """
        if animal_type == "Fish":
            return Fish(name, specific)
        elif animal_type == "Bird":
            return Bird(name, specific)
        elif animal_type == "Human":
            return Human(name, specific)
        else:
            raise ValueError("Недопустимый тип животного")


if __name__ == '__main__':
    animal_1 = AnimalFactory.create_animal("Fish", 'Карась', 1)
    print(animal_1.get_specific(1))

    animal_2 = AnimalFactory.create_animal("Bird", 'Орёл', 1)
    print(animal_2.get_specific(1))

    animal_3 = AnimalFactory.create_animal("Human", 'Алкоголик', 1)
    print(animal_3.get_specific(1))
