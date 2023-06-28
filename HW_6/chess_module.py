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
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(
                    queens[i][1] - queens[j][1]):
                return False
    return True


def generate_random_queens():
    """
    Генерирует случайные расстановки ферзей на доске.

    Возвращает:
    list: Список успешных расстановок ферзей.
    """
    successful_arrangements = []

    while len(successful_arrangements) < 4:
        queens = [(i, randint(1, 8)) for i in range(1, 9)]

        if check_queens_solution(queens):
            successful_arrangements.append(queens)

    return successful_arrangements
