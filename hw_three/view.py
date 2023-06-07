def task_one():
    print('1. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. '
          'В результирующем списке не должно быть дубликатов.')


def duplicate_list():
    print('Duplicate elements: ', end='')


def uniq_list():
    print('Unique elements: ', end='')


def original_list():
    print('Original list: ', end='')


def task_two():
    print('2. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. '
          'Не учитывать знаки препинания и регистр символов. '
          'За основу возьмите любую статью из википедии или из документации к языку.')


def most_common():
    print('10 most common words are: ')


def task_three():
    print('3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. '
          'Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. '
          'Достаточно вернуть один допустимый вариант. \n*Верните все возможные варианты комплектации рюкзака.')


def backpack_size_request():
    volume = int(input('\nEnter the size of your backpack: '))
    return volume


def placed_item(item):
    print(f'You put the following item in your backpack: {item}')


def free_space_left(weight):
    print(f'Free space left: {weight} kg')


def filling_the_backpack():
    from tqdm import tqdm
    from time import sleep
    for i in tqdm(range(100), ncols=80, ascii=True, desc='Filling your backpack: '):
        ...
        sleep(0.03)


def backpack_contents():
    print('Your backpack is full. Here\'s what you filled it with: ')


def print_all_combinations(given_list):
    print(f'There\'re {len(given_list)} options available for filling your backpack: ')
