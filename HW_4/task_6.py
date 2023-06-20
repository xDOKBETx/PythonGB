''' Задание №6
Функция получает на вход список чисел и два индекса.
Вернуть сумму чисел между между переданными индексами.
Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
'''


def sum_between_indexes(numbers, index1, index2):
    start = min(index1, index2)  # Начальный индекс
    # Конечный индекс (включительно)
    end = max(index1, index2) + 1
    # Суммируем числа в заданном диапазоне
    sum_result = sum(numbers[start:end])
    return sum_result


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_between_indexes(my_list, 1, 3)
print(result)
