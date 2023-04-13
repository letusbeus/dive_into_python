import collections
import view


def print_most_common(given_str):
    view.task_two()
    text_dict = dict(collections.Counter(list(given_str.split(' '))).most_common(10))
    view.most_common()
    print_dict(text_dict)
    print()


def print_dict(given_dict):
    for key, value in given_dict.items():
        print("{0}: {1} ".format(key, value))
