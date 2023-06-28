def check_queens(queens):
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
