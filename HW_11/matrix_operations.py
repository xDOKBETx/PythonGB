'''
Создайте класс Матрица. Добавьте методы для: 
вывода на печать, сравнения, сложения, умножения матриц
'''


class Matrix:
    """
    Класс Matrix представляет матрицу и содержит методы для работы с матрицами.

    Attributes:
        rows (int): Количество строк в матрице.
        columns (int): Количество столбцов в матрице.
        data (list): Двумерный список, представляющий значения элементов матрицы.

    Methods:
        print_matrix(): Выводит матрицу на печать.
        __eq__(other): Переопределение оператора равенства для матриц.
        __add__(other): Переопределение оператора сложения для матриц.
        __mul__(other): Переопределение оператора умножения для матриц.
    """

    def __init__(self, rows, columns):
        """
        Инициализирует объект Matrix.

        Args:
            rows (int): Количество строк в матрице.
            columns (int): Количество столбцов в матрице.
        """
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def print_matrix(self):
        """
        Выводит матрицу на печать.
        """
        for row in self.data:
            print(row)

    def __eq__(self, other):
        """
        Переопределяет оператор равенства для матриц.

        Args:
            other (Matrix): Другая матрица.

        Returns:
            bool: True, если матрицы равны, иначе False.
        """
        return self.data == other.data

    def __add__(self, other):
        """
        Переопределяет оператор сложения для матриц.

        Args:
            other (Matrix): Другая матрица.

        Returns:
            Matrix: Новая матрица, являющаяся результатом сложения двух матриц.
        """
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Размеры матриц не совпадают.")

        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result

    def __mul__(self, other):
        """
        Переопределяет оператор умножения для матриц.

        Args:
            other (Matrix): Другая матрица.

        Returns:
            Matrix: Новая матрица, являющаяся результатом умножения двух матриц.
        """
        if self.columns != other.rows:
            raise ValueError(
                "Количество столбцов текущей матрицы не совпадает с количеством строк другой матрицы.")

        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                _sum = 0
                for k in range(self.columns):
                    _sum += self.data[i][k] * other.data[k][j]
                result.data[i][j] = _sum

        return result


# Создание матрицы
matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [3, 4]]

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 6], [7, 8]]

# Вывод матриц на печать
print("Матрица 1:")
matrix1.print_matrix()

print("Матрица 2:")
matrix2.print_matrix()

# Сравнение матриц
print("Матрица 1 равна матрице 2?", matrix1 == matrix2)

# Сложение матриц
sum_matrix = matrix1 + matrix2
print("Сумма матриц:")
sum_matrix.print_matrix()

# Умножение матриц
matrix3 = Matrix(2, 2)
matrix3.data = [[1, 2], [3, 4]]

matrix4 = Matrix(2, 2)
matrix4.data = [[5, 6], [7, 8]]

multiplied_matrix = matrix3 * matrix4
print("Умножение матриц:")
multiplied_matrix.print_matrix()
