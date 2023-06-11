''' Задание №7
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата.
'''


def to_hexadecimal(number):
    # Словарь для преобразования остатка в шестнадцатеричный символ
    hexadecimal_dict = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }

    if number == 0:
        return '0'

    hexadecimal = ''
    while number > 0:
        # Получение остатка от деления на 16
        remainder = number % 16
        # Добавление соответствующего шестнадцатеричного символа в начало строки
        hexadecimal = hexadecimal_dict[remainder] + hexadecimal
        # Деление числа на 16 для получения следующего разряда
        number //= 16

    return hexadecimal


# Пример использования
number = int(input("Введите целое число: "))
hexadecimal = to_hexadecimal(number)
print(
    f"Шестнадцатеричное представление числа: {hexadecimal}")

# Проверка с использованием функции hex
hexadecimal_hex = hex(number).lstrip('0x').upper()
print(f"Проверка: {hexadecimal == hexadecimal_hex}")
