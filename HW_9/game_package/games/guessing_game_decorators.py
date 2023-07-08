'''
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
декораторами для сохранения параметров,
декоратором контроля значений и
декоратором для многократного запуска.
Выберите верный порядок декораторов.
'''

import json
import random


def repeat(count):
    """
    Декоратор для многократного запуска декорируемой функции.

    Args:
        count (int): Количество запусков функции.

    Returns:
        function: Декоратор.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(count):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator


def control(func):
    """
    Декоратор для контроля значений параметров функции.

    Args:
        func (function): Декорируемая функция.

    Returns:
        function: Декоратор.
    """
    def wrapper(number, num_of_attempts):
        if not 1 <= number <= 100:
            print(f"Параметр {number} не в диапазоне")
            number = random.randint(1, 100)
        if not 1 <= num_of_attempts <= 10:
            print(
                f"Параметр {num_of_attempts} не в диапазоне")
            num_of_attempts = random.randint(1, 10)
        return func(number, num_of_attempts)
    return wrapper


def save_json(func):
    """
    Декоратор для сохранения параметров и результата функции в JSON файл.

    Args:
        func (function): Декорируемая функция.

    Returns:
        function: Декоратор.
    """
    def wrapper(number, num_of_attempts):
        result = func(number, num_of_attempts)
        data = {
            "number": number,
            "num_of_attempts": num_of_attempts,
            "result": result
        }
        with open("game_results.json", "a") as file:
            json.dump(data, file)
            file.write("\n")
        return result
    return wrapper


@repeat(2)
@save_json
@control
def game(number, num_of_attempts):
    attempt = 0
    while attempt < num_of_attempts:
        attempt += 1
        user_number = int(
            input(f"Попытка номер {attempt}. Введите число: "))
        if user_number < number:
            print("Вы вводите меньше")
        elif user_number > number:
            print("Вы вводите больше")
        else:
            print(f"Вы отгадали с {attempt} попытки!")
            return True
    print(
        f"Вы использовали все {attempt} попыток и не отгадали число. Было загадано число {number}. Вы проиграли.")
    return False


if __name__ == "__main__":
    game(50, 5)
