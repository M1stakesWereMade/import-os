import os
import time

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            last_modified = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(file_path)))
            
            file_size = os.path.getsize(file_path)
            
            parent_dir = os.path.dirname(file_path)
            
            print(f"Файл: {file_path}")
            print(f"Последнее изменение: {last_modified}")
            print(f"Размер файла: {file_size} байт")
            print(f"Родительская директория: {parent_dir}")
            print("---")

directory = r"F:\HAVOK\img"

process_directory(directory)