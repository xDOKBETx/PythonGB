''' Задание №2
Напишите функцию, которая принимает строку текста. 
Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированной по убыванию
'''


def get_sorted_unique_unicode(text):
    unique_unicode = list(set(ord(char) for char in text))
    unique_unicode.sort(reverse=True)
    return unique_unicode


text = input('Введите текст: ')
result = get_sorted_unique_unicode(text)
print(result)
