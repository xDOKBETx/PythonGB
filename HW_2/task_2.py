'''Задание №2
Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите: ✔	порядковый номер начиная с единицы
значение
адрес в памяти
размер в памяти
хэш объекта
результат проверки на целое число только если он положительный
результат проверки на строку только если он положительный   
Добавьте в список повторяющиеся элементы и сравните на результаты.
'''

import sys

# Создание списка с разными типами данных
data = [42, 3.14, "Hello", True, [1, 2, 3], {
    "a": 1, "b": 2}, (4, 5, 6), 42, "World", 42, "Hello"]

# Перебор элементов списка
for index, item in enumerate(data, start=1):
    # Вывод информации о каждом элементе
    print("Порядковый номер:", index)
    print("Значение:", item)
    print("Адрес в памяти:", id(item))
    print("Размер в памяти:", sys.getsizeof(item))

    try:
        print("Хэш объекта:", hash(item))
    except TypeError:
        print("Хэш объекта: Невозможно вычислить (TypeError)")

    if isinstance(item, int) and item > 0:
        print(
            "Проверка на целое положительное число: True")

    if isinstance(item, str):
        print("Проверка на строку: True")

    print()  # Пустая строка для разделения вывода элементов
