# Копия на примере матрицы
import copy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = matrix.copy()
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = copy.deepcopy(matrix) # Дипкопи обходит и создает новую такую же коллекцию занимающая новое место в оперативной памяти.
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')