''' Задание №8
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None.
Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
'''
import inspect

def replace_variables():
    frame = inspect.currentframe().f_back
    variables = [name for name, value in frame.f_locals.items(
    ) if name.endswith('s') and len(name) > 1]
    for name in variables:
        value = frame.f_locals[name]
        frame.f_locals[name] = None
        frame.f_locals[name[:-1]] = value


# Создаем переменные
names = 'Aleksey'
ages = [25, 30, 35]
city = 'Moscow'
scores = 9.5
s = True

# Выводим значения переменных до замены
print(f"Изначальные переменные - {names}, {ages}, {city}, {scores}, {s}")

# Вызываем функцию для замены переменных
replace_variables()

# Выводим значения переменных после замены
print(f"Измененные переменные - {names}, {ages}, {city}, {scores}, {s}")

# Переменная без 's' на конце
print(f"Новые переменные - {name}, {age}, {score}, {s}")
