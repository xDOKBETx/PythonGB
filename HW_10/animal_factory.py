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
    def __init__(self, animal_type, name, specific):
        self.animal_type = animal_type
        self.name = name
        self.specific = specific

    def create_animal(self):
        """
        Создает экземпляр животного на основе переданного типа и возвращает его.
        :return: Экземпляр животного.
        :raises: ValueError, если передан недопустимый тип животного.
        """
        if self.animal_type == "Fish":
            return Fish(self.name, self.specific)
        elif self.animal_type == "Bird":
            return Bird(self.name, self.specific)
        elif self.animal_type == "Human":
            return Human(self.name, self.specific)
        else:
            raise ValueError("Недопустимый тип животного")


if __name__ == '__main__':
    animal_factory = AnimalFactory("Fish", 'Карась', 1)
    fish = animal_factory.create_animal()
    print(fish.get_specific(1))

    animal_factory = AnimalFactory("Bird", 'Орёл', 1)
    bird = animal_factory.create_animal()
    print(bird.get_specific(1))

    animal_factory = AnimalFactory("Human", 'Алкоголик', 1)
    human = animal_factory.create_animal()
    print(human.get_specific(1))
