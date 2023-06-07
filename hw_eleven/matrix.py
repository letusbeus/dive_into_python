import view


class Matrix:
    def __init__(self, matrix: list[list[int]], *args):
        if not self.is_matrix(matrix):
            raise TypeError(view.is_matrix_error())
        if not self.check_matrix_size(matrix):
            raise ValueError(view.matrix_size_error())
        self.matrix = matrix

    @staticmethod
    def is_matrix(matrix):
        """
        Метод проверяет, является ли передаваемый пользователем объект матрицей.
        """
        if not isinstance(matrix, list) or \
                not all(isinstance(row, list) for row in matrix) or \
                len(matrix[0]) == 1:
            return False
        for row in matrix:
            if not all(isinstance(element, (int, float)) for element in row):
                return False
        return True

    @staticmethod
    def check_matrix_size(matrix):
        """
        Метод проверяет матрицу на корректность размерности строк матрицы
        """
        for row in matrix:
            if len(row) != len(matrix[0]):
                return False
        return True

    @staticmethod
    def check_matrix_compatibility(matrix1, matrix2):
        if not isinstance(matrix2, Matrix):
            raise TypeError(view.non_matrix_addition_error(matrix2))
        if len(matrix1.matrix) != len(matrix2.matrix) or len(matrix1.matrix[0]) != len(matrix2.matrix[0]):
            raise ValueError(view.different_sizes_addition_error())

    def __getitem__(self, index):
        return self.matrix[index]

    def __str__(self) -> str:
        rows = []
        for row in self.matrix:
            row_str = ''.join(f'{elem:^3}' for elem in row)
            rows.append(row_str)
        return '\n'.join(rows)

    def __eq__(self, other):
        Matrix.check_matrix_compatibility(self, other)
        return self.matrix == other.matrix

    def __add__(self, other):
        Matrix.check_matrix_compatibility(self, other)
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def transpose(self):
        transposed = []
        for j in range(len(self.matrix[0])):
            row = []
            for i in range(len(self.matrix)):
                row.append(self.matrix[i][j])
            transposed.append(row)
        return Matrix(transposed)
