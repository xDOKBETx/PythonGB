''' Задание №7
Функция получает на вход словарь с названием компании в качестве ключа 
и списком с доходами и расходами (3-10 чисел) в качестве значения.
Вычислите итоговую прибыль или убыток каждой компании. 
Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
'''


def calculate_profit(dictionary):
    return all(sum(value for value in values if value > 0) >= abs(sum(value for value in values if value < 0))
               for values in dictionary.values())


companies = {
    "Company1": [1000, 3000, -1500, 800, -1200],
    "Company2": [2000, -500, 1500, -1000],
    "Company3": [500, 2000, 1000, -800],
}

result = calculate_profit(companies)
print(result)  # Вывод: True
