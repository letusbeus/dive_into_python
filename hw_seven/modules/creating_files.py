from pathlib import Path
import os
from random import randint, choices, randbytes
from string import ascii_letters


def create_file(extension: str, min_rand_name_len: int = 6, max_rand_name_len: int = 30,
                min_size_bit: int = 256, max_size_bit: int = 4096, file_count: int = 2) -> None:
    for i in range(file_count):
        len_name = randint(min_rand_name_len, max_rand_name_len)
        file_name = ''.join(choices(ascii_letters, k=len_name)) + '.' + extension
        random_size = randint(min_size_bit, max_size_bit)
        with open(file_name, 'bw') as f:
            f.write(randbytes(random_size))


def create_files(data: dict) -> None:
    """
    Функция создает заданное пользователем количество файлов с указанным типом расширений
    """
    for key, val in data.items():
        create_file(key, file_count=val)


def create_files_in_current_dir(name_dir: str, user_dict: dict[str, int]):
    """
    Функция создает директорию с указанным именем name_dir на 1 уровень выше текущего местоположения и
    наполняет ее файлами с расширениями и в количестве, указанными пользователем в словаре my_dict
    """
    name = Path(Path.cwd() / name_dir)
    if not name.exists():
        name.mkdir()
    os.chdir(name)
    create_files(user_dict)
