"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

import unittest
from test_task import check_triangle


class TestTriangle(unittest.TestCase):

    def test_check_equilateral_triangle(self):
        self.assertEqual(check_triangle(5, 5, 5), 'Равносторонний треугольник')

    def test_check_isosceles_triangle(self):
        self.assertEqual(check_triangle(5, 7, 5), 'Равнобедренный треугольник')

    def test_check_scalene_triangle(self):
        self.assertEqual(check_triangle(5, 7, 9), 'Разносторонний треугольник')

    def test_check_is_triangle(self):
        self.assertEqual(check_triangle(3, 4, 0), 'Треугольник не существует')


if __name__ == '__main__':
    unittest.main(verbosity=2)
