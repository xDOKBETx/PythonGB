from random import randint

__all__ = ["check_queens_solution", "generate_random_queens"]


def check_queens_solution(queens):
    """
    Проверяет, безопасно ли расположены ферзи на доске.

    Аргументы:
    queens (list): Список координат ферзей на доске.

    Возвращает:
    bool: True, если ферзи не бьют друг друга, иначе False.
    """
    for i, (x1, y1) in enumerate(queens):
        for x2, y2 in queens[i + 1:]:
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False
    return True


def generate_random_queens():
    """
    Генерирует случайные расстановки ферзей на доске.

    Возвращает:
    list: Список успешных расстановок ферзей.
    """
    successful_arrangements = []

    while len(successful_arrangements) < 4: # Изменил на вывод одной успешной расстановки. Устал ждать.
        queens = [(randint(1, 8), randint(1, 8)) for _ in range(8)]

        if check_queens_solution(queens):
            successful_arrangements.append(queens)

    return successful_arrangements
