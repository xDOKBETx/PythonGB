import unittest
from matrix import Matrix


class TestMatrix(unittest.TestCase):
    """
    Тесты для класса Matrix.
    """

    def setUp(self):
        self.matrix1 = Matrix(2, 2)
        self.matrix1.data = [[1, 2], [3, 4]]

        self.matrix2 = Matrix(2, 2)
        self.matrix2.data = [[5, 6], [7, 8]]

        self.matrix3 = Matrix(2, 2)
        self.matrix3.data = [[1, 2], [3, 4]]

        self.matrix4 = Matrix(2, 2)
        self.matrix4.data = [[5, 6], [7, 8]]

    def test_equality(self):
        self.assertFalse(self.matrix1 == self.matrix2)
        self.assertTrue(self.matrix1 == self.matrix3)

    def test_addition(self):
        sum_matrix = self.matrix1 + self.matrix2
        expected_result = [[6, 8], [10, 12]]
        self.assertEqual(sum_matrix.data, expected_result)

    def test_multiplication(self):
        multiplied_matrix = self.matrix3 * self.matrix4
        expected_result = [[19, 22], [43, 50]]
        self.assertEqual(multiplied_matrix.data, expected_result)


if __name__ == "__main__":
    unittest.main()
