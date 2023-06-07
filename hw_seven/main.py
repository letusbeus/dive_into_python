import view
from modules import *

"""
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""

number_pairs = 'numbers'
aliases = 'aliases'
name_number_pairs = 'aliases_number_pairs'

# # Генерируем пары чисел в файл
# view.task_generate_number_pairs()
# generate_number_pairs(10, number_pairs)

# # Генерируем псевдоимена в файл
# view.task_generate_aliases()
# generate_aliases(12, aliases)

# Генерируем в файл пары псевдоимя-число из ранее полученных значений.
# Для работы функции необходимо предварительно выполнить функции generate_number_pairs и generate_aliases
view.task_generate_name_number_pairs()
generate_name_number_pairs(number_pairs, aliases, name_number_pairs)

my_dict = dict(txt=2, csv=1, doc=1, bin=2, pdf=2, exe=1, zip=1, jpg=2, avi=2, bmp=1, png=1, md=2)
dir_name = 'created_files'
dir_way = Path.cwd() / dir_name

# # Создаем директорию dir_name и в ней необходимое количество файлов.
# # Расширения и количество создаваемых файлов передаются из my_dict.
# view.task_create_file()
# create_files_in_current_dir(dir_name, my_dict)

# Функция принимает на вход параметры для переименования файлов в указанной директории dir_name
# Для работы функции необходимо предварительно создать директорию с файлами create_files_in_current_dir
view.task_group_rename()
group_rename(dir_name, 5, 'bin', 'new_bin', [1, 3], 'new_bin_name_')
group_rename(dir_name, 4, 'bmp', 'new_bmp', [1, 5], 'new_bmp_name_')
group_rename(dir_name, 3, 'avi', 'new_avi', [1, 4], 'new_avi_name_')
group_rename(dir_name, 7, 'pdf', 'new_pdf', [1, 7], 'new_pdf_name_')
group_rename(dir_name, 2, 'mp3', 'new_mp3', [1, 4], 'new_mp3_name_')
group_rename(dir_name, 4, 'txt', 'new_txt', [1, 4], 'new_txt_name_')

# # Функция сортирует файлы в указанной директории dir_way по поддиректориям в соответствии с типами файлов
# # Для работы функции необходимо предварительно создать директорию с файлами create_files_in_current_dir
# view.task_sort_files_by_ext()
# sort_files_by_ext(dir_way)
