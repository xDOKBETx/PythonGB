import logging

def divide_numbers(a, b):
    """
    Функция для деления двух чисел.

    Args:
        a (float): Делимое число.
        b (float): Делитель.

    Returns:
        float: Результат деления a на b.

    Raises:
        ZeroDivisionError: Возникает, если делитель равен нулю.
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        logging.error("Ошибка: Деление на ноль")
        raise e

if __name__ == "__main__":
    # Настройка логирования для записи ошибок в файл с указанием кодировки 'utf-8'
    logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s: %(message)s', encoding='utf-8')

    try:
        numerator = 10
        denominator = 0
        result = divide_numbers(numerator, denominator)
        print(f"Результат {numerator}/{denominator} равен: {result}")
    except ZeroDivisionError as e:
        print("Ошибка: Невозможно делить на ноль.")
