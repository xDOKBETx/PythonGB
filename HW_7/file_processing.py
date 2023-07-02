''' Задание №3
Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла, возвращайтесь в его начало.
'''

def multiply_numbers(names_file, numbers_file, output_file):
    """
    Умножает числа из файла на соответствующие их псевдонимы (имена) и сохраняет результаты в файл.

    Args:
        names_file (str): Имя файла с псевдонимами (именами).
        numbers_file (str): Имя файла с числами.
        output_file (str): Имя файла для сохранения результатов.

    """
    # Читаем имена из файла
    with open(names_file, 'r', encoding='utf-8') as f:
        names = f.read().splitlines()

    # Читаем числа из файла
    with open(numbers_file, 'r', encoding='utf-8') as f:
        numbers = f.read().splitlines()

    # Открываем файл для записи результатов
    with open(output_file, 'w', encoding='utf-8') as f:
        max_len = max(len(names), len(numbers))

        # Итерируемся по парам чисел и имен
        for i in range(max_len):
            name = names[i % len(names)]  # Обрабатываем случай достижения конца более короткого файла
            number_pair = numbers[i % len(numbers)].split(' | ')
            num1 = int(number_pair[0])
            num2 = float(number_pair[1])

            result = num1 * num2
            if result < 0:
                name = name.lower()
                result = abs(result)
            else:
                name = name.upper()
                result = round(result)

            f.write(f'{name} | {result}\n')


names_file = 'HW_7/names.txt'
numbers_file = 'HW_7/numbers.txt'
output_file = 'HW_7/output.txt'

multiply_numbers(names_file, numbers_file, output_file)
