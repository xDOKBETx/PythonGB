''' Задание №1
Мы сформировали текстовый файл с псевдо именами и произведением чисел. 
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.  
Имена пишите с большой буквы. 
Каждую пару сохраняйте с новой строки.
'''

import json

def create_json_file(input_file, output_file):
    """
    Создает новый файл с данными в формате JSON из существующего файла с псевдо именами и произведением чисел.

    Args:
        input_file (str): Имя файла с псевдо именами и произведениями чисел.
        output_file (str): Имя файла для сохранения данных в формате JSON.
    """
    data = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            name, result = line.strip().split(' | ')
            data.append({'Имя': name.capitalize(), 'Произведение': int(result)})

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


create_json_file('HW_7/output.txt', 'HW_8/output.json')
