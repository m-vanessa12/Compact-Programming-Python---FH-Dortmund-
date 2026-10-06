import numpy as np

matrix1 = np.random.random((5, 3))
matrix2 = np.random.random((3, 2))

result = np.dot(matrix1, matrix2)

print("First matrix (5x3): ")
print(matrix1)

print("Second matrix (3x2):")
print(matrix2)

print("Matrix multiplication result: ")
print(result)