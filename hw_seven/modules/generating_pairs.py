from random import randint, uniform, choice


def generate_number_pairs(count_lines: int, filename: str) -> None:
    """
    Функция получает на вход целое положительное число count_lines и строковое значение filename,
    генерирует пары чисел в количестве count_lines, разделенные символом "|" и записывает их в файл filename.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        for i in range(count_lines):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            f.write(f'{int_num:>5} | {float_num:.3f}\n')


VOWELS = 'аеиоуяюёэы'
CONSONANTS = ''.join([chr(ch) for ch in range(ord('а'), ord('я') + 1) if chr(ch) not in VOWELS])


def generate_aliases(num_names: int, filename: str) -> None:
    """
    Функция получает на вход целое положительное число num_names и строковое значение filename,
    генерирует псевдоимена в количестве num_names и записывает их в файл filename.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        for _ in range(num_names):
            name_length = randint(4, 7)  # Случайная длина имени от 4 до 7
            name = choice(CONSONANTS + VOWELS).upper()  # Случайная заглавная согласная буква в начале имени
            while len(name) < name_length:
                if len(name) % 2 == 0:
                    name += choice(CONSONANTS)  # Добавление случайной согласной буквы
                else:
                    name += choice(VOWELS)  # Добавление случайной гласной буквы
            file.write(name + '\n')


def generate_name_number_pairs(pairs_file, aliases_file, name_number_pairs):
    """
    Функция комбинирует попарно значения из двух ранее созданных файлов aliases_file и pairs_file и
    записывает их в новый файл name_number_pairs.
    """
    with (open(pairs_file, 'r', encoding='utf-8') as r_file,
          open(aliases_file, 'r', encoding='utf-8') as a_file):
        numbers = r_file.readlines()
        names = a_file.readlines()

    lines_to_write = []
    length_of_longest = max(len(numbers), len(names))
    for i in range(length_of_longest):
        two_numbers = numbers[i % len(numbers)]
        a, b = map(float, two_numbers.split('|'))
        mult = a * b
        name = names[i % len(names)]
        if mult >= 0:
            lines_to_write.append(f'{name.upper().rstrip()}; {round(mult)}\n')
        else:
            lines_to_write.append(f'{name.lower().rstrip()}; {abs(mult)}\n')

    with open(name_number_pairs, 'w', encoding='utf=8') as f:
        f.writelines(lines_to_write)
