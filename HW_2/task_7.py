''' Задание №7
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата.
'''


def to_hexadecimal(number):
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""

    if number == 0:
        return "0"

    while number > 0:
        remainder = number % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        number //= 16

    return hexadecimal


# Пример использования
number = int(input("Введите целое число: "))
hexadecimal = to_hexadecimal(number)
print(
    f"Шестнадцатеричное представление числа: {hexadecimal}")

# Проверка с использованием функции hex()
hex_check = hex(number)[2:].upper()
print(f"Проверка: {hexadecimal == hex_check}")
