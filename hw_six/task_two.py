from modules import *

if __name__ == '__main__':
    task_three()
    pairs = [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)]
    print(pairs, intersection_check(pairs), sep='\n')
