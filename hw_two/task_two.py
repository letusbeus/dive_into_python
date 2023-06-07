import re
import fractions
import view


def fractions_action():
    view.task_two()
    view.task_two_welcome_message()
    first_fraction = check_fraction()
    second_fraction = check_fraction()
    first_num = list(first_fraction.split('/'))
    second_num = list(second_fraction.split('/'))
    a1 = int(first_num[0])
    b1 = int(first_num[1])
    a2 = int(second_num[0])
    b2 = int(second_num[1])
    sum_fraction(a1, b1, a2, b2)
    multiply_fractions(a1, b1, a2, b2)
    check_built_in(a1, b1, a2, b2)


def check_fraction():
    while True:
        x = input()
        if re.findall(r'^\d+?/\d+$', x):
            return x
        else:
            view.task_two_warning_message()


def sum_fraction(x1, y1, x2, y2):
    c = find_gcd(x1 * y2, x2 * y1)
    view.sum_message()
    print(f'{int((x1 * y2 + x2 * y1) / c)}/{int((y1 * y2) / c)}')


def multiply_fractions(x1, y1, x2, y2):
    x = x1 * x2
    y = y1 * y2
    c = find_gcd(x, y)
    view.multiply_message()
    print(f'{int(x / c)}/{int(y / c)}')


def find_gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return find_gcd(b, a % b)


def check_built_in(x1, y1, x2, y2):
    f_one = fractions.Fraction(x1, y1)
    f_two = fractions.Fraction(x2, y2)
    view.built_in_fractions()
    print('{} + {} = {}'.format(f_one, f_two, f_one + f_two))
    print('{} * {} = {}'.format(f_one, f_two, f_one * f_two))
