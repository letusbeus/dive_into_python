"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
Дано a, b, c - стороны предполагаемого треугольника. 
Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""


def triangle_check():
    a = int(input("Введите длину 1-й стороны треугольника: "))
    b = int(input("Введите длину 2-й стороны треугольника: "))
    c = int(input("Введите длину 3-й стороны треугольника: "))

    x = set(list([a, b, c]))

    if a + b < c or b + c < a or a + c < b:
        print("Треугольника с указанными сторонами не существует.")
    elif len(x) == 2:
        print("Треугольник с указанными сторонами является равнобедренным")
    elif len(x) == 1:
        print("Треугольник с указанными сторонами является равносторонним")
    else:
        print("Треугольник с указанными сторонами является разносторонним")
