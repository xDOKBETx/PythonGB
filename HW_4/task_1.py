''' Задание №1
Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
Строки нумеруются начиная с единицы.
Слова выводятся отсортированными согласно кодировки Unicode.
Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
'''


def print_sorted_words(text):
    # Разбиваем и сортируем текст в одной строке
    words = sorted(text.split())

    # Находим длину самого длинного слова
    max_word_length = max(map(len, words))
    # Получаем общее количество слов
    num_words = len(words)

    for i, word in enumerate(words, start=1):
        # Преобразуем номер строки в строку и выравниваем по длине самого длинного номера
        line_number = str(i).rjust(len(str(num_words)))
        line = f"{line_number} {word.rjust(max_word_length)}"
        print(line)


text = input('Введите текст: ')
print_sorted_words(text)
