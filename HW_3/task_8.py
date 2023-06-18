''' Задание №8
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —кортеж вещей. Ответьте на вопросы:
Какие вещи взяли все три друга
Какие вещи уникальны, есть только у одного друга
Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
'''
# Инициализация словаря с вещами каждого друга
friends_tourists = {
    "Алексей": ("компас", "палатка", "посуда", "еда", "фонарик", "спальник", "верёвка"),
    "Дмитрий": ("топор", "посуда", "лопата", "вода", "спальник", "верёвка"),
    "Михаил": ("посуда", "удочка", "еда", "аптечка", "спальник", "вода"),
}

# Получение списка имен друзей
names = list(friends_tourists.keys())

# Поиск вещей, которые взяли все три друга
things_for_the_trip = set()
for name in names:
    things_for_the_trip.update(friends_tourists[name])

print(f"{' '.join(things_for_the_trip)} взяли друзья в поход")
print()

# Поиск уникальных вещей, которые есть только у одного друга
for name in names:
    unique_things = set(friends_tourists[name])
    for name_compare in names:
        if name == name_compare:
            continue
        unique_things.difference_update(friends_tourists[name_compare])

    print(f"{' '.join(unique_things)} есть только у {name}")
    print()

# Поиск вещей, которые есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
for name in names:
    other_names = names.copy()
    other_names.remove(name)
    things_for_the_trip = set(friends_tourists[other_names[0]])
    for other_name in other_names[1:]:
        things_for_the_trip.intersection_update(friends_tourists[other_name])

    things_for_the_trip.difference_update(friends_tourists[name])
    print(f"{' '.join(things_for_the_trip)} есть у всех кроме {name}")
    print()
