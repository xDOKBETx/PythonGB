import sys
import random

__all__ = ["guess_number"]


def guess_number(lower_bound, upper_bound, num_attempts):
    """
    Функция для угадывания случайного числа.

    Аргументы:
    lower_bound (int): Нижняя граница диапазона.
    upper_bound (int): Верхняя граница диапазона.
    num_attempts (int): Количество попыток.

    Возвращает:
    bool: True, если число угадано, False в противном случае.
    """
    secret_number = random.randint(lower_bound, upper_bound)

    for attempt in range(num_attempts):
        guess = int(
            input(f"Всего попыток {num_attempts}. Попытка {attempt + 1}. Введите число {lower_bound} до {upper_bound}: "))

        if guess == secret_number:
            print("Поздравляю, вы угадали число!")
            return True
        elif guess < secret_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

    print(
        f"К сожалению, попытки исчерпаны. Загаданное число было {secret_number}.")
    return False


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1 or len(args) > 3:
        print("Неверное количество аргументов. Пожалуйста, укажите от 1 до 3 аргументов.")
        sys.exit(1)

    try:
        arguments = [int(arg) for arg in args]
    except ValueError:
        print("Аргументы должны быть целыми числами.")
        sys.exit(1)

    guess_number(*arguments)
