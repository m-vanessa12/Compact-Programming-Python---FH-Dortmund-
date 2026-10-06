import numpy as np

matrix = np.random.random((5, 5))

print("Original matrix")
print(matrix)

row_means = matrix.mean(axis=1, keepdims=True)

result = matrix - row_means

print("Mean of each row")
print(row_means)

print("Matrix after substracting row means")
print(result)