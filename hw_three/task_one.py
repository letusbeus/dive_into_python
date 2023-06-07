import collections
import view


def duplicate_list(orig_list):
    view.task_one()
    view.original_list()
    print(*orig_list, sep=', ')
    view.uniq_list()
    print(*list(set(orig_list)), sep=', ')
    view.duplicate_list()
    d_list = []
    for k, v in collections.Counter(orig_list).items():
        if v > 1:
            d_list.append(k)
    print(*sorted(d_list), sep=', ', end='\n\n')
