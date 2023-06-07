import os
import json
import csv


def directory_processing(directory):
    result = []

    # Рекурсивная функция для обхода директории
    def directory_processing_helper(path):
        # Получаем список всех файлов и директорий в текущей директории
        items = os.listdir(path)

        # Перебираем все элементы в текущей директории
        for item in items:
            item_path = os.path.join(path, item)
            item_type = 'File' if os.path.isfile(item_path) else 'Directory'
            item_size = os.path.getsize(item_path) if os.path.isfile(item_path) else get_directory_size(item_path)

            # Создаем словарь с информацией об элементе
            item_info = {
                'Name': item,
                'Type': item_type,
                'Size (byte)': item_size,
                'Parent directory': path
            }

            result.append(item_info)

            # Рекурсивно вызываем функцию traverse_helper для вложенных директорий
            if os.path.isdir(item_path):
                directory_processing_helper(item_path)

    # Вспомогательная функция для подсчета размера директории с учетом всех вложенных файлов и директорий
    def get_directory_size(dir_path):
        total_size = 0
        for path, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(path, file)
                total_size += os.path.getsize(file_path)
        return total_size

    # Вызываем вспомогательную функцию traverse_helper для обхода директории
    directory_processing_helper(directory)

    # Сохраняем результаты в файлы JSON и CSV
    json_path = 'result.json'
    csv_path = 'result.csv'

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, indent=4)

    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=result[0].keys())
        writer.writeheader()
        writer.writerows(result)

    print(f'Directory processing completed. Results are saved to files {json_path}, {csv_path}.')


if __name__ == '__main__':
    directory_path = 'D:\dive_into_python\hw_eight'  # Заменить на свой путь к директории
    directory_processing(directory_path)
