import os
from pathlib import Path


def sort_files_by_ext(way: Path) -> None:
    video = ['avi', 'mp4', 'mkv', 'mov', 'wmv']
    image = ['bmp', 'gif', 'jpg', 'jpeg', 'png', 'webp']
    text = ['txt', 'doc', 'pdf', 'csv', 'md']
    audio = ['mp3', 'wav', 'ac3', 'ogg']
    for dir_path, dir_names, file_names in os.walk(way):
        for file_name in file_names:
            file_path = Path(dir_path) / file_name
            file_extension = file_path.suffix[1:]  # Извлекаем расширение файла без точки
            if file_extension in video:
                target_directory = way / 'video'
            elif file_extension in image:
                target_directory = way / 'image'
            elif file_extension in text:
                target_directory = way / 'text'
            elif file_extension in audio:
                target_directory = way / 'audio'
            else:
                continue
            target_directory.mkdir(exist_ok=True)
            new_file_path = target_directory / file_path.name
            file_path.replace(new_file_path)
