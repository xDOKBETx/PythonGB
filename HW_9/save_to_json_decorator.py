'''
Напишите декоратор, который сохраняет в json файл 
параметры декорируемой функции и результат, который она возвращает. 
При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
'''

import os
import json

def save_as_json(filename):
    """
    Декоратор, сохраняющий параметры и результат декорируемой функции в JSON файл.

    Args:
        filename (str): Имя файла для сохранения.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Загрузка данных из файла, если файл существует
            data = []
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
            
            # Вызов декорируемой функции
            result = func(*args, **kwargs)
            
            # Сохранение параметров и результата в список
            data.append({'args': args, 'kwargs': kwargs, 'result': result})
            
            # Сохранение данных в JSON файл
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        
        return wrapper
    
    return decorator


@save_as_json('result.json')
def my_function(param1, param2):
    return param1 + param2

my_function(2, 2)
my_function(3, 4)
