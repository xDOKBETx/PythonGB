from random import randint


def are_queens_safe(queens):
    """
    Проверяет, безопасно ли расположены ферзи на доске.

    Аргументы:
    queens (list): Список координат ферзей на доске.

    Возвращает:
    bool: True, если ферзи не бьют друг друга, иначе False.
    """
    for a, b in ((a, b) for a in queens for b in queens if a[0] < b[0]):
        if abs(a[0] - b[0]) == abs(a[1] - b[1]):
            return False
    return True


def generate_random_queens(num_queens=8, num_attempts=100):
    """
    Генерирует случайные расстановки ферзей на доске и возвращает успешные расстановки.

    Аргументы:
    num_queens (int): Количество ферзей.
    num_attempts (int): Количество попыток генерации случайных расстановок.

    Возвращает:
    list: Список успешных расстановок ферзей на доске.
    """
    successful_arrangements = []

    for _ in range(num_attempts):
        queens = [(i, randint(1, num_queens))
                  for i in range(1, num_queens + 1)]

        if are_queens_safe(queens):
            successful_arrangements.append(queens)

        if len(successful_arrangements) == 4:  # Остановиться после нахождения 4 успешных расстановок
            break

    return successful_arrangements
