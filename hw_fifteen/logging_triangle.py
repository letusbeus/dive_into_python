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


def log_check_triangle():
    logging.basicConfig(
        filename=r'D:\dive_into_python\hw_fifteen\check_triangle.log',
        filemode='a',
        encoding='UTF-8',
        format='{asctime} {levelname:<6} Строка {lineno:3>} : {msg}',
        style='{',
        level=logging.INFO
    )

    return logging.getLogger(__name__)


def check_triangle(sides: tuple) -> str:
    for side in sides:
        if side >= sum(sides) - side:
            log_check_triangle().error(f'Пытались создать непонятное, оно не выжило')
            return "Треугольник не существует."

    if len(set(sides)) == 1:
        log_check_triangle().info(f'Создали равносторонний треугольник со сторонами {sides}')
        return 'Треугольник равносторонний'
    elif len(set(sides)) == 3:
        log_check_triangle().info(f'Создали разносторонний треугольник со сторонами {sides}')
        return 'Треугольник разносторонний'
    elif len(set(sides)) == 2:
        log_check_triangle().info(f'Создали равнобедренный треугольник со сторонами {sides}')
        return 'Треугольник равнобедренный'


if __name__ == '__main__':
    check_triangle((3, 4, 3))
    check_triangle((3, 4, 5))
    check_triangle((3, 4, 0))
