import doctest
from matrix import Matrix


def Matrix_test():
    """
    Тест для класса Matrix.

    >>> matrix1 = Matrix(2, 2)
    >>> matrix1.data = [[1, 2], [3, 4]]

    >>> matrix2 = Matrix(2, 2)
    >>> matrix2.data = [[5, 6], [7, 8]]

    >>> matrix1 == matrix2
    False

    >>> sum_matrix = matrix1 + matrix2
    >>> sum_matrix.print_matrix()
    [6, 8]
    [10, 12]

    >>> matrix3 = Matrix(2, 2)
    >>> matrix3.data = [[1, 2], [3, 4]]

    >>> matrix4 = Matrix(2, 2)
    >>> matrix4.data = [[5, 6], [7, 8]]

    >>> multiplied_matrix = matrix3 * matrix4
    >>> multiplied_matrix.print_matrix()
    [19, 22]
    [43, 50]
    """

    doctest.testmod()


if __name__ == "__main__":
    Matrix_test()
