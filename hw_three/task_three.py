import view
import random
from user_data import items, items_in_backpack


def filling_backpack():
    view.task_three()
    backpack = view.backpack_size_request()
    while True:
        for i in items:
            if backpack > 0 and (backpack - items[i]) >= 0:
                items_in_backpack[i] = items[i]
                backpack -= items[i]
                view.placed_item(i)
                view.free_space_left(backpack)
        break
    backpack_items(items_in_backpack)


def random_filling_backpack():
    backpack = view.backpack_size_request()
    view.filling_the_backpack()
    while True:
        for i in range(1, 40):
            random_item = random.sample(list(items.items()), 1)[0]
            if backpack > 0 and (backpack - random_item[1]) >= 0 and random_item[0] not in items_in_backpack:
                items_in_backpack[random_item[0]] = [random_item[1]]
                backpack -= random_item[1]
        break
    backpack_items(items_in_backpack)


def backpack_items(given_dict):
    view.backpack_contents()
    for enum, item in enumerate(given_dict, start=1):
        print(f'{enum}. {item}')


def all_varies():
    backpack = view.backpack_size_request()
    combinations = [[]]
    for item, weight in items.items():
        new_combinations = []
        for c in combinations:
            if sum([items[i] for i in c]) + weight <= backpack:
                new_combinations.append(c + [item])
        combinations.extend(new_combinations)

    valid_combinations = [c for c in combinations if sum([items[i] for i in c]) <= backpack]
    all_combinations(valid_combinations)


def all_combinations(given_list):
    view.print_all_combinations(given_list)
    for e, c in enumerate(given_list):
        if len(c) != 0:
            print(e, end='. ')
            print(*c, sep=', ')
