''' Задание №5
Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
'''

INVALID_SPECIFIC_VALUE_ERROR = "Недопустимое значение specific"

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
            raise ValueError(INVALID_SPECIFIC_VALUE_ERROR)


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
            raise ValueError(INVALID_SPECIFIC_VALUE_ERROR)


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
            raise ValueError(INVALID_SPECIFIC_VALUE_ERROR)


if __name__ == '__main__':
    fish = Fish('Карась', 1)
    print(fish.spec_op)

    bird = Bird('Орёл', 1)
    print(bird.spec_op)

    human = Human('Европеоид', 1)
    print(human.spec_op)
