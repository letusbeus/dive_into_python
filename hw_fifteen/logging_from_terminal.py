"""
Решить задачи, которые не успели решить на семинаре.
Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной
информации. Также реализуйте возможность запуска из
командной строки с передачей параметров.

Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

import logging
from sys import argv


def log_check_triangle_from_terminal():
    logging.basicConfig(
        filename='check_triangle.log',  # указываем путь к log-файлу, иначе он будет создан в папке запуска
        filemode='a',
        encoding='UTF-8',
        format='{asctime} {levelname:<6} Строка {lineno:3>}: {msg}',
        style='{',
        level=logging.INFO
    )

    return logging.getLogger(__name__)


def check_triangle(sides: tuple) -> str:
    for side in sides:
        if side >= sum(sides) - side:
            log_check_triangle_from_terminal().error(f'Треугольник со сторонами {sides} не может быть создан')
            return "Треугольник не существует."

    if len(set(sides)) == 1:
        log_check_triangle_from_terminal().info(f'Создали равносторонний треугольник со сторонами {sides}')
        return 'Треугольник равносторонний'
    elif len(set(sides)) == 3:
        log_check_triangle_from_terminal().info(f'Создали разносторонний треугольник со сторонами {sides}')
        return 'Треугольник разносторонний'
    elif len(set(sides)) == 2:
        log_check_triangle_from_terminal().info(f'Создали равнобедренный треугольник со сторонами {sides}')
        return 'Треугольник равнобедренный'


def main():
    if len(argv) != 4:
        print('Неверное количество аргументов. Введите стороны треугольника: a b c')
        log_check_triangle_from_terminal().info(f'Ошибка создания треугольника: необходимо указать значения 3 сторон')
        return

    try:
        a = int(argv[1])
        b = int(argv[2])
        c = int(argv[3])
    except ValueError:
        print('Некорректные значения сторон треугольника. Введите целочисленные значения.')
        log_check_triangle_from_terminal().info(f'Ошибка создания треугольника: значения сторон могут быть только целыми числами')
        return

    result = check_triangle((a, b, c))
    print(result)


if __name__ == '__main__':
    main()
