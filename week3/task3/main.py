import numpy as np

matrix = np.random.random((5, 5))

print("Original matrix: ")
print(matrix)

normalized_matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())

print("Normalized matrix:")
print(normalized_matrix)