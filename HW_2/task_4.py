'''Задание №4
Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
Диаметр не превышает 1000 у.е.
Точность вычислений должна составлять не менее 42 знаков после запятой.
'''
import decimal
import math

while True:
    diameter = int(input("Введите диаметр круга: "))
    if diameter <= 1000:
        decimal.getcontext().prec = 42

        # Вычисление площади круга
        square = decimal.Decimal(math.pi * diameter ** 2 / 4)

        # Вычисление длины окружности
        circumference = decimal.Decimal(math.pi * diameter)

        print(f"Площадь круга: {square}")
        print(f"Длина окружности: {circumference}")
        break
    else:
        print("Диаметр не должен превышать 1000")

