import os
import sys
from collections import namedtuple
import logging

# Настройка логирования
logging.basicConfig(filename="directory_contents.log", level=logging.INFO, format='%(message)s')

# Определение namedtuple для хранения информации о файлах и каталогах
Info = namedtuple('FileInfo', 'type name extension parent_directory')

def show_directory(directory):
    """Функция для анализа содержимого директории и логирования информации."""
    if not os.path.isdir(directory):
        print(f"Указанный путь {directory} не является директорией.")
        return
    
    for root, dirs, files in os.walk(directory):
        parent_directory = os.path.basename(root)
        if parent_directory == '':
            parent_directory = os.path.basename(directory)  # Для корневой директории

        for name in files:
            file_info = Info(
                type='file',
                name=os.path.splitext(name)[0],
                extension=os.path.splitext(name)[1],
                parent_directory=parent_directory
            )
            logging.info(file_info)
        
        for name in dirs:
            dir_info = Info(
                type='dir',
                name=name,
                extension='',
                parent_directory=parent_directory
            )
            logging.info(dir_info)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python lesson_gb_2.py [путь до директории]")
    else:
        directory_path = sys.argv[1]
        show_directory(directory_path)