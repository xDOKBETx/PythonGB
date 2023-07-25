class Matrix:
    """
    Класс Matrix представляет матрицу и содержит методы для работы с матрицами.

    Атрибуты:
        rows (int): Количество строк в матрице.
        columns (int): Количество столбцов в матрице.
        data (list): Двумерный список, представляющий значения элементов матрицы.

    Методы:
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
