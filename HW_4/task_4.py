''' Задание №4
Функция получает на вход список чисел.
Отсортируйте список по убыванию суммы цифр числа
'''


def sort_by_digit_sum(numbers):
    def digit_sum(num):
        return sum(int(digit) for digit in str(num))

    numbers.sort(key=digit_sum, reverse=True)


my_list = [123, 45, 678, 90, 12]
sort_by_digit_sum(my_list)
print(my_list)
