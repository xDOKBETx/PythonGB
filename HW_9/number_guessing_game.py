'''
Создайте функцию-замыкание, которая запрашивает два целых числа: 
от 1 до 100 для загадывания, 
от 1 до 10 для количества попыток
Функция возвращает функцию, 
которая через консоль просит угадать загаданное число за указанное число попыток.  
'''


import random


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
        print(
            f"Загадано число от {number_range[0]} до {number_range[1]}")
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
game()
