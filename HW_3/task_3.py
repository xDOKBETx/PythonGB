''' Задание №3
Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.
'''

my_tuple = (1, 'hello', 3.14, True, 'world', False, 42)

result_dict = {}
for item in my_tuple:
    item_type = type(item).__name__
    # result_dict.setdefault(item_type, []).append(item)
    result_dict[item_type] = result_dict.get(item_type, []) + [item]
print(result_dict)
