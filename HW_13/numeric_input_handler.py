""" Задание №1
Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число
Обрабатывайте нечисловые данные как исключения.
"""


def get_numeric_input():
    """
    Функция запрашивает у пользователя числовые данные до тех пор, пока не будет введено целое или действительное число.
    Нечисловые данные обрабатываются как исключения.

    Возвращает:
        int или float: Если введено целое число, то возвращается значение типа int.
                       Если введено действительное число, то возвращается значение типа float.
    """
    while True:
        user_input = input("Пожалуйста, введите числовое значение: ")
        try:
            numeric_value = float(
                user_input
            )  # Преобразовать введенное значение в число с плавающей точкой
            if numeric_value.is_integer():  # Проверить, является ли число целым
                return int(numeric_value)  # Вернуть число как int, если оно целое
            else:
                return numeric_value  # Вернуть число как float, если оно действительное
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите числовое значение.")


if __name__ == "__main__":
    numeric_data = get_numeric_input()
    print("Вы ввели:", numeric_data)
