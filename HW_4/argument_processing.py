'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
'''


def process_arguments(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if hashable(key):
            result[value] = key
        else:
            result[str(value)] = key
    return result


def hashable(obj):
    return hash(obj)


arguments = {
    'name': 'Aleksey',
    'age': 43,
    'lucky number': None,
    'Pi': 3.14,
    'true': True
}

result = process_arguments(**arguments)
print(result)
