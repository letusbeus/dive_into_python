import math
import csv
from typing import Callable


def finding_the_roots_of_a_quadratic_equation(a: int, b: int, c: int) -> str:
    discr = b ** 2 - 4 * a * c
    match discr:
        case d if d > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            return f'{x1:.2f}, {x2:.2f}'
        case d if d == 0:
            x = -b / (2 * a)
            return f'{x:.2f}'
        case _:
            return 'Корней нет'


def deco_finding_the_roots_of_a_quadratic_equation(func: Callable) -> object:
    def wrapper(csv_file):
        results = []
        with open(csv_file, 'r', newline='') as csv_f:
            reader = csv.reader(csv_f)
            for row in reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                results.append((a, b, c, roots))
            return results
    return wrapper
