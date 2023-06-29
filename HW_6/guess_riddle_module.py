__all__ = ["guess_riddle", "store_results", "display_results"]

# Защищенный словарь уровня модуля для хранения результатов отгадывания
_guess_results = {}


def guess_riddle(riddle, options, num_attempts):
    """
    Функция для угадывания загадки.

    Аргументы:
    riddle (str): Загадка.
    options (list): Список возможных вариантов отгадок.
    num_attempts (int): Количество попыток.

    Возвращает:
    int: Номер попытки, с которой была отгадана загадка, или 0, если попытки исчерпаны.
    """
    print(f"У вас есть {num_attempts} попытки. Угадайте загадку: ")
    print(riddle)

    for attempt in range(1, num_attempts + 1):
        guess = input(f"Попытка {attempt}. Ваш ответ: ")

        if guess in options:
            print("Поздравляю, вы отгадали загадку!")
            return attempt

        print("Неправильный ответ. Попробуйте еще раз.")

    print("К сожалению, попытки исчерпаны. Загадка не отгадана.")
    return 0


def store_results(riddle, attempt):
    """
    Функция для формирования словаря с результатами отгадывания.

    Аргументы:
    riddle (str): Загадка.
    attempt (int): Номер попытки, с которой была отгадана загадка.

    Возвращает:
    None
    """
    _guess_results[riddle] = attempt


def display_results():
    """
    Функция для вывода результатов отгадывания в удобном для чтения виде.

    Возвращает:
    None
    """
    print("Результаты отгадывания:")
    results = [(riddle, "Отгадано" if attempt else "Не отгадано", attempt) for riddle, attempt in
               _guess_results.items()]
    for riddle, result, attempt in results:
        print(f"Загадка: {riddle}")
        print(f"Результат: {result}, попытка №{attempt}" if attempt else "Результат: Не отгадано")
        print()


def add_riddle_result(riddle, attempt):
    """
    Функция для добавления результата отгадывания в словарь.

    Аргументы:
    riddle (str): Загадка.
    attempt (int): Номер попытки, с которой была отгадана загадка.

    Возвращает:
    None
    """
    _guess_results[riddle] = attempt


# Загадки
riddles = {
    "Зимой и летом одним цветом!": ["ёлка", "Ёлка", "ель", "Ель"],
    "Ах, не трогайте меня. Обожгу и без огня!": ["крапива", "Крапива"],
    "Пустые отдыхаем, а полные шагаем.": ["сапоги", "Сапоги"]
}

for riddle, options in riddles.items():
    attempt = guess_riddle(riddle, options, 3)
    add_riddle_result(riddle, attempt)

display_results()
