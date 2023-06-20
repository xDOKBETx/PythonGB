#  Напишите функцию для транспонирования матрицы 

def transpose_matrix(matrix):
    # Используем zip() для транспонирования матрицы
    transposed = list(zip(*matrix))
    
    # Возвращаем транспонированную матрицу
    return transposed


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

transposed_matrix = transpose_matrix(matrix)

# Выводим транспонированную матрицу
for row in transposed_matrix:
    print(row)
