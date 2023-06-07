from matrix import Matrix
import view

if __name__ == '__main__':
    view.task_matrix()
    # Создание матриц
    m = Matrix([[1, 2], [1, 2]])
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])
    matrix3 = Matrix([[1, 2], [3, 4], [5, 6]])

    # Вывод на печать
    print(matrix1)

    # Сравнение матриц
    print(matrix1 == matrix2)  # False
    print(matrix1 == Matrix([[1, 2, 3], [4, 5, 6]]))  # True

    # Сложение матриц
    matrix_sum = matrix1 + matrix2
    print(matrix_sum)
    print(Matrix([[1, 2, 3], [4, 5, 6]]) + 'qwe') #TypeError: Unsupported operand type for +: Matrix and <class 'list'>
    # print(m + matrix1) #ValueError: Cannot add matrices of different sizes

    # Умножение матриц (транспонирование)
    transposed_matrix = matrix3.transpose()
    print(transposed_matrix)
    # print(Matrix([[1, 2], [3, 4], ['qwe', 'qwe']]).transpose()) #TypeError: Object is not a matrix
