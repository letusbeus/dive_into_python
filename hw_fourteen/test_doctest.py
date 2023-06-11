"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

def check_triangle(a, b, c):
    """
    Проверяет существование треугольника и определяет его тип на основе длин сторон.

    Args:
        a (float): Длина первой стороны треугольника.
        b (float): Длина второй стороны треугольника.
        c (float): Длина третьей стороны треугольника.

    Returns:
        str: Результат проверки существования и типа треугольника.

    Examples:
        >>> check_triangle(5, 7, 5)
        'Равнобедренный треугольник'

        >>> check_triangle(5, 7, 9)
        'Разносторонний треугольник'

        >>> check_triangle(5, 5, 5)
        'Равносторонний треугольник'

        >>> check_triangle(0, 1, 2)
        'Треугольник не существует'
    """
    sides = (a, b, c)  # Создаем множество из сторон треугольника

    # Проверка условия существования треугольника
    for side in sides:
        if side >= sum(sides) - side:
            return 'Треугольник не существует'
    # Проверка типа треугольника
    if len(set(sides)) == 1:
        return 'Равносторонний треугольник'
    elif len(set(sides)) == 2:
        return 'Равнобедренный треугольник'
    else:
        return 'Разносторонний треугольник'


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
