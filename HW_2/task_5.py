'''Задание №5 
Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
Используйте комплексные числа для извлечения квадратного корня.
'''

import math

# Ввод коэффициентов квадратного уравнения
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Вычисление дискриминанта
discriminant = b**2 - 4*a*c

# Решение уравнения в зависимости от значения дискриминанта
if discriminant >= 0:
    # Действительные корни
    root1 = (-b + math.pow(discriminant, 0.5)) / (2*a)
    root2 = (-b - math.pow(discriminant, 0.5)) / (2*a)
    print("Дискриминант:", discriminant)
    print("Корни уравнения:", root1, root2)
else:
    # Комплексные корни
    real_part = -b / (2*a)
    imaginary_part = math.pow(-discriminant, 0.5) / (2*a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print("Дискриминант:", discriminant)
    print("Корни уравнения:", root1, root2)
