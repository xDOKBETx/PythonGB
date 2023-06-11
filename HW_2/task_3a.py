'''Задание №3 
Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата, а не для решения. 
Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
Избегайте магических чисел
Добавьте аннотацию типов где это возможно
'''

def get_binary_octal_representation(number: int) -> tuple[str, str]:
    binary_representation = get_base_representation(number, 2)  # Получаем двоичное представление числа
    octal_representation = get_base_representation(number, 8)  # Получаем восьмеричное представление числа
    return binary_representation, octal_representation

def get_base_representation(number: int, base: int) -> str:
    if number == 0:
        return '0'  # Обработка случая, когда число равно 0
    elif number < 0:
        sign = '-'  # Устанавливаем знак минуса для отрицательного числа
        number = abs(number)  # Преобразуем отрицательное число в положительное
    else:
        sign = ''  # Пустой знак для положительного числа
    
    digits = []  # Список для хранения цифр числа

    while number > 0:
        remainder = number % base  # Остаток от деления на базу
        digits.append(str(remainder))  # Добавляем цифру в список
        number //= base  # Целочисленное деление на базу

    digits.reverse()  # Обратный порядок цифр

    representation = ''.join(digits)  # Соединяем цифры в строку

    return sign + representation

# Получаем целое число от пользователя
number = int(input("Введите целое число: "))

# Получаем двоичное и восьмеричное представления числа
binary, octal = get_binary_octal_representation(number)

# Выводим результаты
print("Двоичное представление числа:", binary)
print("Восьмеричное представление числа:", octal)
