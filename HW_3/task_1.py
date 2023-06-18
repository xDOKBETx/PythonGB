'''Задание №1
Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
'''

import random

# Генерация списка с рандомными числами
numbers = [random.randint(1, 10) for _ in range(20)]  # Генерируем 20 чисел в диапазоне от 1 до 10

print("Исходный список:")
print(numbers)

# Короткое решение с использованием множества (set)
unique_numbers_short = list(set(numbers))

print("\nУникальные элементы (короткое решение):")
print(unique_numbers_short)

# Длинное решение без использования других коллекций помимо списков
unique_numbers_long = []

for number in numbers:
    if number not in unique_numbers_long:
        unique_numbers_long.append(number)

print("\nУникальные элементы (длинное решение):")
print(unique_numbers_long)
