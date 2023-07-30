import argparse
import datetime
import logging

# Конфигурация логирования
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', encoding='utf-8')

def convert_text_to_date(text, current_weekday=None, current_month=None):
    """
    Преобразует текст в формате "1st Thursday of November", "3rd Wednesday of May" и т.д. в дату текущего года.

    Args:
        text (str): Текст с описанием даты.
        current_weekday (str, optional): Текущий день недели. По умолчанию None.
        current_month (str, optional): Текущий месяц. По умолчанию None.

    Returns:
        datetime.date: Дата в формате год-месяц-день.

    Raises:
        ValueError: Если текст не соответствует заданному формату.
    """
    # Разбиваем текст на слова
    words = text.split()

    # Получаем информацию о числе и дне недели
    try:
        number = int(words[0][:-2])
        day_of_week = words[1]
    except (ValueError, IndexError):
        logging.error(f"Неправильный формат текста: {text}")
        raise ValueError("Неправильный формат текста")

    # Получаем информацию о месяце
    month = words[-1]

    # Получаем текущий год
    current_year = datetime.date.today().year

    # Создаем дату на основе полученных данных
    try:
        date_string = f"{current_year}-{month}-{number}"
        date = datetime.datetime.strptime(date_string, '%Y-%B-%d').date()

        # Проверяем, чтобы день недели совпадал
        if date.strftime('%A') != day_of_week:
            raise ValueError("Неправильный день недели")

        return date
    except ValueError:
        logging.error(f"Неправильный формат текста: {text}")
        raise ValueError("Неправильный формат текста")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Преобразует текст в формате "1st Thursday of November" в дату текущего года.')
    parser.add_argument('text', type=str, help='Текст с описанием даты')
    parser.add_argument('--current_weekday', type=str, default=None, help='Текущий день недели (по умолчанию - текущий день)')
    parser.add_argument('--current_month', type=str, default=None, help='Текущий месяц (по умолчанию - текущий месяц)')

    args = parser.parse_args()

    try:
        date = convert_text_to_date(args.text, args.current_weekday, args.current_month)
        print(date)
    except ValueError as e:
        print("Ошибка:", e)
