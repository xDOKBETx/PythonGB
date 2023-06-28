__all__ = ["is_valid_date"]


def is_leap_year(year):
    """
    Защищенная функция для проверки високосности года.

    Аргументы:
    year (int): Год.

    Возвращает:
    bool: True, если год високосный, иначе False.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_valid_date(date_str):
    """
    Функция для проверки валидности даты.

    Аргументы:
    date_str (str): Дата в формате DD.MM.YYYY.

    Возвращает:
    bool: True, если дата может существовать, иначе False.
    """
    day, month, year = map(int, date_str.split('.'))

    if not (1 <= day <= 31):
        return False

    if not (1 <= month <= 12):
        return False

    if not (1 <= year <= 9999):
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    if month == 2:
        if is_leap_year(year):
            return day <= 29
        else:
            return day <= 28

    return True


if __name__ == "__main__":
    date = input("Введите дату в формате DD.MM.YYYY: ")
    if is_valid_date(date):
        print("Дата может существовать")
    else:
        print("Такая дата невозможна")
