''' Задание №5
Создайте вручную список с повторяющимися целыми числами.
Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
Нумерация начинается с единицы.
'''

my_list = [2, 3, 5, 2, 4, 6, 1, 7, 9, 5, 8, 3, 1, 7, 10]

# Создание списка с порядковыми номерами нечетных элементов
odd_indices = [i + 1 for i, num in enumerate(my_list) if num % 2 != 0]

print("Исходный список:")
print(my_list)

print("\nСписок с порядковыми номерами нечетных элементов:")
print(odd_indices)
