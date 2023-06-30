''' Задание №7
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''
import os
from pathlib import Path

EXTENSION_CATEGORY = {
    'txt': 'Text',
    'bin': 'Text',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'mvk': 'Video',
    'avi': 'Video',
    'mp4': 'Video'
}


def categorize_files(directory):
    '''
    Сортировка файлов в категории по расширениям.
    directory (str): Путь к директории.
    '''
    path = Path(directory)

    for ext, category in EXTENSION_CATEGORY.items():
        category_path = path / category
        # Создаем категорию, если она не существует
        category_path.mkdir(exist_ok=True)

        for file in path.glob(f'*.{ext}'):
            target_file = category_path / file.name
            if not target_file.exists():
                file.replace(target_file)


if __name__ == '__main__':
    directory_path = 'D:\\ONE DRIVE\\OneDrive\\Документы\\PythonGB\\HW_7'
    categorize_files(directory_path)
