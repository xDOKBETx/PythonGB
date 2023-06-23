''' Задание №3
Продолжаем развивать задачу 2.
Возьмите словарь, который вы получили. Сохраните его итераторатор.
Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
'''
text = "Строка текста"
dictionary = {char: ord(char) for char in text}
iterator = iter(dictionary.items())
pairs = [next(iterator) for _ in range(5)]
print(pairs)
