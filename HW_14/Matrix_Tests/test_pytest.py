import pytest
from matrix import Matrix


def test_equality():
    """
    Тест проверки равенства матриц.
    """
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 2], [3, 4]]

    matrix2 = Matrix(2, 2)
    matrix2.data = [[5, 6], [7, 8]]

    assert matrix1 == matrix1
    assert matrix1 != matrix2


def test_addition():
    """
    Тест сложения матриц.
    """
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 2], [3, 4]]

    matrix2 = Matrix(2, 2)
    matrix2.data = [[5, 6], [7, 8]]

    sum_matrix = matrix1 + matrix2
    expected_result = [[6, 8], [10, 12]]
    assert sum_matrix.data == expected_result


def test_multiplication():
    """
    Тест умножения матриц.
    """
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 2], [3, 4]]

    matrix2 = Matrix(2, 2)
    matrix2.data = [[5, 6], [7, 8]]

    multiplied_matrix = matrix1 * matrix2
    expected_result = [[19, 22], [43, 50]]
    assert multiplied_matrix.data == expected_result


if __name__ == "__main__":
    pytest.main()
