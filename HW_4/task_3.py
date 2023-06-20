''' Задание №3
Функция получает на вход строку из двух чисел через пробел.
Сформируйте словарь, где ключом будет
символ из Unicode, а значением —  целое число.
Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
'''


def create_unicode_dict(input_str):
    # Разбиваем строку на два числа
    num1, num2 = map(int, input_str.split())

    # Определяем диапазон чисел
    start = min(num1, num2)
    end = max(num1, num2)

    # Словарь с символами Unicode и целыми числами
    unicode_dict = {}

    # Создаем пары ключ-значение в заданном диапазоне
    for num in range(start, end + 1):
        char = chr(num)  # Получаем символ Unicode
        unicode_dict[char] = num

    return unicode_dict


input_str = input("Введите два числа через пробел: ")
result_dict = create_unicode_dict(input_str)
print(result_dict)
