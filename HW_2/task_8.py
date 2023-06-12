''' Задание №8
Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем. 
Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.
'''

from fractions import Fraction

def add_fractions(fraction1, fraction2):
    # Разделение дробей на числитель и знаменатель
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))

    # Создание объектов Fraction из числителей и знаменателей
    frac1 = Fraction(numerator1, denominator1)
    frac2 = Fraction(numerator2, denominator2)

    # Сумма дробей
    sum_fraction = frac1 + frac2

    # Возвращение суммы в виде строки дроби
    return str(sum_fraction)

def multiply_fractions(fraction1, fraction2):
    # Разделение дробей на числитель и знаменатель
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))

    # Создание объектов Fraction из числителей и знаменателей
    frac1 = Fraction(numerator1, denominator1)
    frac2 = Fraction(numerator2, denominator2)

    # Произведение дробей
    product_fraction = frac1 * frac2

    # Возвращение произведения в виде строки дроби
    return str(product_fraction)

# Ввод двух дробей от пользователя
fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")

# Сложение дробей
sum_result = add_fractions(fraction1, fraction2)
print(f"Сумма дробей: {sum_result}")

# Умножение дробей
product_result = multiply_fractions(fraction1, fraction2)
print(f"Произведение дробей: {product_result}")

# Проверка с использованием модуля fractions
frac1 = Fraction(fraction1)
frac2 = Fraction(fraction2)
expected_sum = str(frac1 + frac2)
expected_product = str(frac1 * frac2)
print(f"Проверка с использованием fractions: Сумма - {sum_result == expected_sum}, Произведение - {product_result == expected_product}")
