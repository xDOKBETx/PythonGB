'''Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов. 
'''


def find_duplicates(lst):
    duplicates = []
    counts = {}
    
    for item in lst:
        if item in counts:
            counts[item] += 1
            if counts[item] == 2:
                duplicates.append(item)
        else:
            counts[item] = 1
    
    return list(set(duplicates))

# Пример использования
lst = [1, 2, 2, 3, 4, 4, 5, 6, 7]
result = find_duplicates(lst)
print(result)
