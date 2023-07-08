'''
Дорабатываем задачу. 
Превратите внешнюю функцию в декоратор. 
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10]. 
Если не входят, вызывать функцию со случайными числами из диапазонов.
'''

import random

def validate_range(func):
    """
    Декоратор, который проверяет и заменяет переданные значения диапазона чисел и количества попыток,
    если они не соответствуют условиям задачи.

    Args:
        func (function): Декорируемая функция.

    Returns:
        function: Обернутая функция.
    """
    def wrapper(number_range, attempts):
        min_num, max_num = number_range
        if not (1 <= min_num <= max_num <= 100):
            print("Некорректный диапазон чисел. Используются значения по умолчанию.")
            number_range = (1, 100)
        if not (1 <= attempts <= 10):
            print("Некорректное количество попыток. Используется значение по умолчанию.")
            attempts = 10
        return func(number_range, attempts)
    
    return wrapper


def create_guessing_game(number_range, attempts):
    """
    Функция-замыкание, которая создает игру "Угадай число".

    Args:
        number_range (tuple): Диапазон чисел для загадывания (min, max).
        attempts (int): Количество попыток для угадывания.

    Returns:
        function: Функция для игры "Угадай число".
    """
    def guessing_game():
        """
        Функция для игры "Угадай число".

        Просит пользователя угадать загаданное число в указанном диапазоне
        за указанное количество попыток.

        """
        number = random.randint(*number_range)
        print(f"Загадано число от {number_range[0]} до {number_range[1]}")
        for _ in range(attempts):
            guess = int(input("Введите число: "))
            if guess == number:
                print("Вы угадали!")
                return
            elif guess < number:
                print("Загаданное число больше")
            else:
                print("Загаданное число меньше")
        print("Попытки исчерпаны, вы проиграли!")

    return guessing_game


game = create_guessing_game((1, 100), 10)
game = validate_range(game)
game()
