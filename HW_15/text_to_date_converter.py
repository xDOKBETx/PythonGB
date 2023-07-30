import datetime
import logging

# Конфигурация логирования
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', encoding='utf-8')

def convert_text_to_date(text):
    """
    Преобразует текст в формате "1st Thursday of November", "3rd Wednesday of May" и т.д. в дату текущего года.

    Args:
        text (str): Текст с описанием даты.

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
    try:
        date1 = convert_text_to_date("1-й четверг Ноября")
        print(date1)

        date2 = convert_text_to_date("3-я среда Мая")
        print(date2)

        # Неправильный формат текста
        date3 = convert_text_to_date("Недопустимый текст")
        # Ошибки будут залогированы и исключение будет возбуждено

    except ValueError as e:
        print("Ошибка:", e)
