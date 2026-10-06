import numpy as np 

array = np.array([
    [5, 2, 8],
    [1, 9, 3],
    [7, 4, 6],
    [2, 1, 5]
])

print("original array:")
print(array)

n = 1

sorted_array = array[array[:, n]. argsort()]

print("Array sorted by column", n)
print(sorted_array)