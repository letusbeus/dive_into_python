import os
from pathlib import Path


def group_rename(dir_name: str, count_nums_name: int, old_file_ext: str, new_file_ext: str, name_range: list,
                 new_file_name: str = False) -> None:
    """
    Функция обращается к указанной папке и переименовывает находящиеся в ней файлы, удовлетворяющие условиям,
    в соответствии с заданными пользователем параметрами
    """
    for dir_path, dir_names, file_names in os.walk(dir_name):
        count_file_id = 1
        for file_name in file_names:
            if file_name.endswith('.' + old_file_ext):
                file_name_no_ext = Path(file_name).stem
                start = 0
                end = 0
                if name_range:
                    if len(file_name_no_ext) >= name_range[1]:
                        start = name_range[0]
                        end = name_range[1]
                    else:
                        start = name_range[0]
                        end = len(file_name_no_ext)
                file_id = str(count_file_id).zfill(count_nums_name)  # формируем порядковый номер для файла
                file_path = Path(dir_path) / file_name
                file_extension = file_path.suffix[1:]
                if file_extension == old_file_ext:
                    if new_file_ext:
                        if new_file_name:
                            name_to_change = f'{new_file_name}{file_id}.{new_file_ext}'
                        elif name_range:
                            name_to_change = f'{file_name_no_ext[start:end]}{file_id}.{new_file_ext}'
                        else:
                            name_to_change = f'{file_name_no_ext}{file_id}.{new_file_ext}'
                    else:
                        name_to_change = f'{file_name_no_ext}{file_id}.{file_extension}'
                else:
                    name_to_change = f'{file_name_no_ext}{file_id}.{file_extension}'
                file_path.rename(file_path.with_name(name_to_change))
                count_file_id += 1
            else:
                continue
