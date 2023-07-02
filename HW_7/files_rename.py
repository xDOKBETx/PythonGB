'''
Напишите функцию группового переименования файлов. Она должна:
принимать в качестве аргумента желаемое конечное имя файлов. 
При переименовании в конце имени добавляется порядковый номер.
Принимать в качестве аргумента расширение исходного файла. 
Переименование должно работать только для этих файлов внутри каталога.
Принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
'''
import os


def rename_files(desired_name, source_extension, target_extension):
    '''
    Групповое переименование файлов в указанном каталоге.
    desired_name (str): Желаемое конечное имя файлов.
    source_extension (str): Расширение исходного файла.
    target_extension (str): Расширение конечного файла.
    '''
    directory = 'D:\\ONE DRIVE\\OneDrive\\Документы\\PythonGB\\HW_7\\Text'  # Путь к каталогу
    files = [file for file in os.listdir(
        directory) if file.endswith('.' + source_extension)]

    for index, old_file in enumerate(files, 1):
        new_file = f"{os.path.splitext(old_file)[0]}_{desired_name}_{index}.{target_extension}"
        os.rename(os.path.join(directory, old_file),
                  os.path.join(directory, new_file))


if __name__ == '__main__':
    desired_name = "new_name"
    source_extension = "bin"
    target_extension = "txt"

    rename_files(desired_name, source_extension, target_extension)
