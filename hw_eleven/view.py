def task_matrix():
    print('Создайте класс Матрица.\n'
          'Добавьте методы для:\n'
          '1) вывода на печать,\n'
          '2) сравнения,\n'
          '3) сложения,\n'
          '4) умножения матриц (транспонирование)')


def matrix_size_error():
    return 'Incorrect matrix size'

def is_matrix_error():
    return 'Object is not a matrix'

def different_sizes_addition_error():
    return 'Cannot add matrices of different sizes'

def non_matrix_addition_error(data):
    return 'Unsupported operand type for +: Matrix and {}'.format(type(data))
